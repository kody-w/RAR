---
name: "rar-kody-w-copilot-studio-deploy"
description: "Deploys Copilot Studio agents into Dataverse four ways: REST ImportSolutionAsync, the pac CLI pipeline, the quality-gated FACTORY chain, or the NEW-experience MCP shape (BlastBox two-solution: inline-MCP connector + new-generation connected agents, channel-less parents, publish-verified)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_deploy_agent", "rar_sha256": "837ba4ee8c900514f8e5951e1a230663ba5120a8cc7a62d549391e720b21a05f", "source_kind": "rar-agent", "source_commit": "94508cbb789c5f0b7a83423a7dbc4cc9fb949052", "version": "1.2.0", "author": "kody-w", "tags": ["copilot-studio", "deploy", "dataverse", "power-platform", "pac", "import-solution", "destructive", "assimilated", "factory", "quality-gate", "synthetic-data", "pipeline", "mcp", "new-shape", "blastbox", "connected-agents"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/copilot_studio_deploy_agent`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_deploy_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Copilot Studio Deploy (assimilated) — push forged CS bundles into Dataverse.

Consolidates copilot_studio_deploy (REST ImportSolutionAsync) and rapp2mcs_factory
(pac-CLI analyze->normalize->package->deploy) into one deploy surface. Each source
agent's real logic is embedded verbatim as an internal engine; a single dispatcher
routes by `engine`. Destructive imports are confirm-gated; creds come from
local.settings.json / environment, never hardcoded.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "rest: auth_test|inspect_env|package|plan_deploy|deploy|one_shot ; pac: scan|pipeline|analyze|normalize|package|deploy.",
      "type": "string"
    },
    "confirm": {
      "description": "Required true for the DESTRUCTIVE import/deploy step.",
      "type": "boolean"
    },
    "engine": {
      "description": "rest = REST ImportSolutionAsync (service principal); pac = pac-CLI end-to-end pipeline; factory = quality-gated agent.py -> RAPP pipeline chain (SYNTHETIC_DATA seeds, connector hygiene, verified deploy; modes check/scaffold); mcp = NEW Copilot Studio experience (BlastBox two-solution MCP shape: inline-MCP connector + new-generation cliagent parent/connected child, channel-less, publish-verified). actions generate|deploy|verify.",
      "enum": [
        "rest",
        "pac",
        "factory",
        "mcp",
        "help"
      ],
      "type": "string"
    },
    "environment": {
      "description": "pac engine: target Dataverse environment URL.",
      "type": "string"
    },
    "forge_dir": {
      "description": "rest engine: directory of forge output YAMLs to package.",
      "type": "string"
    },
    "input_path": {
      "description": "pac engine: brainstem agents/ dir or blueprint.",
      "type": "string"
    },
    "output_dir": {
      "description": "Where to write packaged solution artifacts.",
      "type": "string"
    },
    "package_zip": {
      "description": "rest engine: path to a prebuilt .solution.zip.",
      "type": "string"
    },
    "swarm_name": {
      "description": "Swarm/agent set to package + deploy.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_deploy_agent.py` and embedded as the fenced Python below (sha256 837ba4ee8c900514…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_deploy_agent.py` first:

```bash
python3 copilot_studio_deploy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_deploy_agent.py   # or on stdin
python3 copilot_studio_deploy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""Copilot Studio Deploy (assimilated) — push forged CS bundles into Dataverse.\n\nConsolidates copilot_studio_deploy (REST ImportSolutionAsync) and rapp2mcs_factory\n(pac-CLI analyze->normalize->package->deploy) into one deploy surface. Each source\nagent's real logic is embedded verbatim as an internal engine; a single dispatcher\nroutes by `engine`. Destructive imports are confirm-gated; creds come from\nlocal.settings.json / environment, never hardcoded."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/copilot_studio_deploy_agent",
    "version": "1.2.0",
    "display_name": "CopilotStudioDeploy",
    "description": "Deploys Copilot Studio agents into Dataverse four ways: REST ImportSolutionAsync, the pac CLI pipeline, the quality-gated FACTORY chain, or the NEW-experience MCP shape (BlastBox two-solution: inline-MCP connector + new-generation connected agents, channel-less parents, publish-verified).",
    "author": "kody-w",
    "tags": ["copilot-studio", "deploy", "dataverse", "power-platform", "pac", "import-solution", "destructive", "assimilated", "factory", "quality-gate", "synthetic-data", "pipeline", "mcp", "new-shape", "blastbox", "connected-agents"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

from pathlib import Path
import base64 as _b64
import glob
import importlib.util
import gzip as _gz
import io as _io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile as _tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
import zipfile
import zipfile as _zipfile

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # pragma: no cover
    try:
        from basic_agent import BasicAgent
    except ImportError:
        class BasicAgent:  # type: ignore
            def __init__(self, name=None, metadata=None):
                self.name = name
                self.metadata = metadata


class _EngineBase:
    """Plain shim so the embedded source-agent engines don't need BasicAgent.
    Each engine sets self.name/self.metadata in its own __init__; we just absorb
    the super().__init__(...) call without side effects."""
    def __init__(self, *args, **kwargs):
        if args:
            self.name = getattr(self, "name", args[0])


# ============================================================================
# Embedded engines — REAL logic ported verbatim from the source agents
# ============================================================================
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

def _find_t3_template():
    """The canonical CS solution shape we clone from. The Tier 3 zip in
    installer/ exported cleanly from CS once and is our ground truth for
    layout (botcomponents/, solution.xml shape, [Content_Types].xml)."""
    repo_root = os.path.dirname(_brainstem_dir())
    candidates = sorted(glob.glob(
        os.path.join(repo_root, "installer", "MSFTAIBASMultiAgentCopilot_*.zip")))
    return candidates[-1] if candidates else None

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

class _RestDeployEngine(_EngineBase):
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

    def run(self, action="auth_test", swarm_name="", forge_dir="",
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

def _find_repo_root():
    here = Path(__file__).resolve().parent
    for cand in (here, *here.parents):
        if (cand / "rapp_brainstem").is_dir():
            return cand
    return here

def _which_pac():
    """Resolve pac binary. On Windows it's pac.cmd; shutil.which honors
    PATHEXT and returns the full path."""
    return shutil.which("pac") or shutil.which("pac.cmd")

def _tail(s, n=1500):
    if not s:
        return ""
    return s if len(s) <= n else s[-n:]

def _run_subproc(cmd, *, timeout=900):
    """Wrap subprocess.run with Windows .cmd handling + uniform return shape."""
    if os.name == "nt" and cmd and isinstance(cmd[0], str) and cmd[0].lower().endswith(".cmd"):
        cmd = ["cmd.exe", "/c"] + cmd
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"returncode": -1, "stdout": "", "stderr": f"timeout after {timeout}s"}
    except FileNotFoundError as e:
        return {"returncode": -1, "stdout": "", "stderr": f"file not found: {e}"}
    return {"returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}

class _InternalAnalyze:
    """Run the AIBAST analyzer over a directory of *_agent.py files."""

    def perform(self, *, input_path, output_dir, ir_dir=None, mode="openai",
                api_key=None, pattern="*.py"):
        script = _aibast_script("analyzer", "analyzer_agent.py")
        if script is None:
            return {"status": "error", "phase": "analyze",
                    "message": "AIBAST analyzer_agent.py not found. "
                               "Place AIBAST_RAPP/ at repo root or set AIBAST_DIR."}
        input_path = Path(input_path)
        if not input_path.exists():
            return {"status": "error", "phase": "analyze",
                    "message": f"input_path does not exist: {input_path}"}
        out = Path(output_dir); out.mkdir(parents=True, exist_ok=True)
        ir = Path(ir_dir) if ir_dir else (out / "ir"); ir.mkdir(parents=True, exist_ok=True)

        if mode == "openai" and not api_key and not os.environ.get("OPENAI_API_KEY"):
            return {"status": "error", "phase": "analyze",
                    "message": "OPENAI_API_KEY not set. Set the env var, "
                               "pass api_key, or switch mode='azure' with AZURE_OPENAI_*."}

        cmd = [sys.executable, str(script), str(input_path),
               "--output", str(out),
               "--ir-dir", str(ir),
               "--mode", mode,
               "--pattern", pattern]
        if api_key:
            cmd.extend(["--api-key", api_key])

        r = _run_subproc(cmd, timeout=1800)
        produced = sorted(p.name for p in out.glob("*_analyzer_output.json"))
        if not produced:
            produced = [p.name for p in out.glob("*.json") if p.is_file()]
        ok = r["returncode"] == 0 and len(produced) > 0
        return {"status": "ok" if ok else "error",
                "phase": "analyze",
                "returncode": r["returncode"],
                "output_dir": str(out),
                "ir_dir": str(ir),
                "analyzer_outputs": produced,
                "count": len(produced),
                "stdout_tail": _tail(r["stdout"]),
                "stderr_tail": _tail(r["stderr"])}

class _InternalNormalize:
    """Run AIBAST normalizer, then post-process each blueprint so it
    conforms to: no Azure Functions, OOTB CDS connector only."""

    # Only this one native connector survives the policy filter.
    ALLOWED_NATIVE = {"shared_commondataserviceforapps"}

    def perform(self, *, input_path, output_dir, mode="openai",
                no_azure_function=True, ootb_dataverse_only=True):
        script = _aibast_script("normalizer", "normalizer_agent.py")
        if script is None:
            return {"status": "error", "phase": "normalize",
                    "message": "AIBAST normalizer_agent.py not found."}
        input_path = Path(input_path)
        if not input_path.exists():
            return {"status": "error", "phase": "normalize",
                    "message": f"input_path does not exist: {input_path}"}
        out = Path(output_dir); out.mkdir(parents=True, exist_ok=True)

        cmd = [sys.executable, str(script), str(input_path),
               "--output", str(out), "--mode", mode]
        r = _run_subproc(cmd, timeout=900)

        # Find blueprints in the AIBAST output. AIBAST may write into
        # nested subdirs; collect recursively to be safe.
        blueprints = sorted(out.rglob("*_blueprint.json"))
        if not blueprints:
            blueprints = sorted(p for p in out.rglob("*.json")
                                if p.is_file() and "blueprint" in p.name.lower())

        # Apply policy
        policy_actions = []
        if no_azure_function or ootb_dataverse_only:
            for bp in blueprints:
                policy_actions.extend(self._apply_policy(
                    bp, no_azure_function, ootb_dataverse_only))

        ok = r["returncode"] == 0 and len(blueprints) > 0
        return {"status": "ok" if ok else "error",
                "phase": "normalize",
                "returncode": r["returncode"],
                "output_dir": str(out),
                "blueprints": [str(p.relative_to(out)) for p in blueprints],
                "count": len(blueprints),
                "policy_actions": policy_actions,
                "policy": {"no_azure_function": no_azure_function,
                           "ootb_dataverse_only": ootb_dataverse_only},
                "stdout_tail": _tail(r["stdout"]),
                "stderr_tail": _tail(r["stderr"])}

    def _apply_policy(self, blueprint_path, no_azure_function, ootb_only):
        """Mutate the blueprint in-place to honor the factory's policy.

        Why this lives here, not in AIBAST: the AIBAST normalizer is a
        general-purpose connector resolver. The factory has a stricter
        contract ('OOTB Dataverse only, no Azure Functions') that's a
        product decision, not a normalizer decision. So we layer the
        constraint here without forking the normalizer."""
        try:
            data = json.loads(blueprint_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            return [{"blueprint": str(blueprint_path), "action": "read_error",
                     "detail": str(e)}]

        actions = []

        if no_azure_function and data.get("azure_function_needed") is True:
            data["azure_function_needed"] = False
            actions.append({"blueprint": blueprint_path.name,
                            "action": "force_azure_function_off"})

        if ootb_only:
            rct = data.get("resolved_connector_type")
            # Reject 'custom' — that path leads to Azure Function or
            # custom connectors. Downgrade to 'none' so the wrapper
            # generator emits a topic-only agent (still useful: the GPT
            # component instructions remain).
            if rct == "custom":
                data["resolved_connector_type"] = "none"
                actions.append({"blueprint": blueprint_path.name,
                                "action": "downgrade_custom_to_none"})
            # For 'native' connectors, only CDS survives. Drop other native
            # candidates so the wrapper doesn't wire them up.
            cands = data.get("resolved_native_connectors") or []
            filtered = [c for c in cands
                        if c.get("platform_api_id") in self.ALLOWED_NATIVE]
            if len(filtered) != len(cands):
                dropped = [c.get("platform_api_id") for c in cands
                           if c.get("platform_api_id") not in self.ALLOWED_NATIVE]
                data["resolved_native_connectors"] = filtered
                actions.append({"blueprint": blueprint_path.name,
                                "action": "filter_native_to_cds_only",
                                "dropped": dropped})
            # If we dropped all natives, also drop the type to 'none'
            if (data.get("resolved_connector_type") == "native"
                    and not data.get("resolved_native_connectors")):
                data["resolved_connector_type"] = "none"
                actions.append({"blueprint": blueprint_path.name,
                                "action": "no_natives_remain_downgrade_to_none"})

        # Mark the blueprint as policy-stamped for traceability
        data.setdefault("_factory_policy", {})
        data["_factory_policy"].update({
            "no_azure_function": no_azure_function,
            "ootb_dataverse_only": ootb_only,
            "stamped_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        })

        try:
            blueprint_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except OSError as e:
            actions.append({"blueprint": blueprint_path.name,
                            "action": "write_error", "detail": str(e)})
        return actions

class _InternalPackage:
    """Run AIBAST wrapper_generator over a directory of blueprints to
    produce one or more Power Platform solution .zip files."""

    def perform(self, *, input_path, output_dir, solution_version=None,
                publisher_prefix="rapp", publisher_name="RAPP",
                publisher_display="RAPP", managed=False, mode="openai"):
        script = _aibast_script("wrapper_generator", "wrapper_generator.py")
        if script is None:
            return {"status": "error", "phase": "package",
                    "message": "AIBAST wrapper_generator.py not found."}
        input_path = Path(input_path)
        if not input_path.exists():
            return {"status": "error", "phase": "package",
                    "message": f"input_path does not exist: {input_path}"}
        out = Path(output_dir); out.mkdir(parents=True, exist_ok=True)

        cmd = [sys.executable, str(script), str(input_path),
               "--output", str(out),
               "--publisher-prefix", publisher_prefix,
               "--publisher-name", publisher_name,
               "--publisher-display", publisher_display,
               "--mode", mode]
        if solution_version:
            cmd.extend(["--solution-version", solution_version])
        if managed:
            cmd.append("--managed")

        r = _run_subproc(cmd, timeout=900)
        zips = sorted(out.rglob("*.zip"))
        ok = r["returncode"] == 0 and len(zips) > 0
        return {"status": "ok" if ok else "error",
                "phase": "package",
                "returncode": r["returncode"],
                "output_dir": str(out),
                "zips": [str(z.relative_to(out)) for z in zips],
                "zip_count": len(zips),
                "stdout_tail": _tail(r["stdout"]),
                "stderr_tail": _tail(r["stderr"])}

class _InternalDeploy:
    """Import every .zip under `input_dir` (or a single zip_path) into the
    active pac auth profile's environment via `pac solution import`."""

    def perform(self, *, zip_path=None, input_dir=None, environment=None,
                force_overwrite=True, async_import=True, max_async_wait=15):
        pac = _which_pac()
        if not pac:
            return {"status": "error", "phase": "deploy",
                    "message": "pac CLI not found on PATH. Install: https://aka.ms/PowerPlatformCLI"}

        # Resolve the list of zips to import. Caller can pass a single
        # zip_path OR a directory; if neither, we error out.
        zips = []
        if zip_path:
            zips = [Path(zip_path)]
        elif input_dir:
            zips = sorted(Path(input_dir).rglob("*.zip"))
        if not zips:
            return {"status": "error", "phase": "deploy",
                    "message": "No zip(s) to deploy. Provide zip_path or input_dir."}

        results = []
        all_ok = True
        for z in zips:
            args = [pac, "solution", "import", "--path", str(z)]
            if environment:
                args.extend(["--environment", environment])
            if async_import:
                args.append("--async")
                args.extend(["--max-async-wait-time", str(max_async_wait)])
            if force_overwrite:
                args.append("--force-overwrite")
            r = _run_subproc(args, timeout=1800)
            imported_ok = (r["returncode"] == 0
                           and "Imported successfully" in (r["stdout"] + r["stderr"]))
            if not imported_ok:
                all_ok = False
            results.append({"zip": str(z),
                            "status": "ok" if imported_ok else "error",
                            "returncode": r["returncode"],
                            "stdout_tail": _tail(r["stdout"], 2000),
                            "stderr_tail": _tail(r["stderr"], 1000)})

        return {"status": "ok" if all_ok else "error",
                "phase": "deploy",
                "zip_count": len(zips),
                "imports": results}

class _PacPipelineEngine(_EngineBase):
    def __init__(self):
        self.name = "Rapp2McsFactory"
        self.metadata = {
            "name": self.name,
            "description": (
                "End-to-end RAPP→MCS conversion + deploy. Orchestrates "
                "AIBAST_RAPP/scripts (analyzer → normalizer → "
                "wrapper_generator) plus pac CLI. No Azure Functions, "
                "no custom connectors, no custom Dataverse tables — "
                "only OOTB CDS via shared_commondataserviceforapps.\n\n"
                "Actions:\n"
                " • 'scan' — list RAPP *_agent.py files in agents_dir (read-only).\n"
                " • 'analyze' — AIBAST analyzer over agents_dir.\n"
                " • 'normalize' — AIBAST normalizer + OOTB-only policy filter.\n"
                " • 'package' — AIBAST wrapper_generator → solution.zip(s).\n"
                " • 'deploy' — pac solution import to the active pac env.\n"
                " • 'pipeline' — analyze → normalize → package → deploy "
                "   end-to-end. Press one button; the factory decides each "
                "   intermediate step. The only required input is the "
                "   agents_dir (defaulted to rapp_brainstem/agents)."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["scan", "analyze", "normalize", "package", "deploy", "pipeline"],
                        "description": "Which phase(s) to run. 'pipeline' is the one-button option.",
                    },
                    "agents_dir": {
                        "type": "string",
                        "description": "RAPP agents directory. Default: rapp_brainstem/agents",
                    },
                    "workspace": {
                        "type": "string",
                        "description": "Where intermediates land. Default: build/factory/<timestamp>",
                    },
                    "environment": {
                        "type": "string",
                        "description": "Optional pac --environment override (URL or ID). "
                                       "Default: active pac auth profile.",
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["openai", "azure"],
                        "description": "LLM provider for analyzer/normalizer. Default: openai.",
                    },
                    "api_key": {
                        "type": "string",
                        "description": "OpenAI API key. Defaults to OPENAI_API_KEY env var.",
                    },
                    "solution_version": {
                        "type": "string",
                        "description": "Power Platform solution version (e.g. 1.0.0.5). "
                                       "If omitted, AIBAST wrapper_generator picks one.",
                    },
                    "force_overwrite": {
                        "type": "boolean",
                        "description": "Pass --force-overwrite to pac solution import. Default: true.",
                    },
                    "publisher_prefix": {"type": "string"},
                    "publisher_name": {"type": "string"},
                    "publisher_display": {"type": "string"},
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def run(self, action="pipeline", **kwargs):
        try:
            ctx = self._context(kwargs)
            if action == "scan":
                return json.dumps(self._scan(ctx), indent=2)
            if action == "analyze":
                return json.dumps(_InternalAnalyze().perform(
                    input_path=ctx["agents_dir"],
                    output_dir=ctx["analyze_dir"],
                    ir_dir=ctx["ir_dir"],
                    mode=ctx["mode"],
                    api_key=ctx["api_key"]), indent=2)
            if action == "normalize":
                return json.dumps(_InternalNormalize().perform(
                    input_path=ctx["analyze_dir"],
                    output_dir=ctx["normalize_dir"],
                    mode=ctx["mode"]), indent=2)
            if action == "package":
                return json.dumps(_InternalPackage().perform(
                    input_path=ctx["normalize_dir"],
                    output_dir=ctx["package_dir"],
                    solution_version=ctx["solution_version"],
                    publisher_prefix=ctx["publisher_prefix"],
                    publisher_name=ctx["publisher_name"],
                    publisher_display=ctx["publisher_display"],
                    mode=ctx["mode"]), indent=2)
            if action == "deploy":
                return json.dumps(_InternalDeploy().perform(
                    input_dir=ctx["package_dir"],
                    environment=ctx["environment"],
                    force_overwrite=ctx["force_overwrite"]), indent=2)
            if action == "pipeline":
                return json.dumps(self._pipeline(ctx), indent=2)
            return json.dumps({"status": "error",
                               "message": f"Unknown action: {action}"})
        except Exception as e:
            return json.dumps({"status": "error",
                               "action": action,
                               "exception": type(e).__name__,
                               "message": str(e)})

    # — Context resolution ——————————————————————————————————

    def _context(self, k):
        repo = _find_repo_root()
        agents_dir = k.get("agents_dir") or str(repo / "rapp_brainstem" / "agents")
        ws = k.get("workspace") or str(
            repo / "build" / "factory" / time.strftime("%Y%m%d-%H%M%S"))
        ws_path = Path(ws); ws_path.mkdir(parents=True, exist_ok=True)
        return {
            "repo_root": str(repo),
            "agents_dir": agents_dir,
            "workspace": str(ws_path),
            "analyze_dir": str(ws_path / "analyzer"),
            "ir_dir": str(ws_path / "analyzer" / "ir"),
            "normalize_dir": str(ws_path / "normalizer"),
            "package_dir": str(ws_path / "solutions"),
            "environment": k.get("environment"),
            "mode": k.get("mode", "openai"),
            "api_key": k.get("api_key"),
            "solution_version": k.get("solution_version"),
            "force_overwrite": bool(k.get("force_overwrite", True)),
            "publisher_prefix": k.get("publisher_prefix", "rapp"),
            "publisher_name": k.get("publisher_name", "RAPP"),
            "publisher_display": k.get("publisher_display", "RAPP"),
        }

    # — scan (no LLM, no subprocess; just enumerate the agents/ dir) —

    def _scan(self, ctx):
        agents_dir = Path(ctx["agents_dir"])
        if not agents_dir.is_dir():
            return {"status": "error", "message": f"agents_dir not found: {agents_dir}"}
        files = sorted(p.name for p in agents_dir.glob("*_agent.py")
                       if p.name != "basic_agent.py")
        return {"status": "ok",
                "phase": "scan",
                "agents_dir": str(agents_dir),
                "agents": files,
                "count": len(files)}

    # — pipeline (the one-button action) ———————————————————————

    def _pipeline(self, ctx):
        scan = self._scan(ctx)
        if scan["status"] != "ok" or scan["count"] == 0:
            return {"status": "error", "stage": "scan", "scan": scan}

        analyze = _InternalAnalyze().perform(
            input_path=ctx["agents_dir"],
            output_dir=ctx["analyze_dir"],
            ir_dir=ctx["ir_dir"],
            mode=ctx["mode"],
            api_key=ctx["api_key"])
        if analyze["status"] != "ok":
            return {"status": "error", "stage": "analyze",
                    "scan": scan, "analyze": analyze}

        normalize = _InternalNormalize().perform(
            input_path=ctx["analyze_dir"],
            output_dir=ctx["normalize_dir"],
            mode=ctx["mode"],
            no_azure_function=True,
            ootb_dataverse_only=True)
        if normalize["status"] != "ok":
            return {"status": "error", "stage": "normalize",
                    "scan": scan, "analyze": analyze, "normalize": normalize}

        package = _InternalPackage().perform(
            input_path=ctx["normalize_dir"],
            output_dir=ctx["package_dir"],
            solution_version=ctx["solution_version"],
            publisher_prefix=ctx["publisher_prefix"],
            publisher_name=ctx["publisher_name"],
            publisher_display=ctx["publisher_display"],
            mode=ctx["mode"])
        if package["status"] != "ok":
            return {"status": "error", "stage": "package",
                    "scan": scan, "analyze": analyze,
                    "normalize": normalize, "package": package}

        deploy = _InternalDeploy().perform(
            input_dir=ctx["package_dir"],
            environment=ctx["environment"],
            force_overwrite=ctx["force_overwrite"])
        return {"status": deploy["status"],
                "workspace": ctx["workspace"],
                "scan": scan,
                "analyze": analyze,
                "normalize": normalize,
                "package": package,
                "deploy": deploy}

def _aibast_cache_dir():
    """Return the per-user cache dir for THIS singleton version. The
    directory is created on first call; the AIBAST bundle is extracted
    into it once and reused thereafter. Override via RAPP2MCS_AIBAST_CACHE.
    """
    override = os.environ.get("RAPP2MCS_AIBAST_CACHE")
    if override:
        return Path(override)
    tag = _AIBAST_BUNDLE_TAG  # short content hash baked at emit time
    return Path(_tempfile.gettempdir()) / "rapp2mcs_factory" / tag

def _ensure_aibast_extracted():
    """Idempotently extract the embedded AIBAST_RAPP bundle. Returns the
    path to the extracted scripts/ directory. Skips work if already done."""
    cache = _aibast_cache_dir()
    scripts_dir = cache / "scripts"
    sentinel = cache / ".extracted"
    if sentinel.is_file():
        return scripts_dir
    cache.mkdir(parents=True, exist_ok=True)
    raw = _gz.decompress(_b64.b64decode(_AIBAST_BUNDLE_GZ_B64))
    with _zipfile.ZipFile(_io.BytesIO(raw)) as zf:
        zf.extractall(cache)
    sentinel.write_text(_AIBAST_BUNDLE_TAG, encoding="utf-8")
    return scripts_dir

def _aibast_script(*parts):
    """Resolve an AIBAST script under the extracted bundle. Override the
    bundle source via the RAPP2MCS_AIBAST_DIR env var (points to a local
    AIBAST_RAPP/ dir if you want to dev against unbundled scripts)."""
    env_dir = os.environ.get("RAPP2MCS_AIBAST_DIR") or os.environ.get("AIBAST_DIR")
    if env_dir:
        cand = Path(env_dir) / "scripts" / Path(*parts)
        if cand.is_file():
            return cand
    scripts_dir = _ensure_aibast_extracted()
    cand = scripts_dir / Path(*parts)
    return cand if cand.is_file() else None

_AIBAST_BUNDLE_TAG = "H4sIADgVCWoC"

_AIBAST_BUNDLE_GZ_B64 = (
    "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"
    "8jn+eqnQUMgS5p4cRN2sJ1Vr6pNqyXqpCKMVQUEKmdMG05XFfEJkU4hft7MHGg3SHRTRwcveDz6W3+bsK9+M1UbRhIVVY+1j"
    "5sIlOZrTRbVFLMIktFRe6KlcwjyN33NuBCHTyjoHzIvOCbuEF0U7axdWf6xV9NpzOtZKla1myasPIkhM1ONUif53lKpmrlqT"
    "gakyYtb8EPyBKCPOcPIP/dA5Kx8XtOxNRs7CbOip4OXIOSntU6o9+myK3SNb0c3BWAYgbImLD4/vI05iKk07+qzjaUzl9yk/"
    "o1zjiiEu8CBeCO0Cz0rW2HuuCcoMEO6lM5/FWD3QSik7H4kFuU7/xzXe8M9mNKRWdWZ/2SY5cYQ9c3YhdXS56tIGwdSxiTAd"
    "f+Puj4O7yT5xuj5tMdypdKCrPnc67nfIcRFc8+1giAKqFJDuhwJqIeG81J0Tb8b6Su+/D/d/AgAggP9jlP/DcDsa2Nvr/U9C"
    "u8D/l1Du3KKoLNl/XuT/cY7/Z6H/LZarZ2PibGBs4GygZ+Lu7Ghg9H9geqlZCRo61f+t3fsgQyshLUEj4VxDQSkpTTdB33h4"
    "oggQCJQP9X81R8XYbPSFBwBAYAEAoP9/NjezcDZ3MdT7/5L/tbiwbeSORD+9fEey1cpjM9n5LVREZOqu6WjKk0VomlPYjWUO"
    "IR3WGnxyGQlP4m+XfvyXfgZ/E71yzUZf30nrrxUuHg0krjPMct/WNMYcPP8VaB4r+dEtWxMy0eu8hc7I3cXrSrr2+rmOvseE"
    "o3JpVYkgMWccb0jXe2AMXHmk0mCa3Qm6JMtpkC0Kh1JNrNKkGXgPLQs+7+N2jQfrf5mN4XlRG7sjR/lXBM+AfsMOSk8rN5sa"
    "wMS9PhTnBR8Cqn3vy5p4g+13696JNZgC3oTwNcmHStBs1DzfQ6QaH8hgPIVjJqZnmxhUHrePrcfrSPIvjwZ2cFmPFpXDm0mS"
    "uvcncuzzTjFj7kK9kkWg6hO+LO4oaVJ/gVwRfVAYokm6et4/DXBo3dOkkwLGP4zx/Q25Nx9aQcYDEDGKDrddp5r542cB9lJN"
    "JWClPkbTQ25zqAWKHCDFa/XTJUiMMg/4h26IAUBto7UBtWdAZgABCGTFHhF0wwbhXIAS1nPAF+Gozqt+MEorIcKoZ1O4F7kX"
    "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"
    "HRjlZ5he85oSj5M8GPmoBR8rhz3K+oWENL5Er1nbSASmrpYtEbNTxqnSNa1wqgCjb6fkzNwL9FakSnd3NbLfbfd0PAdpKK/n"
    "UZ7Eo61OLnTyE3HziIBnJyA36gM8TlggIbdvd0I5mQUFuzZhw7vO31Jv0zjJ8L7oTPPXJ+iD6euBt+QAD87CV0tZT/kxiQPT"
    "+VBwiq3Z/0LNLqRj5640gpqL9z+Lny4UF3lZsHrrCU26+rieamGhCPX0OYt4Jv0X3Dnsdcl7sXdhUDWwOX1ZdJpzkIyNfNtr"
    "ioeSnwj+jsgVOr533iZ/I/EmeUAO/HX7H9S87rv4BRK81G4pT+BSi/Q9pSn3//BtDuGZMAAOrm1jatt2p7Zt2/bUtm3btv3V"
    "tm1j/9s+e9lzbjkkbw6ByBC0CWbmOj0EB3Uj+bNWEsOgvZZohMfpSJtxDKLJ0ojn+DdYvtJ92EqiAkT5kqIBIvQSABeyGvSl"
    "a+qU+RJYFG8I/yars7aJpWJ127J3DZQ5eigkHKBgPT2njcNfzj5o2a0puU9sQ8YOC6AglnC2EOj1M6bKxU29G6bgV8yL+ZY8"
    "VubwoUO+NM0WOWtWMRbd30wEwIac6ygTtmNiJYCXPhghLD36yffAp1BiDJ8yEMW08WrLlVNWC6mpVuYVZRYA6SiwrJthw1GA"
    "SOPI4Sw9plBaTdYpPK4EEL45PG3eTHC2R9fe9Krof60cM5II3oKO7EtMmsCOGa5vW9bQ2LtGzq3pX45T0RiOgZvZm34+JS0u"
    "HcuQp5KPRShEUUlL4dDPxfJ8wYAPouZCYyGrAwGtp4KHg+dJK/ciUVeAxwWu8Oevw8JNeQJKo/qNpiSptFAzcedngTmi9YJN"
    "76wbMH+LDMRBjF2NksOO6Gbo1OknAxP+8mmReKUSK44aelN0aHQwr8cZFupn6mkqsN6Q+1Cm4srwsYoe0XEOf1inBc8inb69"
    "2moLYQmAGvAdMyFHaHh7MsC8vulAlU/JbTZPBwR7IT+xpyA2U2xtL18wCeYgM4ZksyyT/6yQye6mSFv1d7I8wVzMFooq5jXP"
    "S2tlTpYCbZU11S6UhONDTR/o78CPD3bYJ0CGZd5mBxIrVQYTBCGpCzihXmeFWIg9oljsRZFu00YPKnCJ8AD92Yf30r83Qboc"
    "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"
    "mZoMzBqns6nmw8B1wuaOEDX8imlkdaiPSzlbsPOyEsbA16enD/LvMKIHonaRa2xhpDFVF/U9rQ4i5L1InteO8YcvnFdZE7lP"
    "el/TFMufqVaxACfG/IeVoofdkYIAL8v2mZyD9FH8TNS2TCC/BZ8NiDMqgBM0M7JNJNdi0P/B4pSTM7rPhhPv6G/RdknrMRJC"
    "fFDVVm3vigooFcu+zUP3BXW/iqdDzN4OCeT6DSaaEWJfN5QZs0/Jb+s29UODjRUlhJW1FzjkQ00QA5wXXQ4IV/DyTMBdM7MG"
    "oMwkuUzgtOlszl/84q1Le9Z5Q6fAbXtyhxa6yiuq97LK1tjnOtBGbcqsb/Mz8/ntVg03QTgi5cz2qoSRvXrUsCjJl7VYc6tT"
    "OyVnZ8dKyAqSYaZu04vxqUKoG2Jk/tpqXV0QYRndyU72wN6VNp1f17KASp/1JBX7EOQRttdq7OElULCq6AtEbA5ZnQVFsgZR"
    "e7myUYMLZupSsxezLqBy/OXiPruRG7choPkXmvX6+g5iiq0G4Yi6qkwlsErRK1IwBo7T5adcHYLa/0oFSgiZfR7f+wZJ70O7"
    "inYcm6RND4Oi8rOdfKgU/atBPuoILCbfSy9HWxF5qY61ec6Air7f1xSYyBaR3G7/w3DZz7yEin0ZRxN12Fd3lrQ2c41V4BQR"
    "+puRdleX2rpmE1YvTliqqHLa6OkIasDBsGUy1WEtHxvjqsaQ4MFSRJnKTrrtSNXnwmsE/IQi9yEg/ccGn6z8XgOpqnpRd530"
    "790aNai6M3QQ/bN1dG8fNaAvoqzJ/z7dcccmjVW6aqVGr0FtrUrbFgR7/VL+qXt19vf03mrQtufkpDyBC05u/mGa8Io9ridp"
    "QiEk8KHjbthBKUHT6Eb8q4Z1pFqJjTnNb+OvU9ImWtHJzKCxwpSJLYWMsymBfcvRn3uVUpfJbvk78yJ9AorzZzY76bGbpG/L"
    "S7ViM9EmMbSMyhaTRwu8+sGvBe0fvTyF01N0j/r8rtB+y2pxZ/HlraC6r4nx3m/vG4pfECYQ/HQl3Fva4ypE/A3Z7eeqJXtd"
    "jpu2lUtbGKcte8mNWfNMyKtO6NvPunfVovUDK9WhgKNp6GbdlX41KzJWS3YKdas1GxXjby3vhkAArN/xaN3ONiHzLKLGpO0P"
    "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"
    "aKGyUQIA"
)



# ============================================================================
# FACTORY engine — quality-gated agent.py -> Copilot Studio pipeline chain
# (rich SYNTHETIC_DATA seeds, connector hygiene, MVP->generate->import->
#  activate->publish->verify). Assimilated from copilot_studio_factory.
# ============================================================================
import importlib.util
import json
import os
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path


_FACTORY_METADATA = {
    "name": "copilot_studio_factory",
    "version": "1.0.0",
    "description": ("Factory for Microsoft Copilot Studio agents: quality-"
                    "gates brainstem agent.py files (rich SYNTHETIC_DATA "
                    "demo seeds, connector hygiene), then deploys them via "
                    "the RAPP pipeline: MVP -> generate LIVE+Demo "
                    "twins -> import -> activate -> publish -> verify. "
                    "Autonomous; returns the demo script and maker links."),
    "tags": ["rapp", "copilot-studio", "deploy", "pipeline", "dataverse"],
}

DEFAULT_PIPELINE_URL = os.environ.get("RAPP_PIPELINE_URL", "")
DEFAULT_RESOURCE = os.environ.get("RAPP_MCS_RESOURCE", "")
DEFAULT_ENVIRONMENT_ID = os.environ.get("RAPP_MCS_ENVIRONMENT_ID", "")
DEFAULT_AGENT_DIRS = [
    os.environ.get("BRAINSTEM_AGENTS_DIR", ""),
    str(Path.home() / ".brainstem" / "agents"),
    "agents",
]
DEPLOY_SETTINGS = Path.home() / ".rapp_deploy_settings.json"
ARTIFACT_ROOT = Path.home() / ".rapp_mcs_autodeploy"
AZ_SUBSCRIPTION = os.environ.get("RAPP_AZ_SUBSCRIPTION", "")
# Direct Line probe helper (optional; probe is skipped gracefully without it)
PIPELINE_REPO = Path(os.environ.get(
    "RAPP_PIPELINE_REPO",
    str(Path.home() / "MSFTAIBASTRAPP" / "RAPPtranscript2Prototype")))


def _truthy(value, default=False):
    if value is None or value == "":
        return default
    return str(value).strip().lower() in ("1", "true", "yes", "y", "on")


def _http(method, url, body=None, headers=None, timeout=120):
    data = None
    hdrs = dict(headers or {})
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        hdrs.setdefault("Content-Type", "application/json")
    request = urllib.request.Request(url, data=data, headers=hdrs,
                                     method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8", "replace")
            try:
                return response.status, (json.loads(raw) if raw.strip()
                                         else {})
            except Exception:
                return response.status, {"error": raw[:500]}
    except urllib.error.HTTPError as error:
        raw = error.read().decode("utf-8", "replace")
        try:
            return error.code, json.loads(raw)
        except Exception:
            return error.code, {"error": raw[:500]}
    except (urllib.error.URLError, OSError) as error:
        return 0, {"error": str(error)[:300]}


def _multipart(url, fields, files, bearer="", timeout=900):
    boundary = "----RappAutodeploy" + uuid.uuid4().hex
    body = bytearray()
    for name, value in fields.items():
        body.extend(f"--{boundary}\r\n".encode())
        body.extend(
            f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode())
        body.extend(str(value).encode("utf-8"))
        body.extend(b"\r\n")
    for path in files:
        body.extend(f"--{boundary}\r\n".encode())
        body.extend((f'Content-Disposition: form-data; name="files"; '
                     f'filename="{Path(path).name}"\r\n'
                     "Content-Type: text/x-python\r\n\r\n").encode())
        body.extend(Path(path).read_bytes())
        body.extend(b"\r\n")
    body.extend(f"--{boundary}--\r\n".encode())
    headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
    if bearer:
        headers["Authorization"] = "Bearer " + bearer
    request = urllib.request.Request(url, data=bytes(body), headers=headers,
                                     method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        raw = error.read().decode("utf-8", "replace")
        try:
            payload = json.loads(raw)
        except Exception:
            payload = {"error": raw[:400]}
        payload.setdefault("status", f"http {error.code}")
        return payload
    except (urllib.error.URLError, OSError) as error:
        return {"status": "unreachable", "error": str(error)[:300]}



# --------------------------------------------------------------------------
# QUALITY LAYER — the factory's preflight. Learned from side-by-side pattern
# tests (pipeline vs agent.py vs plugin): demo quality lives or dies on the
# seeds, and live-twin activation lives or dies on the connector words.
# --------------------------------------------------------------------------

_SCAFFOLD_WORDS = (  # description words that trigger NON-activating scaffold
    "sharepoint", "spo", "site list", "document library", "salesforce",
    "sfdc", "servicenow", "service now", "sql", "database", "warehouse",
    "synapse")

_CONTROL_PARAMS = {"view", "action", "accepted", "mode", "debug", "top",
                   "limit", "format"}

_NAME_POOL = ("Priya Sharma", "Marcus Webb", "Elena Rossi", "David Chen",
              "Amara Okafor")
_ORG_POOL = ("Northwind Traders Ltd", "Contoso Energy", "Fabrikam Health",
             "Adventure Works Bank", "Proseware Logistics")
_STATUS_POOL = ("new", "in review", "approved", "on hold", "complete")


def _factory_seed_value(field, i):
    """A REALISTIC deterministic value for `field` on row i (1-based) — token-
    typed like the emitter's synthesizer but drawing from believable pools
    instead of placeholder strings."""
    f = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", field).lower()
    toks = set(t for t in re.split(r"[^a-z0-9]+", f) if t)
    if toks & {"score", "rate", "ratio", "pct", "percent", "confidence",
               "risk", "probability", "utilisation", "utilization"}:
        return round(0.12 + 0.18 * ((i - 1) % 5), 2)
    if f.startswith(("is_", "has_")) or toks & {"flag", "enabled", "active"}:
        return i % 2 == 0
    if toks & {"date", "time", "timestamp", "created", "updated", "due"}:
        return "2026-07-%02dT09:00:00Z" % min(i + 3, 28)
    if toks & {"id", "ref", "reference", "code", "number"} and "name" not in toks:
        return "REC-%04d" % (1000 + i)
    if toks & {"amount", "value", "total", "price", "cost", "balance",
               "loanamount"}:
        return [12500, 18500, 27500, 32000, 45000][(i - 1) % 5]
    if toks & {"count", "qty", "quantity", "days", "age", "term", "months"}:
        return [12, 24, 36, 48, 60][(i - 1) % 5]
    if toks & {"name", "applicant", "customer", "person", "owner",
               "beneficiary"} and not toks & {"company", "org", "account",
                                              "bank", "vendor"}:
        return _NAME_POOL[(i - 1) % 5]
    if toks & {"company", "org", "organisation", "organization", "account",
               "bank", "vendor", "correspondent", "supplier"}:
        return _ORG_POOL[(i - 1) % 5]
    if toks & {"status", "state", "stage"}:
        return _STATUS_POOL[(i - 1) % 5]
    if toks & {"currency", "ccy"}:
        return ("GBP", "USD", "EUR", "JPY", "SGD")[(i - 1) % 5]
    return "%s example %d" % (field.replace("_", " "), i)


def _factory_record_fields(source):
    """Field names an agent.py's data rows should carry: its parameter names
    (minus control params) + dict keys its code reads via rec.get()/rec[...]."""
    import ast as _ast
    fields = []
    try:
        tree = _ast.parse(source)
    except SyntaxError:
        return fields

    _SCHEMA_KEYS = {"name", "description", "type", "parameters",
                    "properties", "required", "title", "status", "data",
                    "message"}

    def add(k):
        if (isinstance(k, str) and k.isidentifier() and k.lower() not in
                _CONTROL_PARAMS and k.lower() not in _SCHEMA_KEYS
                and k not in fields and not k.startswith("_")):
            fields.append(k)

    for node in _ast.walk(tree):
        if isinstance(node, _ast.Dict):
            keys = [k.value for k in node.keys
                    if isinstance(k, _ast.Constant) and isinstance(k.value, str)]
            kset = set(keys)
            if ("properties" in kset or {"type", "description"} <= kset
                    or {"name", "parameters"} <= kset):
                continue      # schema / metadata blocks, not data records
            for k in keys:
                add(k)
        elif (isinstance(node, _ast.Call) and isinstance(node.func, _ast.Attribute)
                and node.func.attr == "get" and node.args
                and isinstance(node.args[0], _ast.Constant)
                and isinstance(node.args[0].value, str)):
            add(node.args[0].value)
    # parameter names come first (they mirror the trigger schema)
    props = re.findall(r'"([A-Za-z][A-Za-z0-9_]*)":\s*\{\s*\n?\s*"type"',
                       source)
    ordered = [p for p in props if p.lower() not in _CONTROL_PARAMS
               and p.lower() not in _SCHEMA_KEYS]
    for f in fields:
        if f not in ordered:
            ordered.append(f)
    return ordered[:10] or ["id", "name", "status"]


def factory_preflight(path):
    """Inspect ONE agent.py for the quality contract. Returns a dict:
    {file, has_seeds, scaffold_words[], fields[]} — no mutation."""
    source = Path(path).read_text(encoding="utf-8", errors="replace")
    low = source.lower()
    words = sorted({w for w in _SCAFFOLD_WORDS
                    if re.search(r"\b" + re.escape(w) + r"\b", low)})
    stem = Path(path).stem.lower().replace("_", "")
    collisions = sorted({w for w in ("spo", "sql", "snow") if w in stem})
    return {"file": str(path),
            "has_seeds": "SYNTHETIC_DATA" in source,
            "has_binding": bool(re.search(r"^\s*CAPIR\s*=", source, re.M)),
            "name_collisions": collisions,
            "scaffold_words": words,
            "fields": _factory_record_fields(source)}


def factory_prep(path, prepped_dir):
    """Return a deployable path for `path`: the file itself when it already
    carries SYNTHETIC_DATA, else a PREPPED COPY (under `prepped_dir`) with a
    realistic auto-generated SYNTHETIC_DATA literal inserted as the first
    class-level attribute. The user's original file is NEVER modified."""
    report = factory_preflight(path)
    inject_binding = (not report["has_binding"]
                      and not report["scaffold_words"])
    if report["has_seeds"] and not inject_binding:
        return str(path), report
    source = Path(path).read_text(encoding="utf-8", errors="replace")
    match = re.search(r"(class \w+\([A-Za-z_.]*BasicAgent\):\n)", source)
    if not match:
        return str(path), report          # no class found — deploy as-is
    lines = []
    if inject_binding:
        # Pin the demo data home EXPLICITLY. Substring keyword scans downstream
        # can mis-map names (e.g. 'spo' inside 'correspondent' -> SharePoint);
        # an explicit binding.system is authoritative and immune to that.
        lines.append('    CAPIR = {"binding": {"system": "Microsoft '
                     'Dataverse", "table": "accounts"}}')
        report["injected_binding"] = True
    if not report["has_seeds"]:
        fields = report["fields"]
        rows = [{f: _factory_seed_value(f, i) for f in fields}
                for i in range(1, 6)]
        lines.append("    SYNTHETIC_DATA = [")
        for r in rows:
            lines.append("        " + json.dumps(r) + ",")
        lines.append("    ]")
    prepped = (source[:match.end()] + "\n".join(lines) + "\n\n"
               + source[match.end():])
    out = Path(prepped_dir)
    out.mkdir(parents=True, exist_ok=True)
    target = out / Path(path).name
    target.write_text(prepped, encoding="utf-8")
    report["prepped"] = str(target)
    return str(target), report


class CopilotStudioFactoryAgent(BasicAgent):
    """Ship picked brainstem agents to Copilot Studio, autonomously."""

    def __init__(self):
        self.name = "CopilotStudioFactory"
        self.metadata = {
            "name": self.name,
            "description": _FACTORY_METADATA["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "mode": {
                        "type": "string",
                        "description": ("Optional: 'check' = quality-check "
                                        "only (no deploy); 'scaffold' = "
                                        "generate a new quality agent.py "
                                        "template (with name/description/"
                                        "fields params). Default: deploy."),
                    },
                    "allow_scaffolds": {
                        "type": "string",
                        "description": ("true = deploy even when agent "
                                        "descriptions name systems that "
                                        "produce non-activating scaffold "
                                        "connectors (default false: noted)."),
                    },
                    "agents": {
                        "type": "string",
                        "description": ("Agent names or paths to deploy, comma"
                                        " or space separated. Leave EMPTY to"
                                        " list the deployable agents - never"
                                        " ask the user for this value."),
                    },
                    "agent_dir": {
                        "type": "string",
                        "description": ("Directory to resolve agent names in "
                                        "(default: brainstem agents/)."),
                    },
                    "solution_name": {
                        "type": "string",
                        "description": ("Base solution name; a timestamp is "
                                        "ALWAYS appended so runs never "
                                        "collide."),
                    },
                    "publisher_prefix": {
                        "type": "string",
                        "description": "Dataverse publisher prefix (letters).",
                    },
                    "pipeline_url": {
                        "type": "string",
                        "description": ("RAPP pipeline base URL (default: the"
                                        " deployed function app)."),
                    },
                    "bearer": {
                        "type": "string",
                        "description": ("Entra ID bearer for the pipeline "
                                        "(or env DCS_BEARER)."),
                    },
                    "resource": {
                        "type": "string",
                        "description": "Dataverse environment URL to deploy to.",
                    },
                    "environment_id": {
                        "type": "string",
                        "description": ("Power Platform environment GUID "
                                        "(enables the Direct Line probe)."),
                    },
                    "twin": {
                        "type": "string",
                        "description": "Which twins to deploy: both|demo|live.",
                    },
                    "dry_run": {
                        "type": "string",
                        "description": ("true = generate + validate only "
                                        "(no import)."),
                    },
                    "probe": {
                        "type": "string",
                        "description": ("true (default) = live-chat the demo "
                                        "twin's first advertised example "
                                        "after publish."),
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # ---- agent resolution -------------------------------------------------

    def _agent_dirs(self, agent_dir):
        dirs = []
        for candidate in ([agent_dir] if agent_dir else []) + DEFAULT_AGENT_DIRS:
            if not candidate:
                continue
            path = Path(candidate).expanduser()
            if path.is_dir() and path not in dirs:
                dirs.append(path)
        return dirs

    def _discover(self, dirs):
        found = {}
        for base in dirs:
            for path in sorted(base.rglob("*.py")):
                if path.name.startswith("_") or path.name == "basic_agent.py":
                    continue
                if path.name == Path(__file__).name:
                    continue  # never deploy the deployer
                found.setdefault(path.stem, path)
        return found

    def _resolve(self, tokens, dirs):
        available = self._discover(dirs)
        picked, problems = [], []
        for token in tokens:
            path = Path(token).expanduser()
            if path.is_file():
                picked.append(path)
                continue
            stem = re.sub(r"\.py$", "", token).strip().lower()
            exact = [p for s, p in available.items() if s.lower() == stem
                     or s.lower() == stem + "_agent"]
            if len(exact) == 1:
                picked.append(exact[0])
                continue
            partial = [p for s, p in available.items() if stem in s.lower()]
            if len(partial) == 1:
                picked.append(partial[0])
            elif len(partial) > 1:
                problems.append("'%s' is ambiguous: %s" % (
                    token, ", ".join(sorted(p.stem for p in partial)[:6])))
            else:
                problems.append("'%s' not found" % token)
        return picked, problems, available

    # ---- auth -------------------------------------------------------------

    def _pipeline_auth(self, pipeline_url, bearer):
        bearer = (bearer or os.environ.get("DCS_BEARER", "")).strip()
        status, health = _http("GET", pipeline_url + "/health", timeout=30)
        if status != 200:
            return None, f"pipeline unreachable at {pipeline_url} ({status})"
        if str(health.get("auth", "")).lower() in ("disabled", "none", ""):
            return "", None
        if bearer:
            return bearer, None
        # auth-gated and no token: fail fast with the exact fix
        return None, (
            "The pipeline at %s requires an Entra ID sign-in and no bearer "
            "was provided. Run `export DCS_BEARER=$(python3 "
            "scripts/get_token.py)` in the pipeline repo (one device-code "
            "tap), then retry — or pass bearer=<token>." % pipeline_url)

    def _dataverse_token(self, resource, explicit):
        """First WhoAmI-verified credential wins."""
        candidates = []
        if explicit:
            candidates.append(("explicit token", lambda: explicit))
        if DEPLOY_SETTINGS.is_file():
            candidates.append(("service principal",
                               lambda: self._sp_token(resource)))
        candidates.append(("azure cli", lambda: subprocess.check_output(
            ["az", "account", "get-access-token"]
            + (["--subscription", AZ_SUBSCRIPTION] if AZ_SUBSCRIPTION else [])
            + ["--resource", resource, "--query", "accessToken", "-o", "tsv"],
            text=True, timeout=60).strip()))
        for label, mint in candidates:
            try:
                token = mint()
            except Exception:
                continue
            if not token:
                continue
            status, _who = _http(
                "GET", resource + "/api/data/v9.2/WhoAmI",
                headers={"Authorization": "Bearer " + token}, timeout=30)
            if status == 200:
                return token, label
        return None, None

    def _sp_token(self, resource):
        cfg = json.loads(DEPLOY_SETTINGS.read_text())
        body = urllib.parse.urlencode({
            "grant_type": "client_credentials",
            "client_id": cfg.get("client_id", ""),
            "client_secret": cfg.get("client_secret", ""),
            "scope": resource.rstrip("/") + "/.default",
        }).encode()
        request = urllib.request.Request(
            "https://login.microsoftonline.com/%s/oauth2/v2.0/token"
            % cfg.get("tenant_id", ""),
            data=body,
            headers={"Content-Type": "application/x-www-form-urlencoded"})
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode()).get("access_token")

    # ---- deploy + verification -------------------------------------------

    def _deploy_twin(self, pipeline_url, bearer, resource, token, label,
                     b64, name, schemas, workflow_ids, log):
        headers = {"Authorization": "Bearer " + bearer} if bearer else {}
        status, started = _http("POST", pipeline_url + "/deploy", {
            "resource": resource, "dataverse_token": token,
            "solution_b64": b64, "solution_name": name, "publish": True,
            "bot_schemas": schemas, "workflow_ids": workflow_ids,
            "run_id": "autodeploy", "debug": True}, headers=headers)
        if status != 200 or started.get("status") != "importing":
            raise RuntimeError(f"{label} deploy did not start: {started}")
        latest = {}
        for _attempt in range(60):
            status, latest = _http("POST", pipeline_url + "/status", {
                "environment": resource, "resource": resource,
                "dataverse_token": token,
                "import_job_id": started["import_job_id"],
                "bot_schemas": schemas, "workflow_ids": workflow_ids,
                "publish": True, "run_id": "autodeploy", "debug": True},
                headers=headers)
            if latest.get("status") in ("deployed", "imported", "error"):
                break
            time.sleep(10)
        if latest.get("status") != "deployed":
            raise RuntimeError(f"{label} deploy failed: "
                               f"{json.dumps(latest)[:400]}")
        log.append(f"{label}: imported + published ({name})")
        return latest

    def _verify_workflows(self, resource, token, workflow_ids, label, log,
                          strict=True):
        """deployed != activated: every flow must reach statecode 1; a Draft
        flow is hot-activated in place (the platform validator then rules on
        the definition). Custom-connector scaffold flows legitimately stay
        Draft until a connection is bound — with strict=False that state is
        classified pending_connection and reported, not raised."""
        results, pending = {}, []
        headers = {"Authorization": "Bearer " + token,
                   "Content-Type": "application/json", "If-Match": "*"}
        for schema, wfid in (workflow_ids or {}).items():
            url = f"{resource}/api/data/v9.2/workflows({wfid})"
            status, doc = _http("GET", url + "?$select=statecode,name",
                                headers=headers, timeout=30)
            state = doc.get("statecode")
            activation_error = ""
            if status == 200 and state == 0:
                _pstatus, perr = _http(
                    "PATCH", url, {"statecode": 1, "statuscode": 2},
                    headers=headers, timeout=60)
                activation_error = json.dumps(perr)[:300]
                status, doc = _http("GET", url + "?$select=statecode",
                                    headers=headers, timeout=30)
                state = doc.get("statecode")
                if state == 1:
                    log.append(f"{label}: flow {schema} was Draft -> "
                               "hot-activated")
            if state != 1 and not strict and re.search(
                    r"connection", activation_error, re.I):
                pending.append(schema)
                log.append(f"{label}: flow {schema} PENDING CONNECTION — "
                           "expected for a scaffold connector; bind its "
                           "connection reference in Solutions, then turn "
                           "the flow on.")
                results[schema] = "pending_connection"
                continue
            results[schema] = state
        bad = {s: v for s, v in results.items()
               if v not in (1, "pending_connection")}
        if bad:
            raise RuntimeError(
                f"{label}: flows NOT activated (statecode!=1): {bad} — the "
                "solution imported but these tools will throw FlowDisabled.")
        activated = sum(1 for v in results.values() if v == 1)
        if activated:
            log.append(f"{label}: {activated} flow(s) verified activated "
                       "(statecode 1)")
        return results

    def _probe_demo(self, environment_id, schema, example, log):
        probe_path = PIPELINE_REPO / "scripts" / "copilotstudio_postdeploy_test.py"
        if not probe_path.is_file():
            log.append("probe: skipped (postdeploy helper not on this machine)")
            return None
        spec = importlib.util.spec_from_file_location("postdeploy", probe_path)
        postdeploy = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(postdeploy)
        channel = postdeploy.discover_channel(environment_id)
        deadline = time.time() + 300
        while time.time() < deadline:
            try:
                postdeploy.acquire_conversation_token(
                    channel["environment_api_host"], schema,
                    channel["regional_url"], "")
                break
            except postdeploy.PostDeployError:
                time.sleep(6)
        result = {}
        for _attempt in range(4):
            result = postdeploy.run_probe(channel, schema, example["text"],
                                          master_secret="", timeout=90,
                                          max_wait=75)
            if result.get("status") == "passed":
                break
            time.sleep(30)
        text = "\n".join(result.get("responses") or [])
        # Judge grounding, not string echo: a correct answer may present the
        # record without repeating the raw ID (proven on the first real run:
        # the bot served the right customer record, ID unechoed).
        marker = str(example.get("query_value") or "").strip()
        ok = result.get("status") == "passed" and len(text.strip()) > 40
        echoed = bool(marker) and marker.lower() in text.lower()
        log.append("probe: " + (
            "PASSED — the advertised example answered"
            + (" (seeded key echoed)" if echoed else " (grounded answer)")
            if ok else f"FAILED: {text[:200]}"))
        return {"passed": ok, "prompt": example["text"],
                "answer": text[:600]}

    # ---- main -------------------------------------------------------------

    def perform(self, **kwargs):
        agents_raw = str(kwargs.get("agents") or "").strip()
        agent_dir = str(kwargs.get("agent_dir") or "").strip()
        dirs = self._agent_dirs(agent_dir)

        if str(kwargs.get("mode") or "").strip().lower() == "scaffold":
            use_case = str(kwargs.get("description")
                           or kwargs.get("use_case") or "").strip()
            name = re.sub(r"[^a-z0-9_]", "",
                          str(kwargs.get("name") or "my_new").lower()
                          .replace(" ", "_")) or "my_new"
            cls = "".join(w.title() for w in name.split("_")) or "MyNew"
            fields = [f for f in re.split(
                r"[,\s]+", str(kwargs.get("fields") or "")) if f] or [
                "recordId", "customerName", "amount", "status"]
            rows = "\n".join("        " + json.dumps(
                {f: _factory_seed_value(f, i) for f in fields}) + ","
                for i in range(1, 6))
            template = (
                '"""%s — captured in Microsoft Dataverse (demo twin runs on '
                'the SYNTHETIC_DATA seed below; swap rows for your own '
                'examples)."""\n'
                "try:\n    from agents.basic_agent import BasicAgent\n"
                "except ImportError:\n"
                "    class BasicAgent:\n"
                "        def __init__(self, name, metadata):\n"
                "            self.name, self.metadata = name, metadata\n\n\n"
                "class %sAgent(BasicAgent):\n"
                "    SYNTHETIC_DATA = [\n%s\n    ]\n\n"
                "    def __init__(self):\n"
                "        self.name = \"%sAgent\"\n"
                "        self.metadata = {\n"
                "            \"name\": self.name,\n"
                "            \"description\": (\"%s — data lives in "
                "Microsoft Dataverse. Identify records by NATURAL reference "
                "(a name); never demand an internal id.\"),\n"
                "            \"parameters\": {\"type\": \"object\", "
                "\"properties\": {\n"
                "                \"%s\": {\"type\": \"string\", "
                "\"description\": \"Natural reference, e.g. '%s'. Pass "
                "the word: list to see all records - never ask the user for "
                "an id.\"},\n"
                "            }, \"required\": []},\n        }\n"
                "        super().__init__(self.name, self.metadata)\n\n"
                "    def perform(self, **kwargs):\n"
                "        ref = str(kwargs.get(\"%s\") or \"\").strip()\n"
                "        rows = self.SYNTHETIC_DATA\n"
                "        if ref and ref.lower() != \"list\":\n"
                "            rows = [r for r in rows if ref.lower() in "
                "json.dumps(r).lower()] or self.SYNTHETIC_DATA[:1]\n"
                "        lines = [\"## %s\"]\n"
                "        for r in rows[:5]:\n"
                "            lines.append(\"- \" + \" | \".join("
                "f\"{k}: {v}\" for k, v in r.items()))\n"
                "        return \"\\n\".join(lines)\n"
            ) % (use_case or cls, cls, rows, cls,
                 use_case or (cls + " records"),
                 fields[0], _factory_seed_value(fields[0], 1),
                 fields[0], use_case or cls)
            explicit = str(kwargs.get("agent_dir") or "").strip()
            if explicit:
                outdir2 = Path(explicit).expanduser()
            else:
                dirs2 = self._agent_dirs("")
                outdir2 = next((d for d in dirs2 if d.is_dir()),
                               ARTIFACT_ROOT / "scaffolded")
            outdir2.mkdir(parents=True, exist_ok=True)
            outfile = outdir2 / (name + "_agent.py")
            outfile.write_text("import json\n" + template, encoding="utf-8")
            return ("**Scaffolded** `" + str(outfile) + "` — a quality-"
                    "contract Copilot Studio agent (rich SYNTHETIC_DATA, "
                    "Dataverse-safe description, natural-reference law). "
                    "Edit the seed rows, then say: deploy " + name
                    + " to copilot studio.")

        # LOOKUP LAW: empty input = list mode, never interrogate.
        tokens = [t for t in re.split(r"[,\s]+", agents_raw) if t]
        if not tokens:
            available = self._discover(dirs)
            if not available:
                return ("**No deployable agents found.** Searched: "
                        + ", ".join(str(d) for d in dirs)
                        + ". Pass agent_dir=<path> or drop agent.py files "
                          "into your brainstem agents/ directory.")
            lines = ["**Deployable agents** (say e.g. \"deploy "
                     + sorted(available)[0] + " to copilot studio\"):"]
            lines += [f"{i}. `{stem}` — {path}"
                      for i, (stem, path) in
                      enumerate(sorted(available.items()), 1)]
            return "\n".join(lines[:30])

        picked, problems, available = self._resolve(tokens, dirs)
        if problems:
            return ("**Cannot deploy yet:** " + "; ".join(problems)
                    + ".\nAvailable: " + ", ".join(sorted(available)[:20]))
        if not picked:
            return "**No agent files resolved.**"

        # ---- QUALITY GATE (factory layer) --------------------------------
        mode = str(kwargs.get("mode") or "").strip().lower()
        allow_scaffolds = _truthy(kwargs.get("allow_scaffolds"), False)
        reports = [factory_preflight(p) for p in picked]
        if mode == "check":
            lines = ["**Copilot Studio quality check** (no deploy):"]
            for r in reports:
                verdict = []
                verdict.append("rich seeds ✅" if r["has_seeds"] else
                               "no SYNTHETIC_DATA — factory will inject a "
                               "realistic seed at deploy time ⚠️")
                if r["scaffold_words"]:
                    verdict.append("names scaffold-triggering systems ("
                                   + ", ".join(r["scaffold_words"])
                                   + ") — live twin may import with a "
                                     "disabled flow unless a human binds a "
                                     "connection")
                lines.append(f"- `{Path(r['file']).name}`: "
                             + "; ".join(verdict))
            lines.append("")
            lines.append("Fields I would seed per agent: "
                         + "; ".join(f"{Path(r['file']).name}: "
                                     + ",".join(r["fields"][:6])
                                     for r in reports))
            return "\n".join(lines)
        blockers = [r for r in reports
                    if r["scaffold_words"] and not allow_scaffolds]
        prepped_dir = ARTIFACT_ROOT / "prepped"
        prepped_files, prep_notes = [], []
        for p in picked:
            newp, rep = factory_prep(p, prepped_dir)
            prepped_files.append(Path(newp))
            if rep.get("prepped"):
                did = []
                if not rep["has_seeds"]:
                    did.append("realistic SYNTHETIC_DATA seed")
                if rep.get("injected_binding"):
                    did.append("explicit Dataverse binding (CAPIR)")
                prep_notes.append(f"{Path(p).name}: injected "
                                  + " + ".join(did) + " (prepped copy)")
        picked = prepped_files
        if blockers and not allow_scaffolds:
            names = ", ".join(Path(r["file"]).name + " ("
                              + ",".join(r["scaffold_words"]) + ")"
                              for r in blockers)
            prep_notes.append("NOTE: scaffold-triggering system words left "
                              "as-is in: " + names + " — pass "
                              "allow_scaffolds=true to silence this note, or "
                              "reword the descriptions to name Microsoft "
                              "Dataverse for 100% activation.")
        # ------------------------------------------------------------------

        pipeline_url = (str(kwargs.get("pipeline_url") or "").strip()
                        or DEFAULT_PIPELINE_URL).rstrip("/")
        if not pipeline_url:
            return ("**Set the pipeline first:** pass pipeline_url=<your "
                    "RAPP Documents->Copilot Studio host> or export "
                    "RAPP_PIPELINE_URL. A local AUTH_DISABLED host needs no "
                    "token; hosted ones take bearer=/DCS_BEARER.")
        resource = (str(kwargs.get("resource") or "").strip()
                    or DEFAULT_RESOURCE).rstrip("/")
        if not resource:
            return ("**Set the target first:** pass resource=<https://yourorg"
                    ".crm.dynamics.com> or export RAPP_MCS_RESOURCE.")
        environment_id = (str(kwargs.get("environment_id") or "").strip()
                          or DEFAULT_ENVIRONMENT_ID)
        twin = (str(kwargs.get("twin") or "both").strip().lower()
                if str(kwargs.get("twin") or "both").strip().lower()
                in ("both", "demo", "live") else "both")
        dry_run = _truthy(kwargs.get("dry_run"), False)
        want_probe = _truthy(kwargs.get("probe"), True)

        stamp = time.strftime("%m%d%H%M") + uuid.uuid4().hex[:3]
        base = re.sub(r"[^A-Za-z0-9]", "", str(
            kwargs.get("solution_name") or picked[0].stem.title()))[:10] \
            or "RappAgents"
        solution_name = f"{base}{stamp}"
        prefix = re.sub(r"[^a-z]", "", str(
            kwargs.get("publisher_prefix") or "").lower())
        if prefix.startswith("mscrm"):
            return ("**Invalid publisher_prefix:** 'mscrm*' is reserved by "
                    "Dataverse — pick another prefix.")
        if len(prefix) < 2:
            prefix = "ad" + re.sub(r"[^a-z]", "", base.lower())[:6] or "adrapp"

        log = [*prep_notes,
               f"agents: {', '.join(p.stem for p in picked)}",
               f"solution: {solution_name} (prefix {prefix})",
               f"pipeline: {pipeline_url}", f"target: {resource}"]

        bearer, auth_error = self._pipeline_auth(pipeline_url,
                                                 kwargs.get("bearer"))
        if auth_error:
            return "**Blocked on auth:** " + auth_error

        # 1) MVP
        files = [str(p) for p in picked]
        mvp = _multipart(pipeline_url + "/mvp",
                         {"solution_name": solution_name,
                          "publisher_prefix": prefix,
                          "run_id": "autodeploy", "debug": "1"},
                         files, bearer)
        if mvp.get("status") != "mvp":
            return f"**MVP step failed:** {json.dumps(mvp)[:400]}"
        log.append(f"mvp: {mvp.get('title', '')[:80]}")

        # 2) Generate
        generated = _multipart(pipeline_url + "/pipeline",
                               {"solution_name": solution_name,
                                "publisher_prefix": prefix,
                                "topology": "flat",
                                "run_id": "autodeploy", "debug": "1",
                                "mvp_title": mvp.get("title", ""),
                                "mvp_statement": mvp.get("statement", "")},
                               files, bearer)
        if generated.get("status") != "generated":
            return f"**Generation failed:** {json.dumps(generated)[:400]}"

        examples = []
        for group in generated.get("demo_examples") or []:
            examples.extend(group.get("examples") or [])
        script = [e.get("text") for e in examples if e.get("text")]
        log.append(f"generated: "
                   f"{len(generated.get('agents_generated') or [])} "
                   f"agent file(s), "
                   f"{len(script)} guaranteed demo request(s)")

        outdir = ARTIFACT_ROOT / solution_name
        outdir.mkdir(parents=True, exist_ok=True)
        for key, fname in (("solution_b64", "live.zip"),
                           ("demo_solution_b64", "demo.zip")):
            if generated.get(key):
                (outdir / fname).write_bytes(
                    base64.b64decode(generated[key]))

        if dry_run:
            (outdir / "report.json").write_text(json.dumps(
                {"solution": solution_name, "script": script,
                 "log": log}, indent=2))
            return "\n".join(
                ["**Dry run complete — nothing imported.**", *log,
                 f"artifacts: {outdir}", "",
                 "**Demo script (click-in-order):**",
                 *[f"{i}. {s}" for i, s in enumerate(script, 1)]])

        # 3) Dataverse auth
        token, cred = self._dataverse_token(
            resource, str(kwargs.get("dataverse_token") or "").strip())
        if not token:
            return ("**Blocked on Dataverse auth:** no credential passed "
                    "WhoAmI for " + resource + ". Provide dataverse_token=, "
                    "or configure ~/.rapp_deploy_settings.json (service "
                    "principal), or `az login`.")
        log.append(f"dataverse auth: {cred}")

        # 4) Deploy + verify each requested twin
        plan = []
        if twin in ("both", "live"):
            plan.append(("LIVE twin", generated.get("solution_b64"),
                         generated.get("solution_name") or solution_name,
                         generated.get("bot_schemas") or [],
                         generated.get("workflow_ids") or {}))
        if twin in ("both", "demo"):
            plan.append(("Demo twin", generated.get("demo_solution_b64"),
                         generated.get("demo_solution_name")
                         or solution_name + "Demo",
                         generated.get("demo_bot_schemas") or [],
                         generated.get("demo_workflow_ids") or {}))
        deployed, twin_failures = [], []
        for label, b64, name, schemas, workflow_ids in plan:
            if not b64:
                log.append(f"{label}: not present in pipeline output — skipped")
                continue
            try:
                self._deploy_twin(pipeline_url, bearer, resource, token,
                                  label, b64, name, schemas, workflow_ids,
                                  log)
                # Demo twins carry no external connections and MUST activate;
                # live twins may hold scaffold connectors that stay Draft
                # until a connection is bound (pending_connection).
                self._verify_workflows(resource, token, workflow_ids, label,
                                       log, strict=(label != "LIVE twin"))
                deployed.append((label, name, schemas))
            except Exception as error:
                twin_failures.append(f"{label}: {error}")
                log.append(f"{label}: FAILED — {error}")

        if not deployed:
            return "\n".join(
                ["**Deploy failed** — no twin completed.", *log])

        # 5) Optional runtime probe of the demo twin's first example
        probe_result = None
        demo_schemas = next((s for lbl, _n, s in deployed
                             if lbl == "Demo twin" and s), None)
        if want_probe and demo_schemas and examples and environment_id:
            try:
                probe_result = self._probe_demo(
                    environment_id, demo_schemas[0], examples[0], log)
            except Exception as error:  # probe is evidence, not a gate
                log.append(f"probe: errored non-fatally: {error}")

        (outdir / "report.json").write_text(json.dumps(
            {"solution": solution_name, "resource": resource,
             "deployed": [{"twin": lbl, "solution": n, "schemas": s}
                          for lbl, n, s in deployed],
             "script": script, "probe": probe_result, "log": log},
            indent=2, ensure_ascii=False))

        lines = ["**Deployed to Copilot Studio.**", *log, "",
                 "**Demo script (click these in order):**",
                 *[f"{i}. {s}" for i, s in enumerate(script, 1)], "",
                 f"Open Copilot Studio -> environment for {resource} -> "
                 f"agents named after `{solution_name}`. "
                 f"Artifacts + report: {outdir}"]
        if probe_result and probe_result.get("passed"):
            lines.append("Live check: the demo twin answered its first "
                         "advertised example with its seeded record. ✅")
        return "\n".join(lines)




# === MCP new-shape engine (BlastBox two-solution) ===
# Embedded VERBATIM from RAPPtranscript2Prototype agents/mcs_new_shape.py +
# agents/mcp_framework.cs (byte-identical). This is the SAME generator proven
# end-to-end into kodyd365 (channel-less parents, schemaname/description
# clamps, thin skills). To resync: rerun scratchpad build_rar_mcp.py.
_MCP_GEN_B64 = "IiIiTmV3LXNoYXBlIChCbGFzdEJveCBwYXR0ZXJuKSBzb2x1dGlvbiBnZW5lcmF0b3I6IGZyb20gcXVhbGl0eS1jb250cmFjdAphZ2VudC5weSBmaWxlcyBlbWl0IE9ORSBpbmxpbmUtTUNQIGNvbm5lY3RvcnMgc29sdXRpb24gKyBPTkUgbmV3LWdlbmVyYXRpb24KYWdlbnRzIHNvbHV0aW9uIChwYXJlbnQgKyBjb25uZWN0ZWQgY2hpbGQ7IGV2ZXJ5IGFnZW50LnB5IHJpZGVzIGFzIGEgUHl0aG9uCnNraWxsIGJ1bmRsZTogZ2VuZXJhdGVkIFNLSUxMLm1kICsgdGhlIGFnZW50LnB5IGl0c2VsZiArIGEgQ0xJIHNoaW0pLgoKVGhlIGZyb3plbiBDIyBNQ1AgZnJhbWV3b3JrIChieXRlLWlkZW50aWNhbCBTZWN0aW9uIDIgb2YgdGhlIEJsYXN0Qm94CmNvbm5lY3RvcnMsICJQb3dlciBNQ1AgVGVtcGxhdGUgdjIuMSIpIGxpdmVzIGJlc2lkZSB0aGlzIG1vZHVsZSBhcwptY3BfZnJhbWV3b3JrLmNzLgoKRW50cnkgcG9pbnQ6IGdlbmVyYXRlX3N1aXRlKGFnZW50X2Rpciwgc3VpdGUsIHN1aXRlX2Rpc3BsYXksIG91dF9kaXIsIC4uLikKLT4gd3JpdGVzIDxTdWl0ZT5NY3BDb25uZWN0b3JzXzFfMF8wXzEuemlwICsgPFN1aXRlPk1jcEFnZW50c18xXzBfMF8xLnppcCArCm1hbmlmZXN0Lmpzb24gYW5kIHJldHVybnMgdGhlIG1hbmlmZXN0IGRpY3QuIiIiCmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKCmltcG9ydCBpbXBvcnRsaWIudXRpbAppbXBvcnQgaW8KaW1wb3J0IGpzb24KaW1wb3J0IHJlCmltcG9ydCBzdHJ1Y3QKaW1wb3J0IHV1aWQKaW1wb3J0IHppcGZpbGUKaW1wb3J0IHpsaWIKZnJvbSBwYXRobGliIGltcG9ydCBQYXRoCgpYTUxERUNMID0gJzw/eG1sIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9InV0Zi04Ij8+JwpDVF9OUyA9ICJodHRwOi8vc2NoZW1hcy5vcGVueG1sZm9ybWF0cy5vcmcvcGFja2FnZS8yMDA2L2NvbnRlbnQtdHlwZXMiCgoKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIHV0aWxpdGllcwpkZWYgX3NsdWcocywgc2VwPSIiKToKICAgIHJldHVybiByZS5zdWIociJbXmEtejAtOV0rIiwgc2VwLCBzdHIocykubG93ZXIoKSkuc3RyaXAoc2VwKQoKCmRlZiBfa2ViYWIocyk6CiAgICByZXR1cm4gX3NsdWcocywgIi0iKQoKCmRlZiBfY2xhbXBfc2NoZW1hKHMsIGxpbWl0PTEwMCk6CiAgICAiIiJib3QvYm90Y29tcG9uZW50IHNjaGVtYW5hbWVzIGhhdmUgYSBoYXJkIDEwMC1jaGFyIERhdGF2ZXJzZSBsaW1pdCDigJQKICAgIGFueXRoaW5nIGxvbmdlciBmYWlscyB0aGUgd2hvbGUgYWdlbnRzIGltcG9ydCAoImxlbmd0aCBvZiB0aGUgJ3NjaGVtYW5hbWUnCiAgICBhdHRyaWJ1dGUgLi4uIGV4Y2VlZGVkIikuIExvbmcgTExNLWF1dGhvcmVkIGNsYXNzL3N0ZW0gbmFtZXMgKGltYWdlIGFuZAogICAgbmFycmF0aXZlIHJvdXRlcykgY2FuIHB1c2ggY29tcG9zZWQgc2NoZW1hcyBwYXN0IGl0LiBEZXRlcm1pbmlzdGljOiBhbgogICAgb3ZlcmxvbmcgbmFtZSBrZWVwcyBpdHMgaGVhZCBhbmQgZ2FpbnMgYSB1dWlkNSB0YWlsLCBzbyByZWJ1aWxkcyBhcmUKICAgIGlkZW1wb3RlbnQgYW5kIHVuaXF1ZW5lc3Mgc3Vydml2ZXMgdGhlIGN1dC4iIiIKICAgIGlmIGxlbihzKSA8PSBsaW1pdDoKICAgICAgICByZXR1cm4gcwogICAgdGFpbCA9IHV1aWQudXVpZDUodXVpZC5OQU1FU1BBQ0VfVVJMLCAicmFwcC1tY3MyOiIgKyBzKS5oZXhbOjhdCiAgICByZXR1cm4gc1s6bGltaXQgLSBsZW4odGFpbCkgLSAxXS5yc3RyaXAoIi5fIikgKyAiXyIgKyB0YWlsCgoKZGVmIF9zdGFibGUobmFtZSwgbj02KToKICAgICIiIkRldGVybWluaXN0aWMgcHNldWRvLXJhbmRvbSBzdWZmaXggKHV1aWQ1KSBzbyByZWJ1aWxkcyBhcmUgaWRlbXBvdGVudC4iIiIKICAgIHJldHVybiB1dWlkLnV1aWQ1KHV1aWQuTkFNRVNQQUNFX1VSTCwgInJhcHAtbWNzMjoiICsgbmFtZSkuaGV4WzpuXQoKCmRlZiBfeG1sX2VzYyhzKToKICAgIHJldHVybiAoc3RyKHMpLnJlcGxhY2UoIiYiLCAiJmFtcDsiKS5yZXBsYWNlKCI8IiwgIiZsdDsiKQogICAgICAgICAgICAucmVwbGFjZSgiPiIsICImZ3Q7IikpCgoKZGVmIF9wbmdfaWNvbihyZ2I9KDAsIDEyMCwgMjEyKSwgc2l6ZT0xMDApOgogICAgIiIiTWluaW1hbCB2YWxpZCBzb2xpZC1jb2xvciBQTkcgKHN0ZGxpYiBvbmx5KSBmb3IgYm90IGljb25iYXNlNjQuIiIiCiAgICByYXcgPSBiIiIKICAgIHJvdyA9IGIiXHgwMCIgKyBieXRlcyhyZ2IpICogc2l6ZQogICAgZm9yIF8gaW4gcmFuZ2Uoc2l6ZSk6CiAgICAgICAgcmF3ICs9IHJvdwoKICAgIGRlZiBjaHVuayh0YWcsIGRhdGEpOgogICAgICAgIGMgPSBzdHJ1Y3QucGFjaygiPkkiLCBsZW4oZGF0YSkpICsgdGFnICsgZGF0YQogICAgICAgIHJldHVybiBjICsgc3RydWN0LnBhY2soIj5JIiwgemxpYi5jcmMzMih0YWcgKyBkYXRhKSAmIDB4RkZGRkZGRkYpCgogICAgaWhkciA9IHN0cnVjdC5wYWNrKCI+SUlCQkJCQiIsIHNpemUsIHNpemUsIDgsIDIsIDAsIDAsIDApCiAgICByZXR1cm4gKGIiXHg4OVBOR1xyXG5ceDFhXG4iICsgY2h1bmsoYiJJSERSIiwgaWhkcikKICAgICAgICAgICAgKyBjaHVuayhiIklEQVQiLCB6bGliLmNvbXByZXNzKHJhdykpICsgY2h1bmsoYiJJRU5EIiwgYiIiKSkKCgpkZWYgX2tleV9maWVsZChmaWVsZHMpOgogICAgZm9yIGYgaW4gZmllbGRzOgogICAgICAgIHRva3MgPSBzZXQocmUuc3ViKHIiKFthLXowLTldKShbQS1aXSkiLCByIlwxX1wyIiwgZikubG93ZXIoKQogICAgICAgICAgICAgICAgICAgLnNwbGl0KCJfIikpCiAgICAgICAgaWYgdG9rcyAmIHsiaWQiLCAicmVmIiwgInJlZmVyZW5jZSIsICJudW1iZXIifToKICAgICAgICAgICAgcmV0dXJuIGYKICAgIHJldHVybiBmaWVsZHNbMF0gaWYgZmllbGRzIGVsc2UgImlkIgoKCmRlZiBoYXJ2ZXN0X2FnZW50cyhhZ2VudF9kaXIpOgogICAgIiIiSW1wb3J0IGVhY2ggKl9hZ2VudC5weSAob3VyIG93biB0cnVzdGVkIHF1YWxpdHktY29udHJhY3QgZmlsZXMpIGFuZAogICAgcHVsbCBjbGFzcywgbWV0YWRhdGEsIFNZTlRIRVRJQ19EQVRBLCBUUklHR0VSUywgUkVTUE9OU0UgKyBzb3VyY2UuIiIiCiAgICBvdXQgPSBbXQogICAgZm9yIHAgaW4gc29ydGVkKFBhdGgoYWdlbnRfZGlyKS5nbG9iKCIqX2FnZW50LnB5IikpOgogICAgICAgIGlmIHAuc3RlbSA9PSAiYmFzaWNfYWdlbnQiOgogICAgICAgICAgICBjb250aW51ZQogICAgICAgIHNwZWMgPSBpbXBvcnRsaWIudXRpbC5zcGVjX2Zyb21fZmlsZV9sb2NhdGlvbigibV8iICsgcC5zdGVtLCBwKQogICAgICAgIG1vZCA9IGltcG9ydGxpYi51dGlsLm1vZHVsZV9mcm9tX3NwZWMoc3BlYykKICAgICAgICBzcGVjLmxvYWRlci5leGVjX21vZHVsZShtb2QpCiAgICAgICAgY2xzID0gbmV4dCh2IGZvciB2IGluIHZhcnMobW9kKS52YWx1ZXMoKQogICAgICAgICAgICAgICAgICAgaWYgaXNpbnN0YW5jZSh2LCB0eXBlKSBhbmQgdi5fX25hbWVfXyAhPSAiQmFzaWNBZ2VudCIKICAgICAgICAgICAgICAgICAgIGFuZCBoYXNhdHRyKHYsICJwZXJmb3JtIikpCiAgICAgICAgaW5zdCA9IGNscygpCiAgICAgICAgbWV0YSA9IGluc3QubWV0YWRhdGEKICAgICAgICByb3dzID0gW2RpY3QocikgZm9yIHIgaW4gKGdldGF0dHIoY2xzLCAiU1lOVEhFVElDX0RBVEEiLCBOb25lKSBvciBbXSkKICAgICAgICAgICAgICAgIGlmIGlzaW5zdGFuY2UociwgZGljdCldCiAgICAgICAgZmllbGRzID0gbGlzdChyb3dzWzBdKSBpZiByb3dzIGVsc2UgW10KICAgICAgICBvdXQuYXBwZW5kKHsKICAgICAgICAgICAgInBhdGgiOiBwLCAic291cmNlIjogcC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IiksCiAgICAgICAgICAgICJjbGFzc19uYW1lIjogY2xzLl9fbmFtZV9fLCAic3RlbSI6IHAuc3RlbSwKICAgICAgICAgICAgIm5hbWUiOiBtZXRhLmdldCgibmFtZSIpIG9yIGNscy5fX25hbWVfXywKICAgICAgICAgICAgImRlc2NyaXB0aW9uIjogc3RyKG1ldGEuZ2V0KCJkZXNjcmlwdGlvbiIpIG9yICIiKSwKICAgICAgICAgICAgInBhcmFtcyI6IChtZXRhLmdldCgicGFyYW1ldGVycyIpIG9yIHt9KS5nZXQoInByb3BlcnRpZXMiKSBvciB7fSwKICAgICAgICAgICAgInJvd3MiOiByb3dzLCAiZmllbGRzIjogZmllbGRzLCAia2V5IjogX2tleV9maWVsZChmaWVsZHMpLAogICAgICAgICAgICAidHJpZ2dlcnMiOiBsaXN0KGdldGF0dHIoY2xzLCAiVFJJR0dFUlMiLCBOb25lKSBvciBbXSksCiAgICAgICAgICAgICJyZXNwb25zZSI6IHN0cihnZXRhdHRyKGNscywgIlJFU1BPTlNFIiwgIiIpIG9yICIiKSwKICAgICAgICAgICAgImRhdGFzZXQiOiBfc2x1ZyhjbHMuX19uYW1lX18pLAogICAgICAgIH0pCiAgICByZXR1cm4gb3V0CgoKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0gY29ubmVjdG9yIGdlbgpBUElfREVGSU5JVElPTiA9IHsKICAgICJzd2FnZ2VyIjogIjIuMCIsCiAgICAiaW5mbyI6IHsidGl0bGUiOiAiIiwgImRlc2NyaXB0aW9uIjogIiIsICJ2ZXJzaW9uIjogIjEuMC4wIn0sCiAgICAiaG9zdCI6ICJwbGFjZWhvbGRlci5henVyZS1hcGltLm5ldCIsCiAgICAiYmFzZVBhdGgiOiAiL21jcCIsCiAgICAic2NoZW1lcyI6IFsiaHR0cHMiXSwKICAgICJjb25zdW1lcyI6IFsiYXBwbGljYXRpb24vanNvbiJdLAogICAgInByb2R1Y2VzIjogWyJhcHBsaWNhdGlvbi9qc29uIl0sCiAgICAicGF0aHMiOiB7Ii8iOiB7InBvc3QiOiB7CiAgICAgICAgInN1bW1hcnkiOiAiIiwgImRlc2NyaXB0aW9uIjogIiIsICJvcGVyYXRpb25JZCI6ICJJbnZva2VNQ1AiLAogICAgICAgICJ4LW1zLWFnZW50aWMtcHJvdG9jb2wiOiAibWNwLXN0cmVhbWFibGUtMS4wIiwKICAgICAgICAicGFyYW1ldGVycyI6IFtdLCAicmVzcG9uc2VzIjogeyIyMDAiOiB7ImRlc2NyaXB0aW9uIjogIk1DUCByZXNwb25zZSJ9fSwKICAgIH19fSwKICAgICJkZWZpbml0aW9ucyI6IHt9LCAicGFyYW1ldGVycyI6IHt9LCAicmVzcG9uc2VzIjoge30sICJzZWN1cml0eSI6IFtdLAogICAgInRhZ3MiOiBbXSwgInNlY3VyaXR5RGVmaW5pdGlvbnMiOiB7fSwKfQoKQVBJX1BST1BFUlRJRVMgPSAoJ3tcbiAgInByb3BlcnRpZXMiOiB7XG4gICAgImNvbm5lY3Rpb25QYXJhbWV0ZXJzIjoge30sXG4nCiAgICAgICAgICAgICAgICAgICcgICAgImljb25CcmFuZENvbG9yIjogIiMwMDdlZTUiLFxuICAgICJjYXBhYmlsaXRpZXMiOiBbXSxcbicKICAgICAgICAgICAgICAgICAgJyAgICAic2NyaXB0T3BlcmF0aW9ucyI6IFtdLFxuICAgICJwdWJsaXNoZXIiOiAiIixcbicKICAgICAgICAgICAgICAgICAgJyAgICAic3RhY2tPd25lciI6ICIiLFxuICAgICJwb2xpY3lUZW1wbGF0ZUluc3RhbmNlcyI6IFtdXG4nCiAgICAgICAgICAgICAgICAgICcgIH1cbn0nKQoKCmRlZiBfY3NfdmVyYmF0aW0ob2JqKToKICAgICIiIkpTT04g4oaSIEMjIHZlcmJhdGltLXN0cmluZyBsaXRlcmFsIGNvbnRlbnQgKHF1b3RlcyBkb3VibGVkKS4iIiIKICAgIHJldHVybiBqc29uLmR1bXBzKG9iaiwgZW5zdXJlX2FzY2lpPUZhbHNlLCBpbmRlbnQ9MikucmVwbGFjZSgnIicsICciIicpCgoKZGVmIGJ1aWxkX3NjcmlwdF9jc3goc3VpdGVfZGlzcGxheSwgc2VydmVyX2tlYmFiLCBhZ2VudHMsIGZyYW1ld29yayk6CiAgICAiIiJTZWN0aW9uIDEgKGdlbmVyYXRlZCkgKyBmcm96ZW4gU2VjdGlvbiAyLiIiIgogICAgdG9vbF9saW5lcyA9IFtdCiAgICBkYXRhX2xpbmVzID0gW10KICAgIGluc3RydWN0aW9ucyA9IFsKICAgICAgICAiVGhpcyBNQ1Agc2VydmVyIGNhcnJpZXMgdGhlIGNvbXBsZXRlIHN5bnRoZXRpYyAlcyBkYXRhc2V0LiIKICAgICAgICAlIHN1aXRlX2Rpc3BsYXksCiAgICAgICAgIkNhbGwgbGlzdF8qIGZpcnN0IHdoZW4gdGhlIHVzZXIgZ2l2ZXMgbm8gaWRlbnRpZmllciDigJQgbmV2ZXIgYXNrICIKICAgICAgICAiZm9yIGFuIGludGVybmFsIGlkOyBldmVyeSByZWNvcmQgaXMgb24gdGhpcyBzZXJ2ZXIuIiwKICAgIF0KICAgIGZvciBhIGluIGFnZW50czoKICAgICAgICBkcyA9ICJEYXRhXyIgKyBhWyJjbGFzc19uYW1lIl0KICAgICAgICBkYXRhX2xpbmVzLmFwcGVuZCgKICAgICAgICAgICAgIiAgICBwcml2YXRlIHN0YXRpYyByZWFkb25seSBKQXJyYXkgJXMgPSBKQXJyYXkuUGFyc2UoQFwiJXNcIik7IgogICAgICAgICAgICAlIChkcywgX2NzX3ZlcmJhdGltKGFbInJvd3MiXSkpKQogICAgICAgIGdldF9uYW1lID0gImdldF8iICsgYVsiZGF0YXNldCJdCiAgICAgICAgbGlzdF9uYW1lID0gImxpc3RfIiArIGFbImRhdGFzZXQiXQogICAgICAgIGtleSA9IGFbImtleSJdCiAgICAgICAgZGVzYyA9IGFbImRlc2NyaXB0aW9uIl0ucmVwbGFjZSgnIicsICInIilbOjQ4MF0KICAgICAgICBpbnN0cnVjdGlvbnMuYXBwZW5kKAogICAgICAgICAgICAiJXMgLyAlcyBzZXJ2ZTogJXMiICUgKGdldF9uYW1lLCBsaXN0X25hbWUsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZGVzY1s6MTYwXSkpCiAgICAgICAgdG9vbF9saW5lcy5hcHBlbmQoJycnCiAgICAgICAgaGFuZGxlci5BZGRUb29sKCIlKGxpc3QpcyIsCiAgICAgICAgICAgICJMaXN0IGV2ZXJ5IHJlY29yZCBiZWhpbmQgdGhlICUoY2xzKXMgY2FwYWJpbGl0eS4gJShkZXNjKXMgQ2FsbCB3aXRoIG5vIGFyZ3VtZW50cyB0byBzZWUgYWxsIHJlY29yZHMuIiwKICAgICAgICAgICAgc2NoZW1hQ29uZmlnOiBzID0+IHMuU3RyaW5nKCJmaWx0ZXIiLCAiT3B0aW9uYWwgY2FzZS1pbnNlbnNpdGl2ZSB0ZXh0IGZpbHRlciBtYXRjaGVkIGFnYWluc3QgZXZlcnkgZmllbGQuIE9taXQgdG8gcmV0dXJuIGFsbCByZWNvcmRzLiIpLAogICAgICAgICAgICBoYW5kbGVyOiBhc3luYyAoYXJncywgY3QpID0+CiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgIHZhciBmID0gKGFyZ3MuVmFsdWU8c3RyaW5nPigiZmlsdGVyIikgPz8gIiIpLlRyaW0oKS5Ub0xvd2VySW52YXJpYW50KCk7CiAgICAgICAgICAgICAgICBpZiAoc3RyaW5nLklzTnVsbE9yRW1wdHkoZikpCiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIG5ldyBKT2JqZWN0IHsgWyJjb3VudCJdID0gJShkcylzLkNvdW50LCBbIml0ZW1zIl0gPSBKQXJyYXkuUGFyc2UoJShkcylzLlRvU3RyaW5nKCkpIH07CiAgICAgICAgICAgICAgICB2YXIgaGl0cyA9IG5ldyBKQXJyYXkoKTsKICAgICAgICAgICAgICAgIGZvcmVhY2ggKHZhciByIGluICUoZHMpcykKICAgICAgICAgICAgICAgICAgICBpZiAoci5Ub1N0cmluZygpLlRvTG93ZXJJbnZhcmlhbnQoKS5Db250YWlucyhmKSkgaGl0cy5BZGQocik7CiAgICAgICAgICAgICAgICBpZiAoaGl0cy5Db3VudCA9PSAwKQogICAgICAgICAgICAgICAgICAgIHJldHVybiBuZXcgSk9iamVjdCB7IFsibWVzc2FnZSJdID0gIk5vICUoY2xzKXMgcmVjb3JkIG1hdGNoZXMgXFwiIiArIGYgKyAiXFwiLiBDYWxsICUobGlzdClzIHdpdGggbm8gZmlsdGVyIHRvIHNlZSBldmVyeSByZWNvcmQuIiB9OwogICAgICAgICAgICAgICAgcmV0dXJuIG5ldyBKT2JqZWN0IHsgWyJjb3VudCJdID0gaGl0cy5Db3VudCwgWyJpdGVtcyJdID0gaGl0cyB9OwogICAgICAgICAgICB9KTsKICAgICAgICBoYW5kbGVyLkFkZFRvb2woIiUoZ2V0KXMiLAogICAgICAgICAgICAiTG9vayB1cCBPTkUgJShjbHMpcyByZWNvcmQgYnkgaXRzICUoa2V5KXMgKGNhc2UtaW5zZW5zaXRpdmU7IGEgcGFydGlhbCBtYXRjaCBvbiBhbnkgbmFtZSBmaWVsZCBhbHNvIHdvcmtzKS4gUmV0dXJucyBldmVyeSBmaWVsZCBvZiB0aGUgcmVjb3JkLiIsCiAgICAgICAgICAgIHNjaGVtYUNvbmZpZzogcyA9PiBzLlN0cmluZygiJShrZXkpcyIsICJUaGUgcmVjb3JkIGtleSwgZS5nLiBcXCIlKGV4YW1wbGUpc1xcIi4gQSBwZXJzb24vY29tcGFueSBuYW1lIGFsc28gcmVzb2x2ZXMuIiwgcmVxdWlyZWQ6IHRydWUpLAogICAgICAgICAgICBoYW5kbGVyOiBhc3luYyAoYXJncywgY3QpID0+CiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgIHZhciBpZCA9IChhcmdzLlZhbHVlPHN0cmluZz4oIiUoa2V5KXMiKSA/PyAiIikuVHJpbSgpOwogICAgICAgICAgICAgICAgZm9yZWFjaCAodmFyIHIgaW4gJShkcylzKQogICAgICAgICAgICAgICAgICAgIGlmIChzdHJpbmcuRXF1YWxzKHJbIiUoa2V5KXMiXT8uVG9TdHJpbmcoKSwgaWQsIFN0cmluZ0NvbXBhcmlzb24uT3JkaW5hbElnbm9yZUNhc2UpKQogICAgICAgICAgICAgICAgICAgICAgICByZXR1cm4gKEpPYmplY3Qpci5EZWVwQ2xvbmUoKTsKICAgICAgICAgICAgICAgIGZvcmVhY2ggKHZhciByIGluICUoZHMpcykKICAgICAgICAgICAgICAgICAgICBpZiAoci5Ub1N0cmluZygpLlRvTG93ZXJJbnZhcmlhbnQoKS5Db250YWlucyhpZC5Ub0xvd2VySW52YXJpYW50KCkpICYmIGlkLkxlbmd0aCA+PSAzKQogICAgICAgICAgICAgICAgICAgICAgICByZXR1cm4gKEpPYmplY3Qpci5EZWVwQ2xvbmUoKTsKICAgICAgICAgICAgICAgIHRocm93IG5ldyBBcmd1bWVudEV4Y2VwdGlvbigiTm8gJShjbHMpcyByZWNvcmQgZm91bmQgZm9yIFxcIiIgKyBpZCArICJcXCIuIEtleXMgbG9vayBsaWtlIFxcIiUoZXhhbXBsZSlzXFwiOyBjYWxsICUobGlzdClzIHRvIHNlZSBldmVyeSByZWNvcmQuIik7CiAgICAgICAgICAgIH0pOycnJyAlIHsKICAgICAgICAgICAgImxpc3QiOiBsaXN0X25hbWUsICJnZXQiOiBnZXRfbmFtZSwgImNscyI6IGFbImNsYXNzX25hbWUiXSwKICAgICAgICAgICAgImRzIjogZHMsICJrZXkiOiBrZXksCiAgICAgICAgICAgICJkZXNjIjogZGVzY1s6MjAwXSwKICAgICAgICAgICAgImV4YW1wbGUiOiBzdHIoKGFbInJvd3MiXVswXS5nZXQoa2V5KSBpZiBhWyJyb3dzIl0gZWxzZSAiIikpLnJlcGxhY2UoJyInLCAiJyIpLAogICAgICAgIH0pCgogICAgc2VjdGlvbjEgPSAnJyd1c2luZyBTeXN0ZW07CnVzaW5nIFN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljOwp1c2luZyBTeXN0ZW0uTGlucTsKdXNpbmcgU3lzdGVtLk5ldDsKdXNpbmcgU3lzdGVtLk5ldC5IdHRwOwp1c2luZyBTeXN0ZW0uVGV4dDsKdXNpbmcgU3lzdGVtLlRocmVhZGluZzsKdXNpbmcgU3lzdGVtLlRocmVhZGluZy5UYXNrczsKdXNpbmcgTmV3dG9uc29mdC5Kc29uOwp1c2luZyBOZXd0b25zb2Z0Lkpzb24uTGlucTsKCnB1YmxpYyBjbGFzcyBTY3JpcHQgOiBTY3JpcHRCYXNlCnsKICAgIHByaXZhdGUgc3RhdGljIHJlYWRvbmx5IE1jcFNlcnZlck9wdGlvbnMgT3B0aW9ucyA9IG5ldyBNY3BTZXJ2ZXJPcHRpb25zCiAgICB7CiAgICAgICAgU2VydmVySW5mbyA9IG5ldyBNY3BTZXJ2ZXJJbmZvCiAgICAgICAgewogICAgICAgICAgICBOYW1lID0gIiUoc2VydmVyKXMiLAogICAgICAgICAgICBWZXJzaW9uID0gIjEuMC4wIiwKICAgICAgICAgICAgVGl0bGUgPSAiJSh0aXRsZSlzIiwKICAgICAgICAgICAgRGVzY3JpcHRpb24gPSAiSW5saW5lIE1DUCBzZXJ2ZXIgY2FycnlpbmcgdGhlIHN5bnRoZXRpYyAlKHRpdGxlKXMgZGF0YXNldC4gTm8gZXh0ZXJuYWwgaG9zdGluZzsgZXZlcnkgdG9vbCBhbnN3ZXJzIGZyb20gZW1iZWRkZWQgZGF0YS4iCiAgICAgICAgfSwKICAgICAgICBQcm90b2NvbFZlcnNpb24gPSAiMjAyNS0xMS0yNSIsCiAgICAgICAgQ2FwYWJpbGl0aWVzID0gbmV3IE1jcENhcGFiaWxpdGllcyB7IFRvb2xzID0gdHJ1ZSB9LAogICAgICAgIEluc3RydWN0aW9ucyA9IEAiJShpbnN0cnVjdGlvbnMpcyIKICAgIH07CgogICAgcHVibGljIG92ZXJyaWRlIGFzeW5jIFRhc2s8SHR0cFJlc3BvbnNlTWVzc2FnZT4gRXhlY3V0ZUFzeW5jKCkKICAgIHsKICAgICAgICB2YXIgaGFuZGxlciA9IG5ldyBNY3BSZXF1ZXN0SGFuZGxlcihPcHRpb25zKTsKICAgICAgICBSZWdpc3RlckNhcGFiaWxpdGllcyhoYW5kbGVyKTsKICAgICAgICB2YXIgYm9keSA9IGF3YWl0IHRoaXMuQ29udGV4dC5SZXF1ZXN0LkNvbnRlbnQuUmVhZEFzU3RyaW5nQXN5bmMoKS5Db25maWd1cmVBd2FpdChmYWxzZSk7CiAgICAgICAgdmFyIHJlc3VsdCA9IGF3YWl0IGhhbmRsZXIuSGFuZGxlQXN5bmMoYm9keSwgdGhpcy5DYW5jZWxsYXRpb25Ub2tlbikuQ29uZmlndXJlQXdhaXQoZmFsc2UpOwogICAgICAgIHJldHVybiBuZXcgSHR0cFJlc3BvbnNlTWVzc2FnZShIdHRwU3RhdHVzQ29kZS5PSykKICAgICAgICB7IENvbnRlbnQgPSBuZXcgU3RyaW5nQ29udGVudChyZXN1bHQsIEVuY29kaW5nLlVURjgsICJhcHBsaWNhdGlvbi9qc29uIikgfTsKICAgIH0KCiUoZGF0YSlzCgogICAgcHJpdmF0ZSB2b2lkIFJlZ2lzdGVyQ2FwYWJpbGl0aWVzKE1jcFJlcXVlc3RIYW5kbGVyIGhhbmRsZXIpCiAgICB7JSh0b29scylzCiAgICB9Cn0KCicnJyAlIHsKICAgICAgICAic2VydmVyIjogc2VydmVyX2tlYmFiLCAidGl0bGUiOiBzdWl0ZV9kaXNwbGF5LAogICAgICAgICJpbnN0cnVjdGlvbnMiOiAiICIuam9pbihpbnN0cnVjdGlvbnMpLnJlcGxhY2UoJyInLCAnIiInKSwKICAgICAgICAiZGF0YSI6ICJcbiIuam9pbihkYXRhX2xpbmVzKSwKICAgICAgICAidG9vbHMiOiAiIi5qb2luKHRvb2xfbGluZXMpLAogICAgfQogICAgcmV0dXJuIHNlY3Rpb24xICsgZnJhbWV3b3JrCgoKZGVmIGJ1aWxkX2Nvbm5lY3RvcnNfemlwKHN1aXRlLCBzdWl0ZV9kaXNwbGF5LCBwcmVmaXgsIGFnZW50cywgZnJhbWV3b3JrLAogICAgICAgICAgICAgICAgICAgICAgICAgb3V0X3BhdGgsIHB1Ymxpc2hlcik6CiAgICAiIiJPbmUgaW5saW5lLU1DUCBjb25uZWN0b3IgaW4gaXRzIG93biBzb2x1dGlvbiB6aXAuIiIiCiAgICBjb25uX2Rpc3BsYXkgPSBzdWl0ZV9kaXNwbGF5ICsgIiBEYXRhIE1DUCIKICAgIGNvbm5fc2NoZW1hID0gcHJlZml4ICsgIl8iICsgX2tlYmFiKGNvbm5fZGlzcGxheSkucmVwbGFjZSgiLSIsICItMjAiKQogICAgY29ubl9pZCA9IHN0cih1dWlkLnV1aWQ1KHV1aWQuTkFNRVNQQUNFX1VSTCwgInJhcHAtbWNzMi1jb25uOiIgKyBzdWl0ZSkpCiAgICBzZXJ2ZXJfa2ViYWIgPSBfa2ViYWIoY29ubl9kaXNwbGF5KQogICAgYXBpID0ganNvbi5sb2Fkcyhqc29uLmR1bXBzKEFQSV9ERUZJTklUSU9OKSkKICAgIHRvb2xzID0gc29ydGVkKHQgZm9yIGEgaW4gYWdlbnRzCiAgICAgICAgICAgICAgICAgICBmb3IgdCBpbiAoImdldF8iICsgYVsiZGF0YXNldCJdLCAibGlzdF8iICsgYVsiZGF0YXNldCJdKSkKICAgIGFwaVsiaW5mbyJdWyJ0aXRsZSJdID0gY29ubl9kaXNwbGF5CiAgICAjIENvbm5lY3RvckJhc2UuRGVzY3JpcHRpb24gaXMgYSAyNTYtY2hhciBTUUwgY29sdW1uOiBpbXBvcnRpbmcgYW55dGhpbmcKICAgICMgbG9uZ2VyIHRoYW4gdGhhdCBmYWlscyB0aGUgd2hvbGUgc29sdXRpb24gKCJTdHJpbmcgb3IgYmluYXJ5IGRhdGEgd291bGQKICAgICMgYmUgdHJ1bmNhdGVkIikuIExvbmcgTExNLWF1dGhvcmVkIGRhdGFzZXQgbmFtZXMgKGltYWdlL25hcnJhdGl2ZSByb3V0ZXMpCiAgICAjIGNhbiBwdXNoIHRoZSB0b29sIGxpc3QgcGFzdCBpdCDigJQgZmFsbCBiYWNrIHRvIGEgdG9vbCBDT1VOVCwgdGhlbiBjbGFtcC4KICAgIGRlc2MgPSAoIlN5bnRoZXRpYyAlcyBkYXRhIHNlcnZlZCBhcyBhbiBpbmxpbmUgTUNQIHNlcnZlci4gVG9vbHM6ICVzLiBSdW5zICIKICAgICAgICAgICAgImVudGlyZWx5IGluc2lkZSB0aGUgY29ubmVjdG9yIOKAlCBubyBleHRlcm5hbCBNQ1Agc2VydmVyIG5lZWRlZC4iCiAgICAgICAgICAgICUgKHN1aXRlX2Rpc3BsYXksICIsICIuam9pbih0b29scykpKQogICAgaWYgbGVuKGRlc2MpID4gMjMwOgogICAgICAgIGRlc2MgPSAoIlN5bnRoZXRpYyAlcyBkYXRhIHNlcnZlZCBhcyBhbiBpbmxpbmUgTUNQIHNlcnZlciAoJWQgdG9vbHMpLiAiCiAgICAgICAgICAgICAgICAiUnVucyBlbnRpcmVseSBpbnNpZGUgdGhlIGNvbm5lY3RvciDigJQgbm8gZXh0ZXJuYWwgTUNQIHNlcnZlciAiCiAgICAgICAgICAgICAgICAibmVlZGVkLiIgJSAoc3VpdGVfZGlzcGxheSwgbGVuKHRvb2xzKSkpWzoyMzBdCiAgICBhcGlbImluZm8iXVsiZGVzY3JpcHRpb24iXSA9IGRlc2MKICAgIGFwaVsicGF0aHMiXVsiLyJdWyJwb3N0Il1bInN1bW1hcnkiXSA9IGNvbm5fZGlzcGxheSArICIgU2VydmVyIgogICAgYXBpWyJwYXRocyJdWyIvIl1bInBvc3QiXVsiZGVzY3JpcHRpb24iXSA9ICgKICAgICAgICAiTUNQIHNlcnZlciBmb3IgJXMuIFRvb2xzOiAlcy4iICUgKHN1aXRlX2Rpc3BsYXksICIsICIuam9pbih0b29scykpKQogICAgY3N4ID0gYnVpbGRfc2NyaXB0X2NzeChzdWl0ZV9kaXNwbGF5LCBzZXJ2ZXJfa2ViYWIsIGFnZW50cywgZnJhbWV3b3JrKQoKICAgIGNvbm5lY3Rvcl94bWwgPSAiXG4iLmpvaW4oWwogICAgICAgIFhNTERFQ0wsCiAgICAgICAgJzxDb25uZWN0b3IgeG1sbnM6eHNpPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZSI+JywKICAgICAgICAiICA8Y29ubmVjdG9yaWQ+JXM8L2Nvbm5lY3RvcmlkPiIgJSBjb25uX2lkLAogICAgICAgICIgIDxkZXNjcmlwdGlvbj4lczwvZGVzY3JpcHRpb24+IiAlIF94bWxfZXNjKGFwaVsiaW5mbyJdWyJkZXNjcmlwdGlvbiJdKSwKICAgICAgICAiICA8ZGlzcGxheW5hbWU+JXM8L2Rpc3BsYXluYW1lPiIgJSBfeG1sX2VzYyhjb25uX2Rpc3BsYXkpLAogICAgICAgICIgIDxpY29uYnJhbmRjb2xvcj4jMDA3ZWU1PC9pY29uYnJhbmRjb2xvcj4iLAogICAgICAgICIgIDxuYW1lPiVzPC9uYW1lPiIgJSBjb25uX3NjaGVtYSwKICAgICAgICAiICA8Y29ubmVjdG9ydHlwZT4xPC9jb25uZWN0b3J0eXBlPiIsCiAgICAgICAgIiAgPHNjcmlwdG9wZXJhdGlvbnM+W108L3NjcmlwdG9wZXJhdGlvbnM+IiwKICAgICAgICAiICA8b3BlbmFwaWRlZmluaXRpb24+L0Nvbm5lY3Rvci8lc19vcGVuYXBpZGVmaW5pdGlvbi5qc29uPC9vcGVuYXBpZGVmaW5pdGlvbj4iICUgY29ubl9zY2hlbWEsCiAgICAgICAgIiAgPGNvbm5lY3Rpb25wYXJhbWV0ZXJzPi9Db25uZWN0b3IvJXNfY29ubmVjdGlvbnBhcmFtZXRlcnMuanNvbjwvY29ubmVjdGlvbnBhcmFtZXRlcnM+IiAlIGNvbm5fc2NoZW1hLAogICAgICAgICIgIDxwb2xpY3l0ZW1wbGF0ZWluc3RhbmNlcz4vQ29ubmVjdG9yLyVzX3BvbGljeXRlbXBsYXRlaW5zdGFuY2VzLmpzb248L3BvbGljeXRlbXBsYXRlaW5zdGFuY2VzPiIgJSBjb25uX3NjaGVtYSwKICAgICAgICAiICA8Y3VzdG9tY29kZWJsb2Jjb250ZW50Pi9Db25uZWN0b3IvJXNfY3VzdG9tY29kZWJsb2Jjb250ZW50LmNzeDwvY3VzdG9tY29kZWJsb2Jjb250ZW50PiIgJSBjb25uX3NjaGVtYSwKICAgICAgICAiPC9Db25uZWN0b3I+IiwKICAgIF0pCiAgICBjdXN0b21pemF0aW9ucyA9ICJcbiIuam9pbihbCiAgICAgICAgWE1MREVDTCwKICAgICAgICAnPEltcG9ydEV4cG9ydFhtbCB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIj4nLAogICAgICAgICIgIDxFbnRpdGllcyAvPiIsICIgIDxSb2xlcyAvPiIsICIgIDxXb3JrZmxvd3MgLz4iLAogICAgICAgICIgIDxGaWVsZFNlY3VyaXR5UHJvZmlsZXMgLz4iLCAiICA8VGVtcGxhdGVzIC8+IiwgIiAgPEVudGl0eU1hcHMgLz4iLAogICAgICAgICIgIDxFbnRpdHlSZWxhdGlvbnNoaXBzIC8+IiwgIiAgPE9yZ2FuaXphdGlvblNldHRpbmdzIC8+IiwKICAgICAgICAiICA8b3B0aW9uc2V0cyAvPiIsICIgIDxDdXN0b21Db250cm9scyAvPiIsCiAgICAgICAgIiAgPEVudGl0eURhdGFQcm92aWRlcnMgLz4iLAogICAgICAgICIgIDxDb25uZWN0b3JzPiIsCiAgICAgICAgIlxuIi5qb2luKCIgICAgIiArIGwgZm9yIGwgaW4gY29ubmVjdG9yX3htbC5zcGxpdGxpbmVzKClbMTpdKSwKICAgICAgICAiICA8L0Nvbm5lY3RvcnM+IiwKICAgICAgICAiICA8TGFuZ3VhZ2VzPiIsICIgICAgPExhbmd1YWdlPjEwMzM8L0xhbmd1YWdlPiIsICIgIDwvTGFuZ3VhZ2VzPiIsCiAgICAgICAgIjwvSW1wb3J0RXhwb3J0WG1sPiIsCiAgICBdKQogICAgc29sdXRpb24gPSBfc29sdXRpb25feG1sKAogICAgICAgIHVuaXF1ZT1zdWl0ZSArICJNY3BDb25uZWN0b3JzIiwgZGlzcGxheT1zdWl0ZV9kaXNwbGF5ICsgIiBNQ1AgQ29ubmVjdG9ycyIsCiAgICAgICAgcHVibGlzaGVyPXB1Ymxpc2hlciwKICAgICAgICByb290cz0nICAgIDxSb290Q29tcG9uZW50IHR5cGU9IjM3MiIgaWQ9Inslc30iIHNjaGVtYU5hbWU9IiVzIiBiZWhhdmlvcj0iMCIgLz4nCiAgICAgICAgICAgICAgJSAoY29ubl9pZCwgY29ubl9zY2hlbWEpKQogICAgY29udGVudF90eXBlcyA9ICgKICAgICAgICAn77u/JyArIFhNTERFQ0wgKwogICAgICAgICc8VHlwZXMgeG1sbnM9IiVzIj4nCiAgICAgICAgJzxEZWZhdWx0IEV4dGVuc2lvbj0ieG1sIiBDb250ZW50VHlwZT0iYXBwbGljYXRpb24vb2N0ZXQtc3RyZWFtIiAvPicKICAgICAgICAnPERlZmF1bHQgRXh0ZW5zaW9uPSJqc29uIiBDb250ZW50VHlwZT0iYXBwbGljYXRpb24vb2N0ZXQtc3RyZWFtIiAvPicKICAgICAgICAnPERlZmF1bHQgRXh0ZW5zaW9uPSJjc3giIENvbnRlbnRUeXBlPSJhcHBsaWNhdGlvbi9vY3RldC1zdHJlYW0iIC8+JwogICAgICAgICc8L1R5cGVzPicgJSBDVF9OUykKICAgIHdpdGggemlwZmlsZS5aaXBGaWxlKG91dF9wYXRoLCAidyIsIHppcGZpbGUuWklQX0RFRkxBVEVEKSBhcyB6OgogICAgICAgIHoud3JpdGVzdHIoIltDb250ZW50X1R5cGVzXS54bWwiLCBjb250ZW50X3R5cGVzKQogICAgICAgIHoud3JpdGVzdHIoInNvbHV0aW9uLnhtbCIsIHNvbHV0aW9uKQogICAgICAgIHoud3JpdGVzdHIoImN1c3RvbWl6YXRpb25zLnhtbCIsIGN1c3RvbWl6YXRpb25zKQogICAgICAgIHoud3JpdGVzdHIoIkNvbm5lY3Rvci8lc19vcGVuYXBpZGVmaW5pdGlvbi5qc29uIiAlIGNvbm5fc2NoZW1hLAogICAgICAgICAgICAgICAgICAganNvbi5kdW1wcyhhcGksIGluZGVudD0yKSkKICAgICAgICB6LndyaXRlc3RyKCJDb25uZWN0b3IvJXNfY29ubmVjdGlvbnBhcmFtZXRlcnMuanNvbiIgJSBjb25uX3NjaGVtYSwgInt9IikKICAgICAgICB6LndyaXRlc3RyKCJDb25uZWN0b3IvJXNfcG9saWN5dGVtcGxhdGVpbnN0YW5jZXMuanNvbiIgJSBjb25uX3NjaGVtYSwgIltdIikKICAgICAgICB6LndyaXRlc3RyKCJDb25uZWN0b3IvJXNfY3VzdG9tY29kZWJsb2Jjb250ZW50LmNzeCIgJSBjb25uX3NjaGVtYSwgY3N4KQogICAgcmV0dXJuIHsic2NoZW1hIjogY29ubl9zY2hlbWEsICJpZCI6IGNvbm5faWQsICJkaXNwbGF5IjogY29ubl9kaXNwbGF5LAogICAgICAgICAgICAidG9vbHMiOiB0b29sc30KCgpkZWYgX3NvbHV0aW9uX3htbCh1bmlxdWUsIGRpc3BsYXksIHB1Ymxpc2hlciwgcm9vdHM9IiIpOgogICAgcCA9IHB1Ymxpc2hlcgogICAgcmV0dXJuICJcbiIuam9pbihbCiAgICAgICAgWE1MREVDTCwKICAgICAgICAnPEltcG9ydEV4cG9ydFhtbCB2ZXJzaW9uPSI5LjIuMjYwNjMuMTMzIiBTb2x1dGlvblBhY2thZ2VWZXJzaW9uPSI5LjIiICcKICAgICAgICAnbGFuZ3VhZ2Vjb2RlPSIxMDMzIiBnZW5lcmF0ZWRCeT0iQ3JtTGl2ZSIgJwogICAgICAgICd4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIj4nLAogICAgICAgICIgIDxTb2x1dGlvbk1hbmlmZXN0PiIsCiAgICAgICAgIiAgICA8VW5pcXVlTmFtZT4lczwvVW5pcXVlTmFtZT4iICUgdW5pcXVlLAogICAgICAgICcgICAgPExvY2FsaXplZE5hbWVzPjxMb2NhbGl6ZWROYW1lIGRlc2NyaXB0aW9uPSIlcyIgbGFuZ3VhZ2Vjb2RlPSIxMDMzIiAvPjwvTG9jYWxpemVkTmFtZXM+JwogICAgICAgICUgX3htbF9lc2MoZGlzcGxheSksCiAgICAgICAgIiAgICA8RGVzY3JpcHRpb25zIC8+IiwKICAgICAgICAiICAgIDxWZXJzaW9uPjEuMC4wLjE8L1ZlcnNpb24+IiwKICAgICAgICAiICAgIDxNYW5hZ2VkPjA8L01hbmFnZWQ+IiwKICAgICAgICAiICAgIDxQdWJsaXNoZXI+IiwKICAgICAgICAiICAgICAgPFVuaXF1ZU5hbWU+JXM8L1VuaXF1ZU5hbWU+IiAlIHBbInVuaXF1ZSJdLAogICAgICAgICcgICAgICA8TG9jYWxpemVkTmFtZXM+PExvY2FsaXplZE5hbWUgZGVzY3JpcHRpb249IiVzIiBsYW5ndWFnZWNvZGU9IjEwMzMiIC8+PC9Mb2NhbGl6ZWROYW1lcz4nCiAgICAgICAgJSBfeG1sX2VzYyhwWyJkaXNwbGF5Il0pLAogICAgICAgICIgICAgICA8RGVzY3JpcHRpb25zIC8+IiwKICAgICAgICAiICAgICAgPEVNYWlsQWRkcmVzcyB4c2k6bmlsPVwidHJ1ZVwiPjwvRU1haWxBZGRyZXNzPiIsCiAgICAgICAgIiAgICAgIDxTdXBwb3J0aW5nV2Vic2l0ZVVybCB4c2k6bmlsPVwidHJ1ZVwiPjwvU3VwcG9ydGluZ1dlYnNpdGVVcmw+IiwKICAgICAgICAiICAgICAgPEN1c3RvbWl6YXRpb25QcmVmaXg+JXM8L0N1c3RvbWl6YXRpb25QcmVmaXg+IiAlIHBbInByZWZpeCJdLAogICAgICAgICIgICAgICA8Q3VzdG9taXphdGlvbk9wdGlvblZhbHVlUHJlZml4PiVzPC9DdXN0b21pemF0aW9uT3B0aW9uVmFsdWVQcmVmaXg+IgogICAgICAgICUgcFsib3B0aW9udmFsdWUiXSwKICAgICAgICAiICAgICAgPEFkZHJlc3Nlcz4iLAogICAgICAgICcgICAgICAgIDxBZGRyZXNzPjxBZGRyZXNzTnVtYmVyPjE8L0FkZHJlc3NOdW1iZXI+PEFkZHJlc3NUeXBlQ29kZSB4c2k6bmlsPSJ0cnVlIj48L0FkZHJlc3NUeXBlQ29kZT48Q2l0eSB4c2k6bmlsPSJ0cnVlIj48L0NpdHk+PENvdW50eSB4c2k6bmlsPSJ0cnVlIj48L0NvdW50eT48Q291bnRyeSB4c2k6bmlsPSJ0cnVlIj48L0NvdW50cnk+PEZheCB4c2k6bmlsPSJ0cnVlIj48L0ZheD48RnJlaWdodFRlcm1zQ29kZSB4c2k6bmlsPSJ0cnVlIj48L0ZyZWlnaHRUZXJtc0NvZGU+PEltcG9ydFNlcXVlbmNlTnVtYmVyIHhzaTpuaWw9InRydWUiPjwvSW1wb3J0U2VxdWVuY2VOdW1iZXI+PExhdGl0dWRlIHhzaTpuaWw9InRydWUiPjwvTGF0aXR1ZGU+PExpbmUxIHhzaTpuaWw9InRydWUiPjwvTGluZTE+PExpbmUyIHhzaTpuaWw9InRydWUiPjwvTGluZTI+PExpbmUzIHhzaTpuaWw9InRydWUiPjwvTGluZTM+PExvbmdpdHVkZSB4c2k6bmlsPSJ0cnVlIj48L0xvbmdpdHVkZT48TmFtZSB4c2k6bmlsPSJ0cnVlIj48L05hbWU+PFBvc3RhbENvZGUgeHNpOm5pbD0idHJ1ZSI+PC9Qb3N0YWxDb2RlPjxQb3N0T2ZmaWNlQm94IHhzaTpuaWw9InRydWUiPjwvUG9zdE9mZmljZUJveD48UHJpbWFyeUNvbnRhY3ROYW1lIHhzaTpuaWw9InRydWUiPjwvUHJpbWFyeUNvbnRhY3ROYW1lPjxTaGlwcGluZ01ldGhvZENvZGUgeHNpOm5pbD0idHJ1ZSI+PC9TaGlwcGluZ01ldGhvZENvZGU+PFN0YXRlT3JQcm92aW5jZSB4c2k6bmlsPSJ0cnVlIj48L1N0YXRlT3JQcm92aW5jZT48VGVsZXBob25lMSB4c2k6bmlsPSJ0cnVlIj48L1RlbGVwaG9uZTE+PFRlbGVwaG9uZTIgeHNpOm5pbD0idHJ1ZSI+PC9UZWxlcGhvbmUyPjxUZWxlcGhvbmUzIHhzaTpuaWw9InRydWUiPjwvVGVsZXBob25lMz48VVBTWm9uZSB4c2k6bmlsPSJ0cnVlIj48L1VQU1pvbmU+PFVUQ09mZnNldCB4c2k6bmlsPSJ0cnVlIj48L1VUQ09mZnNldD48L0FkZHJlc3M+JywKICAgICAgICAnICAgICAgICA8QWRkcmVzcz48QWRkcmVzc051bWJlcj4yPC9BZGRyZXNzTnVtYmVyPjxBZGRyZXNzVHlwZUNvZGUgeHNpOm5pbD0idHJ1ZSI+PC9BZGRyZXNzVHlwZUNvZGU+PENpdHkgeHNpOm5pbD0idHJ1ZSI+PC9DaXR5PjxDb3VudHkgeHNpOm5pbD0idHJ1ZSI+PC9Db3VudHk+PENvdW50cnkgeHNpOm5pbD0idHJ1ZSI+PC9Db3VudHJ5PjxGYXggeHNpOm5pbD0idHJ1ZSI+PC9GYXg+PEZyZWlnaHRUZXJtc0NvZGUgeHNpOm5pbD0idHJ1ZSI+PC9GcmVpZ2h0VGVybXNDb2RlPjxJbXBvcnRTZXF1ZW5jZU51bWJlciB4c2k6bmlsPSJ0cnVlIj48L0ltcG9ydFNlcXVlbmNlTnVtYmVyPjxMYXRpdHVkZSB4c2k6bmlsPSJ0cnVlIj48L0xhdGl0dWRlPjxMaW5lMSB4c2k6bmlsPSJ0cnVlIj48L0xpbmUxPjxMaW5lMiB4c2k6bmlsPSJ0cnVlIj48L0xpbmUyPjxMaW5lMyB4c2k6bmlsPSJ0cnVlIj48L0xpbmUzPjxMb25naXR1ZGUgeHNpOm5pbD0idHJ1ZSI+PC9Mb25naXR1ZGU+PE5hbWUgeHNpOm5pbD0idHJ1ZSI+PC9OYW1lPjxQb3N0YWxDb2RlIHhzaTpuaWw9InRydWUiPjwvUG9zdGFsQ29kZT48UG9zdE9mZmljZUJveCB4c2k6bmlsPSJ0cnVlIj48L1Bvc3RPZmZpY2VCb3g+PFByaW1hcnlDb250YWN0TmFtZSB4c2k6bmlsPSJ0cnVlIj48L1ByaW1hcnlDb250YWN0TmFtZT48U2hpcHBpbmdNZXRob2RDb2RlIHhzaTpuaWw9InRydWUiPjwvU2hpcHBpbmdNZXRob2RDb2RlPjxTdGF0ZU9yUHJvdmluY2UgeHNpOm5pbD0idHJ1ZSI+PC9TdGF0ZU9yUHJvdmluY2U+PFRlbGVwaG9uZTEgeHNpOm5pbD0idHJ1ZSI+PC9UZWxlcGhvbmUxPjxUZWxlcGhvbmUyIHhzaTpuaWw9InRydWUiPjwvVGVsZXBob25lMj48VGVsZXBob25lMyB4c2k6bmlsPSJ0cnVlIj48L1RlbGVwaG9uZTM+PFVQU1pvbmUgeHNpOm5pbD0idHJ1ZSI+PC9VUFNab25lPjxVVENPZmZzZXQgeHNpOm5pbD0idHJ1ZSI+PC9VVENPZmZzZXQ+PC9BZGRyZXNzPicsCiAgICAgICAgIiAgICAgIDwvQWRkcmVzc2VzPiIsCiAgICAgICAgIiAgICA8L1B1Ymxpc2hlcj4iLAogICAgICAgICIgICAgPFJvb3RDb21wb25lbnRzPiVzPC9Sb290Q29tcG9uZW50cz4iICUgKAogICAgICAgICAgICAoIlxuIiArIHJvb3RzICsgIlxuICAgICIpIGlmIHJvb3RzIGVsc2UgIiIpLAogICAgICAgICIgICAgPE1pc3NpbmdEZXBlbmRlbmNpZXMgLz4iLAogICAgICAgICIgIDwvU29sdXRpb25NYW5pZmVzdD4iLAogICAgICAgICI8L0ltcG9ydEV4cG9ydFhtbD4iLAogICAgXSkKCmltcG9ydCBiYXNlNjQKCmRlZiBfc3RyaXBfZGF0YV9saXRlcmFscyhzb3VyY2UpOgogICAgIiIiUFJPRFVDVElPTi1TSEFQRSB0cmFuc2Zvcm06IGJsYW5rIGV2ZXJ5IG1vZHVsZS1sZXZlbCBsaXN0LW9mLWRpY3RzIC8KICAgIGRpY3Qtb2YtZGljdHMgbGl0ZXJhbCAodGhlIGVtYmVkZGVkIGNhbm9uKSBzbyB0aGUgc2tpbGwgc2hpcHMgYXMgUFVSRQogICAgbG9naWMuIFJldHVybnMgKHN0cmlwcGVkX3NvdXJjZSwgW2JsYW5rZWQgbmFtZXNdKS4gVGhlIE1DUCBjb25uZWN0b3IgaXMKICAgIHRoZW4gdGhlIHNpbmdsZSBzb3VyY2Ugb2YgdHJ1dGg7IHRoZSBDTEkgc2hpbSByZS1pbmplY3RzIGZldGNoZWQgcmVjb3JkcwogICAgYXQgcnVudGltZSB2aWEgLS1kYXRhLWpzb24uIiIiCiAgICBpbXBvcnQgYXN0IGFzIF9hc3QKICAgIHRyZWUgPSBfYXN0LnBhcnNlKHNvdXJjZSkKICAgIHNwYW5zLCBuYW1lcyA9IFtdLCBbXQoKICAgIGRlZiBfc2Nhbihib2R5LCBpbmRlbnQpOgogICAgICAgIGZvciBub2RlIGluIGJvZHk6CiAgICAgICAgICAgIGlmIGlzaW5zdGFuY2Uobm9kZSwgX2FzdC5DbGFzc0RlZik6CiAgICAgICAgICAgICAgICBfc2Nhbihub2RlLmJvZHksIGluZGVudCArIDQpCiAgICAgICAgICAgICAgICBjb250aW51ZQogICAgICAgICAgICBpZiBub3QgaXNpbnN0YW5jZShub2RlLCBfYXN0LkFzc2lnbikgb3IgbGVuKG5vZGUudGFyZ2V0cykgIT0gMToKICAgICAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgICAgIHRndCA9IG5vZGUudGFyZ2V0c1swXQogICAgICAgICAgICBpZiBub3QgaXNpbnN0YW5jZSh0Z3QsIF9hc3QuTmFtZSk6CiAgICAgICAgICAgICAgICBjb250aW51ZQogICAgICAgICAgICB2ID0gbm9kZS52YWx1ZQogICAgICAgICAgICBpc19yb3dzID0gKGlzaW5zdGFuY2UodiwgX2FzdC5MaXN0KSBhbmQgdi5lbHRzCiAgICAgICAgICAgICAgICAgICAgICAgYW5kIGFsbChpc2luc3RhbmNlKGUsIF9hc3QuRGljdCkgZm9yIGUgaW4gdi5lbHRzKSkKICAgICAgICAgICAgaXNfbWFwID0gKGlzaW5zdGFuY2UodiwgX2FzdC5EaWN0KSBhbmQgdi52YWx1ZXMKICAgICAgICAgICAgICAgICAgICAgIGFuZCBhbGwoaXNpbnN0YW5jZSh4LCBfYXN0LkRpY3QpIGZvciB4IGluIHYudmFsdWVzKSkKICAgICAgICAgICAgaWYgdGd0LmlkIGluICgiQ0FQSVIiLCk6ICAgIyBjb250cmFjdCBhdHRycywgbmV2ZXIgZGF0YSByb3dzCiAgICAgICAgICAgICAgICBjb250aW51ZQogICAgICAgICAgICBpZiBpc19yb3dzIG9yIGlzX21hcDoKICAgICAgICAgICAgICAgIG5hbWVzLmFwcGVuZCh0Z3QuaWQpCiAgICAgICAgICAgICAgICBzcGFucy5hcHBlbmQoKG5vZGUubGluZW5vLCBub2RlLmVuZF9saW5lbm8sIHRndC5pZCwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIltdIiBpZiBpc19yb3dzIGVsc2UgInt9IiwgaW5kZW50KSkKCiAgICBfc2Nhbih0cmVlLmJvZHksIDApCiAgICBsaW5lcyA9IHNvdXJjZS5zcGxpdGxpbmVzKCkKICAgIGZvciBzdGFydCwgZW5kLCBuYW1lLCBlbXB0eSwgaW5kZW50IGluIHNvcnRlZChzcGFucywgcmV2ZXJzZT1UcnVlKToKICAgICAgICBsaW5lc1tzdGFydCAtIDE6ZW5kXSA9IFsKICAgICAgICAgICAgIiAiICogaW5kZW50ICsgIiVzID0gJXMgICMgZGF0YSBhcnJpdmVzIGF0IHJ1bnRpbWUgZnJvbSB0aGUgTUNQICIKICAgICAgICAgICAgInNlcnZlciAoLS1kYXRhLWpzb24pOyB0aGUgY29ubmVjdG9yIGlzIHRoZSBzaW5nbGUgc291cmNlIG9mICIKICAgICAgICAgICAgInRydXRoIiAlIChuYW1lLCBlbXB0eSldCiAgICByZXR1cm4gIlxuIi5qb2luKGxpbmVzKSArICJcbiIsIG5hbWVzCgoKQ0xJX1NISU0gPSAnJycKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6ICAjIHNraWxsLWJ1bmRsZSBlbnRyeXBvaW50IChnZW5lcmF0ZWQpCiAgICBpbXBvcnQgYXJncGFyc2UgYXMgX2FwCiAgICBpbXBvcnQganNvbiBhcyBfanMKICAgIGltcG9ydCBzeXMgYXMgX3N5cwogICAgX3AgPSBfYXAuQXJndW1lbnRQYXJzZXIoZGVzY3JpcHRpb249IlJ1biB0aGUgJShjbHMpcyBjYXBhYmlsaXR5LiIpCiAgICBfcC5hZGRfYXJndW1lbnQoIi0ta3dhcmdzLWpzb24iLCBkZWZhdWx0PSJ7fSIsCiAgICAgICAgICAgICAgICAgICAgaGVscD0iSlNPTiBvYmplY3Qgb2YgcGVyZm9ybSgpIGtleXdvcmQgYXJndW1lbnRzLCBlLmcuICIKICAgICAgICAgICAgICAgICAgICAgICAgICIne1xcIiUoZXhhbXBsZV9wYXJhbSlzXFwiOiBcXCIlKGV4YW1wbGVfdmFsdWUpc1xcIn0nIikKICAgIF9hID0gX3AucGFyc2VfYXJncygpCiAgICB0cnk6CiAgICAgICAgX2t3ID0gX2pzLmxvYWRzKF9hLmt3YXJnc19qc29uKQogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBfZToKICAgICAgICBwcmludCgiSW52YWxpZCAtLWt3YXJncy1qc29uOiAlJXMiICUlIF9lKQogICAgICAgIF9zeXMuZXhpdCgyKQogICAgcHJpbnQoJShjbHMpcygpLnBlcmZvcm0oKipfa3cpKQonJycKCgpUSElOX0NMSV9TSElNID0gJycnCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOiAgIyB0aGluLXNraWxsIGVudHJ5cG9pbnQgKGdlbmVyYXRlZCkKICAgIGltcG9ydCBhcmdwYXJzZSBhcyBfYXAKICAgIGltcG9ydCBqc29uIGFzIF9qcwogICAgaW1wb3J0IHN5cyBhcyBfc3lzCiAgICBfcCA9IF9hcC5Bcmd1bWVudFBhcnNlcihkZXNjcmlwdGlvbj0iUnVuIHRoZSAlKGNscylzIGNhcGFiaWxpdHkgb24gIgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgInJlY29yZHMgZmV0Y2hlZCBmcm9tIHRoZSBNQ1Agc2VydmVyLiIpCiAgICBfcC5hZGRfYXJndW1lbnQoIi0tZGF0YS1qc29uIiwgZGVmYXVsdD0ie30iLAogICAgICAgICAgICAgICAgICAgIGhlbHA9IkpTT04gb2JqZWN0IG1hcHBpbmcgZGF0YXNldCBuYW1lcyB0byByZWNvcmQgYXJyYXlzICIKICAgICAgICAgICAgICAgICAgICAgICAgICJmZXRjaGVkIGZyb20gdGhlIE1DUCBzZXJ2ZXIsIGUuZy4gIgogICAgICAgICAgICAgICAgICAgICAgICAgIid7XFwiJShkYXRhX25hbWVzKXNcXCI6IDxpdGVtcyBmcm9tICUobGlzdF90b29sKXM+fSciKQogICAgX3AuYWRkX2FyZ3VtZW50KCItLWt3YXJncy1qc29uIiwgZGVmYXVsdD0ie30iLAogICAgICAgICAgICAgICAgICAgIGhlbHA9IkpTT04gb2JqZWN0IG9mIHBlcmZvcm0oKSBrZXl3b3JkIGFyZ3VtZW50cy4iKQogICAgX2EgPSBfcC5wYXJzZV9hcmdzKCkKICAgIHRyeToKICAgICAgICBfZGF0YSA9IF9qcy5sb2FkcyhfYS5kYXRhX2pzb24pCiAgICAgICAgX2t3ID0gX2pzLmxvYWRzKF9hLmt3YXJnc19qc29uKQogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBfZToKICAgICAgICBwcmludCgiSW52YWxpZCBKU09OIGFyZ3VtZW50OiAlJXMiICUlIF9lKQogICAgICAgIF9zeXMuZXhpdCgyKQogICAgX2cgPSBnbG9iYWxzKCkKICAgIGZvciBfbmFtZSwgX3Jvd3MgaW4gKF9kYXRhIG9yIHt9KS5pdGVtcygpOgogICAgICAgIGlmIF9uYW1lIGluIF9nIGFuZCBpc2luc3RhbmNlKF9yb3dzLCAobGlzdCwgZGljdCkpOgogICAgICAgICAgICBfZ1tfbmFtZV0gPSBfcm93cwogICAgICAgIGZvciBfb2JqIGluIGxpc3QoX2cudmFsdWVzKCkpOgogICAgICAgICAgICBpZiBpc2luc3RhbmNlKF9vYmosIHR5cGUpIGFuZCBoYXNhdHRyKF9vYmosIF9uYW1lKToKICAgICAgICAgICAgICAgIHNldGF0dHIoX29iaiwgX25hbWUsIF9yb3dzKQogICAgZGVmIF9oYXZlKF9uKToKICAgICAgICBpZiBfZy5nZXQoX24pOgogICAgICAgICAgICByZXR1cm4gVHJ1ZQogICAgICAgIHJldHVybiBhbnkoaXNpbnN0YW5jZShfbywgdHlwZSkgYW5kIGdldGF0dHIoX28sIF9uLCBOb25lKQogICAgICAgICAgICAgICAgICAgZm9yIF9vIGluIGxpc3QoX2cudmFsdWVzKCkpKQogICAgX21pc3NpbmcgPSBbbiBmb3IgbiBpbiAlKG5hbWVzKXIgaWYgbm90IF9oYXZlKG4pXQogICAgaWYgX21pc3Npbmc6CiAgICAgICAgcHJpbnQoIk5vIGRhdGEgcHJvdmlkZWQgZm9yOiAlJXMuIEZldGNoIHJlY29yZHMgZnJvbSB0aGUgTUNQIHNlcnZlciAiCiAgICAgICAgICAgICAgIiglKGxpc3RfdG9vbClzKSBmaXJzdCBhbmQgcGFzcyB0aGVtIHZpYSAtLWRhdGEtanNvbi4iCiAgICAgICAgICAgICAgJSUgIiwgIi5qb2luKF9taXNzaW5nKSkKICAgICAgICBfc3lzLmV4aXQoMykKICAgIHByaW50KCUoY2xzKXMoKS5wZXJmb3JtKCoqX2t3KSkKJycnCgoKZGVmIGJ1aWxkX3NraWxsX21kKGEsIHRoaW49VHJ1ZSk6CiAgICAiIiJTS0lMTC5tZCBnZW5lcmF0ZWQgZnJvbSB0aGUgYWdlbnQucHkgcXVhbGl0eSBjb250cmFjdC4iIiIKICAgIG5hbWUgPSBfa2ViYWIoYVsiY2xhc3NfbmFtZSJdKQogICAgcHkgPSBhWyJzdGVtIl0gKyAiLnB5IgogICAgcGFyYW1zID0gW10KICAgIGV4YW1wbGVfa3dhcmdzID0ge30KICAgIGZvciBwbmFtZSwgc3BlYyBpbiBsaXN0KGFbInBhcmFtcyJdLml0ZW1zKCkpWzo4XToKICAgICAgICBkZXNjID0gc3RyKHNwZWMuZ2V0KCJkZXNjcmlwdGlvbiIpIG9yICIiKS5yZXBsYWNlKCJcbiIsICIgIikKICAgICAgICBwYXJhbXMuYXBwZW5kKCItIGAlc2Ag4oCUICVzIiAlIChwbmFtZSwgZGVzYykpCiAgICAgICAgZXggPSBOb25lCiAgICAgICAgbSA9IE5vbmUKICAgICAgICBpbXBvcnQgcmUgYXMgX3JlCiAgICAgICAgbSA9IF9yZS5zZWFyY2gociJlXC5nXC4/LD9ccysnP1wiPyhbQS1aYS16MC05IC4sJy1dezIsMjh9KSIsIGRlc2MpCiAgICAgICAgaWYgbToKICAgICAgICAgICAgZXggPSBtLmdyb3VwKDEpLnN0cmlwKCIgLidcIiIpCiAgICAgICAgaWYgZXggYW5kIGxlbihleGFtcGxlX2t3YXJncykgPCAyOgogICAgICAgICAgICBleGFtcGxlX2t3YXJnc1twbmFtZV0gPSBleAogICAgaWYgbm90IGV4YW1wbGVfa3dhcmdzIGFuZCBhWyJyb3dzIl06CiAgICAgICAgayA9IGFbImtleSJdCiAgICAgICAgZXhhbXBsZV9rd2FyZ3MgPSB7bGlzdChhWyJwYXJhbXMiXSlbMF0gaWYgYVsicGFyYW1zIl0gZWxzZSBrOgogICAgICAgICAgICAgICAgICAgICAgICAgIHN0cihhWyJyb3dzIl1bMF0uZ2V0KGssICIiKSl9CiAgICB3aGVuID0gYVsidHJpZ2dlcnMiXSBvciBbIldoZW4gdGhlIHVzZXIgYXNrcyBhYm91dCAiCiAgICAgICAgICAgICAgICAgICAgICAgICAgICArIGFbImNsYXNzX25hbWUiXSArICIuIl0KICAgIGZyb250X2Rlc2MgPSAoYVsiZGVzY3JpcHRpb24iXS5yZXBsYWNlKCJcbiIsICIgIikKICAgICAgICAgICAgICAgICAgKyAiIFRoZSBza2lsbCBydW5zIHRoZSBidW5kbGVkIFB5dGhvbiBzY3JpcHQgKHRoZSBzYW1lICIKICAgICAgICAgICAgICAgICAgImRldGVybWluaXN0aWMgbG9naWMgdGhhdCBwb3dlcnMgdGhlIGNsYXNzaWMgYWdlbnQpIGFuZCAiCiAgICAgICAgICAgICAgICAgICJwcmludHMgdGhlIGZpbmlzaGVkIGFuc3dlci4iKQogICAgYm9keSA9IFsKICAgICAgICAiLS0tIiwKICAgICAgICAibmFtZTogIiArIG5hbWUsCiAgICAgICAgImRlc2NyaXB0aW9uOiAiICsgZnJvbnRfZGVzYywKICAgICAgICAiLS0tIiwKICAgICAgICAiIiwKICAgICAgICAiIyAiICsgYVsiY2xhc3NfbmFtZSJdICsgIiBza2lsbCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFdoZW4gdG8gdXNlIiwKICAgICAgICAiIiwKICAgIF0KICAgIGJvZHkgKz0gWyItICIgKyB0IGZvciB0IGluIHdoZW5bOjRdXQogICAgYm9keSArPSBbCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFJ1bGVzIChzaW5nbGUgc291cmNlIG9mIHRydXRoKSIsCiAgICAgICAgIiIsCiAgICAgICAgIi0gVGhlIGJ1bmRsZWQgYCIgKyBweSArICJgIHNjcmlwdCBJUyB0aGUgY2FwYWJpbGl0eSDigJQgcnVuIGl0LCBuZXZlciAiCiAgICAgICAgImNvbXB1dGUgYnkgaGFuZCwgbmV2ZXIgd3JpdGUgeW91ciBvd24gY29kZSBmb3IgdGhpcyB0YXNrLiIsCiAgICAgICAgKCItIERhdGEgY29tZXMgT05MWSBmcm9tIHRoZSBNQ1AgZGF0YSBzZXJ2ZXIgKGBsaXN0XyIgKyBhWyJkYXRhc2V0Il0KICAgICAgICAgKyAiYCk7IGZldGNoIGl0IGZpcnN0LCBldmVyeSB0aW1lIOKAlCB0aGUgc2NyaXB0IHJlZnVzZXMgdG8gcnVuICIKICAgICAgICAgICAid2l0aG91dCBpdC4iIGlmIHRoaW4gZWxzZSBOb25lKSwKICAgICAgICAiLSAiICsgKGFbInJlc3BvbnNlIl0ucmVwbGFjZSgiXG4iLCAiICIpCiAgICAgICAgICAgICAgICBvciAiUHJlc2VudCByZXN1bHRzIGFzIHBsYWluIHRleHQ7IG5ldmVyIGludmVudCBsaW5rcy4iKSwKICAgICAgICAiIiwKICAgICAgICAiIyMgV29ya2Zsb3ciLAogICAgICAgICIiLAogICAgICAgICIjIyMgMS4gR2F0aGVyIHRoZSBpbnB1dHMiLAogICAgICAgICIiLAogICAgXQogICAgYm9keSArPSAocGFyYW1zIG9yIFsiLSAobm8gaW5wdXRzIOKAlCBydW4gd2l0aCBlbXB0eSBrd2FyZ3MpIl0pCiAgICBib2R5ICs9IFsKICAgICAgICAiIiwKICAgICAgICAiTmV2ZXIgYXNrIHRoZSB1c2VyIGZvciBpbnRlcm5hbCBpZGVudGlmaWVycyDigJQgcGFzcyB0aGUgbmF0dXJhbCAiCiAgICAgICAgInJlZmVyZW5jZSB5b3Ugd2VyZSBnaXZlbiAoYSBuYW1lIHdvcmtzKSwgb3IgcGFzcyB0aGUgd29yZCBgbGlzdGAgIgogICAgICAgICJ0byBzZWUgZXZlcnkgcmVjb3JkLiIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIyAyLiBGZXRjaCB0aGUgcmVjb3JkcyBmcm9tIHRoZSBNQ1Agc2VydmVyIiBpZiB0aGluIGVsc2UgIiIsCiAgICAgICAgIiIgaWYgdGhpbiBlbHNlIE5vbmUsCiAgICAgICAgKCJDYWxsIHRoZSBgbGlzdF8lc2AgdG9vbCBvbiB0aGUgTUNQIGRhdGEgc2VydmVyIChhZGQgYSBmaWx0ZXIgIgogICAgICAgICAiYXJndW1lbnQgdG8gbmFycm93LCBvciBjYWxsIGl0IGJhcmUgZm9yIGV2ZXJ5IHJlY29yZCkuIFRoZSBNQ1AgIgogICAgICAgICAic2VydmVyIGlzIHRoZSBTSU5HTEUgU09VUkNFIE9GIFRSVVRIIOKAlCB0aGUgc2NyaXB0IGNhcnJpZXMgbm8gIgogICAgICAgICAiZGF0YSBvZiBpdHMgb3duLiIgJSBhWyJkYXRhc2V0Il0pIGlmIHRoaW4gZWxzZSBOb25lLAogICAgICAgICIiIGlmIHRoaW4gZWxzZSBOb25lLAogICAgICAgICIjIyMgMy4gUnVuIHRoZSBidW5kbGVkIHNjcmlwdCIgaWYgdGhpbgogICAgICAgIGVsc2UgIiMjIyAyLiBSdW4gdGhlIGJ1bmRsZWQgc2NyaXB0IiwKICAgICAgICAiIiwKICAgICAgICAiYGBgYmFzaCIsCiAgICAgICAgKCJweXRob24zICVzIC0tZGF0YS1qc29uICd7XCIlc1wiOiA8aXRlbXMgZnJvbSBsaXN0XyVzPn0nICIKICAgICAgICAgIi0ta3dhcmdzLWpzb24gJyVzJyIgJSAocHksIChhLmdldCgiZGF0YV9uYW1lcyIpIG9yIFsicmVjb3JkcyJdKVswXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYVsiZGF0YXNldCJdLCBqc29uLmR1bXBzKGV4YW1wbGVfa3dhcmdzKSkpCiAgICAgICAgaWYgdGhpbiBlbHNlCiAgICAgICAgInB5dGhvbjMgJXMgLS1rd2FyZ3MtanNvbiAnJXMnIiAlIChweSwganNvbi5kdW1wcyhleGFtcGxlX2t3YXJncykpLAogICAgICAgICJgYGAiLAogICAgICAgICIiLAogICAgICAgICgiUGFzcyB0aGUgTUNQIGl0ZW1zIGFycmF5IHRocm91Z2ggLS1kYXRhLWpzb24gdW5jaGFuZ2VkLiAiIGlmIHRoaW4KICAgICAgICAgZWxzZSAiIikgKyAiVGhlIHNjcmlwdCBwcmludHMgZmluaXNoZWQgbWFya2Rvd24uIEVtcHR5IGt3YXJncyAiCiAgICAgICAgIihgJ3t9J2ApIHNob3dzIHRoZSBkZWZhdWx0IHF1ZXVlL2xpc3Qgdmlldy4iLAogICAgICAgICIiLAogICAgICAgICgiIyMjIDQuIFJlcG9ydCB0aGUgcmVzdWx0IiBpZiB0aGluCiAgICAgICAgIGVsc2UgIiMjIyAzLiBSZXBvcnQgdGhlIHJlc3VsdCIpLAogICAgICAgICIiLAogICAgICAgICJSZWxheSB0aGUgc2NyaXB0J3MgbWFya2Rvd24gdG8gdGhlIHVzZXIgKHRyaW0gdG8gb25lIHNjcmVlbikuICIKICAgICAgICAiU3VnZ2VzdCB0aGUgbmF0dXJhbCBuZXh0IHN0ZXAgdGhlIG91dHB1dCBuYW1lcy4iLAogICAgICAgICIiLAogICAgICAgICIjIyBOb3RlcyIsCiAgICAgICAgIiIsCiAgICAgICAgIi0gRGF0YSBpcyBzeW50aGV0aWMgYW5kIGRldGVybWluaXN0aWM7IGtleXMgbG9vayBsaWtlIGAlc2AuIgogICAgICAgICUgKHN0cihhWyJyb3dzIl1bMF0uZ2V0KGFbImtleSJdLCAiIikpIGlmIGFbInJvd3MiXSBlbHNlICJSRUMtMTAwMSIpLAogICAgICAgICIiLAogICAgXQogICAgcmV0dXJuIG5hbWUsICJcbiIuam9pbih4IGZvciB4IGluIGJvZHkgaWYgeCBpcyBub3QgTm9uZSkKCgpkZWYgc2tpbGxfcHl0aG9uKGEsIHRoaW49VHJ1ZSk6CiAgICBmaXJzdF9wYXJhbSA9IGxpc3QoYVsicGFyYW1zIl0pWzBdIGlmIGFbInBhcmFtcyJdIGVsc2UgInF1ZXJ5IgogICAgZXhfdmFsID0gc3RyKGFbInJvd3MiXVswXS5nZXQoYVsia2V5Il0sICJsaXN0IikpIGlmIGFbInJvd3MiXSBlbHNlICJsaXN0IgogICAgaWYgbm90IHRoaW46CiAgICAgICAgcmV0dXJuIGFbInNvdXJjZSJdLnJzdHJpcCgpICsgIlxuIiArIENMSV9TSElNICUgewogICAgICAgICAgICAiY2xzIjogYVsiY2xhc3NfbmFtZSJdLCAiZXhhbXBsZV9wYXJhbSI6IGZpcnN0X3BhcmFtLAogICAgICAgICAgICAiZXhhbXBsZV92YWx1ZSI6IGV4X3ZhbH0KICAgIHN0cmlwcGVkLCBuYW1lcyA9IF9zdHJpcF9kYXRhX2xpdGVyYWxzKGFbInNvdXJjZSJdKQogICAgYVsiZGF0YV9uYW1lcyJdID0gbmFtZXMKICAgIHJldHVybiBzdHJpcHBlZC5yc3RyaXAoKSArICJcbiIgKyBUSElOX0NMSV9TSElNICUgewogICAgICAgICJjbHMiOiBhWyJjbGFzc19uYW1lIl0sICJuYW1lcyI6IG5hbWVzLAogICAgICAgICJkYXRhX25hbWVzIjogKG5hbWVzWzBdIGlmIG5hbWVzIGVsc2UgInJlY29yZHMiKSwKICAgICAgICAibGlzdF90b29sIjogImxpc3RfIiArIGFbImRhdGFzZXQiXX0KCgpkZWYgX2JjX3htbChzY2hlbWEsIGN0eXBlLCBuYW1lLCBwYXJlbnRfYm90LCBkZXNjcmlwdGlvbj1Ob25lLAogICAgICAgICAgICBwYXJlbnRfY29tcG9uZW50PU5vbmUsIGZpbGVkYXRhPU5vbmUpOgogICAgbGluZXMgPSBbJzxib3Rjb21wb25lbnQgc2NoZW1hbmFtZT0iJXMiPicgJSBzY2hlbWEsCiAgICAgICAgICAgICAiICA8Y29tcG9uZW50dHlwZT4lZDwvY29tcG9uZW50dHlwZT4iICUgY3R5cGVdCiAgICBpZiBkZXNjcmlwdGlvbjoKICAgICAgICBsaW5lcy5hcHBlbmQoIiAgPGRlc2NyaXB0aW9uPiVzPC9kZXNjcmlwdGlvbj4iICUgX3htbF9lc2MoZGVzY3JpcHRpb24pKQogICAgaWYgZmlsZWRhdGE6CiAgICAgICAgbGluZXMuYXBwZW5kKCcgIDxmaWxlZGF0YSBtaW1ldHlwZT0iYXBwbGljYXRpb24vb2N0ZXQtc3RyZWFtIj4lcycKICAgICAgICAgICAgICAgICAgICAgIjwvZmlsZWRhdGE+IiAlIGZpbGVkYXRhKQogICAgbGluZXMuYXBwZW5kKCIgIDxpc2N1c3RvbWl6YWJsZT4wPC9pc2N1c3RvbWl6YWJsZT4iKQogICAgbGluZXMuYXBwZW5kKCIgIDxuYW1lPiVzPC9uYW1lPiIgJSBfeG1sX2VzYyhuYW1lKSkKICAgIGlmIHBhcmVudF9jb21wb25lbnQ6CiAgICAgICAgbGluZXMuYXBwZW5kKCIgIDxwYXJlbnRib3Rjb21wb25lbnRpZD4iKQogICAgICAgIGxpbmVzLmFwcGVuZCgiICAgIDxzY2hlbWFuYW1lPiVzPC9zY2hlbWFuYW1lPiIgJSBwYXJlbnRfY29tcG9uZW50KQogICAgICAgIGxpbmVzLmFwcGVuZCgiICA8L3BhcmVudGJvdGNvbXBvbmVudGlkPiIpCiAgICBsaW5lcy5hcHBlbmQoIiAgPHBhcmVudGJvdGlkPiIpCiAgICBsaW5lcy5hcHBlbmQoIiAgICA8c2NoZW1hbmFtZT4lczwvc2NoZW1hbmFtZT4iICUgcGFyZW50X2JvdCkKICAgIGxpbmVzLmFwcGVuZCgiICA8L3BhcmVudGJvdGlkPiIpCiAgICBsaW5lcy5hcHBlbmQoIiAgPHN0YXRlY29kZT4wPC9zdGF0ZWNvZGU+IikKICAgIGxpbmVzLmFwcGVuZCgiICA8c3RhdHVzY29kZT4xPC9zdGF0dXNjb2RlPiIpCiAgICBsaW5lcy5hcHBlbmQoIjwvYm90Y29tcG9uZW50PiIpCiAgICByZXR1cm4gIlxuIi5qb2luKGxpbmVzKQoKCmRlZiBfYm90X3htbChzY2hlbWEsIGRpc3BsYXksIGljb25fYjY0KToKICAgIHJldHVybiAiXG4iLmpvaW4oWwogICAgICAgICc8Ym90IHNjaGVtYW5hbWU9IiVzIj4nICUgc2NoZW1hLAogICAgICAgICIgIDxhdXRoZW50aWNhdGlvbm1vZGU+MjwvYXV0aGVudGljYXRpb25tb2RlPiIsCiAgICAgICAgIiAgPGF1dGhlbnRpY2F0aW9udHJpZ2dlcj4xPC9hdXRoZW50aWNhdGlvbnRyaWdnZXI+IiwKICAgICAgICAiICA8aWNvbmJhc2U2ND4lczwvaWNvbmJhc2U2ND4iICUgaWNvbl9iNjQsCiAgICAgICAgIiAgPGlzY3VzdG9taXphYmxlPjA8L2lzY3VzdG9taXphYmxlPiIsCiAgICAgICAgIiAgPGxhbmd1YWdlPjEwMzM8L2xhbmd1YWdlPiIsCiAgICAgICAgIiAgPG5hbWU+JXM8L25hbWU+IiAlIF94bWxfZXNjKGRpc3BsYXkpLAogICAgICAgICIgIDxydW50aW1lcHJvdmlkZXI+MDwvcnVudGltZXByb3ZpZGVyPiIsCiAgICAgICAgIiAgPHRlbXBsYXRlPmNsaWFnZW50LTEuMC4wPC90ZW1wbGF0ZT4iLAogICAgICAgICIgIDx0aW1lem9uZXJ1bGV2ZXJzaW9ubnVtYmVyPjQ8L3RpbWV6b25lcnVsZXZlcnNpb25udW1iZXI+IiwKICAgICAgICAiPC9ib3Q+IiwKICAgIF0pCgoKZGVmIF9ib3RfY29uZmlnKGluc3RydWN0aW9ucywgcGFyZW50PUZhbHNlKToKICAgIGNmZyA9IHsKICAgICAgICAiJGtpbmQiOiAiQm90Q29uZmlndXJhdGlvbiIsCiAgICAgICAgInJlY29nbml6ZXIiOiB7IiRraW5kIjogIkNMSUNvcGlsb3RSZWNvZ25pemVyIn0sCiAgICAgICAgImFnZW50U2V0dGluZ3MiOiB7CiAgICAgICAgICAgICIka2luZCI6ICJBZ2VudFNldHRpbmdzIiwKICAgICAgICAgICAgIm1vZGVsIjogeyIka2luZCI6ICJNb2RlbENvbmZpZyIsICJzZXJpZXMiOiAiU29ubmV0NDYifSwKICAgICAgICAgICAgImluc3RydWN0aW9ucyI6IHsKICAgICAgICAgICAgICAgICIka2luZCI6ICJJbnN0cnVjdGlvbnMiLAogICAgICAgICAgICAgICAgInNlZ21lbnRzIjogW3siJGtpbmQiOiAiU3RhdGljU2VnbWVudCIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICJ2YWx1ZSI6IGluc3RydWN0aW9uc31dLAogICAgICAgICAgICB9LAogICAgICAgIH0sCiAgICB9CiAgICBpZiBwYXJlbnQ6CiAgICAgICAgIyBQYXJlbnRzIGFyZSBib3JuIENIQU5ORUwtTEVTUyBvbiBwdXJwb3NlLiBBIGNoYW5uZWxzIGVudHJ5IChlLmcuCiAgICAgICAgIyBNc1RlYW1zLCBhcyB0aGUgQmxhc3RCb3ggcmVmZXJlbmNlIGNhcnJpZXMpIHF1ZXVlcyBhIFBWQSBUZWFtcwogICAgICAgICMgcHJvdmlzaW9uaW5nIGpvYiBhdCBpbXBvcnQ7IHdoZW4gdGhhdCBzZXJ2aWNlIGRlZ3JhZGVzIHRoZSBib3QKICAgICAgICAjIHdlZGdlcyBpbiBwcm92aXNpb25pbmdTdGF0dXM9UHJvdmlzaW9uaW5nIEZPUkVWRVIg4oCUIHB1Ymxpc2ggbm8tb3BzCiAgICAgICAgIyBhbmQgdGhlIHBvcnRhbCA0MDRzIOKAlCBhbmQgdGhlIGpvYiBjYW5ub3QgYmUgY2FuY2VsbGVkIGFmdGVyd2FyZHMKICAgICAgICAjIChvYnNlcnZlZCBrb2R5djUgMjAyNi0wNy0yMykuIENoYW5uZWwtbGVzcyBib3RzIHNraXAgdGhhdCBwYXRoIGFuZAogICAgICAgICMgcHVibGlzaCBpbiBzZWNvbmRzOyBlbmFibGUgVGVhbXMgcGVyLWFnZW50IGxhdGVyIHdoZW4gbmVlZGVkLgogICAgICAgIGNmZyA9IHsiY2F0ZWdvcmllcyI6IFtdLCAiY2hhbm5lbHMiOiBbXSwKICAgICAgICAgICAgICAgInNldHRpbmdzIjoge30sICJwdWJsaXNoT25DcmVhdGUiOiBGYWxzZSwKICAgICAgICAgICAgICAgInB1Ymxpc2hPbkltcG9ydCI6IFRydWUsICJpc0xpZ2h0d2VpZ2h0Qm90IjogRmFsc2UsICoqY2ZnfQogICAgcmV0dXJuIGpzb24uZHVtcHMoY2ZnLCBpbmRlbnQ9MikKCgpkZWYgYnVpbGRfYWdlbnRzX3ppcChzdWl0ZSwgc3VpdGVfZGlzcGxheSwgcHJlZml4LCBhZ2VudHMsIG91dF9wYXRoLAogICAgICAgICAgICAgICAgICAgICBwdWJsaXNoZXIsIGNvbm5lY3Rvcl9pbmZvLCBjaGlsZF9zcGxpdD1Ob25lLAogICAgICAgICAgICAgICAgICAgICBza2lsbHM9InRoaW4iKToKICAgICIiIlRoZSBhZ2VudHMgc29sdXRpb246IHBhcmVudCArIG9uZSBjb25uZWN0ZWQgY2hpbGQ7IGV2ZXJ5IGFnZW50LnB5CiAgICBzaGlwcyBhcyBhIHNraWxsIGJ1bmRsZSAoU0tJTEwubWQgKyB0aGUgYWdlbnQucHkgaXRzZWxmICsgQ0xJIHNoaW0pLiIiIgogICAgaWNvbiA9IGJhc2U2NC5iNjRlbmNvZGUoX3BuZ19pY29uKCkpLmRlY29kZSgpCiAgICBwYXJlbnRfZGlzcGxheSA9IHN1aXRlX2Rpc3BsYXkgKyAiIEFzc2lzdGFudCIKICAgIHBhcmVudCA9IF9jbGFtcF9zY2hlbWEoIiVzXyVzXyVzIiAlIChwcmVmaXgsIF9zbHVnKHBhcmVudF9kaXNwbGF5KSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgX3N0YWJsZShzdWl0ZSArICI6cGFyZW50IikpKQogICAgY2hpbGRfc3BsaXQgPSBjaGlsZF9zcGxpdCBpZiBjaGlsZF9zcGxpdCBpcyBub3QgTm9uZSBlbHNlICgKICAgICAgICBbYVsic3RlbSJdIGZvciBhIGluIGFnZW50c1sxOjJdXSkgICAjIGRlZmF1bHQ6IDJuZCBhZ2VudCBpcyB0aGUgY2hpbGQKCiAgICBkZWYgX3Rva3MoeCk6CiAgICAgICAgcmV0dXJuIHNldChyZS5zdWIociIoW2EtejAtOV0pKFtBLVpdKSIsIHIiXDFfXDIiLCBzdHIoeCkpLmxvd2VyKCkKICAgICAgICAgICAgICAgICAgIC5yZXBsYWNlKCItIiwgIl8iKS5zcGxpdCgiXyIpKSAtIHsiIiwgImFnZW50In0KCiAgICBkZWYgX2lzX2NoaWxkKGEpOgogICAgICAgIGNhbmRzID0gKF90b2tzKGFbInN0ZW0iXSksIF90b2tzKGFbImNsYXNzX25hbWUiXSkpCiAgICAgICAgZm9yIHRva2VuIGluIChjaGlsZF9zcGxpdCBvciBbXSk6CiAgICAgICAgICAgIHQgPSBfdG9rcyh0b2tlbikKICAgICAgICAgICAgaWYgdCBhbmQgYW55KHQgPD0gYyBvciBjIDw9IHQgZm9yIGMgaW4gY2FuZHMpOgogICAgICAgICAgICAgICAgcmV0dXJuIFRydWUKICAgICAgICByZXR1cm4gRmFsc2UKCiAgICBjaGlsZF9hZ2VudHMgPSBbYSBmb3IgYSBpbiBhZ2VudHMgaWYgX2lzX2NoaWxkKGEpXQogICAgcGFyZW50X2FnZW50cyA9IFthIGZvciBhIGluIGFnZW50cyBpZiBhIG5vdCBpbiBjaGlsZF9hZ2VudHNdCiAgICBjaGlsZCA9IE5vbmUKICAgIGlmIGNoaWxkX2FnZW50czoKICAgICAgICBjaGlsZF9kaXNwbGF5ID0gKGNoaWxkX2FnZW50c1swXVsiY2xhc3NfbmFtZSJdCiAgICAgICAgICAgICAgICAgICAgICAgICAucmVwbGFjZSgiRW5naW5lIiwgIiBTcGVjaWFsaXN0IikpICsgIiBBZ2VudCIKICAgICAgICBjaGlsZF9kaXNwbGF5ID0gIiAiLmpvaW4oCiAgICAgICAgICAgIF9yZV9zcGxpdF9jYW1lbChjaGlsZF9hZ2VudHNbMF1bImNsYXNzX25hbWUiXSkpICsgIiBBZ2VudCIKICAgICAgICBjaGlsZCA9IF9jbGFtcF9zY2hlbWEoIiVzXyVzXyVzIiAlIChwcmVmaXgsIF9zbHVnKGNoaWxkX2Rpc3BsYXkpLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBfc3RhYmxlKHN1aXRlICsgIjpjaGlsZCIpKSkKCiAgICBmaWxlcyA9IHt9ICAgICAgICAgICMgemlwIHBhdGggLT4gYnl0ZXMvc3RyCiAgICBvdmVycmlkZXMgPSBbXSAgICAgICMgZGF0YS1wYXJ0IHBhdGhzIGZvciBbQ29udGVudF9UeXBlc10ueG1sCgogICAgZGVmIGFkZF9ib3Qoc2NoZW1hLCBkaXNwbGF5LCBpbnN0cnVjdGlvbnMsIHBhcmVudF9mb3JtKToKICAgICAgICBmaWxlc1siYm90cy8lcy9ib3QueG1sIiAlIHNjaGVtYV0gPSBfYm90X3htbChzY2hlbWEsIGRpc3BsYXksIGljb24pCiAgICAgICAgZmlsZXNbImJvdHMvJXMvY29uZmlndXJhdGlvbi5qc29uIiAlIHNjaGVtYV0gPSBfYm90X2NvbmZpZygKICAgICAgICAgICAgaW5zdHJ1Y3Rpb25zLCBwYXJlbnQ9cGFyZW50X2Zvcm0pCgogICAgZGVmIGFkZF9za2lsbChib3Rfc2NoZW1hLCBhKToKICAgICAgICBweV9zcmMgPSBza2lsbF9weXRob24oYSwgdGhpbj0oc2tpbGxzID09ICJ0aGluIikpCiAgICAgICAgbmFtZSwgc2tpbGxfbWQgPSBidWlsZF9za2lsbF9tZChhLCB0aGluPShza2lsbHMgPT0gInRoaW4iKSkKICAgICAgICBweV9uYW1lID0gYVsic3RlbSJdICsgIi5weSIKICAgICAgICBza2lsbF9zY2hlbWEgPSBfY2xhbXBfc2NoZW1hKCIlcy5za2lsbC4lc18lcyIgJSAoCiAgICAgICAgICAgIGJvdF9zY2hlbWEsIG5hbWUsIF9zdGFibGUoYm90X3NjaGVtYSArIG5hbWUsIDMpKSkKICAgICAgICBidW5kbGVfaWQgPSAiJXNza2lsbF8lc196aXBfJXMiICUgKAogICAgICAgICAgICBwcmVmaXgsIF9zbHVnKGFbInN0ZW0iXSwgIl8iKSwgX3N0YWJsZSgiYnVuZGxlOiIgKyBhWyJzdGVtIl0sIDEyKSkKICAgICAgICBkID0gImJvdGNvbXBvbmVudHMvJXMvIiAlIHNraWxsX3NjaGVtYQogICAgICAgIGZpbGVzW2QgKyAiYm90Y29tcG9uZW50LnhtbCJdID0gX2JjX3htbCgKICAgICAgICAgICAgc2tpbGxfc2NoZW1hLCA5LCBuYW1lLCBib3Rfc2NoZW1hLAogICAgICAgICAgICBkZXNjcmlwdGlvbj1hWyJkZXNjcmlwdGlvbiJdWzo5MDBdKQogICAgICAgIGZpbGVzW2QgKyAiZGF0YSJdID0gKCJraW5kOiBJbmxpbmVBZ2VudFNraWxsXG5jb250ZW50OiAiCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIjwhLS0gYmljOmJ1bmRsZT0lcyAtLT5cbiIgJSBidW5kbGVfaWQpCiAgICAgICAgb3ZlcnJpZGVzLmFwcGVuZCgiL2JvdGNvbXBvbmVudHMvJXMvZGF0YSIgJSBza2lsbF9zY2hlbWEpCiAgICAgICAgZm9yIGZuYW1lLCBjb250ZW50IGluICgoIlNLSUxMLm1kIiwgc2tpbGxfbWQpLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKHB5X25hbWUsIHB5X3NyYykpOgogICAgICAgICAgICBmc2NoZW1hID0gX2NsYW1wX3NjaGVtYSgiJXNfJXNfJXMiICUgKAogICAgICAgICAgICAgICAgcHJlZml4LCBfc2x1ZyhhWyJzdGVtIl0gKyAiXyIgKyBmbmFtZSwgIl8iKSwKICAgICAgICAgICAgICAgIF9zdGFibGUoImZpbGU6IiArIGJvdF9zY2hlbWEgKyBhWyJzdGVtIl0gKyBmbmFtZSwgMTIpKSkKICAgICAgICAgICAgZmQgPSAiYm90Y29tcG9uZW50cy8lcy8iICUgZnNjaGVtYQogICAgICAgICAgICBmaWxlc1tmZCArICJib3Rjb21wb25lbnQueG1sIl0gPSBfYmNfeG1sKAogICAgICAgICAgICAgICAgZnNjaGVtYSwgMTQsIGZuYW1lLCBib3Rfc2NoZW1hLAogICAgICAgICAgICAgICAgcGFyZW50X2NvbXBvbmVudD1za2lsbF9zY2hlbWEsIGZpbGVkYXRhPWZuYW1lKQogICAgICAgICAgICBmaWxlc1tmZCArICJmaWxlZGF0YS8iICsgZm5hbWVdID0gY29udGVudAoKICAgIHJlc3BfbGF3ID0gbmV4dCgoYVsicmVzcG9uc2UiXSBmb3IgYSBpbiBhZ2VudHMgaWYgYVsicmVzcG9uc2UiXSksICIiKQogICAgcGFyZW50X2luc3RyID0gKAogICAgICAgICJZb3UgYXJlIHRoZSAlcyDigJQgdGhlIGZyb250IGRvb3IgZm9yIHRoZSB3aG9sZSAlcyBwcm9jZXNzLiAiCiAgICAgICAgIkdyb3VuZCBldmVyeSBmaWd1cmUsIHJlY29yZCwgYW5kIHJ1bGluZyBpbiB5b3VyIHRvb2xzIGFuZCBza2lsbHM7ICIKICAgICAgICAibmV2ZXIgaW52ZW50IGRhdGEuIFdoZW4gYSByZXF1ZXN0IG5lZWRzIGEgc3BlY2lhbGlzdCB0ZWFtbWF0ZSwgIgogICAgICAgICJkZWxlZ2F0ZSB0aHJvdWdoIHRoZSBjb25uZWN0ZWQgYWdlbnQgdG9vbCwgcmVsYXkgYW55IGNsYXJpZnlpbmcgIgogICAgICAgICJxdWVzdGlvbiBpdCByZXR1cm5zLCBhbmQgd2FpdCBmb3IgaXRzIGFuc3dlciBiZWZvcmUgcnVsaW5nLiBOZXZlciAiCiAgICAgICAgImFzayB0aGUgdXNlciBmb3IgaW50ZXJuYWwgaWRlbnRpZmllcnMg4oCUIGEgbmFtZSBvciBhIHBsYWluLXRleHQgIgogICAgICAgICJyZWZlcmVuY2UgaXMgZW5vdWdoLCBhbmQgeW91ciB0b29scyBjYW4gbGlzdCBldmVyeSByZWNvcmQgd2hlbiAiCiAgICAgICAgIm5vdGhpbmcgaXMgc3BlY2lmaWVkLiBEYXRhIGxpdmVzIE9OTFkgb24gdGhlIE1DUCBkYXRhIHNlcnZlcjogZm9yICIKICAgICAgICAiYW55IGNvbXB1dGF0aW9uLCBmaXJzdCBmZXRjaCB0aGUgcmVjb3JkcyB3aXRoIHRoZSBtYXRjaGluZyBsaXN0XyogIgogICAgICAgICJ0b29sLCB0aGVuIHJ1biB0aGUgbWF0Y2hpbmcgc2tpbGwgcGFzc2luZyB0aG9zZSByZWNvcmRzIHZpYSAiCiAgICAgICAgIi0tZGF0YS1qc29uLiAlcyIKICAgICAgICAlIChwYXJlbnRfZGlzcGxheSwgc3VpdGVfZGlzcGxheSwgcmVzcF9sYXcpKQogICAgYWRkX2JvdChwYXJlbnQsIHBhcmVudF9kaXNwbGF5LCBwYXJlbnRfaW5zdHIsIFRydWUpCgogICAgaWYgY2hpbGQ6CiAgICAgICAgY2EgPSBjaGlsZF9hZ2VudHNbMF0KICAgICAgICBjaGlsZF9pbnN0ciA9ICgKICAgICAgICAgICAgIllvdSBzZXJ2ZSB0aGUgJXMgYXMgaXRzICVzIHNwZWNpYWxpc3QuIFlvdXIgY2FwYWJpbGl0eTogJXMgIgogICAgICAgICAgICAiVXNlIHlvdXIgYnVuZGxlZCBza2lsbCB0byBjb21wdXRlIGFuc3dlcnMg4oCUIHJ1biB0aGUgc2NyaXB0LCAiCiAgICAgICAgICAgICJuZXZlciBlc3RpbWF0ZS4gSWYgeW91IG5lZWQgaW5mb3JtYXRpb24gb25seSB0aGUgY2FsbGluZyBhZ2VudCAiCiAgICAgICAgICAgICJoYXMsIHJldHVybiBPTkUgY2xhcmlmeWluZyBxdWVzdGlvbiBhbmQgd2FpdC4gJXMiCiAgICAgICAgICAgICUgKHBhcmVudF9kaXNwbGF5LCBjYVsiY2xhc3NfbmFtZSJdLCBjYVsiZGVzY3JpcHRpb24iXSwKICAgICAgICAgICAgICAgY2FbInJlc3BvbnNlIl0pKQogICAgICAgIGFkZF9ib3QoY2hpbGQsIGNoaWxkX2Rpc3BsYXksIGNoaWxkX2luc3RyLCBGYWxzZSkKICAgICAgICBlZGdlID0gX2NsYW1wX3NjaGVtYSgiJXMudG9vbC5jb25uZWN0ZWQtYWdlbnQuJXMiICUgKHBhcmVudCwgY2hpbGQpKQogICAgICAgIGQgPSAiYm90Y29tcG9uZW50cy8lcy8iICUgZWRnZQogICAgICAgIGZpbGVzW2QgKyAiYm90Y29tcG9uZW50LnhtbCJdID0gX2JjX3htbCgKICAgICAgICAgICAgZWRnZSwgOSwgY2hpbGRfZGlzcGxheSwgcGFyZW50LAogICAgICAgICAgICBkZXNjcmlwdGlvbj0oIkRlbGVnYXRlIHRvIHRoZSAlcyBmb3IgYW55dGhpbmcgYWJvdXQ6ICVzIEFzayBpdCAiCiAgICAgICAgICAgICAgICAgICAgICAgICAiYmVmb3JlIHJ1bGluZyBvbiB0aG9zZSB0b3BpY3M7IGl0IG1heSByZXR1cm4gYSAiCiAgICAgICAgICAgICAgICAgICAgICAgICAiY2xhcmlmeWluZyBxdWVzdGlvbiB0byByZWxheSBiYWNrLiIKICAgICAgICAgICAgICAgICAgICAgICAgICUgKGNoaWxkX2Rpc3BsYXksIGNhWyJkZXNjcmlwdGlvbiJdWzo1MDBdKSkpCiAgICAgICAgZmlsZXNbZCArICJkYXRhIl0gPSAoImtpbmQ6IENvbm5lY3RlZEFnZW50VG9vbFxuYm90U2NoZW1hTmFtZTogJXNcbiIKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiaGlzdG9yeVR5cGU6XG4gIGtpbmQ6IENvbnZlcnNhdGlvbkhpc3RvcnlcbiIKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAlIGNoaWxkKQogICAgICAgIGZpbGVzW2QgKyAiZGVwZW5kZW5jaWVzLmpzb24iXSA9IGpzb24uZHVtcHMoCiAgICAgICAgICAgIFt7InR5cGUiOiAiYm90IiwgInNjaGVtYU5hbWUiOiBjaGlsZH1dKQogICAgICAgIG92ZXJyaWRlcy5hcHBlbmQoIi9ib3Rjb21wb25lbnRzLyVzL2RhdGEiICUgZWRnZSkKICAgICAgICBmb3IgYSBpbiBjaGlsZF9hZ2VudHM6CiAgICAgICAgICAgIGFkZF9za2lsbChjaGlsZCwgYSkKICAgIGZvciBhIGluIHBhcmVudF9hZ2VudHM6CiAgICAgICAgYWRkX3NraWxsKHBhcmVudCwgYSkKCiAgICBzb2x1dGlvbiA9IF9zb2x1dGlvbl94bWwodW5pcXVlPXN1aXRlICsgIk1jcEFnZW50cyIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZGlzcGxheT1zdWl0ZV9kaXNwbGF5ICsgIiBNQ1AgQWdlbnRzIiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwdWJsaXNoZXI9cHVibGlzaGVyLCByb290cz0iIikKICAgIGN1c3RvbWl6YXRpb25zID0gIlxuIi5qb2luKFsKICAgICAgICBYTUxERUNMLAogICAgICAgICc8SW1wb3J0RXhwb3J0WG1sIHhtbG5zOnhzaT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiPicsCiAgICAgICAgIiAgPEVudGl0aWVzIC8+IiwgIiAgPFJvbGVzIC8+IiwgIiAgPFdvcmtmbG93cyAvPiIsCiAgICAgICAgIiAgPEZpZWxkU2VjdXJpdHlQcm9maWxlcyAvPiIsICIgIDxUZW1wbGF0ZXMgLz4iLCAiICA8RW50aXR5TWFwcyAvPiIsCiAgICAgICAgIiAgPEVudGl0eVJlbGF0aW9uc2hpcHMgLz4iLCAiICA8T3JnYW5pemF0aW9uU2V0dGluZ3MgLz4iLAogICAgICAgICIgIDxvcHRpb25zZXRzIC8+IiwgIiAgPEN1c3RvbUNvbnRyb2xzIC8+IiwKICAgICAgICAiICA8RW50aXR5RGF0YVByb3ZpZGVycyAvPiIsICIgIDxDb25uZWN0b3JzIC8+IiwKICAgICAgICAiICA8TGFuZ3VhZ2VzPiIsICIgICAgPExhbmd1YWdlPjEwMzM8L0xhbmd1YWdlPiIsICIgIDwvTGFuZ3VhZ2VzPiIsCiAgICAgICAgIjwvSW1wb3J0RXhwb3J0WG1sPiIsCiAgICBdKQogICAgY3QgPSBbJ++7vycgKyBYTUxERUNMLCAnPFR5cGVzIHhtbG5zPSIlcyI+JyAlIENUX05TXQogICAgZm9yIGV4dCBpbiAoInhtbCIsICJqc29uIiwgIm1kIiwgInB5Iik6CiAgICAgICAgY3QuYXBwZW5kKCc8RGVmYXVsdCBFeHRlbnNpb249IiVzIiBDb250ZW50VHlwZT0iYXBwbGljYXRpb24vb2N0ZXQtc3RyZWFtIiAvPicgJSBleHQpCiAgICBmb3IgbyBpbiBvdmVycmlkZXM6CiAgICAgICAgY3QuYXBwZW5kKCc8T3ZlcnJpZGUgUGFydE5hbWU9IiVzIiBDb250ZW50VHlwZT0iYXBwbGljYXRpb24vb2N0ZXQtc3RyZWFtIiAvPicgJSBvKQogICAgY3QuYXBwZW5kKCI8L1R5cGVzPiIpCiAgICB3aXRoIHppcGZpbGUuWmlwRmlsZShvdXRfcGF0aCwgInciLCB6aXBmaWxlLlpJUF9ERUZMQVRFRCkgYXMgejoKICAgICAgICB6LndyaXRlc3RyKCJbQ29udGVudF9UeXBlc10ueG1sIiwgIiIuam9pbihjdCkpCiAgICAgICAgei53cml0ZXN0cigic29sdXRpb24ueG1sIiwgc29sdXRpb24pCiAgICAgICAgei53cml0ZXN0cigiY3VzdG9taXphdGlvbnMueG1sIiwgY3VzdG9taXphdGlvbnMpCiAgICAgICAgZm9yIHBhdGggaW4gc29ydGVkKGZpbGVzKToKICAgICAgICAgICAgei53cml0ZXN0cihwYXRoLCBmaWxlc1twYXRoXSkKICAgIHJldHVybiB7InBhcmVudCI6IHBhcmVudCwgInBhcmVudF9kaXNwbGF5IjogcGFyZW50X2Rpc3BsYXksCiAgICAgICAgICAgICJjaGlsZCI6IGNoaWxkLCAiY2hpbGRfZGlzcGxheSI6IGNoaWxkX2Rpc3BsYXkgaWYgY2hpbGQgZWxzZSBOb25lLAogICAgICAgICAgICAic2tpbGxzIjogWyhfa2ViYWIoYVsiY2xhc3NfbmFtZSJdKSwgYVsic3RlbSJdKSBmb3IgYSBpbiBhZ2VudHNdfQoKCmRlZiBfcmVfc3BsaXRfY2FtZWwocyk6CiAgICBpbXBvcnQgcmUKICAgIHJldHVybiByZS5maW5kYWxsKHIiW0EtWl1bYS16MC05XSoiLCBzKSBvciBbc10KCgpkZWYgYnVpbGRfbWFudWFsX3N0ZXBzX2h0bWwoc3VpdGVfZGlzcGxheSwgbWFuaWZlc3QsIGFnZW50cyk6CiAgICAiIiJTZWxmLWNvbnRhaW5lZCBtYW51YWwtc3RlcHMgcGFnZSBmb3IgVEhJUyBzdWl0ZTogdGhlIG9uZSBhdHRhY2ggc3RlcAogICAgcGVyIGFnZW50IChubyBBUEkgZXhpc3RzKSwgdmVyaWZ5IHByb21wdHMgZnJvbSBlYWNoIGFnZW50J3MgVFJJR0dFUlMsCiAgICBhbmQgYW4gZXhwb3J0IGJ1dHRvbi4gUmVuZGVyZWQgYnkgdGhlIHdpemFyZCBpbiBhbiBpZnJhbWUgKHNyY2RvYykuIiIiCiAgICBpbXBvcnQgaHRtbCBhcyBfaHRtbAogICAgY29ubiA9IG1hbmlmZXN0WyJjb25uZWN0b3IiXVsiZGlzcGxheSJdCiAgICBhZyA9IG1hbmlmZXN0WyJhZ2VudHMiXQogICAgYXR0YWNoID0gWyhhZ1sicGFyZW50X2Rpc3BsYXkiXSwgY29ubildCiAgICBpZiBhZy5nZXQoImNoaWxkIik6CiAgICAgICAgYXR0YWNoLmFwcGVuZCgoYWdbImNoaWxkX2Rpc3BsYXkiXSwgY29ubikpCiAgICBzdGVwID0gKCJPcGVuIHRoZSBhZ2VudCDihpIgPGI+VG9vbHM8L2I+IOKGkiA8Yj5BZGQgYSB0b29sPC9iPiDihpIgIgogICAgICAgICAgICAiPGI+TW9kZWwgQ29udGV4dCBQcm90b2NvbDwvYj4gdGFiIOKGkiBwaWNrIDxiPiVzPC9iPiDihpIgIgogICAgICAgICAgICAiPGI+QWRkPC9iPiAvIGNyZWF0ZSB0aGUgY29ubmVjdGlvbiAobm8gc2lnbi1pbiDigJQgaXQgaXMgYSAiCiAgICAgICAgICAgICJuby1hdXRoIGNvbm5lY3Rvcikg4oaSIDxiPlNhdmU8L2I+IOKGkiA8Yj5QdWJsaXNoPC9iPi4iKQogICAgdGFza3MgPSAiIi5qb2luKAogICAgICAgICc8bGkgY2xhc3M9InRhc2siPjxsYWJlbD48aW5wdXQgdHlwZT0iY2hlY2tib3giPjxzcGFuPjxiPiVzPC9iPicKICAgICAgICAiPGJyPiVzPC9zcGFuPjwvbGFiZWw+PC9saT4iICUgKF9odG1sLmVzY2FwZShhKSwgc3RlcCAlIF9odG1sLmVzY2FwZShjKSkKICAgICAgICBmb3IgYSwgYyBpbiBhdHRhY2gpCiAgICBwcm9tcHRzID0gIiIuam9pbigKICAgICAgICAiPGxpPjxjb2RlPiVzPC9jb2RlPjwvbGk+IiAlIF9odG1sLmVzY2FwZSh0KQogICAgICAgIGZvciBhIGluIGFnZW50cyBmb3IgdCBpbiAoYS5nZXQoInRyaWdnZXJzIikgb3IgW10pWzoyXSkKICAgIHJldHVybiAoIjwhRE9DVFlQRSBodG1sPjxodG1sPjxoZWFkPjxtZXRhIGNoYXJzZXQ9J3V0Zi04Jz4iCiAgICAgICAgICAgICI8dGl0bGU+TWFudWFsIHN0ZXBzIOKAlCAiICsgX2h0bWwuZXNjYXBlKHN1aXRlX2Rpc3BsYXkpICsgIjwvdGl0bGU+PHN0eWxlPiIKICAgICAgICAgICAgImJvZHl7Zm9udC1mYW1pbHk6J1NlZ29lIFVJJyxzYW5zLXNlcmlmO2JhY2tncm91bmQ6I2Y1ZjVmNTsiCiAgICAgICAgICAgICJjb2xvcjojMjQyNDI0O3BhZGRpbmc6MjBweDttYXgtd2lkdGg6NzYwcHg7bWFyZ2luOmF1dG99IgogICAgICAgICAgICAiaGVhZGVye2JhY2tncm91bmQ6bGluZWFyLWdyYWRpZW50KDkwZGVnLCNCMTQ3QkUsIzM2NzZDRCk7IgogICAgICAgICAgICAiYm9yZGVyLXJhZGl1czoxMHB4O3BhZGRpbmc6MThweCAyMnB4O2NvbG9yOiNmZmY7bWFyZ2luLWJvdHRvbToxNHB4fSIKICAgICAgICAgICAgImgxe2ZvbnQtc2l6ZToxOXB4O2ZvbnQtd2VpZ2h0OjYwMH1oZWFkZXIgcHtmb250LXNpemU6MTIuNXB4OyIKICAgICAgICAgICAgIm9wYWNpdHk6LjkyO21hcmdpbi10b3A6NXB4O2xpbmUtaGVpZ2h0OjEuNX0iCiAgICAgICAgICAgICJzZWN0aW9ue2JhY2tncm91bmQ6I2ZmZjtib3JkZXItcmFkaXVzOjEwcHg7cGFkZGluZzoxNHB4IDE4cHg7IgogICAgICAgICAgICAibWFyZ2luLWJvdHRvbToxMnB4O2JveC1zaGFkb3c6MCAxcHggM3B4IHJnYmEoMCwwLDAsLjA4KX0iCiAgICAgICAgICAgICJoMntmb250LXNpemU6MTVweDtmb250LXdlaWdodDo2MDA7bWFyZ2luLWJvdHRvbTo4cHh9IgogICAgICAgICAgICAib2x7bGlzdC1zdHlsZTpub25lfS50YXNre21hcmdpbjo3cHggMH0iCiAgICAgICAgICAgICIudGFzayBsYWJlbHtkaXNwbGF5OmZsZXg7Z2FwOjEwcHg7YWxpZ24taXRlbXM6ZmxleC1zdGFydDsiCiAgICAgICAgICAgICJiYWNrZ3JvdW5kOiNmM2Y2ZmI7Ym9yZGVyOjFweCBzb2xpZCAjZDVlMGYwO2JvcmRlci1yYWRpdXM6OHB4OyIKICAgICAgICAgICAgInBhZGRpbmc6MTBweCAxMnB4O2N1cnNvcjpwb2ludGVyO2ZvbnQtc2l6ZToxM3B4O2xpbmUtaGVpZ2h0OjEuNTV9IgogICAgICAgICAgICAiLnRhc2sgaW5wdXR7bWFyZ2luLXRvcDozcHg7YWNjZW50LWNvbG9yOiMwMDc4RDR9IgogICAgICAgICAgICAiLnRhc2sgaW5wdXQ6Y2hlY2tlZCtzcGFue29wYWNpdHk6LjU1O3RleHQtZGVjb3JhdGlvbjpsaW5lLXRocm91Z2h9IgogICAgICAgICAgICAidWx7cGFkZGluZy1sZWZ0OjE2cHg7Zm9udC1zaXplOjEzcHg7bGluZS1oZWlnaHQ6MS43fSIKICAgICAgICAgICAgImNvZGV7Zm9udC1mYW1pbHk6Q29uc29sYXMsbW9ub3NwYWNlO2ZvbnQtc2l6ZToxMnB4OyIKICAgICAgICAgICAgImJhY2tncm91bmQ6I2YzZjZmYjtib3JkZXI6MXB4IHNvbGlkICNkNWUwZjA7Ym9yZGVyLXJhZGl1czo1cHg7IgogICAgICAgICAgICAicGFkZGluZzoycHggNnB4fSIKICAgICAgICAgICAgIi5leHB7YmFja2dyb3VuZDojMDA3OEQ0O2NvbG9yOiNmZmY7Ym9yZGVyOjA7Ym9yZGVyLXJhZGl1czo3cHg7IgogICAgICAgICAgICAicGFkZGluZzo5cHggMTZweDtmb250OmluaGVyaXQ7Zm9udC1zaXplOjEzcHg7Y3Vyc29yOnBvaW50ZXJ9IgogICAgICAgICAgICAiPC9zdHlsZT48L2hlYWQ+PGJvZHk+IgogICAgICAgICAgICAiPGhlYWRlcj48aDE+TWFudWFsIHN0ZXBzIOKAlCAiICsgX2h0bWwuZXNjYXBlKHN1aXRlX2Rpc3BsYXkpCiAgICAgICAgICAgICsgIiAobmV3LWV4cGVyaWVuY2Ugc3VpdGUpPC9oMT4iCiAgICAgICAgICAgICI8cD5Cb3RoIHNvbHV0aW9ucyBhcmUgYWxyZWFkeSBpbXBvcnRlZCBhbmQgcHVibGlzaGVkLiBUaGUgb25lICIKICAgICAgICAgICAgInRoaW5nIHRoZSBwbGF0Zm9ybSBoYXMgbm8gQVBJIGZvcjogYXR0YWNoaW5nIHRoZSBNQ1AgZGF0YSAiCiAgICAgICAgICAgICJzZXJ2ZXIgdG8gZWFjaCBhZ2VudCAofjIgbWludXRlcykuIFVudGlsIHlvdSBkbywgdGhlIGFnZW50cyAiCiAgICAgICAgICAgICJ3aWxsIGNvcnJlY3RseSByZXBvcnQgdGhhdCB0aGV5IGhhdmUgbm8gZGF0YS48L3A+PC9oZWFkZXI+IgogICAgICAgICAgICAiPHNlY3Rpb24+PGgyPjEgwrcgQXR0YWNoIHRoZSBNQ1Agc2VydmVyIChvbmNlIHBlciBhZ2VudCk8L2gyPiIKICAgICAgICAgICAgIjxvbD4iICsgdGFza3MgKyAiPC9vbD48L3NlY3Rpb24+IgogICAgICAgICAgICAiPHNlY3Rpb24+PGgyPjIgwrcgVmVyaWZ5IGluIHRoZSBUZXN0IHBhbmU8L2gyPjx1bD4iCiAgICAgICAgICAgICsgcHJvbXB0cyArICI8L3VsPjwvc2VjdGlvbj4iCiAgICAgICAgICAgICI8c2VjdGlvbj48aDI+SWYgYSB0b29sIGFuc3dlcnMgZW1wdHk8L2gyPiIKICAgICAgICAgICAgIjxwIHN0eWxlPSdmb250LXNpemU6MTNweDtjb2xvcjojNjE2MTYxO2xpbmUtaGVpZ2h0OjEuNSc+IgogICAgICAgICAgICAiUmUtcnVuIHRoZSBjb25uZWN0b3IgY29kZSBkZXBsb3kgKHBhYyBjb25uZWN0b3IgdXBkYXRlKSDigJQgdGhlICIKICAgICAgICAgICAgImtub3duIHNldHRsZSBjYXNlIOKAlCB0aGVuIHJldHJ5LiBFdmVyeXRoaW5nIGVsc2UgaXMgYXV0b21hdGVkLiIKICAgICAgICAgICAgIjwvcD48L3NlY3Rpb24+IgogICAgICAgICAgICAiPGJ1dHRvbiBjbGFzcz0nZXhwJyBvbmNsaWNrPSdleHBvcnRIdG1sKCknPkV4cG9ydCB0aGlzIHBhZ2UgIgogICAgICAgICAgICAiKC5odG1sKTwvYnV0dG9uPiIKICAgICAgICAgICAgIjxzY3JpcHQ+ZnVuY3Rpb24gZXhwb3J0SHRtbCgpe3ZhciBiPW5ldyBCbG9iKFsnPCFET0NUWVBFIGh0bWw+JyIKICAgICAgICAgICAgIitkb2N1bWVudC5kb2N1bWVudEVsZW1lbnQub3V0ZXJIVE1MXSx7dHlwZTondGV4dC9odG1sJ30pOyIKICAgICAgICAgICAgInZhciBhPWRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2EnKTthLmhyZWY9VVJMLmNyZWF0ZU9iamVjdFVSTChiKTsiCiAgICAgICAgICAgICJhLmRvd25sb2FkPSciICsgX3NsdWcoc3VpdGVfZGlzcGxheSwgIi0iKQogICAgICAgICAgICArICItbWFudWFsLXN0ZXBzLmh0bWwnO2EuY2xpY2soKTt9PC9zY3JpcHQ+PC9ib2R5PjwvaHRtbD4iKQoKCmRlZiBidWlsZF9ldmFsdWF0aW9uX2NzdihzdWl0ZV9kaXNwbGF5LCBhZ2VudHMpOgogICAgIiIiQ29waWxvdCBTdHVkaW8gRXZhbHVhdGUgaW1wb3J0IENTViBpbiB0aGUgT0ZGSUNJQUwgdGVtcGxhdGUgc2hhcGUKICAgIChVVEYtOCBCT00sIHF1b3RlZCAiIyIgY29tbWVudCBwcmVhbWJsZSwgY29udmVyc2F0aW9uTnVtYmVyL3F1ZXN0aW9uLwogICAgcmVzcG9uc2UsIDw9OCB0dXJucyBwZXIgY29udmVyc2F0aW9uLCA8PTUwIGNvbnZlcnNhdGlvbnMpIHRoYXQgRE9VQkxFUwogICAgYXMgdGhlIGRlbW8gc2NyaXB0OiBjb252ZXJzYXRpb24gMSBpcyB0aGUgY2xpY2staW4tb3JkZXIgZ29sZGVuIHBhdGgKICAgIGFjcm9zcyB0aGUgd2hvbGUgc3VpdGU7IGNvbnZlcnNhdGlvbnMgMi4uTiBmb2N1cyBvbmUgY2FwYWJpbGl0eSBlYWNoLgogICAgUmVmZXJlbmNlIHJlc3BvbnNlcyBhcmUgZ3JvdW5kZWQgaW4gdGhlIHN1aXRlJ3MgU1lOVEhFVElDX0RBVEEgY2Fub24uIiIiCiAgICBkZWYgcSh4KToKICAgICAgICByZXR1cm4gJyInICsgc3RyKHgpLnJlcGxhY2UoJyInLCAnIiInKSArICciJwoKICAgIGRlZiByb3coKmNlbGxzKToKICAgICAgICByZXR1cm4gIiwiLmpvaW4ocShjKSBmb3IgYyBpbiBjZWxscykKCiAgICBsaW5lcyA9IFsKICAgICAgICByb3coIiMgJXMg4oCUIGV2YWx1YXRpb24gc2V0IEFORCBkZW1vIHNjcmlwdC4iICUgc3VpdGVfZGlzcGxheSksCiAgICAgICAgcm93KCIjIFVzZSBpdCB0d2ljZTogKDEpIHJlYWQgdGhlIHF1ZXN0aW9ucyB0b3AtdG8tYm90dG9tIGFzIHlvdXIgIgogICAgICAgICAgICAibGl2ZSBkZW1vIHNjcmlwdDsgKDIpIGltcG9ydCB0aGlzIGZpbGUgdW5jaGFuZ2VkIGluIHRoZSAiCiAgICAgICAgICAgICJhZ2VudCdzIEV2YWx1YXRlIHRhYiB0byBydW4gdGhlIHNhbWUgY29udmVyc2F0aW9ucyBhcyB0ZXN0cy4iKSwKICAgICAgICByb3coIiMgUmVmZXJlbmNlIHJlc3BvbnNlcyBhcmUgZ3JvdW5kZWQgaW4gdGhlIHBhY2thZ2VkIHN5bnRoZXRpYyAiCiAgICAgICAgICAgICJjYW5vbiAodGhlIE1DUCBkYXRhIHNlcnZlcidzIHJlY29yZHMpLiIpLAogICAgICAgIHJvdygiIyIpLAogICAgICAgIHJvdygiY29udmVyc2F0aW9uTnVtYmVyIiwgInF1ZXN0aW9uIiwgInJlc3BvbnNlIiksCiAgICBdCgogICAgZGVmIGdyb3VuZGVkKGEpOgogICAgICAgIHJvd3MgPSBhLmdldCgicm93cyIpIG9yIFtdCiAgICAgICAgaWYgbm90IHJvd3M6CiAgICAgICAgICAgIHJldHVybiBOb25lCiAgICAgICAgZmlyc3QgPSByb3dzWzBdCiAgICAgICAga2V5ID0gYVsia2V5Il0KICAgICAgICBrZXlfdmFsID0gc3RyKGZpcnN0LmdldChrZXksICIiKSkKICAgICAgICBsYWJlbCA9IG5leHQoKHN0cihmaXJzdFtmXSkgZm9yIGYgaW4gZmlyc3QKICAgICAgICAgICAgICAgICAgICAgIGlmICJuYW1lIiBpbiByZS5zdWIociIoW2EtejAtOV0pKFtBLVpdKSIsIHIiXDFfXDIiLCBmKQogICAgICAgICAgICAgICAgICAgICAgLmxvd2VyKCkuc3BsaXQoIl8iKSBhbmQgaXNpbnN0YW5jZShmaXJzdFtmXSwgc3RyKSksICIiKQogICAgICAgIGRldGFpbHMgPSBbc3RyKHYpIGZvciBmLCB2IGluIGZpcnN0Lml0ZW1zKCkKICAgICAgICAgICAgICAgICAgIGlmIGYgIT0ga2V5IGFuZCBpc2luc3RhbmNlKHYsIChzdHIsIGludCwgZmxvYXQpKQogICAgICAgICAgICAgICAgICAgYW5kIDAgPCBsZW4oc3RyKHYpKSA8PSA0OF1bOjNdCiAgICAgICAgcmV0dXJuIGtleV92YWwsIGxhYmVsLCBkZXRhaWxzCgogICAgIyBjb252ZXJzYXRpb24gMTogdGhlIGdvbGRlbiBwYXRoIGFjcm9zcyBldmVyeSBjYXBhYmlsaXR5LCBpbiBvcmRlcgogICAgY29udm8gPSAxCiAgICBmb3IgYSBpbiBhZ2VudHM6CiAgICAgICAgZyA9IGdyb3VuZGVkKGEpCiAgICAgICAgaWYgbm90IGc6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAga2V5X3ZhbCwgbGFiZWwsIGRldGFpbHMgPSBnCiAgICAgICAgdHJpZyA9IChhLmdldCgidHJpZ2dlcnMiKSBvciBbTm9uZV0pWzBdIG9yICgKICAgICAgICAgICAgIlNob3cgJXMgZm9yICVzLiIgJSAoYVsiY2xhc3NfbmFtZSJdLCBrZXlfdmFsKSkKICAgICAgICBsaW5lcy5hcHBlbmQocm93KGNvbnZvLCB0cmlnWzo0OTBdLAogICAgICAgICAgICAgICAgICAgICAgICAgKCJHcm91bmRlZCBhbnN3ZXIgZnJvbSB0aGUgTUNQIGRhdGEgc2VydmVyIGFib3V0ICIKICAgICAgICAgICAgICAgICAgICAgICAgICArIGtleV92YWwgKyAoKCIgKCIgKyBsYWJlbCArICIpIikgaWYgbGFiZWwgZWxzZSAiIikKICAgICAgICAgICAgICAgICAgICAgICAgICArICI6ICIgKyAiOyAiLmpvaW4oZGV0YWlscykpWzo0OTBdKSkKICAgICMgY29udmVyc2F0aW9ucyAyLi5OOiBvbmUgZm9jdXNlZCBjb252ZXJzYXRpb24gcGVyIGNhcGFiaWxpdHkKICAgIGZvciBhIGluIGFnZW50czoKICAgICAgICBnID0gZ3JvdW5kZWQoYSkKICAgICAgICBpZiBub3QgZzoKICAgICAgICAgICAgY29udGludWUKICAgICAgICBjb252byArPSAxCiAgICAgICAga2V5X3ZhbCwgbGFiZWwsIGRldGFpbHMgPSBnCiAgICAgICAgdHJpZ2dlcnMgPSBhLmdldCgidHJpZ2dlcnMiKSBvciBbXQogICAgICAgIGxpc3RfcSA9IG5leHQoKHQgZm9yIHQgaW4gdHJpZ2dlcnMgaWYgImxpc3QiIGluIHQubG93ZXIoKQogICAgICAgICAgICAgICAgICAgICAgIG9yICI/IiBpbiB0KSwgIldoYXQgcmVjb3JkcyBkbyB5b3UgaG9sZCBmb3IgIgogICAgICAgICAgICAgICAgICAgICAgKyBhWyJjbGFzc19uYW1lIl0gKyAiPyIpCiAgICAgICAgbGluZXMuYXBwZW5kKHJvdyhjb252bywgbGlzdF9xWzo0OTBdLAogICAgICAgICAgICAgICAgICAgICAgICAgIkxpc3RzIHRoaXMgY2FwYWJpbGl0eSdzIHJlY29yZHMgZnJvbSB0aGUgTUNQICIKICAgICAgICAgICAgICAgICAgICAgICAgICJkYXRhIHNlcnZlciwgaW5jbHVkaW5nICIgKyBrZXlfdmFsCiAgICAgICAgICAgICAgICAgICAgICAgICArICgoIiAoIiArIGxhYmVsICsgIikiKSBpZiBsYWJlbCBlbHNlICIiKQogICAgICAgICAgICAgICAgICAgICAgICAgKyAiLCB3aXRob3V0IGFza2luZyBmb3IgaW50ZXJuYWwgaWRlbnRpZmllcnMuIikpCiAgICAgICAgbGluZXMuYXBwZW5kKHJvdyhjb252bywKICAgICAgICAgICAgICAgICAgICAgICAgICh0cmlnZ2Vyc1swXSBpZiB0cmlnZ2VycyBlbHNlCiAgICAgICAgICAgICAgICAgICAgICAgICAgIlNob3cgJXMgZm9yICVzLiIgJSAoYVsiY2xhc3NfbmFtZSJdLCBrZXlfdmFsKSlbOjQ5MF0sCiAgICAgICAgICAgICAgICAgICAgICAgICAoIkZ1bGwgcmVjb3JkIGZvciAiICsga2V5X3ZhbCArICI6ICIKICAgICAgICAgICAgICAgICAgICAgICAgICArICI7ICIuam9pbihkZXRhaWxzKQogICAgICAgICAgICAgICAgICAgICAgICAgICsgIi4gUGxhaW4gdGV4dCBvbmx5LCBubyBmYWJyaWNhdGVkIGxpbmtzLiIpWzo0OTBdKSkKICAgICAgICBsaW5lcy5hcHBlbmQocm93KGNvbnZvLCAiV2hhdCBzaG91bGQgSSBkbyBuZXh0PyIsCiAgICAgICAgICAgICAgICAgICAgICAgICAiU3VnZ2VzdHMgdGhlIG5hdHVyYWwgbmV4dCBzdGVwIGluIHRoZSAiCiAgICAgICAgICAgICAgICAgICAgICAgICArIHN1aXRlX2Rpc3BsYXkgKyAiIHByb2Nlc3Mgd2l0aG91dCBpbnZlbnRpbmcgIgogICAgICAgICAgICAgICAgICAgICAgICAgImRhdGEgb3IgbGlua3MuIikpCiAgICByZXR1cm4gIlx1ZmVmZiIgKyAiXG4iLmpvaW4obGluZXMpICsgIlxuIgoKCkZSQU1FV09SS19QQVRIID0gUGF0aChfX2ZpbGVfXykud2l0aF9uYW1lKCJtY3BfZnJhbWV3b3JrLmNzIikKCgpkZWYgZ2VuZXJhdGVfc3VpdGUoYWdlbnRfZGlyLCBzdWl0ZSwgc3VpdGVfZGlzcGxheSwgb3V0X2RpciwKICAgICAgICAgICAgICAgICAgIHByZWZpeD0iZnNpIiwgcHVibGlzaGVyPU5vbmUsIGNoaWxkX3NwbGl0PU5vbmUsCiAgICAgICAgICAgICAgICAgICBza2lsbHM9InRoaW4iKToKICAgICIiIk9uZSBjYWxsOiBoYXJ2ZXN0IGFnZW50LnB5cyAtPiBib3RoIHNvbHV0aW9uIHppcHMgKyBtYW5pZmVzdC4iIiIKICAgIG91dCA9IFBhdGgob3V0X2RpcikKICAgIG91dC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwdWJsaXNoZXIgPSBwdWJsaXNoZXIgb3IgeyJ1bmlxdWUiOiAiRGVmYXVsdFB1Ymxpc2hlciIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICJkaXNwbGF5IjogIkRlZmF1bHQgUHVibGlzaGVyIiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgInByZWZpeCI6IHByZWZpeCwgIm9wdGlvbnZhbHVlIjogMTAwMDB9CiAgICBmcmFtZXdvcmsgPSBGUkFNRVdPUktfUEFUSC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikKICAgIGFnZW50cyA9IGhhcnZlc3RfYWdlbnRzKGFnZW50X2RpcikKICAgIGlmIG5vdCBhZ2VudHM6CiAgICAgICAgcmFpc2UgVmFsdWVFcnJvcigibm8gKl9hZ2VudC5weSBmaWxlcyBmb3VuZCBpbiAlcyIgJSBhZ2VudF9kaXIpCiAgICBjb25uX3ppcCA9IG91dCAvICgiJXNNY3BDb25uZWN0b3JzXzFfMF8wXzEuemlwIiAlIHN1aXRlKQogICAgYWdfemlwID0gb3V0IC8gKCIlc01jcEFnZW50c18xXzBfMF8xLnppcCIgJSBzdWl0ZSkKICAgIGNvbm4gPSBidWlsZF9jb25uZWN0b3JzX3ppcChzdWl0ZSwgc3VpdGVfZGlzcGxheSwgcHJlZml4LCBhZ2VudHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZnJhbWV3b3JrLCBjb25uX3ppcCwgcHVibGlzaGVyKQogICAgYWcgPSBidWlsZF9hZ2VudHNfemlwKHN1aXRlLCBzdWl0ZV9kaXNwbGF5LCBwcmVmaXgsIGFnZW50cywgYWdfemlwLAogICAgICAgICAgICAgICAgICAgICAgICAgIHB1Ymxpc2hlciwgY29ubiwgY2hpbGRfc3BsaXQ9Y2hpbGRfc3BsaXQsCiAgICAgICAgICAgICAgICAgICAgICAgICAgc2tpbGxzPXNraWxscykKICAgIG1hbmlmZXN0ID0gewogICAgICAgICJzdWl0ZSI6IHN1aXRlLCAiZGlzcGxheSI6IHN1aXRlX2Rpc3BsYXksCiAgICAgICAgInNvbHV0aW9ucyI6IFt7Im5hbWUiOiBzdWl0ZSArICJNY3BDb25uZWN0b3JzIiwgInppcCI6IGNvbm5femlwLm5hbWUsCiAgICAgICAgICAgICAgICAgICAgICAgImtpbmQiOiAiY29ubmVjdG9ycyJ9LAogICAgICAgICAgICAgICAgICAgICAgeyJuYW1lIjogc3VpdGUgKyAiTWNwQWdlbnRzIiwgInppcCI6IGFnX3ppcC5uYW1lLAogICAgICAgICAgICAgICAgICAgICAgICJraW5kIjogImFnZW50cyJ9XSwKICAgICAgICAiY29ubmVjdG9yIjogY29ubiwgImFnZW50cyI6IGFnLCAic2tpbGxzX21vZGUiOiBza2lsbHMsCiAgICAgICAgIm1hbnVhbF9zdGVwIjogKCJDb3BpbG90IFN0dWRpbyAtPiAlcyAtPiBUb29scyAtPiBBZGQgYSB0b29sIC0+ICIKICAgICAgICAgICAgICAgICAgICAgICAgIk1vZGVsIENvbnRleHQgUHJvdG9jb2wgLT4gJyVzJyAtPiBjcmVhdGUgdGhlICIKICAgICAgICAgICAgICAgICAgICAgICAgIihuby1hdXRoKSBjb25uZWN0aW9uIC0+IFNhdmUgLT4gUHVibGlzaC4gTm8gQVBJICIKICAgICAgICAgICAgICAgICAgICAgICAgImV4aXN0cyBmb3IgdGhpcyBhdHRhY2guIiAlIChhZ1sicGFyZW50X2Rpc3BsYXkiXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjb25uWyJkaXNwbGF5Il0pKSwKICAgIH0KICAgIG1hbnVhbF9odG1sID0gYnVpbGRfbWFudWFsX3N0ZXBzX2h0bWwoc3VpdGVfZGlzcGxheSwgbWFuaWZlc3QsIGFnZW50cykKICAgIChvdXQgLyAiTUFOVUFMX1NURVBTLmh0bWwiKS53cml0ZV90ZXh0KG1hbnVhbF9odG1sKQogICAgbWFuaWZlc3RbIm1hbnVhbF9zdGVwc19odG1sX2ZpbGUiXSA9ICJNQU5VQUxfU1RFUFMuaHRtbCIKICAgIGV2YWxfY3N2ID0gYnVpbGRfZXZhbHVhdGlvbl9jc3Yoc3VpdGVfZGlzcGxheSwgYWdlbnRzKQogICAgKG91dCAvICJFVkFMVUFUSU9OLmNzdiIpLndyaXRlX3RleHQoZXZhbF9jc3YpCiAgICBtYW5pZmVzdFsiZXZhbHVhdGlvbl9jc3ZfZmlsZSJdID0gIkVWQUxVQVRJT04uY3N2IgogICAgKG91dCAvICJtYW5pZmVzdC5qc29uIikud3JpdGVfdGV4dChqc29uLmR1bXBzKG1hbmlmZXN0LCBpbmRlbnQ9MSkpCiAgICByZXR1cm4gbWFuaWZlc3QK"
_MCP_FRAMEWORK_B64 = "Ly8g4pWRICBTRUNUSU9OIDI6IE1DUCBGUkFNRVdPUksgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkQovLyDilZEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWRCi8vIOKVkSAgQnVpbHQtaW4gTWNwUmVxdWVzdEhhbmRsZXIgdGhhdCBicmluZ3MgTUNQIEMjIFNESyBwYXR0ZXJucyB0byBQb3dlciAgICAgICDilZEKLy8g4pWRICBQbGF0Zm9ybS4gSWYgTWljcm9zb2Z0IGVuYWJsZXMgdGhlIG9mZmljaWFsIFNESyBuYW1lc3BhY2VzLCB0aGlzIHNlY3Rpb24gICDilZEKLy8g4pWRICBiZWNvbWVzIGEgdXNpbmcgc3RhdGVtZW50IGluc3RlYWQgb2YgaW5saW5lIGNvZGUuICAgICAgICAgICAgICAgICAgICAgICAgICDilZEKLy8g4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkQovLyDilZEgIFNwZWMgY292ZXJhZ2U6IE1DUCAyMDI1LTExLTI1ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWRCi8vIOKVkSAgSGFuZGxlczogaW5pdGlhbGl6ZSwgcGluZywgdG9vbHMvKiwgcmVzb3VyY2VzLyosIHByb21wdHMvKiwgICAgICAgICAgICAgICDilZEKLy8g4pWRICAgICAgICAgICBjb21wbGV0aW9uL2NvbXBsZXRlLCBsb2dnaW5nL3NldExldmVsLCBhbGwgbm90aWZpY2F0aW9ucyAgICAgICAgICDilZEKLy8g4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkQovLyDilZEgIFN0YXRlbGVzcyBsaW1pdGF0aW9ucyAoUG93ZXIgUGxhdGZvcm0gY2Fubm90IHNlbmQgYXN5bmMgbm90aWZpY2F0aW9ucyk6ICAg4pWRCi8vIOKVkSAgIC0gVGFza3MgKGV4cGVyaW1lbnRhbCwgcmVxdWlyZXMgcGVyc2lzdGVudCBzdGF0ZSBiZXR3ZWVuIHJlcXVlc3RzKSAgICAgICDilZEKLy8g4pWRICAgLSBTZXJ2ZXLihpJjbGllbnQgcmVxdWVzdHMgKHNhbXBsaW5nLCBlbGljaXRhdGlvbiwgcm9vdHMvbGlzdCkgICAgICAgICAgICAg4pWRCi8vIOKVkSAgIC0gU2VydmVy4oaSY2xpZW50IG5vdGlmaWNhdGlvbnMgKHByb2dyZXNzLCBsb2dnaW5nL21lc3NhZ2UsIGxpc3RfY2hhbmdlZCkgIOKVkQovLyDilZEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWRCi8vIOKVkSAgRG8gbm90IG1vZGlmeSB1bmxlc3MgZXh0ZW5kaW5nIHRoZSBmcmFtZXdvcmsgaXRzZWxmLiAgICAgICAgICAgICAgICAgICAgICDilZEKLy8g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWdCgovLyDilIDilIAgQ29uZmlndXJhdGlvbiBUeXBlcyDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKCi8vLyA8c3VtbWFyeT5TZXJ2ZXIgaWRlbnRpdHkgcmVwb3J0ZWQgaW4gaW5pdGlhbGl6ZSByZXNwb25zZS48L3N1bW1hcnk+CnB1YmxpYyBjbGFzcyBNY3BTZXJ2ZXJJbmZvCnsKICAgIHB1YmxpYyBzdHJpbmcgTmFtZSB7IGdldDsgc2V0OyB9ID0gIm1jcC1zZXJ2ZXIiOwogICAgcHVibGljIHN0cmluZyBWZXJzaW9uIHsgZ2V0OyBzZXQ7IH0gPSAiMS4wLjAiOwogICAgcHVibGljIHN0cmluZyBUaXRsZSB7IGdldDsgc2V0OyB9CiAgICBwdWJsaWMgc3RyaW5nIERlc2NyaXB0aW9uIHsgZ2V0OyBzZXQ7IH0KfQoKLy8vIDxzdW1tYXJ5PkNhcGFiaWxpdGllcyBkZWNsYXJlZCBkdXJpbmcgaW5pdGlhbGl6YXRpb24uPC9zdW1tYXJ5PgpwdWJsaWMgY2xhc3MgTWNwQ2FwYWJpbGl0aWVzCnsKICAgIHB1YmxpYyBib29sIFRvb2xzIHsgZ2V0OyBzZXQ7IH0gPSB0cnVlOwogICAgcHVibGljIGJvb2wgUmVzb3VyY2VzIHsgZ2V0OyBzZXQ7IH0KICAgIHB1YmxpYyBib29sIFByb21wdHMgeyBnZXQ7IHNldDsgfQogICAgcHVibGljIGJvb2wgTG9nZ2luZyB7IGdldDsgc2V0OyB9CiAgICBwdWJsaWMgYm9vbCBDb21wbGV0aW9ucyB7IGdldDsgc2V0OyB9Cn0KCi8vLyA8c3VtbWFyeT5Ub3AtbGV2ZWwgY29uZmlndXJhdGlvbiBmb3IgdGhlIE1DUCBoYW5kbGVyLjwvc3VtbWFyeT4KcHVibGljIGNsYXNzIE1jcFNlcnZlck9wdGlvbnMKewogICAgcHVibGljIE1jcFNlcnZlckluZm8gU2VydmVySW5mbyB7IGdldDsgc2V0OyB9ID0gbmV3IE1jcFNlcnZlckluZm8oKTsKICAgIHB1YmxpYyBzdHJpbmcgUHJvdG9jb2xWZXJzaW9uIHsgZ2V0OyBzZXQ7IH0gPSAiMjAyNS0xMS0yNSI7CiAgICBwdWJsaWMgTWNwQ2FwYWJpbGl0aWVzIENhcGFiaWxpdGllcyB7IGdldDsgc2V0OyB9ID0gbmV3IE1jcENhcGFiaWxpdGllcygpOwogICAgcHVibGljIHN0cmluZyBJbnN0cnVjdGlvbnMgeyBnZXQ7IHNldDsgfQp9CgovLyDilIDilIAgRXJyb3IgSGFuZGxpbmcg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACgovLy8gPHN1bW1hcnk+U3RhbmRhcmQgSlNPTi1SUEMgMi4wIGVycm9yIGNvZGVzIHVzZWQgYnkgTUNQLjwvc3VtbWFyeT4KcHVibGljIGVudW0gTWNwRXJyb3JDb2RlCnsKICAgIFJlcXVlc3RUaW1lb3V0ID0gLTMyMDAwLAogICAgUGFyc2VFcnJvciA9IC0zMjcwMCwKICAgIEludmFsaWRSZXF1ZXN0ID0gLTMyNjAwLAogICAgTWV0aG9kTm90Rm91bmQgPSAtMzI2MDEsCiAgICBJbnZhbGlkUGFyYW1zID0gLTMyNjAyLAogICAgSW50ZXJuYWxFcnJvciA9IC0zMjYwMwp9CgovLy8gPHN1bW1hcnk+Ci8vLyBUaHJvdyBmcm9tIHRvb2wgbWV0aG9kcyB0byBzdXJmYWNlIGEgc3RydWN0dXJlZCBNQ1AgZXJyb3IuCi8vLyBNaXJyb3JzIE1vZGVsQ29udGV4dFByb3RvY29sLk1jcEV4Y2VwdGlvbiBmcm9tIHRoZSBvZmZpY2lhbCBTREsuCi8vLyA8L3N1bW1hcnk+CnB1YmxpYyBjbGFzcyBNY3BFeGNlcHRpb24gOiBFeGNlcHRpb24KewogICAgcHVibGljIE1jcEVycm9yQ29kZSBDb2RlIHsgZ2V0OyB9CiAgICBwdWJsaWMgTWNwRXhjZXB0aW9uKE1jcEVycm9yQ29kZSBjb2RlLCBzdHJpbmcgbWVzc2FnZSkgOiBiYXNlKG1lc3NhZ2UpID0+IENvZGUgPSBjb2RlOwp9CgovLyDilIDilIAgU2NoZW1hIEJ1aWxkZXIgKEZsdWVudCBBUEkpIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAoKLy8vIDxzdW1tYXJ5PkZsdWVudCBidWlsZGVyIGZvciBKU09OIFNjaGVtYSBvYmplY3RzIHVzZWQgaW4gdG9vbCBpbnB1dFNjaGVtYS48L3N1bW1hcnk+CnB1YmxpYyBjbGFzcyBNY3BTY2hlbWFCdWlsZGVyCnsKICAgIHByaXZhdGUgcmVhZG9ubHkgSk9iamVjdCBfcHJvcGVydGllcyA9IG5ldyBKT2JqZWN0KCk7CiAgICBwcml2YXRlIHJlYWRvbmx5IEpBcnJheSBfcmVxdWlyZWQgPSBuZXcgSkFycmF5KCk7CgogICAgcHVibGljIE1jcFNjaGVtYUJ1aWxkZXIgU3RyaW5nKHN0cmluZyBuYW1lLCBzdHJpbmcgZGVzY3JpcHRpb24sIGJvb2wgcmVxdWlyZWQgPSBmYWxzZSwgc3RyaW5nIGZvcm1hdCA9IG51bGwsIHN0cmluZ1tdIGVudW1WYWx1ZXMgPSBudWxsKQogICAgewogICAgICAgIHZhciBwcm9wID0gbmV3IEpPYmplY3QgeyBbInR5cGUiXSA9ICJzdHJpbmciLCBbImRlc2NyaXB0aW9uIl0gPSBkZXNjcmlwdGlvbiB9OwogICAgICAgIGlmIChmb3JtYXQgIT0gbnVsbCkgcHJvcFsiZm9ybWF0Il0gPSBmb3JtYXQ7CiAgICAgICAgaWYgKGVudW1WYWx1ZXMgIT0gbnVsbCkgcHJvcFsiZW51bSJdID0gbmV3IEpBcnJheShlbnVtVmFsdWVzKTsKICAgICAgICBfcHJvcGVydGllc1tuYW1lXSA9IHByb3A7CiAgICAgICAgaWYgKHJlcXVpcmVkKSBfcmVxdWlyZWQuQWRkKG5hbWUpOwogICAgICAgIHJldHVybiB0aGlzOwogICAgfQoKICAgIHB1YmxpYyBNY3BTY2hlbWFCdWlsZGVyIEludGVnZXIoc3RyaW5nIG5hbWUsIHN0cmluZyBkZXNjcmlwdGlvbiwgYm9vbCByZXF1aXJlZCA9IGZhbHNlLCBpbnQ/IGRlZmF1bHRWYWx1ZSA9IG51bGwpCiAgICB7CiAgICAgICAgdmFyIHByb3AgPSBuZXcgSk9iamVjdCB7IFsidHlwZSJdID0gImludGVnZXIiLCBbImRlc2NyaXB0aW9uIl0gPSBkZXNjcmlwdGlvbiB9OwogICAgICAgIGlmIChkZWZhdWx0VmFsdWUuSGFzVmFsdWUpIHByb3BbImRlZmF1bHQiXSA9IGRlZmF1bHRWYWx1ZS5WYWx1ZTsKICAgICAgICBfcHJvcGVydGllc1tuYW1lXSA9IHByb3A7CiAgICAgICAgaWYgKHJlcXVpcmVkKSBfcmVxdWlyZWQuQWRkKG5hbWUpOwogICAgICAgIHJldHVybiB0aGlzOwogICAgfQoKICAgIHB1YmxpYyBNY3BTY2hlbWFCdWlsZGVyIE51bWJlcihzdHJpbmcgbmFtZSwgc3RyaW5nIGRlc2NyaXB0aW9uLCBib29sIHJlcXVpcmVkID0gZmFsc2UpCiAgICB7CiAgICAgICAgX3Byb3BlcnRpZXNbbmFtZV0gPSBuZXcgSk9iamVjdCB7IFsidHlwZSJdID0gIm51bWJlciIsIFsiZGVzY3JpcHRpb24iXSA9IGRlc2NyaXB0aW9uIH07CiAgICAgICAgaWYgKHJlcXVpcmVkKSBfcmVxdWlyZWQuQWRkKG5hbWUpOwogICAgICAgIHJldHVybiB0aGlzOwogICAgfQoKICAgIHB1YmxpYyBNY3BTY2hlbWFCdWlsZGVyIEJvb2xlYW4oc3RyaW5nIG5hbWUsIHN0cmluZyBkZXNjcmlwdGlvbiwgYm9vbCByZXF1aXJlZCA9IGZhbHNlKQogICAgewogICAgICAgIF9wcm9wZXJ0aWVzW25hbWVdID0gbmV3IEpPYmplY3QgeyBbInR5cGUiXSA9ICJib29sZWFuIiwgWyJkZXNjcmlwdGlvbiJdID0gZGVzY3JpcHRpb24gfTsKICAgICAgICBpZiAocmVxdWlyZWQpIF9yZXF1aXJlZC5BZGQobmFtZSk7CiAgICAgICAgcmV0dXJuIHRoaXM7CiAgICB9CgogICAgcHVibGljIE1jcFNjaGVtYUJ1aWxkZXIgQXJyYXkoc3RyaW5nIG5hbWUsIHN0cmluZyBkZXNjcmlwdGlvbiwgSk9iamVjdCBpdGVtU2NoZW1hLCBib29sIHJlcXVpcmVkID0gZmFsc2UpCiAgICB7CiAgICAgICAgX3Byb3BlcnRpZXNbbmFtZV0gPSBuZXcgSk9iamVjdAogICAgICAgIHsKICAgICAgICAgICAgWyJ0eXBlIl0gPSAiYXJyYXkiLAogICAgICAgICAgICBbImRlc2NyaXB0aW9uIl0gPSBkZXNjcmlwdGlvbiwKICAgICAgICAgICAgWyJpdGVtcyJdID0gaXRlbVNjaGVtYQogICAgICAgIH07CiAgICAgICAgaWYgKHJlcXVpcmVkKSBfcmVxdWlyZWQuQWRkKG5hbWUpOwogICAgICAgIHJldHVybiB0aGlzOwogICAgfQoKICAgIHB1YmxpYyBNY3BTY2hlbWFCdWlsZGVyIE9iamVjdChzdHJpbmcgbmFtZSwgc3RyaW5nIGRlc2NyaXB0aW9uLCBBY3Rpb248TWNwU2NoZW1hQnVpbGRlcj4gbmVzdGVkQ29uZmlnLCBib29sIHJlcXVpcmVkID0gZmFsc2UpCiAgICB7CiAgICAgICAgdmFyIG5lc3RlZCA9IG5ldyBNY3BTY2hlbWFCdWlsZGVyKCk7CiAgICAgICAgbmVzdGVkQ29uZmlnPy5JbnZva2UobmVzdGVkKTsKICAgICAgICB2YXIgb2JqID0gbmVzdGVkLkJ1aWxkKCk7CiAgICAgICAgb2JqWyJkZXNjcmlwdGlvbiJdID0gZGVzY3JpcHRpb247CiAgICAgICAgX3Byb3BlcnRpZXNbbmFtZV0gPSBvYmo7CiAgICAgICAgaWYgKHJlcXVpcmVkKSBfcmVxdWlyZWQuQWRkKG5hbWUpOwogICAgICAgIHJldHVybiB0aGlzOwogICAgfQoKICAgIHB1YmxpYyBKT2JqZWN0IEJ1aWxkKCkKICAgIHsKICAgICAgICB2YXIgc2NoZW1hID0gbmV3IEpPYmplY3QKICAgICAgICB7CiAgICAgICAgICAgIFsidHlwZSJdID0gIm9iamVjdCIsCiAgICAgICAgICAgIFsicHJvcGVydGllcyJdID0gX3Byb3BlcnRpZXMKICAgICAgICB9OwogICAgICAgIGlmIChfcmVxdWlyZWQuQ291bnQgPiAwKSBzY2hlbWFbInJlcXVpcmVkIl0gPSBfcmVxdWlyZWQ7CiAgICAgICAgcmV0dXJuIHNjaGVtYTsKICAgIH0KfQoKLy8g4pSA4pSAIEludGVybmFsIFRvb2wgUmVnaXN0cmF0aW9uIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAoKaW50ZXJuYWwgY2xhc3MgTWNwVG9vbERlZmluaXRpb24KewogICAgcHVibGljIHN0cmluZyBOYW1lIHsgZ2V0OyBzZXQ7IH0KICAgIHB1YmxpYyBzdHJpbmcgVGl0bGUgeyBnZXQ7IHNldDsgfQogICAgcHVibGljIHN0cmluZyBEZXNjcmlwdGlvbiB7IGdldDsgc2V0OyB9CiAgICBwdWJsaWMgSk9iamVjdCBJbnB1dFNjaGVtYSB7IGdldDsgc2V0OyB9CiAgICBwdWJsaWMgSk9iamVjdCBPdXRwdXRTY2hlbWEgeyBnZXQ7IHNldDsgfQogICAgcHVibGljIEpPYmplY3QgQW5ub3RhdGlvbnMgeyBnZXQ7IHNldDsgfQogICAgcHVibGljIEZ1bmM8Sk9iamVjdCwgQ2FuY2VsbGF0aW9uVG9rZW4sIFRhc2s8b2JqZWN0Pj4gSGFuZGxlciB7IGdldDsgc2V0OyB9Cn0KCi8vIOKUgOKUgCBJbnRlcm5hbCBSZXNvdXJjZSBSZWdpc3RyYXRpb24g4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACgppbnRlcm5hbCBjbGFzcyBNY3BSZXNvdXJjZURlZmluaXRpb24KewogICAgcHVibGljIHN0cmluZyBVcmkgeyBnZXQ7IHNldDsgfQogICAgcHVibGljIHN0cmluZyBOYW1lIHsgZ2V0OyBzZXQ7IH0KICAgIHB1YmxpYyBzdHJpbmcgRGVzY3JpcHRpb24geyBnZXQ7IHNldDsgfQogICAgcHVibGljIHN0cmluZyBNaW1lVHlwZSB7IGdldDsgc2V0OyB9CiAgICBwdWJsaWMgSk9iamVjdCBBbm5vdGF0aW9ucyB7IGdldDsgc2V0OyB9CiAgICBwdWJsaWMgRnVuYzxDYW5jZWxsYXRpb25Ub2tlbiwgVGFzazxKQXJyYXk+PiBIYW5kbGVyIHsgZ2V0OyBzZXQ7IH0KfQoKaW50ZXJuYWwgY2xhc3MgTWNwUmVzb3VyY2VUZW1wbGF0ZURlZmluaXRpb24KewogICAgcHVibGljIHN0cmluZyBVcmlUZW1wbGF0ZSB7IGdldDsgc2V0OyB9CiAgICBwdWJsaWMgc3RyaW5nIE5hbWUgeyBnZXQ7IHNldDsgfQogICAgcHVibGljIHN0cmluZyBEZXNjcmlwdGlvbiB7IGdldDsgc2V0OyB9CiAgICBwdWJsaWMgc3RyaW5nIE1pbWVUeXBlIHsgZ2V0OyBzZXQ7IH0KICAgIHB1YmxpYyBKT2JqZWN0IEFubm90YXRpb25zIHsgZ2V0OyBzZXQ7IH0KICAgIHB1YmxpYyBGdW5jPHN0cmluZywgQ2FuY2VsbGF0aW9uVG9rZW4sIFRhc2s8SkFycmF5Pj4gSGFuZGxlciB7IGdldDsgc2V0OyB9Cn0KCi8vIOKUgOKUgCBJbnRlcm5hbCBQcm9tcHQgUmVnaXN0cmF0aW9uIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAoKLy8vIDxzdW1tYXJ5PkRlc2NyaWJlcyBhIHNpbmdsZSBwcm9tcHQgYXJndW1lbnQuPC9zdW1tYXJ5PgpwdWJsaWMgY2xhc3MgTWNwUHJvbXB0QXJndW1lbnQKewogICAgcHVibGljIHN0cmluZyBOYW1lIHsgZ2V0OyBzZXQ7IH0KICAgIHB1YmxpYyBzdHJpbmcgRGVzY3JpcHRpb24geyBnZXQ7IHNldDsgfQogICAgcHVibGljIGJvb2wgUmVxdWlyZWQgeyBnZXQ7IHNldDsgfQp9CgppbnRlcm5hbCBjbGFzcyBNY3BQcm9tcHREZWZpbml0aW9uCnsKICAgIHB1YmxpYyBzdHJpbmcgTmFtZSB7IGdldDsgc2V0OyB9CiAgICBwdWJsaWMgc3RyaW5nIERlc2NyaXB0aW9uIHsgZ2V0OyBzZXQ7IH0KICAgIHB1YmxpYyBMaXN0PE1jcFByb21wdEFyZ3VtZW50PiBBcmd1bWVudHMgeyBnZXQ7IHNldDsgfSA9IG5ldyBMaXN0PE1jcFByb21wdEFyZ3VtZW50PigpOwogICAgcHVibGljIEZ1bmM8Sk9iamVjdCwgQ2FuY2VsbGF0aW9uVG9rZW4sIFRhc2s8SkFycmF5Pj4gSGFuZGxlciB7IGdldDsgc2V0OyB9Cn0KCi8vIOKUgOKUgCBNY3BSZXF1ZXN0SGFuZGxlciDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKLy8KLy8gICAgVGhlIGNvcmUgYnJpZGdlIGNsYXNzLiBTdGF0ZWxlc3MsIG5vIERJLCBubyBBU1AuTkVUIENvcmUuCi8vICAgIFRha2VzIGEgSlNPTi1SUEMgc3RyaW5nIGluIOKGkiByZXR1cm5zIGEgSlNPTi1SUEMgc3RyaW5nIG91dC4KLy8gICAgVGhpcyBpcyB0aGUgY2xhc3MgdGhhdCBkb2VzIG5vdCBleGlzdCBpbiB0aGUgb2ZmaWNpYWwgU0RLIHRvZGF5LgovLwoKLy8vIDxzdW1tYXJ5PgovLy8gU3RhdGVsZXNzIE1DUCByZXF1ZXN0IGhhbmRsZXIgdGhhdCBicmlkZ2VzIHRoZSBvZmZpY2lhbCBTREsncyBwYXR0ZXJucwovLy8gdG8gUG93ZXIgUGxhdGZvcm0ncyBTY3JpcHRCYXNlLkV4ZWN1dGVBc3luYygpIG1vZGVsLgovLy8gCi8vLyBIYW5kbGVzIGFsbCBKU09OLVJQQyAyLjAgcm91dGluZywgcHJvdG9jb2wgbmVnb3RpYXRpb24sIHRvb2wgZGlzY292ZXJ5LAovLy8gcGFyYW1ldGVyIGJpbmRpbmcsIGFuZCByZXNwb25zZSBmb3JtYXR0aW5nIGludGVybmFsbHkuCi8vLyA8L3N1bW1hcnk+CnB1YmxpYyBjbGFzcyBNY3BSZXF1ZXN0SGFuZGxlcgp7CiAgICBwcml2YXRlIHJlYWRvbmx5IE1jcFNlcnZlck9wdGlvbnMgX29wdGlvbnM7CiAgICBwcml2YXRlIHJlYWRvbmx5IERpY3Rpb25hcnk8c3RyaW5nLCBNY3BUb29sRGVmaW5pdGlvbj4gX3Rvb2xzOwogICAgcHJpdmF0ZSByZWFkb25seSBEaWN0aW9uYXJ5PHN0cmluZywgTWNwUmVzb3VyY2VEZWZpbml0aW9uPiBfcmVzb3VyY2VzOwogICAgcHJpdmF0ZSByZWFkb25seSBMaXN0PE1jcFJlc291cmNlVGVtcGxhdGVEZWZpbml0aW9uPiBfcmVzb3VyY2VUZW1wbGF0ZXM7CiAgICBwcml2YXRlIHJlYWRvbmx5IERpY3Rpb25hcnk8c3RyaW5nLCBNY3BQcm9tcHREZWZpbml0aW9uPiBfcHJvbXB0czsKCiAgICAvLy8gPHN1bW1hcnk+CiAgICAvLy8gT3B0aW9uYWwgbG9nZ2luZyBjYWxsYmFjay4gV2lyZSB0aGlzIHVwIHRvIEFwcGxpY2F0aW9uIEluc2lnaHRzLAogICAgLy8vIENvbnRleHQuTG9nZ2VyLCBvciBhbnkgb3RoZXIgdGVsZW1ldHJ5IHNpbmsuCiAgICAvLy8gPC9zdW1tYXJ5PgogICAgcHVibGljIEFjdGlvbjxzdHJpbmcsIG9iamVjdD4gT25Mb2cgeyBnZXQ7IHNldDsgfQoKICAgIHB1YmxpYyBNY3BSZXF1ZXN0SGFuZGxlcihNY3BTZXJ2ZXJPcHRpb25zIG9wdGlvbnMpCiAgICB7CiAgICAgICAgX29wdGlvbnMgPSBvcHRpb25zID8/IHRocm93IG5ldyBBcmd1bWVudE51bGxFeGNlcHRpb24obmFtZW9mKG9wdGlvbnMpKTsKICAgICAgICBfdG9vbHMgPSBuZXcgRGljdGlvbmFyeTxzdHJpbmcsIE1jcFRvb2xEZWZpbml0aW9uPihTdHJpbmdDb21wYXJlci5PcmRpbmFsSWdub3JlQ2FzZSk7CiAgICAgICAgX3Jlc291cmNlcyA9IG5ldyBEaWN0aW9uYXJ5PHN0cmluZywgTWNwUmVzb3VyY2VEZWZpbml0aW9uPihTdHJpbmdDb21wYXJlci5PcmRpbmFsSWdub3JlQ2FzZSk7CiAgICAgICAgX3Jlc291cmNlVGVtcGxhdGVzID0gbmV3IExpc3Q8TWNwUmVzb3VyY2VUZW1wbGF0ZURlZmluaXRpb24+KCk7CiAgICAgICAgX3Byb21wdHMgPSBuZXcgRGljdGlvbmFyeTxzdHJpbmcsIE1jcFByb21wdERlZmluaXRpb24+KFN0cmluZ0NvbXBhcmVyLk9yZGluYWxJZ25vcmVDYXNlKTsKICAgIH0KCiAgICAvLyDilIDilIAgVG9vbCBSZWdpc3RyYXRpb24g4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACgogICAgLy8vIDxzdW1tYXJ5PgogICAgLy8vIFJlZ2lzdGVyIGEgdG9vbCB1c2luZyB0aGUgZmx1ZW50IEFQSS4KICAgIC8vLyBEZWZpbmUgdGhlIHNjaGVtYSB3aXRoIE1jcFNjaGVtYUJ1aWxkZXIsIHByb3ZpZGUgYSBoYW5kbGVyLCBhbmQgb3B0aW9uYWxseSBzZXQgYW5ub3RhdGlvbnMuCiAgICAvLy8gPC9zdW1tYXJ5PgogICAgcHVibGljIE1jcFJlcXVlc3RIYW5kbGVyIEFkZFRvb2woCiAgICAgICAgc3RyaW5nIG5hbWUsCiAgICAgICAgc3RyaW5nIGRlc2NyaXB0aW9uLAogICAgICAgIEFjdGlvbjxNY3BTY2hlbWFCdWlsZGVyPiBzY2hlbWFDb25maWcsCiAgICAgICAgRnVuYzxKT2JqZWN0LCBDYW5jZWxsYXRpb25Ub2tlbiwgVGFzazxKT2JqZWN0Pj4gaGFuZGxlciwKICAgICAgICBBY3Rpb248Sk9iamVjdD4gYW5ub3RhdGlvbnNDb25maWcgPSBudWxsLAogICAgICAgIHN0cmluZyB0aXRsZSA9IG51bGwsCiAgICAgICAgQWN0aW9uPE1jcFNjaGVtYUJ1aWxkZXI+IG91dHB1dFNjaGVtYUNvbmZpZyA9IG51bGwpCiAgICB7CiAgICAgICAgdmFyIGJ1aWxkZXIgPSBuZXcgTWNwU2NoZW1hQnVpbGRlcigpOwogICAgICAgIHNjaGVtYUNvbmZpZz8uSW52b2tlKGJ1aWxkZXIpOwoKICAgICAgICBKT2JqZWN0IGFubm90YXRpb25zID0gbnVsbDsKICAgICAgICBpZiAoYW5ub3RhdGlvbnNDb25maWcgIT0gbnVsbCkKICAgICAgICB7CiAgICAgICAgICAgIGFubm90YXRpb25zID0gbmV3IEpPYmplY3QoKTsKICAgICAgICAgICAgYW5ub3RhdGlvbnNDb25maWcoYW5ub3RhdGlvbnMpOwogICAgICAgIH0KCiAgICAgICAgSk9iamVjdCBvdXRwdXRTY2hlbWEgPSBudWxsOwogICAgICAgIGlmIChvdXRwdXRTY2hlbWFDb25maWcgIT0gbnVsbCkKICAgICAgICB7CiAgICAgICAgICAgIHZhciBvdXRCdWlsZGVyID0gbmV3IE1jcFNjaGVtYUJ1aWxkZXIoKTsKICAgICAgICAgICAgb3V0cHV0U2NoZW1hQ29uZmlnKG91dEJ1aWxkZXIpOwogICAgICAgICAgICBvdXRwdXRTY2hlbWEgPSBvdXRCdWlsZGVyLkJ1aWxkKCk7CiAgICAgICAgfQoKICAgICAgICBfdG9vbHNbbmFtZV0gPSBuZXcgTWNwVG9vbERlZmluaXRpb24KICAgICAgICB7CiAgICAgICAgICAgIE5hbWUgPSBuYW1lLAogICAgICAgICAgICBUaXRsZSA9IHRpdGxlLAogICAgICAgICAgICBEZXNjcmlwdGlvbiA9IGRlc2NyaXB0aW9uLAogICAgICAgICAgICBJbnB1dFNjaGVtYSA9IGJ1aWxkZXIuQnVpbGQoKSwKICAgICAgICAgICAgT3V0cHV0U2NoZW1hID0gb3V0cHV0U2NoZW1hLAogICAgICAgICAgICBBbm5vdGF0aW9ucyA9IGFubm90YXRpb25zLAogICAgICAgICAgICBIYW5kbGVyID0gYXN5bmMgKGFyZ3MsIGN0KSA9PiBhd2FpdCBoYW5kbGVyKGFyZ3MsIGN0KS5Db25maWd1cmVBd2FpdChmYWxzZSkKICAgICAgICB9OwoKICAgICAgICByZXR1cm4gdGhpczsKICAgIH0KCiAgICAvLyDilIDilIAgUmVzb3VyY2UgUmVnaXN0cmF0aW9uIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAoKICAgIC8vLyA8c3VtbWFyeT4KICAgIC8vLyBSZWdpc3RlciBhIHN0YXRpYyByZXNvdXJjZS4gVGhlIGhhbmRsZXIgcmV0dXJucyB0aGUgcmVzb3VyY2UgY29udGVudHMKICAgIC8vLyBhcyBhIEpBcnJheSBvZiB7dXJpLCB0ZXh0LCBtaW1lVHlwZX0gb3Ige3VyaSwgYmxvYiwgbWltZVR5cGV9IG9iamVjdHMuCiAgICAvLy8gPC9zdW1tYXJ5PgogICAgcHVibGljIE1jcFJlcXVlc3RIYW5kbGVyIEFkZFJlc291cmNlKAogICAgICAgIHN0cmluZyB1cmksCiAgICAgICAgc3RyaW5nIG5hbWUsCiAgICAgICAgc3RyaW5nIGRlc2NyaXB0aW9uLAogICAgICAgIEZ1bmM8Q2FuY2VsbGF0aW9uVG9rZW4sIFRhc2s8SkFycmF5Pj4gaGFuZGxlciwKICAgICAgICBzdHJpbmcgbWltZVR5cGUgPSAiYXBwbGljYXRpb24vanNvbiIsCiAgICAgICAgQWN0aW9uPEpPYmplY3Q+IGFubm90YXRpb25zQ29uZmlnID0gbnVsbCkKICAgIHsKICAgICAgICBKT2JqZWN0IGFubm90YXRpb25zID0gbnVsbDsKICAgICAgICBpZiAoYW5ub3RhdGlvbnNDb25maWcgIT0gbnVsbCkKICAgICAgICB7CiAgICAgICAgICAgIGFubm90YXRpb25zID0gbmV3IEpPYmplY3QoKTsKICAgICAgICAgICAgYW5ub3RhdGlvbnNDb25maWcoYW5ub3RhdGlvbnMpOwogICAgICAgIH0KCiAgICAgICAgX3Jlc291cmNlc1t1cmldID0gbmV3IE1jcFJlc291cmNlRGVmaW5pdGlvbgogICAgICAgIHsKICAgICAgICAgICAgVXJpID0gdXJpLAogICAgICAgICAgICBOYW1lID0gbmFtZSwKICAgICAgICAgICAgRGVzY3JpcHRpb24gPSBkZXNjcmlwdGlvbiwKICAgICAgICAgICAgTWltZVR5cGUgPSBtaW1lVHlwZSwKICAgICAgICAgICAgQW5ub3RhdGlvbnMgPSBhbm5vdGF0aW9ucywKICAgICAgICAgICAgSGFuZGxlciA9IGhhbmRsZXIKICAgICAgICB9OwoKICAgICAgICByZXR1cm4gdGhpczsKICAgIH0KCiAgICAvLy8gPHN1bW1hcnk+CiAgICAvLy8gUmVnaXN0ZXIgYSByZXNvdXJjZSB0ZW1wbGF0ZS4gVGhlIGhhbmRsZXIgcmVjZWl2ZXMgdGhlIHJlc29sdmVkIFVSSQogICAgLy8vIGFuZCByZXR1cm5zIHRoZSByZXNvdXJjZSBjb250ZW50cyBhcyBhIEpBcnJheS4KICAgIC8vLyA8L3N1bW1hcnk+CiAgICBwdWJsaWMgTWNwUmVxdWVzdEhhbmRsZXIgQWRkUmVzb3VyY2VUZW1wbGF0ZSgKICAgICAgICBzdHJpbmcgdXJpVGVtcGxhdGUsCiAgICAgICAgc3RyaW5nIG5hbWUsCiAgICAgICAgc3RyaW5nIGRlc2NyaXB0aW9uLAogICAgICAgIEZ1bmM8c3RyaW5nLCBDYW5jZWxsYXRpb25Ub2tlbiwgVGFzazxKQXJyYXk+PiBoYW5kbGVyLAogICAgICAgIHN0cmluZyBtaW1lVHlwZSA9ICJhcHBsaWNhdGlvbi9qc29uIiwKICAgICAgICBBY3Rpb248Sk9iamVjdD4gYW5ub3RhdGlvbnNDb25maWcgPSBudWxsKQogICAgewogICAgICAgIEpPYmplY3QgYW5ub3RhdGlvbnMgPSBudWxsOwogICAgICAgIGlmIChhbm5vdGF0aW9uc0NvbmZpZyAhPSBudWxsKQogICAgICAgIHsKICAgICAgICAgICAgYW5ub3RhdGlvbnMgPSBuZXcgSk9iamVjdCgpOwogICAgICAgICAgICBhbm5vdGF0aW9uc0NvbmZpZyhhbm5vdGF0aW9ucyk7CiAgICAgICAgfQoKICAgICAgICBfcmVzb3VyY2VUZW1wbGF0ZXMuQWRkKG5ldyBNY3BSZXNvdXJjZVRlbXBsYXRlRGVmaW5pdGlvbgogICAgICAgIHsKICAgICAgICAgICAgVXJpVGVtcGxhdGUgPSB1cmlUZW1wbGF0ZSwKICAgICAgICAgICAgTmFtZSA9IG5hbWUsCiAgICAgICAgICAgIERlc2NyaXB0aW9uID0gZGVzY3JpcHRpb24sCiAgICAgICAgICAgIE1pbWVUeXBlID0gbWltZVR5cGUsCiAgICAgICAgICAgIEFubm90YXRpb25zID0gYW5ub3RhdGlvbnMsCiAgICAgICAgICAgIEhhbmRsZXIgPSBoYW5kbGVyCiAgICAgICAgfSk7CgogICAgICAgIHJldHVybiB0aGlzOwogICAgfQoKICAgIC8vIOKUgOKUgCBQcm9tcHQgUmVnaXN0cmF0aW9uIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgAoKICAgIC8vLyA8c3VtbWFyeT4KICAgIC8vLyBSZWdpc3RlciBhIHByb21wdC4gVGhlIGhhbmRsZXIgcmVjZWl2ZXMgdGhlIGFyZ3VtZW50IHZhbHVlcyBhcyBhIEpPYmplY3QKICAgIC8vLyBhbmQgcmV0dXJucyBhIEpBcnJheSBvZiBtZXNzYWdlIG9iamVjdHMgKHtyb2xlLCBjb250ZW50OiB7dHlwZSwgdGV4dH19KS4KICAgIC8vLyA8L3N1bW1hcnk+CiAgICBwdWJsaWMgTWNwUmVxdWVzdEhhbmRsZXIgQWRkUHJvbXB0KAogICAgICAgIHN0cmluZyBuYW1lLAogICAgICAgIHN0cmluZyBkZXNjcmlwdGlvbiwKICAgICAgICBMaXN0PE1jcFByb21wdEFyZ3VtZW50PiBhcmd1bWVudHMsCiAgICAgICAgRnVuYzxKT2JqZWN0LCBDYW5jZWxsYXRpb25Ub2tlbiwgVGFzazxKQXJyYXk+PiBoYW5kbGVyKQogICAgewogICAgICAgIF9wcm9tcHRzW25hbWVdID0gbmV3IE1jcFByb21wdERlZmluaXRpb24KICAgICAgICB7CiAgICAgICAgICAgIE5hbWUgPSBuYW1lLAogICAgICAgICAgICBEZXNjcmlwdGlvbiA9IGRlc2NyaXB0aW9uLAogICAgICAgICAgICBBcmd1bWVudHMgPSBhcmd1bWVudHMgPz8gbmV3IExpc3Q8TWNwUHJvbXB0QXJndW1lbnQ+KCksCiAgICAgICAgICAgIEhhbmRsZXIgPSBoYW5kbGVyCiAgICAgICAgfTsKCiAgICAgICAgcmV0dXJuIHRoaXM7CiAgICB9CgogICAgLy8g4pSA4pSAIE1haW4gSGFuZGxlciDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKCiAgICAvLy8gPHN1bW1hcnk+CiAgICAvLy8gUHJvY2VzcyBhIHJhdyBKU09OLVJQQyAyLjAgcmVxdWVzdCBzdHJpbmcgYW5kIHJldHVybiBhIEpTT04tUlBDIHJlc3BvbnNlIHN0cmluZy4KICAgIC8vLyBUaGlzIGlzIHRoZSBzaW5nbGUgbWV0aG9kIHRoYXQgYnJpZGdlcyB0aGUgZ2FwLgogICAgLy8vIDwvc3VtbWFyeT4KICAgIHB1YmxpYyBhc3luYyBUYXNrPHN0cmluZz4gSGFuZGxlQXN5bmMoc3RyaW5nIGJvZHksIENhbmNlbGxhdGlvblRva2VuIGNhbmNlbGxhdGlvblRva2VuKQogICAgewogICAgICAgIGlmIChzdHJpbmcuSXNOdWxsT3JXaGl0ZVNwYWNlKGJvZHkpKQogICAgICAgICAgICByZXR1cm4gU2VyaWFsaXplRXJyb3IobnVsbCwgTWNwRXJyb3JDb2RlLkludmFsaWRSZXF1ZXN0LCAiRW1wdHkgcmVxdWVzdCBib2R5Iik7CgogICAgICAgIEpPYmplY3QgcmVxdWVzdDsKICAgICAgICB0cnkKICAgICAgICB7CiAgICAgICAgICAgIHJlcXVlc3QgPSBKT2JqZWN0LlBhcnNlKGJvZHkpOwogICAgICAgIH0KICAgICAgICBjYXRjaCAoSnNvbkV4Y2VwdGlvbikKICAgICAgICB7CiAgICAgICAgICAgIHJldHVybiBTZXJpYWxpemVFcnJvcihudWxsLCBNY3BFcnJvckNvZGUuUGFyc2VFcnJvciwgIkludmFsaWQgSlNPTiIpOwogICAgICAgIH0KCiAgICAgICAgdmFyIG1ldGhvZCA9IHJlcXVlc3QuVmFsdWU8c3RyaW5nPigibWV0aG9kIikgPz8gc3RyaW5nLkVtcHR5OwogICAgICAgIHZhciBpZCA9IHJlcXVlc3RbImlkIl07CgogICAgICAgIExvZygiTWNwUmVxdWVzdFJlY2VpdmVkIiwgbmV3IHsgTWV0aG9kID0gbWV0aG9kLCBIYXNJZCA9IGlkICE9IG51bGwgfSk7CgogICAgICAgIHRyeQogICAgICAgIHsKICAgICAgICAgICAgc3dpdGNoIChtZXRob2QpCiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgIC8vIENvcmUgaW5pdGlhbGl6YXRpb24KICAgICAgICAgICAgICAgIGNhc2UgImluaXRpYWxpemUiOgogICAgICAgICAgICAgICAgICAgIHJldHVybiBIYW5kbGVJbml0aWFsaXplKGlkLCByZXF1ZXN0KTsKCiAgICAgICAgICAgICAgICAvLyBOb3RpZmljYXRpb25zIOKAlCBDb3BpbG90IFN0dWRpbyByZXF1aXJlcyB2YWxpZCBKU09OLVJQQyBmb3IgQUxMIHJlcXVlc3RzCiAgICAgICAgICAgICAgICBjYXNlICJpbml0aWFsaXplZCI6CiAgICAgICAgICAgICAgICBjYXNlICJub3RpZmljYXRpb25zL2luaXRpYWxpemVkIjoKICAgICAgICAgICAgICAgIGNhc2UgIm5vdGlmaWNhdGlvbnMvY2FuY2VsbGVkIjoKICAgICAgICAgICAgICAgIGNhc2UgIm5vdGlmaWNhdGlvbnMvcm9vdHMvbGlzdF9jaGFuZ2VkIjoKICAgICAgICAgICAgICAgICAgICByZXR1cm4gU2VyaWFsaXplU3VjY2VzcyhpZCwgbmV3IEpPYmplY3QoKSk7CgogICAgICAgICAgICAgICAgLy8gSGVhbHRoIGNoZWNrCiAgICAgICAgICAgICAgICBjYXNlICJwaW5nIjoKICAgICAgICAgICAgICAgICAgICByZXR1cm4gU2VyaWFsaXplU3VjY2VzcyhpZCwgbmV3IEpPYmplY3QoKSk7CgogICAgICAgICAgICAgICAgLy8gVG9vbHMKICAgICAgICAgICAgICAgIGNhc2UgInRvb2xzL2xpc3QiOgogICAgICAgICAgICAgICAgICAgIHJldHVybiBIYW5kbGVUb29sc0xpc3QoaWQpOwoKICAgICAgICAgICAgICAgIGNhc2UgInRvb2xzL2NhbGwiOgogICAgICAgICAgICAgICAgICAgIHJldHVybiBhd2FpdCBIYW5kbGVUb29sc0NhbGxBc3luYyhpZCwgcmVxdWVzdCwgY2FuY2VsbGF0aW9uVG9rZW4pLkNvbmZpZ3VyZUF3YWl0KGZhbHNlKTsKCiAgICAgICAgICAgICAgICAvLyBSZXNvdXJjZXMKICAgICAgICAgICAgICAgIGNhc2UgInJlc291cmNlcy9saXN0IjoKICAgICAgICAgICAgICAgICAgICByZXR1cm4gSGFuZGxlUmVzb3VyY2VzTGlzdChpZCk7CgogICAgICAgICAgICAgICAgY2FzZSAicmVzb3VyY2VzL3RlbXBsYXRlcy9saXN0IjoKICAgICAgICAgICAgICAgICAgICByZXR1cm4gSGFuZGxlUmVzb3VyY2VUZW1wbGF0ZXNMaXN0KGlkKTsKCiAgICAgICAgICAgICAgICBjYXNlICJyZXNvdXJjZXMvcmVhZCI6CiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIGF3YWl0IEhhbmRsZVJlc291cmNlc1JlYWRBc3luYyhpZCwgcmVxdWVzdCwgY2FuY2VsbGF0aW9uVG9rZW4pLkNvbmZpZ3VyZUF3YWl0KGZhbHNlKTsKCiAgICAgICAgICAgICAgICBjYXNlICJyZXNvdXJjZXMvc3Vic2NyaWJlIjoKICAgICAgICAgICAgICAgIGNhc2UgInJlc291cmNlcy91bnN1YnNjcmliZSI6CiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZVN1Y2Nlc3MoaWQsIG5ldyBKT2JqZWN0KCkpOwoKICAgICAgICAgICAgICAgIC8vIFByb21wdHMKICAgICAgICAgICAgICAgIGNhc2UgInByb21wdHMvbGlzdCI6CiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIEhhbmRsZVByb21wdHNMaXN0KGlkKTsKCiAgICAgICAgICAgICAgICBjYXNlICJwcm9tcHRzL2dldCI6CiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIGF3YWl0IEhhbmRsZVByb21wdHNHZXRBc3luYyhpZCwgcmVxdWVzdCwgY2FuY2VsbGF0aW9uVG9rZW4pLkNvbmZpZ3VyZUF3YWl0KGZhbHNlKTsKCiAgICAgICAgICAgICAgICAvLyBDb21wbGV0aW9ucwogICAgICAgICAgICAgICAgY2FzZSAiY29tcGxldGlvbi9jb21wbGV0ZSI6CiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZVN1Y2Nlc3MoaWQsIG5ldyBKT2JqZWN0CiAgICAgICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgICAgICBbImNvbXBsZXRpb24iXSA9IG5ldyBKT2JqZWN0CiAgICAgICAgICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICAgICAgICAgIFsidmFsdWVzIl0gPSBuZXcgSkFycmF5KCksCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBbInRvdGFsIl0gPSAwLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgWyJoYXNNb3JlIl0gPSBmYWxzZQogICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgfSk7CgogICAgICAgICAgICAgICAgLy8gTG9nZ2luZyBsZXZlbAogICAgICAgICAgICAgICAgY2FzZSAibG9nZ2luZy9zZXRMZXZlbCI6CiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZVN1Y2Nlc3MoaWQsIG5ldyBKT2JqZWN0KCkpOwoKICAgICAgICAgICAgICAgIGRlZmF1bHQ6CiAgICAgICAgICAgICAgICAgICAgTG9nKCJNY3BNZXRob2ROb3RGb3VuZCIsIG5ldyB7IE1ldGhvZCA9IG1ldGhvZCB9KTsKICAgICAgICAgICAgICAgICAgICByZXR1cm4gU2VyaWFsaXplRXJyb3IoaWQsIE1jcEVycm9yQ29kZS5NZXRob2ROb3RGb3VuZCwgIk1ldGhvZCBub3QgZm91bmQiLCBtZXRob2QpOwogICAgICAgICAgICB9CiAgICAgICAgfQogICAgICAgIGNhdGNoIChNY3BFeGNlcHRpb24gZXgpCiAgICAgICAgewogICAgICAgICAgICBMb2coIk1jcEVycm9yIiwgbmV3IHsgTWV0aG9kID0gbWV0aG9kLCBDb2RlID0gKGludClleC5Db2RlLCBNZXNzYWdlID0gZXguTWVzc2FnZSB9KTsKICAgICAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZUVycm9yKGlkLCBleC5Db2RlLCBleC5NZXNzYWdlKTsKICAgICAgICB9CiAgICAgICAgY2F0Y2ggKEV4Y2VwdGlvbiBleCkKICAgICAgICB7CiAgICAgICAgICAgIExvZygiTWNwRXJyb3IiLCBuZXcgeyBNZXRob2QgPSBtZXRob2QsIEVycm9yID0gZXguTWVzc2FnZSB9KTsKICAgICAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZUVycm9yKGlkLCBNY3BFcnJvckNvZGUuSW50ZXJuYWxFcnJvciwgZXguTWVzc2FnZSk7CiAgICAgICAgfQogICAgfQoKICAgIC8vIOKUgOKUgCBQcm90b2NvbCBIYW5kbGVycyDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKCiAgICBwcml2YXRlIHN0cmluZyBIYW5kbGVJbml0aWFsaXplKEpUb2tlbiBpZCwgSk9iamVjdCByZXF1ZXN0KQogICAgewogICAgICAgIHZhciBjbGllbnRQcm90b2NvbFZlcnNpb24gPSByZXF1ZXN0WyJwYXJhbXMiXT9bInByb3RvY29sVmVyc2lvbiJdPy5Ub1N0cmluZygpCiAgICAgICAgICAgID8/IF9vcHRpb25zLlByb3RvY29sVmVyc2lvbjsKCiAgICAgICAgdmFyIGNhcGFiaWxpdGllcyA9IG5ldyBKT2JqZWN0KCk7CiAgICAgICAgaWYgKF9vcHRpb25zLkNhcGFiaWxpdGllcy5Ub29scykKICAgICAgICAgICAgY2FwYWJpbGl0aWVzWyJ0b29scyJdID0gbmV3IEpPYmplY3QgeyBbImxpc3RDaGFuZ2VkIl0gPSBmYWxzZSB9OwogICAgICAgIGlmIChfb3B0aW9ucy5DYXBhYmlsaXRpZXMuUmVzb3VyY2VzKQogICAgICAgICAgICBjYXBhYmlsaXRpZXNbInJlc291cmNlcyJdID0gbmV3IEpPYmplY3QgeyBbInN1YnNjcmliZSJdID0gZmFsc2UsIFsibGlzdENoYW5nZWQiXSA9IGZhbHNlIH07CiAgICAgICAgaWYgKF9vcHRpb25zLkNhcGFiaWxpdGllcy5Qcm9tcHRzKQogICAgICAgICAgICBjYXBhYmlsaXRpZXNbInByb21wdHMiXSA9IG5ldyBKT2JqZWN0IHsgWyJsaXN0Q2hhbmdlZCJdID0gZmFsc2UgfTsKICAgICAgICBpZiAoX29wdGlvbnMuQ2FwYWJpbGl0aWVzLkxvZ2dpbmcpCiAgICAgICAgICAgIGNhcGFiaWxpdGllc1sibG9nZ2luZyJdID0gbmV3IEpPYmplY3QoKTsKICAgICAgICBpZiAoX29wdGlvbnMuQ2FwYWJpbGl0aWVzLkNvbXBsZXRpb25zKQogICAgICAgICAgICBjYXBhYmlsaXRpZXNbImNvbXBsZXRpb25zIl0gPSBuZXcgSk9iamVjdCgpOwoKICAgICAgICB2YXIgc2VydmVySW5mbyA9IG5ldyBKT2JqZWN0CiAgICAgICAgewogICAgICAgICAgICBbIm5hbWUiXSA9IF9vcHRpb25zLlNlcnZlckluZm8uTmFtZSwKICAgICAgICAgICAgWyJ2ZXJzaW9uIl0gPSBfb3B0aW9ucy5TZXJ2ZXJJbmZvLlZlcnNpb24KICAgICAgICB9OwogICAgICAgIGlmICghc3RyaW5nLklzTnVsbE9yV2hpdGVTcGFjZShfb3B0aW9ucy5TZXJ2ZXJJbmZvLlRpdGxlKSkKICAgICAgICAgICAgc2VydmVySW5mb1sidGl0bGUiXSA9IF9vcHRpb25zLlNlcnZlckluZm8uVGl0bGU7CiAgICAgICAgaWYgKCFzdHJpbmcuSXNOdWxsT3JXaGl0ZVNwYWNlKF9vcHRpb25zLlNlcnZlckluZm8uRGVzY3JpcHRpb24pKQogICAgICAgICAgICBzZXJ2ZXJJbmZvWyJkZXNjcmlwdGlvbiJdID0gX29wdGlvbnMuU2VydmVySW5mby5EZXNjcmlwdGlvbjsKCiAgICAgICAgdmFyIHJlc3VsdCA9IG5ldyBKT2JqZWN0CiAgICAgICAgewogICAgICAgICAgICBbInByb3RvY29sVmVyc2lvbiJdID0gY2xpZW50UHJvdG9jb2xWZXJzaW9uLAogICAgICAgICAgICBbImNhcGFiaWxpdGllcyJdID0gY2FwYWJpbGl0aWVzLAogICAgICAgICAgICBbInNlcnZlckluZm8iXSA9IHNlcnZlckluZm8KICAgICAgICB9OwoKICAgICAgICBpZiAoIXN0cmluZy5Jc051bGxPcldoaXRlU3BhY2UoX29wdGlvbnMuSW5zdHJ1Y3Rpb25zKSkKICAgICAgICAgICAgcmVzdWx0WyJpbnN0cnVjdGlvbnMiXSA9IF9vcHRpb25zLkluc3RydWN0aW9uczsKCiAgICAgICAgTG9nKCJNY3BJbml0aWFsaXplZCIsIG5ldwogICAgICAgIHsKICAgICAgICAgICAgU2VydmVyID0gX29wdGlvbnMuU2VydmVySW5mby5OYW1lLAogICAgICAgICAgICBWZXJzaW9uID0gX29wdGlvbnMuU2VydmVySW5mby5WZXJzaW9uLAogICAgICAgICAgICBQcm90b2NvbFZlcnNpb24gPSBjbGllbnRQcm90b2NvbFZlcnNpb24KICAgICAgICB9KTsKCiAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZVN1Y2Nlc3MoaWQsIHJlc3VsdCk7CiAgICB9CgogICAgcHJpdmF0ZSBzdHJpbmcgSGFuZGxlVG9vbHNMaXN0KEpUb2tlbiBpZCkKICAgIHsKICAgICAgICB2YXIgdG9vbHNBcnJheSA9IG5ldyBKQXJyYXkoKTsKICAgICAgICBmb3JlYWNoICh2YXIgdG9vbCBpbiBfdG9vbHMuVmFsdWVzKQogICAgICAgIHsKICAgICAgICAgICAgdmFyIHRvb2xPYmogPSBuZXcgSk9iamVjdAogICAgICAgICAgICB7CiAgICAgICAgICAgICAgICBbIm5hbWUiXSA9IHRvb2wuTmFtZSwKICAgICAgICAgICAgICAgIFsiZGVzY3JpcHRpb24iXSA9IHRvb2wuRGVzY3JpcHRpb24sCiAgICAgICAgICAgICAgICBbImlucHV0U2NoZW1hIl0gPSB0b29sLklucHV0U2NoZW1hCiAgICAgICAgICAgIH07CiAgICAgICAgICAgIGlmICghc3RyaW5nLklzTnVsbE9yV2hpdGVTcGFjZSh0b29sLlRpdGxlKSkKICAgICAgICAgICAgICAgIHRvb2xPYmpbInRpdGxlIl0gPSB0b29sLlRpdGxlOwogICAgICAgICAgICBpZiAodG9vbC5PdXRwdXRTY2hlbWEgIT0gbnVsbCkKICAgICAgICAgICAgICAgIHRvb2xPYmpbIm91dHB1dFNjaGVtYSJdID0gdG9vbC5PdXRwdXRTY2hlbWE7CiAgICAgICAgICAgIGlmICh0b29sLkFubm90YXRpb25zICE9IG51bGwgJiYgdG9vbC5Bbm5vdGF0aW9ucy5Db3VudCA+IDApCiAgICAgICAgICAgICAgICB0b29sT2JqWyJhbm5vdGF0aW9ucyJdID0gdG9vbC5Bbm5vdGF0aW9uczsKICAgICAgICAgICAgdG9vbHNBcnJheS5BZGQodG9vbE9iaik7CiAgICAgICAgfQoKICAgICAgICBMb2coIk1jcFRvb2xzTGlzdGVkIiwgbmV3IHsgQ291bnQgPSBfdG9vbHMuQ291bnQgfSk7CiAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZVN1Y2Nlc3MoaWQsIG5ldyBKT2JqZWN0IHsgWyJ0b29scyJdID0gdG9vbHNBcnJheSB9KTsKICAgIH0KCiAgICBwcml2YXRlIHN0cmluZyBIYW5kbGVSZXNvdXJjZXNMaXN0KEpUb2tlbiBpZCkKICAgIHsKICAgICAgICB2YXIgcmVzb3VyY2VzQXJyYXkgPSBuZXcgSkFycmF5KCk7CiAgICAgICAgZm9yZWFjaCAodmFyIHJlcyBpbiBfcmVzb3VyY2VzLlZhbHVlcykKICAgICAgICB7CiAgICAgICAgICAgIHZhciBvYmogPSBuZXcgSk9iamVjdAogICAgICAgICAgICB7CiAgICAgICAgICAgICAgICBbInVyaSJdID0gcmVzLlVyaSwKICAgICAgICAgICAgICAgIFsibmFtZSJdID0gcmVzLk5hbWUKICAgICAgICAgICAgfTsKICAgICAgICAgICAgaWYgKCFzdHJpbmcuSXNOdWxsT3JXaGl0ZVNwYWNlKHJlcy5EZXNjcmlwdGlvbikpCiAgICAgICAgICAgICAgICBvYmpbImRlc2NyaXB0aW9uIl0gPSByZXMuRGVzY3JpcHRpb247CiAgICAgICAgICAgIGlmICghc3RyaW5nLklzTnVsbE9yV2hpdGVTcGFjZShyZXMuTWltZVR5cGUpKQogICAgICAgICAgICAgICAgb2JqWyJtaW1lVHlwZSJdID0gcmVzLk1pbWVUeXBlOwogICAgICAgICAgICBpZiAocmVzLkFubm90YXRpb25zICE9IG51bGwgJiYgcmVzLkFubm90YXRpb25zLkNvdW50ID4gMCkKICAgICAgICAgICAgICAgIG9ialsiYW5ub3RhdGlvbnMiXSA9IHJlcy5Bbm5vdGF0aW9uczsKICAgICAgICAgICAgcmVzb3VyY2VzQXJyYXkuQWRkKG9iaik7CiAgICAgICAgfQoKICAgICAgICBMb2coIk1jcFJlc291cmNlc0xpc3RlZCIsIG5ldyB7IENvdW50ID0gX3Jlc291cmNlcy5Db3VudCB9KTsKICAgICAgICByZXR1cm4gU2VyaWFsaXplU3VjY2VzcyhpZCwgbmV3IEpPYmplY3QgeyBbInJlc291cmNlcyJdID0gcmVzb3VyY2VzQXJyYXkgfSk7CiAgICB9CgogICAgcHJpdmF0ZSBzdHJpbmcgSGFuZGxlUmVzb3VyY2VUZW1wbGF0ZXNMaXN0KEpUb2tlbiBpZCkKICAgIHsKICAgICAgICB2YXIgdGVtcGxhdGVzQXJyYXkgPSBuZXcgSkFycmF5KCk7CiAgICAgICAgZm9yZWFjaCAodmFyIHRtcGwgaW4gX3Jlc291cmNlVGVtcGxhdGVzKQogICAgICAgIHsKICAgICAgICAgICAgdmFyIG9iaiA9IG5ldyBKT2JqZWN0CiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgIFsidXJpVGVtcGxhdGUiXSA9IHRtcGwuVXJpVGVtcGxhdGUsCiAgICAgICAgICAgICAgICBbIm5hbWUiXSA9IHRtcGwuTmFtZQogICAgICAgICAgICB9OwogICAgICAgICAgICBpZiAoIXN0cmluZy5Jc051bGxPcldoaXRlU3BhY2UodG1wbC5EZXNjcmlwdGlvbikpCiAgICAgICAgICAgICAgICBvYmpbImRlc2NyaXB0aW9uIl0gPSB0bXBsLkRlc2NyaXB0aW9uOwogICAgICAgICAgICBpZiAoIXN0cmluZy5Jc051bGxPcldoaXRlU3BhY2UodG1wbC5NaW1lVHlwZSkpCiAgICAgICAgICAgICAgICBvYmpbIm1pbWVUeXBlIl0gPSB0bXBsLk1pbWVUeXBlOwogICAgICAgICAgICBpZiAodG1wbC5Bbm5vdGF0aW9ucyAhPSBudWxsICYmIHRtcGwuQW5ub3RhdGlvbnMuQ291bnQgPiAwKQogICAgICAgICAgICAgICAgb2JqWyJhbm5vdGF0aW9ucyJdID0gdG1wbC5Bbm5vdGF0aW9uczsKICAgICAgICAgICAgdGVtcGxhdGVzQXJyYXkuQWRkKG9iaik7CiAgICAgICAgfQoKICAgICAgICBMb2coIk1jcFJlc291cmNlVGVtcGxhdGVzTGlzdGVkIiwgbmV3IHsgQ291bnQgPSBfcmVzb3VyY2VUZW1wbGF0ZXMuQ291bnQgfSk7CiAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZVN1Y2Nlc3MoaWQsIG5ldyBKT2JqZWN0IHsgWyJyZXNvdXJjZVRlbXBsYXRlcyJdID0gdGVtcGxhdGVzQXJyYXkgfSk7CiAgICB9CgogICAgcHJpdmF0ZSBhc3luYyBUYXNrPHN0cmluZz4gSGFuZGxlUmVzb3VyY2VzUmVhZEFzeW5jKEpUb2tlbiBpZCwgSk9iamVjdCByZXF1ZXN0LCBDYW5jZWxsYXRpb25Ub2tlbiBjdCkKICAgIHsKICAgICAgICB2YXIgcGFyYW1zT2JqID0gcmVxdWVzdFsicGFyYW1zIl0gYXMgSk9iamVjdDsKICAgICAgICB2YXIgdXJpID0gcGFyYW1zT2JqPy5WYWx1ZTxzdHJpbmc+KCJ1cmkiKTsKCiAgICAgICAgaWYgKHN0cmluZy5Jc051bGxPcldoaXRlU3BhY2UodXJpKSkKICAgICAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZUVycm9yKGlkLCBNY3BFcnJvckNvZGUuSW52YWxpZFBhcmFtcywgIlJlc291cmNlIFVSSSBpcyByZXF1aXJlZCIpOwoKICAgICAgICAvLyAxLiBUcnkgZXhhY3QgbWF0Y2ggb24gcmVnaXN0ZXJlZCBzdGF0aWMgcmVzb3VyY2VzCiAgICAgICAgaWYgKF9yZXNvdXJjZXMuVHJ5R2V0VmFsdWUodXJpLCBvdXQgdmFyIHJlc291cmNlKSkKICAgICAgICB7CiAgICAgICAgICAgIExvZygiTWNwUmVzb3VyY2VSZWFkU3RhcnRlZCIsIG5ldyB7IFVyaSA9IHVyaSB9KTsKICAgICAgICAgICAgdHJ5CiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgIHZhciBjb250ZW50cyA9IGF3YWl0IHJlc291cmNlLkhhbmRsZXIoY3QpLkNvbmZpZ3VyZUF3YWl0KGZhbHNlKTsKICAgICAgICAgICAgICAgIExvZygiTWNwUmVzb3VyY2VSZWFkQ29tcGxldGVkIiwgbmV3IHsgVXJpID0gdXJpIH0pOwogICAgICAgICAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZVN1Y2Nlc3MoaWQsIG5ldyBKT2JqZWN0IHsgWyJjb250ZW50cyJdID0gY29udGVudHMgfSk7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgY2F0Y2ggKEV4Y2VwdGlvbiBleCkKICAgICAgICAgICAgewogICAgICAgICAgICAgICAgTG9nKCJNY3BSZXNvdXJjZVJlYWRFcnJvciIsIG5ldyB7IFVyaSA9IHVyaSwgRXJyb3IgPSBleC5NZXNzYWdlIH0pOwogICAgICAgICAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZUVycm9yKGlkLCBNY3BFcnJvckNvZGUuSW50ZXJuYWxFcnJvciwgZXguTWVzc2FnZSk7CiAgICAgICAgICAgIH0KICAgICAgICB9CgogICAgICAgIC8vIDIuIFRyeSBtYXRjaGluZyBhZ2FpbnN0IHJlZ2lzdGVyZWQgcmVzb3VyY2UgdGVtcGxhdGVzCiAgICAgICAgZm9yZWFjaCAodmFyIHRtcGwgaW4gX3Jlc291cmNlVGVtcGxhdGVzKQogICAgICAgIHsKICAgICAgICAgICAgaWYgKE1hdGNoZXNVcmlUZW1wbGF0ZSh0bXBsLlVyaVRlbXBsYXRlLCB1cmkpKQogICAgICAgICAgICB7CiAgICAgICAgICAgICAgICBMb2coIk1jcFJlc291cmNlUmVhZFN0YXJ0ZWQiLCBuZXcgeyBVcmkgPSB1cmksIFRlbXBsYXRlID0gdG1wbC5VcmlUZW1wbGF0ZSB9KTsKICAgICAgICAgICAgICAgIHRyeQogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIHZhciBjb250ZW50cyA9IGF3YWl0IHRtcGwuSGFuZGxlcih1cmksIGN0KS5Db25maWd1cmVBd2FpdChmYWxzZSk7CiAgICAgICAgICAgICAgICAgICAgTG9nKCJNY3BSZXNvdXJjZVJlYWRDb21wbGV0ZWQiLCBuZXcgeyBVcmkgPSB1cmkgfSk7CiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZVN1Y2Nlc3MoaWQsIG5ldyBKT2JqZWN0IHsgWyJjb250ZW50cyJdID0gY29udGVudHMgfSk7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICBjYXRjaCAoRXhjZXB0aW9uIGV4KQogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIExvZygiTWNwUmVzb3VyY2VSZWFkRXJyb3IiLCBuZXcgeyBVcmkgPSB1cmksIEVycm9yID0gZXguTWVzc2FnZSB9KTsKICAgICAgICAgICAgICAgICAgICByZXR1cm4gU2VyaWFsaXplRXJyb3IoaWQsIE1jcEVycm9yQ29kZS5JbnRlcm5hbEVycm9yLCBleC5NZXNzYWdlKTsKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgfQogICAgICAgIH0KCiAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZUVycm9yKGlkLCBNY3BFcnJvckNvZGUuSW52YWxpZFBhcmFtcywgJCJSZXNvdXJjZSBub3QgZm91bmQ6IHt1cml9Iik7CiAgICB9CgogICAgLy8vIDxzdW1tYXJ5PgogICAgLy8vIFNpbXBsZSBVUkkgdGVtcGxhdGUgbWF0Y2hlci4gQ2hlY2tzIGlmIGEgY29uY3JldGUgVVJJIG1hdGNoZXMgYSB0ZW1wbGF0ZQogICAgLy8vIHdpdGgge3BhcmFtfSBwbGFjZWhvbGRlcnMgKGUuZy4sICJkYXRhOi8vcmVjb3Jkcy97aWR9IiBtYXRjaGVzICJkYXRhOi8vcmVjb3Jkcy8xMjMiKS4KICAgIC8vLyA8L3N1bW1hcnk+CiAgICBwcml2YXRlIHN0YXRpYyBib29sIE1hdGNoZXNVcmlUZW1wbGF0ZShzdHJpbmcgdGVtcGxhdGUsIHN0cmluZyB1cmkpCiAgICB7CiAgICAgICAgLy8gU3BsaXQgYm90aCBvbiAnLycgYW5kIGNvbXBhcmUgc2VnbWVudHMKICAgICAgICB2YXIgdGVtcGxhdGVQYXJ0cyA9IHRlbXBsYXRlLlNwbGl0KCcvJyk7CiAgICAgICAgdmFyIHVyaVBhcnRzID0gdXJpLlNwbGl0KCcvJyk7CgogICAgICAgIGlmICh0ZW1wbGF0ZVBhcnRzLkxlbmd0aCAhPSB1cmlQYXJ0cy5MZW5ndGgpIHJldHVybiBmYWxzZTsKCiAgICAgICAgZm9yIChpbnQgaSA9IDA7IGkgPCB0ZW1wbGF0ZVBhcnRzLkxlbmd0aDsgaSsrKQogICAgICAgIHsKICAgICAgICAgICAgdmFyIHNlZyA9IHRlbXBsYXRlUGFydHNbaV07CiAgICAgICAgICAgIGlmIChzZWcuU3RhcnRzV2l0aCgieyIpICYmIHNlZy5FbmRzV2l0aCgifSIpKSBjb250aW51ZTsgLy8gd2lsZGNhcmQKICAgICAgICAgICAgaWYgKCFzdHJpbmcuRXF1YWxzKHNlZywgdXJpUGFydHNbaV0sIFN0cmluZ0NvbXBhcmlzb24uT3JkaW5hbElnbm9yZUNhc2UpKSByZXR1cm4gZmFsc2U7CiAgICAgICAgfQogICAgICAgIHJldHVybiB0cnVlOwogICAgfQoKICAgIC8vLyA8c3VtbWFyeT4KICAgIC8vLyBFeHRyYWN0IG5hbWVkIHBhcmFtZXRlcnMgZnJvbSBhIFVSSSBnaXZlbiBhIHRlbXBsYXRlIHBhdHRlcm4uCiAgICAvLy8gRS5nLiwgdGVtcGxhdGUgImRhdGE6Ly9yZWNvcmRzL3tpZH0iIHdpdGggdXJpICJkYXRhOi8vcmVjb3Jkcy8xMjMiIHJldHVybnMgeyAiaWQiOiAiMTIzIiB9LgogICAgLy8vIDwvc3VtbWFyeT4KICAgIHB1YmxpYyBzdGF0aWMgRGljdGlvbmFyeTxzdHJpbmcsIHN0cmluZz4gRXh0cmFjdFVyaVBhcmFtZXRlcnMoc3RyaW5nIHRlbXBsYXRlLCBzdHJpbmcgdXJpKQogICAgewogICAgICAgIHZhciByZXN1bHQgPSBuZXcgRGljdGlvbmFyeTxzdHJpbmcsIHN0cmluZz4oU3RyaW5nQ29tcGFyZXIuT3JkaW5hbElnbm9yZUNhc2UpOwogICAgICAgIHZhciB0ZW1wbGF0ZVBhcnRzID0gdGVtcGxhdGUuU3BsaXQoJy8nKTsKICAgICAgICB2YXIgdXJpUGFydHMgPSB1cmkuU3BsaXQoJy8nKTsKCiAgICAgICAgaWYgKHRlbXBsYXRlUGFydHMuTGVuZ3RoICE9IHVyaVBhcnRzLkxlbmd0aCkgcmV0dXJuIHJlc3VsdDsKCiAgICAgICAgZm9yIChpbnQgaSA9IDA7IGkgPCB0ZW1wbGF0ZVBhcnRzLkxlbmd0aDsgaSsrKQogICAgICAgIHsKICAgICAgICAgICAgdmFyIHNlZyA9IHRlbXBsYXRlUGFydHNbaV07CiAgICAgICAgICAgIGlmIChzZWcuU3RhcnRzV2l0aCgieyIpICYmIHNlZy5FbmRzV2l0aCgifSIpKQogICAgICAgICAgICB7CiAgICAgICAgICAgICAgICB2YXIgcGFyYW1OYW1lID0gc2VnLlN1YnN0cmluZygxLCBzZWcuTGVuZ3RoIC0gMik7CiAgICAgICAgICAgICAgICByZXN1bHRbcGFyYW1OYW1lXSA9IHVyaVBhcnRzW2ldOwogICAgICAgICAgICB9CiAgICAgICAgfQogICAgICAgIHJldHVybiByZXN1bHQ7CiAgICB9CgogICAgcHJpdmF0ZSBzdHJpbmcgSGFuZGxlUHJvbXB0c0xpc3QoSlRva2VuIGlkKQogICAgewogICAgICAgIHZhciBwcm9tcHRzQXJyYXkgPSBuZXcgSkFycmF5KCk7CiAgICAgICAgZm9yZWFjaCAodmFyIHByb21wdCBpbiBfcHJvbXB0cy5WYWx1ZXMpCiAgICAgICAgewogICAgICAgICAgICB2YXIgb2JqID0gbmV3IEpPYmplY3QKICAgICAgICAgICAgewogICAgICAgICAgICAgICAgWyJuYW1lIl0gPSBwcm9tcHQuTmFtZQogICAgICAgICAgICB9OwogICAgICAgICAgICBpZiAoIXN0cmluZy5Jc051bGxPcldoaXRlU3BhY2UocHJvbXB0LkRlc2NyaXB0aW9uKSkKICAgICAgICAgICAgICAgIG9ialsiZGVzY3JpcHRpb24iXSA9IHByb21wdC5EZXNjcmlwdGlvbjsKCiAgICAgICAgICAgIGlmIChwcm9tcHQuQXJndW1lbnRzLkNvdW50ID4gMCkKICAgICAgICAgICAgewogICAgICAgICAgICAgICAgdmFyIGFyZ3NBcnJheSA9IG5ldyBKQXJyYXkoKTsKICAgICAgICAgICAgICAgIGZvcmVhY2ggKHZhciBhcmcgaW4gcHJvbXB0LkFyZ3VtZW50cykKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICB2YXIgYXJnT2JqID0gbmV3IEpPYmplY3QgeyBbIm5hbWUiXSA9IGFyZy5OYW1lIH07CiAgICAgICAgICAgICAgICAgICAgaWYgKCFzdHJpbmcuSXNOdWxsT3JXaGl0ZVNwYWNlKGFyZy5EZXNjcmlwdGlvbikpCiAgICAgICAgICAgICAgICAgICAgICAgIGFyZ09ialsiZGVzY3JpcHRpb24iXSA9IGFyZy5EZXNjcmlwdGlvbjsKICAgICAgICAgICAgICAgICAgICBpZiAoYXJnLlJlcXVpcmVkKQogICAgICAgICAgICAgICAgICAgICAgICBhcmdPYmpbInJlcXVpcmVkIl0gPSB0cnVlOwogICAgICAgICAgICAgICAgICAgIGFyZ3NBcnJheS5BZGQoYXJnT2JqKTsKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgIG9ialsiYXJndW1lbnRzIl0gPSBhcmdzQXJyYXk7CiAgICAgICAgICAgIH0KCiAgICAgICAgICAgIHByb21wdHNBcnJheS5BZGQob2JqKTsKICAgICAgICB9CgogICAgICAgIExvZygiTWNwUHJvbXB0c0xpc3RlZCIsIG5ldyB7IENvdW50ID0gX3Byb21wdHMuQ291bnQgfSk7CiAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZVN1Y2Nlc3MoaWQsIG5ldyBKT2JqZWN0IHsgWyJwcm9tcHRzIl0gPSBwcm9tcHRzQXJyYXkgfSk7CiAgICB9CgogICAgcHJpdmF0ZSBhc3luYyBUYXNrPHN0cmluZz4gSGFuZGxlUHJvbXB0c0dldEFzeW5jKEpUb2tlbiBpZCwgSk9iamVjdCByZXF1ZXN0LCBDYW5jZWxsYXRpb25Ub2tlbiBjdCkKICAgIHsKICAgICAgICB2YXIgcGFyYW1zT2JqID0gcmVxdWVzdFsicGFyYW1zIl0gYXMgSk9iamVjdDsKICAgICAgICB2YXIgcHJvbXB0TmFtZSA9IHBhcmFtc09iaj8uVmFsdWU8c3RyaW5nPigibmFtZSIpOwogICAgICAgIHZhciBhcmd1bWVudHMgPSBwYXJhbXNPYmo/WyJhcmd1bWVudHMiXSBhcyBKT2JqZWN0ID8/IG5ldyBKT2JqZWN0KCk7CgogICAgICAgIGlmIChzdHJpbmcuSXNOdWxsT3JXaGl0ZVNwYWNlKHByb21wdE5hbWUpKQogICAgICAgICAgICByZXR1cm4gU2VyaWFsaXplRXJyb3IoaWQsIE1jcEVycm9yQ29kZS5JbnZhbGlkUGFyYW1zLCAiUHJvbXB0IG5hbWUgaXMgcmVxdWlyZWQiKTsKCiAgICAgICAgaWYgKCFfcHJvbXB0cy5UcnlHZXRWYWx1ZShwcm9tcHROYW1lLCBvdXQgdmFyIHByb21wdCkpCiAgICAgICAgICAgIHJldHVybiBTZXJpYWxpemVFcnJvcihpZCwgTWNwRXJyb3JDb2RlLkludmFsaWRQYXJhbXMsICQiUHJvbXB0IG5vdCBmb3VuZDoge3Byb21wdE5hbWV9Iik7CgogICAgICAgIExvZygiTWNwUHJvbXB0R2V0U3RhcnRlZCIsIG5ldyB7IFByb21wdCA9IHByb21wdE5hbWUgfSk7CgogICAgICAgIHRyeQogICAgICAgIHsKICAgICAgICAgICAgdmFyIG1lc3NhZ2VzID0gYXdhaXQgcHJvbXB0LkhhbmRsZXIoYXJndW1lbnRzLCBjdCkuQ29uZmlndXJlQXdhaXQoZmFsc2UpOwogICAgICAgICAgICBMb2coIk1jcFByb21wdEdldENvbXBsZXRlZCIsIG5ldyB7IFByb21wdCA9IHByb21wdE5hbWUsIE1lc3NhZ2VDb3VudCA9IG1lc3NhZ2VzLkNvdW50IH0pOwoKICAgICAgICAgICAgdmFyIHJlc3VsdCA9IG5ldyBKT2JqZWN0IHsgWyJtZXNzYWdlcyJdID0gbWVzc2FnZXMgfTsKICAgICAgICAgICAgaWYgKCFzdHJpbmcuSXNOdWxsT3JXaGl0ZVNwYWNlKHByb21wdC5EZXNjcmlwdGlvbikpCiAgICAgICAgICAgICAgICByZXN1bHRbImRlc2NyaXB0aW9uIl0gPSBwcm9tcHQuRGVzY3JpcHRpb247CgogICAgICAgICAgICByZXR1cm4gU2VyaWFsaXplU3VjY2VzcyhpZCwgcmVzdWx0KTsKICAgICAgICB9CiAgICAgICAgY2F0Y2ggKEV4Y2VwdGlvbiBleCkKICAgICAgICB7CiAgICAgICAgICAgIExvZygiTWNwUHJvbXB0R2V0RXJyb3IiLCBuZXcgeyBQcm9tcHQgPSBwcm9tcHROYW1lLCBFcnJvciA9IGV4Lk1lc3NhZ2UgfSk7CiAgICAgICAgICAgIHJldHVybiBTZXJpYWxpemVFcnJvcihpZCwgTWNwRXJyb3JDb2RlLkludGVybmFsRXJyb3IsIGV4Lk1lc3NhZ2UpOwogICAgICAgIH0KICAgIH0KCiAgICBwcml2YXRlIGFzeW5jIFRhc2s8c3RyaW5nPiBIYW5kbGVUb29sc0NhbGxBc3luYyhKVG9rZW4gaWQsIEpPYmplY3QgcmVxdWVzdCwgQ2FuY2VsbGF0aW9uVG9rZW4gY3QpCiAgICB7CiAgICAgICAgdmFyIHBhcmFtc09iaiA9IHJlcXVlc3RbInBhcmFtcyJdIGFzIEpPYmplY3Q7CiAgICAgICAgdmFyIHRvb2xOYW1lID0gcGFyYW1zT2JqPy5WYWx1ZTxzdHJpbmc+KCJuYW1lIik7CiAgICAgICAgdmFyIGFyZ3VtZW50cyA9IHBhcmFtc09iaj9bImFyZ3VtZW50cyJdIGFzIEpPYmplY3QgPz8gbmV3IEpPYmplY3QoKTsKCiAgICAgICAgaWYgKHN0cmluZy5Jc051bGxPcldoaXRlU3BhY2UodG9vbE5hbWUpKQogICAgICAgICAgICByZXR1cm4gU2VyaWFsaXplRXJyb3IoaWQsIE1jcEVycm9yQ29kZS5JbnZhbGlkUGFyYW1zLCAiVG9vbCBuYW1lIGlzIHJlcXVpcmVkIik7CgogICAgICAgIGlmICghX3Rvb2xzLlRyeUdldFZhbHVlKHRvb2xOYW1lLCBvdXQgdmFyIHRvb2wpKQogICAgICAgICAgICByZXR1cm4gU2VyaWFsaXplRXJyb3IoaWQsIE1jcEVycm9yQ29kZS5JbnZhbGlkUGFyYW1zLCAkIlVua25vd24gdG9vbDoge3Rvb2xOYW1lfSIpOwoKICAgICAgICBMb2coIk1jcFRvb2xDYWxsU3RhcnRlZCIsIG5ldyB7IFRvb2wgPSB0b29sTmFtZSB9KTsKCiAgICAgICAgdHJ5CiAgICAgICAgewogICAgICAgICAgICB2YXIgcmVzdWx0ID0gYXdhaXQgdG9vbC5IYW5kbGVyKGFyZ3VtZW50cywgY3QpLkNvbmZpZ3VyZUF3YWl0KGZhbHNlKTsKCiAgICAgICAgICAgIEpPYmplY3QgY2FsbFJlc3VsdDsKCiAgICAgICAgICAgIC8vIFN1cHBvcnQgcHJlLWZvcm1hdHRlZCBNQ1AgdG9vbCByZXN1bHRzIHdpdGggcmljaCBjb250ZW50IHR5cGVzCiAgICAgICAgICAgIC8vIChpbWFnZSwgYXVkaW8sIHJlc291cmNlLCBvciBtaXhlZCBjb250ZW50IGFycmF5cykuCiAgICAgICAgICAgIC8vIElmIHRoZSBoYW5kbGVyIHJldHVybnMgeyAiY29udGVudCI6IFsgeyAidHlwZSI6ICIuLi4iIH0gXSwgLi4uIH0sCiAgICAgICAgICAgIC8vIHBhc3MgaXQgdGhyb3VnaCBkaXJlY3RseSBpbnN0ZWFkIG9mIHdyYXBwaW5nIGluIHRleHQuCiAgICAgICAgICAgIGlmIChyZXN1bHQgaXMgSk9iamVjdCBqb2JqICYmIGpvYmpbImNvbnRlbnQiXSBpcyBKQXJyYXkgY29udGVudEFycmF5CiAgICAgICAgICAgICAgICAmJiBjb250ZW50QXJyYXkuQ291bnQgPiAwICYmIGNvbnRlbnRBcnJheVswXT9bInR5cGUiXSAhPSBudWxsKQogICAgICAgICAgICB7CiAgICAgICAgICAgICAgICBjYWxsUmVzdWx0ID0gbmV3IEpPYmplY3QKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBbImNvbnRlbnQiXSA9IGNvbnRlbnRBcnJheSwKICAgICAgICAgICAgICAgICAgICBbImlzRXJyb3IiXSA9IGpvYmouVmFsdWU8Ym9vbD8+KCJpc0Vycm9yIikgPz8gZmFsc2UKICAgICAgICAgICAgICAgIH07CiAgICAgICAgICAgICAgICBpZiAoam9ialsic3RydWN0dXJlZENvbnRlbnQiXSBpcyBKT2JqZWN0IHN0cnVjdHVyZWQpCiAgICAgICAgICAgICAgICAgICAgY2FsbFJlc3VsdFsic3RydWN0dXJlZENvbnRlbnQiXSA9IHN0cnVjdHVyZWQ7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgZWxzZQogICAgICAgICAgICB7CiAgICAgICAgICAgICAgICBzdHJpbmcgdGV4dDsKICAgICAgICAgICAgICAgIGlmIChyZXN1bHQgaXMgSk9iamVjdCBwbGFpbk9iaikKICAgICAgICAgICAgICAgICAgICB0ZXh0ID0gcGxhaW5PYmouVG9TdHJpbmcoTmV3dG9uc29mdC5Kc29uLkZvcm1hdHRpbmcuSW5kZW50ZWQpOwogICAgICAgICAgICAgICAgZWxzZSBpZiAocmVzdWx0IGlzIHN0cmluZyBzKQogICAgICAgICAgICAgICAgICAgIHRleHQgPSBzOwogICAgICAgICAgICAgICAgZWxzZSBpZiAocmVzdWx0ID09IG51bGwpCiAgICAgICAgICAgICAgICAgICAgdGV4dCA9ICJ7fSI7CiAgICAgICAgICAgICAgICBlbHNlCiAgICAgICAgICAgICAgICAgICAgdGV4dCA9IEpzb25Db252ZXJ0LlNlcmlhbGl6ZU9iamVjdChyZXN1bHQsIE5ld3RvbnNvZnQuSnNvbi5Gb3JtYXR0aW5nLkluZGVudGVkKTsKCiAgICAgICAgICAgICAgICBjYWxsUmVzdWx0ID0gbmV3IEpPYmplY3QKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBbImNvbnRlbnQiXSA9IG5ldyBKQXJyYXkgeyBuZXcgSk9iamVjdCB7IFsidHlwZSJdID0gInRleHQiLCBbInRleHQiXSA9IHRleHQgfSB9LAogICAgICAgICAgICAgICAgICAgIFsiaXNFcnJvciJdID0gZmFsc2UKICAgICAgICAgICAgICAgIH07CiAgICAgICAgICAgIH0KCiAgICAgICAgICAgIExvZygiTWNwVG9vbENhbGxDb21wbGV0ZWQiLCBuZXcgeyBUb29sID0gdG9vbE5hbWUsIElzRXJyb3IgPSBjYWxsUmVzdWx0LlZhbHVlPGJvb2w+KCJpc0Vycm9yIikgfSk7CiAgICAgICAgICAgIHJldHVybiBTZXJpYWxpemVTdWNjZXNzKGlkLCBjYWxsUmVzdWx0KTsKICAgICAgICB9CiAgICAgICAgY2F0Y2ggKEFyZ3VtZW50RXhjZXB0aW9uIGV4KQogICAgICAgIHsKICAgICAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZVN1Y2Nlc3MoaWQsIG5ldyBKT2JqZWN0CiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgIFsiY29udGVudCJdID0gbmV3IEpBcnJheQogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIG5ldyBKT2JqZWN0IHsgWyJ0eXBlIl0gPSAidGV4dCIsIFsidGV4dCJdID0gJCJJbnZhbGlkIGFyZ3VtZW50czoge2V4Lk1lc3NhZ2V9IiB9CiAgICAgICAgICAgICAgICB9LAogICAgICAgICAgICAgICAgWyJpc0Vycm9yIl0gPSB0cnVlCiAgICAgICAgICAgIH0pOwogICAgICAgIH0KICAgICAgICBjYXRjaCAoTWNwRXhjZXB0aW9uIGV4KQogICAgICAgIHsKICAgICAgICAgICAgcmV0dXJuIFNlcmlhbGl6ZVN1Y2Nlc3MoaWQsIG5ldyBKT2JqZWN0CiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgIFsiY29udGVudCJdID0gbmV3IEpBcnJheQogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIG5ldyBKT2JqZWN0IHsgWyJ0eXBlIl0gPSAidGV4dCIsIFsidGV4dCJdID0gJCJUb29sIGVycm9yOiB7ZXguTWVzc2FnZX0iIH0KICAgICAgICAgICAgICAgIH0sCiAgICAgICAgICAgICAgICBbImlzRXJyb3IiXSA9IHRydWUKICAgICAgICAgICAgfSk7CiAgICAgICAgfQogICAgICAgIGNhdGNoIChFeGNlcHRpb24gZXgpCiAgICAgICAgewogICAgICAgICAgICBMb2coIk1jcFRvb2xDYWxsRXJyb3IiLCBuZXcgeyBUb29sID0gdG9vbE5hbWUsIEVycm9yID0gZXguTWVzc2FnZSB9KTsKCiAgICAgICAgICAgIHJldHVybiBTZXJpYWxpemVTdWNjZXNzKGlkLCBuZXcgSk9iamVjdAogICAgICAgICAgICB7CiAgICAgICAgICAgICAgICBbImNvbnRlbnQiXSA9IG5ldyBKQXJyYXkKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBuZXcgSk9iamVjdCB7IFsidHlwZSJdID0gInRleHQiLCBbInRleHQiXSA9ICQiVG9vbCBleGVjdXRpb24gZmFpbGVkOiB7ZXguTWVzc2FnZX0iIH0KICAgICAgICAgICAgICAgIH0sCiAgICAgICAgICAgICAgICBbImlzRXJyb3IiXSA9IHRydWUKICAgICAgICAgICAgfSk7CiAgICAgICAgfQogICAgfQoKICAgIC8vIOKUgOKUgCBDb250ZW50IEhlbHBlcnMg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiAgICAvLwogICAgLy8gICAgVXNlIHRoZXNlIHRvIGJ1aWxkIHJpY2ggdG9vbCByZXN1bHRzIHdpdGggaW1hZ2UsIGF1ZGlvLCBvciByZXNvdXJjZQogICAgLy8gICAgY29udGVudC4gUmV0dXJuIE1jcFJlcXVlc3RIYW5kbGVyLlRvb2xSZXN1bHQoLi4uKSBmcm9tIHlvdXIgaGFuZGxlcgogICAgLy8gICAgdG8gYnlwYXNzIGF1dG9tYXRpYyB0ZXh0IHdyYXBwaW5nLgogICAgLy8KCiAgICAvLy8gPHN1bW1hcnk+Q3JlYXRlIGEgdGV4dCBjb250ZW50IGl0ZW0uPC9zdW1tYXJ5PgogICAgcHVibGljIHN0YXRpYyBKT2JqZWN0IFRleHRDb250ZW50KHN0cmluZyB0ZXh0KSA9PgogICAgICAgIG5ldyBKT2JqZWN0IHsgWyJ0eXBlIl0gPSAidGV4dCIsIFsidGV4dCJdID0gdGV4dCB9OwoKICAgIC8vLyA8c3VtbWFyeT5DcmVhdGUgYW4gaW1hZ2UgY29udGVudCBpdGVtIChiYXNlNjQtZW5jb2RlZCkuPC9zdW1tYXJ5PgogICAgcHVibGljIHN0YXRpYyBKT2JqZWN0IEltYWdlQ29udGVudChzdHJpbmcgYmFzZTY0RGF0YSwgc3RyaW5nIG1pbWVUeXBlKSA9PgogICAgICAgIG5ldyBKT2JqZWN0IHsgWyJ0eXBlIl0gPSAiaW1hZ2UiLCBbImRhdGEiXSA9IGJhc2U2NERhdGEsIFsibWltZVR5cGUiXSA9IG1pbWVUeXBlIH07CgogICAgLy8vIDxzdW1tYXJ5PkNyZWF0ZSBhbiBhdWRpbyBjb250ZW50IGl0ZW0gKGJhc2U2NC1lbmNvZGVkKS48L3N1bW1hcnk+CiAgICBwdWJsaWMgc3RhdGljIEpPYmplY3QgQXVkaW9Db250ZW50KHN0cmluZyBiYXNlNjREYXRhLCBzdHJpbmcgbWltZVR5cGUpID0+CiAgICAgICAgbmV3IEpPYmplY3QgeyBbInR5cGUiXSA9ICJhdWRpbyIsIFsiZGF0YSJdID0gYmFzZTY0RGF0YSwgWyJtaW1lVHlwZSJdID0gbWltZVR5cGUgfTsKCiAgICAvLy8gPHN1bW1hcnk+Q3JlYXRlIGFuIGVtYmVkZGVkIHJlc291cmNlIGNvbnRlbnQgaXRlbS48L3N1bW1hcnk+CiAgICBwdWJsaWMgc3RhdGljIEpPYmplY3QgUmVzb3VyY2VDb250ZW50KHN0cmluZyB1cmksIHN0cmluZyB0ZXh0LCBzdHJpbmcgbWltZVR5cGUgPSAidGV4dC9wbGFpbiIpID0+CiAgICAgICAgbmV3IEpPYmplY3QKICAgICAgICB7CiAgICAgICAgICAgIFsidHlwZSJdID0gInJlc291cmNlIiwKICAgICAgICAgICAgWyJyZXNvdXJjZSJdID0gbmV3IEpPYmplY3QgeyBbInVyaSJdID0gdXJpLCBbInRleHQiXSA9IHRleHQsIFsibWltZVR5cGUiXSA9IG1pbWVUeXBlIH0KICAgICAgICB9OwoKICAgIC8vLyA8c3VtbWFyeT4KICAgIC8vLyBCdWlsZCBhIHByZS1mb3JtYXR0ZWQgdG9vbCByZXN1bHQgd2l0aCBtaXhlZCBjb250ZW50IHR5cGVzLgogICAgLy8vIFJldHVybiB0aGlzIGZyb20gYSB0b29sIGhhbmRsZXIgdG8gYnlwYXNzIGF1dG9tYXRpYyB0ZXh0IHdyYXBwaW5nLgogICAgLy8vIDwvc3VtbWFyeT4KICAgIHB1YmxpYyBzdGF0aWMgSk9iamVjdCBUb29sUmVzdWx0KEpBcnJheSBjb250ZW50LCBKT2JqZWN0IHN0cnVjdHVyZWRDb250ZW50ID0gbnVsbCwgYm9vbCBpc0Vycm9yID0gZmFsc2UpCiAgICB7CiAgICAgICAgdmFyIHJlc3VsdCA9IG5ldyBKT2JqZWN0IHsgWyJjb250ZW50Il0gPSBjb250ZW50LCBbImlzRXJyb3IiXSA9IGlzRXJyb3IgfTsKICAgICAgICBpZiAoc3RydWN0dXJlZENvbnRlbnQgIT0gbnVsbCkgcmVzdWx0WyJzdHJ1Y3R1cmVkQ29udGVudCJdID0gc3RydWN0dXJlZENvbnRlbnQ7CiAgICAgICAgcmV0dXJuIHJlc3VsdDsKICAgIH0KCiAgICAvLyDilIDilIAgSlNPTi1SUEMgU2VyaWFsaXphdGlvbiDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKCiAgICBwcml2YXRlIHN0cmluZyBTZXJpYWxpemVTdWNjZXNzKEpUb2tlbiBpZCwgSk9iamVjdCByZXN1bHQpCiAgICB7CiAgICAgICAgcmV0dXJuIG5ldyBKT2JqZWN0CiAgICAgICAgewogICAgICAgICAgICBbImpzb25ycGMiXSA9ICIyLjAiLAogICAgICAgICAgICBbImlkIl0gPSBpZCwKICAgICAgICAgICAgWyJyZXN1bHQiXSA9IHJlc3VsdAogICAgICAgIH0uVG9TdHJpbmcoTmV3dG9uc29mdC5Kc29uLkZvcm1hdHRpbmcuTm9uZSk7CiAgICB9CgogICAgcHJpdmF0ZSBzdHJpbmcgU2VyaWFsaXplRXJyb3IoSlRva2VuIGlkLCBNY3BFcnJvckNvZGUgY29kZSwgc3RyaW5nIG1lc3NhZ2UsIHN0cmluZyBkYXRhID0gbnVsbCkKICAgIHsKICAgICAgICByZXR1cm4gU2VyaWFsaXplRXJyb3IoaWQsIChpbnQpY29kZSwgbWVzc2FnZSwgZGF0YSk7CiAgICB9CgogICAgcHJpdmF0ZSBzdHJpbmcgU2VyaWFsaXplRXJyb3IoSlRva2VuIGlkLCBpbnQgY29kZSwgc3RyaW5nIG1lc3NhZ2UsIHN0cmluZyBkYXRhID0gbnVsbCkKICAgIHsKICAgICAgICB2YXIgZXJyb3IgPSBuZXcgSk9iamVjdAogICAgICAgIHsKICAgICAgICAgICAgWyJjb2RlIl0gPSBjb2RlLAogICAgICAgICAgICBbIm1lc3NhZ2UiXSA9IG1lc3NhZ2UKICAgICAgICB9OwogICAgICAgIGlmICghc3RyaW5nLklzTnVsbE9yV2hpdGVTcGFjZShkYXRhKSkKICAgICAgICAgICAgZXJyb3JbImRhdGEiXSA9IGRhdGE7CgogICAgICAgIHJldHVybiBuZXcgSk9iamVjdAogICAgICAgIHsKICAgICAgICAgICAgWyJqc29ucnBjIl0gPSAiMi4wIiwKICAgICAgICAgICAgWyJpZCJdID0gaWQsCiAgICAgICAgICAgIFsiZXJyb3IiXSA9IGVycm9yCiAgICAgICAgfS5Ub1N0cmluZyhOZXd0b25zb2Z0Lkpzb24uRm9ybWF0dGluZy5Ob25lKTsKICAgIH0KCiAgICBwcml2YXRlIHZvaWQgTG9nKHN0cmluZyBldmVudE5hbWUsIG9iamVjdCBkYXRhKQogICAgewogICAgICAgIE9uTG9nPy5JbnZva2UoZXZlbnROYW1lLCBkYXRhKTsKICAgIH0KfQo="
_MCP_MOD_CACHE = {"mod": None}


def _mcp_gen_module():
    """Load the embedded generator into an isolated module namespace, with the
    frozen C# framework injected in place of its on-disk read. Cached."""
    if _MCP_MOD_CACHE["mod"] is not None:
        return _MCP_MOD_CACHE["mod"]
    import types as _types
    src = _b64.b64decode(_MCP_GEN_B64).decode("utf-8")
    fw = _b64.b64decode(_MCP_FRAMEWORK_B64).decode("utf-8")
    # Replace the on-disk framework read with the embedded constant.
    src = src.replace(
        'FRAMEWORK_PATH = Path(__file__).with_name("mcp_framework.cs")',
        '_EMBEDDED_FRAMEWORK = ' + repr(fw) + '\nFRAMEWORK_PATH = None')
    src = src.replace(
        'framework = FRAMEWORK_PATH.read_text(encoding="utf-8")',
        'framework = _EMBEDDED_FRAMEWORK')
    mod = _types.ModuleType("_mcs_new_shape_embedded")
    exec(compile(src, "_mcs_new_shape_embedded", "exec"), mod.__dict__)
    _MCP_MOD_CACHE["mod"] = mod
    return mod


class _McpShapeEngine(_EngineBase):
    """NEW Copilot Studio experience (BlastBox two-solution MCP shape): from a
    directory of quality-contract agent.py files, generate ONE inline-MCP
    connectors solution + ONE new-generation agents solution (cliagent parent +
    ConnectedAgentTool child, each agent.py a Python skill bundle), then deploy
    connectors -> agents -> finalize (PublishAllXml + PvaPublish children-first)
    with publish VERIFICATION (publishedon must flip; a PvaPublish 200 alone is
    not proof on provisioning-slow envs).

    Hardening baked into the embedded generator (proven into kodyd365 2026-07):
      * parents born channel-less (channels: []) — a Teams channel entry wedges
        bots in PVA provisioning forever when that service degrades;
      * connector Description clamped to 256 chars, bot/botcomponent schemanames
        clamped to 100 (deterministic uuid5 tails) — long LLM-authored names
        otherwise fail the import;
      * thin skills (data lives only in the MCP connector).

    actions:
      help                         this text
      generate  agent_dir= suite= [suite_display=] [prefix=fsi] [out_dir=]
                                   -> write both solution zips + MANUAL_STEPS.html
                                      + EVALUATION.csv + manifest.json. NO deploy.
      deploy    (generate args) + environment= [creds...] confirm=true
                                   -> generate, then import + publish into Dataverse.
      verify    environment= schema_or_prefix= [creds...]
                                   -> report each bot's publishedon + provisioning.
    Creds: kwargs (client_id/client_secret/tenant_id) else local.settings.json
    (Values.DYNAMICS_365_*) else env. `deploy` is DESTRUCTIVE -> confirm=true.
    """

    def __init__(self):
        self.name = "McpShapeEngine"

    # ---- creds / dataverse helpers (self-contained; no external deps) ----
    def _creds(self, kwargs):
        cid = kwargs.get("client_id")
        sec = kwargs.get("client_secret")
        tid = kwargs.get("tenant_id")
        res = kwargs.get("environment") or kwargs.get("resource")
        if not (cid and sec and tid):
            for p in (kwargs.get("settings_path"), "local.settings.json",
                      os.path.expanduser("~/.rapp_deploy_settings.json")):
                if p and os.path.exists(p):
                    try:
                        v = json.load(open(p)).get("Values", {})
                    except Exception:
                        continue
                    cid = cid or v.get("DYNAMICS_365_CLIENT_ID")
                    sec = sec or v.get("DYNAMICS_365_CLIENT_SECRET")
                    tid = tid or v.get("DYNAMICS_365_TENANT_ID")
                    res = res or v.get("DYNAMICS_365_RESOURCE")
                    if cid and sec and tid:
                        break
        cid = cid or os.environ.get("DYNAMICS_365_CLIENT_ID")
        sec = sec or os.environ.get("DYNAMICS_365_CLIENT_SECRET")
        tid = tid or os.environ.get("DYNAMICS_365_TENANT_ID")
        res = res or os.environ.get("DYNAMICS_365_RESOURCE")
        return cid, sec, tid, res

    def _token(self, cid, sec, tid, res):
        body = urllib.parse.urlencode({
            "client_id": cid, "client_secret": sec,
            "grant_type": "client_credentials",
            "scope": res.rstrip("/") + "/.default"}).encode()
        r = urllib.request.urlopen(urllib.request.Request(
            "https://login.microsoftonline.com/%s/oauth2/v2.0/token" % tid,
            data=body), timeout=60)
        return json.loads(r.read())["access_token"]

    def _dv(self, res, tok, path, method="GET", data=None):
        req = urllib.request.Request(
            res.rstrip("/") + "/api/data/v9.2/" + path,
            headers={"Authorization": "Bearer " + tok,
                     "Content-Type": "application/json",
                     "OData-MaxVersion": "4.0", "OData-Version": "4.0",
                     "Accept": "application/json"},
            method=method, data=(json.dumps(data).encode() if data is not None else None))
        try:
            r = urllib.request.urlopen(req, timeout=120)
            raw = r.read()
            return r.status, (json.loads(raw) if raw else None)
        except urllib.error.HTTPError as e:
            return e.code, {"error": e.read().decode()[:600]}

    def _import(self, res, tok, zip_path, label):
        b64 = _b64.b64encode(Path(zip_path).read_bytes()).decode()
        code, r = self._dv(res, tok, "ImportSolutionAsync", "POST", {
            "OverwriteUnmanagedCustomizations": True,
            "PublishWorkflows": False, "CustomizationFile": b64,
            "ImportJobId": str(uuid.uuid4())})
        if code not in (200, 204) or not (r or {}).get("AsyncOperationId"):
            msg = str((r or {}).get("error") or r)[:400]
            if "duplicate" in msg.lower():
                return "duplicate"
            raise RuntimeError("%s import submit failed (%s): %s" % (label, code, msg))
        op = r["AsyncOperationId"]
        for _ in range(90):
            time.sleep(6)
            _c, job = self._dv(res, tok, "asyncoperations(%s)?$select=statuscode,message" % op)
            sc = (job or {}).get("statuscode")
            if sc == 30:
                return "succeeded"
            if sc in (31, 32):
                m = str((job or {}).get("message"))[:400]
                if "duplicate" in m.lower():
                    return "duplicate"
                raise RuntimeError("%s import failed: %s" % (label, m))
        raise RuntimeError("%s import timed out" % label)

    def _publish_and_verify(self, res, tok, bot_schemas):
        steps = []
        c, _ = self._dv(res, tok, "PublishAllXml", "POST", {})
        steps.append({"step": "PublishAllXml", "status": str(c)})
        for schema in [x for x in (bot_schemas or []) if x]:
            _c, rows = self._dv(res, tok, "bots?$select=botid&$filter=schemaname eq '%s'"
                                % urllib.parse.quote(schema))
            vals = (rows or {}).get("value") or []
            if not vals:
                steps.append({"step": "PvaPublish " + schema, "status": "bot not found"})
                continue
            bid = vals[0]["botid"]
            pc, _ = self._dv(res, tok, "bots(%s)/Microsoft.Dynamics.CRM.PvaPublish" % bid, "POST", {})
            published = False
            for _ in range(30):  # up to ~5 min: slow envs provision for minutes
                time.sleep(10)
                _c2, brow = self._dv(res, tok, "bots(%s)?$select=publishedon" % bid)
                if (brow or {}).get("publishedon"):
                    published = True
                    break
            steps.append({"step": "PvaPublish " + schema,
                          "status": ("%s published" % pc) if published
                          else "%s NOT published (still provisioning)" % pc})
        return steps

    # ---- actions ----
    def run(self, action="help", **kwargs):
        a = str(action or "help").strip().lower()
        if a in ("help", "", "usage"):
            return self.__doc__
        gen = _mcp_gen_module()
        if a in ("generate", "package", "build"):
            return self._generate(gen, kwargs)
        if a in ("deploy", "import"):
            return self._deploy(gen, kwargs)
        if a == "verify":
            return self._verify(kwargs)
        return "McpShapeEngine: unknown action '%s' (help|generate|deploy|verify)" % action

    def _generate(self, gen, kwargs):
        agent_dir = kwargs.get("agent_dir") or kwargs.get("input_dir")
        suite = kwargs.get("suite") or kwargs.get("swarm_name")
        if not agent_dir or not suite:
            return "McpShapeEngine.generate needs agent_dir= and suite="
        suite = re.sub(r"[^A-Za-z0-9]", "", str(suite)) or "Suite"
        out_dir = kwargs.get("out_dir") or _tempfile.mkdtemp(prefix="mcp_" + suite + "_")
        man = gen.generate_suite(
            agent_dir, suite, kwargs.get("suite_display") or suite, out_dir,
            prefix=(kwargs.get("prefix") or "fsi"),
            child_split=kwargs.get("child_agents"),
            skills=(kwargs.get("skills") or "thin"))
        return {"status": "generated", "out_dir": out_dir,
                "solutions": [s["zip"] for s in man["solutions"]],
                "bot_schemas": [man["agents"]["parent"]]
                + ([man["agents"]["child"]] if man["agents"].get("child") else []),
                "manual_step": man["manual_step"],
                "artifacts": ["MANUAL_STEPS.html", "EVALUATION.csv", "manifest.json"]}

    def _deploy(self, gen, kwargs):
        if str(kwargs.get("confirm")).lower() not in ("true", "1", "yes"):
            return ("REFUSED (destructive): engine=mcp action=deploy imports into "
                    "Dataverse. Re-run with confirm=true.")
        cid, sec, tid, res = self._creds(kwargs)
        if not (cid and sec and tid and res):
            return "McpShapeEngine.deploy needs environment= + client_id/secret/tenant_id (or local.settings.json)."
        g = self._generate(gen, kwargs)
        if not isinstance(g, dict):
            return g
        out = Path(g["out_dir"])
        suite = re.sub(r"[^A-Za-z0-9]", "", str(kwargs.get("suite") or kwargs.get("swarm_name")))
        conn_zip = out / ("%sMcpConnectors_1_0_0_1.zip" % suite)
        ag_zip = out / ("%sMcpAgents_1_0_0_1.zip" % suite)
        tok = self._token(cid, sec, tid, res)
        result = {"status": "deployed", "environment": res, "out_dir": str(out),
                  "bot_schemas": g["bot_schemas"], "steps": []}
        result["steps"].append({"step": "import connectors",
                                "status": self._import(res, tok, conn_zip, "connectors")})
        result["steps"].append({"step": "import agents",
                                "status": self._import(res, tok, ag_zip, "agents")})
        result["steps"].extend(self._publish_and_verify(res, tok, g["bot_schemas"]))
        result["manual_step"] = g["manual_step"]
        result["publish_verified"] = all(
            "NOT published" not in s["status"] for s in result["steps"]
            if s["step"].startswith("PvaPublish"))
        return result

    def _verify(self, kwargs):
        cid, sec, tid, res = self._creds(kwargs)
        needle = re.sub(r"[^a-z0-9]", "", str(
            kwargs.get("schema_or_prefix") or kwargs.get("suite") or "").lower())
        if not (cid and sec and tid and res and needle):
            return "McpShapeEngine.verify needs environment= + schema_or_prefix= (+ creds)."
        tok = self._token(cid, sec, tid, res)
        _c, rows = self._dv(res, tok, "bots?$select=name,schemaname,publishedon&$filter="
                            + urllib.parse.quote("contains(schemaname,'%s')" % needle))
        out = []
        for b in (rows or {}).get("value", []):
            out.append({"schemaname": b["schemaname"], "name": b.get("name"),
                        "publishedon": b.get("publishedon"),
                        "published": bool(b.get("publishedon"))})
        return {"environment": res, "match": needle, "bots": out}


# ============================================================================
# Unified dispatcher
# ============================================================================
class CopilotStudioDeployAgent(BasicAgent):
    """One deploy surface for pushing Copilot Studio bundles into Dataverse.

    engine=
      "rest" (default) -> service-principal OAuth + POST ImportSolutionAsync (REST).
                          actions: auth_test, inspect_env, package, plan_deploy, deploy, one_shot
                          Reads local.settings.json for creds. `deploy` is DESTRUCTIVE (confirm=true).
      "pac"            -> AIBAST analyzer->normalizer->wrapper_generator + `pac solution import`.
                          actions: scan, pipeline, analyze, normalize, package, deploy
                          End-to-end RAPP brainstem agents/ dir -> deployed CS native agent (OOTB CDS only).
      "factory"        -> quality-gated agent.py -> RAPP pipeline chain: preflight (rich
                          SYNTHETIC_DATA demo seeds auto-injected into a prepped copy,
                          explicit Dataverse binding, connector-hygiene warnings), then
                          MVP -> LIVE+Demo twins -> import -> flow activation checks ->
                          publish -> runtime probe. modes: check (report only), scaffold
                          (generate a quality agent.py template). Needs RAPP_PIPELINE_URL
                          (or pipeline_url=) + Dataverse creds (SP file / az login / token).
    All other kwargs pass through to the selected engine unchanged.
    """

    def __init__(self):
        self.name = "CopilotStudioDeploy"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "engine": {"type": "string", "enum": ["rest", "pac", "factory", "mcp", "help"],
                                "description": "rest = REST ImportSolutionAsync (service principal); pac = pac-CLI end-to-end pipeline; factory = quality-gated agent.py -> RAPP pipeline chain (SYNTHETIC_DATA seeds, connector hygiene, verified deploy; modes check/scaffold); mcp = NEW Copilot Studio experience (BlastBox two-solution MCP shape: inline-MCP connector + new-generation cliagent parent/connected child, channel-less, publish-verified). actions generate|deploy|verify."},
                    "action": {"type": "string", "description": "rest: auth_test|inspect_env|package|plan_deploy|deploy|one_shot ; pac: scan|pipeline|analyze|normalize|package|deploy."},
                    "swarm_name": {"type": "string", "description": "Swarm/agent set to package + deploy."},
                    "forge_dir": {"type": "string", "description": "rest engine: directory of forge output YAMLs to package."},
                    "package_zip": {"type": "string", "description": "rest engine: path to a prebuilt .solution.zip."},
                    "confirm": {"type": "boolean", "description": "Required true for the DESTRUCTIVE import/deploy step."},
                    "input_path": {"type": "string", "description": "pac engine: brainstem agents/ dir or blueprint."},
                    "output_dir": {"type": "string", "description": "Where to write packaged solution artifacts."},
                    "environment": {"type": "string", "description": "pac engine: target Dataverse environment URL."},
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)
        self._e_rest = None
        self._e_pac = None
        self._e_factory = None
        self._e_mcp = None

    @property
    def rest(self):
        if self._e_rest is None:
            self._e_rest = _RestDeployEngine()
        return self._e_rest

    @property
    def pac(self):
        if self._e_pac is None:
            self._e_pac = _PacPipelineEngine()
        return self._e_pac

    @property
    def factory(self):
        if self._e_factory is None:
            self._e_factory = CopilotStudioFactoryAgent()
        return self._e_factory

    @property
    def mcp(self):
        if self._e_mcp is None:
            self._e_mcp = _McpShapeEngine()
        return self._e_mcp

    def _help(self, note=""):
        head = (note + "\n\n") if note else ""
        return (head +
                "CopilotStudioDeploy — one deploy surface (assimilates copilot_studio_deploy + rapp2mcs_factory).\n"
                "  engine=rest  action=auth_test|inspect_env|package|plan_deploy|deploy|one_shot  (confirm=true to import)\n"
                "  engine=pac   action=scan|pipeline|analyze|normalize|package|deploy             (pac CLI, OOTB CDS only)\n"
                "  engine=factory  agents=<names> [mode=check|scaffold]  quality-gated RAPP pipeline chain (seeds+hygiene -> twins -> verified deploy)\n"
                "  engine=mcp   action=generate|deploy|verify  agent_dir= suite= [environment= confirm=true]  NEW experience: BlastBox two-solution MCP shape (inline-MCP connector + new-gen connected agents, channel-less, publish-verified)\n"
                "DESTRUCTIVE import steps require confirm=true. All extra kwargs pass through to the chosen engine.")

    def perform(self, engine="help", **kwargs):
        e = str(engine or "help").strip().lower()
        try:
            if e in ("help", "", "usage"):
                return self._help()
            if e in ("rest", "deploy", "dataverse", "import"):
                return self.rest.run(**kwargs)
            if e in ("pac", "pipeline", "mcs"):
                return self.pac.run(**kwargs)
            if e == "factory":
                return self.factory.perform(**kwargs)
            if e in ("mcp", "newshape", "blastbox", "new-shape"):
                return self.mcp.run(**kwargs)
            return self._help("Unknown engine '%s'." % engine)
        except Exception as ex:  # noqa: BLE001
            return "CopilotStudioDeploy[%s] error: %s" % (engine, ex)

if __name__ == "__main__":
    import sys as _sys
    a = CopilotStudioDeployAgent()
    print(a.perform(_sys.argv[1] if len(_sys.argv) > 1 else "help"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
