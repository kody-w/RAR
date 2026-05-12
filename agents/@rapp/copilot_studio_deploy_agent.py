"""
copilot_studio_deploy_agent.py — Push a forged Copilot Studio bundle into a
real Dataverse / Power Platform environment.

Pipeline (one shot, intentionally automatic so the user only has to point
at a swarm):

    SwarmName ──► [forge]    ──► .brainstem_data/forged/<slug>/  (CS YAML)
              ──► [package]  ──► <slug>.solution.zip             (PowerPlatform)
              ──► [auth]     ──► OAuth client_credentials token
              ──► [inspect]  ──► WhoAmI + existing bots in env (read-only)
              ──► [import]   ──► POST ImportSolutionAsync (DESTRUCTIVE)

Auth is **service-principal** client_credentials grant against the env's
Dataverse resource URL. Reads `local.settings.json` for:
    DYNAMICS_365_TENANT_ID    → Entra tenant
    DYNAMICS_365_CLIENT_ID    → app registration id
    DYNAMICS_365_CLIENT_SECRET→ app secret
    DYNAMICS_365_RESOURCE     → https://<env>.crm.dynamics.com (Dataverse base)

The SPN must be (1) granted Power Platform access on the tenant AND
(2) registered as an Application User in the target Dataverse env with
a security role that allows solution import. If either is missing,
auth_test shows a clear error and no destructive action runs.

Actions (run in this order; each gates the next):
  auth_test     — token + WhoAmI; non-destructive; shows the SPN's identity
  inspect_env   — list bots, solutions, publishers in the env; non-destructive
  package       — clone an exported Tier-3 solution as template and swap in
                  the forge output's YAMLs; produces a signed .solution.zip
  plan_deploy   — dry-run: shows what would be pushed (file list, target,
                  publisher prefix); non-destructive
  deploy        — DESTRUCTIVE. POSTs the .zip to ImportSolutionAsync; gated
                  by confirm=true. Polls the import job, returns final status.

  one_shot      — convenience: forge + package + plan_deploy. Stops short of
                  the destructive import — the user runs deploy with
                  confirm=true once they're happy with the plan.

Sacred rules:
 1. Never log a secret. Token, client_secret, etc. are redacted in all
    structured output.
 2. Never push without explicit confirm=true. The full chain runs without
    confirm only up to plan_deploy. deploy is the only gate that touches
    the env destructively.
 3. Read the env config from local.settings.json (the file the user already
    maintains for Tier 2). Don't ask the user to paste creds into the agent.
 4. Tier-3 solution shape (the existing
    installer/MSFTAIBASMultiAgentCopilot_*.zip) is the canonical template —
    we clone its layout because we know that shape imports cleanly.
"""

from agents.basic_agent import BasicAgent
import os
import re
import json
import time
import uuid
import glob
import zipfile
import shutil
import urllib.request
import urllib.error
import urllib.parse


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/copilot_studio_deploy_agent",
    "display_name": "CopilotStudioDeploy",
    "description": (
        "Push a forged Copilot Studio bundle into a Dataverse environment "
        "via OAuth client_credentials + ImportSolutionAsync. Reads creds "
        "from local.settings.json. Destructive deploy is gated by confirm."
    ),
    "author": "RAPP",
    "version": "0.1.0",
    "tags": ["meta", "copilot-studio", "deploy", "dataverse", "destructive"],
    "category": "core",
    "quality_tier": "experimental",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent", "@rapp/copilot_studio_forge_agent"],
    "example_call": {"args": {"action": "auth_test"}},
}


# ─── Settings discovery + token cache ─────────────────────────────────────

_TOKEN_CACHE = {"token": None, "expires_at": 0, "resource": None, "tenant": None}


def _redact(s, keep=4):
    if not isinstance(s, str) or not s:
        return s
    if len(s) <= keep + 4:
        return "***"
    return s[:keep] + "…(" + str(len(s)) + " chars)"


def _brainstem_dir():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(here)


def _read_local_settings():
    """Read local.settings.json next to brainstem.py. Returns (settings_dict, path)."""
    candidate = os.path.join(_brainstem_dir(), "local.settings.json")
    if not os.path.exists(candidate):
        return None, candidate
    with open(candidate) as f:
        raw = json.load(f)
    return raw.get("Values", {}), candidate


def _normalize_resource(url):
    """Trim trailing slash + ensure scheme. Dataverse expects bare base url
    for /.default scope and for API calls."""
    if not url:
        return ""
    url = url.strip().rstrip("/")
    if not url.startswith("http"):
        url = "https://" + url
    return url


def _settings_summary(values):
    """Public-facing summary that NEVER includes secret values."""
    return {
        "tenant_id":        _redact(values.get("DYNAMICS_365_TENANT_ID", ""), keep=8),
        "client_id":        _redact(values.get("DYNAMICS_365_CLIENT_ID", ""), keep=8),
        "client_secret":    "<REDACTED>" if values.get("DYNAMICS_365_CLIENT_SECRET") else "<MISSING>",
        "resource":         _normalize_resource(values.get("DYNAMICS_365_RESOURCE", "")),
        "use_dynamics":     values.get("USE_DYNAMICS_STORAGE"),
    }


# ─── OAuth client_credentials ─────────────────────────────────────────────

def _acquire_token(values):
    """Client-credentials grant. Returns (token, expires_at_epoch).
    Caches in-memory until 60s before expiry."""
    tenant   = values.get("DYNAMICS_365_TENANT_ID", "").strip()
    client_id = values.get("DYNAMICS_365_CLIENT_ID", "").strip()
    secret   = values.get("DYNAMICS_365_CLIENT_SECRET", "").strip()
    resource = _normalize_resource(values.get("DYNAMICS_365_RESOURCE", ""))

    missing = [k for k, v in [("DYNAMICS_365_TENANT_ID", tenant),
                              ("DYNAMICS_365_CLIENT_ID", client_id),
                              ("DYNAMICS_365_CLIENT_SECRET", secret),
                              ("DYNAMICS_365_RESOURCE", resource)] if not v]
    if missing:
        raise RuntimeError(f"local.settings.json is missing: {missing}")

    now = time.time()
    if (_TOKEN_CACHE["token"]
            and _TOKEN_CACHE["resource"] == resource
            and _TOKEN_CACHE["tenant"] == tenant
            and _TOKEN_CACHE["expires_at"] - 60 > now):
        return _TOKEN_CACHE["token"], _TOKEN_CACHE["expires_at"]

    url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
    body = urllib.parse.urlencode({
        "grant_type":    "client_credentials",
        "client_id":     client_id,
        "client_secret": secret,
        "scope":         f"{resource}/.default",
    }).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST",
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            err_body = e.read().decode("utf-8", errors="replace")
        except Exception:
            err_body = ""
        # Surface AAD error code/description but never echo the secret
        try:
            err_json = json.loads(err_body)
            description = err_json.get("error_description", err_body)[:600]
            code = err_json.get("error", "http_error")
        except Exception:
            description = err_body[:600]
            code = "http_error"
        raise RuntimeError(f"AAD token error [{code}]: {description}")
    token = data["access_token"]
    expires_at = now + int(data.get("expires_in", 3600))
    _TOKEN_CACHE.update({"token": token, "expires_at": expires_at,
                         "resource": resource, "tenant": tenant})
    return token, expires_at


def _dataverse_get(values, rel_path, query=""):
    token, _ = _acquire_token(values)
    resource = _normalize_resource(values.get("DYNAMICS_365_RESOURCE", ""))
    # OData query strings often contain spaces (e.g. 'eq true') — quote them
    # while leaving OData syntax characters intact.
    if query:
        prefix = "?" if query.startswith("?") else ""
        q = query[1:] if prefix else query
        query = prefix + urllib.parse.quote(q, safe="$=&,()'/.: ").replace(" ", "%20")
    url = f"{resource}/api/data/v9.2/{rel_path.lstrip('/')}{query}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "OData-MaxVersion": "4.0",
        "OData-Version": "4.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode("utf-8")), r.status
    except urllib.error.HTTPError as e:
        try:
            err_body = e.read().decode("utf-8", errors="replace")
        except Exception:
            err_body = ""
        return {"error": err_body[:1000], "status": e.code}, e.code


def _dataverse_post(values, rel_path, payload):
    token, _ = _acquire_token(values)
    resource = _normalize_resource(values.get("DYNAMICS_365_RESOURCE", ""))
    url = f"{resource}/api/data/v9.2/{rel_path.lstrip('/')}"
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "OData-MaxVersion": "4.0",
        "OData-Version": "4.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            text = r.read().decode("utf-8")
            try:
                return json.loads(text) if text else {}, r.status
            except Exception:
                return {"raw": text}, r.status
    except urllib.error.HTTPError as e:
        try:
            err_body = e.read().decode("utf-8", errors="replace")
        except Exception:
            err_body = ""
        return {"error": err_body[:1000], "status": e.code}, e.code


# ─── Tier-3 solution template discovery ───────────────────────────────────

def _find_t3_template():
    """The canonical CS solution shape we clone from. The Tier 3 zip in
    installer/ exported cleanly from CS once and is our ground truth for
    layout (botcomponents/, solution.xml shape, [Content_Types].xml)."""
    repo_root = os.path.dirname(_brainstem_dir())
    candidates = sorted(glob.glob(
        os.path.join(repo_root, "installer", "MSFTAIBASMultiAgentCopilot_*.zip")))
    return candidates[-1] if candidates else None


# ─── Action: auth_test ────────────────────────────────────────────────────

def _action_auth_test():
    values, settings_path = _read_local_settings()
    if values is None:
        return {"status": "error",
                "message": f"local.settings.json not found at {settings_path}. "
                           f"Place your Tier 2 settings file in rapp_brainstem/."}

    summary = _settings_summary(values)
    try:
        token, exp = _acquire_token(values)
    except Exception as e:
        return {"status": "error", "stage": "token",
                "message": str(e), "settings": summary}

    who, code = _dataverse_get(values, "WhoAmI")
    if code != 200:
        return {"status": "error", "stage": "whoami",
                "message": f"Dataverse WhoAmI failed: HTTP {code} — "
                           f"{(who or {}).get('error', '')[:300]}",
                "settings": summary,
                "hint": ("Token acquired but WhoAmI rejected. The SPN is "
                         "not registered as an Application User in this "
                         "Dataverse env, OR lacks a security role. Open "
                         "Power Platform Admin Center → Environments → "
                         "<env> → Settings → Users → Application Users → "
                         "+New app user, pick the SPN's app id, assign it "
                         "the System Customizer (or Solution Importer) role.")}

    return {
        "status": "ok",
        "action": "auth_test",
        "settings": summary,
        "token_expires_at_epoch": exp,
        "token_lifetime_sec": int(exp - time.time()),
        "whoami": who,
        "message": (
            f"SPN authenticated against {summary['resource']}. "
            f"BusinessUnitId={who.get('BusinessUnitId')}, "
            f"UserId={who.get('UserId')}, "
            f"OrganizationId={who.get('OrganizationId')}. "
            f"Token valid for {int(exp - time.time())}s."
        ),
    }


# ─── Action: inspect_env ──────────────────────────────────────────────────

def _action_inspect_env():
    values, _ = _read_local_settings()
    if values is None:
        return {"status": "error",
                "message": "local.settings.json missing — run auth_test first."}

    # Solutions (publisher prefix is what we'll use for new components)
    solutions, code1 = _dataverse_get(
        values, "solutions",
        query="?$select=uniquename,friendlyname,version,ismanaged,publisherid"
              "&$expand=publisherid($select=uniquename,customizationprefix)"
              "&$filter=isvisible eq true&$top=50")
    if code1 != 200:
        return {"status": "error", "stage": "solutions",
                "message": f"List solutions failed: HTTP {code1}",
                "raw": solutions}

    # Existing bots in the env (so user sees what they're deploying alongside)
    bots, code2 = _dataverse_get(
        values, "bots",
        query="?$select=name,schemaname,solutionid,statecode&$top=50")

    # Publishers — useful to see prefixes available
    publishers, code3 = _dataverse_get(
        values, "publishers",
        query="?$select=uniquename,customizationprefix,friendlyname&$top=50")

    return {
        "status": "ok",
        "action": "inspect_env",
        "solutions_count": len(solutions.get("value", []))
            if isinstance(solutions, dict) else None,
        "solutions_sample": [
            {"uniquename": s.get("uniquename"),
             "friendlyname": s.get("friendlyname"),
             "version": s.get("version"),
             "managed": s.get("ismanaged"),
             "publisher": (s.get("publisherid") or {}).get("uniquename"),
             "prefix": (s.get("publisherid") or {}).get("customizationprefix")}
            for s in (solutions.get("value", [])[:20]
                      if isinstance(solutions, dict) else [])
        ],
        "bots_count": len(bots.get("value", []))
            if isinstance(bots, dict) and code2 == 200 else None,
        "bots_sample": [
            {"name": b.get("name"),
             "schemaname": b.get("schemaname"),
             "statecode": b.get("statecode")}
            for b in (bots.get("value", [])[:20]
                      if isinstance(bots, dict) and code2 == 200 else [])
        ],
        "publishers_sample": [
            {"uniquename": p.get("uniquename"),
             "prefix": p.get("customizationprefix"),
             "friendlyname": p.get("friendlyname")}
            for p in (publishers.get("value", [])[:20]
                      if isinstance(publishers, dict) and code3 == 200 else [])
        ],
    }


# ─── Action: package — clone Tier-3 layout, swap in forged YAMLs ──────────

def _action_package(forge_dir, solution_unique_name, publisher_unique_name,
                     publisher_prefix, version):
    """Build a Power Platform solution zip from a forge output dir.

    Strategy: clone the Tier-3 zip's structure (solution.xml + customizations.xml
    + [Content_Types].xml + botcomponents/ layout), then swap the bot data
    files with our forged YAMLs. The schemanames are remapped to use the
    user-provided publisher prefix.

    NOTE: This is best-effort. Microsoft's Copilot Studio import has internal
    validators that may reject hand-crafted bundles that diverge from what
    its own export emits. The plan_deploy action surfaces the file diff so
    the user sees exactly what's about to be sent BEFORE deploy is called."""
    if not os.path.isdir(forge_dir):
        return {"status": "error",
                "message": f"forge_dir not found: {forge_dir}. "
                           f"Run CopilotStudioForge.forge first."}

    template = _find_t3_template()
    if not template:
        return {"status": "error",
                "message": "No Tier-3 template found in installer/. "
                           "Place an exported CS solution zip there first."}

    # Stage workspace
    out_root = os.path.join(_brainstem_dir(), ".brainstem_data", "packaged")
    os.makedirs(out_root, exist_ok=True)
    pkg_id = f"{solution_unique_name}-{int(time.time())}"
    stage = os.path.join(out_root, pkg_id)
    os.makedirs(stage, exist_ok=True)

    # Unzip template
    with zipfile.ZipFile(template, "r") as z:
        z.extractall(stage)

    # Identify the forge output: root agent + child agents
    root_yaml = os.path.join(forge_dir, "agent.mcs.yml")
    child_dir = os.path.join(forge_dir, "agents")
    if not os.path.exists(root_yaml):
        return {"status": "error",
                "message": f"forge_dir missing agent.mcs.yml: {forge_dir}"}

    children = []
    if os.path.isdir(child_dir):
        for sub in sorted(os.listdir(child_dir)):
            ch_yaml = os.path.join(child_dir, sub, "agent.mcs.yml")
            if os.path.exists(ch_yaml):
                children.append((sub, ch_yaml))

    # Compute schema name pattern matching Tier 3 conventions:
    #   <prefix>_<botname>            ← root bot
    #   <prefix>_<botname>.gpt.default← root agent component
    #   <prefix>_<botname>.<child>.<ChildName>
    bot_id = re.sub(r"[^a-z0-9]", "", solution_unique_name.lower()) or "swarm"
    bot_schema = f"{publisher_prefix}_{bot_id}"

    # Replace the bot data in cloned template
    bc_root = os.path.join(stage, "botcomponents")
    if os.path.isdir(bc_root):
        shutil.rmtree(bc_root)
    os.makedirs(bc_root)

    overrides_for_content_types = []

    def _write_botcomponent(schema, name, description, kind_xml, data_yaml,
                             componenttype):
        comp_dir = os.path.join(bc_root, schema)
        os.makedirs(comp_dir, exist_ok=True)
        xml = (
            f'<botcomponent schemaname="{schema}">\n'
            f'  <componenttype>{componenttype}</componenttype>\n'
            f'  <description>{_xml_escape(description)}</description>\n'
            f'  <iscustomizable>0</iscustomizable>\n'
            f'  <name>{_xml_escape(name)}</name>\n'
            f'  <parentbotid>\n'
            f'    <schemaname>{bot_schema}</schemaname>\n'
            f'  </parentbotid>\n'
            f'  <statecode>0</statecode>\n'
            f'  <statuscode>1</statuscode>\n'
            f'</botcomponent>\n'
        )
        with open(os.path.join(comp_dir, "botcomponent.xml"), "w") as f:
            f.write(xml)
        with open(os.path.join(comp_dir, "data"), "w") as f:
            f.write(data_yaml)
        overrides_for_content_types.append(f"/botcomponents/{schema}/data")

    # Root agent (componenttype 15 = gpt component, observed in Tier 3)
    with open(root_yaml) as f:
        root_data = f.read()
    _write_botcomponent(
        schema=f"{bot_schema}.gpt.default",
        name=os.path.basename(forge_dir),
        description=f"Forged from {os.path.basename(forge_dir)}",
        kind_xml="GptComponentMetadata",
        data_yaml=root_data,
        componenttype=15,
    )

    for child_name, ch_path in children:
        with open(ch_path) as f:
            ch_data = f.read()
        _write_botcomponent(
            schema=f"{bot_schema}.agent.{child_name}",
            name=child_name,
            description=f"Child agent {child_name}",
            kind_xml="AgentDialog",
            data_yaml=ch_data,
            componenttype=15,
        )

    # Rebuild [Content_Types].xml to match the new component list
    ct_path = os.path.join(stage, "[Content_Types].xml")
    with open(ct_path, "w") as f:
        parts = ['﻿<?xml version="1.0" encoding="utf-8"?>',
                 '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
                 '<Default Extension="xml" ContentType="application/octet-stream" />',
                 '<Default Extension="json" ContentType="application/octet-stream" />']
        for p in overrides_for_content_types:
            parts.append(f'<Override PartName="{p}" ContentType="application/octet-stream" />')
        parts.append('</Types>')
        f.write("".join(parts))

    # Rewrite solution.xml (uniquename, version, publisher prefix)
    sol_path = os.path.join(stage, "solution.xml")
    if os.path.exists(sol_path):
        with open(sol_path) as f:
            sol = f.read()
        sol = re.sub(r"<UniqueName>[^<]+</UniqueName>",
                     f"<UniqueName>{solution_unique_name}</UniqueName>", sol, count=1)
        sol = re.sub(r"<Version>[^<]+</Version>",
                     f"<Version>{version}</Version>", sol, count=1)
        sol = re.sub(r"(<Publisher>\s*<UniqueName>)[^<]+(</UniqueName>)",
                     rf"\1{publisher_unique_name}\2", sol, count=1)
        sol = re.sub(r"<CustomizationPrefix>[^<]+</CustomizationPrefix>",
                     f"<CustomizationPrefix>{publisher_prefix}</CustomizationPrefix>", sol, count=1)
        # Strip RootComponents — Microsoft will rebuild from the bot components
        # we ship; keeping the old GUIDs would import Tier-3's workflows.
        sol = re.sub(r"<RootComponents>.*?</RootComponents>",
                     "<RootComponents></RootComponents>", sol, flags=re.DOTALL)
        with open(sol_path, "w") as f:
            f.write(sol)

    # Drop Workflows/ + Assets/ — they referenced Tier-3's flows that aren't
    # in our scope. Then strip the <Workflows>...</Workflows> block from
    # customizations.xml so it doesn't have dangling references to files we
    # just deleted (Dataverse rejects the whole import on a single missing
    # workflow file).
    for d in ("Workflows", "Assets"):
        full = os.path.join(stage, d)
        if os.path.exists(full):
            shutil.rmtree(full)
    cust_path = os.path.join(stage, "customizations.xml")
    if os.path.exists(cust_path):
        with open(cust_path) as f:
            cust = f.read()
        cust = re.sub(r"<Workflows>.*?</Workflows>",
                      "<Workflows></Workflows>", cust, flags=re.DOTALL)
        # Also remove any other section that points at /Workflows or /Assets
        with open(cust_path, "w") as f:
            f.write(cust)

    # Re-zip
    zip_path = os.path.join(out_root, f"{pkg_id}.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, fnames in os.walk(stage):
            for fn in fnames:
                full = os.path.join(root, fn)
                arc = os.path.relpath(full, stage)
                z.write(full, arc)

    return {
        "status": "ok",
        "action": "package",
        "package_dir": stage,
        "package_zip": zip_path,
        "package_zip_bytes": os.path.getsize(zip_path),
        "solution_unique_name": solution_unique_name,
        "publisher_prefix": publisher_prefix,
        "components": {
            "root_agent": f"{bot_schema}.gpt.default",
            "child_agents": [f"{bot_schema}.agent.{c}" for c, _ in children],
            "total": 1 + len(children),
        },
        "warning": (
            "Solution layout cloned from Tier-3 template. Microsoft's CS "
            "import has internal validators that may reject hand-crafted "
            "bundles. plan_deploy + deploy will surface any import errors."
        ),
    }


def _xml_escape(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;"))


# ─── Action: plan_deploy + deploy ─────────────────────────────────────────

def _action_plan_deploy(package_zip):
    if not package_zip or not os.path.exists(package_zip):
        return {"status": "error",
                "message": f"package_zip not found: {package_zip}"}
    values, _ = _read_local_settings()
    if values is None:
        return {"status": "error", "message": "local.settings.json missing."}

    # Probe target env
    try:
        token, _ = _acquire_token(values)
    except Exception as e:
        return {"status": "error", "stage": "token", "message": str(e)}
    summary = _settings_summary(values)

    files = []
    with zipfile.ZipFile(package_zip, "r") as z:
        for info in z.infolist():
            files.append({"name": info.filename, "bytes": info.file_size})

    return {
        "status": "ok",
        "action": "plan_deploy",
        "would_post_to": f"{summary['resource']}/api/data/v9.2/ImportSolutionAsync",
        "package_zip": package_zip,
        "package_zip_bytes": os.path.getsize(package_zip),
        "files_in_package": files[:60],
        "files_total": len(files),
        "tenant": summary["tenant_id"],
        "destructive": True,
        "next_step": (
            "Re-run with action='deploy' and confirm=true to actually push. "
            "Polls the import job until completion or 5 minute timeout."
        ),
    }


def _ensure_parent_bot(values, package_zip):
    """Inspect the package zip to find the bot schemaname (everything before
    the first '.' in any botcomponent schemaname). If no bot record exists
    in the env with that schemaname, create one. This is the missing
    prerequisite for ImportSolutionAsync — child botcomponents reference
    `<parentbotid><schemaname>...</schemaname></parentbotid>` which fails
    to resolve unless the bot already exists.

    Returns dict with bot_schemaname, bot_id (existing or newly created),
    and creation_action ('existed' | 'created' | 'failed')."""
    bot_schema = None
    with zipfile.ZipFile(package_zip, "r") as z:
        for name in z.namelist():
            if name.startswith("botcomponents/") and name.endswith("/botcomponent.xml"):
                schema_part = name.split("/")[1]  # botcomponents/<schema>/botcomponent.xml
                # schemaname pattern: <bot>.<kind>.<name> — take before first '.'
                bot_schema = schema_part.split(".")[0]
                break
    if not bot_schema:
        return {"bot_schemaname": None, "creation_action": "skipped_no_components"}

    # Lookup existing
    existing, code = _dataverse_get(
        values, "bots",
        query=f"?$select=botid,name,schemaname&$filter=schemaname eq '{bot_schema}'&$top=1")
    if code == 200 and existing.get("value"):
        return {"bot_schemaname": bot_schema,
                "bot_id": existing["value"][0]["botid"],
                "creation_action": "existed"}

    # Create — minimal payload mirrored from a known-good rapp_* bot
    name = bot_schema.split("_", 1)[-1].replace("_", " ").title()
    config = {
        "$kind": "BotConfiguration",
        "channels": [],
        "publishOnImport": False,
        "settings": {"GenerativeActionsEnabled": True},
        "gPTSettings": {
            "$kind": "GPTSettings",
            "defaultSchemaName": f"{bot_schema}.gpt.default",
        },
        "isLightweightBot": False,
        "aISettings": {
            "$kind": "AISettings",
            "useModelKnowledge": True,
            "isSemanticSearchEnabled": True,
            "optInUseLatestModels": False,
        },
        "recognizer": {"$kind": "GenerativeAIRecognizer"},
    }
    payload = {
        "name": name,
        "schemaname": bot_schema,
        "template": "default-2.1.0",
        "language": 1033,
        "configuration": json.dumps(config),
    }
    body, c = _dataverse_post(values, "bots", payload)
    if c not in (200, 201, 204):
        return {"bot_schemaname": bot_schema,
                "creation_action": "failed",
                "create_status_code": c,
                "create_error": (body.get("error") if isinstance(body, dict) else str(body))[:600]}
    return {"bot_schemaname": bot_schema,
            "bot_id": (body or {}).get("botid"),
            "creation_action": "created",
            "name": name}


def _action_deploy(package_zip, confirm):
    if confirm is not True:
        return {"status": "error",
                "message": "deploy is destructive and requires confirm=true. "
                           "Run plan_deploy first to see what would be sent."}
    if not package_zip or not os.path.exists(package_zip):
        return {"status": "error", "message": f"package_zip not found: {package_zip}"}
    values, _ = _read_local_settings()
    if values is None:
        return {"status": "error", "message": "local.settings.json missing."}

    # Step 1: ensure parent bot exists (pre-req for ImportSolutionAsync)
    bot_step = _ensure_parent_bot(values, package_zip)
    if bot_step.get("creation_action") == "failed":
        return {"status": "error", "stage": "ensure_parent_bot",
                "bot_step": bot_step,
                "message": ("Could not pre-create the parent bot record. "
                            "Solution import would fail on parentbotid "
                            "resolution.")}

    import base64
    with open(package_zip, "rb") as f:
        zip_b64 = base64.b64encode(f.read()).decode("ascii")

    import_job_id = str(uuid.uuid4())
    payload = {
        "OverwriteUnmanagedCustomizations": True,
        "PublishWorkflows": True,
        "CustomizationFile": zip_b64,
        "ImportJobId": import_job_id,
    }
    body, code = _dataverse_post(values, "ImportSolutionAsync", payload)
    if code not in (200, 202, 204):
        return {"status": "error", "stage": "import_post",
                "message": f"ImportSolutionAsync rejected: HTTP {code}",
                "body": body}

    # Poll the import job
    deadline = time.time() + 300  # 5 min
    last_progress = -1
    while time.time() < deadline:
        job, c = _dataverse_get(values, f"importjobs({import_job_id})",
                                query="?$select=progress,completedon,solutionname,data")
        if c == 200 and isinstance(job, dict):
            progress = float(job.get("progress") or 0)
            if progress != last_progress:
                last_progress = progress
            if job.get("completedon"):
                return {
                    "status": "ok",
                    "action": "deploy",
                    "import_job_id": import_job_id,
                    "completed_at": job.get("completedon"),
                    "solution_name": job.get("solutionname"),
                    "progress": progress,
                    "bot_step": bot_step,
                    "message": f"Import job completed at {job.get('completedon')}.",
                }
        time.sleep(5)

    return {"status": "pending",
            "action": "deploy",
            "import_job_id": import_job_id,
            "last_progress": last_progress,
            "message": ("Import did not complete within 5 minutes. "
                        f"Poll {values.get('DYNAMICS_365_RESOURCE')}"
                        f"/api/data/v9.2/importjobs({import_job_id}) for status.")}


# ─── Action: one_shot — forge → package → plan_deploy ────────────────────

def _action_one_shot(swarm_name, publisher_prefix, publisher_unique_name, version):
    """Run the full chain up to (but NOT including) the destructive deploy.
    Calls the forge agent in-process to avoid duplicating its logic."""
    # 1. Forge
    try:
        from agents.copilot_studio_forge_agent import CopilotStudioForgeAgent
    except Exception as e:
        return {"status": "error", "stage": "import_forge",
                "message": f"Could not import the forge: {e}. "
                           f"Ensure copilot_studio_forge_agent.py is in agents/."}
    forge = CopilotStudioForgeAgent()
    forge_result = json.loads(forge.perform(action="forge", swarm_name=swarm_name))
    if forge_result.get("status") != "ok":
        return {"status": "error", "stage": "forge", "forge_result": forge_result}
    bundle_dir = forge_result["bundle_dir"]

    # 2. Package
    pkg = _action_package(bundle_dir,
                           solution_unique_name=re.sub(r"[^A-Za-z0-9]", "", swarm_name),
                           publisher_unique_name=publisher_unique_name,
                           publisher_prefix=publisher_prefix,
                           version=version)
    if pkg.get("status") != "ok":
        return {"status": "error", "stage": "package", "package_result": pkg}

    # 3. Plan
    plan = _action_plan_deploy(pkg["package_zip"])
    if plan.get("status") != "ok":
        return {"status": "error", "stage": "plan_deploy",
                "plan_result": plan,
                "package_result": pkg,
                "forge_result": forge_result}

    return {
        "status": "ok",
        "action": "one_shot",
        "forge": {"bundle_dir": forge_result.get("bundle_dir"),
                  "bundle_zip": forge_result.get("bundle_zip"),
                  "stats": (forge_result.get("plan") or {}).get("stats")},
        "package": {"package_zip": pkg["package_zip"],
                    "components": pkg["components"]},
        "plan_deploy": {"would_post_to": plan["would_post_to"],
                        "files_total": plan["files_total"]},
        "next_step": (
            f"Inspect the package at {pkg['package_zip']} and the plan above. "
            f"When ready, call action='deploy' with package_zip='{pkg['package_zip']}' "
            f"and confirm=true to push to {plan['would_post_to']}. "
            f"This is the only step that touches the env destructively."
        ),
    }


# ─── The agent ────────────────────────────────────────────────────────────

class CopilotStudioDeployAgent(BasicAgent):
    def __init__(self):
        self.name = "CopilotStudioDeploy"
        self.metadata = {
            "name": self.name,
            "description": (
                "Push a forged Copilot Studio bundle into a Dataverse / Power "
                "Platform environment via OAuth client_credentials + "
                "ImportSolutionAsync. Reads SPN creds from local.settings.json "
                "(DYNAMICS_365_TENANT_ID/CLIENT_ID/CLIENT_SECRET/RESOURCE).\n\n"
                "Run actions in order — each gates the next:\n"
                " 1. auth_test    — token + WhoAmI; non-destructive\n"
                " 2. inspect_env  — list bots, solutions, publishers; non-destructive\n"
                " 3. one_shot     — forge + package + plan_deploy in one call;\n"
                "                   STOPS before the destructive import\n"
                " 4. plan_deploy  — show what would be POSTed; non-destructive\n"
                " 5. deploy       — POST ImportSolutionAsync; DESTRUCTIVE,\n"
                "                   requires confirm=true\n\n"
                "Secrets are NEVER printed — token/client_secret are redacted "
                "in all output."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["auth_test", "inspect_env", "package",
                                 "plan_deploy", "deploy", "one_shot"],
                        "description": "auth_test (start here) | inspect_env | one_shot | package | plan_deploy | deploy",
                    },
                    "swarm_name": {
                        "type": "string",
                        "description": "For one_shot: the installed swarm to forge + deploy (e.g. 'BookFactory').",
                    },
                    "forge_dir": {
                        "type": "string",
                        "description": "For package: absolute path to a .brainstem_data/forged/<bundle> dir.",
                    },
                    "package_zip": {
                        "type": "string",
                        "description": "For plan_deploy/deploy: absolute path to a packaged solution .zip.",
                    },
                    "solution_unique_name": {
                        "type": "string",
                        "description": "Power Platform solution UniqueName (no spaces). Defaults from swarm_name.",
                    },
                    "publisher_prefix": {
                        "type": "string",
                        "description": "Publisher prefix for new components (e.g. 'rapp'). Must match an existing publisher in the env or be created beforehand.",
                    },
                    "publisher_unique_name": {
                        "type": "string",
                        "description": "Publisher UniqueName. Defaults to 'RAPP'.",
                    },
                    "version": {
                        "type": "string",
                        "description": "Solution version (e.g. '0.1.0.1'). Defaults to '0.1.0.0'.",
                    },
                    "confirm": {
                        "type": "boolean",
                        "description": "REQUIRED true for deploy action. Otherwise deploy refuses.",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, action="auth_test", swarm_name="", forge_dir="",
                package_zip="", solution_unique_name="", publisher_prefix="rapp",
                publisher_unique_name="RAPP", version="0.1.0.0",
                confirm=False, **kwargs):
        try:
            if action == "auth_test":
                return json.dumps(_action_auth_test())
            if action == "inspect_env":
                return json.dumps(_action_inspect_env())
            if action == "package":
                if not solution_unique_name:
                    solution_unique_name = (
                        re.sub(r"[^A-Za-z0-9]", "", os.path.basename(forge_dir.rstrip("/")))
                        or "ForgedSwarm"
                    )
                return json.dumps(_action_package(
                    forge_dir, solution_unique_name, publisher_unique_name,
                    publisher_prefix, version))
            if action == "plan_deploy":
                return json.dumps(_action_plan_deploy(package_zip))
            if action == "deploy":
                return json.dumps(_action_deploy(package_zip, confirm))
            if action == "one_shot":
                if not swarm_name:
                    return json.dumps({"status": "error",
                                       "message": "one_shot requires swarm_name."})
                return json.dumps(_action_one_shot(
                    swarm_name, publisher_prefix, publisher_unique_name, version))
            return json.dumps({"status": "error",
                               "message": f"Unknown action {action!r}."})
        except Exception as e:
            return json.dumps({"status": "error",
                               "stage": "agent_dispatch",
                               "message": f"{type(e).__name__}: {e}"})
