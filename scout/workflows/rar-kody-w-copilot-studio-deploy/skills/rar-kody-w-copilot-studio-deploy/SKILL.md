---
name: "rar-kody-w-copilot-studio-deploy"
description: "Deploys Copilot Studio agents into Dataverse four ways: REST ImportSolutionAsync, the pac CLI pipeline, the quality-gated FACTORY chain, or the NEW-experience MCP shape (BlastBox two-solution: inline-MCP connector + new-generation connected agents, channel-less parents, publish-verified)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_deploy_agent", "rar_sha256": "837ba4ee8c900514f8e5951e1a230663ba5120a8cc7a62d549391e720b21a05f", "source_kind": "rar-agent", "source_commit": "94508cbb789c5f0b7a83423a7dbc4cc9fb949052", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "copilot_studio_deploy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/copilot-studio-deploy:95bcc5268effdcac09f0aa159f88af5bb9b68c320b76c9cde1957d2cef2d3e63", "kind": "skill"}, "version": "1.2.0", "author": "kody-w", "tags": ["copilot-studio", "deploy", "dataverse", "power-platform", "pac", "import-solution", "destructive", "assimilated", "factory", "quality-gate", "synthetic-data", "pipeline", "mcp", "new-shape", "blastbox", "connected-agents"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/copilot_studio_deploy_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `copilot_studio_deploy_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
