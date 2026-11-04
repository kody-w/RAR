---
name: "rar-kody-w-copilot-studio-deploy"
description: "Deploys Copilot Studio agents into Dataverse four ways: REST ImportSolutionAsync, the pac CLI pipeline, the quality-gated FACTORY chain, or the NEW-experience MCP shape (BlastBox two-solution: inline-MCP connector + new-generation connected agents, channel-less parents, publish-verified)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_deploy_agent", "rar_sha256": "9c15148dcff8ac706a3a49a941dc42e3b915a8e9cb0a6b8a147b0a3a60308153", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.2.0", "author": "kody-w", "tags": ["copilot-studio", "deploy", "dataverse", "power-platform", "pac", "import-solution", "destructive", "assimilated", "factory", "quality-gate", "synthetic-data", "pipeline", "mcp", "new-shape", "blastbox", "connected-agents"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_deploy_agent.py` and embedded as the fenced Python below (sha256 9c15148dcff8ac70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_deploy_agent.py` first:

```bash
python3 copilot_studio_deploy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_deploy_agent.py   # or on stdin
python3 copilot_studio_deploy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/copilot_studio_deploy_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_studio_deploy_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/copilot_studio_deploy_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/4y7h7LkVnIt+isnqFBo5oIkvKNCigfvPapQgKjgoOB9FTwwo3+/ON1NzrwRpbknOsoA2LlzZ65cubJP95+/i5e5HMbvfvquGdLjh+27779LsykZq9dcDf11mc9e7XBMH9zwqtph/vDmJa2Gj7jI+nn6qPp5+ODjOV6zcco+8mEZP7b4mH76cAXP/1C61zDO3tAun9aY6eiT7z/mMvt4xckHpysfr+qVtVWffb36XuK2mo8finjO0g+R4XzLDT+SMq767z+G8cszphD8kO2vbKyyPsk+DM7+mMr4lX38gW3jaWaH/WPehh+mb3v+dLn4ucEPnw8mQ99nyXxZAj76bPvhOkM2xp+P/Xrr2vbryb7/3Pa61P7QZtN0+Tt+vfpanm01lT9c563yKkv/+OMVsWyPu9f13Hc//cd/fv9ddX3+7qc/f5dc/lyXvvsWua+B+xpO5nOPa2Eb98X1xOu4ctBf369j5cPYXZfSLP/49u0PU9bm339kfXGd499+/q7M2tfP333/8X/+T7PFYzH98aef+49vP9nHv31M8/iHrw9/xuzX5//443W9ev3hjz+2w5aNf/jjXxfN4/E3Jj5/qvyyVPUff/jrbj9/9/V1ma4AXeb+bsXnz5jNy9h/fLr74y+f6/52k78zO2bT/NVg+iUi3z7/iqSvX6sv8PnHm30a+3Fc+j/8FpL/cd8LeF9t/4q8r9+6ZPrH21xr/+Eu//Zvl7U8/gTZdaZ/YPDbcz/+muh/7H6XfEvGBd8vsP/67fkJ/eew/3bvh283/9GRLnv/25H+e0Z//u7WN/2w9d/w+PEv/zz9y48/f/fxz98u/I2FbE+y1/whfHn7LLJ4uq799PHxTx/98I5/+mB1AYLg393y598rm//45+k/P7JxHMafPv55+rLpN6Rf5bH/8bv/uoqvv2C+JJ/bfdbeP/3Th1El4zAN+UVdybDMH9dx56rLfu5/7v2yuihs+sIrY/YJvOrZZt+ee41DnX0x9DHkH3/6/77yI5h8deuX6Ytfv3xF7y9fSONPP3745WfRVZdLcfvhMrb9c//l1ucurwum2bheFPM85uyHK+M/fH74zOyf/herP76OP33Effr53KejLqd8JPFrWtrsx89DBGXWf3M5ia+07FmyXFbbIblcyKuLlr6/Dnfx4Zpd6y8/pqZq24+0Gr9Q4fHF9hWUnz6N/elPf3rGU/lz/5WS0I+vrWACrwd+c+fjhx+us+RtVZTzzxdrlsPHv/z5v/7l4y8f/9uqL8Y/97AvWvwW8stD1bPMjwt6S/etoUxzFqdfQv7n//oW0cvMRdQf3zj36+Krdpss/TW8nsz8gODExzO7wnqF9AtxVH3xUc0/fij5x2/+Xpt+3po+4o9ymOaPK9JZn16t5LisxtdxfotkfzW76WoOU358/7FM2Zdd//Qc4y8udr9c/WH+05f+Mw9De718uvnloWvx0FdX+H9L/tfrl5HxX6YP9lcTP36Yn6D7bC7xqxzjb3t8Y4VP8v51+WU8/uxYP/efzSX7DNWXtvU1PF/aWJV8S+kPnzm/+lnXXYmdft37W6u7wOcPF1dk48/99A3dV2u7opIMlyvHR7FUaXw11n/9BqmpHJY2/RK/7GsD/rXzfcvKFwz+nTj4Wq0ff7gSXXVV+7ntHz9+XhAIxq4GOpWXThiLywLnfTyXPr0g+ndC4pvR/kLt5c583f/dAvn4w/+kMv74FdXx64Vc1P7Lr4Tc/+Hi8B8+hUd8FehxZj/8e38R76U6Pj9e95or4j/8+1frf/zq1HCR3LftpmW8LGU/fghxUn5Ml9hJsm85vvL6Bc7tUFyZuKos655Zml6HvA70vJLVfbLfVZ+XzWz8ZIevxPWvV2KnC6hXytJqesVzUn7mZrxif536eXz86etzVyXw2TdqW38F+PQld5d0yaux+6qa/vUjGbP0M17dhaRx6H7uvzDBj1M2fxbE9GM9XTkHr+3Xahz6Tyh9f0HrE4dlPKbJcPn8qWnaKskuiHz3U7+07fff9XGX/b6W+ZQtF4C77DrX9Kl7LuK8GtpcZV++xclXIfnnv9OVnz37p49P9fnLddL5L1dJvC5A/nL59ZdvifjL69JH31L9l29vVzZ+uTA5f/zrp4b86WKauP/Lr738L9+y+pffkvqbqa/LPw82H6/Pk3yqoUt8XS3jW/z+u4tu9l6ukkovgbR8atuv+OcvyLk3zlfuwrc0gL/CY85ef7PD86KFLO4/t/iaw98PwqXY/icUf/zhs2Fcibjqr+qT6hW3f/xy7mvNr0C+2OuHefjhevtNTP/rbxTyb38nqf/K4P/+pTv9tuSryP74gxeaviz4CvcLz/jM1fgvLH3/N7q5PIpLd1/t9jcW+Hr2f/3oLuBcsCuzpAGvpOT50KaXs5fAuLy4RPvfDxB/o+F/X7n/Vdr/P2v4tvpKmF/VOvhXTZ+UVZv+/yX970n5j69gnX5jy19R9+WRL+jJ+uVCyn98ydwX5CfX67dwX5+u416vn0rpu//8Haj9TdH9dzB85vUrUH76mK+OmM1/M1n9zcqPm6v/LpC/sOovVxf4H4D2q/G/tv6ry35Z9HHRzeti+5Ax9OmzlX0rm9/dpuqvR3+5qKr838/wW6v8NlKBnxt/drVnu2SfgJ5/1/xXV37/GJfWuQjv8m8bqzn71cv04zfMxBfvfGZj+l3T357/5axe/yBEn6f7+NJ1r873XKp2/vjx101+vJb/rvnpktDdL1+Z8u+te5/3wK/wvKj4b2J84fh/JKfL6PiNhL7Olt/uD89PafrlSFd3/Toy/vm7i4LjzwnqGwl/U6+fR4vHH6bPdg7CP0LXLtf3r7Lsuvf/oGu/rbhq8ZJY1xI6gXEYo9Ikz6k4ISEiRmOMjmkMThMMydAnDeMxldHJE4qJJxXDGHl9QmMCQiEKxtHL3tfe+cunSqk+vXgmUA4TNEzlWUY/EQQlICqDcpQmyDwmMhTJUgqCoOdflzZVn3472lcnP4P1m8T+0nmKb2X2JLDrSRmbFObrDwcCHo1Ez9rSlQJg8Xy7P9OVI1pUv+t630nRGcAkOSf6ABj3VmjUu1R5StfA7ypMcHCh8A0Ancdp8NTOg8ZKO/bJbQa/CUiVG73xNmfagvD70hQcO7HFxEDSBgNhDh52DtlgSF76nYJCYaRufG7djSiFompUlcEGkrcjmLtxxzDRFSM5OuEHVMXQBrSaF90ijzJX5PNh7o0Fw9WDQRPo15O7aw/zNu/vU6xv6T3LoZdXMxIVOdK9b1khPJ5la1k3lczn2yQiLOaPnfgaEFwd3sZzKEfQkdgKi8PRiFSuf+/huvvXIYIiE3AgiqLkcYwigevH+ty407qJgpwSG2hMYmKXGvNIKDO0MZ9fbDaBQ0QGqJI2+e1hpV1oYMqbGI5Kehc90JK3gXtQNU2/r1Ch8GOGHyItM2r8TvTzWSKxZ6S05byUGB5rGChwYje64608XiPOABFIWj5f0nXHi06zR2aGF6ueDdIt9G9uYw73tU/f6mmVniAGxoJ0FgUlvTEw2luXjy2CEUQ6YngDgXvOnCfRvr17YE0SPLO3KeMW9XnH9uLBvRH7VFENZMESMtzJjvfRZskckXGReWJWZXtHDcVVxWQ8lmXJFu/C45bnYRBHY4hJMeY606NSpIyRXXkeb7l01dQk3W4xCWfTGTrnu9soFjJib5qxeC1ySdzeYm7S4BbV/k3ILMfMlLTflBOZ79Dtls+qX7fswkPPUNuIZRTjRLEWu+90CFNSuNYwCTSqm3qGmf8oRaWP1LySupqsAarISDTk30a22paYeyAOUgDwOADZEHKIsrEQVMIcqaVUhGPPV/tK0BggyUDQobv1drtE7OttUO4jqeFuam9CkPrqbXqdbPsquoqQ8tYEbqimiKIbCS2b9rmUyNMz1z2mehNn8O6e0F1uR08bOaLJRP7gLYXnNlFSxkdJ21aKO3NmrlUPmtQjw7PiTuOLX3vPk7zfJVj0Up1iTTogFHUFl7vDAI5fCOcrQV/BBrPOekCbLZ5uk0I7toBaVEqQoT8EieZOCequSrOxbqi4QolVdnRK3mrETGvfYsBowXtIbld1vZQKHJRwqbDXdVaTFdo82UJQJB+5KKDpduHXBaL1ZZ65U1Tt8hbnzDGHx6TybsHAs8DeI+/1epNTpNjNo5xTgck5WHh110UcuIF8zFtdFcYsQpsMBzdNaD4B3xTv0fDEarnKqketnn5pYmJ+w0vreUJEvkvaRbLhK5ZDIHKB51MFGNcuYTgxHqw2xUbLHU7M1dVyXH4GWLvNKTpyy8k1G97V1SA6qPgUOUZQG7JuEKc1HKV0BW7C3pr1ptUYszjFvWh72AYtmBFoHyp3ckB63lwvokdc9vTMDSp+i4boQGbX7U3u0ZGIpx9GiAng7XDP/P5EXXnThJ7NWV4zmZW3QInJVKfRxlMxZXV2X/QZ4/IeIXfLJPV34csI8YItBN2ZR+hI5JspuhYXWVttL1BldJ8OvKZLji+fAvIOamsLuiZYcX6BXrJ/e2AI9Qiofnr7Nkmz2CvuhHunKzu7oO79zbFVUUNIAJhkFdUzDlCp/FoO28fJSbyztjDAVMctYjl6KpsreXdAnJ5hjzzhT0qJ3XcdIszEFZFcQhRTkq9wCHJ/PjkDH/RSIBo5hVmELFyrzLeMClbMoQouMB5yFTMo1hKFSQVLUd+JkVhT3aGYGuDVEigaLo4DjTfrDVZho0Lh4D0OfNoxNzR5crdmTqLBdCRibcemkry6sKJYKJoYPKaprdkr6l4G1dgbWFFfhasyVglj8XaT0FQpnJYwJzTw5kB76/CBERGNsDyfXbxbpwk2PDFkzlLdR1fp4xAezxseOG4ANqJ/sj7DUWT27sir2+ZHe+KQQ2dwM8YNNVTreKYyUbmeaaaxMjCPc8uHYYzP3GMWbhze8QXzntw5mFjyltEB5f4+0ABqtpwwWKtcyposePyd2mUfURtrcdBt6+zMC1nWroNHLW6v2cYG4QFvz5ZxHgNe2Dyo3KOY3qfdRxhjqsbKCvc7s1Bw4o+TJoUsuumsQg/3R3rbOOi5n3cvfDtR01rV3dUBLtNukmelXqNPSAzoVOntSeIMMj69Ey2+xzK3uStbY4Z4F0CcLV3u5uJbCvbFw9CkwlmeF2AooHkQFgcX25ARGstvntRBUeLDgiXUMXFzznlyiiaKGvwuR6/DoOXeodybn5OBJBu8M4VNg8NsLswxlJU0nDobrBG6RdyPHQIV/eZK8Q5HIm1cZPC8qR0H3iX0UDKSAQRd30rfda++7SBkJGaV4izCFHLEeoeqshLr5VGI9xM8pebcxRcI9h1ewpQlCrPPzgSWZKRAbzuM+gzEDaVyinOCQ2sTb0wJcKCB4SDGY8LY6WahlBg0BQQ73k2aDWv3ymoRTqGykabUUkSOXslY4dtoGglutslSKHpp0F7L2dqz0Rnbu53Gg282qdJQhCcZ8CnpkqZzmhPR7rrd/N31CpVRqNiOgnCsgFpk8e1pcnhlNANu2pUnD47juYzkQCsvGkEQx5d6co22c+/tDZTfDJAfiuOpaq8XAwGuOI5T6hxV9/XcGSwGhtmichCMQABFBxYZrQs6IsY/lBiCbECqZT2eZ12oFF9ofI+lhKGVYcGoVMEeONYy0H6/WjEMghmzUc9zs1h1py2NEjdGCbq6LGv1wU9xk3QdVC0LUI3Y8SCGYnY1lwkiWKQ7SyEyHWmUthObiMdUseNiSB7lQHgKDauBnsV48M3LpZzfYfMSB891YE+lgRiskT0+hdfNwZMrXaX4nhiwOEc5WrZ6GAo7ji1k3jLaNWJ+EMaNp+HBjWg+lu6kndCJr3i3rhBzcMoSPeIm6YxExPKzFVYWs8XIbh5Wtx1oodI7XyDCN3y6bFcV3WbO9s4gtydSvpGpuFjFYi3PtIozZpJCGzrDgZ2EfwvIEiNGzDavZ6UgxcLQCIEXepeepvLi73bnNZdkTsSC2nqar6SqNTMtlta+5Mi1L1y/bPiGs+wHuVk8Ynkxy9halNaXTCZtexbumGpWx1vIc+U15xb4QiW9QZb5XRyrinpCLhCc1graWvGa29h7QHjsuVFl+OqUulaaVQmZgonpA9oDOiCPQpduE4dVOtRTLRuLEHWArdsg8C0Z4d1Wbwm9zeY8N/kd1Ir7OnCtKTUMmSCBiEvLismbp9fDygCT5G6s7q8JmTkuEslKDow8cME+52jnjT8Je+JqrqipVaSfrUust/dJa6sNhQcPwW+aJvjmDUGlQwwwYYVaxPEWE+xw4m2J4FtepsJcCikRzbxqDlbs7q5O74yr6RsKnKsYEjteJw+RVfzOGPxpK2gxryITjt5xKT2emyaeezvK7QGXyfs8q9teSnzXZAhn7vOuPg7uVcxFZZyaU8VmoMZ8oL4s3R2qlnOyWlZAM6tq+SFakqa+O4pdOMNsN0bTmpMkSlsFKa+su54zwrzLWlsySw2apFcRsHQQKNKs72365l75oxF1xzP5dtzBNdEe1S6ADVaIvaI4NaXtoaAJCMCOR/xAZQjOvEisW9vypKJMB9m4VxrC5buvg4L8rILTWC0TXMdlOMvHXWUDhlMEEBSftjmusG4BN+4xvpF5ULg8eXmbRLGPV25GG/ouLwYUkzLfgQFT+Q1cNVQT2n3dNIysbph6KQkZEpEqk3l1jqcigx5eIAQK0F3y+nbTpYca+gawMig0g2vo3hNllDe9jLVSaEjJVAUxxAVZfCNxUdAKa+bizQMd/BogakN6Y/ARQe8b35NNBt2N4LJEyeexwQLDoZP8xklifTUnPcMeF1Qjuhkl0vU5/Kqz1wPtqBkMN8LsUqLUwUHnkmku4l13CgXVF2+ggIkXSXQem4C5t6Xl0KuOnVHqi46FXXNqsVPZDENVEiJ0AMgcigLguskzFCFiQMmQ/TDHOJATkjhmYjeHJBtJ8b0xUYKBrmo+X6aezG51zQOk7IP3QWkl6cpiVXHnjX1R6EKLiHCsMCAd9L3gwJgSUXpXb/Dzdqgu6C549GQV+y7LyCElUm2y3qbMVsOBhZVtwbK9vYq7hvwym1z7fLJTP7HdoCPbBvWar4cSnb81UD1CYvCmR0mpUWMssNrSnLrhKnB08hV2Vz4LeUBSeZ6f8eGx+ga8PMM3e41f0YZl8In35JfV04Q+T73t0HYQ9AFCnaPDYlH5uukuCDhhsfa0SJqjS8h5fIP1Q0jtWtxBuUDNmZR822wMXt/QioTk7ZEvpW3cuGu2YfnFGkDcrfrHts8iwluZhp7B8gbHeo7BtWyda8BlVrOHsLHnVbfFYWgIdldPyEMe6FITPJAxhFdNSe8FeTjTHFv1SfrNmy1CLueCTaZu5C2cBjwO5cytB77lBy10ApXfVRxlyIWAuypVQtjjDZg7GbQawvjKMKj4c9q99/cWHMei6TUt88dtmurZ4ZNqM6T6dJFN3riILYrUMOzhTlU3dCzhDiUf19xwv2j6loP3qIfRDoap+Uyx7r7w82J5D4KxA48rwgeDg5OyVpBPxGqoLk2Yy7iQJPcl67C3vT52EqTTMF+YTha4WaYrsXygWM4gFxG4cZlKuBaGqYPNkScxRbEaixAu4oq/DznSNA8d3JWZARCLcYomYd9uW25/xbpukmkjYAnqZjEwKtX0mmC8XLreoi0nuWqMW63I1RGrLjXs1pExyskqutpaJ88B32mZTIIOqUziKnnRw3PXWxZcQ6BYSupE59T9Fb1ei2hbIMAXCC0o4XxsFubILE5znYVmUEk9eCmbiRZLIgpKmfABXjN9nxKY32Kaxt3kcJxjAt1PqyfQFUylO/0arEwnM/Cd5u1dXqOgY5rdj/x7HgzjOgGZfjzmhDEKjpIoW+rt9UmTBgw+MRFvX5Y05nKxzkVug3l/Ew31dgslVKIKpyMhB18txZWo6Ki0oRCisHwaz+wkfBKQeyRQ7oqQNjhnqdpbP+SjvuyrrP5y1dfTCbKCj4RZ3IkXg70olZ8WTsM0yhELjTOfMqB40etNuDdaGX12Q5hNUmVTRrTx8GGHR2J8hDlCyEw47p0hvdf6C+HQs/QI1PA2FPRm6hpPqSGY4VHr3thTZhOL8HiyoAH+/R4WYwckgbQKH6Tui4899CUgYMZUOJVBWOqaoPYTjo+nBrDkdewnSLqVckX2kATLcMJH/G7QvHosRx2E+5lu3sTZNhK0O+sYTnTKEzRg3QsyGwR4kl08xDaz1ijqQBtcmxf1hkInV8TrfCszdHp4ICuA1EoyEtv9WVzN9eiy51BFCfhYM6ze1yDqfUQe2zjbE7U+wjlkznsp4tV2GJZP+uPWvMqcpp7jJUNVHulGmtj0I+e63AjJETBsXQwsXaqINSwdBG780KxVmbFARbKKgUZtGB79YSyLfF3EJLon9wy9yB6k1hraJmFtixYWR1R4EdU2TrmLekZtt5C4XU3u3IIwDGu6CjLJPtZL62QkZwIZTDLc9DTJUjbJ3Dgd6HhnlgI+UJS4xsqp3rTTu08I2NJ5cKzQuwkmZmHTdvLFs9rKngMe46RyQHC314WB+fuuViLHikxjKgTs+pvQBUPTr4XpKcRsBHf0ID2i4tfDwyofbu7AG+qlJhVvlSIuzrN+xzgfC4YszFIjCJShabQL+IOL2Vl46Xcy70IlNeK8FgmKBbCdoI5pgX3rofgnMxnVSlESwF+NQrQTI5guaRFP5fP+qFq6XAuaMcMkH4rDT4ySNczQcioxLbHHS5bVIEWAt7Q0avzGQn6ZEMzc35XSDWxR03mhEfU1lkHZjgwekVuuX2z3GTfU5aRAdtwb7wbaM1AqD0KrEO0w2TurOMbjnV1+QhWj0xC+ZrJlexVhsdTmg3Uz+Trd0+fIHVcLLxjroWI188jC2lMQ/zkCeBLdkA4AHjU7vhh4TcOr1TCZFomesCPAED5VC3UBx+xp8uZmwwYH8mozE0KrXS/o90RMUnpLbzSp2ZHc1I+qcv3MXNG+psYhn7oyIRO47pTpZPT6LuwRrKO5AAapSnDt68y2AdM2LwwAT3W1QDJl2DdsUgwKiMCIlG2lKrqZiUIsQka/UBQboAnbr9FNfXPiu5tbU6Yt19CEG+96W9vwieC59zDdwWrwgAuGhKYbk75icOxC3OrAHdEL4vA+hJxyGPP9PO70fhOxqWfH9I5559xx5DWDsTfogN5GJocPSm7QrRXFQqoUjJMLxqEHCSvfdjMSfip1nMmAbzFfH/kp3+jAOLBXvEAp1T9GZMOOtiSgWkDsGm0uoPmUqIycNvbNzWbDAmZSlX2PqYWzRmAre34/xdxtVfkle6xdQu6d4FkM5lTneHI8oxvM7DbmUYq7ifPCnafEQGcSyKsmqrWRvmk+//kiYkfHyQjpzVySZFf8cgg3NBkcdLAlx2nSOsyfynPfY17d9XC2YgusSaCjH1lLsxbMPq/CsXdQI3dR52uyFZqzmxUafynXZD2Y/Dwd6K4ul2PRQE3ro7j2cTF/5nnpbE9McJn7ZFDB6UQw/6pShyyTxylRgHSaTEs4et3nfUDfAJUYJ+lNoCL6mCx5P2vbF91br92XwxPfGa5Ls2kb5T2YT7UuVGvNH3fDFd4Zm4Q8MLDXW0tdY/yquHmXNitPSqceS/bpG1yYPgDiVW6BMSzYoDxkQhm3elZuALMM4iZQsGpLk2k+qtvqVaEPFelKmwu1e+Qrk9MIXRyiXvRAw0C1s3iVMnwBAPLy+dyTbreezhM+xRgDHV0e71R91HFA0u2buDjgGQJnVIAFb8n+kZ5JhyF0STWb++KyN2hXlEhW7pMF753FmDJA4PMt0Ajyjj4B5Lhz29YKYESO43R/aW49EUl3DQfQRiTJ4hrMpSH297UHhhpB6vMCK/T2zeKdQ5ZZYHwYRCmTG07SKke7N2JzVK5DgTvCndripc9SvTialnVxeKaLupMw6Tw2xNNEKM8TacxMr5Nsm+nh1uIVWWkLNBi7+Dm4CFGPO6Oh7XHDlas1vcBb3PrS1haKcyllnu9SxJRvvfPgsSWM9FsqTrQz2Zx2CG2uqLeXve5c+4a2YuevmRNfntXI3miw5vvUWpUOaZTCMC3XGeR6fiXJLb8KjG3FTLJgsnoVT0jHL6GmV64SK69+1xet9ZbKmbUtB1QjSpx71sjSiof47m+1J9SurS99iOxVjReFH2eKqp0883wSaok7at4pwab7WaFn96LEy4pR94A7ykAbg5O1WU9rHGmbbf/ZCzEzERnLzGnEYApN8gcczhO4FXnbrQ/0GdCleB/A0RIhlxieStgzTycOUVn1KG+7KJY8O+Skp+m83xMCjmrXAjX1hCf1HJ7b4WXNNbk9YsQCUWRjFEMWrwEst9gmkad7gKgpmO8B5DA4Sh4xKo9KkowUzsRhaHDmA3JKNkBFURDRgOLYhnobFSoRq7bX2Nbeeo7uVWmAtH7t9jwHZUJ+PrxHesO3okBaiiLjpyszLYmysEcQziocN563COUMndyHFvExuPfhAd0BMHAU62nXGz7X6msofY/fQsF6M/iLgSJKWjG7wohImm5M+sw7ZiOm3lUSN8fxCm8O49UZowODkhtQfc+gsSK7FE6MZEWn7K6mlvqpIoz+PQ4r+YYca2RQ8A3VMS1qRLbgMe49TUxm35aav6oyukblkILvQvKYnJjag+GBJi17pUgwzO1+NoRNPUz7Ia7tc5M7MXRIWkFPaF/PZPNjMpLZ8sZxWqjn1wz0xD30fXhCtNR3AwpzezbkUsAZyjPCkGNenJoiPgbfW5b0pN02+DHBth7rHQB9UFLSxm/7IrM9BwE7BxuYKYG11NqUnZ5RwbZweHfGKmhkYAa6hApWB2VR4EkZOCS6rDUoTWnKBIiv64GSFXkDnIuI7rIg1+P98olmQUFMGIS6hITTrrguM7dbVOG9Nt9QKs89ZVH6lF/SqenG2xQxycgSL7mIislHX2Z0W8gqQRqKntRDOA4R8xglKTH4pUGG73ozuSfUab+YteJFJurkocYlmCe7t6NI2LMhAg+9BCxBq2VfIWaD25TgWvcSJ7DtuUpBoDBv9wIrp/rMvpaCGmOSCJdoXaxp5iuFhauxlxocvgRvE36fk+aDBboJ66WpZHqCe/xkUmJRaqH2Mey5rjANXJOTGVeSmxZgDXfAugNAtgGk0bNMEuQgJEnsUYv0HtP8BLAsM0RnazuqusTp4Af5BlN1e503PsUW78f+WfK+p6xoHShO/hKSodmeBqN1Wk2ZF+8vL+7GQrktSTK66QDia1dt1chGB0eww2CN6xxtdQdtZVuzRQnr6IvFFgmdqd1F9/fFDc+Ady+THUrjSP5KzLlcGY+CDGUr0ngTxxsCc3OUlaFmJo/1aM3XSGxXsV9zEm104yPsKVQBr74bEapqmRqZ1jwWQHGqiHOlIprYJlWymV3pwPNFzTTEsfRQ2u+bOxFOJ2I22PmnO58vl/I1OfF7UQit2bHWZLejRHGcEl1DfGhTaBQEISsqw7d2Pn/Obf6ySnJUVZemX8/ANcA1HaQMlZ1gRh4LJMg8eUTmaTexjzNLKtFsVdkqu1wB5WVWYKmie9cDlYnMU88i8ZZdmnvzKMvpL6mpD84MTs/XNSMuDJ6EZxWMG8G8jhO+g1dNFgjei4l/J6tIviP3KZKs8pLvcTYy08wtmw0P7N2YtFU8yIDlpXjKJOm+PW/zPnCe57uPbTtAKnVuV0kSZ5t4bCarMh1eEyR8gMsTBNDrD0WD5R13H7RU86geGHwBCV0n1aczkDEAon2pUNFqLzLivMIRIDQDH6m6ISp5YPOBk6un5ShgrAubufbMJDSdqKUAvqGnnBIBa/MIGpxVMb093hArSSn4OEd90dHelHJTY7HxCm2n/LymQ5k/ceZZ5jaMYNIdLN8AcS9tcZ3S9/M84LgJupqHkOpJHGBOOGhxA7JJFa6J0W50idHYF2ALbLAIMufoKznxr/G00LjwRQ1fH5wRPBdi3LVVALm2bdZZLk1lU2Y5cCm6Y30Cn4LikFbdWwtqs2y2nLwHCD7xGGRPxJY7ZO7md7xk80VgPMtAvL6wAXXHapFc+QJlzHyu7JH0hKetmFf7QnEERudL15DWFfB+fIKjfY4XXV36epwEYVzvUge+gAolz1S8g+CBIs/ybHqbLM1aYDWfoOwR4SQCrFrymZhP9rEUk2Vw7jwZUe0Fx2EhB57tknnUSnxNzMB9DJ2Jmed7MrCJR3O3Vw3rYMlYe13dxJd4vy28d9U9vQwBGIdZCOj4Qks7i1zDgFhc7Sa4k5fildYRH3GQjwBgGTKgmprULN7S6zRQyKXdYZ3vPQE+GG27qMq73cWnE95E3Iep05ElL+R87Yp/u2xl/RB4hHHr4W7eikidy2GLAzXYt6ncV7/fWCqLF3dnwJAjyMKA5gYAuBNOiHW480NCl0DExcdRgbssqkwLTo/G2GWj5wM/qR8Glkwdo/WnzGvce7GtpqSW+lbe2gLjQqo4Kg17gDAysuQOsGZvG20eV3F1Ww4hMx02ehHZ0KKSn3I1UHHupOozDTc101OKEzsnl9whjZofkn5zANlP9e0Bn6/de9aUoDcsJPl+cN8enBpoa1Xc9PadJpNOE3EMMEkBqo4JPisqZYWRXUgjG130nabpdjds99FOr1wSn4ESyW9uaSxLBiZuwtHKlIWr7oyzWwTdKF8xzyBPm03KpIXWIVbMPcla2VPAcfFnI7QJDex7swOSnrPDR46nu+blM7o/E53rnx1sw3mMoZd8k3KyzA/c2jel453TrRCX9yf1BaBRAmqeNRW5Xkfki2RsZ5rzrDnoWEUu3dkmrRVCaCuGAhIkflEWKH8F5EFn+M1zvWIoGZkq2CF7HxNh0+wtbM7qkOCnjd+veZpJR3Dc9JpLZQbJiytnqIM6TZ8dL64vBcyv26UylFOee6RPlmcny2B/8Egv3dBL7tt1vbmSbm020x6OWCoAk7b1xlY3mFmadd/kAw/7odLd+XmUHEf4nLni19QIe3yzS6HGqvLU1CnwrhIGlvM+kqBeCwuxh1xjWc5tqF+B+3irU/ze5j5D5wZJFnoKKLCfIpsiW7QxYBa6nX2DVIzVlQseaF0JUF7o0lJw+F1LwNLKt0DVhZk0Fg4oC6sje2kN7kEDkfTxBm/ruVpHD4pPJK/bp7oK+iqMei2cvXlfcj7fhIFsljefNvwzeK+Y7k91xU3VtgMwOrImWta+zJ4GjLxabHmfhEvGVG9BOE0aKYlIIwFlsvCk0KdZ7ff0DGClVyT1kADmLRR3jFZrG3jtiLf4240C0bREt2TzHoH/1vqXbBu1lSw6ysRe1L03qbWUvBDlEgQXz+PbZtPR4cUWtFICgmckKqhubxQNgYv5QEA5dOFRXLphbvQNCRjIwRwx2x5oj6MqnRQBqU/vMdoxAK+Z5I1hLhwY2yg27v3FzoBwV3Ubu0BtRRbJILbwVI9irEIDj4W0M7lkiEA9Y7cQ6fYtV/y+kExtfUCD8JJdduSRTj2VR32mjdDhQ85eaAUhZcrUwouZI4CIoD7LGpC7qSSA+eLKXab2aV7egroMnBROBt+WUsUcfmw274kXDR/YswgwGpwmwqtumYpOCBF9qmS/AQ/sJvD4Eg2xwHDewCpbZT1FjUdMjAnXw0ms+4Bp8NA0o8HVJOd4tXENU1JbnEpfTc/Ucg9WeIgDH7j3M2BJ+3Tv6v0qxpdksrFVv9ntYDAL8x3laRQaESqx30567EHY9BQWKXONYsvMcF/urqRhdENPyc7xwGseSerAPexp3ozszA57euLMVOBgnclIKk+5HAFwG/H4JEZnhjTOpmJGYYkKBGkMbNDJc+co726WmpAIAnrX0QqJFPvsqMKpLMwoDWWIXgJNFhDhCw9bzjHxKirDpi6eKfFcXJOJL/Yarwj69d6p1Ad39rE/PGHxRopatLdiuCVJA5FAefSe3WomQjBR0uhZOLGkym0FgTa56CYhNDq+IF8x3ByJqCs6La0K66d1KuAgeONA5jGtZ/XgCjTNJLZ4geMDkvLwbFjQEzeJHujNo2VjR5K5L5ZQXzbS6kDEGlyCdIW7BQnn0ntvlw8TnuinV3Xdz6AIzthTgyYVq3m5ql/I1VsCuxUfcHZHzqhovMeNp3p+pqyB5LGXQd6NILsmjP4FXbMWuVhcxKI8g/qdXZXlQVQqljbabd9urB91WQolGUsTvJEvUqmrWlsVICjkbK5Z1RrbGgDYLJaLFK31o8GICGZO+FlyBud7oqrEiJPehDMi2B7SVWPC7nU7vIk7gHfv5r20ZQ0+hRsPJadFV6XBlFNde1tcWPZ7HhSLRA/HMDKHNztjSPzqiTzTCeNI8KAZOuVfOl90WL4EkY2jUcTUWk7DLojjL0SOb0WNui9A77VDR4tkW8FWo8U32ydl9bAakQ2VgeXGur8989FEVyt+E+zTvuO4VsNq53oeGslTdGt2nlm2q7YOqlk90sSnS/nbVMXKjdFoCzXg9ITfB3QmLyFjOzNMc5ACnYa+3lLkJWSQLpSUj7gQWOESKvZlGsC3uyAtbSX3zE1i33ROrwep7bdxpLCbpV4Ch+ql8YTLNsZTfFxesMrQRnNh6v2utGtwqkG5i1cvousB8t959/m75GW1JsW8E3MVaDF/VTA5JzKEcXnPdu9Kyj//1qOhnHNV13TJdeTGR32UIXvA6io1IIIpqdqMFaebCWDlg1bpHyEXycjaLWITd1wdCbvtPPjHQQ9qhe4bxaVahnHiliYML1kGFBW4Jd8y30XRNbVXBDDMVy5i4im/nUrmo53sK+xqzUFJ4Y9G0btTOLTHOpRPaNe23tUhNqvehp5to41vtd6kq0VtsVHNTu56PJ6KVBtvluPfLBzWXC4o8aNWjUCijltgC4o32IAlZ/cTmNAyzKYqiDTFjhoVCiuzmCOqKFehjoGbNbVtatwdbi5Da2DJPAayaDjdESrMJDqcnLEecsQYeWqWCW2YqJsHJT36OAUHBL3OR2dg292TjZu82JLWBORQlwATmRZ+YLARdipz1OUDIkoSRcSKnZZILDhusUtrkTrSCvva1GNZ2+fQTNW4Ed7igeVFQUO82+NT/OgDQLvEi2o0Nu7pdl36l15JH4y9iFnn8pSKSJ2VK7ee5eiiTgC2GGgyG+PATFbUE6Brksg6chuwUGHuFZ9CEF8nkVOlInxX90dxEliZMbXJnTar+wlt3+NHWHpFL/QeIt5VoHynEIBzKk0erDzh0nQmxptoLBPXXb+uIk9Jnk42a9PcPyolpgxIbew16n3pyfnqHhlVkc3l6MrmvLlx/ZowiOIbyuhTt2sgpX4xOIESSGGOmJPAqcbLVimYflXuN39NwYRCR5piSKNa8h6nUABt9TzgqoF7BUrBTZQpDfchOws5j58bLjJgkhJ72xt3CNFL1ky28PYysp1w00Os5yPJfP69trk8w8OaO2cv2SkoNxbUjU8jYNaVCsQOrKuXrskHXd73Odr1+pTlcb6n7EUbwNLyXYn0b7+iXfLWPseArvz7FJ/a2XVgMC/xVCT6JWK0tZmcx713EL4deSfqzdMis8wIFcRrqRs35mkY6WeailMA22jfgWhuKMHWbyrZdA5J7IULRJZK6asiXLP8CcTHdDsjP2UKT0j5DtHlxkHPgBYf4wj1nZZHtEFTyft2X23R0oN3y66xlJDBVTxDrTi+ZDwODeidgbqtqASU2+uWlxiU3PfnainzmrAktfgIwcohSmE7zxfe7kV6Hr+AQ04D3b6/9owamMbCFNUiI9gY5YtyyJZ1FMyDmjVq+ZmodjQL5+oVc7GgX9L7Hjwxj5cAYVoPFFDIWpYHAL+RKFDBSZejD1W9FEFqJmrePz1gKfOZlzAWgntef25tHEANpAPNKYTBxKzyTFGGOAx4Lp9+4jf7Qse3h6BOAY935o6s4WCFYhG6gbA56wLqJnYA5RyX7KoH+bPycUJjom4rcjKiWI9o92K8nbduZ8NKiljzBIuzQBHwhiuOJckhfTMpq7w6c9KC9iniIH08D5RpaRb1Im2SG6+ztmKhlTfC3vO7G1BKW2Syk6jIc3lMpCWYyytjswN/sxTYTCtrETaPgTdFGmgwajzwuK3GcQsxALY7RHk5U5++x0crPe8VEdWb0HmxAhfVwliZYCXG0o7GOnZoOaKxfXsK4ItaMos+EFjJbbqsnQZOypoUCVFe7pQMouIIve7Rnh/3gZeJst78HRulXo4gkDCdxbHzbqQf11yBpFd7pyEUpSMRZ/F2WJSWwamVPvcdM/Bq57BBwR+pEI5NcT6S8cSJbjQc53QwuUsY9AST9YkQ4O2e7pHuSAOJkk287phj2I/EcfJUEKITo3j2TPMVueRWLIW2Z1S7cFC+xGAlXvYrmwKedaL2th1bQQksYMvSm0CeHMVmmNNjcm9D9D5LmwLpeYS9FBUhSe/d5MYT0PSdfRLlM7eCcHk8VkjqmwHJGWZEuDmctGZcliMIpnzK2lH0+mWsCFjuKqQXXu8sn5GF8Op5Lla0J9IDxkRwos95wcEoNV4MquDaPmIpEkVGeah6iiQYMQqGAa0huDZw/uZxfd9RWbeelm9poVhl7+g4lgjjdcs7mYwsPhsf8VL8Wtaf7Uv2FvYx4QaPsQBJrfY2h23UyQ8/cMsbfrNLGffz1qAYRSN8rUp2Bh6ZyhvBZw5uYbnlGWaoVNjtAGXtg9GzIruS+fForIYx52uanpnCz0CSg5Vb60/y7THwTvXWFULIGMdhudq3B8/kuxdcEC+kaIICVh21pl/CNQNIerK5KdinTFmplblyukmdek7CwJuGznAbraezVCq68N5Y8F4vozcRRCMMBxceZ0UTw3HJV3hhbkdO4BmOyumDNtaZH9Mtwy+59krsNcMe45LARzntBCBh17aXTHtqGMwZ4f0pK+pCYK8B6XpMx3UomehrxNcZXRyaRWhxDt/WWYLw2r+EMYv0ykw/dOX0AsC7cXmhrf4t451752zSEpI0sk/ZxbSPKAIjYWxMgr3Z/Y2+zdVM0c+ppkEx2ptuxex8tHvv4XcJabgHAXUzh1AIR95wtuIVgQI4vYg6cIGfGwrAIo2m40VlqZu9wAgm4bJHQHz0Dl7ZQI6GewwypFf6wFlAYV59V7OSnmI8Qx+NPARW0fpte3+4oavHdSwkGmbX4UbsPsXv26MPGznXO5zXJBNgGL0d8P6Ic87VNMnejQioZiuxc1Z59jC0U4h2DYbb4tnX6GT44qWAKwprbdtV7hBO5EK99+HMEJfLL3/XjjftHpsTLhX7jF8BYq3NRppI5p1tuZ2rzfVI5LymBIbZnXXjm7Dx51tyd4bBzH0x19G3A/5SmpwwvqVaCmFd5a2EzGsKAYvmfBao0He2vHLKsS7dQeZP06XSIgJyWngiyNy/XgYQT5eqY9Tdo7loM4vnYedycbubKYYeRfcuxgeG7tfcDHOfv3oWVwXDzgKXl2vOKNsq6PkpYeiHSSt2JR2o1W4OuOB7bueaCOHQVYZKrqlKr7S1e95JF7qSW4nsnSrbwRX8o4NPNtuFe/oKtuS++PkaXOoCszW+OEZDuCKW0ub84mBaV4YQfMj1kOtcsnossRQu7dgSEJzrBYxbzm9cZzRDhb2qPIeJiklQaONm1L+qz6CanpXs8JBr+l5BXrZEu3/nCzFjLfDzf2CIEKqMZ1BYtwhYPHfYc4q+4z5t8681IPMKdgtywfN0a/OLaX1oKtOUZVi5KBPWwSJCKKQhItLyYpIHwPAaH6SYSjDgdAgbnZ/8kyKaG7EiUCalWSCg3TyDId49hoXMCOh10BXmv5mAAZXuoCZg9VKI3Ecw3bxbkMRalBYEHOerTAhzDNt+hsh0E6HWpiWg7HZL/0TY4m3fTr8n3ZUERAAhue2+knwOfI6gc+VvZsXGza323XjM2S2Hed/h1q08hJHB5R6UEdzZlCm/X9qIToDYldQzo3HxtWEyQrlVLrvnVc0tVTOl+nB1NuoSF4MqLfTBm0MoMjgzh792PGEedoWFUQ/OmnmnCtVqGuHJ9PpbChJoEqQ3w29GlhZaguslOkGraREcdDaua1mHTruBJMXa4Ug3icNofQiwMueeQBh4vTLFHf5+FzEXRa8JhA/s2doKvKqDV47FjpypPR2Oub3UgwEPzjr6h7xLrxHu8gK1hB4hyMygytJ0K33BKJ/Ys+c9CE1HMIFNCBjAPpUrdSuQvBMq1x5Fk1wTyVtR54Wk32IDmWBoXqPcaPueo0SDU74igWatwy+P2FPMDLuObsmp2gjiKLJzBy8cPme1gWFoI7+kZ2Unr3IAErYxinPQWkib1sS4NcJwY6dtJ0IvKlL3OJWuPCObTpzIL8UdJKRdsTM12U97AZwXWbcPJkoKhi+IUoR3RvX7cuHzftgpry1ni0EXTbcTJBclGRqBTzVsZj26LZi2oOz/peg8dlsFAij6QSzobRl6731HNb33r388KVKcCNuDmbn3HCGDDBgOqHL16lVOJQITxiwXO40H/sdiPxxDC3UQuUbn0Irptuo0J0iYZJhDRMMz4snuzRs+yvZMnX4spVI0p334aTpqMDX9SGTLyBDYucUoAslKi875CM70+8khWNEY34BseDJ7T/7FVJgbCay0psRpjdG2t1p7+Jf5v0nNu7/k2TUH1EGVCf+YSfJ/6jAgaYE5ulUIpPKHrGBpb8hvMYiCl7YszGHiW1fClGqU32r+a6EtSlRdQueGvOhZdJ1rDP2Sv5HatFOncq5DOGDvsppry05nP3TewRSBSasrU4WxB4ZEt09ib7Qermx1kuJkfOYN6hn/Gza9+N1x0XSM0HNbu3HZbRsbxAJQ67dRXuORZDwe13cf6te176XDDOqLBf61lGfBZjVJpYNcM/qneeAfHoLDDgAmlTPN/DPv1EUvlrysNYl/QNpQM/eObq800p/DQbI498z9XB6l0Fc1yQJdsyAV0aZPXwo6RYbwNm6mdJd55kIT+9oKt9aPRF29+29IxSIpwZZsx6segp8C0jsxCQY5sdulcvZ7oFFlSK/d6Rr2j1+G2FeBNkjnNs7RsSUrVJRZdCL7A+gv2QgmEw1zqMjUDNu66yLStx3vDi/d3AaxxptKM7q/UuIcSvfbCnWQmmOouXmol3J/XRpVP2XJ/4yceiCpq+IAL8dnqKi+ywni8Bj297yz0sZuv9q6qmjXj1VHU3qaP3m3nIi5+xn48/SjTOqoeoq2/TWjIaCxvc/IcmtdUfAZybzJIgf/JYFuJCAb5e44v11HZVE7G4at7Abc543YtrUN2J+pXvIuyLZSEX+tK8BsPv6dbdNjQhHrrm1Khn1vBP9HPZtXuijgCiixqQukiCcKnOJaPJezwzZA4LSUJ5sGRdc4nrbY6o5zT2cuyap2qfYNOT8hOipE0go0TNrnGORIvfDY9tO+SVW97kK4Ieho2bgCd/DAtixMXGvfwBe7hNPwrW1TPSmfIgxRu0NWZfyVY2KJ7d5ujX9owQ+DBex/+jIp5I5JLtcyfz+6bvpDmMkTW4MYfADvsdxmji1fuMkoJra56jS/kaguONe/ZAU4b5nIBuizbPIqXhaGdductrdLo8m9azsDIoVbucW3LRNvDpE7Sy1rWcUijnr24C/PJ8VYwtL4JbaaxkXiAfYHZiK1ONOE3eB9W0TRzAAvsRUgY/AltAquTZK9eJab/8zjGSXCh0IXoSIEfQjF4fJqseCIB3TlBf9YdLyp09MBCaMT6PkqpPcwIm/5SPYRc6/KDfCh6S/gmqT9CKENne9z/W3M7Qi1bKsxr7Gt44KT5e8Xwnem6GJwZOcXkpTjFhiOdyQLYdQuMrF1G3ieMAnrr5dFTM3q9fqtNOz6o6k9XkW3IXY3Q9i9yCoyMKtoWnpEktSIJUlY31MSYvuGKWzOQCdsVm5UAt9SwC2W0JrJB82sQ3ZGcefGAC2O1ICp/SY7Rrf+pmWg1ycoTCLvrBfmKl37itc0+JNS5jnz+KrmyIr/MGW33QarzycN/xaTc4KIpesudSoQmFIAy1kfxutiu/a0NU8BdibMtOomPqQY3IIvpyYfnXRbVqUEL84TfB34sRe+CHjUt68tET6XZ+Y5xlQEvjU3r+fseu8sc3c711U5UtyOb/ON+v7zrdLC6zI5qlvODEInUS+VL6jXimotNAGue84srkf/L8dYnbJm23RJOkg4YIa9h9CAbILz1q/J327MeVtzhgxCWl4E4rUA44TeKMLR749A60qqyqZhjYvPb+ltyb/baVjp1R/AEaw1pscEQc8PbwQooCZLQwXJX+VtToPCpt/6Tx2z7gf6ald3+6CGiU1fYsr1u5WVclo0D3Y/Tkmv91Dxt8mfNA4XLMPiiFc9uzQmHlorGBwQ65AX0ltJ2WWFdM+ClfTR3/aHowbEPgiW/3KFLtGwvVlX7kt8Xah0N4KHZKh17v5sTBdZ+eA/6t5cVf3r74I1veFd71o+M613F/nELd5YsHTe3ZtqMcKPZERFgFKS1IaleUHDMSNLb3MmyTPbAXtPVgufftKc0+IfDCGxeNp97JwH13qCyyYGj5ElZD4lDdq4idhvPUFe3UvNfY7LFSvUq1+zttCZ5dufV6NP97aMfmtZ7XZAAfxVcfLOkwnLOMnJ3PUHtw/A3v5u8kbhgldhDfif9oAul9ePC+C4gj09bBIVTQWq9ffLJK7WRfenZLMY9Dw3fXsexwDpvCJ4bJ6hN6ad2pOgVxxLuA8YjdC24lT551Wu6eal4zJkm40XOCKy7GtXDR+HEWPJ8XidqcuC4b4Jv52Lh5tpd7f9AYUqB+vhZZVI6j4HDfZYg5X5mqw7gt3rQuw47+7L4/ubhUUgXs74LXgCibVn8yTY6P1iI+cAejrXBz74QdJjjBmo5Bz1Yp0wfi+EfYkoer7ZNGdctM0BCCs8F1JXKYwgJo4YA0CbHY0KBIzR0n9GEv/9qNT6uSjEiXjdgkfs6GEbkrXaxALqNsUKcZzuI7/OAKOAARN7fZDkClhjGjVXIvCHnS30ZepP7WzSiGGvMwADZMKtQ1QsO8hKRtAqO8NLZEA4iHlHUwS1aK/Bk4zReHI2lD5E++1mmODbkDyHX+izE+pCebkdm/HkoCj8KUJRlInzHU7DmIMadgf2MafHQ9alqY30LZsP+BqZU/w91vuFsQiQP4VKVuNnRaYHFIzi/QFdg3CK7F87O5oXoJFp5KEQsB4KIYE+ONYzlXEeCUUSKv7VYryWXfnIN+f9Cl0bK2Hzt9HI4FoodI/HhNPjGZP5Ia6lpy4YpY2F01MbOBi963Y114Oz9vuxS2avR8yR7qYZaU1CxD2kPfkrhEobXtGNfIhgiunEYgPxrgIoCkF6FeKavtLLmytYkxm/BsyffmEBiRZgeeqY+YORIrovZw0BvwbZMWHqD2JBaHWcZGTXB5Qoaa1uJklqs6FL8BwPjK4sNeqwlkQJmgMMGmyLCewtwjsRpPvBbJWaUp3iSUHql8ku9UR7owpYMHHacykuTgHQmxNt+WyWGtBHO3oa11gNYTxr/ckFTmRAZ4Cxs3ulZpeqgEHQeXLf5P9zeGMmABB0iNdMXRKlbhLxh4MekZ69U/V63JjdbQXoPSj4xY+O/22B/jTJi7BPI24ANqDDhPYzYvY/Min/hj9Wc3j+S48DPxOWb3HrMajYIL4fNunhwOHJv+HGnra+tXr/AEXb/n61w2MYDORlRmcwIxZE8YDGlvG7s/V8yocR0r4Y9oFFbX9v67zxo/RGf+fCjHva/BcRCHbhDYWOpks5tcHMb7QDWl7GZIzIm83GJCjZ2o+274MbOlHK20Alv1xfn4gX+Cxu1s4yO+6PrBjiB9a6VnV2s9Gt4kc+WjBFgt5G+bfJjUhP2thuoCCruUz96dBm+5ucEJibe/ZjEwqhsj52CQ3aryHh1dEqYFfo29p5PVCcRe0UftDyGRqazB+dYLC2Pb8wqeMEqQPhE1rEM7Rr5bdkgMzj97rUc3jTymu99A6754TpT6rbWkpT4+89qH1k4MwOs5MvjNXT1vZv7g6w5+R9grY0di4jOYgPvIQ2GLL0fL0/2RE/fUa0W45Ed7OQ8G5bY6lsgHFJSp1wGDCZeyt2vYAm0EHEKr168PTeb4Y3Y3BxGV//RfQvKjMG+CJNQ7g+I6S85sxWRrmrzumj1AfyTZTgBd5mBuG10wD7gVcoQDAH/zksy/EQcKHQpp5IqmI52rBTxBDC9s0e6geehGxgRCFPuaJ3+JxPvGwiekZOkCR313NKLuWTKvz6+zPNhw3XB4LLPov5nkLgKy/Rf7HVqJvs+fuwlugvu4ZzABL1j7mPX3gQ8J8Pl2AwEcSIoct5dMrF9cjPR7pVpH5PBu0rn2kWeAq6LcC8nPHiSusbawGQxv8JTvZ7A90dmb9swyOQAlD6xCUGGqJuMMPfTeCxyCa6zlWnY2WqZuom7KYb8bVpQ9ZCh8NxZ0nr36Ex9R91p+ghtwbx59fK3105nY9fH4C41JcmjKiO8JqRQiNidL6XF8MgFBLyAjoZA83bN6qFnX2WXOu2xK8C3+xTvJzgW/LQ+Bf4+ys1CusRvSvy4kEkMl6pIPYS9iDYuTf/ftJROS/7O7tUEk8gUv7y7V75g1XICCDjqy9//mBJTGV99Obz8eNDyvf5phBn0KL+B0F6lGB1SNLe1EXfZEiKD0pNW5D2Y9kSK9mwEOAR60CPkanVvbcLgpdd4dfSx9b6elCNgpizfzuAOnaTfJFG/lFsWKiwaMvcj50pUvrZBSZv90t17qvvZl3mxg3VCRyoppr/ATFBM8Wg2BooVqZse59Hichd+y+xTS2uX9rHo4oDyixXSbftPu8iLTqtunYHqBsnZY2U8pbTI95tYZV7OfULYNYzNEzpJPOdpfbKXiFH4z6tC8znzZ0pRRp3rxz/V37LpPTfrbFByi7v4SteX421DbwSmGmoKpPXm8qbXScATuTSUqgAadrHUUxkvD1ThKEAuyrMui776P1JYfmuSrxlwns34+ObQsHbFfwKJJ/EOmHnymBp+v6lvcD9Vbt/vWmvehLX/v6m4Ulk96a/OrTl9w/IqkCo1evN1pad+ChHhsx4fcuLIQA0idNpdSDIERx+FIpkCB9mH5t28jBSF/ZUbEE76HU9tiTDFCezzkeHh8IUwZ5PSmP+tfAdY1zdEku0YASTVProjjjXEePdoN/iwyeNKHn4/V9hfURP38p2qf02pcFJ0xg830fpCPs8H3LlxKu4KFP85fEvrWP4Do8jAFkh7tDemmqZFeWV/FiL+VqKTMkeXCQSWrtrSpASlh2KL2KDfNeDhqpUNk9PWHImx0oPqX7lbjszsdoTvcuIBj3GGkBrc4ZG/pGOSlM2hfBoOl8vQLzHnaZH/NXeWDjtft01Lb7gqGohATCCf0YWBsP6fXoKJjbaDaUimN7v+HtLjyZvF3e15i8oqU5xKhSv8IZLyHeMqlVGEgjui1f6Houd6Ct3YNTjOb5nLUFDixtkUdLf0BGvGbl9O2T8/wWNXBx9La7ISQE8z3nEPXF9qjDZg2iIYutdWyg2E+poyQpqAJnamEuDaX9KYwZJI1nxdk0/HQdkfnekORNZ/cR8crb8jWEAZAgUZMH7+mzmDX7mL3Xpqs/DLSgGzczfKgmRBfkDGicsNI7NMl8JBwXS/u5J3zvPYtXw9JFXg4+LVPfiOn3R9+3DaPn7YKfBRkCNks0KXmnFeOnAImYqsKwjDXEYRhkv2mjqMxSy0RP9vU7dMpJQ1fk/HRzbBogmKgBM9uxp0f5TjFVgkT+TL6GlUYQ9mXh8BXyiMung8l84j/AvoLcl6h1UUlWAtrJEstJmnEMFXNQUuXr2yT2cWi+2cDy7ax35idfJhMoyCdns5u9qZCpoE92I7M5iZcExcIHd4rga1DwCKIrsFLbi0LlyDmDhL7ipw420d8wLhgtP7cfZA8e74jjQxwC3kc9eNvU7ftKNbh1/ySMb4tFC/7yiJMU7Ot8/zeVz3aqXa4X6H7Mid7OJSlq8OWdsba2ETCedF94H2BxQMesUNTcRRttX3r3C+JkCbR5WqgoesA6xDmnA+RtYDaG4wXrYj4JJERH+dAbA1mFkiVs6A2rHtSpEvZ5rAItEDyvO+iyj5Ij9oELWmBMVCWHOlYNtZVi8YhAfzwFq8T/LGF0I1vpKbQz/teaj38O8PX4CgPVy0QDpjjeOHebnTxNdQomkH/gEAy7p6M6Kmh7jjUkx9WsBy/9v6StgRHrATx/o4hhocxtoJvKQJGgazQGacqw+dv8+sxj3TTRm0Ok6AObvJCEB0D+WezLwx6KA7JxU4dyVm6JNduDpUPuoSQQ0IFgDtqGQPIB6PewkuUnHKJrhq6KJA6T0OunWYV8Axq5fuBPfK+UpoNUaZpXEX4Pnfzy+TEWL+Ujbt7nOZ7CoFg9sEWsPo/UuVW83NQN5Wa920jzyjae6+QDkTRSyV+LHJ8yLoFItp0R5/+rjitBfUHyZCmdOtVKo0lcDVg5lY3lUmaRPBug/i3jnIt9VCQcbnDBsIf94qGXN/HMon1xjov2RAxbLSxNeEr0dgTRBrnE8u8rcqB3ZKnGz4SycUZqyrA/1HNIAgKIfSUypVO7DEty0JtMJ1m7Kf4Xe/xnR4Ci1I445H1GPGH/mC9+ap6/BJft/KmwZmUznMSQ15//LYwkd99GjUaXAiFCPHk1hsY9okszwessCv5kozZ4zV6dr9veoKrdNynAKVELvP1sdW0KSmXebMcbn8QtInizv9tvjymra0hEknBdAGCZKyQdtrUk9QTFn/At0xFcgEPOTIDaD4i6kihDHxztjpexj0OAPE7ypjS4owbjPhG7D4YW/Txv5nZaU33jOq+mZuGgXp2dLwetkk18xjSS0dedBfc1uXHjINRc16m0nfyV1Q33X4FY2fY1UkYyxzifMuZPZewHmidya72kpb6vx95hL0kdSoonJGJJLHPPFWhxgSUCoc3CQnkixyrpyZ04fGoA01nULD1mUMOoVV0HxNCfFbczhz6uR3GF0Fz8spcKlsNPI2MIz37eSqZGWHvfznZH+ws6wfPKc53TCgtWLQXKU/monG/8KQ7NXGNkMm5MfHLA7ygSn144b/y4IO8SJixstV5e5QceWOOk+QZtDxBVN3zvWWQAZ6CzVGjuH9+1T4gNqEIOfiQbz/sINhe+O1hoCKEr/WucKpEIfd1P3Gx38Ycm8N3eNzvKwBpMZMo4aLoJ/MNn658GN19LvbyNOFHgm4C2+or7osVjw3bT+3BK/6NCnZLhB056wvyp9xkyfE79HV2RaW9P0MAwwyx2jdc25xeB02d87mhVO6wMXuHKwJK+tIjdAz3a2tGPluOLjqdfq9E9/oRuChgN0TSY7bvRgPi8RIIK2JHhpse9woC6iQ8bZnD+6BSkv/agcRx7eQrKh+xRUwMFIb+h+3qi7zDe6ICrrBtzyc0mrEleE6RYa8rcKhmfGsBN13wXLIR0mg8nZwNW9aqTXULjVH9W/Q0HKMp78fQpTc6DHnDxV1fl/9S1wJZenyaosuVMJkesc/bTR5KbEyjghS8Cy+Ash8SuZdqOPvj+C9m4zlG/DMvRSsiy6CPlboXO/c4r9Ah23s4PmLzMBfLzwtJyK7uOdCs4O8Gl0kUro7mJSbo0PvqqeM9TLWMi793nH4xlVc1gw1tOHF/FBBwxZWrkOl803wadJHqfzlGWVmHyPk3ZdivAIfNcIpJeMyJR1cV1UE84B16RLCGXXSonTzwO1x3AFqgLwUnMMUoGwhEdSxAEZOgLs6WOFNUsNIYLfmsFULSCx47HEWtSvi+xJ12eErqL+/52UQs/dQp9pMyoOPo6aTBVcfQrmQ5g8xmK0ssADbqfJflP3dE8gggpE2NiVeMAPYtyV/sodWcmGs67YKLBaj8Uqe+iobWwt9uh+7QGAvVwpjSFYvZ/VkNJ8yqhJMa4Eknqmz1uHcbsFsFh0B67qj7SXoopS5Qr52pkksE5aGglwHKNlGayI8DAAxlPDxG5umz/CGpNk4NPLv7z+BYAf3oiAFaIxQ/aynSpELp7JCqyVXg3oG0YLDYLdSCF/iwhHBzMAs7YH3vIL0OoNL6OGR8mMufaLOeSByr07n7UyFWIBG+FD91iCoqowLZ/KAANCKfSqDMBJF9FquTlPnjDJs0dRFWpV+JPXG03FAZPwmWQ6fANbX5091jsQ31JBK/eYecyKgcfOOiisP/7iucRAfm9K6Ffcjkcn/IyYslzXmBDglMRKo9PAU6W1YGyYHh9PG6usO3dUY7K0SZAacre24cLk/zVr1OqAQKTNxY92tnOrghkLnYhdIOKRmOPLjBIyjeJ5STexDNo48YvYQ8Vfp9EAAyNOhEI8ub0xyWhpJhTdreQJ8ZR96sRx06R4pAhF6GCK3Hmj6fkoGMBytyqvQgk1hPN+IR33nyfP+282x40IXGirJsqcrm6S2NedjWMQRpwChm1yBrl6ljk7Am3E7mFKC9deS0cAZaat1U+Fg0Ijv1aWHYWbBsLqpV7qGm8FkxZTNVjkkfxJmgtgzZAPzCihKoDmKkJz7OVOhYcH/VbV6kGV6UekzHHDRabjaoNk9wajp/fa0CIS16x7W877v3GKHCAvJZLCjuoQEUHz+jdPng52zcR782/65uApr0GvwVdaiNtu1ICmgpXhWJvdhd3LuBK46s169c5eA7o69exxOE5TEnq4upTtht6rUVOX1/Y3ernrEuS81SdXy8aRA2rGeWov9sNpKBjysP7W6F2xhOEo1C+nigXowZarlFV13raUeGS+PPRMqewtasN0rLPuE6nBzsLYszbf5DE8l1cMZgTutr3/NmEXMCnJ5jvqko7vP/KMdqe3grfxMMOM4v566ZslQuAly7+fuB9DThSLlT6le3R6FmfnJiHIJkIHQfiG9N6hjIo9xKJdMZXO5lIn8Izt7HaIjM1QqrnjEEIkkuNwQBhCvMmHosTWt5aeoYNOdzEOk/Eroc+8MmtDcriTtXDC388HxpbBwzaMe9aGUVxOEQjD5ocFLjCDLT03HKqHzZ2QiW2Zv4l/3WgIq1T8rnFKHTrlX8e4VSMot+GarM1fgrjISneZUHRB6vU9EDpzeIvMnH+K6W8ArH3Z0h/KSvsvYcoXtTgw4/kUSVd7fMxWjWjLJy2fu0iSjFK7WuarQe2CGSdq6XSHcRZyhAAz80D0uAXiufWy2yWK6/pfinc6sJeHBGVCtDBB84Ji8niLB+QzNMZfGo8HMtRqBAb3I26wKnqdp/1y7yWHZxbCAVvZTFLRAIdwFMLfgF9OOZdr/6Hmv5BHMOXR84hqlMVpSwED01hP+tpkfhKABVGv4uviwilneEfqdxwW4fG+9hcZOJ0BRcRspKtzFviiJUm2/DJ4FVMvWgkgwB3/k19sdIudBty6wgDCIvTl98XF3GjFsw2HlpL+u4OLW0LTiBgr5l2nRJ2BGENiLM5hfkw+EfCPNvqvUnDYObvBJL/3WudnN6PddhbE66bTEzZh23cmND7rKCbtnqnmuJybPIznigLQu4AjHkVd+Qz+b+DDd0wIg/Z3CHDwILF7JM/+sCI5DyMd1WJQY7IP9QMuQbXsN8+ZrYsCBIFjCvcFpOIUfkAyZ4L/ZkkyHO/djWXRk7w9mAH6JiQCIW2Ujd9mmxIH/C3sRlE0MxRNzqV+0yp96KS7vANC51ltr129TeTA+24vxByOFgEbNdGgv9Bmt4FYx81p4IcC13oOPvZg0iwKsPc3j5Ah6zEgELJ0He21JpF2++9VDIj0R0S9tVBH+G702m9lqCgvlbjJXRaBS7+Enmh0TKiCLJV+D5TFrAMrcFfeclCg8kzGuicdd+AxggTIRIYbLtkp7/ruYAVE3b6RaMNr6IbOkNS9ts9/kdTmA7EYg7nHNOIb75MFmraBKf8ddxfB0mo3FFlKrAr1iAsgzmJQ3uRu/nbWezHKefPk9Ejd3bJQVVPu/z0F5MLjtgi+BNpugIqhrRnnVGGbsE6JBcyysCrdjo8FPU0KSZKEeiB6Nupv6fz2CpRtACJkHvAQygUTyO5qhWD3XD+I/qbvDgzaBblQ1IqZqs5V0KM3qV14RPgdHNI/64drDrGt3s2JWGjZJkFZj5ng3m+D+CxNs5dgg8poEBkUJu2tdmsPvSWvPzR5hsMjm+4HAfBFWSxRwYvSZWR40IIHxLIcE2tkcaB6QeqPsLDgmvmhEoDxL01zMnnVBaoijNBko5HvRlHWPEC6a5wfB0XK5J3JIknuz/cQ/hNt+pI8N7WjCDyNwqzUKB5/pxZFGC7FL4JEU2NNIA9tvh83D+c/Nr2aRVVqoxCctb47TZJ95LRuy8NHHdBK1l5yyoelyP3wLoEFv/U6ipYOY+rUt/TATYc3TenW8Kvr1nob/ngVP9vY8fwDCOqlnQVgOrCsdEtyNOnvNZI3Ace8wVOuTQcg6Me6SP+G5kZh3d+Ed9if9kxbSXPVb45SDfP1dnoq7rfjRIcjmpfWxRwKPskAkTUqxZvTgoWD/XwqQEoHC+ZU19SADRXJO4y12mlZLtWnmT9/h/RYPbz3iIr0giXfyk0ZMCB3B8Sz7/z5TXaYCDKxr2vQBco6qwccD5oTtihcnxd0YHOo01ZR9t0xMxNHZUOl2nRbl3WYEZCHhBesFuXSVM3Xl78w3wpvXaX87tyOjluSC6gXEefb5NzMDF8+a0UEv8v9TDytsFpqoy44xA0eXEJsdOxsu5LKN/claKljBvsuw9HjtkmPYIUPl9Lxa8Ia1LSU02bZAIihGa9eSQDsDsmkySTFyzaMJNNsHhKv+Ru8lD2GWQHYI0hYtwksuoy6wd4jnB583zNNPsrKx0mWMbugRWwXPUEyoRbMlhdrP6rrkDCY/O2gaFlfTzRhKXJED7faVYLj1FwOxKvNADcV19acSs1spE5HYompEZidtalVoozojDuXRLCB/bdG32qHHhHIAMI9eh4M1GTZ4EUSuMUkAyU8c/nEP0M/s2+8ewB9y1qdFkUytdp8i+E0adqGE4LIIu6jbpEI5N0Qkf2v+fUJBTmfHJBGcxFd4w/pBwPrbzsGU+dqJcgw3LvTFPM9HK+cXEDVwP1EAKlsh4WtkfBuVNOwzsEXQC0q9AnTUkTIdIZb7osrxU5co5LYnWJ73BrXNJjTIF2uMMGqBoywcnGBYXo1KUm1HeXwSFC1dOKeLV0HcZM2Z5h7fm5+VSH9P4HW9varhu1j4dNZDlP/p8yb+tXKrbpXlL6CFMN/yB2o9DFNAex0nb/TAZVGjD1jgR9N82jQFp3srZxpLiGKPEkmhV7tB/3imW8jyLsAT3qXBFDoF0TuZuKTNf6INaEWvbGdqC63rd6vWnH24vC6bzNHOJWLqpFoW/kGPjF7LQoqMrYFAq4rv84HxRHQOLdt/jZ61pI4fgt55GkRILkHQOntbo0sP72Bc3eJVbWyqmOVhQgAvi+IIQV/j9KTDfoFfJVMzJJeXYS43GLeOXtUjEEnnt9ixpN7momJVAGUFDQiwpKIGQs84giqkUOKhpPYq2Q3nks38pdM6IjE2NPlDv3dt18+7I9ESvBKScwUTVzrj8DGrmOPJe1beovOrHOP8IeLD/kZjn9ZECcmw/iXdITnhn6Y2mvho246QH1uJaEX0bUwO1EPTelBkhl6weN6OEJmpWHviTyRETAKlC7RH1CHAJAYDoSgDv9PtfwicfdraK1ePPjU/xrE7zcmD/aH3NiqeFaee/wk8Pt8LpvugR9St7/07oDsIiQb8iqG9JWdIarXGXNIPAN0gHt6hHurPiRf/gbbhYuN44Cl/D44/BuUojB36pzwgaJGcdRbcQf2lqq8mQFmSw0WzZAtxPpqJS+H/IBTY1ftAA0Q/WnCZ4lYPhlZqnqej+aX4dvHznRoHQZmrgO5Y10nB9XgbP31UJghF56rXaMluAU9B32d5oLQfQMPn5/rw169ENkdiVG4XDdAv8zOlA+hEFGuPDV6AGyOK3kIlgnF6L6Wi+pgd3O3HhCG6ITZi1NbHa3FA4bsB6JI6jfxRBf/OGP7yqrg/rfUE8N7EXWbVivN2aa7yoIJ9mKoiXveU3auGo11/N5UJc7wfMKLHJx7zRaG4+GQCVyzuiA25DpidDat7xTr50Z9uu5jF/uU8UDs2QeZE6UeNkIP5E25k336UScuRL3fUUYlQB2uhnHeJejOjQZAnM0YjG83Q1Kdi1iNop2tcKFLDSikOoLqFYyCv0aDZ8ACSg+VnVQdS7dLtf831aFJuUkvLLpgrHJin8bhp16QN3Q7ctVoPa2jI/ThaQuUM/QauAWCYM8OjdD1DUHvo9eX/FTudwOkTzcW1FzVtW7xmdBOYim6qq88xe6ZsGzm6k0iAy/G2tjoZsOpRJH9HEWSAEyHKznLQkaBE5eXwNVHOfnyMSsv/ETbpLUzykUReGUhUnQ7lLi9IZNG1jmWlegOeBu0r824gPhzsy7g1+NDnj9/nR/fSYnWneqDWttcuA//2KkJSj6cghyLmKQ65TJL8h8fQ9MhSzLnHY6SWxaZsDnvqG7HOwb5XE0v0rQ3DRLxg7R4TWbQbeD6mLHkYyg0dfym16CBuQ0WYXOuTbidHq9B+YS+np1+lJ2yypBVuU3dZXmPB0+nhIjAyYqZTjcUgdakaida3gZRG6f1F2yE+vDj5qJvfYh0RGY8Fc0UMGOr9ZzGb+5Syfb2xJhgRgS6ED+0NppwRJn+6AEpIm1TcjXZB13X31FALgQV9Rf3g7ufoDzfDEh2M1QgTHWY1W9C8ad1zxCEqEfwQ6zgFLqzdXaKC5E7DMa8fZCQj9TlKb1JPuEgAuBOzd/KAzLHpzIzCVamA5Qqq++mpoYDQYiPL68/IqCROXUCVxh8AOaxlXSQvSJdJutd3O97HOmOHSWqFbQYDBq2k63UaceOuqk8JGswY8gHMHrwZDgNP3dkGgLnw4U3AdMPMDDMPiHTsSwhwFfQFzRDYvzCqUrWKsjnz650Com8LN404Sw+cCDb7oU9Nc2rlhxmwuBmpfimRR+7CKDSqFhXGkAa+KG4Vf9tE1sFpbhbS1grsVHyYvhFYixSB2pBSwRtWMshHHhHKdeoDwfUcd30fKWGf65fcJiZMcn5NfLS7EyFyza0A5dFYtXPqF8qU6VMTH7+ftVRMgu/3SCSanlGdiE2rltEgiwf0CmXU8BPb1ocAXiKiA8botkr1nHFIDvnT91RugueTZ19gOiwO8DRXXWw+G87y2bzF8ya6h1RnJOmzrSzogjRIx3q8pU6eyNjP8xftnu8qHhGRKE6pD8avmcdB0bOUarn7pJgo+VmIfBIhcWsn1SlSt/sCSliQwz8qXwenjkh5Gc+kyAUAw5PSTcLoyPCxcJCJFLKLt2L9Y9XdZbgUBG/mAWnICuFK4JBWcNJQpZeb4HdBfq2oq0oBdD4Qe8S9UEUDm+1MSqcWrrSQ8abrGBNJyY4p6FITYBJgciVHAZQlaQ9n/bA46zlCK6C44/k5/1Vj2qQxVrl0ueITzZHKec07EMEa97C4XErURcRYLAM6faq5RLpXrCdTxgsvXGGwkYvlVdmDm2wJY7v33spZ/N5ewPOgKskngGcH+pMiRoR1MsO3lI8/0mdQ1S0MlyMGmHVUz8KWo4WB1dUSaJiLwLYeiWdJnXik+euODHfxWBx8NWjbGmFOcxiSrmJLIfuGcjAhunTmcXGZNYF5P/OwXt2OAXlDQq/6nCk2yOjlT/3N/wbAs5wilrMCwWvvkAI1krMv0Teslmg0z5EmSy8cXqcMHUIg2bHpwTZx3RpY2L33qeZgZDk5t/hlbEPzl5VhCbSp6y69wg7EgjbUsKFCls1+ODyS3UlH/7KLwEQcwCFfUqKnQbXF2e7IrLxFnC69bQYw5j1NMhm9vzKlVOIPhAdwoIGnsRAt1z1oOA7W/gZCj/2PdI2cdYegHYDYxZBUDjY2lb0x97f3X6HnEmHRhiGD5/LnrVIOv9ELcRuJhRq8eaDQrFJsfMLadRs+pQK3Pl8IeiIVKifLelROXhJYglktp5Ce/ZUG5TMcrSC9b3t+aqcu2ZBHfeF48AtxOzcfejvCCoeOnPC/GaCOn4NtL0cWwIbIgT8r7Gy0T8SwAqnkSIZZqZVi/kjabzcJq3PMWJAkUPdB46XNlOYAbjJoQ+z4HaCf6GPn0T1OdD4VBnmH/Vc3+6DPk/5t4b+ZgCKYIwjNGVygZjrvTfmI8H4sJTQhcFHYrvFtOvpHJeKlcLg0jielQp0+FSe5uGoJmar2wzvE2epjWFl9Qd5cKQeuTj9Jsey0i30h0d4g1xc8MqTgyEJpISds90KdFObgV5X6/DZfRPeu97qRv426D2SkQEYkb+Igr8Na9zc9GLbBHvdbr7fX7fHYYdYwkIl3CfqpTORRyB2+FUpVjJU/7KXqNx5Ed8W8WdIb9ATyFuNUIcyBILFZTSUOtWP5nOtCx0YCrcaeedc1MQiErTEFV7SNNWlrsh3S9PlGIZds88isupyccjwppHm7B/BpyYACYk9PXbCW2Y43GF1TKh5LfR6LK5v6GXgpktKdEkaZ2Iimq1DLSmageUCIMmp7zs6HYLqUc+YXDmgiQEJHf9PDO1vBzePRu0pXbeJ9zvJpSEjiAqMKKSicTHI0IX3APTneNZuyoKgccaDYNYfBCp6pDp5nbk0azjGu0mQkaPhH1WIG+pMTzwktepxYMQlyRywVn1Gnrgboxr5Mxw0EkIhPbQd38u9HXp8OxXCmeVfzV26jSSnF3n7Y/kmcaTZxEaUIjrOmzjeDzSLx1B5VRraxPro21YPJTxaJVXiHd8fBoDycUGaJHdsh4/4TVlBHzXd7QNIDbLW1S6tXu4kG14MbSkDAu6nUTgm5DEU4rxMli5rw00iziC0vDEa4UcBgIeBRGkbcyJMgl+hZ7Xja9/ncpzZVg5ZBOoj/FsUy1mtUXrYYxjxU6W5KSqSkUYwgTUrVqU9vbR9vVcIs8Kc2N7LFepW2Lsmb9jVVKXDJ7CEu/j3LbFXF6HlXN5gIej719tTlO4DzX/xmo8Q/HL5SsbTzKrLjEE7EUW0i027eVG/sBfUAylNb/QbAGrAHjstUngH761LF837YV0dAndLpHOaoNzErZrauyvI11p+koEjx7uWZv52RBPeLVIN/2/e/LjWZRr4rQ501//2g8/FZ02zGDQTL87OJM7Y5Dvm9juaYRC1eu6B1afpJt6D1twD2CNBL7oBqEs9TEmE3hk9rlOFeBemSDBuNALB9ylAT4RPveq9yhApsPAsy2xLgTTAjhWyUm+HQN6dwy7Wt/wD7ecXX8+azx/yVcjDB9IGXZ/DzTPRktL6ifU+ICkYqPs+nrNlFHHbIvxD70b60tPZO9kPiW4QqZY1C7oEny402pIASydHTWMXe0qRX3Vo96sqsgB0OHRjXPa1TrrLMkRHjOc9ugwpvfFWkaggZZYLRelhcbHdRZx9ngDudMWmBNkNGiLCSE75vbB1cLCMJ7Xw/roR1kgAhoSn5Lsxgo8UxP4SJAqYSNnO0zRmnKpO5hfJC95qHPfgOAlVWtZ/fxYrcUmeUImSaa+0Jj5lFdI85j6TubR0juH43wo5P6n+IyCxI++53n36EtnO66jGUgAJbU/2EhH6r37zY44pVPBJ54cSJ6RFpe+Ts27VXrXgRRZdo2ju4Pyt7ixUR7H/0jJF0PqG/5qIU+t4MvsSwrUm1YWB1Ui3u04mHZv6MtKEEhPQQMRdTIKlRSS4H6rr/bmpDkHdNSZj0yd6stXwZytvQ/Uc95s4/+ncksvfaxRgHMmfI1iKLwpsYOmR/ltKlObpg6RVI5pO017s4MQAzoODY46/FRojvl4Nnm93UpdafWdvqdwbEjzwZSIYiMwXbRwYRk9ibIWhDqttX96V9jiHX1U9DQf+mC1bUnrqmHJCiR0pNDCFXyNNk0lEjJCQdgVD/fOxCxacBLv/3VZkIxd1BMSi1ZfSy8O61Od4+WVu6e8Z52czszo7Bx6qMn/W36h0IhDx7QzUKLeMU5fquWyukBv3jTR8WK0V85NrEfj3N5lET4eAjfIMEL66vAVkoIGH8/v1BhI3rQVdMa4SbK2fT1yoo+vnng2zA6rNpd4TOOEkCRfVZ0n/be1D3TfkxeXYWoljzELYSChoN7mqe1qSnVzqdRL7aIIHKheVGOSPI3TLTQR3dVYkLaUtii8L1q0Rm8lWuREAxY8hNK+1/Z6JrKV2VZynrwjo69379G3HKHTZnjjBiMkfTIPo+PJJChNSPm522JdPUkiUmUX/b8g2MHySOF/Z+j0AM17j5mfg9eiU/BAXUcTiYSPlpOTxNwI/R9dlfkt6IjEvUwWu9IsYVExmqFa8zFv+PJ9fQWzr4v5uy4FjuCCKnFE+6bsNaefgjl6ReSin3G/BLekFEhxF/FyEjyiiDPv1xkVbsSyuEKT/dnv11IUeKlhHZ+WtqeA/pGYVXGUCDSfYsnz/jaj3mNdfQzDI/YQaUsWXSkOzNMkSg+RCXE8nl/zw7UBmnr61JgTBFtJROR8T97fH+9OO/WgBTgaQoEYzEy/+alzLg83bZ01Q87vx8Fm1sfgJjx45SfaQ/IzjspVCDfBqYy5srjZC+yQF/KSS2w0wGgHp+W+5LfgotS7xFxr39wmVXGuMNGgLNiNZMnKd7gyzHiru3Zr8VstWguLXumpCem4KucdgTMKC6UBqxS4V9aPN5moW1DQNJbceqZz20zCWMOpH0H3/au9B8crm/WPAFDSEUnV6ahYNQQRwc3l7uaVNajUOfBFZl8WVdvLlBqKyAyu4lmcaMw94O6/Ej+RlpTLEiMB01zQm5IlEjU0zpe8x+1T+YjLnrMMDtclkZX1xc0LCJHr9MHTNeAcQwd2+cedemD2kzfD/BfnzZ9mZvi8p9OAsxE+8W/+zE8Ubj2gQk5bWye44+eNCiccsNiAR3h+Y/YTSqOjB+aUgtbi0dWrRK+gTGGfjnnni1b5ODgV+2dWPgdmQ4tYtJLWNXDxg5lzijQ8uXS25+sv1GH66yS2/jj0PXL7+lI8Tmt/fIVYUXB33rEX0IlxMUKd+lajkQrKMLYKkhdjA3UTlHjMc0ebglwotsmyv/BW0560/4/lzigqwX2IZjgo9fMw34GRM4yEt4FU5mRa4/6JDI9Kg/2Wa8xQ180IZunKAPNZWYjvoCKitiDQOwdRPO6MmRQNUdCEmfaGriLAiWiI5BY5iHEJAeyp1cv9AwbWKRWVuHuukFs3ouIwwBRXeS1+Ukk2FaVWReum6RiHMPc0wpAJ+fKQ/t3SSmiEWikrs7zNKUghdqcj5Nba8Y/wZdGXgnowhNAFuswheOPE9bOEbfKAH3mfwDWXgGottHkBUxr9Fk/72OXesItjx06lY+naJJe+ClVxNLki2nxziT0lLEUNIdLVTQVtpGyhlvyV/o99O75gnm8TQ+OT1Kv38ZqdfzVdooMpVbRIXe66ZXLzWi4cDSQvT13L/A51aRqNMLrmJdpXGhtKvsGYBvakOSy/4XNliwqNTSzD7Gz7DAH3kcvcQ1GoQjVlN9xo95HFJEATo/KPoPJIbhIIgeiAW5LQk5xwE7IgCkXM4vfFKrnLZ8JmZ7n6F4C/ZNeYkcyK18GVEgpoqGwZWwO/cHzq7PW8LoHJcZuRvQupGhQAgD99dNOTVMaETQ9tS4m2h/08odRqZf+/+4QYRNWMaApt4+fKuouXJS5b1rDCV1MeszEdFmvAa8L0QxsXjAj16Wd6ljo2gZxdk9hrOhN9IaCJRc9Nh1QJSbho/A6ZNnvvBq5U7XlJLMesGKxztU2RSQ63HX4fdy50cYVE2vmvyBmF5/S4ZtsStC6sZ9U0mLumZ9ZTMZh3Mr7mIMWXZqm4DVuvAb8CKTOmmYtRZXuiTTr7OdN2RqE/loK2n+jQYAfkgDXzbjMEmebWdm1bLZ14YhbdwEued+1/hikDREdrj8zj1M8FIvsKHFqefcoyYkcqYk6bFb77noOyZvBWadnTK+AxZoNzpoWVnxMbUydBZDMSUWbBQxcgXHFVp563JNPXQ9BjPFUGtK5OAboR09LFuB7JQK3iJpEaYJe3P0ZGwXarcuFRb12/9YCNlxBQM4t/S0uuClUErJIo5OPG9kurDTmZgXIxO7HVmgLHaajbFDzh3ywq6Uq08Z2jF/JGiso2c+6YW0IbKhinlEOO+CrggOQAUnU0T6EmadBceMC3G3FUpZDUrIiob1frABKUPruJWBW4HKsJdWZ4QCSl8eyrDPHGl76PBG+yXCyg/iGpcLF4Bx5BlWA9de5vEuxqlf6bDB0EJ41jtaZdU0Bvt08fr4oh63Ea7Daf0IG7CxXwwQQiXJg34jOqjtEwirYDnn43TLjk/eNxyMK2E0feqh1SM+P39GcRxwulX7L1+GAkUV9tr0MLTTkiwGtaALtSJdQDEoE24yl5ZX5+4oD7N/Qvd7FVce9KB8Fle5HXq+C3nmSN720kAoCD67umq5LFxS4lwDD8Tdadvo1fg4TumTxHcwM/2F02Zc0eex4BEvS2xo1CJMSOuL/3q+thrfBau//exCNDThDDdBp+GN2sM4eiWRCgWzLlvdpQGXDgJoJSz8ljPSJdmkKx8crHeoDWnQ/C4LPJ3+CTLp4OaIUNnht0xCgUuHZYGlohuovOyMo/fLdketg2mAsNiL2xynGWYY3AIq6nREMceAFc6BQYKgO3Em1WsyB+/MNx5GVTmdK+IdtndwP1k0gZdzILX1wNC4k/dYtL8Mozf3EouonMA/6PUqhDWsf9N42zvQfoj7NYFWFiIOV52OVO4dzATGBIxnXUDpXK3VyvdH7TBCNlvMMRmPHI0qEEGj3LVf+CMA9G9eJotI3VCg5aWxVgO5RCro1iDxlbtYV/FJNLot6VtOO5HnGq0WL1wIg9D10WHiQdE6WtRW6EAQrBEpfFyv3nwBIwaCZvSt9wHhJwt5ULkcGyBqMtiVNGeDubPkcMNi06lurwmt/7ulrFE5OfTuLUxUMdS2BtO7UTI7LSVKx2EFR+c+Kp7F5Bj/HMN7pJ43kCOs0/SQU5mIa1ov0J2pXk7CXsMWcyI56rZn+g1BkluUMnj2UFj0VbbMC88B0AEPtPl4QyvsD9AxpA6Pbdhb/r6XN1l1A0MsyPJdlYbk1kI29GXIsgHRmXXy/izhYdMwCC6oS65iJ4YtzJTAp56LKVprON19TLuuGdZmgNmaJFrWGsK/a5c0AjuzRqkeAo0TvASftREAOz6azopiz0n+SLiyDfBDweOvtuUHcOGGyzQ6HF+qiKBfudH4Tj8Hp5DZeyhCSij+5EDW7/+yLXmMGNYC2ZfAa9icUNwmJ6qyeqgkXvPdFMnql35xXF8EJcILmXwDcIfYuBtPVdTG96PoSo49dNdfuh4Mdhxgx3XYDVY/3eIv5/FPZHudzspm2UGg28/TEujNeeTWETj53PaY7+/DsHvWCe2EYMrdCsyJM8VOgmOsV60A8Ig/f9+j6ir0rkUyXFZsLgDwrBtulHF5ERE1U3hZuIUl3FUkL0XH2Ur320g7cBjCvw6AruCySsuF9XCYsjXQn4sFbHz2iy+8EFILn7DAq/JFJmZq6gQpFRfPkPYFeHRSsbtCvSAGfvzkRD8rtDH+uJVmqCA5O0PSN7IF9By5vsSWFipmKjtJqFWTIE18OHWFBJOKCiobj2QHwxXYw0tGvL3gVNEUVp1epWvmqX1xBxErA0+932/mQMKFy+TEKvk/TO8PMR+iLgAugpvqcBb6S3evftO4VmI6+NJm4H+gVB8wts+4k0Bq1pdWIOJ3KLzg7dPfUCuI2cJWIyuzaEI/GpZTzsrDeFBoh6tfewh+1vK1yrpVqHLbTrYizXtGUOFmY6karhbDfn4Kw7UhfXrLFQMHOatlmME7uQ8m12TOkjPCzHQ/EthiyQB1QCNxqRBdAUnBCBPTt9daUoUdFbvAdgMs0YxozrjxEpQTKgcYSWPHmn00hsMFDOLRuE2SexciTO/Y8A5uq3SIy1xFsqshwmfQz2f8M2sCc7qK0HFeNebA6BvS9t76n7uAhBI5+OQ5slm9YVuuAh9A9Z3AQlDiLswNqHlk1HNebZqc+NhORuAhNIHZUgDJQL7ElP5CbJA4W2hutkt8ubXN1V/FKRhJKhTyjDCKIMREB8Dl2RCJGRHLaZV81m0enfJ16MVSnb2OAFkbA0u0jCmt2zfGP5fz3lpRJmoV8QXnAuUWVe132t2e21fSq/IakznQ8TP4isaGmnqg1Xd+mHcD7Ihm7rHtETqbvawQZJL7nM0/fkzQUUIeqBecu0pIvBXpYToDiV4wkFtVBE3Qf/8BurQOGxVY2Y9zfMvuBGTew3Qgc0bh+tsvb6xm0zeWL6gNkiAw3SqzEdyo3bVvqpL8hPtyP6B/O9L9nxJ4nN5eykH1yHUXVVQx2ksCinugGQPiAf094pwVRSk+mXDB9STz9eg1t/iMl8GOYbugIHP56IckbkDhjk/MPd+RFxDBppvoNedVyd40O/1SYjUCBSKIm+AlEDjC4FlLDl1Nz8FMBEK9KM3FD/DFnvJ9vE+RuT2nxhn3ugJryoQlXFlNDJYsfZzga0o56l5QEbFkJgo1qsMBMiaklP85UJWuEM8S1IC/Kk7TnLGqghSUO61bh2X8OqbSUMpYM1EjPBSLAS5RrdLwb0h/3+fvQia3rP/PdT9DesAxmFtLW09is+Kph1AB/uU6kWfw1nj+7SJZymF/uS3TbJfIA/uXuXXouqJ606a4zuceqbvj11801DIxwEgua1M43KBFsv+/0JXMz8S71C9fmuPjRGrz3cgNdpSR1uN2PxQE25MqSGyQDD21UUUW+PFW3Xe8DpuCIHBAD6EoU2sD/na75edwpQdDZzhqaPeNGcg+xisROTA1b1VHp7NXuzcGlABpdD2qLTwZRP4zGfAjIPYrP3htO80ZobT4GOecPaTcxHLvN1a73tg2v+vqhyN+5a82efKZBf0j4S0r44jctXp9ZrZzsd7p3SNJtAHJPIHLUMn5W9o7oCbyEPobtdB7ZHESswDuL8/Uk8p65XRoizNWec7+T0BsY6itdX8fCO4Pli9yjn7mRD6y5KJe+OUb7FfPwZFIHSxgWSL3KMEFqt8ULpFP28TSBxYs0Qq6dTXqpDfMvxQNWQ+wk9oBJVN56liPj9qh2qI3UXvfyeV0/EFF63GWb8eV063BUe1WRmIYGMxCqiObxc0b+CWWfw3GBJ0A50AsbxaF4nxmfYp3L8jSHNQCcIB8NFb/wcoLR3v8ni51C4taDC5Miz8TNghsGWzWiAXkT2I8+ajVMOv+sgAbZZnhoYf3pd7k7KoXy9oRGXw9mpoDrXus4sEtv8VNVK9dFwyMhcscKIYH7Z6lh3gZRklv9FK+b8o+rIj8srytRXHq60CBdsffwNAZLDD9cVyGAtolVwAYYN0QkfHCCMwkWUFyhUD11G1dlcXlFOxx4TOnHigzBQOwPp6NQH8CN/5ES/UvBPASVXeyH6QShTVaFg2UwlawmB3iW/717wgNHFU9TDmT5itxM0z0uzmlTYSQi5tQ+Mxs9CkE/OX/9T3SJ3sA/slDRk34GHT/xbJFGXikAwacO3O8amRfrp/LIrKRwYUAE4erCWVcScLH63Nw2gORp6GGobouiVhxcvqLFUV9xGt4u/1NHwQaCxJ0rEkteCNmJixYk6b9t+E+5rymsq5QwFnaaipOzMuZVdetNiu+elMGaz7hmElyqPGapMGJISzgd4nRSaBlowDAzKeRq1fsTJRyV0oznziLJxx8au2MN+VFIGb5kYyXv/iXv2WHcQaTjqBCpsZZnV/UYzkCiXr5OZkUQ4dQwTnsL5eOVZpY9viEcU/Ioz7q8UGti5vokOL9zVyR9C+eT7gBqoX0Nm/Rsrjj4CWigLUiaANY+xtwp+nAsb+mJQkZh1jvZJA1xpo2HQDO/7bpaDy/ZnBAULK0tzUjWjCEH+FQfk6P7FpWSeK25BjO4aLNhfHw8orkvgeAx1MvIOJjOyo9ZRcwLO4PxV/sd3rSHG4sj6iKsrOtVZrMl+sti9t2cO6EEqjqQXmYxFMlAF5DDEJn6LUB3oJ454UvxCtjYiDK2WSvB/RlDYcCyMWIFIPxFF815Vxg9/2j6pOSv6xSKTYJcX8ENFtUkNkjUnocvkg9eTO7G3AtO7HNI+PcadZ8KpAsFFZ9Q4ug6E8YUs2/XtPOURM6opOHZiUKgVmTZ2yeJRWhX5y9TV5BW+OBZy/S6achdRoUSjpBXetVf+sftIOndJe3IcZz+8Orf9w1fsv5A/a6QkKOMRggZBFh5eJdpMH2rOfyqd07OIffJTkAECelcrD6r7gvJ7aADwbWsGCO3ym1KBCNg52eg4ss4LfaF3WPpP7+sy1vbmPi2MOVpoNj7SonZShFFFdHrEeuD6zAD00L+dDyVx6F+yz3w6W0wGeuugHB5cUkgBgDP1HbDe1gZjxtQ2kjly2mEqjVzr0Q5/kaUjdr1eGPFYBZ37Ocay4JkRJwEWv92OsyUAa/Y/PoT5ZJPjEbexSSUm0rwAlYOb3pVR22i6Ja/KLQKj+V+oHWm411J9DZ1foVuPkosLJgZNk2587D57vLNiDJWQM6VcAn3OtniLm6SlbHdTC9uPrThAT6Vn6t2yFiC5cZpPaRq7Tw+ArA/8S78y/netorPMDcdEv/aFPPeXzubdTql4f2BQerhJHtImsFdYPWDFGMsmlT1ZCmMD2+1vrdBjueGl8aptM3j8cNrvUaGK7lD21AsGk9uENBe2SuoRSnf3OBBafMjDaxWlYOq02G3DgPbifcCrlz2Rj2O9zie6q2/Wrnefjr/kAVJ0R0IOZy2QYVyxGU4epv6E9b6HIfy9FA2mMU6/HK+5Pb4ZnjWNpxRU/NSOZBqRYGJOFFm3TBKDtbvrP6SdFxSc03SdSwVp8yK3LyBgHONgLLaINZVEdg72efq5q7N5EIEZKjllOJtEdO0hg0UzOhbbh1R7LdOTfvEjOnBW9uyFRj0uJykThhmMIKzE8zVxQlnYuhme29ZZpwfD831nvMcdmFwHpn4o0nbb7atBzkWpPDdwBk2n1a3PaRofcVHMssIRwJPa0M8Olj4W+q84aDWrwBmOIn4NCVLRklzEw48ABty7yLK4U+mZLJHwsDxOX1iYGaMdjv0XWoi/temVcOocSQ+y1qmHZvo9b/LQG5b70+HYMm8VsKuKsqsLDq2Dqi/tdyP25be7W9ANAU1H/XZOSyufnheikNwVZ+e0iazXl+PWsj8LvLFC/bTFyBRI2Yegg46dF3mpHwUttvxuqFzQiMICAwaXcNiFUCnbDRyWG/aj2K091cTQH21w+l07kEsc+O7tdkgBcxqszxrMa4wUJ0rqxRpfzxsI5q++i0lKG9XOgBoI5FQ0NuraZKklAv72Wvamc+Gou5vtdFzC8DDiIFgTQ5j3I1j7j+li0BkewRedF2nQSE+PG9DsgPCXQJQjMMFv83/VY9uMMVtuwcZ6yUt9G7kUynZziF4iWiRoqDPLbLdNuQq3G1/EpNBpfC1g6Q2gH0WRSOj6nKtNju25MH9rod0K9z+67yTgzgb0GNuXWNNMdewHuasSXByNo9NCRCxduoRKk+0H7a2HLsEm+MVMp422uJ9B9BIx6T3X4Rj2qyHw070WCKnveCn3AGTKx03PgT3AQbrF5fDp0HQGCfF9FbnwG5jJbt1cH1l4A81Gh9s8eLoAxM6tXsPYzHycY8onPuawQNEOrHopHmC9EBWFce0aCqYqN/UbvxlnX9C9XF9qK3EYgjE4BT/UcekZBaqRnI8idyMUMBOCQAMjBD7tLLRTbsTM6opXLGmcqGrWKXbcSXxZ2k71PjBbknute1Ypir+Ceh+cSSsoRdlgC2PttUFT6kCRV7ui9Z9j6qmANlQ8QCV5BaD8cFzlzWMyfGsIZhlE/7AhQjOoJ6tdbS+JOQI++aVNEXGRHQLYMwxgvfHo+iTFZDaAs2Q9Ir1YeeRuhy8V1H8oIumLpvbmZCOniq/JdRP5wOZub/ZkN+3iSOwTg7tvP1ctfhptinOY1wxugwTuWAC09wPCTkoa8M7YKFhdnbiPoJxEBkZ7jqpwoBc/XNZgyeh0oGR6wZpzVIDE6reAPkybNd6ZPY6KywpkbSTPAjIUS8Cs7zYEQfYQIX9MzrFGZRfOmi4ZVUrrenaoo7i6YS375JrRqJdYQhMeHvu4wmgC8OLqpvjeE16v9ESKDl8yjf0qxoKgEgD5fUwrZfRPNhbjHLwmhSpig3u/6ZNAneBTow/0OkmK6x0JaK/tJuRuUNRBC87gtv1p75W4BOUpjNV98mbq8yveSU6jwQmNbZZAYzpotYuWbHcK9xqJGdHyq3YWG8gTR1Mj4Cgopj2yrTSOa3xe1r/NkxAsqDC/qdPVoGNof/KBYhRz8umoJB+ZBHEXKeX4oxVTinX0esPjwt4wwMuONlMOoo1wVUPbs+u2c6SMxSjZLmlSyc5Dz7jflUiMPMMYuDO9hYqalOa+HLbsdcldwZ5YJeAb+gmas+5rU/wqKeJVjpHedTgsO5I/7zS4MgGrphZp0UblFGTndsIwSBmyjQGgWA4O8exOaKwXKMHHwg8w+TCnRkVYvv1C17T2wnAgHCPo5yrACiNvRpCaSiLMhfCCfg0/o+2yS9dOAD986DGxVpPKlQhi4+HPzUGy8oQOlh0ld8csA169feBYtF8Ik34FNTd89ZXGQ7kNxveYqm8T1OcSbgE4QPW/cUIhuSu7ZCN/OYlR2zhlJdZFeiQOht43OspcTtXOWJYT6uBlLrePjnW3mqjDjuMU569aM+qA/neFHpU5zhL4/wnjj4A73qdilWxdevDz+ulFcycklu3nTB/vnXADNIkKlXa9PaifINOSbRnav64xd/3TKRhPQfNOx3H0VMU5BPb+mL7aHKIcOvPaJT798WLsm0z6puRv2cx8G5ICJWRMbLjQSv8G6SPqZC9nI5pVIOUSp3spTma8O4spD00XZLC0/vSge05lJxPIF4Dt7TiIgNAl30jmW6pFxIPTcRjTQFW22hKR0CHe2GoXSgQouB0LJzcdVSM8pez2PShjWTO3ufx7VfeD1rGUFzjwOfWmcmgvwKf/3hQPg/CN53Q8DTQ/G3+tVukCQFnxiIwGhn5/iLO2BGDaB/TWrf7YZNcuNfyCS1rkJFciL+Y6g8ZQ/9zD9FKPmaLWdDgJv0vnY18P5cIan/GfyOtkXjLQtubZKF3ZlgHOgx3tA/++ZlYRMiuP8dPvtCRooOjExD8SbTL6cgsjqHlMssmECFr7VgwvdVbVsSQxXPsqSX82KfNTnlgbxdkpFdesrMvA8Yw4bUDhu/O4xxLHyAX1y3sgufr0VLAJ2DcggXNSxgfyBv7BRpdjEEsUxW5O0yUcydtxh08wHWqgGyMXYt6qWSD1zM9xFBcQA1MlwxZE+0Fq24F1X7odC3MXNSanq4O2sW1KKpLbgHV+DCBvH4C+i4Na5ytvOviK3JcD0eAhu7NYFmOaVEzbwy1UgPDLarqmOBcR1shoknGDSdNfE3pa8Og6nWR3jLPEM3CcE+0VId9/GsME4EfPLFD9hY8WZ3jbvaedv7JZ/eJiLr43uoLcBmgzSRQyYit6ksOLLb2qrSgofP8IjcnFRWYq0MqWc5Mk5BEuOSjUQzWkxv23LhetXWBgivrNKaIv/12GgeArHfP82ymGgEPi/SfypSRoLStTkqN6SzT9VUY9nXc+xknLp/6mJ+qAjfP4YeyQCqMVzN/ELqeywCwHPJ5/wE9bc8EEh3rwaashdBQAws6xzhuBr4V0SRedh3ip46mbnmLEJUOMA7HebvdmXv8T49aHjZdN15F6CkV9RFe0yDEamosUTA/zlg9MKSZaODXUL/ZNHv1+9kkDSxfHN5LgXY4UfSVeAQbEO+Iihs6Zhc+1JFHxNX9si/uBzE+UbWJD1Db0Gs+yDpRxFyZSvMXKJ1NBUVYuO8kwhJPIq9YvzwiTgCvzCuB1EkbRoz75PDa3PKHgPGRnn5JbWvM/pYchSg4UdirjUD5DzHbHEZtr+lmpUfDSVDCce9/6X02eplwFMgoEVBufdy7AAxN+dJ1dcfjh7bokuHLLWA2fvwDLiu4LrM5FP6c1kD/a3FcZDH54vHPZvs3/8fiKVOxxjjwUwE+XMz2eH203R/VH8PWjtCGCn/+zKtyDqUp81FdvvBIJwU6IC+BILflxk/3PKbGDq75o0RsYGWpcD5ccrImLcU0iP5xTD3C4bEzd+gG/Jp/7n6KMFX/g7DOHHcubWJd8B9NU6zydqMe864AL1vkJgQHj+G8FREaF0RZy793YEdNPYcV0neAn2MvycD090zzYrXQfyzaGR3ARg3ETl3YoLcZTiuO3yD6R15XFNRFfHjo0LBm7z+fHVUirNTC744ct7rr8aMtAYqHyJbKSIHfCYYHr11yFkY2wv6klR9TsoYUVKnva4n2fLL8M1RgAEG4HZugVqR4LHkqy6yVlu0LMDbMtctPAJb4jyfCAvJnTx2fOzQNFnqQJr9YAVRNutP9EpPyfH3T/AqZa4R32VeGCH/dsA2ExAW6fVCWNsyIXjx8L5fE2ddh89aOt66c+2zxKrMNgG9gEs3lSOCRC79XJC6UebVsEekBQPy3oshJ51zL6R6PUZQfLZLkjnmp7/6WtqyU2x6z9RRjQWJOZ3dtIdvXZIpoY63mlLAgcsMW2MXvFV6WcJWgkusXE+aDVxt0F644iuMLbhD5v7spcozeS2wO+KVZZo4PMNl+yC2h+R6knePveyTgHgklSYCahPdH1WqrorfbqPF0Q9fYOwOc0/0/xFnAP1aLnd6Cvlnh1oAAJR9gdVJkWIXtL1QMSHBxbLqVJYkh/+0MGm9AmCO3yC7YrWM2olokV/VxFpy3ow5r5GJNyrZ31EPRsuaRo/ldjpkCajbUyFOuzNP8sRSHH21Ux+EIlQZJypGNQkTm6LvBmsiowgLgYGvvxAZAacP8oltneWFG+sHZywqzlHheoYrXCEWmN/Lz//lXnmIN2oXGFsFEyIaB9/ngKSJcGqZFSXCSHp3DhAh6As+vxNJm2eB1k2q5BfWSvHRCdVhNTLR50/IzfdpqcG8VosKTAUh6s6OY+6Hu2g63fSGWIrtBh5K1mBZnPWHFtAXxb2stL9ym9sE/NUx97V5HSpec+YqU0QqD1JsTl4JIGcEqTxA5DhgstF+O5P54BnvIMfg5DNdQd5GVSm8kglgdXOCSGuoKIwcEXajsstEjyuKJZtc5h6v4uL2o0iMnd+VINu2cLeH6wJRUx2qcxDDZRn2s/TBOe0g8C9wRwLfVss1KrJe9hvwwI5iH9dQZ3kfMxqQMh+4zCayMPfpxutmh1cj3C+/LiZXWXRugPX6KZ1vKyDupKjusJJoF/tHsN7k41XNP3Qc9lCp9xwzRGbBGNKbc5m0tIBGF19fNlSup/50qz/zbmVuVEAxQlzuseDRvbIDwHgYlcC+a4sRtsO3hXSEjRZg4NDrM1ixCob8WQw/hSQkDHiPp6SJdXf314YTGj/RugdTBn17Nn0njkGFsc8Rzv1TjmA9IgkAYQpVqD/bT9pNK10K6p1Kdy6Qe729WV1cRf1KRSRKwC70o3KEFlAz3NthDIigD2rwrKIUBNdG60rPux8e30wHE4qjYbMAusNhMCW5JLXfwbbryQ6FOGyI+DZrB08oUy1RqrOwspqmTUYrtpoj0iiDiNH4GJMaL7KqRonKz+G/HwJNXNsSWV1CY0JBCGeZgRJP2vNSpxD0/JYm0KIANTJr/7gIjurx0GyZQm72qOVNlJNdBKrOGFpB6QFxhiwEFPDfdS64U9YdUENuv/dOKObI4SKqqlI73yEw/Tt12e4L6eGzi/2VNiu2Secls3PNXBW+LQsNaHV3n7Iya+CSYvOlENAoDmtvoyhm0taGpB/x+0iIIGN+3RQMiUxNVR5mRZswavN4ktyuziJZPuJ9kXsM/Y7Rl6s2Jx7gfKd+cdGL+Ts0xxvg3uxeeFz4A1G0jiT/UhL13JlxQYa9gBAlF4/0m0Kl5qZL8FG/koXyM3f5kM9qVyN09PL5z1bgoarrcEDb/S4hFg1jgNotrFuMI4duIBwgF+ouE8LHgF9ud73GWm8stoEeDyIh76noeFlG99SeUNOVEzAB+MXPcQy1n9CoNPVl8j1ve3eo6bdUYmuPrzZpDxoP4jeBF1CHPXjjJvAVptvI1AqNTUxTEAlh/VawBB/i6N4LAkLYiyGzieH96iyhmN5I4SKKMnOC7CA2twZpQxus4PBgMOXwpDYcXCvanpPul+rFVeWqvOgZ8E3SS9eaDzq740k7NfsV8XS6zHAFvwt0h4wbjUmdjrt0F7FjYYvbzfcoHTMhOPVcW/hGDG9pryymgwoXZzWe2h3NeVhIlN1auxcfB3RMOMeBifAge6wtWJRmeV03yzs4AXA2WXrxUSrGKEbfLOb3B7N5/yrs2WQeoexFEKLRR5FHxv3nPg0ddhwf8ogS1LIHMYDpg4kxZMI3LX487H0OMHH5bqAShg0ykXiYf1+Y4JfxqltrGekerAVqLC78DOnnV7UG395EdQld7ARiNdWX5EGU61AEwVSD32Nmqas+EllmB3sYxxp2ywyw8Vd2dglx/pBWhQnNc7w7bL7xTTlRnZl9Vnl2iECO5l2hj7XijlerXS2o91MTWNkgINE2KKqdEudIJlgmoFhyadz/sQDmL7og1G+MhsAwRSJhDTON+OjqPbNwCIxyJa/TRtYi/tTYp/D++TQljcSvJZG/ERhC1ZRfzPjujAhf9il71FptRNYLx8Es6UzNfMgGU/OkVIQoxvxYRJc1Uw/yET3+wdUTlUc+zQTNzRQ/lacFXkTV410UHuYgGePGQergsqZWGBUG4hPaSR2RaifR/8qaXm2sux9B+o4dHRFTq3gV1GBALlxKqLFifz4Ga0sCfzV+oCaz5u3UoaBNzzUVH6tj4PVTZM6QezVl7khkmTSJlSLepWdVEhezIeLvv+22erN4fYfkaEGPl2u8/8t9FCcHoCz2l9rlkgG1TktG7BEwynNt4kWHsisd1O+0UWv6CaVTQ8zmxvYinQ/J7sZ4Ln5C4ENFAh+w7rDhvNYWn3jAHT6+51efBj59voBRXM4xFdQbfBC4yIX9HFpHsQbP00yTLP5mx045fyaSic0uvWJAEbT1HHUpxxfmehN7Fgjx7tJ8Xgp/4r69R4VBPxdEiZLYckJqzwBVasE5ncZ2z5lHCocz9c0h06mSlnkb2Ro+4Z2phzG6BmK+wIoXRb3RO/rwMqJ6pQ8f84q8Rfv9IcNXf/SrdGuquco2DfJdJltbGWzdsAYPusdbEZSelfMgqd90/TuKvdXuBujZu9oC0hlcZXerI00nTym2+YHpEUC6Cc78MDEEBwrghF0FUUMu7T5eGKXg2j9U23FAZOz6JQaQWMMM0Xo6ITtgQ+Za0vcK1ePwer+8H0lfugAyLNRd3yatLbXnnH9iiO/W/6isBNEpraFwaE47+qzQ+dBPmypU0R4wC58vKXVr2nWQkP9BsfFg6P2SlegggLckt+nmjVQ/AxAFj5Ey3aq2h1p+GYpFD4XmJl6zdKRmxnxkP+WGbIZE632rF8R6Lcalkxfedzqc1sNox75aZ60mBQpRG3A5GItJLq5rWZbQicVotfjcJ5giuaeDvWQqjjWzC492trzcZAfQIsMxk/oiGH9lvHVMdYgRsa7vn/iH9dPw//eRK27RsK8o0wa0ltYPhrJNmtPh3wKD4s8oEBkQwq2BXilfVYr01HuOKySCig6+hHa74Km1ce361JNfcToTgQYkIy0wmnrhRxiqeCGMhhsBZa2gxkpQwX5Yydq4mpWhZW7ZBWGH+UU0xPBXfX/3s3o978n4etF+dwD2ruiQxA2uwEOIuRLVu/RjKIgY6A3pft+DJ2o8X6Ashm9giSTfhUEhbnqk4Gx8TC+ivgqV0zvy++aukeBWZu4U+9HtqP6Jse5FSU0vE3HOHzhwAQ9N3mS77Yv6vdkcTyIiIyJz3jFfpUL1xWF9qkyYm2lBpVL3mocWYThmOUPAzZgXq1PPuEZ/OmWme6OlVxjRG6Dt7nnbLRn6ySj7KpS4vNday5sfzNDvriqoT7bAzQWpJh9qG7katRHlhd4gYc83rOhIddjKS8JOUYYlH2mv4PJOiyVUjTJXjDLvJXcPdCJ/n9hrj8rmBW00rwGVSrtFRXAE+i/aIQXY8iMgxJf6cNklvh1ppMD7B8OdC8gIqCBRYK82OIAhP7KNhNc+c8oAEeoj2THTGN+9btXgxsQTdyH7x+a1QC2WoTHU37AzYIzQ0BNG30/5Ar5+PcGyozZbk+u/h8WFJXPMenu2NOXk6mdwG8IMcotPHdqbleaPvmiK4sU86W7GSCM4VPBPmn+VhL1mtacyvDFCZ0qgKQjiCcy8p/DGaMPNGC4Xa29ufguORf6UOWUGwUF9qCTFKNUZLn4vyW7aEkkm+Q+yBliug55yMfh45hDa71idlL1C1wc0i200QYsuHzA/RrE0+i1KgIp8qvq83sgIsaI+kC9Y1+hTctBhvTPtVjuItMU16dJedVEqS7aKcPNG5H6XZfUk1+ACT72K1a+ihEKShI/qmhfMDdC/ncqAoisfnBpEa8xu1jYShbVPdbtMN59mv3TCQSyNZX+vXerh5sEpkNgR5QH/fx+F3UW7MSBT0/yFbSNyFGF+oeFQphu4gapSI2/bvtQ6MqUlVciJEme68x+Np/hmtd+T9Es5QPO7q4Q58Ik2nftgPUGCK74oNFoBwe/aivWbcEc9O2IwvqvhIcXqwiCJ1ioAoWHpvWb3O1KiR4SZaCro30mNsEi4sOckL10yHRFmc3BAWpijNQezHsrvmQ1hxr8tKG9B3ZgMsW39oyOOugvaFOjSwz+bnRIjQRnEQ+w7iG+Wg1BF7lnzxATYj+1xvtuY9NKDtT+mbihhjfuCa44h6fFfbArBxweVTNW0L8EK8EflRjvR8047AVlURH9G8vNLIx3lQOkDSQJGsD6KZ2Qj3DoZaaaZALAz3A5ciliCEs2Oc67DbQouGjAJ9lTO0DgTjfB/lsQ0ZwzeEo1tfys7QDq6l7olx+tNvNj3O2yLyMIKbE6vuK4JNJLBENUQwZr+wA/zKTkNAB4Bsh1KNI2RBOChL37g1ECWtX4YW2B1lX5P7zilDIjSdS0CHE4nikcNgLap0GADIrZSJaQU+Pu41KOlPz92uh6HOrznAZF1x8A5BHGvQaYy3UlyQV3+r5Ox5Du4lbhJidNo7Rn2H2SwkzkBc+cEeprCxcv0gmV75KBT8Mj6LaKH9vCnLq9vPVtrP8X/OagTbbQQ6V1DqmpWUqL7cOq/Ow9igRQcimELt270WAguxxOfURAl4jV5wbn2fHCxTKKB/MJhTllsEDc5WW9lwPO17tWqlIoInw7yxCRy0m7NMMWEUVoDbKU6JOzTa6rJQvTA4+vb0JtE9jhr8+RsWzHRgqsOg0qXFAc5IGCXCySkv22gm7CqWJ/eBVn1Z85Aa+3nqQ8mwgYFkEt9RqC9xeNN6YGOni8Ue6qnt8e1Y720E9p+KrqztQJaFhTuhHo7IRO9Tvtn+qcmh9QHAP4ZUUv1/xbsPqhFQg+oGnmtGA+kkUVy4mt92oMdZevnTfw1Z+oas6OTzHlMEo73pL+zR14TjpYDxWL343QXdmerWCLQcCKKxsQZqzgL2nOujMUie+vIGeJ0+Grq42aHbyfzXvTpxJABb+H3zfh4p2oF6osV8pB9SNC8c798a98R7NcDQ2aj4+RhMJFytYJcMNqIAZPF7cBvBMf3HaazhqzvfH0F6ZeKsbnIuIttiqnAr1U70qdomL8/f04KUAKpwVwexO389ueVBD4VUaFZByeYM4nPRWWwbqlDxE5uz1JI+eHFbYwa+i0PoIIBUuGzEzBPVC37jAJu4fGQP+Fg3LVE3iNXfynPnsUGMQQhH3uCz+eFhDCGuJwlbKzWQv3moTtZtG71oh1I8jHsJ4K/Gx0p6HnVZhkW+nTuXRfNCF3FFaAz+ecTzT4rX5IdBDbkgWNISM2jFgwDBLVUhU6+8+R+quP2MRWIuV2t40XFuJPaomHcFkqIb97bsNlcNKqQrcGaUN0msMwwUROQ/6ek/aoyZmD48QzXwV71KhcBVzGxfJ1EFb93Q6ynqXE8NdlVGsh3waXfSpaE8CgFRv8Di6ebBZeIWG9x1kE33zCEszKTj+Mw6KglfHaq+/FiunBqJ1E4vmPJHYkonBTri35ytKBsYt919s0dthYhPUq0kAAPYnYfmDQR2bqlXbvwrQAGvQdzWuyiY1FY8caOGfr+535mV/hfByTUSyjuTfnExfnDFlaPy7oGDMvyum5E6Lj11WKOHv7s+ndcbuOHzVFLnqt7aEmD6towPCGliIU6ALAf7lS0IAXSxpxfENyAEoCP4NIuzBa4H+FIsPWviid4eHJVP6QT23BPGrUpaQ+OSHizcNw4deoipkWtT1wZMo1HZxj57wEJa8ufcAddFmSv1cqs+KZQLSCkSMPfweWBfhRJbjLoNdOZlh5iIwTWFmvVSO4AKslVhxlZAfizLNKk099A56a4T0dlvtgH9atJQ/0ZRgyxcLTbF5Xk6MSwHstyTKAsT8DDLz2TxCNsYill0eFj8ETbR2jQp9MarsR5nzTrj+gzJl4bWgIm5cbRYou08W99qvGptT9EACEj0ErAPIewlLGexzWP5/gv84LVvI2tNZ4srgaI3fCjgBEUxq7dBR61AopA0QPJB/6wHFal12Gvm+HTnOkUFVqu7MVVRC1qpudazMq2HhMSNoza8EB2gRU1tyABhRF3Es/BPoU+xegbydLh4Vpmk3ZZGX/3rTcrLDeWQ2WsdZU9rFm1dXMUdXvClsexFW4XA6FT+kVjhSwPn4vueciak5FN+k2U0AqOLABWV3SnHe/oXtH7ltbCIiq/DIsN7juplFPYdAS9DZ9Cs1dc1h2HNzXayL0HdcgPuPvpS3CWlBLDxEGBAAg0OeCtfDRiQXL/9gIkWE9W894xdgP2Kk/mFFgn6e+JMSRQTTgfQdu2AThUC7cNzVPm+5DirJl17dw8tJUGKK3qpYIsVh7zbgI86VCm+/voEAsRKT5S0YyFba68OPiEeKoMh0ROZ7LbaWMy52WD2TXxEvUNk5aMdWFSdw3MuUwJJZg5AM9AksINAyChUgLA9zLY2tI85DtXfJJZDGr9U9aiXD/xph1SM64AvlOZfN5KrBiQPfFpmQxYUbZJ8BSqu7lFJ6f0XQSETzFb3MM/+WYhx7y5zVe4zvci3RSEWt+issKDjT5zT+0zjiYHZBXkocpH279Hhk8YuzQEwar9OGvkjzwTel1IacgKA+jntg6RT/XXVm2DX3Uce/SBqePOncNZrXFmqCMib8SdHW+XPNGyx47uyaZY+p5+qpubhUH+CtaBrUwKhKlNx5ozKUHm3pKq6VZ6Oe5eGf4CuojG0yhHplQDVvFTmsfxTO6dlc5esgnW2bZX4WNApQJQCRHGIjok/1uIzXk8mNZEv8SkU0R49iICleXunYEG9qV881Sb2Ht7Ot/ly3TxHvc3orQxp6mJ+3g+gRhXXHLphfz3/+NkH6heq+bLmydkNLhdTdPZdvpO8nDb2j8uW0Q4uV6kmxWIBdKh/51VuEP/vlRfGWAAC1G9Ra7UWlxkQ0ga/yEcLSfPlUoRMdTCxdvFz+3eAFtfxG5yzUjrX6bbkDLl68PyLu1EZgkWddcX+gtD8yHjnIwSwR50Lbd1nqXEHnUIuO/JMvJ1/wwKTk/HWQ4qn8TVnHGoIcSQFhaqem3nYnz3tYCOBHgk6J1To6mtLDvkN08JVZkGx53hTnAUFVKuwiC++PA+H7Tb1cpJTq1HIP5r/UppjF/PEsIiocrvQPjtvBuvZsmKBYyKMDgsZyYn+/ZIv0CccqmAZUqpVYw92vrfLacy6yw+Tg8XscgqXPQEwo9/2CAknLBO378F7ROt/qVaQnm1ZKAzEr570mZ5vPwPDhLSz4XamqMInXcRZD3E5zU1AC7IaZViYYqN2+MPHKtpAuAMncgVtPjhaAndJZ4wJlQvBSPFI3V1eCMNZ9XUPMbknjpUAtj0lSgnFPU1N3IsSPIM4iEHFFnWXU94e+EQmLcfqnxSWOiQTF65DB4Fyta930/Nj3QRm4o1LQ5Di5ccL+PLnw6EDf6IWYGqsIaqxuWd6XZ83S3+iocAZMfs8hjijkzTB6IL8SPXq5vjg44TA6KJ7FcXwB6UCCkIUe5y2HfEailv7/S6nyxOiVrLsC4rn/CohA2Duni/qna/scuVQHsBoyYG5muYkLZIavUyfrjf7e4j8LqXc846/k2+EG5rAr85vkVtbWjV7g7+hEb7epgCl0/xCIwm1xscSSo+/l9LcNccHgdkGgZP976dc2H4+GGUFTKxk5rt415wftfaWwRkn0GbKHwbXh+xzlPlFLBaNXA6JVzbHuAxVqN8usxDHG4mix+j4b/f14l2a738FfqjaAOtgbkkO7nsFi4kITJHQ2yiocibwJNon8exIeoXjvipmQoz8WTEZ0Zfu3WxMx7733b9PLXosNMmr8BVtWDJ0OmYmQf7BMcnyuN3TE9wqGg4YO65GMXR/eC8u8QieAPOK74NjRYBnuVmwbvN4RHDlZQTSzkF9IkyQCk6UqZqxqwCfOU2LLK1PqFIfaQjvWDMyWBgk0/FZH6xZg3JB94KqNJLvV0lFrRVodN+iqko4cDKoDv/Jx/FJ3FloNAEEU/iAVuy+DuFna4Q3D5+mGWMzknSXdX17s3JI23LOKAkQAYSRZewsHrEIoALKn2WY9J/GI/p7aBQZB8niV18KxSgwtiZcXcxAi8mcn7RRW+xXSyjw+PMd42DkDQFFJBubb51dptOzVqJeysq2TqyH2EYN9TeRWb/K9BTxuN+J/GZUAPAkwJr7C9CV5ATVC/At+d34WvE3tkzJ0aTsF2vyfc7kpMbPa2wQAb/TYKO4mQpQjGblqMH2YnVgpgK6p0EtKm1C2gQfKN7O3XlPAvH8rzp7UkV4ase21HYceNy5kiditALKCp7gETf84r+XXg4chqp7+sPvmSdTtjMBcwwnqyizTqxwgHN/WpVXZZMdXacAUzY5GZo/YL15WElllvtRQHAI2zBhseiAjepnUzZcjLFHzR8bVg1cOHRQHOSUqdbKy5oNP9KpP7EzSlNmXwxlMRSH3Tb00KcsF6zTO6b1V/+l1t2quiUv8yT6nIaqJy2NoMbkH7ZhGbBKgeU7Y1D4VoezLpi74m4OSPH8DgrlA7uBNDsa09TJu3B5SvhQG/3bCCx0vph8x15NPYoqoCzR7dyMqrP2PS+iRMNPo2m75Z4/OQ0skZdteCxIMkKlqKh1ay8YG3FCuxu98kUVIMfzhKAvijMcwDVPlevj9lUQvpSEhTNgL5YFwwx3MNiBYtA85wZt1Wx5yRfX4pYM/CUtAcOX/nZdD8S4iydPqwTFyJtq39n6VfLFmZLnAhcMkGQxHM0clORHCIo+pJG58qnWzpZ/O+ER/MQGCNZo+U9EgPkuW9pgMHAX7euQAW54fPfDAkbLt+5uE6EMguO5XOPQXoUScYf+HxsxDZuWWOVimdq9htlZpGgK81aYlTwJgF73ruPI2j0t1iM/JgBe1fClhxgqIO9wECXu4uqdjSj9tqUivAPTVA5AfCGTUVwG0bBqSXIkh5Z8hbQVD5qSGSPSawcZ9VccX6bEywUYmQfgQWAJ1GFNudU7iiUX1ZTzFykZ9g4BwLBz7eflMdpgJeC5ro9tT1SDTDej1KKHzRmlTF3Iy9zaKOOsE6zpXZpCAvlv9In93b/fseP9Me85ApSvnOTsoSkDJ8AMQXtvhvSz6ocZ3rbWYYvkruPgoOqV1OQlpB2NLog2lgA+lZZSOg99qOZqms9riPjbK17bKreOwRnvBBFCjBRpzI1WLvyCfgKTjhcxdkxf3w/9MalFRRMwBVJbZrchAqftD0mlLn53qVWyjr+6YkSRjY1uDs8rYWp2YZyzQpP/arSLnpmdJA9ecXCf29YiCaDUHxcEK6KOQ1SkYKABgKDhqM+c1Z6ZkGXaW+39pL2kXy17sVmJd/scMMSkdKJWmUaxsza1nFxEvK1ksnWfll8E0hVObZ9/zomMaNgNlRlfkeXA8tL1dL+kW4SqfpqRqJKjSgTAuwvVZ2s670Isq/HHbqiKLe+L4awIV808X2ZQ5cfGCebLa34oJgoRU7l7ae7vtsGZVFVfIyb6osQgVyl5LBIrSmnO/uXzF2kl3AWWNXCxTtK9+AXkiYNIp+w+zn1rmXhUBRZKldKzdx+WGX7FXqrH9sjm8r2BGF1crgwDmg8l0vOVrO+Cvs9csLpzXkiaIPGt7DieI7piH77ZKWSnzZqX3ohCTcseL7QdHgOE8J1pIf2lBA4f3BS8nNX53Vj8D8BZ7lqUlctemJfyx6MfImPEIXFuaAxnFStP12166sm1LR/CGWGylxohl7CXjJb4o+O7uks0UJMwimxuj7W3KUMN5hL40DnrVDXAILqaYMFP8h4cXAA2DjCxfuBqdz5R/IEnltQG5UEWYsqJpa0yji19g5j8Ly2TgZmVXud9CPpX7iiOoiT8OLtQU+mxv5g4eO5V2OPwGbhrQJ5UWkS769wpypzD5V7D76QboDhAW5DkK10KfDOSWeQhi8WjsZSuPzStEAlgUq8xJNza1qken4A4zMgW9G+iJJSS9haptwknLUGRGjBeN2BPX3mW31rLi6n6qiFAuHhWJrAUYcZTMmlvAA58G7wyv0HHk7EiIVwAa8YbXk/QVeSYzg9RP7z+dbp5brld8UVjkuQtFpoiGIP40hMUVTkZjj+EIC9uT+9pFEwhgcs4fCMhOPcdHU/lIP6A4wfW/R79VZhfU2MHp0bqcLSWs/YtkB36BOUrf+RXyN1oYknWYjXkIZW/dQ+QbF+m5sVBtLjAMT8Wd8eBB7PLglrOghYb6DqwCWXl6UuRF4t78A29KzcJY3Pxd0ikhwbKlgxNlkeTEC87Ce5/fu3N16nXUXnzzeFpoxVMRNvZg9fz6g55IW5d+UevxfbG5e0afntQ6qwCPaL8kVdlh61YQqG04bpf7/+fZjG5H1W/SrjBWGJma4Grw8YvmC1J96YFSK1qhjbXo9/KGUACF14bzRiHDhFLCG2mvPMULURgOF+prNSc/5JZ0UvanL80CGWmIWquXf2CLNBfvOOhR0q4LLPr3K26dnWoOi5i5FXFejyidtjghgfK03lshGlnIl2BjbVBO15CRPijb7ZPJas/1eYTwQkr8hA5KLJU1QBaaWut+3pBwss0h9Sxe3eRDWEUg8qKGK/JQ1IxTew9f6fX+gAYtqkX5mIjvThG+w8nsEJY4Y0jughsmumiCXfEW+B/VcLmmHKf8Df6Gl9kZBDKSoU/M3Nm6tGCZl3gRy62mZX8n05qk8M65tvO7VZ7gcF90ffHdUFdgOpddjuFkbLKCfdGQTyBFaEuZFdGiHA+oF555gEGs+27B9VtKmfnKCPwAy6CjyTcZk0w+hnHlBlxYlN0CA8hziIDDyKTPbEwotx9kxJHUbMo1jWyCK4HFhtFCTXm3J5ZDevlOgWucUHPdzXFJFq5HOknUpm9qsKSPV27cfSlKPcMiRZ3ani1BB6qpblHjUL7jW6EUbYr90d9VGppHH1rRx2rP9Irfs/b6qIpi59MIpdwDHRQYZE8dHUCWK+J40nISemtTXVZxM93x4MiqMmQ8f+yrledO8q8OZWeikhsFI1JzTwO0ggNLU5Cc41BNT3hRrCrIaEqyT2LNgTcrnoItxJ3gdvC1zDxtuGEZXLHxXH29C03rw9ucU8OXjLPz6FWQduj04xNjWydbvpjTXyTdCUN71KVFalzgQdZT74F9dtFZLuZee4VKghybURMoa45zWUg9lgdvmmKpMgMxGc/mHgok/ERuw9HcS3PQZhNZIyPFbRfePEc+PLBjQeQeluE3r3V6IIJFL+tS9c+kMuNKI6JuAklsuxlfFpgrLOARSC3HMUiAT9qmM/Ts/1GepIYm2kLa4MZBEvgyQYigSR0dnU+WJz8m1FWNkRTjMRtGHzg/ooJuE1GzmMyY9AiYfUIGx3PoK3vqaRoidjL3jp/tccPLF2AAzqBJfaFnucpuTrlquyOFpwxLBYVBzZ9EskKNemMgObLS5HtwpgwJ1K3HomKqDQfysYUDIAD5fOIWIuq84OIHHh4Ucnofh9YfL3XLuNKW7cJdNdxC7gjQnNQSLaat7tsMUwhCyzlVnJBQaJzL61ExLXMOTST642hpd19TXFzzwi1IfnVuCqa3qHOh2oJwaEwcGBCNL/6ibVt/et8qEfjcftKrkC91rVYxwGcbbFTErmyoZobPs4Wc7lnq2t7TBGo9Ex6g+eYpsiZ18iogERke9CeMrPM7jMbEfh3xIGKl39NXEzxMaMXD57XIHlXiXHxb9d2tryoBvIfCNfezLaX5lWEXOfn5LVmnpzw0oSCMOT+LCTxtX4Dtb3OQHdnMLltCuOEkNUq6kL4YaX0B2uePnyxRwqWEOVeML5XgVTCw2q8mSEMBitdCCl5/JurOhy9UpO+JYu5/tTLHqWiQemQdko5xomzz/50AXoVGp2sElSQ4OQXc8jI5gbmUY0rO5MnIuQwKdxhDYJfAT5uOcFMKXGIB6QAmnWzRL1dJLgDVJskVFnz9LeO8sipuSVaWp/EWiq4LL/k15IhXX/XeCxRITz2GJ6IhWJKUooY5yDf/VoTpniJQ/G+bQDemXHRQqx4WXp9QTYEJARLrTflEOKLXsxofR1xBCsPwDbe/GVZadm5iOUKSn5obJb52JCXoLDw0iz7k6uUG6Kh0WhdDlStlHzwXhgQ982tTs/mobBWlfPjE/zptQsMneEuzFHfptwJgRwCC7p/lDaElchLMtNk3e+FPG3pRGGOwBeCbEUWGggJVl+Q68XefCtYllhx+DxROHlTc+O2YSwQq7aZF5xmyqs0B6m31IffZhp5EIC06AtmnKDd07y11jlStIIcJ6QReoK2S57ivR8qeJiWGteJs2DWD3T7gt2ynTs/dGe9xA77yXD5TkJOffTI5FUnjLUvou69tAtTRFgUdEWP/8Kdi6wxOlpvzdxg/Pv/auEIv/gWe7xUMy3DxBTLPVHhNOQhmFu8tdkE6BiGtq0hUuVt0GKv0bjS+3+ex0dRsfNfuuuqyDXftZYk2+qLbcX+BoORvQ6+YQUXzxOkw6A+8756XKoG/lVwRY71sEmhjGxYVPcgJizgihUDL7WvGoYxBcVOz4fA5HkU/wKYUvjU18iXufL5XYlCEYWmI+ZNDQG96Zh/rAfUmCoUSl1WI4DOT4TLOyJnkGVRvwuQjePK8Mbd0SlSLan3bNX+DfzQTBgQDRsGi5jgOgBkEVUBonPuXNTIJrHRD+5gp00vUSURQ7J8Es6m4okVr2sd/XWfA9cJ43GUAPa3+fLWxxJvFApDfpwk3HRFefSLM5FCkTHEq/+ezP3aYSFAVmy/ZAi2LP+TKabqDaFhTf6VyeSVOgG6v35YoQY9HqdfV9ruYZeIhpkpmMHzI9hziT2PruV2MErf40wFRI1rLFK/dtGSG4fyv7FbohSWyCzhdlHkQGzfELJQao1JC8aavVzAiudRyvcVAPnZDUxyNbIkYTaqFDfyZf1UQSZJjQ3UpLjC7w05WP184s3F/eeOI52OUg4iH3520kGZLtea0ARCKGiw5UscqDQ5b7NuBkjFtuBJXx1fEKOBg8p4KE2gF2e3sgFMV8GObR03X9pHPuX9Z2eQrnscgbWSnIqu1mlJFbEgWNDmy6J4XE6ALpwWLi1L8f8OABUuN1rTP9j+Jc4GvQpMEhtIf/PlahoEql+AmVD3ULlc9pzsxZ/nrc5sFXNIsp6/rOS3PrAMWNpgeYAm8Fq/Hl+WK/EH6LuUCzTAbc90VMFaEFmS5QtJaO6WwKggRFN7yA4qJg5sf/2msU6mDuFTpiM1USP/zz/zvHJsc/3WMiktVHHyQqo+CgUvPVifH7g5fxbXI0mfb0HJbFCH92pWXDktRGlf49niJD6QcjlQIgWAQ1uuWOMNy5yZ8Vo5FURu37L3xdxx6vtvrAERKmfxq2nZzE8ID1vbe3ueWSxRqcxRw129UPGZcTudgjf8ffB0VjSfEvv/p+xmaEU/mnglo06w8rM3RiuI302SPhSva5vGNibrZVs29QWbncmWE7NkHgGqFltfHT+b8uFGseGa38KIg2WcGIKdDJ94dTZ7iH4R0i5eyw1QRFmsPqGMVJU/9b9Z+KZkZFgaHOGhTqfTyyyLlpufAko+5ziu9XVdAhnAymELwG1uSAJkFz3GnYvN5UoKkHKk1gXgrr3Z/SbkVzSBrW3FZz4L/FZb/xblN2lQOcrSXcIDt0xU3kNkspeo974TRLYixJ11p3A8hCx208l/WwnCAr/V1gaxs6EIm/X3Tpj74+IyYwxpbj5Kfdv621MGsh9b5/f/Kp+zB9VXL7hzxB3izyRbKA5RDzmpaMhMM0EkH3gOeJIyVF9ie6wE8Mmfe5hsp6bJnBEYu7P7gXL51/5QY3ooj74n642/nyutsmIHusFSOZS2+kQBiPXW0l6dsL4tUxE6iYKHGBxR74oEKqP8jGrPxXlGxBlJxpHddokBfGDoUn/7g75ztlPi3R/Eo8/XBCnXIKKaZOuywLtjccbgEG2HL8ixv96mAlTVhsbViYtYK2KPWivHc8XxaPfjs2svtGSnk5skVjKk7q8n94HdpzV2QanbqZx3OY7JIsD/Ogfopqn/IjhM/T5VyJfG3+47U45kAkQyvYxcYzU13iWavnCkTW0OGzNkviSj4M8lEPQbn54Ap5hhkD+g7tGyusSon4nK3ErXbO1QsiVhkx6YNX5o+++cN3VO9OoSAPJxgtH6ig9FQVbS5xu8R+BwSHJJfMQDgYft/wKd6u3z09lEr/+RY68Xscv8PtSQGMy4zP4o+29dnbRjQAkl0+Nel33+u3EQTn2TXBvmv079R+Zjf1ib24ctkRZ8U6qOkJgsQfs0Rnzrtpt3lPq8umKi7YDQjKJrPbXQ9lEaUaXkVUL4U+aeoQiQlukWYD8zepQkdN4PlDJyZ5fLG7w55Vr3WxQ4FGcWUPSY/i9+W2uPLINXsolA7wcjocpiQ5tQ9w4NZqPjkGbR06k6tGbIIBI39IsRo7UgpKZE6Ahd86mNkHGlBBwyFKhoXtgzQYKUY3UqyjFCBvLdS4Uv4lE0UkEzHwYDPqwUEwuVn0nAowZBFlEVTK2GSd6kYWBlRTId02EZezH+G3IEBQyduyd+CVyYRYtyBf4V7DP1EkNPUvVzwLEr9LfC+7p+KMGTV9oi1v/B5ozaN5xcW6KnEfFeqGTzxCMg3+noyjGQPBB0ugK5tpeKcSe2oZ1fG4tZuXVyBXgT7MJePT6/5X4/mc2JtvbjqkfC0UlW1aL+kZ97amjKx//YMx0WHwkCyGEHIsFUrG9P3hNsl7G+k+gpwCJwFpOLr0g3S3vF7MDhKc2yOKpjfmsFVTBAwBdNTyR+uo7x6/YxsWfoYFlqROQt6Qrmg85Me5+N3zG0g5qgx/alYEKUaIsxH5qWKAeBg9l8iidvv49LACW/FjXuDkpdmnaYd72p/Xt64IrnnfDkik7aBOs0/zbIWEy7HKgjtAgyJXg9UEbfeNfF5tK4r9afjQZo+ppmcvql2H+sbhHK1mSaBX/3/4pan6lVwmYIX96nKdSBN+CyZiN6+5psk9Ihr7MhZnnktvCVZX3b0Zq9M9/N8bhI0FXjghEPi/uQxSuTZOjhy0u9g0QYUKgqVj+oRu87U6y6LXN64h/V/2oWPk+UjQ1aEYztHsTdy/kJ6T4Xdw/GyBnr6tXZAfkXbpBUX4Ljy6jnfondLRuXhEMI8hLdQxAEnBGJnrC8f2cSj4GzjnHau7yOrqMCh2nPAmvp69bjN9JcI1DzmZdA267DH7qh8CIgaYQdGZsm+X2W4Tts4Gix7ydcLts5z1tQJOXixEcHbKpzSUbw5mB00czpZqlXdLBmntDyjISkwuovryWzeAH2w6kVK/ofAH4Nbx+8Jv0xMJ1nld3CbMn8glq8ob9KjP9Dh8aL5nA7VqAZf4VjHW+qMGJilGPOISBHx6grXJxyuxtWs/C+y7JB0g4NtZ/ezaMEOAV9bz8G3u02X9tCn1MGLP1fIwDUzmOFTzm22X+MsyEj6K8xi+cpn/NPx+0tK5C+AnZOanJGJhUsVZa72Xcx9v+sEtweFffqcL8FN41Jih8RTGGMZoWW3TwjPPh3nvDuVNKUkVNn9bYeIBxgCA1jNC+NM1UjkiSGlGik8BH9hwoqY+BrXkSIYSVfoGZtsvJdv+TldmEehewYMDLXrMO/BKsiCB3cMH3W6q7hEYEDgD99AgTOR3H/eSUKJwIbGes44Fq+8U5GTFdx64CjcmFHDbI6x47nBbOYCARXDLiXXFXlmD7isYAGKJ4M5rZe/eea1pskU/ndUjGGfDbqhTNj4yMPy9iBEI1PAbKhtQuiU/labYwV9kzbNlVgtQJ/jIXZRQ+OgfpgZ/ggV9jUmwG5x/RydU0BYMpGtsbsLFl6k63/G8ynS74xiJRx6Nt6TRvxUJsmsA61xo7x7PmpssJVcCiz5UVRW6Dt/bh8hpJE77u/U+P6LT/8/BHD0mIB+47Ih1zu5sKP53IQ+id2ioNZxDqCs89SyqLqBbcWl5RxcU8xn7yqpdcNAWaoa1iIK8PY1GfUeY6z3hYiz2vjZD/vahGbLK2gBsPLkOv9qoq+/qo6WBLmKxgwKgTFZe4odfJFlZpyKOqwR7gACQ9sMcL4Uo1uQ9Qq0r5adJY3iE8+iHuiNgxf6I2KrRfD7TGXCTILyMPKMr6P7OzkxZEvKH+Ta0JaJRLx1+8WrXF/SB1E9CI+MCEsMJGdNl84JVNnLdAh88FWUEj2kulEJrI9NlIc1jyjNW2PBMlCz+1YctPk41TeWJCEBDesJsuPVK6n70BmlevVaoJdjsMG77ti44+G3NnIzEH7bY6EBsw4/j4CqiNBn8rD/UVBtbU3GtUA7y4T27wLbInoBMsmT++UppJhsnNLcRnJsVYrkyR0nWGZdBcdt9cg5s19xiCcIQyguvIzv2XoA9+10A55t8RXW62OQ+RqznM3AVjPOYIj+Xe1oe60+TZE/JgTYjpOqIAE0Jk6qYIjrNUfVAigtjwD7Ou8F0bUhY4hoCjsgefBhjRLcBxh281Q1pdTJj1bx+87ja/zgs38v02XY+mpmdU+rDZlcohuFSU6YMz0ZYldL+d3XqJo83/iLbb/MNJ+rTst0KduPIgPbJRJur8Awqmj+ifFYRKiuVQ0XdCsC+w9PlopSTGPBTP0xc1QpWUeIkaThUZkPHD5T4ItW1JM7SZKXqqdti60OXp6H87DiKRPulL53nMc6fuR81hwPYSawnQmjMyvUW8pykYo5QEySGnJHXaM/NcAo4cnXXhBYK/gJjn9eemZAXfZU0sPxKFMSBR1nC7ySDFXCU9Og1tmIVKnU5eOczLXu3SS6DkvYoRgfZQEVPMrzEqfkLf4hJQM94oW7V6BSJcGpOR5FJEas1DL8GohecSNQXSMGJQnDM1Ajcexaa/r/Oslml8a6JWTEnjik/BZUD9EKBIxrga1+J9PFwbCKx5RxCvuNSO9+4hqS0lEijNN3hBMqnDUfBhyJ/QOrz2yb1NNdg+dC1LFitfDeMGT4KbODrkXp55MKMPxsNVQ6RDQsMyU7hLPrb9hZMNXpfmLBH3VbtnoT2aL22192v/t1zmInpA5DS6B5WxBndR/Ht1Um+qSnRwCq4t8KGKWIDIKoeDoEAWKoF3dvPFdBtSYRGf+dgeb4IYykyw4Dk3camHS4BjEotYdFPs7jcSs36Bn46CJ00UJx2IOp+IEykvoPhEVq8lQ/haRlaGKjHtebj9nuIW9Vj8SOwhu6wvlFQF1j6LE+e8AsQn3iffynNPxqgCw9gzR5CfW5EaJovkEcUoWoJZpn1mfDOyQFL1FllrkgsPlpyWY/feByLNDO3R8uu+7foe0ade2fKHDQ3YPUwRMhCAp7gPTlE397yBXtwr6Um5RPvctV7qgiBszwttrlhEtaT8R20WYR4nuPEGlQzuXgV932XFh3p/LUjD3HS8krVud1rmx2YjaBMpW+iZmaCsVKKiOlA3J5JKz9QKJKhua8Y8HsV4xsOFkmz9yDYBXt1ZuIa4qQexld/zlEHhx8zgW+2HAzP7TlXhrOafp68mL9+Lw2aHlWHjYl5aoCHG2Fl+uRUfu/rb1ZKSz9nO0tcn64+MOUxYiVpAwoL/G8XcNUsb/2h15KnxW5a4qqfnIE3T/dkLWxBD1dG4kPhpaiijqDbWBBjanrcU7IPvBEHjUxUUjS2ETp+0milWdI3AJsB6lwqQR8THY3SVEVbkrLMCQxN7fjsZABS3zwIz3FGlqDxKNA1kmkQRsyMQdvzPX4UNA7VDgVEcMeBgVPoagxR9G0XFvgBe+gh9Rjt0ozY/ZIwTSJUsXJdtYD9dQhXZVRyY6fwpDE4x0TZyudtnzRK+0XwWVCeZYklOr7asbYojBE2lLuD8KUX4kn9UzLhQIBgue/+vwvIaxhrLem40FhbKvA3LRh7J/Cxc6thbRLHQ1u/xvFL+o7PRAefYBHshEAVlhC8vm4MiwgZDW7JiBl7AyxjJHupletpoy6/HLoSo1Z8Of18hRAyzR+00ONZPUrUFTOmAH5AEZKLcO8snnTWt2Jm4CeQBh/hCU9pBpNi+Dq4kUVANiPs0+v4MXTe2xsLERvJOgAizeVU5rMviRgf4LADIt9ODArUByOFOfWjiXNhFlTz25LVhMBhHV3kmW8XM8HxBOur2XMdC6MNL9738j6mQfBorbp2WGRI2iuhVCtJCkWzOkYcsOL9RnX5ImPXGi3fKvpJvRdLU2NPRmhgmKy+Q/ndyAiuBYlk3xoWEWmuriwHPmB6tJ/VtjcfYzHj5/cm7pv03hD+wRh8riSC4uFdaN5ZiQ8ILO0CGwH6HdY59g3Pbo+y21Kp6gAiPQZ/nYPLOOC5eVbUln9jffmRZemOfSgo3Y+HH1z1Pqb6bugiIgegpHVvIGtpNsRhvPgsYBbhXMFrwQG7eZl9RiNfkktjDn6/jaKhWfVYXBz8qOzKjxS9E3fJunHP6PdaMvnv/bvI7nTlOa2/4EYfWmB+TI0iUy4FYPR3yY+kHtaIeiEgFdBXgK7e792qlKtRPHCYb5INQb8aGkexG7sGn86XeJHiy5/t/wEuTKUSOrhKfo9JBF0bagrwmSf0QoCa8BiBxqB4YO6fxQiMfqJwJd+vGbjB4VmcONzr0Idz9pHtJYsGGzvMx47W3ehQGxVeuq8oRXZY62bkJz/EcJ021KiWu+62f9VYQDW1Dy7idyBRt5tjDSxge7CTxZ/3jv7A7/dAG3hBrLvPygT2BOm030DDef/B8Mu5vGTIa9fVJQFs3uUTVQoZWgdwNVX1QwHoQXk/TZlwSL706N/Fdon+IGVe6l0Yp4P/o/2NIJgEkDg6AUvtNdzXUtkGFNM6RS86gTvYg+Gc4RdFUFbR5RfCxfoastPCgobIfHU4tWfdRHbLq2H7I3LmQnUKvqPUD/ayCJsHaczNj+OeQVV9GAT0JSMRT4DHHg9GiZ3+lrNI0Vqikb/jHiTs1PWYmXPwAwHGfrAl5XOvo2mYlIr9BEmUJOqYnOoqNFEt+I4IOtW1P3ZKIFVnEkUgKRNUcUSvDIyCEL6O883cAPUySM2i78xo5MzkJ/eVn/M54hFmbFw0qFizTmp9OQwvvV9Y8DTjh58WH2dwfNuBMIOsfkXKNgoODQKUxKOBriJcX2lVoVR3eKHMUmdTbHVHIq4L2XPkLfrcHlehD0cH2XgVJOq/Y62lH+UDPG+5h3vuaRNNJ9hLBNIzgYHPXdIuQ0MENqUbsy+v3knZDB33eockjLVUjr6KAHSM2vHMFhVQn7g2r+qGc5cDjap31eC3BDdSA9GEti53/vJcNINf/MpGE8pT1IxUdIYa4uXQrn15W6GILhHsr2cBGj6risPPJKjLgmznXvPR25juYsIQ7sfVPsXxDIKLNETbKy4vBp3PThBLPnQ5P1XoVhrd3VPBCC14nZbUYpKhdPmoAOGRmhOhAfs2l+BdEgf3ejRihPrYHC1P2CvHyeVNsLvN41E+LKnMBgY3Fkvo1vTW7h/0l9Um0D5x9DbzBjFv+yeNOvHSF4Wf55sDb5qUzm84ze6TeS3mNA316nYHVlFVqRDfm9WJyjHeXEU9fcrrZ4vhkRXzEnS18LNDBhadmLov27xZYQSd6GNrDNI98DNw88zev62532hnEbOrZIl9Cnuu003/Sovds/UbuMm8lp0JRQO9Xqk2vPmTKbmiqJpSfPrq53Zy04L73J2DGs3dW1ABbUdky4merBk9iztPelVZQKfUzq/AN2r83cimOWmBFqNS4yamMZUl6WBBGw+bRYQ1kbh4ClidBb9spXSw0WWcKa07uCxvwKNnlgSeIsSa3kpBzbAtPaPJgypQMZNQ9wN6PhJVPyRewlnf3RWmUgc3cU+mLRcQ4TWpZGWl32cb+OHegxxT1w2W849xzBAdlAmjixaEFd0xX2SoPWOAjulZ84w2w/uLZspXoGhP75MDAv/Pm3p2HyP2Ki4KoBdwqR+NLKHWDGAzVsqh8mElUCJdQp62EAoHbv05L7U+JfLxoZKAtZ8ipf67rdIssxcAuZeCitb9qZxu238MDNDaTmTVVKphJFsXwsRo4LPsYeGD1jRPn40kvkeOpiFE5PnBVyiUFCnesoh6KmpOUgYptvqaHMxArh/M/P67Ep/rumgC7O2M9eINGaZvU9ys8jm+ifCHuzb1EYJs4Sd1QsKvFpYm5gAOi5M0DEkM3j8zdE6M8HKOk//fuRC8seTyWPgmShpas5yhgTlOu11qw20Ck5Cf+U2bMfu8kQi8DHLKnJUhW1FQ6xIpgTiVZ+q816Sgz1meObP8OVNwhYaU+37x1tK4ktuCH5MAN8xPy6Tx//YRlvuDKxotxhukgkDHuyconsxEaxtyWQtF9VTEZ0UkRY+PLUjb4zPrlQQoo5Elvw4FnV2J+Q9gUpoEb+LObQc+XsVEe5Lsd+Zo4Se68IdGmtYYlXV+Y1Npe7em3RQFDXvfOqim29+e0zL0x+PvRjoF/kT5FVYLKUJckLndER67AQO/N0n3n/bGUA99M0e/wO/Kfh0Pj6LSi0IOIRV+q0CZiPNTejwVblwm/WXleRbgzC6iBBTM6qJpqdjF96V8JavYKNTrR5gbK1I8vxVXk1LbwmAaOV8Ryboi+aqx5uu52WYCgNQzJU4CNt36KScWUnvNGIj6TTANVNqqi1sMc0XnkhR32ItVdkQciV62MeJFz6t1k/Kl1iOOBGiDGkpBqoqY6hL4XDBaFvtQlVhi6ze94hTKPWGIjayEkxemXBjVHgQ9Z5rdSfkVJDH/OebFtoFUFb+r/pvdA0+tdmY+54OcIUcyGS2ENWaGw16wGqaTmR+IH9kbIaJFrQ3RQ+QyxDY4/N/xLejFsot0ovAQZPvU+mzL9h0D0nVeYQe8dojlr04TixAD+HO/mNweH+PZ4i2gMlQVDi7vUaptncv+aQSUS8S3p4VpMaMKetrpnDmVPhFNoSIO+W7kvuz2w4oSApLy0q6CHJXDNaYuy15mgkJqSK/9MFvcOMwhoFbn9UtdtI4MgAbozI/AjDyClRsWoSy/Ybx6Q61N3g9JhJbzmkwxG4QIZ5iXQzlFFXp8m/J8xCfhrfI2YCTtiScbNQMSQHOqozx/gs2GuvDr/5u0A73JoHTsh71GBTt5NwRXfoRT70w8gcZF3t8Z2reWMaaeTMav+NJFtuXmNxjY7zBc8NgTzid1gAxHlvwGQMyzjL7fL2zG6/ql8bgHPRBqiR20PGz6HTKS8PJc63Qp8RBP94Q8E1CdyyvenLx4l5WJY+S2GQp4vTuyc5njsM3ogCrHLyFlLX8y9BqDjy9pMXBIW+FiKMsRwJQU2ttTDr5iUvZiO1Eh7VXY853GPEC+AwWQSSnFY2e7KXSYO7lu9L2HP1fLN76SGIQZjOSHtWODgygf20Wg1QJRW/tO/O5VzroNv8BfEHMMdZaafgyz/KiX/wG12t13Q11zZnE0pi4Ebi1tojzEcm4HidVdtjx7rHccR7BUNQERJRZ170f4ZxKIQJEG437kYocDQlHrpVNOzS4M8LuhJ/mjDeL17lNZhdYvVSVWTsV3RIF78bit9FBgmdrGo8XOhxE2zuCeEQuSEbR9mJic57kJMOLwZyKrrlDpd3pi8O0KRIaDRVh96G27AZyv7+23gcGuVKCzCrS11s8epCUkNhj3Xdw6YPzxBQZaZDwn4F9A81hH0bQygjkIqln9dXgrY7rl/oBk92NjShBcmDruIw/+j844/W+XbJ/hzjKkhGS83vS9RPsM0cA95ShtYKaOZKQNBgruSSYaan8A5fbXA3s7Jv0mO8gDFsmZja5LlJqP/cO5vf+6A7hnQcleKR9lXFG0d4NiSrrQ5ynDn/ucqWG6dFf/URMX/la7K+fy0+rKsRJYOh12bxPq1uLwgwWLZO1LgG8K7Uz53H3CspufODdRCoQmqy4PomTgq2tXO04FA+5YpL4z1J+eSO38DQn4XYjmOCzlnCG027QWJT5gQ7DScBZ+p9FgwbXrn9QeNmQWd2fRwEM9hOsl0bcgGgiODwP167fQ0h7H9jz+dBs6q01KwIPddMxagbax6Z+9dbSIWHjCEj3MLXpuEdi3rbCDiyS+kLVSh1R+vbUPIRRiTQ+W4wqBp3ifZqczzkIY54STbzU8V2Ou2A6lJ7LWQAVGhSoCj6t3qLqsyoeMRgPKbj3K5MQ0cCqXqefA6ndPshoEf6Xy/7Zy3keA+5o1OKAZNsgrSLUtgeMsPV67582a4KxDAiV/6QjnJYXHe8aHhPvVq0uS2RXOS9bgx3681n0272IBy29UDRo5RkQWutbbk8w1peB9EiICcRh7FttDpxIaXKwrPA+ykqnf4rHxk3bo7p6Hf7Y6H3F9uCbAm4ppPXCYo3eGVMIkPFdJuFsKJIMKhPfiu47WEo5Ejc+oN6CzQPt9w1kojq53HH6ZEdweNACCPWa28cTJbKLbDPL39gqFAx82TjiIz4HA7UScqyIZBpcdlkwXfCsu0lMnnxIRHR0QXwhnoObmQIIP3Y8bd3YfXdWyGBGfesA0l6gUK0Kamn7+gA9+tpnk+d8o2fBRVVkexP+/8nRbdOxsovpxEPZaajooYr0Mo9/Daem7X+0Q9q0wL1cCNG6I1tolQNod4orzI5OAcDgJSc7/nymRVN/DcMegH5U8s6yFaITmsW9SZrko9+u5eP0vs+oUNpw0OL/ZtAV1h/bN3CAAp60FaH6p2zAIrNGtM2H4u6j9eAHZqAa+lnz2rCxSBjx6NN+N8/6GldvOrjoQsqN6hjRWbZohjyEgQQCLX7cxoM+ucW6OaT/N9Yi4g2WduSZCP65aDKUU/6wMK9T5AED9yx1rArOFfL3kcBYe6bAxdkcFiyZlhBwpY55Vrcu5rduY+DlMqXxE1aLfuD9o6LUTunaTF2wEYNMRQtmVSMUD0o/7SBSZ6hHsXgW9A8VNYdSms2RDvDCc+fv67k5LOwzuGp2ad4R1M0lQE2u8+L9/7QL4BFrXDFJdBDjcnUaNvmOh25v/9fHiNyq2EgpN1JhFMmt+zrQBgqjD31sOKxd4sSR0S0LNN8yp3BX3RFCzL30FFdAKHGa7lZFSlLX4Mnwre1R6JK4ml2XFUZCbWrVXNhjlXBOtxYqx1RXkQf5b8UFJ2gOVY19XssJ4ixhVdk09Res4UKxlJu8iwTV+TGAMR/A9VdATPihi2y2ouSxjqhR+nMO7P+sNSWc92NL0u/W7trm2QRVgzGuqXoJ9xxSYDfo8TpGy+uMB5JddGSIwpeeAc0/HNFnHorodUykmqhTgl9WxBNRGSuymqjVZKnZoi5m3zaf1OfFS7+/SaSGGWr8HBj7Y+0hJsZd1cGD9SsRXPrXIRHwAQ37mumasJVx6vD42VMrqyV7d9vk2PzGLFkZE7hi6T+/3jGMoZGilUNKRs3ncLnD4/2N7X57loeZqGgJB/lfvnxxbIdLuzCxqU3+ZfNgxE5i7lczDE5Wih3BHByKwYl1hh1szEqx/0hFwxlSDHnBlvn78NSSq57sM8OK3Qzfjm9ijZ16X8wUIOv/GRo5o6uttDeUIq2pn/bo9OgsI234kDmRwP//2Ez58NGmZ5Y2gKAdajBxq2AEaxvrHhL65aDoBhXTHHl3T/NQIzePbyewjijDycdUV5DDlEHTWM9MP3rELPFQ3hbMK5ekslmQq9nvwD3zFAersCB98WYkb6/PB7QkRhwit9ttKSHpcHY6rCDpWwRPzexUIARKJnT4HL9w1Tq3XX8z2owNrJTh7kc03hVtBgrsolA5/7Ca3DRaoXYEp2CustkkKBWv7sYJmFIuy7HQxklYX3QpbRY+X6Oynoq+t5xj9Y1UHh8HHPbD9DIDDlFSpuwBa2vXTCZSzVBvC87X62AJ/ytEH3nRoHCTyn1YlG6JqyN8Hweky8RFUxkzAS9P0fb/xOvhCihVN9eQ0HFqvk6JRaFFD4WMavTK/MbzodM1E9kzDtBnLxdgQA5fUZfT4JWiuA/0YzTRJx0SIxeDrZS8j359OBAuFt5hML5SQkr4znIcAhcfHomkJ/JFVD+zkN+CmX+tSBLszeSJDNsDt2ANG30t3KkzlvxQx1ptH/b7ahTFsjh+R8H8DaB827rkReJdiLKrjDpjpiES24ud18m4+tAMePIoLbAmBQj4EyhYrIw9LaxtscxODHQxk3gC81yywLvsD30irJZoqUUivddPPTz8q4A0BT2NMxV3fin8MWItoi1D3/zNKNL8G+M9K2d1O0TiWo+PaYuYuGY/w7mmR9ivb/d3TskJEnNJ7Kiv7FWLahJ8/An1oIVM+K6Jba+Uu6s+cXljE9oH3S52NeV9GPCPC8PhebPFOs8C+pwsqppkAseU79+3Vk/L+cRFDuGfiIud3xZJHAr8NMg4whP5gEQIPM52TaXWWVE+hljXqXpyL8aRlYACn9dP9n6GaxpjexuKWP3SlVSo5jM8LB9IqjFWIagIX5s+MwlJkBZvWJmF1tgmNtlRStMb8QajjjIfb/3Lf9NrP4mekH46lloej9vBGPwUg3dTuh3UGUyt5fZYZ3lJ/rSE9Z1HVUyyIf6WtepmkgnZyKuSKAM52CoZ3Gnf1Y27VaOwgVUCeuoDEMu+QrG/u/IG02lDY7K3Vyu/t5Ga6NKZIplfm0IijqBj4lVOC5HxxQCagYBleP2Tab0hpI4HAp0d0xvczGxR8mqMWUAVsoeAJ4cgRkl2bKpqpE9IAWv3E6PyPYoPBUs8kR5UXtxP1ga5Dt+ZACOVehn/+D0gQ6jKNE44JTNiTpE+21t1LrVEkkF6XO6MqEzI5KgRCt83HyxJJbcNpE4ji3GdE+JNUotGEACekwHPjtPqbicqtEU50uKLTHuPxqECX+LHaId66QbPoQ2HhM/Vu12HPnmOXv90mldGBa1zWMRC+5cRClGX9nX3eFXFHP3Mx/D9BSb3Eme/YxkLn0gJuUJ7Tpkn4+CxSaZhy6lh8U8l2zil1U9Y5VOOGNtv4OdbX8KxKsSQ7sARF8sWnaec87XXExjcWzA+b00/30e3nmyqiKVloKG85rHGI7xDMMkG05JrBEZqwauRwEPy8eN6SeRP4gTSfCKupKmJ8AA1RFyGi+H6xvkgGJycYm4H06wgdiWRP+/1/Skx9tmbFRXN5S8Hq1R+Dp/EfReex2yAURNEPYkFvSwym9w47eu+Y9vUhlqIoimKb92buPTeY4faFpqedqWq12HwCSLzOXY9PyMObkn/MNz0zhYNeJnsskrMUt/JmN0qJoxv9IdvGbw99aoJR6frPzTR+/G0f1wx+zNtTTLna4jJngAdNrVtfVwwNvq0wGRZ3nkgWe4pS1XpYxGP1rMZ9ogl3KA1lym00GXWcr2hBalXBkeuCQ64QIXDe5RvFZsH7LIwYkmqpnQt2C5fvrdlntJ+z7c8ms0/GZEQUZpDb7a2qgBMliUqrulozfu1qHU92Imk2DkUnuiyz+rRkn3VbyOUoIUdZz529zLHB5gPhbcnC13cI45aTc5lypf84ZCbzokpiRzp7VfFBrppAVZWa6v23yMaklz0iXq8k028E7r/MIzwno0L255B1zuLybTiQmDuhou9n+XnYws140Am6Wcbd6vNEVYXoehoPI9JaDha5e4sUnBIlJqKuuN/U812/HoHjLPRrof5C34Vzi6xn6fsYCXIGwo40wyE1m43ozHxdwHPQHfgDuhqU899wPp21ES49P/HR/BoLPm1Uj3MumukuMmKv5WxHjpsa9GNqtpZMvjwTP49ycCGnFTAscqmo9i3Gr2/AhCqT6ll4rd+80UfNF/j5QvtaJEPRmGK1WOAYYXO8LYYOR7QIeV9oRVeFYoHF/KzGj+QyWHrB6SoljiHrpbUTsJ3mw9UwhtoN91txITw2fTAoH6tGbis2fxhS5v9nKsDGX6g8ItiSQiKZ8TKg3+s1gzgtE7RdJfNgS4lPz7Zn3LuEv5llats6iZncS444Njy/02HIbXHppbI9YH2gjz1tmPNREkc6nKwC0kUJ1N6JU895uwpJO8X2xq+hm2TKR8c183oAs1U6fu0t1YTqCQGjZKPGH/MwTr9m+WKNcuQoJxRj/G1kgLuuUjDAuU062tZ1g8ozGvrWY+2cOq/PtB/qiOnLPhu7HC+njVIFv49bWUK8m4ZbGSNcWf0BDJeYzYxrHMyMoB96/5Y2C41PyNvC6XRK6koeIoKCi7NKLOODj8IISGX93U3cJBbWswr+sYlofSb4EhL8zktcOz0xuot+CRXXTIG2VngF/D5kntqYa5R+JGoaHzz7lS8seoScy1hH9fdtpYOlCFEA7SRMptMNUu6b7SI4jLrl2/8YDp4dF4cJqR+O2rnH6n0Zmp7fDA3+2mr/mA3I/ji1R0vp+mwj4wvSDjRbU+VhNC7fVreAJGJPyHCjDsP0F/JMwbBPfNHlQWfbuSr8J5vprRnKkWZ1AP3X7mgSLI7PD8BYkcZ2oSk+vFm8gb7tqD2/AzoR+SbkK27AAoScVf9VvewqT2HEy44IAwHhcdM9RJhy/ft/XFMoIeyJICpTN3zfHi1e+juXHyoV1yCrQ4pWSTc3HwuTtlNY0NrKGT2PBxHDzK8JGA96hTIejCsJcr5OAyKYnbzmm1iGQ8X8PyL/d2vQ8PiUPuNv6v5WKIDy3BcVRJkdTQB1ypgxl7hcERig0sAAtoHOKc9stBQobklT698h+CI0PewWaZ7zUHaRIB5Rf49gJdMYlAqD6xdDxmXXgZacXi8jo5x8rgQeMl1qbSkP4b8ysDl0LajmWpA6P8LQJSrtqNWOIG/u7Ig4jpLa/2dpJNC9h4P0LgbaGWjzM0FSxoQV2V/bUgJ2ZDvhJhy4/AIzN4SPtOBPCFLpIBk6JvdTrAolfqlOMjZRPsfixjmpcYTxaW69a+yTthlnwTxnivAMO/iM1d4JI2bl8iuupGXZqxSDMhRV04daJzIoOuf55QIqkDCvXCAn5oJiQK/nZregbqYEi+DdHyLfbyzBtgZbyGdeP2tCWFhNsZoKCtz3LcboB0enz32WqeuGVB6muWDZ+t2xtzfZdasal61L8DdLh7JUl5IH54pXn99l8Ge0aIapnnG3cwQNoCk9eCzgfqTvOrgDTE81zYwmlxLdIjAoQiDMF+ep+06xQAEwAKm60/a+h8ozu/HyFXAGWfutaP2z1GCdNd86K8nUPR/NGP+XE90ss+yYzFyAMXKD0lYvSno36fIjqBb8FGHMsEV+XbzCYxcd+9wEP1jZtY5geY8msQUGj2BH3x1nWwhXgZxSOsZqHDl/Xm2baoVzOq/fm/9/z6Wm8PH1WnreKqf/59dLprUdZSAMeCR79AU7mPSrY4tOELZ8iZgkx2E7svjZQCAz/NlUFGKjuByEBkX6RDBYAPZBK0W4Tpnq006pUMUWb7NrNLRJGjda9CphMhM80g0tVsBODing7QntXc3GXRzKQQeQrps8dYFIgw3M154tSoW58SXEd/S3deL7WN4VoZfj+PhKakrKgCqF4Y8uOLaHYK+NKF3HOn/IZHu8JoMkmRGqHKV3lDs+mvixUz8Ijgq4Gp/EwZ+HKUR23B3lAJRyJcWnD5Bs3J1cqalc/RUH9gmJnzvK9JFtBfqxMXVoCjKFJd3mbb83HNH5wfrDUB2YUuCpjULpcakDobcXgIAnfLQRdcn/j2ItWdlYN+069WX+7muGuvxNCtz4ZD8+5INjU8VGyVhKCewPi8UmLK8gAkfKxdwJCyS0cqwmnTOvU56lzOs7IUARLxvglE+RDisJR5/nI/CGSX1/6FlmHwMsAn+spNRMsPgyU/m5Hg6dau07Sf3KzVFAPgDBVtUbycLvsKAtzqa6m5j0p2vw4NN/tp5Kq7xIj+1o2i9LqxT8GjpWag/PqHRflrsS5pYhtw8JNL8b5hKW3QXRyjMYDCgj1OXvAiUI3fjSbZA/DaWUAvbcR/bUOig7ftmF+iI6eqBMpDz2XtT0en201vNrXioLuw35vfzOuAVT/IRiJCX/bqPqn6RSGfi6SVo2Cms7Pzbe0Uid0A8WdUbjwZ3Wg54gvr64PWkbsAfyoLuChYDax4J+uyZTwlRkGFsvY+DyTdDcOtaozQOokqIyhejvSrKI6hxwyWT1ZRc5D1l7/vqi9ZLyQ3+1ZCSMQ73Zc20iXqf2LztkKp2N5rhSUYPDpF/EER/D8hgTwofW0QWG+nyYJJ44HoWVUr5V7ecXH99dE74Z7XfQQF+7SbY9Albb9FB705e9Cmpk5FDMQsOU6DXV8DhqV+Jkywu3TqfPRoGZnV3oguUuQgylYL74TIJbeBPwZGSR02ty6czG3IdThn1juu1Dz3mlwVPvkc+UGLWVqPaSrGf4EZo/frfR+4ktoIzqVHyJG1EbfardUzlO2VDkph4Hcm1iRpsjgb+EUA5PC/zSUubL7++UEcnu9s5IehOzy4glA2iTM4bdoq6T5rNPXCv/aKw+dJCk2DBFheWivXwO04txTXy/aj5m47IQ7emCf1/K/e6iJ0GewIMYVo9uwyqULZgvUR9uY+6XDTBBHTZQQDCIgAHG4yUVYUlij2dA24VUL52RW3a4lz11e6k9xAmIjJPs7p3j4VudlP98Hjh/6Y/NCP+AnARS8DrbI7Zd8bu0rxw0GA13orVGcWRbo4Z+BBVxEoO69DriMKkEl6n0NsXgPhchUqWv5WDaI7gfZlCV40++hgJZNa2eFgwjDgcYJ+CaDQ1z8XkLSehDb8DId7JuqjqcbHxEoj/ryx4KrAu+kMDKZLCgPEJaZvStaTNa0mNSMH+PfoIQDCIhIVOmBxOg4XMPWHmP4c8JUHXGmnrdzGts8r0Hyx622IGTl+IQlNL5hkvMS6KwYleAuDA0IwvhUfaoqdCCcK7Jr+3zEiN723vHUg7Ehw7NZAvE6AC3oIfZW4cC6iU2HtI5Aqt8J8gq92qFzdx/17uWZnaTMXFX31f+ZEkPCEymT5zFYObOWtPSoX0ATqpS09e/4Rji0ACZFZR8/F2StxgdPSKJ3qftMxXLxkV7FBSqWU7QbEjoBqfxWV/2GgjCguXMXeasXrNUIvh1XxacLYjJqfPHTM7VVqOPIh+qNC7cgt4M/CVgPAV7V4HtUU1KsR6bm3xyYVG0vsj8kXS/7nXJLqGcRF3nHc+NMP8Sn2foYPrBvTpeBwU2USUdiQ95llFxXNIa+qXXb7QcF8bvx9Nb+GP3Hh1GJfr2DVOCMsl/y0mzmVDkI3lhvccUOG4pzrU4pQ5rH9BF86B/gAv+bmGyKZgIYhscjPdZlOu4WVcngxiyUvB+eDtEwPDS66glrrt4UOvyWToyuD1aPE1VfNv0ieWeFbUfe1fFEUnY9wwrphqOU0oyzkjMNkiiTlYR0Ji3TgPvD1iM72uqVdLj68Hksjmc2pvxXLTLmrer2VgY5L1fAQRgtnCG3RlgfdexcTvwu9PhNrGGfHLKs9encJ2TO94z2f4n9uJ+lRCtMCgaOkKUbO3/jWwTGegdaATTwlvqFqfxC2GdoXRNlO5FYaLvH7Kcbry3Wot/sW5YR3MIeUBqbbskWuHHkSevXmLumQ8WTkhoFqDSB198Po+VMd2OtJsAlFbvxu4kj27I4LckKjL69DQrfKM5SfnMbfslpXyhiVuTr8i5YDMLkUwiFqjCEhYLLXPn+n6a5140YkO8Nv6Tmogkm5O0xNuxxfsBNYflS9ku9hVcC0Rgk0T94maPDORv4RJDRmIdQi3QnupvcMgcVrZiZAkgW4SBjvxaeKKnKzvtk8Qd9dffdnnVyFHI0S8S0WkSMsaueuhprxfrmiT2zMEFl2SoOamjAKtBqVDiaqmQs5lAF4H4TQmepW0RW0Mxi9Lbim65TY0QwYjPASWakTUiUDvo54B6X0+hdwG+cdyViYMJSalvlKJESWNcH74CPhV2EAwbEnBuFwJ7ivFW24cYWH7FXTVhwZPG6VFOFodnxAq8hnuKS2nxgP1I00I+p8wdX1gKd/pYnJxD1bcCYbN67s7K8NmP5c0PT6WPXGF6fCYRZPVpS3NlUaH7T8kNW8yMsKvSdrsExArhMj3Ubek42aG3q87dsQTn4VS5D4GyXstVO48R58m0P4EwQye2O7f9fIsxy2zYwD3fDFbwLmhypi0m3J4z/H2RPhXon900l/NqP8jDboILcwo7U4MD/AUqIrhg7kaCBAj7n5NwODKLKZfI0Ea4T08UIoJv/5XXsquPBNJpDFAX6ePCqYpKKq6hnmuBsU3op+vURmoIRECgWwt1zP91AaigbKb98pJBjUaCeCNb57WVlvg14W2izt0jW0LBAcKJIsRBZfQ5koIqQjjSm8Of/BnCfvmXpWgE+NWaCKklj/SxQkcB0lIjeED9mK36IzqDiaKDAY5Mv0JmvpX/t5a2Zp6uF+t0T5HHoq95vuSrkIjghpeBgWleiio5WwqExlzYNto6KhUq9h65snzKUpU+5Z+Th7YM6QM04eWLMIDhq+p1NxNbWXK3VNb6nI3k4nRgFsQwoa8BEvKmo+0ucq4kYbqb6KzGC1YWEK4NXwfNV4pHRrsxUjfY2LS5prknSwkhy6ad1TfN921VEdm4a1vv2+fSYa2MQO7ngSyR2Lvr5RKrUU20DfBau2/wQ5hVLhQiQRKkpiYkNyUTEcQmgq08fm6b1AWk+KChNSfcoQNfXf2JR4p8hKLBQpWLBG2yuUETKocQSgnt5erDey9qN+QO8yLQxAM2Zrqa2RPQRdltBlxBkLF0824Omxa+IEUfcLW3H28xb96uZpzq81PWBOVVOHlgSICSnlvKVLCdx+7gdiwqKkepn+td1TVN9stMEmWdb0iJ5MhXw9/dR4g95oTEfUE3CEViPRnzjHhalgEzU+s4szns5eSvi/bQNZMdInjdh4erb2Dw96lGiuAFG1w5WXCw9sD8ynBGjZQt032Nh4smx2a64g5Yq8jQoBHm8HOQXWumIXw7LWquzU8xxkpvztO8iHQeom7udATqC/kKtxScKVKJGRReHDvcCd/8CJXReT7ibj/DcekKYcnQHp94L+GP/iQBaJ8WKH8VsyfnD8tHjRdVnpK6M5XUAZeWCVq5NAh12Oglvcg/LI+Rpl0CaQSBbOLhkwiSg439dqu5wUT7uWwwxoYUv8uzsSgUg1ShwpUklrziGxrrfZps0Bvme3H5bFFbQ+MgRZNgXME19TlB1SKENcG5I5WTcmfTAmQ+0PvEXWvZSppvskJBwBa10UVqcNeh2o34ipJYfgEFj3Yf4zxZK6Q0OJGlTvraGKOw9PfmJ+IAhdBu99p5fa6thh48XthWeTzxaciPfcWA6YmDDSpnPx5V9zf888XDb6iQP5/xFx4flFr6H08A5cCJ8WMxDUZzNjYw5aJtJnv7h2puDxPt4fSCw3erTcTx1sUZxb55dQqhmagD5MDlrbPW/bO81HOaCdLo9fws0hVNUPa4RPNDrZJeLST0q2d7cVqYT2XHqui8ToYqpkBkm1h8qqax+iWZ1QUeSoTSHLCXAdxaFvr0Y7x55s2Y+ilmSdpkgHnXsKmIP1oFqhBAPyVJN+HkYSqOcZIlWFUmBcCPud2n+jgcR3ol2r30dwNqK6IQXNAFfkcLZeNghodfti2fYa9o/g7mK2hhGhXh5T8BoYlDJaLmX3G6Ur2nX9EaVhjWHNkgYsnigafgpFt92NdTtUMK3mJmmykTgpTxEqUSwMfbkUwK95Ey16TKI6+fxd96kxqGV5k8o5PWniee4RT43Ul5f79y1/hUh12b5oIYp2p5yXlU0mNtmUHwDxB/HMKrhk0JO264l8XH4IrkAMT4coIPfEoLlV81pugweLHIN+kMBUkQnIRIeFlc8JHTAbsoRGViU08UckUfXg4YZdHGEk1I/J8v2IJcUBHfIS2w2ch/qe4kZ9kFqk/4jX8HBd/wzkAWLf1DmQDI3zp++QSNNR9aVqqhXO7D6+g+nNOXr3xzIPkp1ag2i8YUjaOzc/fSSB4A/CaW4u8IBCPQ6xDvm8LiY12ymWn5WkKgsns8iUs9PUE8qPDQ8WvbknPRx6yglA88mgm/9Wa41ycRQza4Vp9b+vADiTDg8/jXvuMCLPn5CN+gEfkvTED7kyNMyNVj/SJX8wE/EaaaxQIUC1FDc8CD4uM8TVyCyP65q98zKo3sKnhAUEURXns7G1tqh32ZDOuxZ+lSlpe5tMTvZyDjh3CRZlJlNR9RT3yaH/GlsIbZ8P0lHLBRNWP46P46YDupxHUbuWm6XzO0AiTd3odp5ZRiY7p0jI26Z6HQWYhmk3AUixgKsluLfPwRg383lPbyzMwet5CjA7CHlNxTJQRKPqga3kbST0MfEu+1o+43jRywbfoMPPJFLyaNarFTp3k4whvCf8Z0UEA+/5Cx5vsSIPcCdQwV9L52Zpf7LJIKiEd6ruDpbD00ZWOUC0GJSoJOUi60oMNkmkP5kWLs0T2UHl7X22nO5+Wmw4Yj/uRXR/VVH2IIw+k240xz1dSPgyiBb/1r6hlPYIQKW6Nm1ZPy7++glNTMCrehz70yTU1Tf6qBQVpSmB7KODjoGuaX3otF6F3ajK9O5bofkkDf9BOhExBwxN2pSngRCZm8ZoH/Vi/dmYP2oWio8bELuy3QbP781rq7ca/DF5sV+qidRF7UvaqS23GLBxQUhlquYeBqVjmJpe+iTV/RFfyst4mtf0XSBXdicegHGVJN5fDyzg9crus6/OUaKOnw5YHwC84goFxK7BS1SgsLHXQp6lo1UfizS/mjTyaaOvTy5vyk+1DJuKKyXRjUX5PO0PhrTNyH3F/U8SbnU2b0zF98ejWG4Rpse0mbhQ7+3gbAFNNTkvRRjI1Qar6/OOe39LWmLJU/b/a+gDlilzX8EAbbTJOzofVUYJ9va82wsbng2kg/aG+Dmtjp2BwL+sNg7hIfwf+tWvT9I6Joam3nXEKpKaQVUUhfNvafVu8Ah5WM6FO4ESXyV9dJEeJxjv1/TQjebEVvd7iERk4RleyPvd4nsETwg5HhejqDDyXT/4x0ejqBvpFv0nWBMHvAi9OlwmRU1LuXK+ZN1+4/4v8FlmD+teZ+0huOef9qKfvUkcLH1qLY8oVfC8D8gJXBI9IfN4UuLa/mWSbzLO6PyWNMvAs62O8IzK6t4fEXApVkfxHcOVN2vjMDYqjXBfVGIoruT6Ff2q19E+L37RkbFKOGjhIWhKAYiWyVeRtW+ChPsfbDUpvjHHPaFj7/11kS+WqIGH+V3mf7FJirkVWHOm6YPzyPJhTJoqBO1j1vs/ohSkK5yDlrymN6C+X1qzuOeHOHjsBnZ7LmIHm9IAx09x6zPMKI5KxsvMlic/DbqNrG+aC87IB2//uiU61ozKDhMdtUPus24bPDcyTgHDRIV+XCA55ogRiKTEHZpWrldj4MwOVYpRh22ViOFg+0FtCY3wKApbQB5uCJHiKFpSoNQjcEerroEe1KMag+Y7jlCX1P8vyF+SZhOvl2/QzXpGCx5RwcTeTdnenDeDy89TIAh+NBWK4Xga+y3aUJkp3sH267vHlEYTOxvzY0muYTs+lAfKNDFAaHsDXjz2oC0d3h8OhVQZm56AQYeDLiOkN0A0xAaq3kkQVTPhcQZ1fdHG3Bh0jCOqWqMBPLxdVmeS8/hWHZy2GdkcK1lIX0FvGL3oJFTtD1hWCshRziSe+YOdDASdWqXR9cYVMDCmcyASGZCt6yQrljQcIYWJXG7idM02ZOEssdP0DEsn1/054g2AZlGQ+cnZOTulVcThZLRawUd+qndyXM5FTxoodypx7Nl0g2kL0M3AR+0UHF92EusBs6QO+aYJDjt1q+EWqfc7mftVsqrRTXjxQU0VVgcUNzVN6xkSV+/UWOFQqeqtqomqtHj67YA6YtDiWFk/gtj2mDL2YDh2QuxrEXtoLxicypqfYl7d0rNToA/b7Jtqbom/LDp26DxChkozQLTuWRVxscWHI7XwD7Eu/Awu0mnytzANMAfwxcO1SeggRlWs8ORDCKbRO+PmZmkKDcq/BkiL+URnOM2niFVGQPjEwve8ELdUTmt5qfH5mxUvIyczycqP7jlNehsCfEfIffLCwnRSuB5lzKpCgL9gkQwaQMsCPtiaZ3foCfg67sOGbqDzVF+eV0IgcTC5N7+OlpKswIKtsI1zaJ4XBOf1YDbtrVToCWFhe8veduvpevnP/65n7tGu0EvitqkBVgVg7591D7KTWlBwK+3DL+IlTii+SkRJC/TUivyu/2mT/pPEaqQ/0OaAEsfanPxIW4jLcr2WNwjmzYZ2zHkF7F0HCAfEXPuI8z5X/Ghk5QFTxsvLxsHEveBTtjSGpCF44R4C1Z4Glf7TJYKz5OEiSzj+oN++++dpR+/HpNg+k+w3WBF0VApwSBmJXjMVjvK41zwyw1r7XPiwpFwDmwR8fSTDXPTb/i+7jYQti3AzZP0aW01zo4SiHhlm+c56ReJ1QlpVY6ahrafmQj5+CA6qxyYZzaPppEOaTr+5H8G45S8A0u+/c9qkJm5ueh84CLbKxUY55XtLC04pRq31zSrpZFjNrZpbF/7cTxS80XYTnpsUHBUD07frk8tU1Ngj+h25du5rO81epThHBUCu+zIXkmAsa4HiwM8WIE8XJzfWH7ylG9qBlIW5AYi8miz3TIEOe0dyrNV/5Rx+ak31Zb4c/Go8wQL14w8etZQ8nvU/Ij8cnEvDM5gPssFE0HxjdUZY2bDhqfp2UvT7ftuowvRKNERTsJvnBWNnT5ZSAt+B8yzjN2o8iXziyr2jhipispC+sXOlwe4ZJ9DMS74PA4IOYl/stKIXxb/gztaoorZaSnH89vvzw55UiFqmk6BQ7Jb0eb/8fhd6Kmyj8Gr+7Ml52q+yDApdUkHyrq/Z2ROCMcG17IPr/45uWGFq6SEYgReHeLkXpTIYX5k82nhy12KIlri+A/nlu99diocV6S9hBg0btX1HD11kDNZY6pWPncVGsSom/xdOtyd78yv/41SPXtfiE7oFRVD7xEUu+rGzY5jdJEUcUUo37xiT+INh5IRpI9h0BraOTHpI8BBv0+yhlABHSCDLiSfQYzvVIR1YjCxmF6OJngmWRJpoy4nwRzd8qkVwob3sxdycqztqh6Z79qjJr65MtLUop+xdObfFxmG9yM26COCNG5MIssUc1MNYYDPrpv8KZYFCjXwy3H/tv97FA5maQwMar/tGnrasflS9uHy1L8BX/HgilBR1WpjzA4R61VSMoTwV4N3nx/8eMWefAyIVww5g+o++33/3wf45R1MbH5/okwK7pj96dx9SJ+W35Qz45s1+OVT3x1Lhmax8MCZ8zEuLnAVP8AQ4xKmMDq9sfqA8hCG1ggGB2RdBFsogytbyEnjJlgWOqool3cnpePgXWjPSnOFsX/bcHr+G78Mpt+bDGXoXQ62e0KeYlc0ZAx+hj6kVoLK8rmTAiiW55rhPjfV8U7oc7KDij1FPC48bOCE++L+sm6xg66jxpEvg96YfNJTXTEUwowSiLibGemBGoVjCA2igjAmIjx8RtYocURQNRPu0FZLPuUmpDRqRr0jQvV54zJ2V3XVezlS6UTwrQQ2FsOh8fIZZ0xMtB0zkJgdmYA0UOTPy9Vf/FYsj7dDOfltDhoFH1oMjQTmwQ7G+QbZnzF4vWB6BPmy+yzKhdAQ2zbXDAGZ5qqx81EE5MHCofu5JIyFUcv2w9h1wIH45CV/k9750g4UbKGgsmiLN/sjub829nZYrsgWbXtafsDBhgiXEu8Xn/35ltoVrN7SSR+6oDkisn7ijpCZx9xi6XxxyE0+wuLbj1MWjSi65pdUXx9KerYjbMWNU36xuomOEKFnmlMbjto7JuRnCvjP4Qn8VXAYqiOFNDYxQuOulcef5NRC/9D93S8hLLApK+M+owliqPg/iMcLl3US+E9atlgwh8i2OFy68S7iMAhOprS+X0Xjbszb4OusTkQMHvHH7QHxxIyCy96ghwiocLfO800V8VRXsrMnNArShtl/N8MmBtsI8XFDR1yM5XEy/NMzwtn1bMzPve5R8msUGR5cFe+WXQYFDLm0MUozg/nrocCOR41rj8kh679Hn/dThjPeqRCWkNaFVpXjIzzCsM1UNmYxZrIT/hGozbyfDqJV9F/f0Hkra690fFt2EZuB99Lueyur37jySxgdF5po/d+g9GY9dVh77CPJcsTkkV0amjk3LjVwiffNpr1ylE32Tuluz/XDwnkP9vLpN7OyNAb21NpOVigLmUd57nTTpWePV0ngslghWAQtZ9zwNAkdXZC0hE4cVwp484OHIHKENQ0Wt83nZVUT6rlZnw/kLrPeCVbTdnVPlzqCf5W/XLa+/pqVLOwjFzwcMukbzweI9eGP+0YmIYx1SBp7CNzjvklo+A6jnUtFcmGd4lkqhI5U7KuhSq22S5gKLPYVnR4+vNPULGVEET6+4StzICZLN0fXhE/DMMkDHgxUDtgZkpyUUtwMVban4NudhczQ22sfGdL85gNuJ7a7157QJDU7ZN9Xwfa424rZNtTB2w/Q6ZyrLHSniJhoK1It8D+zp1x5MjPXOB8+6LqFqhZpMiDImDTzxmbHaFLy79SblV5i5w5OCsIHnjQC3mojfRap1z0DdPAA+chRSIjSPcKAL051AcifLLmBvXa39WESp5XlBz3ErOQ/LBuyJ4k+1Dmy17dnHucG1Vux/M7EMYZRnsHRgi8euiul42A4p1k3NbSqeYuM1jwRYmZcogCTMCERKgc5REgnCa4wjueaIVXwijsxufDXda9M6P6GxxrgZRRK5Xsrvtdnrhvh+DrD5Yj0KibANzs8TcPYae57M5NYxHz0t7cdZxpUnyM9K7BW+fdELrqwwMLvFz9TyoV0aNduMgIPgZtEn5sLDsO+0aA+rq7onHRkSGTtXoJ2YpuQt8nKuPmqB/pOsonydtcmSL3IbsQxls3yH9AC2vdw7Mk3ypAw4sh+1uqKe0y3TvUwI5PYzZqsuRPJChD8grHYTHEoEYceAWP0ukbQsFe2ZR/Tp9M7vbNT9z/ERdwZobge9F02ddLhB8RucyVeGO2xi9KysUzJCxAgn4774dO+mZHwoLt4ZtRO70ZDCPAIaf4VgcIAyC+3DePcI+PuwwmfZtBSj7WOH2ZkiSNzGZDqoGoWke6ysUAZO+kFxqBrm3k2vxN+4lJLYY98tEAyTmEc+w0aQLYCrfGyhHYyC8sW5Y0CSMCWttsZ0xX4ZK5Ke3Fru8V2KdFtCb5QUH+soSfZFMaMsfZthdDoV1Fctm4X3eDrRtmDHw9XcR+ZURFHXH4Zokl4jXYypoVYL3KVfJDCNrIsu0oRg3Cx17rmX0t5s/o3QwBXqhM7cj2dcqfBYU4wO2MunqXM5Vh9/6En1LRZqFP3cTzQjJuvBV/e56nRCDf2U15k623vC3MRyUbphqRrs9Hbe8+FyLtgX0TMO7EQJxuqNqXx/c6hNgLik4MQcDX3XIxRsUPiMMErAKxhEtM6qPxOeTWVxMQN7gxb6Q+4BozKOO5iHDiEddqfvWb+5zN+gpZNDFbWSICnbAjsYO2Mf8Xg5K4WCvJ6yGbntu3gZRLnGPglN5k9tH989abi0QMla7kQva1TXNLZCDFn4inUnAkR/F8cTik6MiHNbEabpUbzBzNfoqLugY1BuLlf37mbCamUFrBwFyDQeMsgLI4i7uJanj1d2K9nPlUdMol6F31b1HTXywsfr/+i+cVjWSJG15l2ItyEycGRI3IidvTnisZEiSuB/EdiX44GC8uHLm+NnF5PVknimEuVv+CN+fOYM+r4DFIvvFbzNXV3TOqQYVlI1QuNyrAS+6x4Ij4P30/xqOTFXKYAx2z3Fussk5cngbu7flt15JxQIYNKNF9Ek1DHD1iOlGFRIemWicdXtrCeWXJkTTF85BZc1WEl7a1vGEr85J57C4sFT1hs4Kszqh7quctQAiHd7Rw6LWF2AVzmmnHgxcDrKKn94pmO7pUs00sANr7+bydsPmrXcianSToCYO7fwtqlNJyiEoWNvon+9bkFZaPQlWmec67vhpvkt/wq62I2mly7wsCCnGDvckMnYomA/jcpGgAl4y3fYnn9sdyYOnq5Z+FW4LvOFCJw0U05XWK1KyxXZDjfHrs6pluhHmt5SWyVNVverOGbjSpZUSZ33HZgdOTY0IYsHli7lk1b901BWj8d5LDliq9dpo/u5sXFPAj9cE8EEvhn5EVshvl8UD5bk9MFX29NkBI566LbbIJSaT/Pio4/6x97IIITY+N9SBItZyutMHRKADhV1JcDWI+OiRIwHaVUAoCv64hWXQZCV9Gq7w9my6HICze1geYlBtgdHoGgv8rYkutV8U3rQSZTaXC3PU+SxxnogDOd8ZPytMksfFeBUSb7cYm7xX5M6HKs22RW2gNgm9xgXBlgZiYeGwIuwpMEWXLMUJZEeoU1BQTYSAkRZSzh1jlQmVsyP1mLfe1K8DaMDdZz7d1r8YwgwawH07WHLAM1ZY26w9qcmVOZAQPHnfyEMFcibDdWqy2DvT3MIoEnKK5fVA9/a3aBIWtYsFrf3ViEYwrho/bjVBnXGGaNsW601GliQSo2jTAq61L6pan90ECoVpi2AGtg8MhxPTvlw+DxbfjrZ5551p+LhWfRAtIp9kXkG2ENfo5sMX1aKCK/Jh6NeC7RouRF/UaIGqcDDRgih7LA6xLfB9JW7p01fGRBUDDMS1dCH547tPItz+ifKVmH8TIr0TnQSTWphBVZsKasUcWPqdacdgSEzfNJUWOnPyIk0GfQXprlBPQxrektOrWWybgMcNiCU/KdHQFyZSqtyC/N8mzUFA2mg/n7c7C7/LCIRHzJukp9VzAEzcFa35oPO+8X+EBxtCfJeFgECbVupq7yD59icJoRDFroYAmWMUeLyQn6JHDa8xqdOYwq3kIc9lvTfv8JosxcB8tT/jrdFWqXBWUJwuZtnnvZqEhbuED0PRc4Dv2zNqlEwcCmwX1GcZPHsLcMXzryqgl+7Om6VwSJIgLAMT5nZmyyVf3qtLaKr4XVWTBWQzEGX76XOMiYx3CffGIZh6N/byJsIvuR+Xy9lnN7QqxLzG6+UgwDxSMk0qjt6i38FxtvmavhEP0C2IfEsHnZA4flp1fIOqxpjZsw4/+sXdPLGeplZyxrCVDE1Xa+8x3/aVH20lnN7oOz+txWI/Pd3UXYkCzg6anB1DGY4llYAFFGCjxQ22CNw+3whHX3QnX7uJnyFQuvddwNDPszTytzRhk/jBcm9KpFf9B4T1rl2MhCbZxn41Pl+dB8zxm0sxs49Lk2HbmbkMYy6I1wR54CVvead9NOQRl3Lptf9ulTv5zPEWlpieeC0ChYbSAn6JQwNlDfhxGIXfqsKkunxTle/KTDVi+jcT0p1pMoMJMC5S3JKntIXx7DTRRwOk0IAvYG0AFcu7lncBPJW06QRI+UIgBZ0Xk/dn2yf+4Te9DRJIt3gNu5FVMzsMOlbKkMiS/VEHD14ZX1DUWgQ8T0l/ZvFirU00kPtWXPi4RTpzhGRUn+xRvagBbF06a4gDpWYY3IhjckikBoCamhEM5WUDnLx0+Lu0WiLpalxANvp07aiBxFygVuXZfcK2yvSe+YjsCePAw5DMtDRxZlTqY6IUfCvl7pTJDxYYJ17c+46PbVB0AKIbTp4I5Q28TqS0YjFKfY9AVKiVefe15qzrCvg2ZDMOoadSXuufvG5/4g2HRx4py5qwGZmsOe6S71CWN8BhqxpS6EnPGqPQTViGftJhOfLLpx2pNOB9GljFBqe5Bu9oDJeCMqJKf3uZHEsVAKDm6N89SmPaDQetlgf2z5FMtdNfd5a5iSDVcgGVmW+sUs0kaOhJXlvOzFfsCcdv4Js59j5svkfJ0t33BajCnejp/O06ooRN+erfWuFLBOmxLwkwEh/CXIylowdQv5LDzQ/QoIRYV9KgHQUNvHlBU8XJ7HCxNxZcvNizWpSLIFtiy2qVls/idQt8fi2f1dAKJnNBKJyx+M9QvdnWZQAaaTFgXUh70N2ICi1pH9UhxJMRWZrtIuPBUKYr6lHGkTPr3uv13P39oKaMeTtIHoI3zu1ySRN9Fe6PwA6njGvq8G5rLPUlZdPgfWxQH1qhNx9ZkqTbLCHO8FqKyNku5Q9fYgoL/bwhtFnM80wRyTMESmNr4w+NUA7VAqQ/6whdL1D/ABZGJUrTV2Vh7HgZNr5fTJv3SdHtcIURpWD/ynyyltqCFNJI+bqxGb6pRTNZH9Anfu2qWmUZ9S13dx8f9oED4oHWdUtT4W8E08cpJ2z60VBxuDqyMIJHGiiprNNkPoPX1E8gHkcaQGbWgplKpsSMcvIV3dWVZxREdKdMqRFKv8DHWfpf9cFtlkMEO63MxpeMf575edHq+Ib4Os0+JGMtIM8fPNXswPbzgHUvt7RGDmBOmbeZcagwB8v/gOWqgc/Bjm47UO4Grnayms59eUzpDU3uWWLjL/6F28BMfzrYUtk9gDX5QcIxrBhVW2oxIEMNfNdvMN4bEtbCAQFv9an8IXyYaRejd0Q6zYDcCuTDxF/phPOCx8zPKD+7FhQZ8w8XXtynO1FsF81DBNxdSS3FGUZTPt2d8n/VE2ID9I7IvX++ohXm2lB6CT5b/hF+uk6Ybhap3PVoRQsd203XlTFBU8w+HPa9LtZCK7q3TytBArmNBTbWhORS6Y0NawjJeW95AWWiUHqqJpYbupxLyDdYWoCVIp4q8AJtaAwR8J3c7ezyqed0Dzj60A64spvkU0c1N+CNfwRL0782fY9sziFngCgaAgZMI+6+hc0PQXFNKX3Xej8CnmHfXzh+IAkjtE55ZblYVVpLQXhQ+rYHIO3bZNENQmiwK0Va5EPdNCwWF2BClRUamhCrcDcE9cVgZMd7tRtfJBtP+hEHPdSHxZg1DZG2Z+CTBQ8NQWaWqSH3Hmp6fFcrszs8ywT9mc8Ch1zhqjlNl7Xj3kAPpLdFX/cZB7NZN+AMQlS3lDpvqV4RChr8gaIUYIf2rpslv+a5ZdU4J6Z6N61X98GeGSaSEcY1b80LOtIrxf56xSVapWNZkCCZeZY7A84B47yIwUpNrlZ9S8LlhxEmgYaz4cfGxW9dyGIzl2whkcsqNzvrlTe/LRX/70/iaFCPV6HgwyqEQQXMDd534Zzlon+jzYJDErYjywNtIKqWLr6G+gKqMJvVnnIV8do7RvKJyronOaSaulB/fgaHnOTl4ReZJYR5lCYE9UdMe+v2UrA0+8nYE6mdRgqowQkue6fnqvVgJCzv78MYvbPIgzGZcS8OuUGMJHqkMYC7k+IE9cfBy/0tNym2dcqNfb+qMthpyshs09MawS84WlZ72F+1paak/bd/ha28jgMEo87fg6pTPyGC64eirvQ74xusUsHbUI0c+taFvsbNkr+HvN1FL/GkvRb08zEnY1QnYtqIirH0BUYyW57C8jTHmGEF3Pt4vpgyqPfYB22oJjXtzF+rbgosR0jmr5SPusmP48ht7wz5Pg0L4QfIJ2fs7aUTUp6a70ifBGb0m8aJqI9N8SRe0Q9kO88sSSWZaRNtYoZsjQWSIhjeq0weoMd08G68NquD+kkqlV8IP/QQMXN/NDpRUWmWitzmpHzqUOiAmjiEz3GxgudL9vIgq4bRfrl/3OxkAdM6jizVZ+vJQ8odp8Ih3v+vNnWtBrB5tMiLySRVlrXMWEQaEZHdZxBoMXmYAcY3DvoTiQN1lfRS+KF+ppggse4NBnM8yV9aJuxdg+N1/y7AYn2A2j4hnlXT7ttHAfT+7rRhQ23Av8IlWiQ6SMJnXgfAEYWSbQ5+P8Vw4ra1Yb1AcqGf9IjvIvM5qQFtdVgiSqg8TBaY1zHhrxw2qE414X1T6pBnvEQCeZMdeIKZrPxoRWgVe43r3lHkk1GBTrQtc4kZrvI0WwU5R1pRVCP+UaOYHNWl00bO1AwuXBGWbTlNJPvRhyE6wXK0gCSV3bYlt/y7f7t9F1gwjpVvAh9320+eiVXKUL/SprsW/DfZhZUJDXLRPjeMcgWd7dAS4QxItGFX1hTc65atDFvKTu8NTywojeHu+fa5rCuI8mlBnXJfZyqZzU56Dqol2QeQ88HEruyaTOS9xL5HPWBQUGB7PfKw5jEKavuyL7dmdRaRROL5h0RA58mszx6r9aMozvzRIOZlrdPLHvkBtmAIvIqEjWH2a0QBugJNLFc9k2IkUlXvkpV2MdqlMkm1dGJyrPjOlmN54f/dSimQFRyATHO2MLAHv8uY2QJ+70xHGJ6XIPOvK/yIc+xqSCgQz7ZvDtzMqNFXAQwxssGZsQrEudNvy+dF025zMOhyXOE8nfnDK9cv/PWJdZBuisBiZpcVeL0yLNH1o4OTIP4rOI7lBIACCD+JATkcQOYmcbuQcRX69cZUPtqssI3Z3pltIiwZKUdH1Kwiq6yrxpVoDGx1xzKgFG1mRgwXCxsDDEK++7fG7Rcb/lHyzcYavdcNYfmZrdy24R7HVEgmj+2Wy20hrHxSOa4mY9bG4asY4/u1PF9yAh8WtQYwNJXCtpi7rNpPOe3VDJqd1bFBwSMu/4ziwy977AXg4k/zVQ19Es0BW5fqOsJe4+rEpgTgHq2r4mMDPyEOu3weXlnfyWxx314Z6vE8CK0ROHRk+1NTx3A+JtVRLDaRiDQwVpXl08VJu00jvnJ9PSO1jbvnpMLh/Pu0kmr8nNQ/DCsII1NkrZsPyANuuPjmvRiU6zmZOFrsewgJI1v738SjSK8oT79lr84YK9iL0muZeEE1GbBEaQr9GKWA5PSgJCILbhOFoFgS5niziGfomnRkyAEp9jZDk1b4ocuERSxoWDhCD3w4YZNDGkF/7DdpaSCT6SX3zIMEj3pTWBnFqpUS2bqyqAdG4U5IO96P1fVIjbXtJSlVLltJvP4YyTX962xovkrY3FsRJ8JRYwNy2k/rfWE39skjuIcD4VoCpOoBOUhjZ/RDiU+p+vZ79qeOMb/sKpAUBStOUm60MEh0rKlJQ68AHCinTYiSpAWSneLc/TCxSZwQT6KLU7y/VOYajzFlRg/KdEc7w+X9v6xAjTEWNhqzMMPHhDaL7iQUI20clJkAfkvsib8f//icgszsNMWAbca98BHHvSBx8VINrWNLEPWZfoE462ye983zHm6o4TIxQ36pBAuwXDxdL/v+1S5Qtf+CDgLddKielN9foeCIasnwZE959qNLVjIkVoWp+5aCfYPrDD+203+M3vPXhY6c/a0l6JW6DJvDCDUT4ekVnldBgoS3cVyQI1BvnkOJ+pI/5YvAUmTpEM9avOYIX6HkPQ/cVH/6LjkumxhnjMxJlE8t+xkFJO1fyRkIsEpLrEPUE/nQ/7gFujHDDd4Yq03tAxaWfXxXgkdT0l4vDTG8nGTsVnzkRgpcm3HNSJHZurfylAnbAlpjL2nOOxa+oe9FcUHFOh18XWti9iISFHlvHDqTammsjayOViFUi8JMDIuHAgydYhzIJvSeJ3H+YUiyANUcPYIknk6KVTWVxtz/Y21ZAaPcUtvsIiBA7WLzV4GsOZcaySq4LTWyay+7/9+YBhYwdte5QCG0ZI1O+da7Y+PSrCWDIQcyiVeWYZnwAuGr7Rcz+SfY2GUkGgq+RMssGhwP5t4MlsceWwsdN2ThbKpbF26zvs+PMF4SIiSn2d1aN07H8yBPIpQKw1Pj7rhwQjAo5s/FyE7DZhMZaecLKswInNbw7RJuj6oW2AZvUN/wSi+sDQdu4MtUeHgATH6OQmaavSwPSQBvtB/0ELdZCpspd2SdvPTyAWydBG9r1oV0qBReZmRK17LXsY8pLpo1xUPB7KeRSwX2IbV+h/NApo8C9SlNRZSlMWfNqvea06HQJ58PAHrqBN/3UI7GKpNfAHw1kKWwH5DL/yGBhYxRhl19eUIxro5zeFc0ab6Nx8QpYQpWD+1X5OdjsSBA1QpoV24ktnLMQitclaZKLWfhU/eBn7zdIDzqweZe3W4U6ynDw20m3gokMrRRR/+sulS9PChkCvi/CRu/VZ7yI/SCSZvPMk6u6SP9CxYVraiPrvA6WORpYwoR3nK4avNG6E0f7psHkOPkZWvqMGjxueUJewCNiPgRlCCdOb+CCqvAShdPZzgWBX5f5UNvIk+//oAQSAM7LYnpCMVeg/4zmpj2owmTdQQCy6SbYwL587a1X86uJM7EZ0MM26v6B7jRRDsN4mYSAwXSec5/Q20tGKvlqxh7u9yK/B4+Bakar+Ql61ZzR25R9YI26Y5/NRopY2LJTBJzzpqrep1x6v7q8w6WiWIfRzoFmRpThI2rQApY8JoFFNL8LDZo3o3BBkveIuEO6oR6x//slM8DPaikF3TFo6y64tSS5OX38lasp5YRfX9UFaMnCAFavzAufpFDQJnMcW+vCH0pOrRPoR4zUruEa5ZyUAaA5SSweUX7TDCVDeERpi5b12z1OWu2taVEfBvW0AGcz2yFzHK67skTlDgtsUv+NGolrDfezBgFGn6NMOnSYPW+NxXdONbrrVb46X6bzlDuEALsan6JQ0XOJkqZc/RwiNDtHVD48uCp0nlXBkhnx3uNSZqpUlLcfj6AT1/091H4Y9vNSAYcSGiamciuRX1rHTY/5gIwXM3cVjspn0WH059oXxIHA6lYDkUubedJ6tfBO+omVPgRAiYzOolX500ICTFGRoMcxeNIV/pe5Nb2rzmMeORNBXzi/Lb6FAsBzu+RyQunoHUu4PJbEv+/vFXByRCLJUU9yMa3xLkC7JSkZWpfmkeCN+H7G+HfqNTVVvfZodmTzGNBK//qT5CmEHCi/OlL0WmpeIhA41giybM2dcUtYxWOKAg8W1kB+lndC9VeAGRWZh5Q46YvXjqnW+OIj10RVraEGO97ZnAR2Xc1LgB08rzQfwj3IY+nwPmcRa6FqM+GUwcwGu4eF/wsy9Ev9E/ApD8oY3SOUvc/+4e4WfXDy3oMmU/oUHlEnPUldFZ6W1bq2Krxy96tfGxG2M/YIiw4VhicD+vx/snVSeMcxPRrhN9VXjH3FQt7XW5AWkvINrl6dlywjp/WNkH3+LN9z2f2keFeV3VH1Rk8JafVCpHWu8s79/YH1X5tvqw1eb+b2MSgRqp5GQFl0V4d90xkz7miDQ00cOI8hTXBZxP4H4/BnBdVtle1Gq55Lh9Cyy1220LLuNQ8znV5fXWQkUjV5reItIIDF3J5Y04C3nDpN0eTZVR6QT8v+k5WUV+da8fFxhU19jXQvidKOD1YfrUiXaCMpWzLy8lHG20W5UD3PfMCQwX5jeex+AWXry9dalK+HwHLnuiRF8hHm97E1+kTAAKdfl+s1ZxiO5qcPfWYX+p4g9CFKjxg+K30x1kevATnBSLsmvaz9BfVvTk2dvnNhH/u4nlaR6bOhV3+CB9KW3VcernGOSS9Kpf+kLFxCpDHEfKVpAJq2Z6MJAoRh/kTK7VghODo+uYm3dKQzoxoQrEhQh4uVY+cSd8B9dMgyeQ0LfDoF7uLtFYhm8Ag1AkvtSL2CLrDzuqlRhfpFwA1ciTQrtg2UsAP0LVbQqqGuA+PAeF70qJTnmllfKIsnoCEi4D5QURLD/Jl5huQ34kRkA8rnJ6O70x5eF+frCOWLnh6uXQi8mn2HJ7fGJ0qJ2lmIhighI+FlliZKt/6iUuH+MLBryXEqBJ1U8jD6PfcBeoWEdo13snSm+ih2wYrqFqje4423wjWiunH9I9FbjhC83TyyAbmJjnzgpVyyr+kiMbPNZT5JACeYyn7vdjrd9dSfqWKgoizztLrLiqhNs5wZyoBQLKjpHKrP1dP5mSmYJrLTy01Yi61HSwedLkhNilDF1eMuWJ1BwfdB0oT2OnkUb0ReB5f0YiHH/7vQ4oXQxXOgB18hy+u0c7xPVXyiWXpeddsKvtOnjKiiJj+sLyCYp9ALqjWMb/ncxfnYb/HHvliNxAqFtwYmZiFc/v/GDXSbMsZaTXqxQfkgTk326g6DSyvR/ojM3RpkcLZ+hkS1RsMGd39Taa/XrpZ1txHyhzoLrtFMjnVzAleAdslqKVFBKDbODEuOn7C/4hafiHDV4GA0IWywCYCQUP/IjwaJuNJXux3egqkxuelnLsH2oo+2QJqDdcwSKk9v7rmGIGk3jw8O3w+eHxUvTiWxeiNcQmAiboAKbvKbZBeHbUuVsQDkFYybLxhj0zVTjN98/n9puyIwon8nDEPHlkXkiwJ9pvubDMlCEIWXyat/ew+3k+R+WNfsP3sJHlIEyE86PAkROKJQOrLSnDTJHb0XIWsKDncPd6JREz4ahkj3kTWHgZCjoLeYPlJX8cJL0g1wl8ESzqd5CNYyXrkgmPtsrQcdVkHsC9O2CPD3jJrsrRT0T0CmwORpoGvLafG5UavNQdXS39oWGAKa8yJe/TDe0p4VoH1HBaYmZY4YEFviWa0tXYqNaEU9z8cRiFr5zWC4fH7Tja5bOCiAlx8ZTQvNzfizBQ8a7CkWzXZM77hybVKi9U7BzxnQgBlA+wmY6NWVY2kuVxYBn3nmJLf16fk+CvQiWBJ4/fNr7MPxZFmcy/NOIM3ZzECFvrpAiUiOzKiWsIVFKfeM/OAVhM7iouMmQbiP10unqONuOK7PTOHxtguz8In3GipSsRCiKhYnDGWTdgrQ9mOCRtapKbPm7Q++shpVzOKysmBK34QRhn0sRNIykx8OlFJEZF4Puo9N7nlw6rxCflLncoN3QrMSE5j0HkwxgfD5o2Rfqyen6bXHHTxv4hoOxfyQmV6dWazD5g/SU9MMfLZEeX5HRN1eMDnj8hwHaDS4wKrgHqio6s8g/Rasb/yfvQI/0UwM5OsJYJ48CElmyG3jhwjC2ufUgFHdqUSRALWToyqxP3fcMN2Bbm6X9QeSgZYqB6K/JDayUFy0WMkvJ1ZzY/4HPBSvlN1tEllctl2FUFwqbolhwXVVQAPQC1RMkvTxwQHFZrUtN0qc46NabQakfD3F5q2lwSVrTF0LcrGaH5BjWAHUt8pBF1Wh45HfgfSGPlEhTZbQ0nveF7q7l2tswPREnYrE5ThfjwQPPF+H6jhIttojaFzDnHfgvn4X5ixW8wuUj2DtnfF/hyewg151uZynANWlogT9uLPXiFHyu3pzMtIhn72YiCt5zVEHsdhAxBdPbSqvXCw0rcwVlKyqPirZGPWH7+m3RJYOAXjf4mDIG7DRHTev0b0q5ncJ6dnnSfu9WiPCrSABlHEWZeEQVahRwK90dlCQIAndpGZS3uXZeiybL4JiuziqIAlsdPEimsP8iAZ0484grdaB7jNH72izfrZyag8CikB115d3BOixuiF15+iOXEC8NHgSFiAf/SnU6JRTBeAuhZbExq7kKz/qMyXpGwnHt1WAdNyCfRBI+Aa6fZZKifzEur19lun82bjLN1pSb3YJ3mYKk1rCtRXrQxkfkz19ZOVX/3QRT6cak7S4CpZArcC6H2Rz+IMUrFUljjXJYirUjf4q0JKvB/nG33h3NfYhJtla+7a5SKM9YTyZntUdc6aeaHqwWUi++PhagMyrz6sQuFkwhAqjDqSH6/oFGLgwhSUyrN0LfQbgVYvnsM6OWWHvwOhlVWmrYe/z/c48o4amoaVp7iwPhtXBbxjVZgktTUVzmb3KBd2MRSyBNqXjm3GwewUOnZuLGhvJVNSmav1o5fYgCJvDk1VM8GPGoOw+u0qlZ5itIZOiMTYSb8RswAdzfBAr5cc09ZzgaghqD7LTLE1jj1+sCcqTp7P8WgY4QiBHf/lmDyQ3LxIqUrxAREpmxUiUwIHf5mfUACEw015TbbM7ao5SZ8qXx708xtw7V7+60Hn8+RKg3It4Ygs+l+z5p+e5jn1YsNnh85dDVq97Z2fp/XbWMdUUPnn8ZG9ODbKPSpGs+cntYi/rKscmyC33gGRYsSOv6Ttj97mBSsDmlP6M9ALHfogegTlPiVEyqvi0YCrF4DNCNAH3XYlT8sCmdBT/9qEly8XIWMrzAm0R+23WhGYFel4zJ0veGz3XdMs05eGTX/m62iULEJCsQH9TEwYxaNgA7KxqHOjLuE7BJT0UOwW6UcABGCnaJsHyXCF3PoEyams1IrgJycNeaT0s8Jm7uChYz4Urai85WMzGjzkkE4ZL0NKRJ5cPcXM8OhCs9putH1Lap6S8hInjkOgwXxFJq8HCy3vfL+90pwKVjASPcA3yeMGbFQTcM+TC06dwxnrD0c8tlNeIyWza80bZ84O74A38eNW5WI68qLEoGhcQa4gP1L8pZNj582bi5EXMtE11sW9R4U5RL8aS4w8/Lihjw/0+NyNBonVWnwgy1S8k1YwCZvLYoo33FJwugrouwwGyw1yXx37XZObqgyZAbMCXDXnv2Jrht/T6l/g6xvkWJG1HVwJAmeeC9R34YW/F/c+PDKisMxuZoYkBsux7CBm3JKFVkaJjfwWPEP3XG+C2hwnikOqtg+9w10BABAiEKl6dTQoAX3FA2V19dJD3H1NpukjEOakbWLv8NpWqsHz/93N6FjbQBxhqpj3I7vmiugP4gvpeRv977pMSDI7Oy39shU2ACGYICyy059Ms87tFvCujigCaCN+R9MYHhOAc/0rEjMu+UYCh9JteIE61A23/cAv8Dj+3ZlevVBZL68UtPkEt/6CzghrfDvlaz4+kYO0aKbf3Ta3/OjOExdtYuyIXGVInUc6whKurc2332ofcGtVFOXfi6eXCaEsR7ZAyNnV//2jKP0rvikfYUTC5Q5wohb0AfZjTioGL4ADq1IaaHPRbaSg9tWoCR7ANu8Jwezw1VG0/fxJef3vBBVsoXoLGBKemUBEwToqRRFdaWnaSCbYlNBC3iUnypPDIw8eBJXwRxGRtp0tWXIKO6dw3ffMRYOSc3RT8KDi1eLFLOPt39WqVXSHlkn/tq3To3LXqryNKV49r+LcskNXpL7OTGkQqlB/NP/kB5vX65dZDQllqQcEwI3nncpjM9J9MWmAcXFwmGWfObkJem2btSfvEpuJEM1BIt35Dp/xYVaWeMqZtPRNk5fcMuAv4TSxcbHqMJRyC7E/TlwgQMlNuyjOixVolTeo3EyLJS9nykw6uOGHYUBsNp3NzDpIajUqBu5/mWHFjxFNGWIMTn7CS0UYvg4hs2/q1NTXaUznuqchdjuCB7POgVtILZF2On0W9TNJvBS9NiujU99sa/28w28mbIH1sKkYITbYvuLFBJHXO/XuHNzALBF7dhzV1o24z30SxiK2vi18p8ZEGJS1Y6ea5b0EyNohZpR5C1JnDX3oj8enztXgGQbgkAzCeMlzo/73pG7+ZLJUuer+/PvXwkaXfeX3i5JR3thL6mqKvYeXDwPyw+a70jHZetT7oXGLaB5C72U9bzoEXbalCh0f+glZu1HtHSMfCneM+OCR9rYp//lQepM8O/wpxCzzudzazpcmM3yLrt6VRZIBM2GqxgZCQneq9IwMk4owhDIitO5l6SB6Lbai0t7qxecz3wlziYWx4OVAZNPmuTdkWjtoi2tAmq3OFJVE/XrMYf3HY948l1kusNNU7gdhib/XbB8djvWzOSTLpdxDvch7J57ryjsrrmGcPLhNv6gMDbGZ9YyaXTZnHrLqoONnDvzOzJp5CWTC7/uafDwp6CgjK55W/WbEnjuo+zvEu3s+K90yEUFRwgpgAUemgRc+uj/PFYIEAY3TaZOfZPpTSYhHqThesX7qjwhjnT5EWgF2e7FggYb7mguXRNGVbvrFFQqsMdh04h84ClXKZr9kruCNWcIBavGsoM7N2IUZ6PKadQ1a4qwuju2eV0iRpWa7vL/38zru+Pq7tD/qWtGT9fPST1MzajbCr+CW2XEgpNJsYe338IvWIxP45QGLgOeiEAWRYP4r/HADRp+gY3upa4hUmtmq/+VIusV9gjw6IXfjv7ydSSwkxeFsyyVCaLpSbg6uas2VtG/F7Z9fMDGtzKWLPkRSIZcz6dNJHAwr8kLtlkSyEYIptGihDQiwnWxeW/oAXSWXP6tlxcK/6k1IB0aXoIuEXjXP0ZTSZpb70suSBAcTlgAX55NqcVrqxZ2nLgciYnNAdLaZebS3Z135ysvuI/KXU7DWT4V5I6gMqZyDXgl8dcoGBWLdbphFGOvRw7UZnKNvmhYgPeQlInDFxcMwVNrWD5GKyVSx5yr7syAqOvoBIyKY4Da6UTefNfts+EYCY5MHftQ82lQMQZggT7qoHmhZLP0AIKHwb7WUrPg1MYiUebYW9sTPc57tbROMPUrey59z0eI6l9SngKpDlQkV19VJKREGci7pPGNik+j4w9lnp7mvd33idwDo+A6gCCiyelDCz80DDtp4O80Prwsky/TnMqUwg9ro/Xsh4U3hYHtenkRB/+dY2NFt2fNe8DNZyEH6EsrxG8Ikz+oVmqWz1ai6wd1PSC7Kpfiah56GIHUz/RHK3/YzZwHEUtCVYdg8MYFPB2x/X1b/Ajeg6BzzgzyN/3OfSdMEIWD8H4Ll6VDbTiRM/pQb8LNLBW/2TzcYDXBIDiqajujTjcWa4RygSZPs9wiSh1e4kZimLLl+kR2kBWTmGTxxP7cwO/Sz3VWAyWVmrGSq6dVNys+TiSXL7/NpWSH1mzmvkzkfxESX1wZjZIBsM5Qbhqaf+t1SoOVclUpbEGAfxPPmY8+aTq/JTVjKZUE1KJ3n0hrA/x0TTQvdT83TdErbJV4w3MiwLWMkhkU7ua/bXxDrK4A/dOEw+fegGrrTyZQwtUzrJKs3JjhnBKUi9nAbiK5xAILGQQQ0mtTRG52ahC3BqOJX7IabDS3aM1l43bVgmy+iBfeapC+HfaleWOYwd9NBmeJ+Y1vgoH2gTYBwy13eqZDmCn5VxG9+o7Eg5kPWqAZoCpfqmiX2ZD7OPbAJPf192rXCM6H1gSItzGIBNPxdL+xnhGWB/VY1u9qkgaFY91zaby+P7J4QOE9qLVDQsP01qscaNeN2mW+4ZVa15TyeGpU94oS1IUBZHFUOvTwatrGS/JJVqoXNBt+mKowvDxBRwNOzjQQBlRiFQDulcIDvGu2PLpcztKxl5y2nykSAEopotCzikcO4bY8DganxgOcHs+c1WbbSOYn94f/1C5QNF6+HjWFEfanRSAaYLTaYILasfZvgNAy8OyUsHSYRXTRbs6pdP3eV76pXs0qBZAtgvniACAz75FRZG6jj6Zq4RjOvA7+wpvQEN5nfYnp3Zhufi7C2CkCAbnxvm7bhV4HAY6kaCPollM6QVsoSh+Qs77ySBd/PB9k0Y9Z9FYDjwZHCSnj8BeAmfbWL5Ts6+/jAZHVrmEmLDXwyJ/Ahb+une9Qsdbs29nhL+9CrJj0/ODZAxfDWDKkuKMKrBwzUXLlWOXSIaxwn/s54eAWIgkIxkwRQf7HJZRsUWGud5Z6KwMO3222AbdMBlPOIwI7K+jwheohlYsGUpJG5d+byymPOGIQHTSjmqUENHPIrwQplykCD5+mUpx9luJARFW5t+lGp+nl0mMl7V0hsL8Pcw71hwcIbZvyrvqBc+AVQhQdXDVV/dEQ3bBCB10oimqVdPLoaLphWJ7FAF3Cwjzdhr/clcDgJpTBoLyedxjULnQstZBD6w7rB1PxyFgDBfFzLlPPS5M+9fJVhji26hx1IdMofLjqJpOkCszQ6d6txWQ4k+uHqOSHIbriB9EBGlBFjZ/JbsYsVQQsdBdfvK4ygYdmjLXfaA4PYcp1w8FBbDgDK1zz2lusgJEyQrNBL0Oev1DwmaL+d9WN4mS5oNflo3mlL8kcz2tM0GHJzRmEs4+lEefG3+ry1vKP9FlE7skZKzyPeg6MjTNjckqfv7u1ETBHPh6b+NRkKYXdpmu8BNkFl1W4Uh35aWN+Vo5FsnGBTyugQgHaZx6aNZJjJLQp0TIBP1K4RdMGLkQYWzLwNoL+QU1LMz/hOPjEmWeKo/rqblgGeyGRjBhP8qVAD2kLxAjA4z2c/xDatsLqiqO68HIvDu+KNIzLNCrB2AYQnJBkHrihH8PVlAceiAPeie0jfrPFqNMzmMgdqmlUtvXDxanE9kphJLHgbitB+02JiVoYb1/WuIHBS44tKvSYwpZpvRUXM2F9rwCvtWm8GiHR4XnoBnBtzqAFPFtxIjOd5uUrLaaNfg2QIBmZo+IcYuJfrIV84l9VvBGGAoqhtJEp7fEH4DGt9jJ0X/3KRozDYFiIG0AfzzEYmZOHjgomFmEWgwZ7YgwVYK2AVePMucCnSlw3gx1Hd5FXPs2tP/bcYxI4jZBoG55+6QT6MhtNuF9yv/oLo5vUN/pDg2wfznEVBAEHpqek3z3YOqyAKv37gSTvvBhJTmOtztUj+DV7jaNuHQPM39SB3fwribEl9WwIDluGOlcle/1MCblK2xMrhsjmbjvugoNEoYKZ6i/tooX4J0S+bHUVR12+BSff09mXERZKvs9oNvoP3ivRgkbSrs6l6IeHpol4cdoONNs75VlHtAuAdm/7kBLgPha+QkGHc/5hdkNtMWWRnOP5mIAi13nS8w0bySeOjUoM7lhZggIsvMEKZyynA/1JQA4qpwDGeT0WZ/XUB2+erRykrh987N9Nw51SDqOS4Hjf6v50v7p+8HS7TctjAiBQHu/OqlvckALzf0ZJAq9g0/7P5TjmNA26GmXeVJsP8bLgp4KHaPCDwiUmzXJZXxKsrWz9S0b26U8kG7fka+dBJiv6+jrZS9HM7vktlO6IrBI+4jy4jSQIf+QI9qhO2qYrHZfHbTOn9p8Hudr2Zvx2LSkZiFqrgDS6XhoReKYSiFuSpvY/KjvRApDleeimpYcDNY3XFY77Xl+TetNMOU+y/MJLHJ5vYHmWFfwZ2pprgfNCdLuosb882Y/S5naSpFdDfU4IBRCqSmV705W43j5Aj34fbeppBrvpc790ieieTWM2IpydXiIPEh7Con0uWtz6mtuEk3KpF0Hg8iGX6tOXvjlQMXe7UHrCL3UMjKm3NhKZP1L6qOBQHT8RVXHlTNGMZawfei4iFmd7J7adZcOe1zmW2T8kL8EY2HCfuCk9UX0nihFVhxEzEuec+LONNf99o4TSHB99EsEBQyMj047zHQIFbCbn7GvJtbl0lbSGtQtRm7FZo2bBvckZwsmWswuXo8EddXT0ETJaHwtOnppqwDBS9UazNSU6I/A5GBetLz9u0SreGcIM622wk6wBJ2P6QoozQq/Yteq0YICCxTtqh6WQU4W1YNicOaCeJGaFSI5EU4PpE732dfOkiVrqj3kcHZwlHoCTKdpHkflNo5bv0jSYqwcVH2dGncjjzfX0XiIk1qamtNOAnuaOfgOrz5KSD0iU3ASV183OCkDPEg5hr1lZnh/Aj2msiw5X82h5VY+INR8yWPWsg5UZkaRw2A1QgS7VpO+C8CYZIkokvl5w3+2EZPADVo8u0ybZSQlO74qBWjRLnP5NOpEo2tSW/UcNe4gX6WL/Jyx8QoHr8ZFKkifAu0fM8osPWOPpsNiky7pzSR8MHb8fWnBySBmYNihKAShSGFVRzK6lGi8zTBia/8EiHIhUXqLvaDshqttp3NKqtZ8jutPxPeQ5jZlCIUQYt9HsoBTnAGLY017KTMx65kdlpD7Kkn8CXaXdf2WOn65dnBRjpxhGYbMwmCt4wkdNKMy6U9yTjIiGsqdI18XhQ0eHFSf709t928gjDdy2no/nE0ncFp9elMJPoa24rTsJ8FDn91llFOJUfVEM/dPRtEZzzH3teBII9CVKKMIY8kamTjBT6BxzxpCMi0tNUufcocCkhZ9zGAlt3dOiCl0CMjZoapM+7qwcWidsLWl1M6Ae2HNgMI6qaqdAdI5Mn9U3eQURpJQCGBgRXBnEdpEUt5TQvN5E/5wD82Jg5AKJLcGNTuPtKRAUrOXt7eS5/kfQgXAp1fQMQMeAoF5OgcitnRCXDLCoY/Tmnsrn4loy9ikoAUJ6H7S2Bqaza0sqkP3dzCK+sVumtZtsRZ6oRIuAP96lKXvRi46j3jTh6Fleywgc+0GbotkKWzTJiClKJNScxXgwhEvhOMR5eCf7ZMy8RnBwtzFEZr8PqyCh9Eel4UgAGaF33JksJFWqDqwHRk+PFvgx4wR682aX6HK2ct3c80v7CArxmCdGCnYKfO7g+lIcZv3zxEieaErZJxVKEYcdZo84XPH8u+V7N3HPGmuva73UGk0XcObp7WCWDv1pESw0e8CZHjipmApPzbvJ0EFMvtFAsVPObnUYo3Krr5tbEvjrcyT5pZZv+ISnRzBL1sTHhb7juJI99efvboyuWaWJL8SrTh+DIpBhgUhe1MD7sTRonkI8aI2NYHExE4no71BJB8YbqlBs7itu5KgYc4w2r8csUQsiV0Qe+6H0sJv7q4CjXBw5KW6CgJ7kFcL//f0v+BjQYfmKTe8iEPFyG6PdF3df1IyKv+IJXO3GekqQpl1zc1bY6ku7/LHpyTBGPW+BiLori0M6AmgiTH5ckq7fuvHThR0GfLCBynCCl4gL8CLg4LXqQhfcrQMLyAKuZ9bJiQhaU6wRLW/glVKVBvyGS1l3bbtnmEjRG67b5FwBrydQKaFNN8lSLE8UEopDzF2YLL1TWI1d/xhPNyivbtFxt8xU3In5cN8gnkwv+lM0nMHkvkD/9nozHGZCslkPBnvoylO+3keUxv8p+vPKboXMvW86aHod1P1mHEKxdXDABEXr0zCFbAlHWYyNBNIegXnrgjKpDhXYMMLPwg5284sPPDf4/sY5WVNJpvhJpQEUyOcT7+qoJ5bCsJgCLasjgnRrWTPSQ40nPegbmdsPHAfZPHOMSpepOdC4B5kzHupejaAi3RFao/5GAx6ZlWIY3lrX7Czm7Be7KLkra/CzHnMaz6LOwlvddZVov02kIAnw/MaPzar8gsT/Tya1acFdt+cjKLW5kITrBPA15jhFoe8bTjDSDfr8U4YO4+0dn1AEA6P/hRqlFO5aKTvkAzFomcVJL1VJg4cTfDUiC0UWvqnj28r7668urzWIZhoEWkAgpgStLczF0WmVrYsH64xyO7lXydMcgRm2ylbN1GpyLu+pW79sYviSPCCEWOAPOOUvn9Egl6yBhDo0yEA3mn0e2zii7D5DTKEPCfbxQMeVdN8gMNcbHB6qvwXfeGosauswR5KQ+zn9Tzf0qVueMm6jnBuj7/kTca99OvFLJvlbFq1Ls9a9ZoTVmw7Fk2XCjHykzzQCGG3u5vtj+UmCBMLH+8lBFcnUWrFTI083Pjw9mZeZcDn/Z3fEdOHnQb78qrh31NN+zlchrAZJuumP0lqmq2RL0XYZq6CZPbW9xNdlbsPemx7OwmPgqKTJByJNJGtWnpIeKCkkGr88Xi0jimIKNdycjBIa5pmD7rnFLKNtzTd2F25kYF2Z5COtK2IezkbcbovbIPSj2jGfxZXb0bG6s2OVN9GzmtbDK8pvVkl/llXgCY57s4JWzcixRmtXfCFmJ1pWtY5WSSsp+pvE8ft+NxjT91E48ooSNvHYZZ14Qh1AHChvU/Z3lxgyRjtivq7rboDUuuZzXXUrxd+63GW3gET8f4AoS6IvmQnTgY32AMtQEPjMmu9xK8rgJ+nxspclERHW5hSQj4pK5KUyiQPmQFQ3NMAExOSCwKRlzwYqNn6uOnB6WxeGML+x4oLAls9ot6Zo8eoyPNGRU4QoK+tZRso/dJ/Ndx96yiAEcWLtAuXD3CXDX4EiYtjiV+/X7T24cy0qNksTorWBSaGoxELxudyK+hlSaC98YUkBJ6c+pnQPtUR6G0oTxxhoyT0cD3rHUdryh+vo5Z9AUXbVqyiqPdwFYZ12Lqj0GmS4RtkgqI43qEk0WOYIp/nY4uyfVtibSxoW+bHuePn2oSi1jg0AaoJCwa+JKwoItlio+JuFZnRZUHjo5AHAr0D2K4Qx3JjcxOy7eyZcv3YFTgVRd6pBU9kbyvOFsOVa65mrMqTPuCtjx710CNrTWdFft+R2LK0WR6XfLrV1tsALFDEL/cMQZBvDoi01UJ+ScKgXJB3nwtxw7nNMXwpnQIX4jfhREYPDT+TLBjh4g1VLPif0ZDBCWtjBx/EL/YrpE6T1suKA2n33deSiEe1dQ/zQvBePls597j8LwzgP36xAgCxByGeXj/9iLADytgPvx9wUVGCT3zI/zwYr8kzphdV8n8xXEUmh8fuQtJ+qgYWIuQmTI81Gmaovze/kk31Kh5TUC4GdJ+cEqWwiawGR9ueF8dCW86vjX2YHPY0EsUETQ2EwP81UNdoLhe18EoyduBWDuIuOxPR28B6Ndkqn57Lq+4LOK4/CWE4yP6KJEEBBguh+0/u/Bp6aNXP8kpEav0v/8WoRhz/9IqpuNLfxHiq0hVQEbzsc/NB3BXNvHk0LV5m9wvEh1O6fZ5fuS87QfUAebCOUJ5dfAGE7++XmXQTNcL+dfvXlFe2QavqSRxPkkFqJJQtoCmMrYFvaLwrlnpSk+hP7qozgHRXWNZa8bb/0TF0FvY/H26KxdG2aR3sDtab5MjKbZxzUVBFTPeHACIyoJbNP0qc0usNx0aKCWTOdodJkwIFRwL27fp8Rj8XaR/mIEBkcXkvGOwNwSFCzTGJwulgx/SGWsODAdPeTbXD4iJZklbDKAG6XW2pBoppeesKIlHZnSWkMvhBBEbyewYW9BpHHopjvZ5PzfzNjBtKJN7BPrJygF6Y2ga1bPkxpMAoUBGYOUdBGhjpWErKW3mc4IXPlsuVv/QYx8dMjKOAEJZkHn0cCg7DDAniFP9tOHHz+ABT8h4WBXp8CXb9KqUUl9lrFOQPx0w8V3AdqoEy2HIk5DWyKSHYEtPF/I2hKo3UO+d6rfxECVpmaoeER/4J/SxxtAYBdBmyMqsCDu90yQaEFHpQrgpTrUUjbSZglmjb/v6Q6K5tg4o3TFaY4PZCUJ6E6g0y379vRBORSjaIh2JUmJbWnXQwAcR4ClRDK3fpAVx+ReP8cc1ExPkyUwoM5Qn2I7fOlDfNt1jmrdiLREsR+ouIYaxe1kbGSqsX5j/DYJd9jqwfnWv9pRD9rfHV3wHNuj2Hk+s2nR9kkSomx3xDVqIOKaDiH7gjryyKSX6hK30DBsc81lRYCx7/mdSw8m1gVzrQrxFA/dLDcRfOGVq3BMod3TZ+QAuNT+g4xputPGTDfF1xwLj0DsUgGbMi5cql3fj9A9F6Gyva59rd1S9wdaYfD4OG06vMRtr52QxN4f8dsyg8XkBIOINWY+b0p9i/QM8dPSlYHgRugLEPO0bwlKGwZE3JuP9nVBesjxvbzuVHEqSEso3QU/XdlcsY2aHPyv5ApVSNOk3nhSnPe9RBLth+eq+Al5pynWjjnU+QmfbKWTj/omCBYz5oqf6boshmWaJ2LSxi86Y1FwXSuvu/eb4D5qzngE744UHEieAAFbxO8RyTZ4Hd4wzVvDQBPowy/pL50uMWxAENl1kGVRLNc+gfwIcxXrj4D5vJMVn8k6y4cYcntWiKZaxSfg08c9+if1C7yff+SAlpMetYRsRCUbzG+gdZCk/rlolHhcmkZKNlSsZj1pYQJJuox17T+4XSpRaUuXnrqR/22bA8yMRGvw5NjxxAwBYpF240HfMtFqgWBLQbtLSY4uHLPQZt4+gWK0q1m5YqahEfR4UOIMZmaK5p2BRcLX4gu5QrdJGHZNg/RVnSzLTSI8v/FWPO/5qnlu2F8tPmR81+/4u70OB8lqWnJ2DivyjzJlQ8vTrVYuRTsUSjKOosjaZPaHrhh6zaN8+WCDAqd8oNe+vioGfVglMU80I1H1pwEkJz22Zuao6DGc80SF1dTIJbX5GxcadI2U0MWi4+wM/PQiuXh433UEmQyRfGlpJJ/ZF1+vJWh9+8T+x5K494ZL00EWOGGs7sNy02YhQ+ptB9WRq3diI+iJIz9Yk3wlgoSoKvi1TFRQVg2Y1wZL20S92iln5iI3H8fzziDEwZNMGZgV4d4mpDe9IT6DKonqkk/wvAlf8kIPIh26e9d6M/2uq1D6Hz8c9yN2NistyGYVXb2rns3SPf8Z6OnuHfddvrVGXGSAmE3/CkUeR4FoUb1s2m1TYN7FTgchNFOJVCYNcBsE/qJrRegb1WdmiQTrhu9aBLjoJ5tAcwfBqt7hOOJm6HEMGk0GAr+k/nV6QR+IinXBQvc+AafnNk4GoiPv4EZdql+PrbknPwh3RQYMbO+L2jv5r47kgUU7Vm9kGYvJcXPhFuqlUc+tUjk0VCotsLkZg88LaaKr6xahx2Q16NMf0Xb8xcwNQyUbJ+WvCmZ9Yb2hjawmz2FNmk7CC81HEnf3G+FfU16+EoPfjzxm8uGOZzy3gDl9327PaLOp8T7SLCSmTmNfeGYG1x4QRumF04v0w4sTqFIQXR9Wb3W6TGNDnn/B/X2GK6PAHvIxfgalN7yFNJ7T4WDu8S/zU/ZqPHBJiVZmX+fWzefuad5HwfClGwssqkUSIwmRMVaFGg1ph3vPL+VZISjxHE6n6/+HRfIUUMA8foUOsxPppStT0X7gdZlb+vwmaUkXpuygevhLGe7qHzJe0umwu/es7z7f48Jsxd3ZUpnJpUXL9M9D/m0vCnI+URcQ19E8cXD/K8FHdnYXJtGa4y32kXJr4OP6EfWcjXp785ZPKCStNvz4fxsmZ/K61WfPidpbYj8rbfPr42du6MQVlgLwqHc8A1eh0/Tz5fBg0EqnqDsw5ytrjvFl3ThiC2Eog0m5GshydcHbC5oNRYas2enhISeNsOd1RbAqDXeoh7RcvDrkrVkHFFozbJFcHO6anp7uq6pSI8vMFZsqzJu0DvvXJjCwLmLOGcxvJBbZYA/FRIf2kA7813z25mJmZKj/V/k2vnaVY5LHu2ZjRsz4u1ND9WpuGneydaRYdc3qAdmPHdUNRGH5xNxSA76emftDwOUYgoGuUvU6gcX9d2VHxiYnK14NFJxlDwsv/r3Qwq/xD2fbrp1feAPG0zO1sgiwTuR6YhuM9BmDCZ0dbU3RgFi6ZBcW3iaioICCo6C8OWMrZMW5/XMinvr9PoapNFIeDETsWgdCJzsCJFz85LNLMXhHfKaxAFR7Um/e2R6NQL9lKUPyGY9Gi0YqZgjtjCescn1WcRoy27n4r6SXtweDn7rt4ii+bW52z3Epdq8HyeZgvoIeiwnvPC++09yvJpefBXzNG8gPHwZf0Db/43SswB8LTLN8Rf3MQyUFb+IwUDeB96lEIJYCOczY86lnM9hAQoXnfBHuURG/davJCRr2532DiIk8bSQdtivOBBq21dLz/XIDYtIG2cPjNSrLPmx3VTaqgSjJSQfrmdc3+DO+JOu3V9nrzEz/mbyJiyNIeln0SxScOYdN71s4jxTkagNwHU8SY++H5rzXYY1t0eovWzhxX1mx20GRfDYM4hj1rZCXsMVpxuq8e4HsMBEDdSVIxecRhrRB4J7/B69piAaJWxKGlyP/e8fmXrso6SwozUC97njfSHD27ubBW/yEE3UxNYxu3uK3haOY4dH3rZ4ysFtHSrw0uX85Q1XmHfwXKx5kQVf5XDeoPwVPHxu/5N47WRT5pLryLqUL/PzH2VswBqRn6x9FZbLsKREH0gxjgNkSDBtcZTnC3r3/cN8xaBAJ9TlVtCN3kJvRy1ny08rWFPudVnlC/a0C0xbOUrQNDCgHLFko/tAJEwg82zC56E/iDV7Q2PHHJ2Rcjc7pyzBYrza4qSQuOrSVbpl8p19fPOC1C0V+mmBlzo0jilcgGJ9EaDZSBzupdUBPlz7SBZHHA/S1LldZheoPafvym6EyQAgwKD1y67DXYM6UeuhEuUyx0RVtM5YOIgn4XXYB5lCzfUf35xNFEhrPmYvAscKydyuP5Intzk3A98Cao2b/uUzJMLMHuG0kDvJho6kuTJ/CIa2v8LUW61LcrJ9ec2d4Xn5e5lHR71cCw1DhVup9KEIlvJhSsfgTignuMQI11fLROHpvxmbUouCHfN7TZDOuUhDmX36CZ0Gkr3oJIWFR2Bwid/t6gR9HSnMCj5Yew85WPG4pS45zfevweir2bCdRPCB6CkeUDHSR8L/VEhgA1HuiBBXgGbVyAUcRBYZAQ3M/qKQz89zKeHFXL+pl8RgKhtLGl6xAQ1Oi/iSSJJvnzF9b85aOcyn4UyRkqr8dBhsheRwvQPd2Ck0f61PRcH5n4yO2kayxVSnEQ6SsAVN0bZvLAERlEaIfS2Y0PFzvMgOwB8ZNePANCWnE+Sulo6DIVMqjuyqJHBY3euAQo7sXPRXD+MK1MpKW3y6jBqUxDdCYTJvebQbt+l+EMFjS8Xe657s1YweY1r2SGMae/5kt82DjL4wV++FVIOAnHCbbyeXAWc2tukCPjd/nsBkYZvzi20d6/bu7jlkny1muQLtOtgVI3M9YZBoZxM7JubXhDXAInMT8uro3VqBQ2vbAGLpqCihi8Rh0pjJcRxnRZvr0EPh9W5HY1rU3hn8tHh0MaOP0LZykgjY9P7Y/PplRW1/oKG9sFKbESXkmouT7jntjDoMVjKNk04xJWgT6FKy8G9bY8jxzEVJPSkryvpIKh2sJlWED38lJZ44RSGqRNZ+mcepl11pLctkwzxqJ4uZS/nzjbFfwiM2aBqCs8KA84DPwkSvEBf7OoJNWbuL8jNXfuNliFXrq1HI8W0pqEG32pEDZIjuMa8CpN+OUzbf7KqJybLFL94LdV9NaAvA/gjOz525JPvSbazyJM3Mkqo7VrEBmlgE7RH99FOQNtsO3kqUR05C85tZlELdmvVowdBxD8POlZ6KgVeFqDXGCgHbq0uNsTbgARh0RTrYANfzKrnml4moHPnvXlW9DPj4LfAczm6PnyWt5GZTMxyKfVesw4fypg6U79g4YAlh1+wHYrnrRAVxvudFozeNGzr3DwQXzK6KEKt9zsO1TWg9ovLlCm83bsC/etyYPNCeGpWdX1iVCMZBh09t1NcT1BcSjUzouGecJF3ej0q9F3v9HN8QoxnyYnjIxgrGhm7zNjA6pv7zC9UJh5fDtvOtBbQt8wmyZRD+CgzkQrBXydVElil96BWf7hSgWBxJfG9tcwWlFIoQf7tjEbFB/627W0I0i/+qHU5GZH/fwAAStlJtdrRbTBPuc4fhq7lKEUPmRxawl2ThghUsaraVuGvXk/Mab66s65C0OAzcG1e3gdQB/g5OBU8P6G19HCbzoS3A31WSGry/N3izkMGaRbQcNwQHLwmV05ncIY43S5h192geJzCMSbpwJyHMw3PiAI5ITKl5bw31rWVZevSDKqjqTQtKqbMgOWQ+CUTu4MW4xAFFHqvHNAzvY9CGdJRTzM8nIbbfRrW+3yNuQDTDZI+b0HnMmzYYE3JampOKPOkIlNNZ+GJr7Gw794netemiwbKN+/l+qKDuOwwAVL2OIqEaGVCPV/xPjYhoMMorh+TRHcrvKHij6cAptrz/15y0ZSsLcdyEjsxtpHd6CkTvhgiEpv7UON2k7A6ebwnEME+eZHkohvOQQcAPug1qjHcH1Lo0ojIwJ7kSHUuDHm3TPJXsKPM/7qihYE9ghjclQXpBhh8YXCJwJBNOcqtZ0J4kDEmG3TILP+vvFV3JHjWKqktVYkOPTiYv7Lg9yNOrpXDHiHrFUzRnZoNFlWOw4ggL/iaLvnt786XLwotAfbOJBym8SPYGL2uiLamGpikBMelQc8BngOUMOX9jRqH84izw77+TtnwzwBUqnKrRTUF2euu+aa7on0ThJLOJg/U8jmOW8nsMfkW+ro8yeczxaa1HE+qo4hDdKZ9on54FS41Er6qQJy4JIwcTuVqHJ3sQOcbY5VtINWCagvGblOnt3V3ZEWUhjHwOR5t1x56QVYTXC0lsLF0MoSBVgX8zGxWW2uEC4LtD+WBf1q1J2Zd7MEliJdFM901zctHLASyaOk7M/EJgbMzC77hACa4TZiVgBajhtUt5chJ0Yw5S2mktyxgoFxg/IQLqtCCwZudDEjuAVgoYwkOzTK9CS2kNn+8GJRHV65p1EU46fA4Bn9BpBoh6TUSezQL673omtgOlPJqy8MPTbMsviyjZOdfq9My4EJ/UzzVS0HMQzChMikGCxAneVPc9rGN8o/LCw+ouYyaXYcQ5pbBvV6SGn5vp+hB5YRod3UJJ0Dig3vIv2z+N5XUCLUuIn2Ga+A95svDuFKaCmMr88JuLJNm72QuobbKT1dt8Dmn29P4shr9eqU0hr7ci8ix8EvP4uyDu2ML40V5+g8o1RsSM15BCSyGL2rHVK3Ou78YKip6otV26XtMYvtJxwRJ+Xb0NIs/Ubk8LR14ZdevZdP2fpDupAEdZQ75ScRUwQM0mrDUN99jwLK4N80txmK80JeitPrHoIkUETGA1iGjJ6fq+6Xs7+N+33kEk+ZuOge+/RJx5OiE/HwosR/98la4iYrS11stu+vvLxYJGRq27ABh5sfENk2PBdGGKWMWANKP9nWmZe9fno+Wc8EJ0qBhxq/gDHxleKzdsfdEyW0zKj8RYyu3hDwTtwvoX+uXMY9VVvVjWIIdvWjnxp+ngX4fMK+kCfA6vwpdBIIPzBkDL+zAqcuQyWn+rUSfZdwYde0OWEwMn9jpMjNkJhmamTQwyN5mRrop7Rui2X93Ve+i00ncnRAZE0NUSA7YsrwoTi40iPcOfRbiNFkfdDf8KAtcbabONSW6H9kdJvu+QWmgkPSAa4RW0f20seFXM4w4vnG9gF0jL1fEKcy84x6T4AveS4N5Q+cGH7ZEXEmkjKqtTY+nlleuY87nuIYJjyAJKrq2tbVR2uVvBzJsMBc8BTY/a0tXtBiEs1kfxVb17Fn33OAwT8MUbxH3fNY59941Zcl3Bsx5dzeCOzoSXHxJXBKpTwBCyAEVCJtRBidWbY9V3iFO3zGFfme6ff4QhzCfbkGgI+kuBJxe0N3iRUl+MYdoYnywb0GUEm/6KGgtV6orjQWejUGgPP3Hg335iwGGqhfV/xUX+5JwwFImgEGYp1iSLIABXaBcIf2Ohx+xdwVRvNEBhc+egrHmkHAsWzRiNbtfAJ/m8PkQimyd2vF2aDsx4Yd/Th7Sol1GDPvexX6IgMDClFQSdwYS8E6v6jjdusZkRczIkGcXA0nMI2jG02t/2YujHXQtgVOTcmgTaB28xGjKaNU2hMydpp4qF9Dl3zY6sLxxHVsKsO0iZljr3KGkz20kfslv0jHACzwJWSSNBsFRX0H1Y0yKvs1RS8vbNp7V4dR6FpJsH9v46klERL405L1MnqETBGmYSEo/XXAdYWvsE9SUun2vStwS/QQRR+PEsvJiwCOr0wOzzP368mnx8/qO/J2PwrOmggEfr5QWrFOjMzHfqPaQSAKpGA4hULC/huQm5j34LNZa5ccRXW+SaDkmC/g8gXqTyNX+MKI0hS4399A/ZsdUDwV86uPYnp3UzQG1OPZxwOGbzjPhVmpa0h4cB2MN6UnwqY73L31IT6mZfhKRUa/FSmnXBpj7AeoZSjF49PV1MZ6vaxn9ZXkTpf80OxDGGS1PyopfI/dSmhqsohKVIe4+gbrz+AUroTNbkPTuGBcEHkRnioadHAyTroquLJIXcVorshQCAgHANdXfdRgoldVYZog9gW7+bibsFUTpMcFQSYepiCU6ux6e/b4wk7slk4zHXQC+echefcaTl1wkEc5/ZCKdEmC8veIwFCZMK4rvIoTXcjOAUJaLmknUIjcDQpSfLL+9Qbh+oU2GYTsdL6nKv//jujB5lpUJN3+ppL2EVAWW+G656wGYGrbYMaMdJK3jOsGf9IwMlEOCeWjCj9EOXAPYnC2L3sLnEmjihkdTH9/gWhHR3GavmhwRyoHioCrjDCKivrIHwem+5+C7srp6/ghxZdCidlBcXetS3OKus2pj4W0dYLqw18w8jr/cIfs/KGfb+Z1jhkB9kXv+qq4rigpYpWhG3EdGx4fOIPY1PIzf6A2TgWnAJDVgHnKduIBy34hOh3rfoaMykDJLlLQP99EhyFxesnW4MqhakOu8uZlM3pmZCKWjXxEq3b7gcxIY+TJgywmWxutY6qLxiQW+qOnDFkVXGX7xiYV6CHQ629or14XhT1SzchQycI/NCQe9jE+iBwxUm2xK8qI+KsMLwGXQgF+iBy4N2D7Be4HlylmIK5YHKHh7x7g9aPQfq2VRSHrQxUTv/S4FKiAngbZizwiVIrR+ZtQ96HdZn3lXYKS9UfcciSipsbrMXPIkCwb+M+K1j+0yIYmITz5haAT0I5gAVEpuTPtIXHR2IfE6+2eWg6hWUUR1rLDi5t6zPjvdN0WohAh7y0l47ZSliCR55x67o6rzd36Xi6BfvlJocERTw1HhWFSy/grCOoHwKxSJs9+Hh5fLpw6Ny8b+iV8xUg9fmaMu5bV4mUaf4NsyXlCCnp/C4z+pD4EA0izAnoikO08bZhM3UGhzrY50VyfbU80LGpxR6f8LXsY1OgoH9tPV1yifq+OVbxd5aI1K96D6jifqaaEr7OSOgdvQgF5f1OYm6y3RliuwIsZaRzf+m5cf6zDv/yfmZcCWhvCVPwoCkhykOA2VohirkCqTb11rBaYGzAk8/Nj224Tu4i9FBkF7okDstasVG1ajUHS3E2lmZBZcsZyAfOTEaBMcvW5aIBtrhyVqm7D+pWdKiII7kwweaBfgJu66ZrIfIlfFDDVLOAezaRVhXDnD+xZi2eiIfArVljkTsnWKexOhbY/Z2isuUDgDuV0aAEHms2U5C9rxNL8RB68NXpKyfiuh81AVLReIrsqjFph0lYBjQt1NigPfbxtWRh/PuSQZjWfZg0GY12Ars5VTXBm/hT5ZGDTM40KQb/Q3G9NXVJm0TU29nn9ev2bZHzbi1zh17BeLur7pXMZ8BTBpwj9Tkl/Dmn8R3pe51oVWyttrVtT406UcBViWM3k5zeGLHOoXaGeiFbfFBbFqMvlbGEg1EJrqDZvfknrVgSQhQCcXrqP60TfkilB8E2Lx6oqVbWDGaIt8LpkHnQnfpcZ5QNBTwMqcE2XclewS4zVxQRmZIkd0LjdWQIWj9PJfnLAUEPrbolbB86isAoUcMRymc1UUKekVbYHvvdTeBor2VIJSGOGsrC/p2XJ7/ZR96XTXshtxMGA38/KUKHOTqZLsNkRyYffMfE5ORTYY5bL+9nMD4hXsL1Tuo2/UF9m2lXShS2qoHDCJUAZuovfv679CT2kc1M1MG4f0RJsW+wWssNvtO/0EYuzTciQ7Z4aI+mIOkQa+7gJDCoDSNyShox0DEAqezvuHWBT6tG/E69pwbPp1Fn1m4EgjbsjLJVR/rKXwZfr/IlBKTVsPZaOE/XHVvrFSz3UB/aOb/NRglJYFbgUQGBYQApbsqFwUJufTxNLKkn6uMqOP1sUXs6PRDUiqkJR/4kR2r5ftfLFTd6QOh/ExgSNU8Mf+ZOmzRf7zXBb4I5dyEzRBh9crEUE+4ILvVA/TugkS4WdISMLLU0x9vCxVpPNm4OW+HO3qZoz3dO/DD4EjErpqllmRL0stmLZazHcdm9zBL0UBpxRBIRbNUKL1x2NiScIuiMO2BfLaTDyzwf6aUnMNIvvNIL2N4cLC5Y/t+GWyYCUwNfhEYkkHEaNcM/AmykjRESSbIx26ZQgfj4MA646uo215ASWVCG1rmvMU9bIFDy3hfveHMteWO7DKh5U1EEfu4CP4xp4Q736886ydfx7t/0sSu2Xtzot2Hd4xUcRQ8krMo+bpRzxtiEPzG5Y+nZha2L1JR+PbOyLAqwluaS7gkMituAvBzVSX7AZFqHwbj1zRkoFPS/0W5EvA8Y8Gqbf5QQ/H45dvoM+XqLElBoM+4K396oYebgnQUgUL6dgY4XmgIsHCnv/lQrrvn8THsZpzrshHJrBHqSpc3K6biugWrirCq59Qqryt9jIBjFks7wRZXFoI5vMiXJ+SE3K/OOh9P68rgAs/vXtei9oaiTUzDv8LrH/4oVDJDTTi9I4aJyrEafmqsj3a26/m9+Rv7U3PVgQ8rhlCtouY+5bMT1GHYKYiY8QwAJg3LedVgIsNvdkoSRQuSZupQqUg7wJNbVZfOPbdeoMr1N56TEBvllFbyz61uapXjTsMHjt4/89ya3sZuH5Nqu4B8LJGQyZqbC8ZgKJb3AErI16sak+SnfGtXTg4Y9IKGCxX8yGBBK0HFIH4ctgsmjabwMVZ9NTMX+0dIX0zBpg7ZHHEAhPwtBI3CKnx9llIA7Wd1uBzybkeF5CaRE05yIGX4F9UkLVPRYUQrPg4A+8nq2z+ZeTSEtryzFo+ZwdcrNTnK+HknzJ+kj4c2eYbRhYdAQRnKdh8q/c5POIbZ6fKLrqZnN9O2PbqwhOhpQGYLvZpiHdhbS1tgywwuHHyYiMwAhJmyHLUPnra3OEW9fm8RsrvEJcajA5cOWmdWl1MjxvUrtGyB+Dt86ovZt6qjfYssGuRkTS+LR+Jz3LgwQ4+Y2n7B6vTyMHArb2Sr25GRS3We49y4M5kxtx8weDNjR890IMbwHdlfycQF9HadnKxC7FtKZ3IKNZ4CeuF7FQdqGr9XhtYQYFcpBB3qBtxuX3hH4YC3YFCVW2WlWvClRZALiBsTSYkTbde2Zt2evOgWxknQ9MUlmlQB6W47HfSL4WMelHt9L5sQaXD/YjopBE37BckgY1nq0gxBBtUuRP3AxOAL+br8VtvtcBZzIXTi8QLfVtUrHwtBsOgtATBL+tahsd/chUh+9fCEO99gvirbZI2BWZhySyimFgYLWJPTDTBcZuhTBF9fTr+7NwC3odv1wvVZvmt7G90aBf5Tbq3s8yst+lVRkWBi4T+8ig8iUi2qFHOoNkxy/QVVeXK1slYiyLjJd0t0aeWqSpjAMoLORMOFdWZh7NJgo3HLeL0nqi0+xX/M39368/+7WSweQT3YTg6L9ktGzJbvs8l0HZGbi7klgcMbk4XuBFoYYfOfMN2aIEY6IkdjGTJhfJLM0qKadDrm96qT0XqlIuopTiT8LRW3kV+/XDReuXrxm8NZQ89ofKzeCs7cOzxCR2NUb0Bh30Ok1TFBL3zkod45IJYr4O8XD+qa8qrYA/UMm9ipDvEZ8n4EkL2vHgDdo7WqxAxUQPuf4e4Ld3JCEu533W1M9VM3mzddsriDhv7nqsj53GinlbLDDvIWawYqpESeItRAm1om7NoOU6o5e5BMDF7E97NEjgtbBV5POU3a9tBDXeiS6vdM0KobcKt8qrJgTp88l0+cs9QEnmSXp3fOj3l396seIdgd0W4NpvnRFXGfFJs4c6gJk3pXsv/rPZ4M+/q9XllhNNxr/7D9mhkL8XcX7HPCuAtVq4MGLS8zcbvXnHIJBJLf7FU+AZtdF9T0CIk94nUpAe0TXndONUtwhV4OO6ooKe0AMd+LO3ozMFiglB/L5hGlbARZxQgTuEjcPYwQSvxu6McjSmkEdnaLelXM+J9AuxDg1kxp1XtaMGW2nD+oQOJuqTxOKFgXMBLEkwjpo78Vmp4IqTtUZOVSFXseMwn19QrEyixaoudeIPefpTblq9kBr4PQykwm3dXhWxqdlNEnHVA6TUF/BR+NcMnaVCrpzgc8OWPBo8h3Uhr/4QA399wDfrsrzf17mtermJ38VSV8jnXi5sfFTxOg3Z49YkEQP7YEjBHL3MKbkr0XlvONSSAC8L1IKdnIp8Veq0PGJ/shZGu4t9KIg+88HEnNHfSKqGkZ3Eih5MMwUl55pBdjPIDIJ1cBFrgtBvULl7bZmPw5qW+qpGT3WLuXCBqUAz6tsfsTnaTh/G/JsiQxSaXargPqk7ToNYx7McF9zLpV+eH+JLy4HH1TxpPitWe74dvukYIW80Zad/81hekp4Q0x3uInB2QQse2vSg2mVu1FoL+EcyU/eZG9SUjZjTRrYGlYw9QU/JWtkzknnLXmFfRO4mEaegmqJqfp54fgB1VJrbKXC13z0DMpcRl4ByVGqvOEHQd8KiBZ5fZLwjUooC7WW1Sx2vZWynIK3OalqUiVmucYMEjCa5HPPYCJeLLhUT/lAbO7P6OFB4tEYAnDUGR3Et4jFAkyi39uVegDWhoBLLzv2sZ5JMZbIo7XJpvTxsaFLS68w6hDVl/RLZzo1uP2L77ZJWziNmt7B0f0Oj41uL7UghSrNmFe5FOFjk+3Eqw51G6JjBQgGdZraAdywEYSnPMx3RDaa6XdgOFv++seMTfk24AvtWNiWrXyptyj/1u8FJk7Ebv9aiXuV3yBdW8gMvWW6Iuc3b/GK4hnxamEYicwB9Hkw3FgqzBWJImxK4H018BEm4JHa0Sv1gBmHdmvRTbsdLe/Zubrnf5cglS7RHaa1YprdDt/svvnfG2wKrpd4K0AiZij5qCXgZqhYDWFfd0aqA2cGcZ2iTKzjjBzVxsg+Iz+9pB3j3G8pqk/isxz1av87AMLnlFj74TXwj0z7AM4ey52d1Dcu/PuqDKWgWJpOgPjYy7gTVows0bELmmPQIzsYagrnjI4c1CqySqKF7lrR/qbH2PybbAAEAekHt8bxUq/AbB8bT2AkKw6ZQZdVRq0/yo/lXH+R6cZ7PzwPqPAAZqmMoBasxrbQJszRbX1/WwzHQQL0yA3z4p8V4UnYwG+NVoRPGQNE0Xhdpg/vM9EYzsmNA6TdUgk4WxBrMGFXaoVr+nvyvm0XhzgEACNT1VQcxF/shmSkjaQtEDmUSUb3N2xuz5RvIp9ecrR94d4jp4uaAnnR9ZjNgsr7K3OfIG+ka+GGiNHpF71Z6HUNFkqYSNt4p0P383XpYfSwjoLtMszImus/i+0sesvC8uL1z5grYTyRGMZPOwdVRoIoxciXorXo5BvEzBYqMaOTRNmewqRwq9I1AF9pF/+JzU7GQwEgXWvNzmiUf8bzEa6mgSnEYy7Hd6PnO933UMsxZOTYOA/Wq29krTGFKY8LbLiofvXFXAA8Edy2DJ/zUyHz+PpmDSKO8Axx8y+MLfFITQ1wBGJNhAeD2Q0bKoSmLGtzfouON1Jm9HdF4hS5dj/vQYEKFEi2mez8CfFFKQtxKXvotiL/V18Rlrsj5gnrC3VR9tTsflpuNLQ9WQO9ahr/aPSKdVd7T8zntzEpsT/UCTFtMjzuoKKDhg2sEHuy+4PUEjx1aExd7aKflCxX7thWIX7lkqqzeHdqtMYECkm2kch4zMUyzJ1FbAxUjL8IchKKYRDy8fs9NkkPB15xWfTTufI/9/toQZz8EtPEfVPIbTQ/guBPM1MInRVXWJWwcwRKfrTK1OvgcHgH3zBcEx6kuQsNbKJT/ZBhtFey4mGoNecqVd/I92Qqe9hAYbYr1LAxvUyiDndbi2QF/AxaRwcH5kppK1Ros4H+D7/04qh6izB4e0dyqdpHAwYupmP3NK++h2al+EAMQv0lMMgrCkESa2JCPCUhD2nYAvtvR1EcpKJB592rmpcLkb+cBYeIMsCnlC7idan7aXlVvQs//sKoKTLgESZfeEZ6IWD7gGOlv9u7K9Kjyg0LVcfpV3HNaxhR9IrNTqAJk3/oAaRJ03f2t1L6egrKlf398fSnVj0Q0Aj6Sf1yT67VvkOrTxgPpz2/XZ3PBM05lhiEvy42UbWjZQlaN3JuStuUOXPGVTmbGbqT9ioq0XprQk7J8dSuaquZdQklZaeAMpw0PGe1XoWS1btYwhpxprym4NHSkLrM37b91Npi9yF1yUA+/L/T2qsMqtiOlTTlrh7RmeYiyt5/2GLIY810tetV2B/lCRYGtGXGdZf3U/WtQgAgisrXnLBblX4sigCt4z7A1kPFTs8HjnD8Fjt1ZBWRrOjDsHdp5G8tfX0MtBpn67KFY0oUoTTVh7UPfARTQt0rkC/XllqxJIo8YJg0QjcUXfTpUSgPvc12JjRjH7VSK1k5DLMAJLis3AcQzcJLb3P7WBAvRHVrpT/XxFQEfnAI6SV7nTUmXoBNESFI20BxEsMZe3H1pTXzoh2EA313OPJqHoPcy49rnESrzl/YNtJYl5hxTqaIBqp9LG0QfajNZrQClAUH+ZlPWeeNmZm3f+gJE9Hfgcnqs/gHxyep/ruFCbMM/TKxRhMQsPdEhD+J4vbB3X2Xb0+ls7HRrlT0kuVCowBFv9ub7cQWRoVIv1rAF+zwsF+NzcbzE9/G/qPTGhWo1xWg2ru3rCcV6rGB8YcWRcWUqmwP7qOAZ0Qxx1tzIZ/O9yMVKp1LI1F36+2QkIU8NrqbrTYFXlXw7tUYh6+/VzOGzmr8lBO+cUYB+F3vD6PyLuWjL3X/NrC44qrUXuG4MgBwHxP4wR30w4AAoQUnaIPhtpdKTiNykC5qsObxqcr7YUmxBnKzRIoqFVJ847JHEkCacQrOgaJ5edidsz+8DbtY+YaEoDqiimiyt3SZQHTY6C/EoiFsM1IvpgqitnavjjIpDOW5CNrrJTycWicyy5dsmfyDeoMWXkIhXoGopengPQPtnK2BoBtDhdybw6TF3KU85UudRafzMVK4Gis7NR8ACMP+csYFr3M9D8MV+jfRxUFfpvWkmoAkYpjZhP2QAZlLaOllfG5EIU5IpddiX3UjCISEax37IK1NK/BhsD/Klj4P3UnM3sFVb4vhs2aG7FqY5+NJ4gmJRZ/HBeIMpscdxHyqih2FcmhOh50+kcp3O/ClbNESYLPBlwqI7rNYwNJID6nq7/iu0LHtBIQXu4YqLIaMRIZGUPs32glRDTWgL2tA4eb72YAR1bK0N2NJweUWln1fevFP8+RRsd+D846Fa8F0Fk7vsifwmERakkeX5mMcvA6BVyqkHyAUtRGPf5LKOKcbKzyC/oQMBBfx5xKY3HQlvyOhORfITgzNUg7W0fvi6wChj95f5C/AU+Vif4UmjrtBy5c0IVhTITcGN6WclZEsmCGCnkH35TkEUobTPGdijX3eZ65Yz3dDzWV6kof1K4HEt5LX9mMUVeI7wzKUMpiDDU3x4g+yCPxCkDE8Jk79mpXyvKGxBQScVNNz3BuwPs0V1jDLxl6IdDl9SsjzCr5IvOriVm0zpU4hI2mFTazItJmqPQki1ko/+AmgorVhNC8JJPnGt7z0XvOxws21pOorcpS2HvohwHcRJ1AzWdZuWE6ggySjw2w7Cdq/e4itsGkabapdi/OA1DAfd3d/SGaLyeU2+W/FdTp/NxPLEWx97sV5v/aarScM7wD5dfzSBfo4TDda71AvMd7WB5ceoP9iVcGgXEYBGDHnKgr1aj5QS3zAT7sYGDxrtqzv5o2Qdg5JZWbKfKDZshp61vBp1ZpFUMcLOHVbECntWby3lGpo5QrL7kkWxNGdJzw2zKSHTZQMBLU/84Gwk/YaoTROFlO/ChvJRfp9UB+ejpBqQiLjTNJwJdlQ5Uv9awLZYZklZUl07ZWgOmVeEVPiefL6717J09gzuWAlxbKWTkIyUtgyHdQdL2sexRudGSCcFaJpLToEpLtdYD0Q2pG+TIpH9mci+atm0zmGamI4P2pWhXkuI9XkCEFexISQzu10vnbLllLon8SPrEnk3kz7gSgzCikjxzqk0EMsAXNrptg/BhPOiH5wRuEmNX/RppcXOxZDw0mxHG0xxE30zPvK+8cVogYDt2nmc8rW2OuTzNWy6e0X917/NZ6r3HIPEkmJIPNIdNJsfh4dv8GPmZihfgsDd08Kf2nUzOXPFbvAhFkHJwhSlbR2AAGaY9Fdc8eEVtnbr0afKJUQlJ5L6ziJj8ktRv74its8HXHXMR0NP1dzEuybSp7SCeoGT785BREWlsxXKyvgrItJ9OCgsEgaHR8mK88WFWD7M/AvBtAUnLABywul/igba3FxvABxggS/It7pFYlE9lxnkJEB/oLBjqYO2P7G9kVwhmIgg5uozaz918Xnm5+DoV1vwxUj6mI+/2bobj3mQ4k6CZU1XoG498LJ/PJ3FWBtOcD/XXLB2Fuc4Fxc6TdRIvlRZR/JNYcc5kaI1TG9V1YLz1UylD9CBy/O66/ovwx+7Xsj7BScRL83hlYtylTT8K4CI9ow3cOfoSZ4oZ9tPtBw9x/MCQsW4yfm20hHMQjKPTlmG15yUq31q9xl7pm5lYZmTFeWjF1Up583WwSfekEXTUHPUboBp6opGa4UJrPEkTQ72dDcwQ2cJ8bJ91kbUn6srm02WKoDy7EvffOxiNIFXqaQccadO7S8iRP225dI53zTDM6hUpfGPEqEcm01giqLfsa3qK6EcOmkBfLwek5OVQQmGS3YsSiWFSV24kYs/kxBp96Gq5uLal4rpL7rzpBitmzRDMMSbbTzsitkg83bQp/ZNP07QF9EI/pxtsD5EXoxMwyNXU/M/ywSypKS0jWhyP1HeCBywtYDnOgAsSXWdS9mKjU3eW+ABUcsuwLj1ctXcgvn5TE6TjnSNcGIlk3ueHkhZudKRzmFGhkZ4UwH45AV74gv3i8lk12xZwgMm03jyZJaUypNRI6fVju+qrQgiv2mMhL/XDknySJBgz7JnwCM/hC2cy+F2HEegvX/hNAIIan7eRKZ4S/AhPd33Yl1HhZaDUatR9Q5z9inOFptMOy9m8O/tOH7Mn2DhOKwex9orwb++OlLXdWlVqPRNNoT+RGzN1E8AC1QQfRK3rkfb2Abm426TlEu96RsozACudzweAjduwG3gNxlUAmwjq0o9uhkbHGBFbwLOwJAfD/PSn8Q9zlBr0ooaNOCyOUTCyM8r2wVB4Sfz6JA3t8zSXwaeyrTwAY3UxElHRvNbbW43FvIkVEvM1n5EsddkBqDa2Lcn1T/U/3FNbFa/teBmNcCxv3Wh8fvXY7bV6qPEDqBlGkHjxpD++WgT6vuVFhNibqWJcP4GfVcEqJPguL98ZP74/S/jTQBA3eHpn2VCDCpZITP1Fs/x7qlX+AKhNoOTJ7TC56cPTEMwC/QL4BO4TI5x5bKm5vh3XDj0exjBQpH5h3N4N+X91NSDpVkVtP7GjNzAOSfrxREIpsweOzUC5EEN/S32qrHkMaD3pQ7mCaDjpp0w8RckPRSVzqke7yGk45EKdw6enoPcFfbcip7nVYIIMR+4itrOk1i0O/OE+Df4H6ZvY/BKxD3yINpKL9J3IGoq2hZfKKzOkK/P3xtjWI5AOW3bMoBGoA2fLoJgbzpDSYwvmYdi380V5VORycCw3PJRjcLEPpTWtpADfH8o2/zo+SFrbltYImchVuw+zXiOR3HE3YcTFZBrxc1ZM/DRssGG96+hUdUTAqOkgr3aLKnGKq7NsqmevUCiYkRMoHUzFrQt0RisVueF8iA1KQXxXnKaDCCXBakCZtFRMHbpCGS2p6FKE1US0PIpHMes6nUKhvubJ6R4cbbY5uJq6s78+A747f9ETep2gP4WcEj4M0reE95H1hS2kvgt1K+WnOVFHSK3jH+PJyr5Qfuwca/4hzcHB45YxbC1qXvNk+3UmWB6W+MFDpWIIPcoIIeDJdPiUqADVJpH9Sppx7eyzqQyXQeVaA98kfdIXlrfkavRcdrBnPZpd70TZVm33dkMEEuJkfJqfkwswgp6ZaYeAd+gWgzTMsOsl21CW7ejmyZM/EweYoQ+oJRJ5A9e2T4WrQroB8BOAXtt8w1AIS45NPkcyquRT9Fi/dYsAXKva7VLm37Vd6ksHT24GS6r7G5P8XUI50pvkIvSPzgRVXz9Ok3SJ7bZb904CDJwTK/KeKuEdebfI55sXu6L+YRTwekx4PGquAF9CPitqE/uA+r3VTB4Pa9JDIZmoISncU7s86mIxsixLvMQsC8ZJLCQ4ljq5zOWnQ+1n1+NmNYjShFWzNaiyq55hXQX2wTy4ZFedBuWGOmVGHM4nyQXqCWf3j9gvoEgeGV15X5+qKIEdletw05Ri2gsDtZLSEN/LOjYbyhf+CZqPmRBR0sGn9RqkZhYPPWJ9kiDmXQWf2rP4fOFLg5r/VawKzsskLrefl4j6g3DL+/yXvzdL9pQj1KD8xjR3U6a01RP9zwGNhUKGSZTI48XL+cvYM5lbQqvlCPFEitRg7TmGGrRosvJZVvH9OWH+I/b3wpuo1hXgJdxjQTG/NsWIwXStdjfnTA/PEVQeJBzwTJPmqyQHfvQLP9Myju51O4jAZAfn9P6SEBtrmHe9D04PKxkpLpyPhTo+sVplL3HyZn1Q+IWdjMpLqM3ACRyKDa7L739iIM/tmrRvbYpogIEhtZ/2Ql8W5L4cjDNcvmnlTjWn8PjdK6eA3sZA9MgA7FKTLe5TyZ9IWkke2VCohSC2HYk/pWXZJ6eqRu0rNxEX+R1AqIe9im1JVM4V1PgS/SxupgJOueLZPOeRkstFXFA4h1Ngux3Nka5ej2/QMHat49i7/lkxFV2zG67h3TojMAdq6GTiEVm6GQKg+0YOOUc308si9HFFsgqHCiASQupB8ztN8qvwyzwz6bBAiB7r6lYsPwC9AEVirsHB/oJhG/HJ0XC7Nh1qLPWPmUP9BflNATrQMEBl7+YOLMgOo0VpVwoR6ppVtlTQCS6PlIoIA9OCR0622jwlxDkCrof6a7KqA2qN1JX4TKvsFUvMn/Jo6jFgnfIgHB/1EbyV7M8TvdQfbHKz7YbV9/5Gju9PYqEs/qk9f0KuG1G4czJZbtkfM0LxlExG6q4niiWvPIX7MeGtT8oKzca8Llj6vlkoNBtGPDweDl8YbiGnzw9kSegRQ0EFq6NqesX7xyP02aOZqgVT8v5yTr0B0mSL9rH7/nq+1I0cSryLj4vfZBrax3gbsoFP9i+gToqJjBMSoVH3grh8DQydYVLsy8857HWWaMtP4uQjWda7xe0oxoxxlPvfjJsyb7Tx3+DBrCvpHKwLXiN2ZBuDGz43gmeIsfavH3L6T2QPyuSbbidCOVOW8btFL4O3HCwE4DXbwsISJQwGthAswuYrBuEHQWPG1wa4LnHXgkEgfdqtw8AV5ufEWDPBESsttgijzBwjpEoQV/nd3/dkBpubL+/wwUl3HlAHlyqYGl+Nx2Pq0DXto3I5g0FeSHTbiWXOb77+X2EeY3wAf8eiM72l5y49kYAouYMcP9BsM9DLfXdN6x1Xm8BjsoDE8rXy+6UP4POBcx59GIF/c2JjVlTmYCxja3sgwu+N7tK4DH8tDVhHDGqC4gRphTnhdtnfpEIwU5ITZ13Q3lyFeGMrRt4nJgYDKBsYeGf4ZCe6gCduyzABNOmhCuyCPdqYkZcqUONG9Y6SMKlXnz1fYP+5p/4zmBGAUDhMpJa21jKXF232nXb/JpQjCpsTVYAllXRZrhcN/HpdvB3EFNBbX2XMQDb76oYNVJb8ef2yyTa5Xz5aBhnCQLPI78jPM4QYzhkEdDK5toVdFMswu2Y1I2PXxedmfThwPaL+E5Y4QgunmtuKYwDW4PFD8FJVYVoC5eF2LQKILMllEBWSgNVva1ammZs280nZDQge0pwP0yPVTsLVsIAu3+G/nU+QdlZZQTc2ReaVyyY4XVR4I5RzxbI2GNz5PDRiGsf/KygMsIlIWy8ZSzqMhikB5YW+MA9sQ5Ic2seFRAQt+CFSof4PrQ56ayvGHPQcdn4eRwwcBX+tDcetj1UZLqwmPypoeYRl+aFCj656nhF6OQt8rPNRuTxCCCbMeBpw1koZnRPblCVWTRv8ocfI1KiwdstQtso4PzV9PGLKNna0DVTh11BhsSxv3ZMqF+JtIqdSFMrPrQ92ZPEV8avNqXaq3LzSkgPcViuzmGhl0fWS1CH+34ZIuqOqtDf3Q91k+appUl+gsxoRqAySCMn2RAubYKduJbrqffHM01zV2ARSJRd6YJDTVMgVN1I0LtCvCTwL+7A8a2HEqQM8ObTYUQp9Ides5mzNzc+n+ZjUBZFfZuM4+GyAo9DwKGMej2xpbAZFI3pZGvUl0b2W5/JvtWmGvbc6fKxrkKFeVD5og1TfAdGvnct4g3xwANfsOMSFfISpe14rwrUvMlkD5Y+foq2WQT81Mm+rJRdlbndVrY1KEgDnmZr2BBQA1AR0x9YRwMs6wsRFYNFgvUjvQhYWKnwAz7OxIU6iont9sxcrIyhRsBWTE2zue5/s8BIi0FapuixekFYNyDwfodV7G9L4+UzepgrZZE9qCeFBvBOSWCL/r6HkjNz/ioCkqN4a/k2kHEa0FvM+InQrRRAFK7JmOWHVne+/cnSgcGS31pZ8T7ZS9dCYu46a6O2rESCPgHN2TNYtXEL2jXlrbSEnwws7mFAzYXxjh7vl/VTfJfyGxqfiN8i0d+YNc2x9ftTc5p0iupDzzOlJSzRpGnIed+atvQrDJ1aX01iPtNKr6Sx4+MJ9pavtkCBiiULSGKfUTzr1LRJdFrCyCifgT4s+GGK9te5GCcaOBbU+m5CbFlajzRIFgqR5rkd5qzT/JnGcm7TZzsWPQDccCTURjJxrFEnUBnw59uEQ1r2a3NHMasceic+E7b9vZ94DLdFNZmVmXsnneFSPJdvRNdyNM5PUMLP29DJuvCrjdqVaGFZk7VEwfRVsqka1Gi/X1LuJK1/PbMueCrL38N+98N3hwQfdOEAFVQYAGUN3hBbYLCXu42IZMU+spVTtAadLdzx6eZvpGJuFg5acCfcXP3KYzy4+05Udc/WwIgAygCSQvzoGrA/rAJeCuaqmJoQsWhOpWyw4s28dEj4pyvHYUci6gRr0KCDj0IR13laLZrm0sRc0mo/7YJHURfCW2SphMG1p2MxsMIfCfdm056dHoP2wTEGaHBVZwGjjwiE/CDmJTkrqU8yo9KD+vNuSQfPc+TfrKI+QNCQeRitMGzLAo+oJWpRxLvl+JGd3yBHKe1kC1RxMNE6MvIp1r55APfZ7vL42ninIAVtAf84OosFV6EgiH4QC9yWeHALlh3u7nz9Y95uZpGQ3O6uqkPgUgb83yWF8Cw4jDsxArnUyNcaOGPQZ5K+yGProQqrEbUOfFfRjoX/+LBj/lasXT+9hdKlQXNavwhOKhq7Bi+P9iUOAAvHNOwlg/doErx2Ogru5TquYFy6k6Zw1AAVDHumfEp85evGVehA4U8vQN93VJm3a5ejz5zFW2uwFK5UQipw+DaXFhFQNFVWnrZFQK2/PuqX/T5SSM/mQnpBWhQqVqT66MOoQ/VWa9P8c0lEEMzunV+qPXGSkVQ8lQ3yFOS7yffp/Hm6xhqBaz28eqIGbzmCN6TkeJj6dAuqAbRn5YKSz7mNOprn0C+zOyLX6ad/HPUIIfrLJAQqMNVjOAL7AlyZaYiwyni599XK8SFCmZuV5JqAZfiPQqzSxyAVF4qJXgsteDXr0nsFBik5Dh1feXJreUZl7gNpELdeWPgRY9tV5zhVCkHCvrgIfEGzIGcHrOz3VUDbuWQCuA508iNvQZNY59HfBSf8V04oXuaQbgeTERtI6sC73ELAnAbljOfHT2+oeTyBKZRPy+9LPB9SgbAhw6pOe54Es0x7YlJytVmq18LfPL81/k4pA7gH6on0Qkd7gMuTVSHYpq0cwH505wbnQNL06vhUdYHiGaIkQvAen5J8hQVMfSWQhflF5X4NeHKnX4eGDij+OhxJgAwqap68Ded4s3eCDhJ5rX6koggP2oP4Njag9NPuHm/kf2L2aF/3L82LTSHU5BKNSj+8DYovlVrfU7fUc87rUL9IKvugoObWnhc3X0tC9/688uUX/zxcPu6ExalAAII1ntNrdbcqEEhQAHGKZimtkuD11+Fx41A/6PjEv6kOcp+IyC4AXaBdENX/yNJUbHS7cdo0OpPFX+b5NiKk39gkjBHbg+QtwSY+2YcWQYLi3DmLzDxxZasI7h4pYxAs8PVQFc+dbZG6uhUn/d0IuV0smj1KmbJbOhykyRe/VgJO00QdFC4An/4JFPEgKrzq2vw9v4+RaWOlZ8A6fAwjr2S+9AUUYcUPH167wc4/6SnfwKmJLQsLnCUG+5Kx8qLom0GGxaTyAxliB2XlCcvveX6k7dbW39u18iu+SpyZoEvkXJaU2zKrGW4rnh69K9L8tcwjLNrjBg8PurzyUZdi/lZ/G0JYRl09yJuw532oqAk12OYhLfFIgnh3ZUNoXOSLo2j5GJ95u36CtJ5W+3kjMmqIOYe0KNB+cb1qZeT9IIdaX4/fD4MHLmowMlrld5/XHuebGn6B/oR+c8JvyfoAXxPwpSDUcLsdD4yAex7d/E0qh8qUWtLyYr8E0fV7xXBqWtlesRWtc5vAR1sLAevgtwmoG5upzHXRO3bFbtRVWYsJVd5w/Xh9tz/CewGXKm5Q0EtkuNlMeqXhyEugfcACQvGfSQXm3JXZSZDD8C3ZGkpCTlCsaSuuoN1I4fjcY7q4HYGfGIVxIcezz3egDoLnBk2hfm/RcY4mnzWGKsOi54ioYb88idDTrZDHdcr/bkuX16NrKhOBHYAkpSlCn4vrI5Zpwc/L736n97Qn66uyiEoGMEovUYP2jTvPgZf9y35A5eAId53f5T/amUjWs34ulaAVQmP3x1xBhPpJndlXFtdagMhW8ijkrEyg+NwX+EhDLQ630EFQ0HHwGP6wJ6ARW+red60lhNY4Hl6RYOJOdA8NREk1+4/a01rBobFAFIL9HZ82g3ICZ6KfvsGtfhc9F1dH97frNK7v3tjW8f0MM+81d8VZZ2PxVvMecwsuqXJKqPK+36NjQUCNAjSPyZgc7kGyta+zfR7+1I3MekVkE2Cz5TyC/OSus5H5lsRRG9W1p2ksmDpqc35w0vKJh1JqnxhnAGsWJh87DIhRLu3HFw8KGgDVI5ftJrj9O07rNqa9wwRqRCNF/Lt9bHsfN4fg6rThAZjG8/z3PSW0Y+k4k/5Ox38kOuzKT0gk8m8fhyMcY+RmoUEQG00AwwmwZMAis78HNL3v0w0y2nOy6hIkf3+kKIHdD448aScPD0paVVrU8vYtkogh+ZMq1taTgRJf8MOV4MqH7oACwlnyv81yLJsfaazQjaPlF71pGhYHuzoIhxcfOAzGQUM0TqN98kURkYPncfMGfXMRA2SK1Z23Uq4LSiTFrfMABjE2zPKLYS/701+xhKvk15yPJj90ZCipUFvR5V9BcWm4vO2fyeWxYH+ulYj/9g1MEwxwbrHFkLc5gjHzOf5zYnpuFalyZWr74ZVMXyroi2y1TlYYRlBGRSyTiVSf7HePxPguOl3toaWQ94eqfG/66rEgDWCPLhv9xjNXAQ6ifSffDl42gPwijCRE2s6zUZ7EYWNgMNBpWtwxaAUmtZA5DhAIFdPf160Ydy2hOdAQbS+T6Di6Oy8o7lKcpTPuyDbiO4DwD780TfNFOD/vQ5UPjeMRv/EnIYC1niG9u1FFGtRloEexGkNewRUh6H/YW7Z1rhkIkzm52rO2K1yQ8swXeApEIn8qhWBSnsQfO77vn8R3TDv0YMc/+rfkIEODIznzfFcdHvzHmvmOnRPiq/cERfB3I9ETPEAH/HVxxO40M6UrTFIFT/icCEwfOCMLCCdmBOwYa2eWUdZHtBEX+rFUFfU6w/d8kAb83APL/ShHsV5QhDKEegBy+aF+XsheWgdj74sWnii/iCLjhX44ckxH7RjOXhjqxmcJwZLdBLaPyPGwWNnE4jyhTs1JdZsciyg0i+StpC3+ivoK9VRhL+xxv9UXNowMVTdpCwgtKUDo0LwXYIO8a8K5K1VznTEAw+AvIqN0W3wP5/cm2PjbwXSFgYxkNyU6foB31X6qaCj9Y4DrlKxqMtZNIhZMmehRcYtJX3qJQxXT45HceDwWpCsHtITFjA5LXKGkuvHD5Vkf4FlRq3zNv65/BYtvk2XCtquiIQm1rwx39pF63yBNByxtV2OdY0UHY/p4P3ADWNJh5CTNfPe4MJoRxhiEs3FkaFWYu+Q+D3PNdGnZAg6yZnhCWKMQYA3IEZui2cU3zEtJ2Ps4eltHEWi867za4aB3EuwEw2lb3bgDvISE9Aip7QSy7nRcoXgs8FIancqrr6cZdnuxBe6/GyS3l3vDvMddbQFvkmJx/rI9Cvx+JLUxYH3k4WZlgRP2C7ooRyjcQ7ymVp3XjqOiKm2vJFfbrL7v1BITT4RDN7V0PzVA39FQ0XGdqp8C1fGmTrk3ZENLFqlfrLPt7aDS2t5/5LMBeSe+3W5dt8UhWZsZ2i9Mf24usWp5p8wLYb1UIEFaopevlWZzFm3/YJvYvk7wlSNuBucBwsgdg58gt2J4Hbk3x+79ocImyrYPWPuxUsHLTYgcM29y91PegbzlpG5m6vfY4JMmhmrrrC7QfYptBo+Jk7Wbrjl9gbPClg7iQfPgVPiRgnmK0sVM0oHti0jXRUfR8x/ZEUJ9JW+JaXsqL01cnTupgtghv5EiyXlO+bh6xThzV2hKKQp36upjWo7iXi9euyuo2WGivQHAJiUq0C4GN51Fa5IH1eRI4V69hfCG2e/CFUdrd9cLUYBlm3fA45ZhfoXhPKnlIZ6jpKmk0gC/In0b3kAtd90YZmoQ4EwKf2M5oJJVC0h99+nhiVnc48otqpPJKnH4viFQopkTpyTS4waRqsRg+10trAhIcHxUHNmk0kPF+so+mzr6YYXynMp1i9+WQvwEbsjA3+5bgUJcq1+X32NK2d6UgsHQTzmDpwkDH/FUdrJAYos5A6Dkc7ftoWMVDjp1HugX/4ARkSF+mv68kaUGOkTRFGYBa36F1f32hy7RySddlcKulOKgolqayx/4yuzXM+0R/0qIig16nKQiq33tYJAAsPm1j6huN8MzocANGOI6XHerH7j9XlVEJEkoKP0a358K54/q17BJJiXoO/qhCL8ek6Ad6QQfFe15KfdI+iNSAbNJuRzGo7ydVWbmv11g30g8wcxzgGU5n+AlmvKgiAiFvRb024A3MXxU6vHRzsHcGTrXzgfTR/K+oNK13hy1wZm4npfU8zFkD6fKAk7zbZtTsWQLe1JJ08A7InWTMSSRyJnWboo94Y50nZKrXtz34VzSLdy8xO2TJ3wtLUMUCww1LyuH9gr7DnGhMpKJbfx4UySr543U6lPnJvrBXsCPZFj5QbkSNQkaHZj0i9z5SyYiu5Z/2zEz75tfc3kJ9I2cz1Q6XQ0OxOYUWx2O4fJAgxbfzAyBjEDSWqKDoWwTKBAa85UKI0wD6BiKIDUMTbU9FAi6mhmBMHtSWfk1FEH6VLqJkTyO0z+w+hQAfzKLE65UqEHJcUHZIs8FBv7qDuM2/efHF/wtUXiCpVhRdFqvPLQon6CNL8cwjiy2PzFhS2HN1nQHMoVaWrKXfu8fKV0OpniDChJD/0QQbJqn8Ws5sKOx1qJVrKXDz+v/qNCsCga1EPEm29ccsgqrzImFF/NWeuxpgRMFUVBMalIkUZhxBGZJBCU1dIDyNONinhsU0tzbzl/W2VrI5Amvsz+bOz4UvN3FFH8cMFy6KoOPuzUTiHOT7HVdHwWc+XKWZX0LFWZfWcR70kjXjugEuVYyNHWKXwyFE34SwjfW1yFDI1dXgP6CetI2Qalf9vahasgyCWcR3pFehPoTqyj6bHyr8ooa92jcCgWrRkYQM3ewIsZkrG6Ix99+RAzR2Bz6jfJpQrbenkMpKaEN8DHct0sExQfGrTqTzB4GOpShA9/uxE1Z1i5B5PohcHHseD5unEs2o2gy6RY9vefEeH0cKYDftym4czAHVAakE0hBRZ3ZRoRq5LYB07mSloYbYNVlK0HcTbWAAxco3PpxcdQ+M2fqaOe0RidWNaeJ3CWca83nv85ylklxgc0OHSxrIjtC9QhpoZRdur5eknPzzdiP7Wy0/u1VJgtfI5Uw4Xu2+EFJv52evlKlcLrTZALxYZ3kSM8Z5E/zGB21YubD+9g/3I57XcWHcQDeYJ3sY0ZUkVD3e/jpanFuRDjqf63Z4kH63Ie9YIU2CnAa3hlSrKHYconj06/EClaHC37W8O4UptOF8yxlq13g40cFWoQvLdnfM579bJVfcuUqabOSZomS1CFUgPAKkgp4tZhOo3JnqdGAn+4YgGedBpzGLF3FvcCjSi7BYU7/tvJV93SG7yRh16WpURsKnhregsVZOcpmxspEGSrP3DyDqMLw11zRFZ1Lho9cD98w9jcJJKAQzRinEJYDzw6pzdcUsgnQrMQkGiLR99sonze1XxTHjy2Rt5m4V8lpkfHG+rVS1wmlrr5xsQ4rgdoocKeqqpiSz82MNOymOQrYdkqrP08TDRO4Mv+DeF9gUZTfbvT5qSC7MxVfZjaY9hzX+7cP7xhp6Arulee8X2F9ns3CDK7t0by9gIKQ+UV9haBnT06E6gNtxliDWHL8SBtPpZMGYDm2xNmu5ZsqgYLA5jNVxMvE2Z/kS/0WGlIAR1yANWBe8pnIiO+Bif3bAwkeBvv9DIV8osgIiD8bW0OyAD7bTQ72sQPstLMrXAxkDxBAgF06/b3BHxNz3wMy8qYMv8g6fn0dCqqYYljK53+Bc74+0h+SaIoVzgJQ2iYU9ymSrXHXG7XxXCTmDPjaRFINmAtikvqgIf+DLGDHgHLjPvR163OwzYtnY55p/iyTMd6Gis2nkoRtqIQAqRpgN1LVBiorqD9qf2HCUJjzsxCXdSMG9dvqi8k+vX59R7t8QgXlNm7SLP5I1yKEdR/fii+dsbp1AlgIAwztF0su0CxhfmIc5QgAqAf9GQ31BlKWk4SB0SEvI5Y3rBct4vrlc1jWL792V4jm2IUTc90RU+C3CESXeq48jfp2Bh9GFa9vPvs5PvVC3gjbSZj5YDVuay70xpZTu2wRGJrRHxijtI8kkYhHrg1FE/l3mEXeAKQ1IY8jXlkoXIyYh3Hf5i1qd/kM5W5WkZT7kTlcPtZPjkvM8zExKzdQkvz2xAzNOgw2sU0fI1lIDowYdKbSzpcpD9R1nK/OpWbsIDYxK1LxS9ypw+yJ9tKb+4BDltV8Q0OycBJQIZ0w8otQaApLvjs/aPtMt+ZPxnOE0O/Io3GpaRH5KXRiEDEsVfZHLHns6VrWq7xaBIEeh6dz7uUPPYzB1bpmHDLhJeLJvEPIQFAS2J/m461oEU6x8mmte+mr14FbY6RVRd8VzQiVWF1iQYvKSeRHPiewImwCqWHBhnYl1nZ1g3I/A0q5coVLyOGQwPItrtYqCCJCH4BiD3jR/RMfmjZj8Xlq7Cp01otqImP8JfV9B2wTfvU1eUPDCG112hnVWZyVq38QBGOHqVAze0QHGsj8jSyTAz7AhdMgwN+TU7oj5HtXmQzak+5/ZTBcdU9yVbeTF4qP/P1ALqfVNSfzJQS6waikNns9tBhIP73Ltw+ysEn/KvNVisp6Gk7xlValpkdZGUgUUIGFtEgTLBVrQbdr1fgvCMrsdf7Cqx4vpo9LfPxi+7baVzgzefyVWBFySZ71kcM6TbjhHtdIlwQvtrDNLWWw2eRs9RA+PDqQP2DeYDNpVgLie+PIRtTHgf3JPbPgngXbr0NwSZQrokT6rEMSVRvXA6AxatWACQ9exiW+wIkv8OmnX83kni5yXgU40mhcNSCmXvMCkpDlSaHI+/lKhw2hJmA+66loWazj4IJyouIKIKJep6QKihAqx2IVl7fJZg6ojYlhmAe6RDLkqkasT2K8aTbAVQ9NrNeIvMKrCF18quVzXIPZhKOD42FPu77rUnuJrAV8/YjIfQPrtQEImq+JTjX4zxjwcI0TcELXaoRfsZ1XVcPL9yDL70eR6+bMJsR0vggYceBK34V8czWXF2QrWz3gir6FXtzcKCikUBz11MpsHs+X8O/CblD7ky+NmOS5TS7E7Rf1MmrNrkNdhPVcdnKTXSRTJgTcgxp2zCR02d64VYvaLRsfMNymKSOHY2e/pqo+8Nb8PPal4x7LG3A1oL+tA45fv/6YL33e49cedk2lePxAE53nzEK3MaczNqhshjIFu9katvEklk9uIW9gh+mAmyxcCSJjGj8cokQM7z0O8HvD2Am1YMuOouLwmdz2qUVXXTIxbrLcByR0yzQR0pwhwDtQsDdyrssaqceXqHaV4xxwlPVGIQlp6OQcMrCwbXbgwM3Oeff72Ho7pr4ynmuPl3MSXY8ulG6ufvoGeAfyEeLSfoqMljWq1rWPW9XKIgwtdeGt+fLJl0W0uEgWsAdCApzlA2dtCzm4G1hBANCd4LRROTPc5K7g7MMxg2TJdGLh4qDGUS0k42lywZfJz1+/m8fsot7Y46yLOXB2ZO306aJZt3d5BYQhIQJmraOhxnrsc0CdoguiRJwytShvuP2U505+UGVwOxViEaTqh1NtfKeAWCsbfHfaDhdxzc4EIdQqLXTIafSzAHCfkv1zjAds2/QET0dSDksSxB9BY0Pq0PyBwOOOEZFSrk1EowGET7Je5tAiYT1SbIBKqUDsVR3DwZK6oCcs5Y7h74zRd/67BFi3SZW0lHr7kBigvuuLA88bx8GBRe7G7Om9COKj3Blfhsws9LhVw6H9gFZyNU+mpanRvltqk6XgGzDnl3VIoX5Vzfn1S/HBcl3TmCRXv7aNTFGqoqEjDziiz8f0GBlcxcY+/c5Lo5brJ/TX9+chkaDcXsywLC+lm1AoQyUvHW6lIs3HUGOv9FWHBFm3sQQLyYltmX/SCx8tITmzkeTaDvP8YDhtDE9xGMsgnzU9aAsSIerpAWCBnEwty6KPjTrcG7BKZ3eawcnx52Xy5ocKPLSfghtRNnDdgRP5fBxXE7Y29AKafHY2S3GglwYqUkdLHCtOHuzhbJGi9R5w0ZkF6X2szsJ7ym0ieF35vMqK+86lGEhGRB5ToKrHLIMzCRWnJ46MOLE/f+M6Ssgq2ofYT3I2rdsiGYKHjce43KnTzDHMUh+VWUEhGwNTvH5fDnH8ts4mphq85K2ewW/UluaHIfHy/B0ikV8YkvaZHGcm9TFWDFqjjxcIkjOGhNlGMIxV8P1IzoB758PYpvCdFXM7eHih5x1PyIyT8/kM4HDP3PGXe7uR5IuIAOZsFsp4GDksfdTJLTd3f0A0lvEoS35iIfxOBH7nGxBhU9QBv3J/Ft5s5jgPjddovd6i20TjwPdbwvvXdHcZfRSEXEJAaiMKXa3h4+sC570E6r99giLUbqaV7IrqdalRaZwomz/OI41e3A4bpzDQAQ2qSFcLXsO3YXjGggsYK4wgkMohj2m7/4XGRNNshorI8vwGynGNwl113heSWVW8eWW9vL3NvyMMKDNXyuOcENc8lNrvK1fLcadgnufI9vT4x7KHekb8HAiKfNeMA/17JhUxUBYjx7EpKL+slfJixNK52Skbs/BLoG2ISLhWtQSh4VD6K77wjcK5UzqHZo0RqqS4x0BI5lxH6gkMRQRRguAgrgjX9KbKmUel9zPXMsb4P7xbdH7TWi9Enx3o/cxmzFbvUeVAhKBYL2lj/aPb8w73+iVSEq4T4hrAnxp/teg7FWP3iRTjWJBQIr0oPj5zAeC7UxCImnyk5DGL9iOY0tlU7mRtDXZbe0b1MLCi8E4WPIBBJrhAP+At10oGOa81W+f4bTuQvIm26pmqHFm8mNn9MhGc3b0cAQpQAs01E4BlHc3WRtYnNSm9RzXqIRO77KeWXc6UydHKNt2zYLcJUq5MGIcciqdVAmn4oZcZ9+FYcHRZnmvNW1OE5n0u/Ig50HQkloQK2CbdIq+v7URzgV7pDhNYRqOowL+gFABHKGj9PnngjTUZUjIJbxdN9HpAdtEasYO/eUxIejB4XQiyxh06achiltHzEifgOZLI+RE+1UfBNpA2qBaOAtBrAFKHoSPt6U/5gy7YFRkJuHDyi86270X3fe2LhaiKbLLot6Y00S49gO1NPucttaA33WLJ3aO0HA2KEmCFMHyOyM07OaT+7gp5k62PQh7SYvJBpynD4Z65UqGnd0OZ2JScNXYuuq1wN+HOTkenYG2Xp7PTDnTSxx7LiqDfp9v1+un8oEhvkNi3NaM+1XMGBeNjHDew9yvFUw2iCKnkLfJ2S5oU3YpHds5P4OEsUxr0e0ZFv7PHLVD8Gg+SDUv1Q1/6XrCR4wpexB71PG+VmnGslC7QGQtfIM8sAsALDiC6H0RMVt0fMkX1M4w8l8qAAt5yd1EwuFRIwGnRzGP77HEFyxQm1LOyZdlas99wspTc4SwRUfbJ6NTw+g3NnarXE0qqQ+P3jUP4ZNwQo4Z1ctX7INIv4KqAb2NZbngbEmYYu6yNMiWNHPRPjNg/gL4DP0uOqcKUd32adRm+ZwJPfMWrHl6+7u2SwktvZkdvR76EL1d+lyWHWrw/vvBNSrpUG4cugO4AIwyaEVaxHqXT2aHxNfsrqtvqabaHwAE/FOjUTtUekTJDoCF1qYWUAtxdwiRmnAbaYAbILqRWuUCb9Ie4wDgiO3CIPhbqq9nGjNFYrbmP5lvj3IH0ieawLMbidTHpar0OVjeXbB7ISdxE7bF484Fg69k0yCTeGBrvOzw3TE+P0IHkFt7zCVJ9QACKQ9M2gXTrwaxas2szFtgPeyNOHkoG/Svj44nsWVnBmO/bws8MqY/YlHD5Afly+6ib2KUfosXHepg9VW4n8smeB76gTaNfZ4K0YNfOCkHGk98xwp6lY8aB2qPaJSXB8cxbh/m47hjDcGNP1WlwZnNTny+DHX2eB7Zpwj1SpYoZY2e2xX5YpBxN5+owPSMN7yFYJfOhZpPzAVLvWfVgPsk+FD8TdUiChpvpwBRy0glkChYn+PBCp/+wXc7mJhsv3/IUTLtjv5+yg1ktzke2WSv7bg1yLigm/WdC6fWljCGXFxBR+Mky5xcvUqWof9BwCaAzpH7ONR8D4Hfp87fTkcN9AbIyKX18rQKbHfFuvfEjH5EQvEH2NIcQqAOYA/uPqSWzUWIYlJIbStuzqLBQoz9hU/JJKXRvzqzqkaUG+40LMMSA4CBQVl6/mlyrzC5Jv4Jftx2ZiKh/djR2uMEJVrFaxJVUBA/Ye2rRvtlX/0nX31bfb+RbyTjUGjTerv4XYczBGGwptm/r8GDqFBF2nI5aUQ3PQ5IsC7CagmW4HXP4rLxtx07EmE0iQjke6spaE/wlWOJ6u268hJquz+fJkyxYdC/giHmRfwL6k+q0RRVB7TkN/ZA40Owb3RCwbzMtOCWWxaj19iwKPSA34Pp3XXa+nXaupYua4kOemz37eUXkKp0ME8lBfeaKxY8ELIQABM1HA6doH/iQ22uZARPCR0dNMPYWyEC9xPBFfaDmFHu/s0tqx3PXNpWgPye1wWEkG3/NDamO870GcVp2XZPcA8QRcupDcXer+EJiUcN2rz8vQ5PM8RZiAw31gQKZ5+cFAqgj+IpzKFqntNpH2ZnZGAbwSPnKThFf0PbkGrFyTbxp+JxaR2jrUbVp9lM8VEL98m84zCKQjzvror8HyjiTezn7S20xTgl8JA8r8pv64u6GJPMW9BhkqcSOYmkK5MDUEGcEKh+kYedrEDv1EqhgvQUXz8OiowtkzXHBc9yJs00sASxMUBZXEAXqEZSFi8C+ELgfl8kpGvJxNjzkd7cglZz7jW8F0JiR+YCEjAwoh1rO2yAiXuHslP6gRrAXZUR+uRddxHkA+RXt4MnKqADcjfht0IA17OUZf0EAMVWJ7KGj6+fii4cXTNuzDgBocybMTqo6mOMHbJ/GpYf3xSKA3WgVVbaRmli7AJ3tQDTpcweAXes72qq2l4rqTMOVvtH+Jtpvzzc+/p0T3Vm5zcTL0ERGnlbGGngDs3qWs53vIfxjFZ3/f6LtTfSJTnrFhOblIWkm4WPT6pnWdMBbWUhsHG3LKV9ovmT75ltDAbARIOVSD7ZYUsLMFkx6FSbDKZZ1o9NU5nqhztKG19l2Hdgc22qCfMM/SY/1icIKJ+ZfrTydaJV0UMor/hV/Nh5rAofkgMBu/5n4yUYgxWegS34GMuwj/UxPZvRHGFmwvscPPstFLiI556EXG/bkcbCClDHlVfTSzQYLtvJ92xMB5bxwEMAanTUayRpADRnRs7O7io74++8aipYh93FrV3iVeQYlMuaFjTtXMCF0CyXcWiu5SxmuTWALAQvFBX5XVKS3ry2A1rMJphskITX7YTqw4Sn+LlnwPFxMaZK0uvvf8wL0Awih7Q4oddI3atQBGAUMFueLIGPBoBMZRnbKVhJ3YHBhun2gGrA7IjHX8ZikVxOmFYEK7LhaCiR21pzvE8OTLka5c16Sh3SZaxfC5ZtZcqhMHGG5jrvH3fv/mwTiDPlF/P40anIZThxIF0hmuMRt+cnFkEtvocLZ4Rhy3koMHoxyH8A0E2aHxj16l97rBaqfetvXOwckwIp68/UIDsZlx6n9JFvHodI23Ei6CGgB5V0FbhKLDuAHcMJYq5yfWIFd9IxW4nSQuZYkqwAXGYO7WxYxTHVGRdlAONlWC1aaXB5zgCDamYzHbRYJVXcLRh3G2AAD6WOZdUMAvW7reB2uBQtPci6pz7STWafTMgTv6DwwV4ePqVKOBB/PnIRpGXtjHyLgoEfJyWnRxK5sFwpF5s46R1TPvZe37BOCro+Jcz/2Zeec8wn39DphOc1bDMTaqWm7JmafwryK3KhWNf/q62/VUcqFGi4AvuQHhkUWentYqcBP/Dae8lgl9uuD3uFjHSGiCO+UVnREE6O8RcFMsb6lkDTo0G4JpWvUgsOr7cOxMFDeTCEhqkewQDLvh/+yvyeWSxlJvZZa+bM1lvNNIrJj1yMpPSkKJh4hWNKbi08jhbCHnLyvj88ni9KuKurezqyyxQ8wxL3ax2mpmwRIS+05NAhKsVnrsWhPIUwFDnZa/PtNPRbAtYXI6+9H/cyYftrxdza9eBuDP6WWb8AQ7YdhZ/E46wBV8XEjOOEq8eJVHp/JGNw23unXMlZbglVC9vWNBZ0MqD+lRrj1wKLkyDDcZz1PG0hJ7yZlI++5LpWK2Hk40NzTBt0w8KtiTQtcwDXW1wrt16cxI68TkcxO9kSgYQQbwtDCZAuNtJqzSpCC/QHA/+5J1+fhW35DO7a9EefCjHSOlSxnaNo+tZ1QL/NV5sJMksKkyU+jwgEWTLqBjEFS/K17YLLmII5Eoxxfe303IsWBpzFZyb05y3FTWKDuE6gYbN2Z9Uogop8R/3i/sLHfh7zUMGTo3itC4PzRc1qgATGXrMk7eUlQm0t67khUH2vmoqDGycy6VvS62uP5VeEPcljQSFKzuSw5x73rVa66DbMUn4tYM27lqKMwjGjs6Hr9l9OxORTiWFFG4UOUkiIsbkDXr2k6z1c++2lADQqMUISK1YdVl9jivESWKJBMmOnDp9wyfqgKeZSvgor12ZsWKKS0/vlY4li0eI6+6ACsrrOl93SkK9I+iizUvauUwsJGw7RfDz5tiXdBF0ivNkdM+8ZRNHoBjfqhzb1zwl/5IxbROS8Iwr5WkKNmlLLT9Fi2PkakpQ8wk4e9soii3tpoj/U4aapfPDn2wb6ueeJFPpxaOB0etxBb9CHcU+0Zy5J6rgDtI5m8/BFJZ9QeJ5z3+uGN3+GlZSPbQw9ZGNp8NLR35oZ/Xsgm3aFmrUaOnUxS09/zI7cwf+XydfH6nMQ1aLCAB9s8j6gFsKs1eCETUNswhkj2FxZwsIHI8vjAKXRA+rMXnHStVDBZA9pfnJVTGj0x8jUOZ01rTRrlvkV+akfUVK+3gcgQ9gRXhe6ramErEWwaVCMIAFwIhvoBrZSX91Lt2s/ThXIaSu53k0pFlqvfd6+zz0BjajokApaRaFyJQe0sjrvsdK5lpnghhNyXE2drg4RqKnrG1xN+558HfPrsZUtwZgXY5pxosImeyx5SG8Hs7368nEIltxpX/Zvoo2UdJdo9P+3Xm4UxV2BEPNzZw7eJagy99y+NOJ87BnP6SixmeGQBQJzPJFlOEIErDJhaf3af+fMDUGZ8dJBxYbxSMIDHzmBEUb+HEMgF7ZF7I2zrWj+4Jttvyusevmk/wGDUIlTxPoVah46j5o2B55LVp1FKYGwkCh8WEHIX3kNrJoBavtlGDohFT3RdYF3jmyfOfstFPvPNX5f4QPL8COgL4ACbS2g3yOL0dMqQwW8zkvj2+fE1ICEEbY6gbm2zPNAk+y6AtpzbmPxklZojIiFuhJq/us1sY7Y0Fg+aTuztJ7kCHJlQ8ZeVmRMtDDQ9SSBUsXqL8y9sfKU8PR4gDddSutADvGO7gpbvOVvdZ7OAmUyVKRyhyomkr8njQ3+Rw0MNYonz1sqZN8uSYCdry8ykC9TclyTX2JCno1tk0KaCcEuYPdvdiB9Dt8tHehB87QTfgMlYVYJVjROAj0kUgV9FlJ8VQhWfSh3EhqQI/GEPJsPjqKK7Fnl5TSd5/qRM+5VvS/IGi7J3Itum8bG+v+o9RICV6swsMqi6p7QPWMIImwLlYJauYlEBDt63abzODdjY6Uu/66gLAtN/ybi8tIXdmao75TIgoAulGC3eovA78GnmXr97NV9QtlnIRDNPX/v2RflBitxRPj+6svEo44n3QuujA6dTdfR8MTw7FmSoZZG/7X5N1EmcB5Z+npB1erQhOdXFUEenB7JJyMdH4XWaV5FU00dRMl/B83r4JEFBgS2r08tku/airqt8+1Qd0l64KQ2bW723rqKPgi6wLKRitSWi2tCBjEq0hMPC6WW4e6HbpJSjgpaZYP7TwVCtIRx3BnP5/qm4r6Re/JRJFDdCYf3ttKVDUTsfGB3tpuTyoztUxBIxq3z0mnxf0Z54hztqM9Wle9VytjOKGC/cm/YKPkpwQpO0uZtoqa36JVW/tDIEOPU0LXNX8LStTNtqJRMgf5HW+VrVj/ThR1wo7UunhPGtsVHfzb8HqCpD8MHVeZx+XSFTga2b9N4Ohtli2wOun+2KveOtVNa7ZCqn5YPv35KifrNUoWtK8M2rU6mvCAFYAEyiAtMLRzneJ+y1q6Xj0+0Enry0ALNgk92bPjyJEA362cN9p0JbS0XGrX5l9YONLHuJGGTJajNjpawG/wuss0JT+EaAxIIX5fnDeTBiQTxpW/7ij4QlPHXHykOuN/jSNiDb1r5YL6HJuEncnWiSgYmlxaFbm/EIeD744oVoVmUFT7XBlT28VgFZkXj9sYaleMPnLw4W5plFVshuMVhPDWpSd+npuVj67YcCOy8QNvjlUKpwugAIiQ3OEIdb94lwlipbuU+vrSC4T+AiuosZbtQd5ODpQpVpchbEgdBLWoeGjYtnMUmsdExTtaIlGTAQXrQvdyU/Jt12GAl9RhMsUR83LGgU0Ew5Vser/p2ghzy/YaE7hkoBoshtWXYfk9OkoT4GtvlSeYGAzfHkh+gzRbcCMMBwk5Ny5cqNOCEBXwX2x6V2oA+tR7VkqWAmR84bzZSUJn70yroiW1zh6Z8tHAoIrcjhPAfEHtOlnQFGykVQQ9Vg2jh4uwcHlFojnkAlU5Ih/dNlkiLG5TdQJkU5OoXFL/NCoReHUcqXxm7Ac+J8zWNM5qOm7tNfi2hyJm44UW5jpqaXiH2ZFDG5jYPKbb8ZB2GA6/cbdhgAPBdBmksE3soX/woTaswD2g6gU+a/le+cG+Kl4YqwX3UOeC8Z3kclbhpBrhahAak3E3nwxggUF3R1/Je+XIUGqFlEuOodAjOfqrsArmZl3If5ohrcMhmbP375MUayfNe5LstLzMgG5r63pWO0b1faoUwt40Q2jnpQ6gOf4/BeFwPaSf7BFINZBV4AqnSs7bgtkdDnF68cTL0yD5tcltmqxd2W+eDFxaHbocpTeAJeBqSYIkiNQpxuKcv3nlZ3IwMw0W1PSEnA90H3J1QIpUhOxNklFsXTkx51VVwJXMg/BI2UhrGUeZowUXqUHAi6n0S0TioxFoAm1gvLlXK3k3QJTHQVUQxlxBClxpxmgxrMp5whUf6Oyao4VcT+OlJyKVS6GfnXxCluNtOMReroPq4udzxy24pjDXz5mx9BFp7zrqJCL6u7WJgi9Rwl86zqvdVrZGpu9RUeb9C+qbRCHaeLj7p/JSYaZ5oqiqfl/LASvJK+7u5nXkpSDdFBJQTU5uoWwCP/Sp6nPXU7fnpoy5LuxHfc1YlkbttJckaTOuwwCe8PzPoVRD6d1fmRbEUBGpTsz4UOCgYG2ASXC/tWv+pFLxCEi/iJvuTFozuWUT+rz1T+wxNL6VXA8IGHCPp2WTEWd2RAAVSWC4yPxr4z8Y7mHweINuedpLw+63JAXskkF8AAZkwJSLz9EMwcR6AKwMIH7UGhVA0qUY84OYBc6HCDJGoHKLrmd7A+Lo07xRC0TxQlGnA3TS/mPB0XUpRkEO8cxv00yN9KLE2UAzfWki9P5ooPQnOBB9rm9NXselU/bmmTh0RMV13SyIVLKewTcO9odxQMBxbtO8/dLX3KDSLfdjqZQ4xvZzMcK/YieRzFTR57kuNTBZBuanZxdRHS0CQU0Zq1nBpKkG2aR19r2Dofn+/TEhRjvUMrZEGP59XJG81OK32VFe3DQKnxSTWa8Szpq5eygRCgpirTxI3hEmYV+MsSAJ3U4+gACuPDQMQVmIG0KvUhGEwwssc0sqPemIc35nnQv4xEiK1/MnpBHiibHE6i+WAMxxQ/s3Zrv6XKYW+bvKj6DLQlviOG1agsL6LidkCVvF0tXSovFBzS41EnCxQ71w6TYO1dAiBleuCOm1SQjIhvNhMTerTgv8HnWrlJOSiWFBeZmvhcOnLV8yFR7bEGO6wbzAljnFK9VvJj7Bo9H36gr3D1+RrixLYl9gCFhnYp12fh75ZU07S/Gb9T65QWOLfiDjt7WHEyEPIlRMkmo12YtXDNgULUH27KExAdqX37ZnhifEcsrT9JP6dy9qgaDdn6cgnKtVR8zaGLZNS/hHrt+SCT3ob86+32c0wo705dqnZbGhmyAlqZSp7HDdY+lZSteOaI6ISSrnCiH8WWmfvw8AN48/oUO41I/UYlWJczHcIKaAPBWeqE7KPY1T+kGJtICSaj5NSX/yrk66tw6g2siX14mDtnhMOrL80SszWxJtiFoC4WxTsCKfYJArbTr5PnfTxLWAN2FeHbxjWf4V/gKyBq5hBpkBb21VMGI2gFRbejU50h2AhTa5P7Co6rq60sMVrkk7zxDagKFLAoDi3I7zkafgN5b8gyPF0ZrRpNePrAstCkcAqQ7c8xcsfWXv4kz0YHZ/pwsGHfAxFhUBn81kkMeKScSwooG1fF+RJ4Ca2dCB4i4I0EhWOQ/e6Ene67ffdyq3BvjIVuD9JOYquhzqK1TKMr+zU1+obQUH6a8IJ5XSbq0nN61d2vBvRRbJZdZm5uRXTyS0KkSfcD8EUgubP6MEro5eYLASCIwz8wXeNvkRJSFQX9wdOBlOlq/BA0G5Hu0Q+TL7aUHSizP+R7PNN9WA/grYrC6+OVmou6iBQ7nC7zo619OQz2Y8gkDU6LNSiYLU5ecgms5f2GPEuxxVmYpWENoFNyWN2vfkdhSO88b4goeuGQN6oxtKIaiWohgHZzKncWk/RVY0zHmK1EbSo+K+4QacoCQUbG4xEbE32tNHihlKJYv6KtUUkzjESud7eiHw0bDIzCYujvvn847H6CjocHKotTaDApN37zRfPj0dtrbIdzebO+S7cvsL2Z8TIGWdhyJjuA83JuT8kwjAv5xbh22XKkrsqqRfx483LuH+A+nhWDEBwL44hmSiym2ChibbEsb66nf91c571EDAPfP0k0h9IJCIzPBi7HlIhfI/r0tlJPYv1d45O3yqK+z8QuF262bLOcv81wU4muzgJ91Vhhxuagk2Q16vXfWSSa3dh7dDeqi5w27P0KcUdHznw5t1VBAXFNhDdfSafp7Gawg8xXltPW7xefGuI3EmjS86vVrT1aNC/Q5vx5jkcwmyNBGMnTMcB2/T7eftr9ZrZV52saCLcfWxFWszqaDo4K4wOtYn5/djCaN8G2fy89VaavhguY3Y1VyWCxj06mpg4jg0+6apPnlIn7zIy7vBJPAGPuTfLGGdLXsFOKunOATJSfmyf8HJTZq/scCjoB1khq4eK0ztpUax63xR40/Xv7SlKOb7MD6ucGFXJo3tCxU6l8zckzA5bboPDyi/a1gZloOj3LFj7MttKQHwqd+3tRpjwIZQAeIH/AM+LM6hHRA8k9/+23OlCC+XRwM7rf/DrxO6gmk6gn2+8fRWeRJSEQBNEDscBtibs0Djvoxt3l9MMcAF5TlRnx40FXCkD4A7zfhD1Xg9zCN1ZuLs5OcPHjfoT6Jp/bUq89UVceQd2blIyph3AK8iv119MMYOWq9tOfEsjTv9i/9hEuiRY68Xq20sW7wwLcf294+Zi5bG/A4/SlZfdfjv+YJw39H9wiDS2i1tUTzybcqvZlAXOHwvNEv1VdgSgfInxsYmu8sVzPi9hIVBX9KxhNkKPqU4TcRqyxsULzZ6kq3pY0T71cJig0DujQB/+WcWvEwObWcwQTMzG5dmRUzR6vNP7QNmLxE+Mse03+Am7qN9lRF1wr98DVri9a7ktE+hyZ1Wnx6ljH6scwLxoroSaaX2LgOiUhVB4YfivNh28EtpZ5B+UUbk93hIjQRH8q6B0jdpHfvkrhmcJpa39MZTfU95p2t+X9eNeJ6z6bzCvrQ4DuciQMUdgG5VsomSiZdPNz/DBD7rjHBqECcHvbBEpW1b/uwDGmRoLzUqnuNz1JD/u+Fp18u0Z98W+AB5azCOVgL5KlgTeb4Cq0QJh5k191zhFkywk8ZvtBIbBHyECYJPY15+XD4J3BU+va1HXYGBc+tmz7NI1T2Kk4KSl8xteFRbiVAS08MWQCiaJEo2JTi6G0paVEv00IwEcJlI3OmSak+n/HVoXXFnIypPidYSPUJ6etvlc4FrfEtIk15gTfxi1Azv+anbsXI1B3OTQE08fCe5hQGMf9Lnj0Leo9A72l/1Ib+1WxKN5adCdLoFq3Hp8BaRan3d6HLw14VFjxQ10EO3t8qLyMAzQ8LjePJBr+qO0QHkFDpVkRmCaUaHWn4vzjt/kMvegERTDjjGBBYa+lmc8x64s1ck6w3atIZtxBNzaKd908Qprn9QMoMp9AjOfnp2V4BzoEX6pRU7TeA/EyguMyz0K/rgEYocpZ1ka22JkrFDVvYuy/662gICGSPOHxgRPkl0oqPkJYe6AjYCBr31ZN0bpMT+QOxw6904sE8kFWa5kDJipH2iakF9e5wNHvyZawCf+KwhZrj0lakXtVKvS2v0WodHEHND/H4m6wK+oXTEt8L7x8GZS51H3aEQHD9fPm9kpsX+MY7M/k1IfXSctEWX/Tvh8/2V4wiIr0VU0zWo9vnVUE9JklqtccHvQxbNSqTH2fcKWOH10pKR2tHF/roUFsGuR80kolbeYXsFFmlqINdhnq6mpHSHGZ+RXl1R8eQI3HikVSXYb2ijCzJD8Pb3xQikJcv1V9PBstNK8ZumROv1ZXS0uZNCT8pkr65/EV8zdFZvTR4keeAxxIgRAjXJdDNvs7fZzhw38N/jpRpTYByhlAKnPMkaXd7KC/sNrje/5E0/ggNUaQStEi02PXkqLqxnrWJIaOqQ3Ndgtxy/w6IA4pYD2CjSZG/ToMbaUIB7NZpOprXvxzNrZiWut1OEtGh474gY4zfbEoSLeG2Ks8X4wfEjc7Ob3NN+WozNjEWbDhEjpIT9nWoGNOi9bk5vkI2G5izCu3G6ltML/clgJfqQCvHwvrT/NSiiLGrWm5A2/05LdhcanCgHUDZyDLPAE+Gx9Bf7JrhZ020MMoSIJaynkKtgpWB/1Otoxy2+uAB4JODHB2PwjkIXXSjThe8KrmWYlaaIvVKfRoHOT5IQfZYDuw12/qtJOc/szlpJCXI51L2j0LiMy387ECnPrV3Z77488TZbKrAvUhsZkctTN3MP4MHvJ4vnVKaVaysZiAgqRN6gJPmA/lOjykLfJr+zlhny4vDmIc6irzEUfVqHnTYQRDLWOvqGuv1Fl6sxFULPS8Ah3+8wuSu4PW33AgVfXaiq36eUXwsDqVNWKveQe/EG0B3n4ITUmBg85XMdi4vgrjivlqwoAKA5SEueZILn19ndaYio3VzW22LL+by+Dm3cPQAeZ7tP4TI7hd4Bq8c2R0jYa+yytF0epxael+bDQr0TEAPl3GqID9u2qAms+Z7Q/px4Xq1EpAuvpKK5kgTyADiNPbCzkuyu063ax4OXqVeUDN/zedZ7oPA/qq5GQWvNs5RNH5t+xcRx6FPoxp4FltXDajMwf7MlBoQBCL5W8uLXGg2wO46q/ZijRjp56LYN0MFYTjGMuByJwRpyFMk4mORTps66BHOAgDwq8qBIIgIzeYOZGuUEOP4HS6El5aleXTpaLTLXTE/waB1iPzk50tdCR1+i2OuIQfG1MwCsy7HtBgrrxHwM/2FEc+c52myNxv2so4TueGDB6BaRorFK+u08kFoBigCh2KSbatRU+dzKcT8E9EE5ioUePjJ2WbkXQin61u04OkM+0ilUIhWtDN9TbPJ4gyAYVyhOvHpEJLtdU7ppmJh9Dv8QSzxrUgA+K1OV1X/WLYyXDd2chDdUhrr1v6FKBngBj1LwUFjTIHKY0wkiJIr8lsmln5Mk++ivvEKWLS8EsPuKQ0BR9lG/zakV3kD2d9WQPMC/vGTwitoB4snLn/+jvvhAnWAr1Jy5SdmMhyAr7E1bfKCbwzSjJjBu+9oIPS7c/LTJFcUPZG5uBbJQD1KeiuaFk1nhBWyMjG5bnqAGpfT8hiFDJo1AbytMy7UeU6C6ffG2y9oMwH+HNhfiA3lv16N9wM38oA0cIYpp7raP2J/Dd5QW9uVCejgIkYk9I+wLvgIyceLy7SUaIsMHutoQqnGgPAkjN3CyyrZhLGXTkS7hUwGbpi+GW1oikLw2vcZNZtDYm86Xmrtve9lgAy/ztDtirkGUNiPE/ND8WnMnhhx7bIxX5416gg2vaDGFf4iWaBMthgaHUu4jDAyCi1gC1DJqYZdcVeXjyDTNmk8OFX9sUQNF+X5ioOiISFmsjvOOs4ZYmdE7HubFMmnD3mvT2g39pbIC8N/JF/QVmE9WyOPcZrNzRoPGKx39bTNiF3CKy/ljZjhSYjGWuHR8G20bHmFP14KvwT85K1MfTdARhpJLrSxHaGg8BzCCCq8zt5DJBIMNBMFKS+AxS0lwuc8LvOZTpDuBLveOevTepqDQaov3+fGM7vCcDA6MeG6V7JZQ0238AZnW7KcOCoUD9ouh9/S3oITrSNvTEqDHmAm1e3crihBgelMmCv8+PY8X0Px+nwlxVIaC4hVEjZ8f3/VGKAictmqSIfrBGxFGXaXyappJVvUsWzN1oQx3pt5jKrYAVbqKfcWYz7NjLTvpFlhk/+rWQN5kehxron7kn6KNjMDOMauPts+ORqTsxxn8ZZ0UW4/nxFTeeCnOINwFXiD2FZQvPtOYmiuyU4sq4kcsA4dXNlC2PPdzKBObBGfkkem58LVbMPNH3xSwuXdsvC2dVK1GACNoGg+nKQmC4xF1oug3Cf7lp2aLHKL+ZV9u4iwYR875itS2tiC+LynpIeribKaGepDnxCFovfIiJwA+qJIVw8KRfZHi7aDCJTzYAbpalGB4Jti+6HHZrXH1wT6Cwc9NS/AW0H+sbS+7vVi41UU2jDGTbWbnAnyue9A3gOBss/O9yGSuh7mQzLeP/lYZ7DcGdFTebSb5oQ/BdUg3qyL8nI61x6cTKr/oc4xOZGZIXofyaxDCKGXJshaKrh+lFfzWgvgmRu48dr4jfebq3J2/V/xHXhGOApB49Ar/SgqtfnB1AUVMqAixIPC3/D4CvBzY3mZMZiQ7b7W00ZH09va3EfdVnQftOZHeMCDeEHzPIBMXb3wU6SlYqrUXH09Id2V1d5hWsx19rJYGR6ztfSeY2aK0zUNBAo4LQx0D0dBX+oXSQKVyNbInpanA5tVnFjEnBD+BDz9fvsVTaaOdxIC5ZbE92cqCearBxdUHYfAF69+OdsX54Qjss4pPAyx9NVfDDgHjgklWwsUu2SPEdDsQ/ePsre7CB32o+9f/nq/g4DiQxhh6HsUAAxozvWJCssduFVp9uJjSVWe+rxAlzstnuOQZpkELh+aOPM76MSkU/KivSx8h+o8pubIhzfJXHwuqbkgO06Ffoj2W4E1vWNrFxB4fa+EHZCQnIS2Cb3LfXfpgXUS595MhESbD+ynY9dOWk0c27qj58dLr4JjCOKaWvDQfH5kY/AIFOjRRiyPjR4YolqbbVupEAMIxBYrSbJgnKsc1mjOPh1xYjWt3h/Pv2PAtI9scVGa7qpmAyVXjJgNtWxsttUFZhXLvbRuBCgdPMJwoDtkSvqdhwQRbjhhU6bkJkhKxglFxSGd1zVv3st1dEmUrOkiH7gwgfg4Uq+MBWkoNhfSQk41e1I9qq7EO1jcB6JWNGH47GidMYZ9csEOfw7TWbftltdEZDiQJ3JAfkhh89sR8QHkn1O0575tbEx+RjUzoZAYQe5FiqrGOTf6raSaoLh/Re2InTKc201ujeccqGP9Vy3H/JeIgcYRkLT8kOd3iYE96aUjQDiaCFO6mecNlzLb77ZVtzd1Brq7CstmIFIiPwLkThy/3JJkCLmZL+PYs2zsLzYa5LeAPOsvBnOK4MBTMokoRPSnGIMZnnA6HOIgQSvCKz65ASfOCxsoKvpcp+iF2sQHsXiJCSyLzYi+1cHLgAP5bFmu7c1wR5JeUCGIN9HY4qobxnG1tJ2gpEqF3vnm5/7Sh9oj9ovmN2WyCq8Rd4nKxWg8/u553mEAwHWmsLPcwUlP8jgGEVU55+cfizFMDFYNJbw5ubMWheCLjo/f5gpsZUyWjs2fAy5tIacW3pAMNn24IHGY8L8//lbT4Czv7Te8zPVlTD5tYTRfpfECE7zp8B1YlEXtr+YdRF9b0b2K2aMVRkTpXgrtdvebeWAICyRQFPNZHb3vr3lYgrhKoi7yX4C5N2T577rV6jC34kB8Eyj7OdSOUVxbY+g8XC/jA/BDaOr01hV4ilgo46Y1IiuG4lE1zcMasqz/ogigJF8FB1PfGgTFpI5HThpbFG+vgZOaH5kcaV8PSut0T2p/AmwA7qoMSPAhIWSGuWKIbaHKRQ7YNuR/dgPlXU5vdt37874gUaxObFZUTRjzAmjAkPB0fKZ1PBq1cMq++g3oRd+/FU9AJg2izHuaq1MtloyfaQh/ss0m7GDx+I94xO/BhL39EGZQjkb0F0YwDy7dJaGExAdzVyM1jS/aWAQPrwA4B2XLnSaASZWfXkLiyP+iXCGTQZxWX8rHl49+zLruWJexEE/LyE64LMCCI2z02h7go7Ig4QCktmjxa4CTjY35r3uNUGSoBwQ/CflwSKRIWWiziMchLDYQorPSqB1okP/BQQ5Cs3zlb0TXC+GgkVG8CMCM+97I2qYd3AeTZCafVmlYUbySKQJUnTJ+lz3Z/qkU4FwHkx5/JtX9iD/P3jzlrl1WkWP27bSFstDmZimfSUVNAldC0IqjxgG2mE5oR2Pxb4V83sTTbTAtgiNfScARv78J0Sor+P4rjj4eBe8Ldm2+bVoiQraiX+v5U555TylYe5NrAxdsEkEz/S5Ze3Xh/GNcOuBkpSwU16kW9RLNRU05rwvVSnub7B7QBNEPQ9AFTN5ab7Z6sBsrGJ6b8GsqVtJpWGbYa8hA1p4wppJSoGKZ7hezu0xWQpEIiGlp+vRDzqHjxsbhfxFEyDT+j7XRV/0oXbocvkWOLpHefVSbIAivsp8nFV0n/vPzYVK8sK8Bj6vS/J8g1MmeKdejs13WPFGpUNJtP1wgpYjqZ9kAlR4sNMsylyKZ6irhZhzpkMwjJwh2fVSKaaxcAAi//RkJg29i9S0ULe9aNWYYO+b3XLoynBLNpAr+8sNSaust9V5WahT+Ud1oyFj9X1FZRsVstv7iPysT+LOXwEU0ALkdaL743KY20fwu67LTFpt+bU4KYvZhtasLOsl9/Yhs0jpYkGB3Tdor0LyeuZLCjbeSwdY6PGopCSnA86ZSdG272QfkwLGYDPxDsW3dH36UshZL6AoAz+QxRGmI91yLTg7E+tu5F5sJu2MwDwVVBZ6cEY4bH30ke47gi83tFfROkQ7xG8U5F66FRgc2zaehmzpseOXsTJ30IeylMNXQAP7oJtPmXkTuuTzIeJAfK1BhyFxeligsn8zo6NDyFfIq3lG+D0B52rfE3mqA8p1SZNGkP8BUa6pOreKmXL9+LIyXb4sEiihm2YigZrAJO7QvBvXFiMycH22LN/hJgFTo0I89zQKJ9hCePeNWy3AOwgGZiTcrvtwHIm9bj7ISERf+SAnacrsjOtWXwKtfhAE9WZkSDTszoOy65ocP38aSbweJj3S0Qu/xif0NlXWyj3htqPUzb0H6nsR6Cx2+vMmSiItVh9CUjWpMu723KUeb+foyVufK+N1aAr5MUaxJMIBuJpPN6uiBvheREMgHbbqtayzDaip9RCeYe4XSW6IdCAkZq7oseXIqbWyJSOP6nlt3eq7mLRULrcp4iQUbTLw2f1yD3F0/F3dZNAm5URD8QYhRgktVEV/8UFcv8OMoS/Hg2B23SYVuZxrXeg2bMA61a5RxWpMr+lt7tLCfoO+H/KDxzS70HUmse1gWqGH9+m6B5cZt2p6pQTnQJwbncnMkUmb8xpjqfezxDKmIzDD46j+9I1b63UnUI9ahV3eil0B9gByu/0TntaiKId4is83LAZS84s4jp2BEt+BrddeTSbtE6OjnN9op4Gsu6duC8Ig+8OJrsCC7pBfpjpo7uImeyrqO5XmilMBp/y50f0KrN9k4jZPRz/VD7xv7iUL0naig2a71E5xFDZ1NXm0nkxF6oWzEVtCRVOJhRzYq8SozEiuPPd01m6QO3/UiEcH9ya7eOn9V6jSSo4n7EiCUN4nbCn08wtMlk4uvNR1mYt6wmkvv05Pq2kByQuzkUv/eSDor64JJ8mwf/LLAwUJ+S4LzdkHzVk6T5lmPnwZ3cYdlfo/pXm96efw8JLSIodjQOcIBnr/unERrMgzlWIamZ8nlvejir5i9za7BvcB8JvAMPtG30ytI/ETlI6Of+b5ULHPQjplviQ2QNxw0ZCe+M2mr/VqgHru/NkMJsj80OdU34VS8kPHUDTs4LKwkb5ni/uQ9PhllfdRauRFg+dXyTjZyycqiq855t8DyaUsLD6GIcfCTo+uZQf4huo46j80RkpixcAAaaF7Db3VM4QqVt1KD0cI99CJyaI/oChJGnyqTzDJtCKbSFYE43oJ6psQy9LRQI/4LdnCSVuRCW+AUCRVy+MAkc1CLCj4eh688X5zvOX1FbW4q42jXVVUa5FsV3PjznHhd7IJS+lYpD3z+OMIGGCdzC4p/G85TI9Qu71fiCGvoyP8PlLCmrAEMpa5MJ1YA5qmnoRvA9/B5I4zOSGDdHGPx8Mi9zec3WBYtDT4bLSDuEsaqasWuUAOJzqFIDXzwRozUkDtlIIrLgZWidFM87X95fWHA0y7WeIAE7jAfn0nJimICxwbfgtGJR/ZozpF0bViOLbqt0f+V9gPbCaJ0IMX6MZwhanCmJploEYJqaw6C1mkzMB8VtY2DmoMX2/2XT0jTocTRljN3lM5aC2SG8g1tjn4i9IjRAbrBSRggjwmpCqTA4ILsG784+0nVAEyeJzHsIMQW3/YLriu4veYUhxC74rsYwCbJZbOm6TgVlqgIXW6m73MlYbuv196/jSsMxp94xzprHagLAekQ6oLQsuDlrwXFVNz/CxqSUfUuoRRP7EfhWdh5/JLHNwSqMGOXWJVG9+J2fqmrVsoa8KufM/76LDTKyEyxul/nalLP7FNPbLUHG9yvJO3Qd4YAPNMl+gpEOoByeMw3TKOKCVD9034bIIKHRr6aKfNXCpbUBCOH/ruITOsI3pC8jmcFWftzNAhJxnHKt6GvZLL5TmONQSlGKp/IrIhDaDZHTr2YTtS6t50XVXTOMNh7ZrsP1zQSYHV5/OYkCeE/lJT7M5VZhRqiYXb8w0nhyv2zW7XWKlB0bOY8DkwYta6eQDLHWPXqqCbYjzgEFB/+Idg9Fzw4bAhcQigeIUhhDbTMQF3vO3tCWhqmCiqMbuENPKixWoIlSuVSYV2UPfdpgEVo7W+GiCQCmRwz/Wsejg0DeRdOUIwgWGNRNXQv8oQW17XPWvoOifTS9AndTUK9mtWEfEv0A5UdA/RNEGkJ7Hfl6RAWX25+CKsveO/F2+vqdbVzk7tC5B+NENnOOmF7CNecTF1YKQOeS2xnIX7rcwQQr8uQn+KjgoG1Y8SImI8P86N7n8HbmfrLd5eUkwksbUWVV8M68rvm11c8kvOjLN2RbkrK/qJO/7enq9AJmD7oZQgqGk/nMYH46CPrEmQqsli4XpjoAZeWIYsYdbWko1otWnnfX9EBKy/nQSRKvxFgnfLAQw98A6GDcj8GKoQaHFZP8eZgZgERzDOCjxwtuUcsYOhLdAChPaDYwnrpnG7GpuDEIe//0jfAYNkE4IwKTSZclPduQVg1L1zuqD5Kh7+ZizHDY/K4XZJ9BnQ1483i16uQ6h8ZZ0hqFR8WWEA+SsOzvo/w+qwNQMTUph5yWzY67scsf2afJb31+g+sFXZhsNUcN9TKGuIh/CEaplzRcXkIMzBiiJlcNmmLW6l8MNJc90xXf7nnd/bvitA5QEjE3VxhSg2cTqBMAfE++2HlqJ2oUyR5BUHYl7b56LkfFpbAt7B3WiSQlLANX9yaShPH1h/7OuugODcSfKdk438nBgJKfx4exHAUMenm74JoKGEqrgtX84afm2mmP3W7xuibdQGnUUlO446E6TSVbRHwkiklM1V4GiZnsS9UbMQfhMOipRtwTESEWG5vxWDB58omhQZk+xVvUqucuUab5awQT98WPxo8WtQewt1QSGJnPMLwN9Zp0F72yhWSkiIh9ucCHe1NnhIMwwu9LAMHBdhk2gGt3lBpH18HsRLV59HVKrjVdg7gSno+VbfTWs4GZ59UhiirfsdVffpemQVeqTLtLMOZMg5n73p9d7zKmwGkIgpTgvLJYSSCxnw49G4xRrNsyuAFSDW6ZFdf9yVcyn89YncZT8azqFHiAUZmrOj5E8EhDbfyv2i/BUZDEuplVmLffs5Io5wFpLgr1r0sJzA3qbev0V14pQrhoBtsfnC9sgBjY3lW89qPIg2bCs5MuyXW4cEFIISqC1rOu6v/hTNhzReK+UDXaKlHzvxNzAcUZWq+hYzlhjp8rXug1P8iuzFCHWw7Nv4YBXRQY9ZhvNlGlGHpoqRjuTU8ND5S7TMMj1kzIoFyXvlJCryo2bdxwaWZ7wQJ54+bV/bCNjEsL1J3jHjvqX1DJZdawOArlNwwYPxCLi5BwK5hs8XIBUfDXLxRfYGoWzNYiVp7K96L6R+jd+DNSyydEoNUad0AsGPDzhetAtG9eyUH1PSqdz6tPZ7ULKA/oInsq1MLDf/Jwwfpsjzi5h1R+2AF0OAJHUW43p01ZxKuAAkuPnJ50vY7Fmugjw7KVuzEzb1f29X5I17Dq3Nty2B1gycEdWn/1ZdlYHrdqO6pSg07GdViro3GDwth6EyazpYqoM93wIwd1C3P9KUj4qmjO3oJP4+sB3IUR1466Q3I8zQH12SqQvhUj6nIv0IyFIyggdNSLBHpm6L+XtFtT7ePh+fNHpR5VdV+IZu9Is2reRj8yzoJTCn8FKL/TFnW0Fmzx6QAv0xH2i6XHnfoH1oEVJUSsBar+uhvnPIfOp413XADBVLu/qcOkVGi4G1PFSyD2biirae1l9XyjXc6RlX/82umxEqeGrEB3dhT74PsctbPFwT9JaKRzV+YyfJVWwR7z4c9foDtsds3tYGqU60uLpuFRSUGJ7eIRHOHS1Qrg9R9+lj2l8l6qVWcLj+l7PucV17ukCvXgqpcIQwxdeflvyIM1pAwFfNPPdkdQrpVO60qEKdbgNcDtH8KS0NF6kURpAJhpoZzwWBf5hrEX9UTMSSJ06fMdK+99k03yVCllvX2g/GErvyKQ6CrhM7yejfaU26MkuK2JBkdPjk+S2CVlJUUDyaV5YKJsEN73NHE4A54Yr0iWGwmNHB28F9sfjNa+pv0O+XGsMNlGfOQY9LB+bL4IoNRFIuEbQ2z2FPK0r4IPblmFJqj2cukVJkIgacPMf2tXkgd47vYuSOH10fSKbMboXByWtuYnfVVDLXKhWsTQ7F1QOZ/ANtZLo5npfurrBM3hS0/0KWi71rOKHrOrEL5b7iVltsg5DZz11uDG1EVz8U11HS8MCAics59D7fdY2Jnw7VUpmlP3ZknP4NkGvViplUtMH2FaEvY2vsDuwM534fkXi263nrAJYJngQQ4p5ljTxmGZJeb71U53+Qt9go10++Hs9Q7g9ROS0CYbL7C4dqjrpTk9jM2QO/GVNHKI3nUy5jh8bxYy8O1wJga/RcTk+my6XyIdlE4NfCUpwojZdBRV5+dbAebFRSHxyAJ7eh/7Ox83fXlrzlJUWJGchpE9U/mpOVCpMr0DEa9FaDgcrWCB7EuMzcRSHHj2pNVQz32icMYov6QDz4M1CxfEth2zJflH2RdCeL5AGYHAzT+x/39v9XMYEJ0fonUnnt4xP6kaLpJKLW/H9VtusCXWMMOMrCyycSGXvlAy9l0ALRufwY4ScB4K6YJYFCwh3BABUdfEKcZqZmGCepvk7Q+uwTo/srwZyVC1ZOExf0M9/LAQu608Mrurl8XkXcy6kTp6IlkPRt9umxgKBxpqwGmJdCkeuYTdZVR5YlhSzBhq2AYM6d7z7s4TrsER/DLHahthkkTJSESbcXiIMcUzagHudJb5dFJEky+3UybpAs1QIx6F56iom6MBQ4ffsmIWp1rBHh2snZjBInCfdB6k/uebA/j5l4KQGpYUMJjZHeUUw8Z2c5bffK38gchLqFmQU/I85cCTFGf6boozXjTn1x/5mFj61ab3QZSaqoFd4Vjga8mWLAVWYWm+MQzBRUtVIlQ9rTxzRgJxFFhRIjNOMZ5TA/0My3pQfNUv1Rj7yMogwZtPKTwiuzpiuhz5be4mDl6xUYHd1Gu6Apjovxxftpl6blJHZRUR4tnpImcojfkGfBMnxmLWb3H4Pe2CcoCtv9yWPGtkLwG2oc/GQbBCHeELBryC4gVdn6dw8gs+YwjoITHbZoZGG7U1f5T0LZ/dc36KQKWWFLiGgpIT8sluye27oGS/yX4h/KXmBsFZse/2bPWdjlL4IG2siX76MD4qgqJOO9ICHjQUFaYGFl+059BHdUMSvez5tZHQ/KWhRtYsgsr6966bcKPD1AxFvc/9aM4pBzGZMs+7ECedzzRYKKSwq/ldvJuYuL+HbtxFZ9A3Hg1AdeIT9oVgNHwETWj9B8kA+brGzhiceIGje/i3qqGp/eDSJ+phRchmt2aSqVtR4gurHHJoH90i0T1Jo4Xb14vAxY47qTYet2WwnjcQEaBAR9/sQcl6M+H0gGAKjiHNdvarmdV8Hqab/SS0GAjxs3585ZOkCXEF8mJNoeIwS+MZ/s1YBPK0oTtETAAEiTEHcGmJ2x4amn9xeyf1E6BqSlE+a6WEC7BE/Ah7cVbFZZZPr4PTNZC1OHhThLjHk8h5HdIm3HilYiswDcJWUJP1Rlt37aCfsjaA8zweWK+yUgiS54qZFM+14qKFuZ1slDXx2fzZ+eYt0gtTdxGXhI7LvkrwDH3JezqxHssxnfenYe/2fRmLTAMC9z067dHPVvRmdNtnk0keDmJOXlpDMYTvmitueM0W2MY5CpVNt9uHajiNlkdw1uxMEEKNzeBIQbgaa4XBw7ofScMgniCxvrjCiZ85me26HWTzcW2ZLU5ehr9W4L8SR2Q+VPnswIHEhoOuuYi5RZ0FHHP+rS9zvV/ViGsQ+5MVm6pQb7VblrPmzGCunJ1hjmwSX2dbz4Kl8BL9n6VdNtg3IP3dGU7z2y/GXgd+zxsRrtgJxpyrSxz1kEm4vPrxqWEuCCEAS0BJ+kclS5LFvooovDy/cT9KJGJtrdsaHkH+JPlyNPWWeCFYMJI/tktsveAN2mkxjhsyWV9mAQ+QEsenoFsoN/4BPz9a96/FHSiALhhq+7f9o0kCp5dPjW4qnrM8PaqDm/uqEoyp6CCG00UwjADJOP0xiK+gOww+/yiGIo2J3IIoKnNQIAxt/khvHS8N83Rxt1/pKhRqb/J+dXwy8Ei+pSwLnvA+2t+mf71htKJUvMML5hMg/xUbnWlj6gUCA+IAdzWr7WwuugiIlRn4Ab8MC8gFKSFtxoaJUTVyJ3GylaH2VfaQ+sOXCP/fbvasQEaT71bAuoeyifhraHHHb4vjb7Hz/U0NVre8IU35IN16ysfVBSDk97w8LHhYsmAoIfBr7RMSt+kiPJFwRTgECMWDH7M1XnozRDMC6BbhBHDIpqFHxIZyho4/QFxVtFSkhCAv4rNlupOvaXrNSRIu4vJBzthuk1hyRQB4NAmQKi9qqjGCKEQEyPFphwq/tNZoBPvkx9frFDbJDDUOl1P8rFSqyzMkdtG33XeODy1BMhZBxHjYcJsc05fRA0ysjiBOgASDZS++xqwV59gMXEKf+S6nlwY16YM65kFviGNi8mijpIvzwptSmjLfMr9ldwlxatyLZyg3wROd8UqzJnQsZ8nXnsAjo167VzYnJ9/HxI+ZiX8jtxxMpBDvEdkLh5jV09hB+etec9Gub5basUfO9yNEK941zr7IPtBq/BWPubZcLhKDNyjNVoVU3cklBbLmv87aH//y7Z5PBr9Duj1usGq54qLmQiKz8uADPKkr70P47yPUHMC5Uahoa7BQ4HG0Y8b5B1bcgscEaiKr7F4gqa6GNX/q4kSy+/z1dl157+NaLySIG4y3cEtRTx0qkNf/OideoUrpbTB2kJUwg0B0KRp9HtDZDpK74YVrn/p39/FCThO0WmnpU8zoEdSuIClcYcUsWjDPyKuhRufx/kl29nO8rYj+ybn/m1zFJ3UeZtrych3lBopvrGCmw9ILxWBUyvEjST4o4cTcas19dzS36vx65mNqO9cxOJwmwcUP5LvFqOo7BdiFuqANPbPa4NCG4Ty3L9SYjwmtkOD9M24JdkaGMHmoL73q9dW7y9LqMfAooCCPSBTDdG8MKyprSndCE0qbKK+i4lOruYhXwnRc6LbahGtBAj3llccC0dYwTPsyw2+xwMQxWmsoxMF3weFZqJFfbZtqHfDZstThtT5kuIIvRoBpZZeP4ssK9kqXEMjbtwBCJ9bxsZhxV5s17QS9HQlzGRg9st0WfnAAR7nCJ1HYj5E/UBMTnF8h3EA9sN9nu41B5c5DE6uDIB3X6sG0XOerCzcNcs6BRBhzU3nH/VOg7JbcE2FwbvIXut3+NA/HVYPHbjbZRVvqyjJPQXaX944HwycQ/5r3arWmOaygC5u+p1zCLW1oHu06rH3+AY5F5brm7ab6NNdlG1YGNWVIKaBbMeP+uvYw+QoIxll+eupSQSUoz4eGq1mEwoqbv0bvEiOViSwuTXljl7mRJzXJGUhePcM2fusVFVHuvCyb2M6Sg7lcaZT4qE4zk8q1rbTX+krxHgs4NSxO7jAojMHCuK8DpD/xaTnhUBJ6VkGmc1KIsiOoMx5apfOCudOK+s/G7Nsjhd3vItPiMP+vc0fTVjNcUQaDI23jYpAuy7dluBX3TsxxS3+J4JmRPetqgdT9vOKvj1TjAJnk/kSHnzGwyw+lqNmOYpvji4Agk1NH4CEYraFUYXRy07F+5Z4epAViZ3k99/xTOuWVy1oChZX58BtiTYj5ae7yBpMOoNGNN2hpAlaIuz71riJFqwhHPl/ezrp6J8pByxiFyU8zhW2GDXMp1WTfCRnx4Bk1OrQAbz688I9auVEFQ3NhKsonWz5FzsFrmvqZkskFte92KmQ02q5y1ugmlGtltP662gPZE65qcFWwUDlojNctdJ08gLv0IGPOMh/Y+iBtBP3ueG/iGnCGpBAK4S9QszhfhsZlG10pW2/yNJL6UNzY85JBBxDHsbwR9/VZumkwd6JN5cREGNFs4W/YkMdOlj2wJe6H0Lf9TZ2Q2cNx0zHN8ZHA92X68oFXArUeHGBfMbBgqrEGlPWWprX5ARJR2xsKpiPIJdfjxq2ntiSBDnYDW2vlFLFNwH5ab+h8zsIVT15p0rmypmcE1+ykPZ21xQ4XrBDicsd/ygE2OlrLWI22lI1C7O63CvIzZ480sTTVJuSGW+SSuafDkmtA//6XTS2hZLT1LWWhqz8q/iTT/KQSFbLSaKf0xNaz/z6CqNosL+lVtYbEHAeUvfmBaewhIBIg0U/VWwMouUT6+HAowmwWU6/60lfSXcmrp5TiVh3r5p+Ca4HbrZmjYndh1wY6BscSorkDrDcXrTMW7I4vfqpSJOzrNfmaEM5yM4/BGeIUtXPJZsg3qBuWmmJYiNBqS3dF920egnkuMvBct6VL8hILFlxfSch3oDeU0aqIuFFFU4Psn8Yw3QXkNp31w3FEYg+0M35oZblMw+yeciiBIXDZyJON6i44ROmrWbTRP0z1qL8O8+PhiNIb532yU+3CZELtFmcy8+ni23YwfantjTjAAo37fUMjZ+YmXudm/Cr8EIqPWLfIHe+6oVEgJRh0HTG22fDzrv7IxmRKIaqInIRjEJIS+esMNBcyGTOCuvJVcB2kAI4J183hZjbP8n25d8KvvBTypxqfYuYrE82DP+2ZG98Ss9ON4WWi2BiGGC/wWyuo1sJAGVDmHH4e/1A8dKASTurv+Gz5H39ukljuGtAAC0gjId1guOufzpzzkEiJFMkjj1G4+RP7XHjk+Ut5gScWoY8vOdl5L+oPagKM4Ja5jwjR0DB9DPJvagYKtLDS88XnUREe7F5uPDVdHszdIiLJGg1o4fJWJMtoatAzdyjRfoH5D0lFbhfOo9GMA8F+WRx9RCoJt1Lx+hrZqq1ok2QeeDqXrnviQlPb/LwUF6BY7ZHmMfReOJgUpy4WjkGBHZOJGrZlwWRdmAHYNPCOOac51FaRV5dllYoy45fp48kuvPhlL7nJRXoAQhcYnDGMzYFs+YK90Uy7f03Cq1q6KIiivZNS4NVBXlnBAdyMj+SIC+pxaeWdievJfcy4VqTh5XFRKkjatQgUUGAVYbYitubW84CWY+j3Q1B5sRFuxk3+rJPjplaHdpLtNDi5i2a5TgFEsofhgn8GjR/4LBj7LPNeQnbWwgMsouvce0VbL7DuZWCOI7Aa18w0NNTpeIPoK58MVxOpM72D6dsfYi9MubB2Mw+w2uq14L+m/L1Oldx6P/QF6LdrZu0nZ2knt+pIZzfpwMnXBwufWqz4jfx3a7iHb6PqLrxwF31CfuVTG2jzJ51mMVq5wuX0uJKOFwVpm6zhB5zF/TBLQgpW5PvlutK2LRZmpeN4ymRhedyOuI1ftQ4gwveBIYQjEZgVmlkICdhFSxpKxAABbag7om1A8mV2zx2xFzcwJA5cmnwwqJVDV4lg3ITdZb4HKze5fe4DZvxNHIPxgKjxXsNAdtgcme7ie/X92KOVx4/xgt4C/CHDoCxJ/s6yF9YfdfFsW6334SpGVUshOAR9b41xjUECpRIhBoTOfZmLkVa/q00MCunYXW7qi0TQI027TosYpg0Cv1kMGPA5c1qDWEMB3TUoHtgaiT7GD6J/YdGc7SIp1GDiooutJoJ168/achUB7wDio5mpcp7xNCugJP1W/mOm1gsV8/S+CPbZrrakdB8vJiGYbdHYDB4jFU8rjrUsjt/GugDeknie7TZNFJlQKHheaVZj6LAZF4tj1xovQXxBDXjFHaQ4KNxwJ/vG0Km2H0VdLwaUMzbDKG396MB1mZ3PZVL0aFUGETivpLxsRHMYbLpAvkHs7FdYAcTBkCXtc3+XFs00gKDphuHAvVb4W4zLDZ9cuBaFppuqZQ1lH9H2Iom7otvIUkLI97j3hZGSvwJuZVn0lciE+B+04nf5WdnCxcWyO0SOndRD4XrAzemH1lVKXLlTWakQRU7itMAbyceDLIDHxt9PL+sNR3lI5APwFRv4Ub63tt3zSY3OO3JKnYjq/kxz+AGZpjSYpom5D7AZvfAmKdzTomHCs/ndUDwFDkpwSK6u2W7ueSiBauY81n3THM5Z47Cq3M1UjUsZedn20rXhyoeSuCwlqddOGziHwKOmIF0DPT1fVC9yDMbE/cPZUQpbw/tUrcozSHFfauZM8uNxkGqD9U51Sh92KTjSqPWECU6CCN32xcnUL5ZCr40xTVW0sTQvjmNp7cON+vvy8HUCpvF98s+LlH9jyYfFfaOK2FenAaXeJpZc4vpeAmpuuFQ7luy2Xa8R4Bkofq33YtS5KxejH9ivsn1c/nt8p9dCg/VJsvlRBhiPHyPQNAKo3hKRZqkTJLxx6KOnk+7XelcRFD+XgmaDs5YoCoHa0cNz/v0poNqpCD7+EbnI/lMzy3gJlsZ/lRdEt+dRVUuvgWqXhDeclmZDmo5jjscesh0eRLiaNQC6iwGrSV8nzUxrMliaI/oeOleVfOTdY2TiLueB2W2tt3b5DzKiOcu9jvx/At4wQnmj62U5vvwmpYJqtOgecP4CnbEW5qJuVSsRFxZNbROrZvC9F2g0IylLw4T/6YWNzAwve3V4e97i2lV2+aBglUrQscL2R2h+B9v7txKa1NsKeqBIZs/+T19JGpBuLYnSGEqCqpk9Mw/9A9pqkDmNYKe1LuYrRt5etNc0EDuHXSCpMRQWl4AUZz9O7Yq+xXuKVmTiFU/coRTFgN3iqric64eyP39CA/4P/4TY/+qhhcEpL2hUfGJjdGO1by0xGEOh0AFs0VwBzwXEyABiYvy6knHfLs/tzvzcABqYAKBSwsRAQTulAc/xyAaRjbF2r2kStBBzyhZ/2VbYouX5lNHh9sRNEUCwPma+5RNEufVShP3fXodc8cBPGj1hUUiDb1HO2uUsmv1WgGCijCcxekpha61i6Nt3b/rQkKpDe78t4k8wGbX2q/6MwnAbbL58aIBoEMt2qhOAN/JqUQHFzsNOhzGilEGkeUOhON5oBsAoW2E3cTfHOuRJSCLFw3POSXvuX8c5NvGPEqm07xtPuZI37Uk9fPxlBpSwTnP4H+yLpBKJPTp+ylmaCYLBVZYth+mbhKjH25dswGslJHYZ2lhz6PmNihMH6ZbBlifdu1ie2grejCOKTIAzfCtONfUZ0Lm0LURHivDhjHj9jLfuSPq87xIq2+hz/7cY5Tn/Hu0ewAOs8qEFZF75T/yUIk72MNJWo1BhnWU/7lzKJ+dtf/p2mUVE/RZ7o2E0R+MWpGncSbJoORT6FYLJ//v59X25IuH/LDywqdOPcVWs8fReeR3SAQBNEDsSCnJUFkEDntyFHkfHrjnZ6eLZue7qr6kpixu2tyIQzeZglC9gEruym9YV/CrEqR0+PiIN36vJd/2h1IMG7m47iZ3c6IooH7qcccKWQBCjTQ26OYQwaxOaQ5FIRLO+XmcZO1qzcIbkvA6PP/r/4e/2fQAAc7qJgqlBtnkPP8QiUrwEipjAOlWqp8zpejWKIMfMFdaVmxRBS3hWilAAs4PJ7ltSfXOguj5gElklqhkRXoqqpxXfF10DvibZWQ8iuxtGZwStTMN2T8CgmcLPYRDXiKj+HHpqV65cyM+4D6iyzQq5It5qG1BCBXLrLSXCa9aS16QZWbD7RymbrR7Pc50aoqdwJCLFZGtz0BiDbcHRLUo30CAMuZZTYkjnEpOXS31P9E2MW6Pnmd/7swqjWcCgoqkECoJRc0rfo4NhezJbOXj+CRLVk//H+863ouL7DxLZ7tFeGP8zp3Pu6qwAoSNhEMff0U+g262lwd3lpm0S4k8fi6k/kRO2oRuQHsFg31gHhNmOtHGklJayU78OZXcDzzN2oexm+7FTNbWQx0pPcL/jkiBAf7NfyZzpGbZE9DMxXs25HSVSSs1UhVng71DGTSQqBeVn1OX8tVvHKmiu+Nc3myfrRic4psK9NSVrGWnLbOU0bwvmmpYygGNBw6DlhtH82CFzQWyTfgMmmKB1n3p+ye5FHQ74cJEiRvquI9Ppw6BDZHOCETsr6EL33Wrhectd1TLUZWpKsbs1Ev3HQH3X2QSTYxmf/S0xtUmOmzuGM4fkkkOsIHcL5okJtsAzXW8UXBHAqKvUvXG6b9JmWHTk0p5Xg1VT8xIjtsrGJ1La4py4hd+MXLIQBlJAmK0gibdneg4mQ5qE2iy6wud8AwMFvB56IhsnIlefyhFTnFwou5aQ14X6A4O4bobq5V+Z9q1exOV8V6DhAhNDf9IYumzh5uxptGPeSQYNJRVQOSOvUj0rgmevhWwLhOLIvwlIgYZ5149rMNWUxni5kW4xkxNkDdJjIv+bDFbaBKP8mO7xSRBKsIRHz1/Ju2GE186NuXQ6MmQNyX5lRbOSov+HLO6S/4gwI2TB5gQeJTiY/krWtLyYqBu7/PLkeeIV8q/hmpvLp+iA1YIzOc5GeQwn1BOfZV7PO3PVt9kxl7BTSlkLaX1Ix1H3K7FF+ng/wdSS5dw3btDQoQjs+onrXcduS7W2/rTHmdYxikJRLspqU3rfxoyqoyiex1CkrqIGy3AUGEj3uY4OaUUOp3OGhp6vJpdAxZFkQVer68TPlnacqBlPBFCJ9OB34v3vOfEwIpd7OKXL/MBVW+V1kmKhHwdrkBMMXjs3wpTul0HMDHy+hRjq8a5TUXht7+d26pyuMOatSjN6x9iEHsuYPOF8UBnonRN05mvArAi8OoKBqdmP2HbDx7Sl0FLaHYnWls2+FhItDzVrGYL6b7XjErAw2bGSw8EcWwH2/pUx1pUfbT/lMj4huryZILvEn0+7WpnHDoDHcUTqCdXvUkYM1XRrsP4DpclN7gJRuXItsamXsJ1EksVB2qOK50sJkQrHPYUiSvIT6H8ec8C6pAjppIPwqTntD/wZB0nb7Tu6jfpysPI/Wmi2sg95OSZq/RvaixTXAdp07A9P8e3DcmWRjmA5ao9fk0OHoFqxoZVv5YxwV4qedZ8824d3TGl3z+dsgbrMF8T2cmZoP4rEe3phIbwzXzR79J6yHZxouO1Yo12NrmPrFSl0OeiMfO2o34rs1mjKfeRfHKwal5ZDH6PhuItZUa1xDnQHzDQSVbC32jysfG3iAIJKzSwMdnFIdY6h++ODxU8hS86jgfQ61XylLgLI07o92FVaEK3XzhtjXIfsN0VIBjKtPhDBz+UCAqjtnVb666qocK3SxHv3SBXGpjO1qtisOpi+69kEaor5g5HIJQ3TW+Sf4rtqdQmdbll5dsQgYuKua0Ef8nKzm2iWujK9DKbvgvGXe34QH2tqkeVJsHmMFl3nPc/nPgBrCXPkMss6WYlqnMW2fHDy6qBKtYuZBDSG7uBSleqBvQVdq93i8Oxwa1K8vc7/oOtpr30PWz/WT7CV/COWnrgQt9oVRg0Fk3Pw7/XR5sR4j17JsQ2u3HeS1/ekBPDDotIOVG0ta28k2PEgQWSN9+P5AT4ASfuca7FvZUA1hZjIYFMHFij/p+D6MN6Jj8J04vMgSL++hPhM80eMzgHCvOPCnfrF+iwGGPldOklEEDRGZFMTEW+XjuNGHVpCcPau/IbHENiOVpotHBQToOY7Vrh4qOJbX5me5rG8FrvHCyQyCjAsOVQjQMij5ANZtFkgs5fImMN/NRQCNyvjt7bkSa1EIkFnbsqqcJJIdvm8LwbjSWjiWfsMYwRv0iHNE6YHDxgsBwGcqHtAcPWbSGxlg++pceTCJHT2mpMzTmnsiW5BNS97YsQw0RduH1kR+gX1qhdagMdLMWciT7AdDiORGqwfXesJNhLzSCuXB4/iUfa1fqblRnVMPa/uc70iu4uPt1S/QcxlZPL63nNIW0yjpebJcCmOkpCY/3kRa2g7BAeb/vYAfX8/YMGVuNrZGb8E4UiV7NSdJ36oGZw8+r6mLrvKGZhiY/7MxDIqPfi5RYGAMEveNmfc5rEkpm+Ej3lfPgsjl5mth7GypaDIojLrnbXkG6/PECXDnUxIUMG22o0MVt2GVnEGB9G4/VNXZrDK0nHWNFL0vqFXDfiM5ckfuJP/VKLORbNK1hhZ0BoahScl6yvQFdvuz+s27LvsLF8LFYcg0i2qOftCFDbDK4Mz2RApXnJx2pINPnnnTdOhWlauyVFjsmvsd9mh5rmqhSEcjGkkwt6pcjJXBOK6QECn8PXVhkaJ+XOSjzGz16t3B2PHL+PmyrSz/UhaNT+JFyPbzi8eCItNgoh4HeV2LLkkMVHanRYedWnwCpK2PLr2v1FaaBtUKeEASgs0qDk1XqNHaEa0TsGhdJZAxG2K8zthZEHGgnkvHoNerbqRzppixbbtgngrd06NZK3t09r2n+NH5HzweucmUqZ6RKsfcDVWeys37Hbda95bVvz3ygRVLj6ZvpfhZDj+lJ+wRrRE2alXiWvArfzQp9VjFi3yH0pLCBSWCPEh23ta06TrqXg6jk/CNKxkh9ATEGabgyevOr+itLfNHnBTDT+33Q+8SsG7l1aX2qUwhH8BdVImPudtydfj5+2zTxTCISdJPQG87oynqQBWmECYlS6zsg8Uzwsvvy3JAeML6RoP7AUrb7rlV26VN9/xj19hFfHNeLqUnC90Xo4Y0RYFYuIJ4YnykR7xdCUddh7dHHz+dZczHvNy4SaVGHs1hAk7DV/+Zyr82BjIfqXB7aFAHdyJBjTI/3TQ8JIvgDsbQk9B9oGfpH5/Tuc8fSpMbUdZDia298wxM/QNxXH+Yzhkp+9E3ph0c12huPk2FRTYMvUABgTQ6xbRYvRFGIAyx35S74Le4vQe9fiqydZpkRsn4xTe1wvm0bHiXQyvdBnyCN+vhlU/oGFUTk9UsubNCky0Tkpf4I8L38fMhICJRnoR/shrE+BEb/RWMlKcvYjs0k3aFFvVG2docNpgwrNCjfhC1oU7/7Xf2/OGJ/+2pCCs5Cf52uakrl2uHR4yhp/HLYAxq5Z6gC23CAzEdNHaCqIatWARp88dNloX+Ui5hf2l8W/MW4tojqXMVXmF2zcJ/PADGzUClkvho3CpBGF68KuD/dqKBxT3Pv+Q63kBj9R1htwXsZdIlmwuBSIAa+AmoHdbZKoSVmtg/0yAo9IFgYspYPopDRTaCGFxm92PzbTgwCxmeVpsEDKKgyWEuf66jmmk/Mmt8+25b6028dOkpAz8BlbREua3XvzKBlG6Fjb29PXyEjB6hZ/vs8LvWY7CEXIFwhyFgFFWk5FLTDCUQgP2lUDk5nbeu3gXME4h65YmByqun/3XezsJgvT0QuzQ0cesJ5wM3inAmEFlDgUrRZs1fu1NlpJsHfK+H2TLN/jnP4tnAhntM9m7e+0lYrnfKoXBaNflXuoc5n1euR77/wCLfwfDMlBtPT0dKsDa2QVoKWXEmMzLGzdHlyUkrlK+wJyfyo4RZVWHyLHyL+QifyShhpNc1LkFn4xyjyeb9YxYt8Ji120eQISoGj0gfMSyQR0P4Mw/4igxtDbsyXostm9eKxyZzoYfXx+dVL9X5qNR3HGzfD9A6yjBy0nyBhVnmyTuHTRvePCjpe0UZK36RF5d3piZ9qmYqdQVgTR39fPyUJUG5WyubQhezZIkTo00igrQKq6CI8f5fKXEf4+y61EemyY/OV9Pt5V7ADcsQ2FpegxeONjoSIkkfd7IIH0lzPLs8Fjc+PvGSHbosiSwmco9MPaPRVo1tM3cuPNQPeTtf8ytZG8BWEU9JGOCgmaYuohvrWVGigN0blMl5fKRzD48/OqLK+MMmjvyIIGJO3ek/54A8cftDWq83nmx9Ve9rSuUqwlvCjeidcRLOz5uxOsp+tS/Aia9DaXbT+qXSpdbobxMaA/tTHzJyJxfxcTQEopjOz58VukPE/FmMiIUz1/JIHsUkx++5h1A8kJSHpaUa68ccf5ssNy4zwUpw3Bpya6ubZ9uje2OaXaVLsFG5AzlqCR4OytZ/U+53wqdJJOOQTP+8i9BEl0HWq8l2ztnzCWvxCms4+K91iSRTQIi0LNrFsgSPS3+DjyhDHpt9uAKexR65WIH9L+wVyj3HSJCRWnZdBTWQuWuPGtP/EQsjmYj4RFr0KUswrNsOG9BEnv32nSSW7hog2pO9lnY0ON8jMNg0hZkbYsReaTyvl3magCndhLzCa2R578zaRwmUPVVXrERtn/VDiew/EpYBJ+BCQGK7eCHQXBwHIjY5MB4A7ukduSfy6uE6g5aH89GlfOvfyoPvEgaT1L9QrzStO3qGvpjtCbc9raExlivolZ3wXlHtwOf3RgRQFpmZb5fPwAPN9irMCm+TcML7oLBUK2vniAkvW5cMIU2Sd2EWAGPXpePtAGQYIvjheo6HU/GxcY1Op+w2qPfuc7QVkyCPzY8o9XQI+CCYf+2eejLq0veiPU4hj3ErFH+YVn6ltfmgGcuDPUkkNk9tvr4545MQIvycMpv0kvk1AkymewMKITHniJAoFWyERgLKmS+ooesYBr0SxhpdpluSpCKTY9bRcW2V7GD2RnhdFVsDHNmGkCziq6ovAQqGLTcbMwlq0AHYzC6/AE0F3AnsvYHlZgw1Ou/+rxezlxGgBULvZh4NzqPtVbkFBpQgIMZuYqwc+UAL7plq5Otdd5DTSBeNkpfmlUMUTw2XXDK+8o+90Th88DvzwHpHBGmjTs62c9+eNImLFQ+h7cEDtgMttgxvGIIsl28lkIRXN+KJ74WIZjdVx3fX3tCZPiMlUYSER9MO1X9fUWTvXCuK+A5xJLQtwNv9T0FgYMBaxePTFWkX3YT8Fj5dsEwoMDv0WajQJvnBbuNowYEbJFrIb3rtmPlzyjMn8ZRlBdmMalpyPulb1CVs0GxzvUL0EMdH/b7EUfX9pesCmgNE7KEV7c9ipMIU0rnkaWdASAgEma1u/iEGfb0o+9Y6sff5HVg+FIpRNGQ4yH4vniuwn3ac36CxsJJVf5wPKJlvtJ+Jde8BgT9rXXURRZE0GPI0QItUJ3wwEvhPMlRM+1VMqoXfocQl2ncxvnyMYRkt5qyt1YyFZ+ZHAcpFf/bp2w5T08uHBi86TBvskeQryRaY54eq4a6Jg4idLZwKlm1IiCAYJwZAHnTd7eXu+h0BcEb2RFExxoleKG5p4CZ44mVmTTD/xGGrSrYemvx03q4utYIwdg5nGKVNtpmi2b5YnRKn88Y5R88xoXpJUOSrQ8qAM9zUTIysCnmS/fbr7ftKnhg63+fEvFIYVcQdpH5zgj9A9aCuRlsESX5PsvdvliE1yptdii6XIB1mcd7FkU/KiAZXQ6PKOs8WaxzqPobM8L/NaUYNDp5IIEe6rBZui0fqcElBuzEnBuPijS3QZzHUTyfg8epECt+JjXmly94s3eLuhHoGju2DaTnU5fns6mNTpuTUqzLElBNvX6U9xS0836ISON2Ae24idOM1jLDzHJeEoxgGkOc/fqRpaes5g3Kug1I8SP/RdsNNyy9eegRpoHhfNqB6QAK8kDOJcA2tgWhV51RwpHuaLuOdxK76BMjUnFyOXce8G1sxkLqTWmOS0ifHVHlIkn8W69lmyilNwyIIWQOsyAtajp8oApb211wktSvRjY7amslBLX82vq6x/zHAccDjQSO8EqRlfUQmkdQey5l1Gri6inpqGRhKgyCW5lHSqKuFZXKKqDyli30pePAr7XmO6p8WJiIp2CbigkL9Dht5BkfMey571BiXtViBpTLsjUFZhEAlHALclj7G3zrKj5ZUeXTeZ/8DppyIgqkuz0zD9ygy1jo9OlhQ96P6gk9rDAFcnz1dPs+GABNSE4deVWHR74k+2IWQ3pU/QPRwtcWJiUeGpofb6pUXnGx3e16JtDX1g4bEjtCMp0eWLpg5w8uAJX+Yaa9Sjmf9aGnmu76CKPHyAbhmxoy8z5R0QKsN26mccwmx+SqffdrGOGuxOQEhe43ZvNG1+kZ9zZ7UeYedYBZvy5e3/BD3gylbZLqWIFp4LK1t2QWbvizVo3BcQIB2ozE5uShbl+SLF9JJv1A9WBoyasFn3lql5Nz5O5GceZ9cbqLbpSi/bbL9RfcSgi/y0i1V0a5qIdU68KVp7vqbuCYretNxJeB0ACIXgQy1064qc3UjJn87FtdKa+jH4xJRahDcSezYgR1DXffSibeQf493JXdO+6K06rUuVqKlHyJ+TN7c1FBTEdfdZ/AUAHjb+75E0qa2cCyYmpka7afXIfhXSqt9A+AyUp6B35gHHp65AhGsJ2n688YlBSaY0iExBSIqSuETRrE5TSj+b0ccyLxPreloDL38+R0dOpkMdDdJTX19McE67yPjNgP20cUS11n0D1WRjxVZhNE8hWEAdSr+uHmMLGe5GfpyZhL+jzXjf7/d2ITiON26lpZts5c+qfcc1V8g3KufRwNDlKRrwB6Cc1LeP1r7tyEidN4ti+mehVFZUWHRgz+nJD+gHJbiVm7OlJ7nh6E6DNtG5ub17WZMw99qhWjJbv6IlgSoMF4CZalkEbuA6uBSrJJcQXyqoq/33DKnZ9XPx1/CmDsOxB9lVkr2u3Fve/suhWoCN0DNdKzHpJCPpbIKc1p2yYfJPa2zX+BMk3Gc8sw4TzLXNaMIEp+N3YlqmU16DW7V+UEjVQkq0wB/UOy4VHfRk7mUuE1pjyrbQ1GhJtycudlsw3ctYgepMw8oxqOSb63zJeUn4Xk4lcH4Y2Yrb0piATX80nb8x0v6eJ3mCrPTZKYHPSbETteK4b3oPXKDm5KLl3Ao3xenX4nqGdEwIlTN+WjriUr41Cr+azG/gAEBxbh7B0IHAbPyyYQeSfj5URU10Fk8J78G3LzyLwKCk+dwZgjU1vU6IEHLKgSxsTZFQqfNTX/ies9zgaKttVVds4Kh5CC2L4Pe4+ouiVDpAw3YvLgJgeQEDD2QFCg7KU4Ko0R79tKAIgcl1yazNMdajXbQG6BzhnJJ96XLx2dFOzN3nDdmYHeqasBi0W1X6GqdzpycM6OCYmP8aVg4BMAO3Alue3fnmVwn75G6MHdaozod+SbKXaon1vx0AwIV29DUbyl5eB+TK+G5hgqz3+pECfCFZMH1WT/URa/nqnUKKZ1s736rA8N7PrK5aZ1AZyFd28uWUPesI9MMFFLid5aSRC4UjALFAGN6/+Bh2EXJVcM9W6lcmrmPHfml/M9Q21MACn7ZyXcbR4IfyYWfaeHud/5SfpPza2e/YQnizchIWdATZckUDCdgANbjSq2c7A+MnOSwrnV+DewB1esdTsedc6x7aykeBXfaTFKOsTE4sKXw17EUcFRyS7WBDniH9GbW5RsAn/GjskT1v9oGsVr3eOopOcZ0xpWWJoXpiIRrpQwREJu3PZQxG+rK5gOLatBLulSwLttUaxWQVsTLl0XYdzn+WVKWRo155VHFYg/qC2WLmH7ZT3MEnWlN7qibZP/uK+kqPDGL86MYGk91wQoUSNtNZB8ITzPiRUUCKwDewwV/OZC9ip0hfMeb0zsxq0Ig1o1vOWYM0vBfK+yxTkytpAwGJl3b1ZyVR7f9tIKRSeXriEXSRwFnyxS3WMcrMRv+k7aJgwhqoh97kOtZ+GCrLaSPiojKI7ze4pk5S24Q+Wmx1g+BHm+ci2LbiBAdddQ2n/VKnRxgnHKWdrxRHM1Sax7h3nnaR+yNGn7UwTcKThGdEou2hCKMzOQn5tiKO1k/IdWsRCrlv/8idBSlmE0zEWz3sTRd5SBaTqKLwQsquiX+LT6OrTi1iuarzeBP3CsdEVXxLqhxf0yukEEqGxY5sXUfnOFdUmCMniNAq7hsMbm/UHBlqW5w8JhXz5/VkxFCL1V5bH9CuPoRgk2LtpYQhEsHX/unZdsdqKNTNWFIB/F1YLcIGOEj1EcxBWZV8pcwXzwe46bbvPYjJkZrHmCqS8u1xF2InXrSbl4owwUedDyYsjmJ7JD9+oNMENFHlyF97kGeFXPCTGW9e/8ob74uOIbJcgK4+Xewh7z4ZnkxzjAhd85bXfK/l/sTnyu0ImPK7nE0LKklAk7bmhS5Xl6viulQK9loUwOZMmVbuxD+kj/HdOp9l2ZgftzkKK/xerLz50uziNsjOKA8E4pde8Mw0xnV1pOO2VTilh7HxfhNjIUZmcpqcaqJnSQAsKazsGBZItkL4Ws9WaNO8ywZgNGRAJIUnGGluFWhzqglYW2wuQTvMVvmCtb2nhtvy/qmNTk8WFk+ffhvbL1TwXg92g0Z1HGLqbC2e0BwrOr4NpfqdSGMTA7SkKE9GPp3zOGhmNI7b/ZSJLEX2xyzt+htM+4G7+89QKdcTPPZohYic0AHI897mhJFXsKw9gPwD4oC0Zphlovf5pfwwT53tpyeDQHhZJDusG74wA8oxJpmXSFNN745M6l+qlDXbfptF3PmamIJB9sujfn+BHaSFV0O+TsfiO8qGpeUb9Exu/kPMwU5en6yJQlz+TLf+fVgY5hU2ZczN4yuHMDC4mIOo+r/nhSsVvboJL/zwefR1ve05bdlNpxuwDr1xDxpHEFw9RL1ajK0E4RGQk1QCeQZ3vIWbVL79ftuJBXhC7oi4sZbp5O6VZXjzM36uEh6UArqvMPwso+BZMLEfER54A7jl2TdiUGZwnQMK+bGRnv2i8MRdfwP6lCWYk74X3PVDNqVN/ThlcNgRbBXvhsLtl0Ri2BYoH+80ZpYHSX1XSzcr3Qv6QBjwhUh2JkoXIIW+Bc/eZISiaMI3zmboMLBX4hunvXjhrJ+PZ0rj+pK5SuSLFNkNTM7TRK0rPzCHqeHOY1owr6kFPJP7oKiU8N+zcl2ak7GETn4o+xngNNkHZwAcslmrQwp/Dw9kKpNnJlujrO0fi3QmzrV6ZUV3XwCemwkUeNXr1Mwzcj/2R5HyxdTr0DTP1in7NU3jm+nPyHqnA92AX5LtDpHAOBYypWZR5moTixmvnijbCPlEDlpHv031BNyDnLdz2Dbd+8yHQGzAfa+9mdJAycDfu04+uEdlyi89t6AQw1r7kIp6VMe8tOgmK9sM9uXJixh4Ij/uYuYuRAOoktLhPmnGf5JYCQdTZt0diNCenrlKbmEZyXiUhdBpI4nfAerjyaX5d04ukzBbjVFioMbHAdt04BgBZtlsXzGJ1HWsdI/TevsuKZsK1FcJfIbwg2CzcLqmsV+h9XgXMzUtxLi5LsETGpbBYHV3hA/kwJdCYb3SzuHrpJhHbf4nZDumdQjlQ0XtspBAGkiHotK41n7hply4Vqv210JK2hF5okDJ2nHmIp1SMn1xNUexRo2aXzM/QYdsBZp9quDal7xDcs6CAB5DFY7Om/EYSPZDPFiFSFsIBjN50+WxocaDaApetDdwkpaax+HTylVAxVU13CEG5xd9A1FEhPpn6yMP6Y5GUIGlSdNvkIyOnS4hofrGt0TH3WzPZ2YwQ0cf/QseqCp05kmFhoIUdXI7KrG8/HFq90gN8Ewju3+50/o1vvdXWEVSEyyHVIxz70WSVijgQbbLGT7ZELgzJdLQ3Ao24j2/gA1K/sfDlUqLQLd91dYNmVW1Q3JorIyaTyLfhnK/wuQux8JddxcehHwFyQUfipiRJS5cwxJwWtmnoIm+Z9yRqZeAnu8sW0BhMPOxYKUVxCwih/vzv7eUbdkdgZYaa3w/cHaxLQe3ohOenmMxWhKdBdm6hWnLn99KAX2sniMOIzTK4anRPVih0pCYKQbElnlLfnSPxoY4NH9PR3xjNr9NWRqCo6eGLkTGzbvmBwVVkoCTjh74Ic/UqtEVq8tqnnKEVvzQX0ADYm6W8DcBUDyfK0kReQY4iJdAEl9kyG28+8l1Las04Fnbor9wD4eHOwWxT/k8wTyrsSikEHzVEREVhPe70XyqIKL5mLTZ9yEFuxI0RxEdfQ7hYzPgwWkT4GK20Xh+T9gcWwrpRUj2FkxIjdagk1LLw/4AC0sWVmzyI7J+lgQegJa+hXUtpEEmf6dMdIEf6ZvNUZPFs4ZHwcex2mn8fnci+3B6iTyUuKFXhgChfCsFxT5bicOqupyRy5fgB2ZqMGvxkFeXXHxkB0ieY0RJo89ls/UNDlzKywHzWNsjuRe5KMag8csj6bW6OvPkiv3MVgXDYVojTZbf+sxbkS80QrQymuYOmBFSIlwvt01iYOTHbMWidXat6dQhmO78bH5omeit4QgrsCzeBYlcKOQZiK1Nm77CVuIaTEmhsRQKGPjp6aqLIfXheZX2d2N26MNvBp7aOlZE3glKOWvweHpWu9sp2l8h7+IptnVbwWAZF/Rt8bTZm48P2esEzWPPIPr5DmPz1HFwMWu+L6X82mOVTxHd7iPaVOHHDNgKAsFAkrqfxb7NTKVVPXH3zlrcIr/RZcvmRBT9qVuouxSvGz0pFFhDHcRiaETj69Dijlqi5ovuE6sbLwsKt47B1QfnMlFKq6B1VyUYthAKgBfvVCKkhbuRhIZWnrv/7UC4y9jVwv53PenIsFBqABrVhetVe/GKXMi3T9+wfyBWtxrsffC3bjkRZZx9bJIB5vJWMd3GkctKIh2A07lXwHP01wnpflp1gPs/dMmV9xoKLvdRaCXNpKfTdM62eUx1hfR+wie/VoQj8mVomOEbeu7RY+7t5GosfWMKg76GAvw4Wt0FT1UOnEThY8Ol7Qb2L6VcJPFSBPnppf0lVZ9iD+Pi3amKbPJjzEcQ6Rl7RX6la65RiZeGqcYrgd82N8RJ+FzRSuen145ncLFfzF4Q5ASXB60ioWD44IDcOn20yEQGY8TPPVslcavDY5w1QnI8uqeCvQpEdG79EMK4H8V1OgD6OiAQS9NUy7TBMiFvxe8HzTv0KPfMeBD4SX8DTmML6UySAYiDNz2Imw97htnOyOW3DMMuoyKl/HuUY+M+wQzRrWR2o54ck+eG6yuCkyk337Gteb54Bm0uCDcCmYP0GXPazkRzaSifQNIFCnxZQ4jRhGLqmge2X/B9vNqNN+qbRTqLg8KwhsZVQvBgZZhJalK0TMIVYzkmUGsWXk4iGTMtVlXKei/OE0ayXfQoafSv6/PxAIeFnAxLZn5vgl8qdElx4kM1Fg0+kHcgaryxXHQBVGME3R1ojPA1+dDdh/yE9OojV9HNzNzY6v1nVmGKwwtz3qYL50Bw2l5t+TRwqZWUYjY54YtIdhnjlb6doc9+KH4z/duN6nWWCWsnsKnKuJgHJ1LHFvUEJPK5/XGN3KEYInC10+8EbdRUSC3QstFuo9egHD/YO+kltk16fPz/pHSLA+iTeAPAbeZ86uA2KXD1Q8UAt7OO3oi9azfXe5RVpOyNaCjD+CTSU9J1NveTVUf0m5UmmsNwkdq8HFGe81ECTqkdtCgCIc6rAdQqxwkv+bGL5cLSzF5z223HssOJiNmfle3iZcRWa6cl/GNIdZPhKpU5KwLbMFicGY5U1kzUFF3CHfjzDmH94YK1XeYEWvCnBs9yJEBjH/H6ivY8OtircqPL4ojyO0Xz8Om0jOIz8Ajhg4bsnzcE06/Zo9d2XVD/nIROtdKVNvBDBtsZyIN6lh4McPASp5hLg0KfHYMX1SJu2st6CEfnj3tCDTRygf9fxbt+UHT3OG5SuWSqfmM5UBW8kapuIpLuuaF96GGnj1Zl3EUc9/fFabJZWJxlQcPP64kHIRgaz67Q9wWrVqAqaN7hwhTU96SHgtR7UUq7vjXh1Jk50eStJHqcGMsTF/wilC28BgCfwIgwD5QagkM9EOnHQv/3nZr6LHZDqxNkcFq413FTftPZ4eXal8hlon7MIKcGnqlC4MCl9hYLpSkgVmrwO4dZnf6+TzqotzK3oITXj8JHLR9keV2hQ+3LhbcjOar5O928zmvtEsOTQv1Wrb2f2xmZmuYBMP19cWgBX5OKtxNn6h7IWTPKtaLEiCS4RROY63lxcabROJ//bvBCjxGF1l47YdYyb/evbniyi6NXFp6bggsZcLQd13XU/DBpHV7g53t3id2tVkiu8KjwvQXmA3xbXDrwi4b+BquXvVeFS3u0Jn4f9cIjw6wL3+QiKrYF5H5t0Tx5+trXXqEEAfQMzbWIcxSOQHsEp1nfTSLlzaZiKUy+e/Mz0tMd9dCmU4EBwZT9T/rBaLlzjTEuCCP+UtBQMl8qEnxK5NIci3faeKHgf6M5lurwiuv9y0yilDdNwNLYiUggDwDwRHu1BWSUQpOjkxmISh7/669Ojwgk2SBsLn64k5/t/1071CPeCK6VtKXKSstl3NzZJwzZLWOuTsEKWqogqbojZlj49cSYLZkw7ut51txYoMByA7E2oDyQDPH/BhhOkGd5GeDKnn3MrUxUVXqM3CWqq7WEhveQp08B+IxC5iLa2HG++2dbbQ003M43r+40f3ZM3+JkHFz0VZa7u6mbSe0KHNCA9scRsIvZlrR3Veiz4/3JSgRzLqQThxbA8XairEt5opnPTu/9ULIdlz+YyUJIq3ogod92kqMj41XOYNCgq9jgYb2E+9qjQjODUQM1lcWIHFTtd6rR7qo+sLu8ec8Ki/A284AiIhL15A3ONaZ8fdKoxl3NrOh1eiurLhPc2SyaESb7mTgodmz2ZVFpQT0znn4IU2DgnOY+ecdA6oMxmTBfky6mnhB2S14vnm/WQklzb21XDzvE9HqdqiLjkIItR/l+eSKx70GiDunX1msga+RaYI0OEszPwEoD9YraQwnoAy4mUQQQxZnaM4dvLyj1bhHvrIlbMwczI1i48rPq5+Ji/+1nQDVL9SXsIbIGHnbOuTtMyL+zSKuUtmxsJQsMGAcYxXwWm5Mu72PjE3Ir9tSyIA2Ta1xgJcuilEpGxnd4Dcezb6kDctnLWzzoFBaubQ+UOR6qdj/igNfFvYY/iPxHGp9ML/IgjZ7HMw9CXeDjm+xMEBMHrfHe2bcjMQ6DyyND+uGgVqJvei3Y3bFojXu0sxiWYBFv34TqhBQ+WYJOXLqAVsAnBUwAAFUA7f0bEDBwV28gwKToAzse6f41UWPSSUEZj2g+4KBPzq6LJxRJXuzz5U+tWdbXDK/VDhAo5IlDmeneagBQf6OK9DzIZ/nEOZl/aRTIb2k7ps3Q87PHD9CYlYBzi043Q4kBUZGREdpRLaGzl/SESgysgBBW32CJz0KVfaGkllCm3sGz0dYrkkq0WUo7/SQoGX3D37kYDJjC5LfFGECuwyZeckPXLWok0sORuo29plOeL9i063b7JCwxPz4jZN+n1gRq5xUcr7scud/XX7XeulRrf/YPNL60eOHmobclPjw2Omu0hvFj9bm5LasZDBuhZpSAOW4PlBYHqRZnw4/s7Jf7SdVPzTV0Wz5lKWcIuxKLLwNtj9nlg+Tqu+wSYV8Jmq7hyQ7v3qeBeoUxI3BDU5KXJCZEgEOFnC7HXL35RS6BIIc1VH1LmNDYXb+CVfVyyE1d1SJlWGWb2Yznn42cgRwhfXyB2atHsKp0v4CDiusBI5M8/YnKk/5AQ2Bcz2akLZ8YdSKjLi304Kyf5foO2kLAxsM/4s+7Llg/A01SZW1w+ve3wIFEy6PiNCvb2ytfj+DhN8UlUbX9evDtRHk34cgg0c9I3CeLYp5RQ78C57ywS28M+45lhIW6gyk97gAUvptE6PTUtxZBYHZ6h9SD70kFZXeGlEzLop+ZppWdDIvJTPYRpwXhwYU+Hx6UB0qILeAB5o+I32E8RvzHLtT4dwoLSJRLu+j0DCTeZA9k7gCqZ9CXr8N+NPfBGzgCQJnwBcZJPMiiPiegnw0MKFy4kxDhiwy4gnJyGfADU20bTqwhxA7elsrSRHB/Nc6NFW8eg7N5xlkUyXTQojUz08dKwOIOVbiXLCVSz3S46ulGSyMw/HVB126w3MsyAnBy7B9QgmOGvkGU6aM+rqEL/HGj2JsJCxXAkSoTFd52HsA1ItdSH1VfqH5DEtKcQMMNZIqRXy3Y3gjkTUk3wZQ6RTBIrKWKdhG7l9arluWMzUjiySUxuvu3x+W7R54dLu9/1SPpSLQcGaInsU6d0lH9BdIoYTdpcPy9q70HbLQmAyKlPUDOs80khVzmL1pv2TbCIiOW1cMs3wC5IhQZQKVs21P4kubVUtD3Al3yczQannmXLuxdpordytOVvhEA85Biisr2EzJfQHY+8qgusqMNl+EHa8Sy53fvQHXCctHET/Qm/Z+xFfO98wfk7dSYiykTsvwM4GlZmXJNpVeES01/2M7KzhZbkoBKdFOHEUOfLM7a1OaJx4pFbOpxWswvoZn/UyLTfZ5Cn2lTsu0NODT9OspKvwSJFn1zerhLsWrJBs3WQF9M5o1/OgQFnb0Il7ZBVI8emBirZquhfXMJK0eqVnQKkiWTqAKyde0I5RJ/fxLYvfcS7BEG8Rc64ZXSswt0Cguv293lNejWTIhjNM6mYIaA6MT+NnwMlcouwmSm0DUVf2dvhy5TkxdKgzukm2+1pAZxxwbzFfhbZHhL2/mwnCRtXD02i0NR/rIgNkXMlVNuesZtuAyvnSOXxycBU16dA+CFrUAWDAuIH89rSAXPqFLTCu54cj/rMztLYSCbrq7n8wFAzC0STFv16aXItTg8UFXXgQLKdf0xmxWflqHW1hrV3O2BRe+IIdFV8Zda9ewI4ty2SXXhAeClcnDyvinc6VFpf8d712+ax8hHih7ArXNYivjZDR0In/Uxfrxgeo1intgMSGVdj5QgyjJJuLEDxGsvQwN4wgHMfdQSUw5HXfHpR4pOSTsRSn9TadfYTmoRmEO+PSw9pl6h/u2Vw1se9vNgzyP3HPL7dZ1J+eHV6jWyuaHv+Gr3sR8H0D5pixT6lFsJapDjagqf1BRYZtiem4xhXO6+bZuvn6den9+yZH0qzMVGMVE36AgVDDvTfHuaKjHDw5ZAoifOB4waI8dlNUqdxJNhjLwCOaNjna/+ID+icdj2kKNYqTn260t81x6Elt+fh68CBK1MK0USp6mP2qoTAnCDvXkfRt+EbOYxqnzloGHJMHaHvYJp2h3kqFRnujAnGgHKfGzz52mQTUk3PFevVLHeArrhJgF4beYReh9cjBt0kVwj4ysNOAT56qrpFLIGGpp3bX2+H4BajtOEsHrYZVRWyFOAMmfEPfIi1ynwE4bT9HSBXE30ahy5M2vp+mgumiUJ3Slq0rrH1wfmrvX3prVgv8s9JNLUF3O38FgZybbmbhoEV2gvfoxTsAHKE5igXtHs54Jty4uhJWstEPJuS+Y5TXqLR3NiS3ySwzLu5uQ7ETKLVwPL1DzurzYvZQl/ULEgJeramVhms6t9E5n04plr0J/OhZG8N3o5+xFo/LX3sDO/7phIH8w+oHiBwnAu4+SWSylbbmxWcidP/XMr/rf0PNkF2VEu/+gQIrjlqLGf8UfBZrKFh76uO9gr0iiSvrA3A0e2TBeKo4JFbkIsLsFfaREBePKU5PYGsblsO3ayVab2qJ+YEjDZpEW2gsOuPc9HTv0N+LVzFtxNNHzbNUGQchfJvAEfaZPgRTS6/ivr4kjS8vhi9a/jlxY1tTmUwZgyxI0mO7JXbRc73wZuFuOKHaakfAwAFnaLP/opJj++tEVFEQfx+j8pG31ccMpz2XxMrCcrRUWWemQbDxu+uDbkMMSnlkndCqEo30a5kzdBkj8LOb58fSb5y2mLGhA9Cv2OqGOLTnSTCvM4CgxSlcVcAP4lYHN841dkUbDEd/btiRa9WvFLexi+ym5X7lObRRPEYCcTvZYfESyRCRygHiUV0nHrSEpDGfZ9kjEomBemO6d1HtA7mZW5xhEUNYL1KywhvC6+cg6S+ojCG5QGKJU1uWMuxrGUY6uN/mo+FBCY0qekBAMqf1U3Igb3YjzZpjQcYc+R5/zYefYXSZpQ2W76Dfcwj2dmAFhVfY5dSa7m7kDKMR2WNjdBbwDz5UslhpFTbiwKa9FccUQxBKxJUuHEgcJqt8RyJP9s85AkL0GUy2iXw0gNVsCBs4leuGJsOSryz0SMlAAvsg4zWRqFFLZ1Az1OiwDMS47FMH/aSicTzAWxlnb+EhPuvhmFJ5/cMFyde13pwG6wx7Lfil+kHSnAUpWRbAgIyQPEIwQq2pClmTq28Db1JZO7Rqt7XE478BS+V7A9EQDPZ0nEZT9y1Cnb+uM3Xof2v87pozfTUFRqy3WXHai3jItsNeJqAF0ANy4s9E69pyvCN3n5kIOhXReHJAoPBvldevUPF2TnLWb1fH7YzqefnymGYfdK0PGFALq/HMZfEqMXQrhNCL1Bykwai7l/hVEujJWL3Ci2Irgvtc9WZNnQtPeGYZHx4fsD4d1Vyw2v2Nv2q7eYI3gcy0ATeETLBGBJcX3BFEKubFDoBShacqtG0xeebozWKPmRgponFuTV1MVOP0HDIaCAM+aAqHn+rEGQ2e9kkDt0qk28eYUfBpOTNFXWLkwb+/wh4hHxpsXuAdvCf+rL8ld+B37kMdHB5aqzuNdWm31mG0fG4/rpWx7R1UQGAVNkPftN+/27zVOPezTvop6Sd8EXf2JvxZO5zyfQKFPSA5nlU4NHC/yU0D52nyNwK32NPNjOgmF75bcp3v5oDy587T+KziO5QSCKggdiQU5Lck4iswNEFDnD6Y2r7I1ctkcw/71uqQRvLP6mtZpx/8jLLbfmk8CqstggCwZpSPclJBkwMcvTfvkU1ldPLH6CSDSNACE8cWcIYdmnGbDmqWY0Ei0UOHRxKDvI2V6cidaBCxE2GjglfkF/EF2TNFkjJWDhUr4+zRY4R+zmYdzJL5tHdP+Ys9sa+GIiDoOYfL2dYUFjy5KX4Tk42hjLOSgT+wTCQnfgPiiZEX1p/+EtxksHf8LwovqsH7sD3opBAkYqPLBZV499q+pJvdlyKo1JVw4E+mrB323FKFI2Swf1w1mpF8xzktswLPFU54yhKbEaHiPVv63EifKPZR/FaB0Hnk9fqV2/sM/ZSz0RqwtSS/2mwosce3UX3TDHOaWwtniiXqVYnwv8AY7iXeU3hOqNYGZHzGxfrhO7uU4m8wq5P9ePTrAr38meNLZiGGQNDHg4O5YA+hkJ+igQs8lXZl+WFkAqHnGkE0NWE5cOz3sW8RrMblb2NyjF2GU4QuB4tvIIpmOxdN2k3y4UjGL9enBgvn7jkb34pb5lxzwWT3o3nUwgBQMwoX1k74VvH+A7pZINeX5g6pqJ6IGlvMnISmJPFZVp9yRXqWs6sGZa1gP7BIYihEi0XfC2oacWplx7ad30/NlWwHeC5cQN/EeQVwDHaZn9v1WKOm+emV37O+VA4BGUnlt/6vmwIBPyhRgA679A9Ut+eB9UbQ68zY52GTfTsBXTQNwOq1EduOhFmnVQK9zNqBepJKnVAxlRgB+UC0ApA6GK7ON1mkIc/PCzL9rKiZL54jPZSj6eotgwhY6FMf3XfxeRkyogRdMao+b0IUC/LLhAe/dN7vxf4m5E4uiuy0WZ3iL2n4RQInpV8CDiVaOHtOXze2G+sRd/KdfmjvnDsIR3V5eSqJACUFANJ/OsXf2UFE0l+BgrZ3taw385YcIi9WYDy4/v6WzNJdo7xoxLRHbJjDeLB53pJE9hqUS5G/Cz1cIZ9gC/OwKthJsUOLUBxL6sk0InpPhRZPl6DJd2QtBffhBfaRmSRCx567+AcrNanuKjmT4p2S/gysJaMpA/tic47w2Oi8BGwL6/htmSZ2Gv/ftLWL/3UJZPoiJ9PomPsW+VNkpKNJg/ojpMj1Uqk/GBW6fxkzYex+fWQyop51B6lzGHXneVK/TD9lLSIZb0PbtdcNMZNR1jjLdXx85BNPgQMUeh5Q4EFh7D+y8XrTGwLLQqXtlTYZZ5tYgMyt1k7qJG48OfACi+HKCzxwli43GvPFoDyTOd1icihPBVoneS9uNIyrFqsS1uLZ5dqQMv/UJDDQZ7/frabIIdL6Pqu3RD5L1giC8J9FE6ZOekCrw+4cMD6eQQymSEJzPKLXYywPTLjlBPO7otfMroI65Yb1UyO4s7+a15sU4VrmGK/S2lsq4hOUUk8KZKej+knyaXaVUDcmiZW6Z/Qeij4HT4Oll8/eBXvqWTO39mdfO8DtpDKXGzY+UkinXNZL5tz3B0pi50mEclW5WppNrKiBuVHafC0KvktK+xIs1M9DYNtLKsEuITAmfA6gIS3b8J6XjdcXmisB6dlG6iOzU1UqVwdc0LM9WXP9Q4Ho6lVc51l8Bc3nEg3SMdM4NVWmwn27OWlnznLVfbghR9xLc6L7wz4tG4wRn4m2KLgaQz/mfAJtSghm1jg2fGTkvilFwbWpqb5rx73MmSHf/1o0H+RCmczxeBqIrxHjp9/DZaZRNqLLkHY5sMIgeuWisL3DB+3wGsvcWOBlTbiApZsSCcKus/5HABghq3CP7sFXrTH52L9TKRma8NEXydl1A5udWN7VRm54B/+jTbAkYgouXE2aDNlx6IGFV5kHIo4LRyY99y6MCos+NYkbMqVobELIQRMCKFLjt0zu7U8t+htjcC/JJZRayo1SkpOCbibnq/wsOqlAjzxHnOoZhePy2PUGHsfuFEhp7191AJNWu3YwjWm826Vz4hnbEcUrvz96+qwMYpm/fMxia67rsWjb0zGtSEk42+54nFjbcxkzMmkOgz1x8GJr9Ys2GR3qoYdFFnI8PVV1goYIPA44gihMWg6pw/Vzy/Xi/5dmQ4Tf6QXtwIZI64UVvBMRPoIVd51z48YY69k27Ov+HEJLE+hZRxvv7RqWg7+uM7UDUgjHe8jfG9ISeRo7SNoqtdrdxvJ8Xc9jRszWlvVdj5kV6FOqb3qRyICCeXBtuDZahYAwtkXQYlMvwETJUolAhZ35u+4TyhSnmo6e/XP1yQdQwVIqGdKBGIM5v+yJVyRJRyoFS/fiaAHWInD+lzoYzpM0NQfuQxXMZXSayi8JpENse1tIdfb4MgG1W3TI7TcXmJiP1U6Hg/do8yGDM/CFauD62DhmjSBCxUSrw2vZPphN1h5J39apwF9LYm9xuunQd6aynXARM8f4tD1P7hwScNqMEamEngb3Q8ikQyWZih5VtGRqcR20tzyJafmP5BGcUzwvG7H0PeXVuGF10ZfDp/WlDE7Kdx/hnfSWWiT44/QdPZdIqsTVV+1SFwL7V3T698WFJBfgbCBxnCYyIsif82aWD8sYo/T6KPkgN3S1IJuvx59OuaLx4CMVkC1pC2eZdzWp0N20Q9hp7Ws5vIIeRHdmV25m9i6iWOZ9vZgq65ZAj94sZ3mHrMefnG8KZPVQA2QH6fFkDhTrHjyOFkuXORlNE+rJK4pC53SP0NM74s6dIhQmvM7HmYFUX/IkNAEekB25OOHEisBFCqeNKtVDhlTpjsEEB8Ic1J/RoMOi8d2N5HrR62HsJHGrjVG5zK1WRLPoshOjBkFMsHhwksd91jnEeyb8N3V3hYduprFcGiFpNMcMDnAma6DEKR5qh0+kaBa1+bQlc6fFAt0d7IYIWJHl0sr1Q9b/zw5H0yt9e9zkWey2ITwFm+W2gV0m/xuETkoooK0uHQsPVJNYvU2UmIiKHL0K9fvWd9Qq41f+XX7yr24nScmMEN68ICcDQKaPEhrvZhpJgV0q2rMY2RsCyFi6zgKnr0Muf+zXJGHu2j/EX74VKpcTbwsmNkuuO50LMjip6m+2zilCrPsim2Bg8XU8TnD4OMjS32TE5qf5Elal+lZZ4Odx323qi/NdP1JoqZagPh5rcgiTyiUQF9G76JFi2hwGqGV+Lme4l1+j6kARa2uAMPmvUXlGZp6fv/3fc6ng3vi0Nt5/Dml4g4mcBVzSDUT/L7vk4rBJGgR650GO58FiRs0wv4iCmgION9uPFKkZ07ICZfFhJ6VRL3lG4TD3tNfHos2ZGl/mCoT8lt4YzIJvEYHjFI2EX3ngyl6lR5nOoOyG6/G7MNYZoC0WNAjCKksAIkrOk8L2IlLp8IUCggJ8NgYCOSUHVHqIFtZtJwSd3X35nov/PF/skqZuyxwJ4JtZ82pe1nI2BM9JswQGgpIJ+ozxLxnaDsp7nR7gt5/u6sxNHTBv6kXBGT4sUr6yBunh5DL0AvRhsqbeFZ5oH0e5kGGu8RU0M0aH0+Dpl7Q6L9+vxrzzdzI+bWOvoES6RQQyB2+5yxhABmpkg7I7dKYYIQYMdtFRgyItbJ+qMNzhfdeaQ6O79E891N2wz36i9Hmri7MEuttqJ0KX9wATSusBQrc399sGDFOPs+PiaA3jjGuTLRghNz9AFXnfFQH/WHWoo9wsM+vU9IWfNzYITXzCnFZw178slF0uzRuqja7CC75qupH/GOkAePVS4fx85enSkYrcLyzSlMYuSQtbtinijKf6oXww1Pb+XUIz4o+QW7Eq9aEcnUOtqiXCoHpKTm75eBfwCNAujk0/fQFMTmIps15BwYfSw1Tj+V05GgHikxVLQHSDqbnHf1kQMYA9j77Bt3FoFSA6G/S4Wwh6PWZz+juUJeHZv4IyCPQv0hy/KlZOO8/aklB1RWtCkLgIyuIldBCwhV5Bp29IRnINmV6afAatb9SMzLGQdeMY/b1m8gRfuQNYKiL2djlAJ9XQdOU3cFIzaWAikft5AsbPkvLcihMMGbb8eN8/emGA54WfE4aqSWCAXrLIkoCIEKa3Lj3iGHyiFY1d4EFig1/xBCvuM6WkE6dpWRjfZbi0MFJGcS4sNEMRYacYVkk1WkDH5zqXIOKoh0cF/nU+inCIjj9skbvMTYQLzWUbiZj494glpZloqR8P8NnATtK/W/SwRbjLhMzZ/ZFApUuw1jGlO7ayfWAuvgz9r9PqoSbpbaFwi9PqikQLoS6Z7/XEc8IyBBg8h0HQkqqExBLgc3HYmUd8WXwrH0FZbo/lH34BCtoNamoh5t5ia/5XNO5TrmeAVuZ8qLlaDDihY/9dyeZSoyPQQcKqbYjvJUh4iS5wcDWz8pVgmtyhds57nLsvFeBXDagMrNd0SHoKb3Pz2+giBX1G5O3VYp8YKCC+ThvcO8blhyeXWE/wITYWqcm0qCzldazAcYsAkJGdoGnBNqIRLETkQ5U3XtEI9kjn6E9y4msBZx5Gnyd9kcuvhK99IxlYWAktRuiuF4UwNn0ejV6QLhsSaoiOE1ldD19Q5O3rteszwonpT09tEWK7Tq/zuvf8n9M1CIZn9Yt3kw6gjzGQnRMymhwpt3hHrpOFLeFJYy1EyF39Fa84tSgXjWOPHWiGhLoGi2CamfuZvsJwloywYNx2LqF/iepdENUecVN0cps7eufyhqpNXHQ0+YA61kJ/ZSunLzLYtNenFd1lnKXhJCtlBkY5mp+zwsYNMxPu/F9xgBUhz700Jp9LwQA6ZqSdOAlXRvTZMvUTO0yAgD4OFbc/645aQ4VPUrPzslPOYi7lROLPjR8J2FXdUNRDHhpiCIvXveoeGev0MFOjpwGd2IImiWvg1Wk36fM1gqFvxW2gP+brWFDguYPqHyVplRul8T9z7Hz9ehAY4c8nqjUpgnxPqseI8PhMuceWLf/bbaE9Tt6vbTUZZ5oyER2xUqS7ASN2tqTxTtzcMPpcieDSDBPg5739yJzaXyhQ8ADYzyaTiQwBtvueg9zSKueRPw9W+fFzEl2rh+Z3a36lXucyzJqrNMyyzEnduzTvgarNmOJYIG/2zXt5gbGApqEELi1274LvFOADN29dJXVJ9ZTce5OLYhpZvpaM9oxB/46oL3b/BZWQwgmhrPz8zq+iUx1agLppdAJbc9vdEvTAeyM4VXUNgr9FjeFJIZWf039dCMURpcn75cD6J9396Q1nIWqtdNxpQGTCt4Zo5LljNRhSRbxzEqEvD1cfvQeUJDze08slPR4xC2+5I/Ng9s0aObjAp28l1+VYutEZCCqJAKUO+f/FPbNkcKSbCnv34JdY5NByltWa1apFtUtibnqNqgOaAMNFclknFAB/DElY5gPT3IP7ydC0S9afen99iOdFcqOVJ/zmUUHQycbbMAd8DcyPx974Wmz/d6PPfxYOkr8gSWuUVhDicr4FAVWSDpEB08Zgq2lcCdkBr60iZ5RRn0E0UiWAIv6hp4A5CzgHEzpnKGLYLSmBdMUJCfkvwiJFzvwaOUV9/8ck4Mol5jQyBps0eGD1oLV5xLmPMIVUwLJhQUIltGT+eMnUPTFgTSDDO9YKb/sXCu0/KlkXx80cRN5BJB6GxvmJFKU7QYDaaong8hMG+t50zWlNBPHmB3w8+fT5ihrh5PCLrJKhMBoY0PDXydklvh/n6/Ij4tbo6Qdh10haNfdv7HjYskXF+feRQDzlQJrpXS81FdtFXF6tup96vUWyIJButPKN2ojBvupwZFhchdNaPJGOYqgHG27df+zK61F0OfCRN/xtK3AcGOndpgoe6qC9qCxVU2w7dAelx7RA4yWJDE8gDivDTnQgQb1VaaM26W0m/Us37yCkr/KSywHtlfLhUu1vlNa755CAJGW3JfFpsEm6V5Q1yEbsuTqwhamjw63WYOIClPV7DG6BnjWBItjF9mx0fRd8ndUuNbPhbSSd8ccDGgbPFHNpBldpawfa7L7wTS4KsWvcw5CZ7VRryDAiWFqb44jbkAoXtVoBKaKZEKFYx/4n3YaI4uUfmTdPDP+fJFZ2Z+buFfbUFJqt8h5ZOUwAoLgPkBqVGM0kHLvThLaFPPs9H+PVrZGEeb589d+1T768K63NTV85qW+anUxxLJXiuyPJuXakELZdlsZCxVlNDH34J1RnF1hl8ijodzVzOk/o4uD/S46rs6stp2/UhjtRQDfBdvcN2yp8kyh8SV3ZPiaK9S/uXlgZVOb7PuONcioQFXPg7Fktp6wakMnmHTJ1G0g9QwY/mSw5BNWjZTwGx0soq0RYUWn6XHk7WSev6TYIwB5Czev/P4taUlDVgZ8d6ng0WP3u7xKSPykt8ku5UU/BLEiFesgHQ/FkQnELJZ1JcOjSV5V5jd3HrgevFWQBYz0Z7b9W4Bp8Jy1iRYnCKppfruNX4fNNk/0YUZZnkD9LokU71XqJiBTbbHFvOx/l9ftqWPYxDJvQAQmqUgBfY8FuoZATtLICNB1oBUqZL2WQN5AMpULoOqyuyAA+ft8Nsw1/3hV80CipboLcD3DfFBKjmUJbqOgzrsTFJJUP4iZtX3qIx6h7UbiA0fLZBvYuV0OrHp5e6VhlC7ZW81+lOW6R+l0shlUS7/wJY7Hz+gtMZgGJdGANhCXbk9sr/InYyxP8S7HHA95WJHHBCIAAa5LTsGb+leuHIfqzNtps3YEkD+b5gjXVHKp2QYxlu5d5G9bC4Pi7/EdN5xsH2m5ER1z5c56KjVCXl8Q0vt+W3ufU3Vy9nfFgsX/cLpVCKb2h3Ara/m8D7AVg+RwBoQ7Cbq9dN+bR6Rjn6Y+Qh6Ju1MQs9ptxOI4L2cvGbVvfg0RKzyRiq0pglXUVuDVDbvJkLTL4bLapCC4nrPT/eJVgTYZYbziyPrwHbbSZkM58LKaTyiCXR4Ktbqc4Tshww343LlNZVk83UH9G32EbPKrc9se4egHFDIGBTdEzUgFldVfiLmjMZwOJGHNK8B7Xz4WPDflx2C5pLaTsbSQTYpfbl5CaC8LULbKEiK7mje/ccrlAoc6DfuAbyXyODpvw3Jt5UV+2d03RI/jM6e2thWzCj61Rt2ME1rfgGDqiB646lfx76Z6RybPqASUWjr8E6i/8pMBVHFFhCzUNef6WhSYGIUGAl4ZP8qSkClnhhDs6TDYYWrCgP+Sux7rhetF4aHuC30GC5fwkLkQW/jAgUSmSoB0OBiwzRQUpHLib8fKm8pmuqfxWQ0JQHRFLNO/d2fQlncWYhBkKdTIfqQS/i6B3bjA718W9WxlFp3i6WwdlJxux94N+IifT3pLekXQMS+V5mWDxmO6UKevAw8dhTr1b3svsIuyTQP/igXAq7/l9qXlTgWSnzLmClB4K/+8Q8QLzuMFxCcqcpssg/taWWAaUA3lQizvBAte30WCdPYrZgf5gQILsPQE2JcePK4bYWukHxmCQCFb+TDqfrVKiDUZnZ1y2wzr7WozIMOCJ+gt/P6aXqeMjKGu4vbD8Yj9NECFFiPTL+N097SjJBSnNIyaH2FA4B4Btv11SFEgV1LhIUCkL/+/xsuQy+KMGxi3ylFqvWabvyhqaeEA0DSXG+nNgk38S66aFP8VrrC+l6YPd+0KuAaY9tVjcQk8vnjldloaipi4B3JLAjPWjCb8qy7d/b42bdWdODusclx31No74G3ucn6iTaBYH6IAVqSFqTcR8IhTdlThn8s2CTGRSs5U2TcE553p5fwdG5OB57qBG15hvLGraMJEVRr6jeE3jdUeY66NOgOPo5sXvX6gPt4+0UYoax7at0ov3Ke6vP162eWtuHhms2RQtY7X8eMRHN/It9eeYD/t4riTwppV47QaBDAUho50eXGoYkQ3H3kR6IdKVVWJK6/QZhHvV+jsoAjOXo1lXJCMPmQ8vJx6ozk1j7PNyqFIRqmRVLzd+Ph8mmaRdYKrHhYzWGwzx77NJKibEXY/CSRyEqa0BYguusQ0TwQTq4Qd0MAoH5E+vUIDU9Y28Q+gSzJX+yR/ThE5HyUgMlRoZRN8Mllkxn0LZUxom73n1xhXYm8ZQXLlFchXGKKouoqGcKh88HaSrKiK9h4Zlp6Q4Nsze8i+tNGfCUUIPoB5d13z7CfYdz2rdk1jBSMgD20awZoi7XKfOIY364F88yruvRY96egDrN+9p0PkYg6qNZmgC/t1ozdYfLcPvoToyQaECOPJggAamCeS1KDkffpM061tawjnIDB9dP8OXOuQbxMCAyo+SkZ/Z18uuYmW4t5zuHp4Af00NiFOe32FojtBfOdHNFo3RUbsKKB4inQQXPVaeIL3Xc7IGuGOmL0C+CfAVXL8FnAPsqWZlLkrdMaA7ocijkJmCpT20oURFwcIoG4264DhYIC0H8dHLf10wkU7HxaZ+p8hKiS98g1Z4k708U5nydpcULhMJNIdrGatxnKZVmMipoJ49O0ui7+/J5VKQN6ViVTQIBVJzVRlecPaF/kfh59qLtnUlRdqwBJrGV5hILxwHa6t5Q/wZAD5bbttk1tFHlh7ocTdQINSdpFhGvorXtFJVFkDL5DzHwPjcKNFZnSwp78KmaaHXlOBvBbhK0/+uC3+3yXmL8LePeruqpgDghLovN+Y9YS2iqayNh2YWmc2wslowy8LlGLd+n31nZS/viQWwWzPDk3a0SaEk0FfLwz4V0mQAdaVx9ridmtpoKx87cv0McI50D8sfqdKWQMQoVPgg13DIVfseYBkdrbqI5v5b+PoDkyLODuROs0/YRPhZ6FeGbtSsmZlcmvzDDxCvaonO3qXNKDvTlUH275vGDNafW1aWvUmwRM9iPKlx4RRHfbbLtQ/YBf51Wu5CVIOHjr14y/oy/jFPutS+JrcGilkWR1Ku0nPUhGfMqXmdVmovxIqrNuGvbFJswJsDt2Qi4Rf//UD3snERiv3s54XaTDZix+LIBqkNSypYCA2URJv3otXP0tIfv//njkr3qsOW87pUttQFFBWUhb9D4W4FWWquTVzjGFmRJds/moCeuvP1Je4d9cdGQ0arO/IUQqxusHFvL+00nHraZ6Dg7LlhQnvNqi8eADFtdoapNw7uZJMkoCUACx/IUM1JikVJy0j4mJiEltOoYUwbP1TnV2cxYGMO71+8ZqByHdtRYokN2+CqokJpQ/yo+n+bCY8wMotoWYPiy/dwipaLJMkbRNwb4lq+k4XoTdDXJ48Fdr0GamyurT3uNbzrhTQux4HH1BGTzkzwWTkT8eR5fPSq5Trs0KFJV2RdbQKC+/Fxh1PDsWxmV+B+AXzVzE5dyZPAOUd2yhQfrMIdj9gBeeLpseNPzqA7oPGKB+yGA4ZDBvtdFuANCXeEM1lDJMZ1atOEwU04XiPXk610zZQYklUydXv2UmotexPVD9rS9Ym39eXSywnKjCY8Q5jJdv9IEjAyXvTxSdr/QWLbS2qhD+bCdKHJomWIWpRgkPs627UcP9lq3IxRsz5Dxanfc5G6O8gcDq6wyA6+EubmabZRkmSh3HHKUmHgfkl6HnV8V77xcStT/v7uRJOCUqK1HUhnn8XnA8J27vK2unmMP0TuElhepz0dUv433/RjILDXmQMlkK76hlHsT+RgwUQTZ3VJbUY2sX9OskPMH/S0gPqcnL4+TL4S0JyKPQ2m93XZT6RryelDlu9V122mHSa6EtejLTLGsEfG2UKqKJRAonogNeLr/pkwVETdvPIFSmYMpUDBE5lVjezGb8Oa71gERjJ/Tbgfi15nnxI011jynYh4S2nzbbB1oGJwI2tLgUzwFPGwRENqhjzHsc4fja/Ir4/yQxXhyBcSckhFAOnpog3RzHadF4XSAJ+9mdiNRMApE/DdRUzE6TWhWFn4DL0sVRBqAg1A3F9wBOGFixYmt8ahsojqW2/ue3/S5n+vmIzbsOMDrMdg6SQAokB7iS7vN/ZfQoanhI7oVjDbp9zRJGe0fj2jzH0O1re166TpTi8bvn98kPrcXyEsZNMW5BLZK66fpeodM2jC8mw0cGfE35LtUlIfb1C6SQdzEvpRSwU4a47nFFw02yQlVKWmh85qn1KzSlnVGoWecRt0E1RiYVevt8UOqUqxXWgSFxTSQte46w3EWj+hPFgd1T/GNJ5bqmyBQaV5dQVRyu/OG3AGDtD1bMxxLY24f7eKk76Mcwfs8T4VM/aUnkYUcgSe73pAhwYJ/DVgLOCMroyBiZHVnsTW3MxjWAEn5iojAnU0UN5HwjleuxQps0yvHq8SHgPVxpHmfyaLzzDm0qjGogcnPh7kjFNPno9kPVTvH/Yo09H6ch7M7UFyH9gb+Ram6SQDlzIPD+9Gk+Ww3ASOSiPiQAjG1/HCWRXBZaHBFU8CgZIAFLs31iILmOQa7xX0RKRJSGnoTKdma/sg+TtToRaeC7JqDcp1OiueMOrtZc0IuPwdG/EnQTDK6hAF2JJd2O5C0vzwREAKBA2wD0fFKistqoQwnWt6+6kTIm/xAeAAYoA2N1jV3VMEBhn/TjLkLfIPejgwpgsc81ki49ySDi58JqL/QmheUA8OJj9z5e+fVMNucO8asAPCfVoXyC2JJh5qdyfA097x02gHrvkyOL04sRSR0wjAXBA95blV+9Wkeg7VdlnyzLtZThsfGhapWoC+7HYR5ns0ixQC86bL/jpZGXl0HMBRZitLwEcneP7qAg1PPMqryJPZe2pPic+tLZmiyDYw6FJXlEejwrpJbWPDg/Z41wXEMBqkZE/YSsvHEf/vsiBxi3BUhDzan3PmdGBHP3oFk6gHioqRKT3iPh87GFQwB9J6HAuN2+LujOGCWMDyhBV49XjGm3hcvFn9IpMVj6Wr9c6ciSkTwU95lI6q+lQZwFHEV4Wrpnmmq+EHxOMjcDKQSI1YjRYp6ImJm1YeW7nMEPm5dp7n3Nq6EK057HQmnPui3lJgW9wfylU0NwyqnUzViVzJcSruNIv2qZYfxcAWBr0soxf4BliLso44Ikk1SPf5d6NE6p83LsgQC6mnqVe6M3Ax3TgTfxzQIutSSxC7X4jMyHna+JoaPFvfzWL2rP79r8gJSVXTIiGhUB/cw+8I2U5JTilKYmEl+Q74MEIIacxLDIH1svXXGNl/SsqBr10YwuAO2gLZqu+1niD9s2LMyNr7AJzyA42EU/jbms0rsM7HfVru/VqRarqvaSbCE4hQyoYmme5jtCmZMlFdhx2EGWhfP5MZTF94azlNtSVF9YDSX29zaOBB5YGRWzxayEZIpUM/Uqt0bYO5+XLahI4yOhgXjveTNK0jQVeXFVwY220vu2BfymjtPuAHhyGnRkV/FNHcDifdURmGA/R1fBmw6fegPf7Qo/XGZA90iQK444xRrgz2LkTIqIWOOChuCmP6RJsQb6G/SwEU6joMSt+0SYSkbtQk40mwCB3kFEU6wiLNG7+P2OGay6cGlC0OwJTzbJdzxcr959PWXLIvNU9g8TCL7Jxfcd/pKP109YkbUfIpLIdafmOcfbp9tPLuPH4lNWbQUcYFu1jFSUiTl2Swr4dX6BGmmpDZTdhfxzE17xrOEAmMSfS1SNUprm6cTx5bZST67kOP1gPyS/SmdEpU0SAk6/RC4MGDkZ7/RhOouX6SOIUWekHGoLa+zCT7/rqy8P1xL3wHliu1uzL5TTk5Xu76zr/BzA/SyDO/MCLNohiLBDWzUXLdR/ZkmwumpdQLUuUy1CnI0suFPdx/T6sotCTRhhkon6HrAGx9xJy2WY05JYwu2xMgq73Ol3QlDZn/oFPTxZR+Wb8R8fIrkhWVrG2+r3oLxMkkJxM54UeGIC2Q5UECWfUe17ccByxCzx9vDIFrBDkMcTsDM4UlV8qaAu+0eP3g4nX4StKY9NwfaSm09FZhG/PBerPiexehVEfByyAjhpWc7QhG8GywiSWj9kLMljV85KGCCHoZbuoAi715aYz8yWeST9rCgtzZcMBn792y6ZinSxZiB0MW3kT0nm8oCH5aIs8X61uXZJzG35d5PeOAVqxwp2x4UIOg4pEJ4E99I+rauNWJpKUHzWyo0CTlI9wOt5sDZwgJKeceJZotBqsHzKpOIpFlre31/3idP5NtLXx5yPDCf1yuSj0nSG8klAJYSNxFicFpW+K09MakZLxhnlRYKdgu7swLEh8/6dsJowrtMHGmF4IFIgh0ImMhPHIOOHARtk1HkpgbjScEamZusehQ92BDVPui0RnD1+gqM1zDsWVbsu38ojtjkaUEgjYyqvdZ3mcujePPuwpvwFhUO/YeBrsF/XmZaRDWpbxKED6qZp0JOt8KS0Ou5wVlzp8Mcum2VgrsGdfufmAMXqoU4JWzkaO1Gml5HGFT22jUuCCaFonT71BKqoKyZgklGhYIrd20AO/vo14kLljHAxOtHocjcuD2zUh9Xgx3fg7o7I8E4aVBWh/0sFr120VTPSVwMQHNkrilGDAOZBPA5LIh+7krBXFMD1NrrGkFPpH1uF+TGztOmO85OMfph5mCX5GAcKh4sRzhH3O6oTN2RFv5UQv/DJgSXTbskjeRJcPgas/hgRtT6T6FmY/1OVbC3bwAWQaHsywJ6XNZHZ/KT4mV2GbShjv/vlKt6EQfhLm5XOKuLriCoQgBQVPzuVjonANHqtTUC4CRt9ZlM/Zw4L6nXENoEd7smzxczjhy5GSpnx+Yl0QinGkpeAqZPXJbleBODmF76+gsy4+He8GBlQMDgsL1WFgdtVVXq6KsGC2Hm17b1yQ0ySbFUO82xGIvEcg5Gfcrv1PIYgRUakSM1n6PoT/ySOeK2poamKSu7dgmW+6KpffTQc4Jp0TIIruB3a+WsGTmAUohq/1tZSs4wdWnrHLAfUR3CvkyWZqQbw3/0em546sl0buSaZL1q0mBc6xOHz2XCw1TEuNVdpTjOinkZCzVIVdZYmemDIJhabm4gD6XxOrP0Lhoe5FLwNprlP0g14t2gkdLDuUsbxh9g2j7WI4U7Sw5rbMbFCROF37Oo0zp9qP15tCazpCEapqCZiqSKx5LkF2WqrlVmy/6uCtL7wzY5RwID+ORFWLcaZ3U11lKfuEgPxNMDpCvUqI/RB6+affEWdya0FvwI9iRMocQf4p+lZ0z228jMGg1Y8IO74HMo2dN/NaNCRNf7U9JlzVQz5+PC1bEeyRf46HG50JI4ZAkrVEqBkvUYL1xJq3yqZEDL/evlUbVu2xhc2VMH1sxL8w4aqjIY2saFkHY59etIrx8YfMPuiLGi0bEDjF230q3oNewz9Pkd5vcihE0f02bSl2awG+52PhdVHIsImb0qGVXw7+MaLaei/++WVhRKh7QfZSpLrfxiOThOxjIZOtXMjlMVB+oZn8kZ/PbzXN43ARtGVdqIxlWAYbqTSPDJqUhJvPaF54lCGJA5q4576UydekpuOArhj96JZUkMGE4CaTaq3EOwIltc4kH76irzmK34omfPJFYgJQjiK9YwjcDwxMDs52WuMt3fosQsL4TO0C1IeJQ+cTvciD8+zXnk54lO9gbzyKN+rIJYy9qSgbNp7VD0xAA7B6wkt/qaB/sc+cYy2FJM7UKQHKRVadajCsSbUv3bLlhWucgaKZXp/b6Vf0fBnMNy4WhyG6nkQG8zJW2rSiQBA7rOI5veXAfH6C/vO+koi7LG3EcDoSoKITodM95VWyCn2n0tegP86PRsvOB0SBYZ6Xx70lwHtTwpbVq3WhDmgc015mogOh27PthIp62+U7dycLiZ8MFmoU34fuKUhaEhEG/Lz8YXXD5Xr5PmxCwx4Q2PbsRgkBoURXDhoWXwGWK7PmwWjZYTlgANPBEOYj9K4SQ0iiHwRfusZdRDezDkaWS+nmMKfVjPR56Mo/lM1SlOhOv/yUjNRSvn4kS+FKBHPeFf5pjKTA6piugEe9uen0MsRWhU+MmHkSDhSimADZ0l0qXf02ORPPBvRrytfYd7+uJ5MLGIjoIJyjyuEUnfkZ4hEySPED6g019BZzX7EMLwC7ZZ4HQniTq+7iha2FEsu7Xf7c+soLk2bQA8u7scV1WmJIdyiuDbq0IIwJ0YYLn4YfuZRjcDphr/2gBU4QsuPYfeRnOdryHXMd/Wbr3JhIKyplhJZzwZn6TQc5nmaZG1/o9Lbfgd7TFwgH2OZFFU9++MCGMfv0yv0j5wv927eEVPcw7tmktFHvaaYq09OA8k5L9iCPgU5/8KY6zSOhyIFxljxXPjig+oB++IXX2Xsb6oHzJexFdCGwkeTbtz4dorRMCMDup/W5lX+Zk6SZyt5lAr8CjYtlHpgFTCHRmEhZu1TMW0tvKGdUGNXdFGUJN1kUbXBoatmJCrrGcHGyvQd2E1L4sY5k98cTkjMKQ1CbMPEBX3IrWmwMs8dZGB2khHZQtGieb63Vyb0ZSW7RhAhjcFlvwUhEDcvX2ftt0WH+wu7E4DAx5RBspuZURQadVIJHn5z/zdyK7/XQAE24pS5WqnNpsfdbwzIyt+qwjxtAHywRiBuXnIEuoPHzD3WVX62ilZIhvuCx6+fchUjTOH7+xVQeW3tqMloD21q1AvMDLlW8u4199b7gGlB70uuwppQUv/cayJMLwfjsCvIRnS4680JpPN/F6ZMW67G7LDTBY5+XsVDYz5d/TFEepfv/0u2JbmymgA4PV8CDABSlpe1IiKNePm2X8KfhC9pNAW/d3PLawWCFL5+AnZFUYzGxLq9Fzj1zi94GQr0UhjOyhcEf4Etsb58wRMS0vPkxq/L6DS0vhI4o6c//Dlt1gKl1B6y6ANa3daFanjNQw3tACcT4keVMfiXISFZLVDGG2s3oRq2YQ1HZZosxKdyMYNM5e7x6DQogRT7GXJZmSVMzAmExCAm+jVeNN2TiGZ+XiurU0vS9GFqlxKF4wz7D1tpWqd236/GyOVDfUMWiaSkBn5oyJfB09x5w/wcYbk1/DTR0jnexAh0dXMsOFqmgYcmLM4Pv69la8c6QE4RRuHX+/OgAztGi+a6g+xqGNUJ2E/vNA2vyGMRSipMajZ2KkKYy3VueyhoDeAX1HUJdT6Z9IyQYAojffVHMu/t6QAhhr/UD/LcIwWo73o6DJFcHPN1J5a+L+xkkwN0hUFiYaLCOPV6POfwFkTkc50xbK5iiK6URWv4gTJAbTduJ+JM8jBi2uLa7/idEoquYCVzLrDhCw1FbRFlMDg71xZrxokJUE4b/zARxvloP8jYpFnpmzCMdOmBweHElpTVOIV1GL0gdPcHeTKhwpTsOxAfDYxX+kSMlj9zADSAJzRObiaIWsCLVPh5LlCNyvB9Df1LNhVcw0oOXrNG062jl5/c2zZR91H26Zc1frMhYgeRSnhCxdF9N2c8q7W7ZjrE/G1ULJOXT7UhlS3LnGN4edWFQMSgKC+cNZXYehBNHS8oPh/gz4Kt73QR9Dxii5XO2pfP1TdCUAvaBTDNShs4RlKxApKTzHH4WbVQfOFIc3FWbwH8SGCvAFjG5DOzmuobfhzpQ5eCyJPI9vD5RsRBMqAyhc72HAyxgqwl02D9Z4U/ba/6SRctd2bD71g5tklxxDZhl03W4yE6Re0tM99Wi/+LYZuHKfs4TyFzhZ96c00k7i0S3vhqmasymXmzWkt/pRYUY9JjARBcI5gp+e7DoSPyWSQUFFfeBQEOqTeVyyYiqI8+GUiiLCg3ZUvKSsNIe4jvtVNik4x139a5s9Xf0fWT9ryuywWf2ScGv8Xu7z0K+u5D/d2y9f6aU5v4NSiVzzF+5Cj7gqvTrkgYhcGX4ymaOWIuTVwuvEZYB3YIVoKtG373w/Tf9C3kehyujBnAH1FE8/G5puLJM46tD2SXVjxJZxnPayxVvXkpqaoW3LiTs9tBK7iQPEqNFFFhMdHy/l/ltpHoU1MVJ2+bHL60UM3OwShN4u5VdRhRQQ7qmB1Ada8seX17+Xi3oa28bvYQQU5JdGyDVP+b/S+o8r/6Xg6FMm4CUTOhD0DE8C98l8QPbKpl+r1e8LtULGE51dKm77M36Uzo6FeyFmixrRw1xJyKdWQP4IFMryU8q2hC7hPwSmSauFsnPei2WcGrX1c/+U+WzzD7LEfjUadBNSLyXA9JgbZvK9NGZMPUT0rx2pJk1BZkEQQoijqIvi4U3GffdNYny6R+9R0WLq4WkIblNy/bYIdBUcR24D6p7nAEX1yoFcm+xkSnxD10YabUQsJdCxZmpc4P8xUaKZhvgBMPfOr0XoaaT53xhw3oO3M91W/UrycSBiCC/IhjtmgibflSgNGQaSuomIKUv5JL+EG85eBIMgixLwyynrdEAYKDq6WlP25K4VOFgzpiTqZkQpsyCt6XG65bDqv0/2ODqNDnoryBN3J8p247deVo4zskjDU/z1986f5oGGm0UamNMbtKhfVdOn7Wpu0+CrRV6xg1bL2CgDtrQ5e0c+1MJ4tFpx/fUgXAgOgti2mZKVP0xwFL+7XLTypBzxCxEVtdZe1AT9mMfmALX9mb2H6ffiZWI/GaF9SZQVTN+0Pk0gy6FyFM0SbV8rgGbutdScAqq5COo53jWmKxJQctheOTDBzEWdTb/zuWEHrp37GRGaJxkzX/BAJ7uN3CqTR76tP1DV8No0RtDO7v5ZPvWbmNobBLA4/xwIF0rZK4qpi/9g8CWYUMRFBCEeadStMPSbBy7573XVtkXbEVL2Xf10ryFXZ8zxPk9qQQ0UHn6YIsslFlCU4u3LpDx9rX54nToyvk/2aA3TgNuq0X62JxoYag3nSAGFftuWwH2gf/akTN1Nx4b5t+DZLc82UDB6wq+BYk2haSUWZyMwganmc1NI30DfZ5CoyRsfwmVH8lh6cNhCyWPYfGezCn36Z/X0puT38EFPR3g0/9MmnRXl7sO5iDuCB+hnYQMeZMikBd5l21NUxLMVPx4aC8gEiXXjcd+PWItG6qv/IxfzS93PRiLsjeB+4YXakyFiaBZrL2Zd9rr5jFdH7O9Rju6zIEoAhVIY+AUqt9QSDmunSGUk1WTNTONz28+dxGfB9EeAHda9C579uZs5wYcJJDdl8q0nTI7MonYN1+yleNcstC3u9M03okPO1M4oLFIa/QmeMDWzT5I8c27KGA/bWLHmC+XxwsjvD5SdeSNH1aVW3xIaY4xnAhaLvPI9YUmZYAl7/HUrfx7Kxt/qJZcoaGjiKMbjjPoR4LhrAnco4DOXt1BGDT7iKY+PnlGbbcKWK2on5tKj3n4HY0FoTcNKpEP6QpAfX7W4lqmr848W3dDrYPvowP6Y+is1hyEIii6AexwG2JBA3u7HAnuH39MLupTCoF3f3uOydFuhUGt2DfTw9iVlCzs9Kud4DL6j2Z+F07rxP+R2K2XOV3H9BnmbXtyf4081Wa4dEqX6CG1zkcDmn7cbRtIHP6efv08xL9933v6yWLy3yqgsXHK0evDxccnzqAtNx2HDAo0Y20Kj0b6iIkxx8yvriTSexFh8jv7oNI8p8b1AKZQFHiK0ek/L0bm6wUnz/ngtumYDfLBnHBKf5/5pdjHJ37lqxDDkM085BqcJQmd1IEONvixc+ueom/ydnPKD35LteqBDdfdhjJ1cN404X9UzOjWT5JXObVsJVm98x5/sO+9w6KGaUahQo6dd5v2NkVupB/fYvrfmMfiIVy2A57msGr7EmC/XT+dN0rh76WCRM1q921rvs1llbRzOzAyfrdcT9J+V4kQuIUsioOXYGE67Yx3Hleg1Fd5de5/mUg2rdJsoCvubFElYElXM9QLwPBUmjNANEltqe6XFE6L1bkS7zqSwBK5HPX0Kh9Lw6/jaJwNO7mPE+qQYrM4w8+pbBjHVZ2tiNVLoSjj6/urPW6V7+v57ufjdSHF1+hL+BlT1Jv1iiRGxmZxhHmtU24gcx+GBZ5IOO1rQRE+bWoiUfIcHW4IRBIGA79FImCjdQBFarpzWkCfkZUXnvfkobwa5vp+jqt0KCqC0fib9v9T+ywBLcgqISpq6LcVG8cw6Snh1zm5FhML/d9IpOOT/dhySGkZsigMfrjKZYK8fOdFGNmdAWw/2yWor4r8KTn4KtIFRgkM3PEzv5k2L+QIIfRUs3jqWbxaUjkHzOMk7BzPvvWBYZe594ndozZwww+3mO5aNTlFDqmtgdMnuocglkqorc7DANduRaLlKOFvAwbcHZnlF4BORpGtzkVlQwfKKX+FGdTTceMZ/+L3dwGPWfXm1ht3v2bIS1NlValIAdEJ0kUagZg1IMt49zvKFhq/JKU1obfDGTSvTWltnkKTPUo7eB+ZMyh4KYz5Y/sHcx/MNBKNRQevGh+sC8g9sRpkHIJVJ8S1MAm3h8LXrpD4OqQb0JZNA3Qbt5RfcEon6vo0imaWKAPQBONGU87G49m+I6Q57rYFRDyDPEyaT1Mr/6e/OFrnvM0pxz7rzeTHeF+S3T8KdEU3oB4PyaNhsdnFQIflJl1F1kTbumw2wpGqEQLOUyiOcz1zEj6hskFoQolycxGne/PAYEckT0PdlUxD/XdS80BrFl8c61TCb8vZfPwbNoeRZUbTYxcK19WMwoW4CEy41Uh+rlJ/tlXAtSmK6LOQuTHxtz4fKj1I48enRE+UBViPwLVhzZoplpTi0Z/tIL57jmIf3OI5jKoLn/Kr53Mqz8Xi2pkPhKaCFWpmDuSc70haQwzCrfbbDkRUbXszUGbBG+xUbUI1npvL38F17xM1YICT8MnWk4jO/8caEKFQHoTWXXBedarXb11S1qqDg+A8HAkMbDvsoVXdN3QtiDsAIqJlNVU2K91VfFpnP9fVrkPYDMi/iKZ2s0QN3zX1nV/4VxkIOKtPfidQCRc0eGc/099PgCusim7o50E6+McqWIVIDFHSt09F49T7dKNWEUu32Jg2XNYoMKP5SE8Crl4gmOBzXQzTN9Sz2OysRXQgsyykEiVU561TXdBAWI2Ku/Bdo0oFikBdBKn8BUzJ7gSnoPzCGIyassxjQMOzgm/s1yy4NpEY5y3KdKqfuleZwoebOgB7YIkUVF9Kn6KMsKQQLp0GqHTAuKOiI+v3jBTsTF0SjGjrbxgGGBFiZ2mKFi+Y4/HkkyxTjE7ixX31Gg8B4D0JEgG1+R4T6U3vboDb/Wyw9d9NVvyLUI6pFQgs+HX5rRJ9gIc/MisVmPlCrJCwAxtsuay3Q1F/RyVwr+arFA67BWQQPP9gFflGkVa4B4sWj/4aiUhPQdunPVKcHVBT5fHQIA4hn9p3UEGJ27hXWc2eU10nCXS+dAM5qdCOjg5lVYm/8+hN1Cu/3w9lR/t9EJqGE1UtL9BdpTrTqdfEHu618A5x9mqNUojIKHWmCLoFD9uRkfaIVrEt/w5cwnBBMM2U3HRn4dr3ZYR2UGKaI+PjNz1JI4z1U/lcWkumFECQuakuJM1BmMKtU2YQ7PhqAog2fvDzvc3EgxtqMFM3e6iwnSs91KiXgmryDUu3Ik+mqQHVVH01ZaFUskjHjFD0jqBA1zK+Sm7r6nA2oopu3tY4pV0D09B8cagTCDaJWF3WBFEVUi2SZHbNpk0h0bTOPDVVJm0jJiFjYXlFF1R1ln/ZxVa1WF2Jx76ZPIV0sxerbloO0piJ6pGoebx1O0bg9AAw0rBJNCSCrEROjku3O+w8Ob6RY2jAKGpZEAAETIsgH4hchQxjp8E3UBBt1Nwe5UUo/RFmYgd1GliMwdKHLSSlp5CTrmIMZ7Py1c7zCd5OxEQeNnSHTbCEI4ZSstoq+0N2eDN240hiJNcvrZrtade4oqbz5nnk0VcGTcvsab7GPCEQOJda8ISDq7DHyR3k9KEth0jvVCH0Bho+IEul1dPvyBDs94IWqjfNZWwts+W5pd7X6tI2+A4eDS23Y7EQp55HNZHZu4M0KhFyPhu73iBZOl93t3uXXYOpsFGeXGdV8HYmb2YQrrLEvVoCLFLPZjbdzqaLWz134B9G2kOY8jQz98gy/TbVbWtPDCQqs1pX4ZCKwzSB4841cJadaZBI2lS4F5kLG1m+/mxE5zQq5p1rjLX56ltvS+6HHwH6nTuinQ20v+G1C9o423KObYYhWAfLR5OWf/FpPjSq1yzycnQvvr9ab6J0DkMNXDLU5irEZo6VxO1UY+Dr3cd+oDhERieL/MS6T/gkkq7P3piHyKCXx8GcLPGVMajklr4j8l+XdL2xmAqB5rya5aG4FhZ9NpBQzk6kVWEfXLgx4EY8Gc84Sm8MumocYhRrSVOndhFtXUDUe4cB1jRVEI2+SSkzq0EgFRTKNzpieHc+v+HwchNZJ37bQrICUVHKaZq9dtKKGyhCo7jeGl6DuhvTcagUu5CZB+BjJ31jQYsFCTDXhbCahJAc/3FIcfKwo78f5tYMjdABPpp8bjuAB3N/vgx0WhwE+HOskZv2wjt1nmtdFIWkJKvRjpTtFgL+uktYszEC2p3L8GXL3RQRFBaM4tKXu6Edz04loBjGp3ZyOlHx8Zblnf9RM4osT34am6sdT6f894eirt+faScMehWbCmynIhUIghKKQZ97TLCg0N5d9l3DQIKGMlvJKeylwAGyiUWz1K+WbY2TQJFnUjiZ7fqvCnGhuwaJtE/JMRPHkZ/t8KymeIzrrfe2KCHbuie2qcRLyHas8y9jWbRV7LxUbgSgVmlwB3c8WIr7Tvjnc5MsFJYaYqdzfhidpETHBuX4NGLvoClUkCgnctv+bpEkxR1vOBnEroSnpSZpCimteqrEOIY3zfTR3Z32sXoR0+AGyLcNhevwRd7xrY1iKaRzb1DyF5d0QMhdlWCT3sosKe3Ui4+n/ENJcuufHTGkbUc1mnSHGw2cmc1Eixx7EqXzBCkQqtwcPk+7BmQ2RjbKMtDx21+exJXoCZs0hQOpUYyGE2UeI0HHdrc54qhw4DYxgE4N5/k/PpCUWgVTdMba5yxo5pEYkAqgDIkdhMkrI1f0H8gzL7VnFuDK0TMtBW4DpdW3+1ICjMUK7pWHlDHAfW1FT8UsVPDBnVJmgapIWJ/zjcoitQCVhcZaNWQEs4HEF+2UxDfPo43POtDkKH6dLQ8B4e3oI46s+6Hy8xXtceHizqC6xP3uW45txqcwHLCG3NhxQpMIsB70sM1tgZB0VtHH+QFKOP7B72+qT7S7fcp8VILF/i9TyT+vNfj2xsqlwiTXraK4aLk62sO3hoDLoqd9/r4ScwgcUClcaqXkRUgJ73kv56P7/bxXP+r+SYiszPmGRyeqDSsedxX2hi4Tq7+O85w+W3Ojzd9MOUnSsWw0EtyA33kmLAVkabHl2tr3EitUDYLT4t4arcDvEu+AKKbz7Fgy6G5j47uIReCMrl9dolkwA+OB1ksihIOw7CwEO8oGbT5fEHQCQT1W//vchn91tyQkEamoMKYljsQfhKghyY58UP8bH4ZKDp+jbLxIhnWJ1uL15xFgZuqFtLNjdhvUePruHuRLsrwM9CfE49TCyVQpwhCjVwR+Ug39Stj6b2L8xTqcNoft6SBX5cVutIkz9UsST9EwsqC51nDnWsOp/INt167d2OhyF8+cDxRljUMXfLw9jpgPZk3l+XDypXPOrNIEzHQ1MNN5HhEqNb7bZHXS4K1yQl2UcawdB+koiof5p2W9Lk4EjP7vSmvuCDlH0Ge04iDhnoBgTr14jj7jAkG+mxGJbBLZGIIhaTW1DtRwW/QeNrWORotpOqkfD1ypvEjVOdnHYpXCVhe6vFOwwf+6X4XDa/OzCQ3im9RHRKyH83sGuzSwXyHWN6iiStLyCPTI2N9+cd72IzHQtVdlt8ZWNnYa/HFqaXZyc04roWtjRs8ISv+GDQ0My1jUbD4/72QFcZNcJIgcnLc+EjgnlBOdRdGN/m3/hoiMumgnrmCwJ5xvlGB3VnuJnN121tzx7GRMYxlRszw78sdLflFz0dpz7q/i5vpjlZ/Jf8ZBWOGYUlebYOQlvMXSaGiTV6V7efkuOql4SX1ZfXEbvyfEF4OYcxXPYXNfFm1qaXSYxZSKhpFco30BPJyCFduzIKlqwahNFAF6Mt0bF6X8PEyKzwMVXG/u6rcwYKIHZFvE5diVcMisHjR1oGbJPe22OCzzMuoLveGGZnTyArAJKY98Tu7v2wLekUTjDgwcA/iMN8Ew2UdrpqO2kJmlnsUySChbYIk2Cz/SwHTbSk56QGHOtDieSd7go+30nNto3zbXUdhDmwtvwJpvy7z5FNyxGpupmDOTccJMPVD2L2XuEhtDSscHFkovsmKysuP6e+V5Ys8wRFywwCkEFzq1pWaIk9QXpZ1oqTywxu/yBWi86Pi2HFW0lpqupkSGgtAwIZ4wy9bjBOnPYKtlvdzRjM+ZL+g/QiAX+sRpZuGRX+LKrBB+IbWjE2jxgLiR4joKJlOU8076sD9bdKdvVLz08naLvvAPGHF2ChQgUl4f8ahEB4gSzjhtiimcXxZqVvtm4aaNx22osm/KqSq9r122eszEf+W0P9eUiVhyGIM5oToD91eSP1+1A63I6orlC/hqFf2BrMHLt/ZKXl7/rDNhf6miaM6qZbzEsVdzmXL4yK4N8gEx35SrIszbY7mR8nqetdpEwPhjOw0TBIgg0G0xGSobZ447BXPovNoEU4LHPlI4ELoHwBr50ELiV6Asg+OA7JyaCnebMVK0o7ZFtv1ez5dfJy+euG/1CiMb0aOsUa3c0ZYruaMvTVB3uT6Q4rp9hh4sTIUYcMHBoyGSE+OuRsJ9OgSDd14Sf97Sns/uoKl+JCPDm8mSZcxQJHmafGRS9KadjuwxqPcjEUdeYHFdHld09PZ3zVcSXF/xz5ap4oV5JeTODjwYBHQIn7D5cZuuqUe6zxe2V/oYfrpzS6g+6iQ2mK+fXAb+6JDHWJ9Y36lK9JupVhEYFDuD1j1DgQgXX19u4FPF5SrV9uV95WWQLc1BhBYLAiCcsJZaMZVR4TMSJDP77NGgypphtAuH0ZuP2arOh7jKmnrSf3DNNf1iUPJQpUCcjOiieY1NcFwCmWJVSqU/d7J7/JbmS90DQf9KzNDh6I/RhNY0ciwipA9UMg+WmbJ0M7xcoLFR+tffJbb7dvOquJXIdbK205kL7w3yTruV7rtRV96nt0U4FUfdiMpK59HSXylBnGtUho7HyphjJTfMX40XyVcUsEB/rwhuFkgWl0yfmpCSAKEHkQ4xmP4crZKjaqxeYjON7DO326ftyAvA58g+c09R7SE76Cow7H4B2jxlP7iM7Bp0PAzbVLcEH/GRzL9aK/VPrsoxhMz/yDqQH+fVF70alG00mgLU1V+oYjgEMmHCJw12fl1HJ4a/4/mBZrxZyQ7ZINZyKP4w7UgQvZzwNDYQOundwsI5uJViN2VNG21IvW5vrpOME/NgOpScsucadNtY3HL6HHidfLTo2hf6r0+9GMhcWR97uta5j6FttMWvs5B/bzZxrAf+Lt5ab8pM23mTV3qMz/XkYjQiuLlKpgUNJYSMmxPYqS710uDeIunVRrgH+mSDRV05y9L7zspjEFVVCz7sq6lFDQSUDP4cAgBTacvbyHkxZ2dUAz+Dl7j3xbK/Uo5rC/7kB7Julu1bKTV2HwCN6zuaYEMiNyocOzwUrh7uAMkCnormcvd4r9BuWRTUYXmDrGgnmYlLGVfszyNnB9A9gcPz4GnjEl+Cgp+Gaz+aKwmGJ447zMfAIcBTzOT6m37zMYWP23Hjl8kVbQzlwqp4DUlc36m9eMPXSocV0Cp1eOffGgzYurTct6B7nvibsX4zhv6Nu502AE3hpCGgXmN/u0nFf2Yc1znPEmfrMUej/cYvcHxn/8jKuvNyucPQnUYtiOxbz5oOlNHvkiGu68aU4zVsXCZCMBX1s8fg7dbEicc+YzthwTTM6i/+4iXSCdAuis7Lp5J/OyfjQw233sZTqx519s05nF88cOdwvzQNmR4xi3YXQziGB6MEwhAyheX8jmTFxMtdFOcAxzljMdSPES4jQ3Sf5Zs6XwCg2h/b7dBy1zCt0HsaY0clo/lqTRbGCAgkzQA0zemwQBfdQHjNuX9KwFWyyXQ87TSnRb27PD8dwfOSRODGEsg9gcs6vPh1+gASzxsGoixckf1T4RwAsVL92PCNmn91eF16g95byTNM+HbvnAOwSRafdHHOWI/tP+rNRp+px74LfYRQfJ7wLSuXFLmi0prS8RmozSjh9NgduegU5q5LsNDqSJiU+EEZ20uveEwCxF/gYs4kKhJc5sezCgxo7hswu71cyk9aMLyWY/lyDpafRJP7V42+ILBa/WvmDLD+fkVv/EddpVGTSHvaJ4wm0S8jUouZQ/sXuiV7k9hjHGTxgI2CUN3yMf4K0/vjO9TMr188yneO010jwK92BqqSo0u+X6GjeNq4qQWOvZsilQ/OoANHqnNqk5wVRV87701Danb3gApGs7ko06UpilSQSu6UdhF2QPyFpcPdqx55qtTKxIvtQtzQIXN02+eYiGrZ/OT+T3qEdzaaxuTvDTnG4mdUpaD4Jk8HmJcEm0mQR8iznPLfb7vylg2p1Vuz/p1FxhlEHNzw7jAnPlqI71paZ7s7K8ZBZOwFs1efe4OeX6sTKlXf/FJVYOXiXtnDh80fkCsDGWdWEY4k6qgbBfGOlwE0Jr6LhVWpMj+IKt+gBIuNoJJbSup5IKgvYcdMtpw7X7llLKMtgztkAiGJASRGYGMJGjMsKdve/7G0XrGofYosNMR+mhJSBFgJvFIqRFDO0aVhDt9StDP6mduY8VRjuA748b5Je/v2ZD+xrFiXp4aJJPd8956sk9MdhGHloE/1cymLVOrx0TsHuKlyIupUpKOUwNvKEjHiC0/3uxVc2a+ruMKH86zbPBlnJ0urfRZJTJjxgV0YdhLEDz4KaIHCcPjSO1oJNp8hFGJp7bHQBkQTuuXplkMrtjvFjho8K2dH+rWXY4L4GXIgnqX+EK7KgAg/QyUQC/giw9C1nRFhCx6Yc5Dn03wXrry68ZWLD+YAoXhA697m8BaOOS9AkdVdu7o4KRG4cxTh2KZZXV0tx29mSMzCwa4mOyHpUlYeBnx7ZHXQG9+ilCXFhFnvYKJDwTS0cvOvoC9DHGkCFWVmE/DVSYDMOddE7z3kow9CE0axfooJ362fpS3ygfYX4slZ+EccM/SiHGmQu3CGJpS82N5YgWmXmM0zKKtp88r/O/cG7lybEv8dgIsUzRDyDkCE+CR6o/4E76VeRCDF6JXBGfIF77S0Dy3NBFYx+vBlHqYH/LZoqDcMXQIKIhGWHcs5DMcI9PofeuXfpCFZc/DUcu8qhjrVze8+0tZb/cx1vqW9yjOJbMZvLZBKtd9QSlAjX4HvZjd6q6fyIQend9EiHI1Sj1jY4vXyy3xdvnPRtqC4rjHyTLclfJT97jTGFg9gYyg0PYkB4WZ9eI1OmFyO+jvPFgpTFJaJr0NQ+QmHdAHqR86cfjSWHYDv7mw8rYPLJWtC3be81UjmPOMvxVQ/krYVAZq6sIZnZ4Gr2B6PqNKjAwp+BCXJRvcuAZSN82qBJZy20DI3J26fPyM0eqU8JWPy5tp3u+YSZPZwCByAjDVp801ZOf35Aag3ZdIEMzvwF76jAy8fjxG8hTg+SiFyN1gVw8sW20ci4z9Rxqv1ACrdZe/GyBXM5Ed9LOWQMaXLi/CepcX7tcEZbNswuvJ4pihKW/Bm0JB29wlupMX81uFzpHv/D612kQOiKRG8i+peIT56C+grodEEKTz6WwHJQM4Etobbp8Fhcl4Gt3EOuiS5Q7k+embE26pbe2zhWyL1IQZjNGiX//gw7/suVhbovQC/zkAVQmXOUBZZJNHjwHFdZOmQZcLowpldCFHJZXY1aXEW5/FnS+GZ1qA5kK6X2IazNu+CW6DP69Nk5QIEgIpTAV3bVQKy0UE8zCXAaT9GkNE7gCBvsarWm+MKGt1DX7IzVE1gTri3rdbIvDjiqTV1ZBs+h7fdCBKoNTyYUz+rHJim24xC9d0yWjnsVTMhlcgbtSXjVshRki2DCNIZ2qcQkpcTN0YvpUdCdoYUBoG1gfy26VoCeOVSTDpjaplu7NIKZLa5Ns5kCTgfI4xjLZJUCSDkEKeKYdZTiDSAmO6ps2k19H3ByjNFfGp6gcKfjtfc7X1UaOXmB8rS5TD8bJQCiqwcAdMHLSfelaYgXMocu2V6spuzZlqveWjn+Wa2SSxiaE7T3OzfQrN985LN99a9xaPF8Ax8pAUG+xrJFbPqRhMt3XM6AYHZkEP7h7JtVLNQxUz2K/0Eh3X9JCmkp650BEkP2ZttE+WBr0Y1JgZDD8ceO8bm6yMViOuL93HpoKDedlH1h5qQufG4VkjARuZ6URbcw76m1MF6SNGsK3e9vVVSX3z1S79pM5RJ5uPc+9vckB66dtve3mwpUVGI9A6F1o57U6vSCJ7eoB/hOqiHxAUCbcgCgZTYt9mi7l5WkIFZIn55LKqrXa1rJp7vbcjFHO87TgAtas/7yHvOtfsoNo76V86m8fdjKvLDLEfblSSSI8YO+j6zDEfNQTyByMnsLy8ZFN6PL4EsKP8/ExSXM420i3fglOYw47Om8av5vSO7+/SMpXFbhRhDDYymarxzma5LtpSmbAKiYUKUYoT1jq4ua0n2He645237AqyR04ygjA6pBxsM24OavhHd85TWZhTip1xZ9iH8qg3G4SsLXZut03ujRLqm4fqTwImc1fgUcO0gMO4oeQl4etXoAGQMzndT8x4Jge9Xri1u0865kP4+AWJdh1QSYRBE/XUVOgxL4hjhf2UOUDu135nScwWU/skyC8jOarkSNfng7iUqNjmGLzLwQsYg45dNSgcwAPeVOh3Gmf4eRZnTZYDBQPMepTwZPqrFl+mGbTZw2jYn9kwQI6IFXJa8MImAewGS8XZDwI45ImwE7syrLzdIGwVMK3L5PuKJI3xa6BIzHMwjcOp29nTc0xHtvQPb2gPWnrfTE8RZwaseEdtuQh/ONnmN9aBqi7+73aAplOMSKtoUKGB/PLJa4Hd0tXmpN+3hI8qTq8STh+VJwPnV3G1u/UqMx/egXpwMNuEKbnwabLbZAo/zjLLSmkJJ0p6+Z2WIV+UrMCU3zwy0Vh9H3Shdpj7QkA1ppIA/9D/I8OyPYM6oEYPVD03hOUIjXVx86uElKRSIN98gT5tJ6iip4gYxvoTa2KeFRGgoLDlN6BvhmT4meHsd3VPIDKy5PEGpR+vs5oazpr5pPHc4G9AhtOjAny0rDGFLTLxOMxumCqQ0ZzZKVmG8IIBUvMSgaQsyfTl8m4xv9h0kF+wF4u+JQ2s8GSxljxLEzEdF3CdcqyY4wcz+kwzQ+G3jt60O+hBncgMipmmgW52HYj0CoIDFf1vXPbUnT/Q0gxPHCwbmOKiQzdhuOfUxsTuV280kZ503EfakP08ENL2mt6cBIwB0QRo5r7LqD2f3D4Z2pAQNT3tBsYU4KfIR3T73bU+tdVCGEnqJ/lAJ03hc64+NGZmcxJ3PlNDp83Pplasa5fOprh/eydSmZaiXEQrt5P5KMFDSQHgX3zM209GmQ3awHGQD+j7ej+YZhcVqf0ekT9gpsCRbyn8mQD0S/ox9wH9G8teTwV4QE4vGa/1PntRDIPkVQ++Q6fpjAEjaALgEPfUmD9x7VM8wVJyhPD97gsmR0At7vAD8tjayr92KWACCiTrO/2gOFHTT3SmJvv2C/6eEklB4kUJ8xNfillJ+Ksa9FfWv4wobZxY1zBOvleiUw6yZfHTR2PeSwBHf73dVbyWIFRD/gw+dJ7uiPrSpPSBJqDAxu53q+8UXIZuQwvX/GZ6tYzYWSdQPuMUD4+J8Tpqno4Qau0JIsMTpx+lyHy4dmXU6AGGIb8QlkyH/Ax+3lby26pYZz4IctO+WZn+7hY11l9+feRdiFQ++HWyb0LzLhZzhvnnWz92W9jVCwLgN8+rI6ekSCeEyCqvBmbWUJ9ApeZTnSpOWA+oz9xdjvLyuEoyv1D7UNZXSoWmnyo0uMvBUmNl3GIuT5v3n+D/qbQ/L0WgI9KT9WvwvdfFONAv6MrHYktIp2UOXG9i+HDXU0j2H0egXEvP7p84FngKfWFxvIfF3c63CXauX7aiL/3v7y8PqXm4vXQZ9QMuwJDanbw55cxCZMqwQLoCz9ZmHy6STgCwdyE1PBNOzTeQhcw4Lb7P6vXQ5tx9V0TyADczQYVoQ7gWqHClEACauT/6bfeF0FAP6n1lqFPZ8UnANWqejSipjsFYEig1jq/T+hmlu1q6HS4Pj2nqFXNCT6YtLNb3C3SLJy2aXcKC+oHe+urLEHJotqngt/tFu/NMuHeSo35e6dF3xUVOMfguqKc8WjCOPYsbVotO+I/wCqZtgK8AqEmgf0f+6fUSKiXS59GUk2s2sfMrG5jwi8H5CiTY6FS/hA15vTePlaSiZPw/eTxmGYaveqvikNrZBmPNk0bRTt+9jzSu4so1UTK7ekp2nQAI2nRu1GbjFSMn6VQ9nuz6roXmrS7aqEMHl8qi412/1qI3xvIRHuZlx52p0wHfeugxTaRLlctQ7vO+8GRrq6++aKEJaKmlv+aZAVjgdOEyWDk4Jqv+alza6PcKq1UAvRkpYdPOq8MU/kzmKsBDFlluOibaR/XqzTaVCFEhoUQaw5NlVdf7EtLQEw24ViLzDu/9RKKNkAAVzbZWdEpDxu8Mpp9SdhP6DFwagoWc2WzQjZt1Uv+fQLNSgDr2oJLUrlV3O0cTkNx48q1K1QBCFGeakb0GYmBpbny1MAlO9qhCVqO1D2bh7O+LzEtMc6itYorGA7f4ket7luX+q4kD9p2XwlYGrxAeEHb0LwGuTvIGfRghCX7HxQGbLT3LILsfnwQKnhgYKSfHZZjQlKk2Sz9091ZrsJ10zUfr2yz8PVSqyX0tpdQnt36QNAMvAAdEoIxOS5C793WFHk7mxs0a++uWnV7CaYXyh1xIDJi0pLdTKsXgU+r2xEngRQ/8cA1FzEYFIBqGg+60pLVi/E2UfmI6cmdfMtbSzFyB+roCbh46sk+3l6N+1+0nW8kitn6CxLHJKTaEmuIdAnx7aqbdEInG9q31lHzR4viEFVo9UgnANI1iF3T3/o++Zw5qVqzgbpvJCR0PP5swCvOgmxP6Aw2NwJgRVSDX1OTr/CJIjrPLIYMOUxcxV9Kbmza9oSk+3Bi8+IM4ZzR00tK3MsXGswqmt7DNw+o9yQst/Q3zxUgOwkD9NO88I+Ho/iMDwpPvDd82GkVkm5Bf8OZG9tXCQgBfDUhiem2nE3EaYsklYHdeIMUhFRtQ3E/+xjTtb2m3px6KrUhOm9so4+qynu2WEsXkohWkjkj5kZKpu7ESdriS85Syjx0GnvUg/KWmEJrt3BtD2B6A52yQaeT3CbBVtznVpX0uFlpNZSztx8SLLyGNa713ku+85kVK/R3EtWnWlkb+xMkljeZ7nUR/aEJEIj9vaOT5C7D60b3gUT1kpw3YlajzpYSwTH7e8maMfjUavN3NrZBu5SkdCLXxEsJ14bn0Dg0KrwNTyPUMXaWEB5AfwyI5GOaeUjuIIN2oRQKHI/jSxgukF4s36EE77rEdBn/V5hm84ZxCTC4FhQIkTlxvOP2jR9/4JnQoJAe0661pPUL2dr+P48HW20pozRTxJzhdnSxuSdVgw+AGKZ2pqwU7Txyxy70aGdfqSGiasAAZ3dpmiLHdT/XUraW2einSP+EoBHiiOtDfm68x9msrXdgYGc8q4eJevU0phwrli/u8lRPEDyif+RcyPAg9DHfgT5LtLLHY4k+xVlZilJVa4fL/OFQW7qfrkz9vseR7jeqAVDDL/bl4zwdMVGdUB9y+qVeZCSNtEOX4luGYTh9vm/XGnym0JIzTmhc5mdwfnAJjYPQZVtVrPY/Q48T9jnpOQ/yvCrFzYPOYNdks1d6Z1Onr4HzbeGSff5g6nIb+BjFSfWNcaVnzQ6ijYkUl4rMwaIFiECCjRJixuXzG61uv2Rq4yEgILGhlYXom26IwEOPyNFDmPqKtVvtI6eACgI9OqSL3TXWwjhCAJRwTaBl+9eTH5RbHRP5MsZJ3hkD4vTnnsKCtHEMGpm3oQKsIORGkvsf+6uxwL+OQsh7CjlNee/gfmiAAHJLNVswdpH7MattAjBkmVyoZhqu0A8Y3Tr+aKLIH2tLQZ6SAtNg64R5IBmHf0RdjlGnvaTPIUyRO3VjlDzdm/drAAD0u85deitOtYQeE7Y/Sxb3AKz/tAabXWY22m6KlopcWIgpMJNcrVzDOB8lfP7x4iDPdLp2fmUGEoGtv6IrqSiVGi//SCtmSUDhGCvF/eGsgVtHnAADXJGoUoVHeH3Fgw2CJO3rZe4beHPN8q8TCCc1kHImHbkFnLR/7jhq7qlL1sbu7/1Ep5sHVm82U2q3oLnxKQJu5F+GUn+oLmvcEUx/YmVud8tJZoDYfSCH0SIVLPSJW/XtrbyVJrfTAs/mJwgWc/o2MnNhRAPD9l4JOGl3S0ADZM9eKmR2xVuQKXvrqYfo4NiPbxZn/z4QAN8jXa4/iqGdj8+eTzt/CnTjj8+EBk4yDsG3rbqTFWtCxlHLsgD8DHViH9kcK1Jaid2ldstNMvfBr5M4wxyKPPMqZ1wqNfqDnfVvft+sfzPYztioDO19qPuJx0jzhsD8kVc0u0N26xhof6eM+QEd5fv+MP5EEoZbS2iNF/KiAVB/mvwvN4XwJtv5Uc9DMdVV5s4cB4gM3MtZJ6+50Q61VYK2vuykvXImGq43IRWbXk2Dn2/E8Kwf8AX6gyywXzKRvdKPND4cppnqrWekXL43u+Bx6x6p3UrhouvZ0YA6HSYC8UXap87sBH5CrMNI60Gc3QOThxtTXYIUnJpl1jpOH8P1VlYM6eusbR8kSgOCNFu21MMtOhqGpnwpn42iICXMKzxYjUcl4lDcqoa0AgecEK6PQTPhJzEXJwPgFRvYT6b6sWSL5lslape5DV2qVDkCQcWPU0XiQJBfpVGWdBNMwFI6xr/SxFavwMt4XRiqrTxSpl0KoKcScT6XeS1ptubHPY/XKCcPRNGcNFkPOXi1up64g++DignbjccEo5AHEkHZDyQW1nkk6xnnM8931rQo4CZYfhxxRwseuXOSYetscvlkHtp3DVrwqvQ1/W8PJJmCz/yyCHvfIUUl/E97X9zKcwnTTpL4nmJMKbqwI/vU/z+s85G7BZtrNH+IzHlBFrD32IYVNC4kPcPtiNojsHiK/RSj0pDsLOMKZOfNDAz0XJCn2iMJOo1uLEvxQ7WxF7pfK8vkttstrRtoHHJNgGPgGyAuJ2DBUaqc/s1F9ZF5VTEJkbCg3ilbpYPnod3tNlQR0dDBOmHLMbkwNLi80Y8gnecv36P89xbXEPfIwRvVC/cjocOp522qse1sHMgPrD2T776FT6PPVt2wZ4jGQddyOzu/5nCKc9G+OfKW8C/53/W05Prhkay5T9HBly4tEUrvpz+CFw8ek8gVSmevWLFWEPrNbBwujla0VogPgAbXABHJ4s8OesROTYQQYEqUnZRIFalXvNEmpayjEIxh2/DJNmScgn4dW2LhY2Yg+1io0dIFmjak8VpODDy0BZ40tv/atDfv2XWBs+UvzigAb/BEBaURUPcU3Sykor5HH6/Vvjp/w1fRgN74KV+8KG6ZW3gN4N55NI4yrl9CKsP7/fTy8PmoPDt0aD8X45CJKuYifsg2SH5UogATIRa+4aJzrp5q2cqU2BLEHWXfh2EAwsJs6cT4ix6cWU6RLwJx234XsCh//rdsQri+wVnJAW/y2jk/1mbfH/PWCaF412deBVhqCZzUPQtbgSx61iN958xz56A/fNpVejvtqfP8clviQOvzQ2alGAyK4F9NBnIR/rObYkfF+Tif6one6EOtTRIFgZJPIb8hCCRly3B8gMJOuSmWgMARnFHScnj75Kq3KtjXuQuq24rX4BZjP0i0Aji6E6SkAWA3ukE5A1fFhDZcQ2HuWiFRrtBUubvXWMqLWFnIylqKqhOLDR8zr4Bh8/tKWDwMILQ8be1ZPfAUOqNmgzRf0oWo52J08DtFKlOYRgAdgAtotzAeJXBPXj7UKHxhZN82k784lzgmQEbuXyFCDgDZzkkvtpUkdckd27I83MuChOkFEvXlWh83yaBwof6LiGyh7QMmyrG1MWRs5Q59s+3ph+DxgR5mF03IBQANGr/v5cLsoI4vBVm0s4DWFbJh7HcI70wPOwTX7DAS8nlATrMLuFe8dyqM3MkU2CFo7yvcdSBsVTeL626CGvMY5pwQGqSaS/4fcuejuDp7w8DTbVJEnhK8PrBXFlBQfsb8cpXWyNS8CdQw+bYxgALY+tI5PRyxoorZzBu2UcH0/gshfXQPrrRvAlQGrIWWAHwbfpUWMVwwJrxv0fmbkhfY4Dw+pPrVDSvnn49D2AMWOAh+gidP0eNCyZVptEC3eoWNy+Xlyw2YiLT9t2iBXlWaNtFFtPAuB5YAFOpYhwejOxAeGLV7SaUT6ksT75VrBz5ndvgxZMg8IWtX8vpEZiY8HxB6rW0ceW7VBWfpTsIzPhkeORucSBIyFEoB6+0hy/r5VqUjIcjVI7zmWSiXfm20/jNRVRaq2z5OyqoJkdTZp1AvLJFCRN3oXd5CHbuc+hl4DUmkbUyx3ioDQHAlH96zgHA1JxRl/aVunlYkQa8MCcZ45OXDkMjPVDztIGwEdtEqio9prcEKK1LtpAIuGHypZ+qUo1rT7VP87v5X6D5DgBfzqQtfPULPHI+/a8fic4e9r+T9Kx0Ygg2+UbmfEJIrZrKBapjWOBPnQAyzlc25Szps7pkbKFFYgT5474c6v5VHCBpsK6nIF/hEOVaoudjRQ6Rdvn6/6U4oevdlXzAeB24KYrL/3Qfw0XEkCVwC+HWagx1M9/PBTOjpDKA502GttSPz2aDURvGZhrnqBJfIGA/SVlE1vAUBZXESW3vVAF6LdGMOZ+9tSzw2QatmDIngIspD7iRb/4mwy125/5dpz93VpwhRmU3UNA8V07ZurXR1GkYetGs1Moc3fx0xT95t3B+s3G66uXstzptaVAeQ+lXL6kl2e3xBRt+XI/zcpzuAB+0Aa12TrETK/QsJxvK3ZFRyF7BAuNFkhtZB/mDmKS1A8IcGxwzdg0/Q0bil/jKyT8WJMIKna5ZLDHjcxne9CaAIXSORgg6+8zxARaoZ64/BEz4f9lcwpG5D/zctFUaTY38Q2JitA9uW/BNfYeM4ZnX1EgP4A6KLG5Hm9JbrffnUPP0gvJ//7c217xoHVqBUD1kGY79XMAWsqvaqhWvtbe4K6rhreJkZZUnA4j/Y0la+KZTcPFaeMp/38/jTKJKSx7fzsqmMKf/n0Pv4Q9+MeQm7VY/DprJBc2aN7YLB/BRhZRvMbEr59DtT0G5Nhxxc9mpBTftKa11ystimiBWwtgC1dwvVK4UC2mdJsDOwTQ8Egd4hPVTt7/NQ15LW/cgVaBPkNfa+JoFQ2VjzBmBVjwuPX3U1mljAE9VlwwEBuVgzENcs/SNcYigvgtbYoEHzng4sZlOZxMsHNIuS6MGP93GKvHNYNA6N9Dr3gpK1GcEC8SpRLOY6jIlQYAcJlr6TGGjrB3cpJdHwN1U77RECBsPzM+zsu3CuSGe9yrJ5q+j4oQAgHgvMGKLn5LuDocMmwrlrAw2eoKzOx2IPUU2U5zH6sca1yw82p9RPCZmJSVB3YLIEgKSvGZTbb2kb9mGgB1iYjdZwln6m2n9Jwvmn0S9TK7fB2KLGheP+uzXJ+SzJMhWfkObDYZjwD+fZqnl93p1kG8Mnv6yksBWiklJS5Bl5PitOYSCe7CIQUl2HMYzgnVxjmN5fJnynW2DZnfYvr6XA6uN8AMOrJI/C5nDjKKZPSwHgQWjhEvqn7oxol0Ahx6yWWj1wfyfDT4ERGJ6MBGPAiRswDi9njAwV8hELiE5QoWxEY+QOg/OEK1kBGqHlERbM2iqnziyV4X8Jn7HOvXVw7mDJkqc190xh2oedoVn0gTxwSbaDp6zaxm07SOglswic+LoGyftP9Vga6xDa7do9yW2oEiUfWY6OiO2IUwh/diTzd+aKgki7Vl068W1s2i7Op4+VTeQPEkb7iXhu9STvlFhH8ASdtgwzEzR4lxbj2o9cdll9ua2vnfr5dUS0KAH1M+xDEB5Xqgu61/E6k9nRBMP7xw515vdbDDP9K5kyHIJkiqxvQKQ4YS1+DI0VkA9g0SZjV7AcBhgJiK//6Dul30QOt+LZOO/wwARY84OD3l90FKJUsN6icsjLkA40gs6psaqo9+dVldF12+yBhiAW+45rUNV/gHF5BhYEsP3qEjUcZ8J4uVHtMp0H6kE7iVczwfR4VJExFgeLSkLf+ARqCCraS73mw5/mftqiquLXERx4CjTHTxHlFDRdbXxxo91PicuL7ZhNcCBe4mTu8uR8qkhT2Fja9Au522uMjBoGEamUvzWlObP+hWJEy/ig6iy0HgSiIfhALPMASCe4OO9w1+NcPs5ucMyTQ/V7VLUK6+fOXtimlgD+kTVXPdlwPmjML3Ao+m5fGgABKMzwmlRAjES8mzzbQVYzpCZ3vF+tWdaMveWmWAmgjWeshf7y3WqY0TpzvPBN9KRUqfy/I5CBTYGkortHPxz8/EJLv6Pdio1Vx5AQtwXJ0so6kfBFV2O2DCNtik8ObLRXtc5gAw6vsmvBwXgFkh0zffrNPJ5mEpSgSk/7/HpuRp+NEFUB5r07KFzbTEqYWFu3WKTayi/bJnoY+FX16jV+jUlCFfGE+BMJScALwHZNR90wea80gfer2QcXZ5h0nFAaUW/fMJCX8/lwDX00k/5YMh+/ojzt+GfK7GrxNFoxWiA7JFv058bpJTsMhTZ5j6FA96E0EDq1dh0TJ0p8wPq/lSarRt+1Pmmtl/hRAslc+/P1dq8QzWIr9gAoAgMkETnLVXGu8LHVEt6Y8Gik5lv2JTSGbyT100Adczpm+TP6UzGRK9lunP3L34oBZ8qwk0cCR11GF7Kcp3LyThbFmtTgF6Uj55EFTERAjQgd+s7igYJ6VdtK1ihoC14NuzDSwgzqEyd8iStSCOcVfDyqJWFPl9uWhbuQ96SYr57YuJw0hcuSXfQ8bL7TufKshG+3Vs4/Z8bQoo7V9Q5ti7jgBJlXsRowebgQFuZV5m2B2aLzZOHTOl1TYiVfY5ZSI+CAfUCCCqq+xcoD1yo05ERe6CJXprC3HHzEYywgCqW2bIMmRwfTsYDhb9JJGCVIdRK333zNJw5ySMzcnOF1PmoUErfiJSA8aqMyDGVIR1bSSLTVdrokscBpN2lnczGqlYO2jTdUTHYerA1F+fJtieUtoR8UbdcTf/vqE6PnfxKdms8uY+M1mnU4CTXwKX7tyQ03p7rVyWXb72SKuIdSAlGyqu0C+ot/zRO68Jw2qYkg5KUvQX2aTIrLiQ23QmBPIy9VHLDxOe/UzYt/OU6xusnBk8wbtc567+hv90mggzPSAfm21qvKzO+JMdINtr6zV6FX/g1FKqh2AI5XG7sAaCnTIyKjIfYUFeSY7elQqVBjc0LcytuG1gfLXktiGZEZEY9VWYRM7uWuWRI9t/Fre//pEIgDgHDpfQ7WiWvz+V5eoZeRIKbMiygNSxIBa00Hamf1qP8VgmLkixxDkknMOTx+/Udov7cMwrx80hiTeBpfmw6cY+NYRhHHIaskzElSlqjlkFiO96prIf3ShDwedBtwOMCf07AjHM+TOdb7tNiEDM59qr/Sdy4nGe6mAzOD9EFLq2cgxTXwZW0Eun3KmUJY0naWNfK6Api7BtI0Q+IN8UeARJfeIWHLoucdxcBOEPS5+kqL3jSFM22A9FsUHFNdrRbR24sYfnyxSArp4YyqKOdHcknOOA9YS1M/yoZAnDiPsvLcRTHoPWrR+8fd6CHn86CjtuwyR26jYW5BN1wkthFOF+87UWpumEWZKoAWcmnA352sswxwWB99THBiMgA+7etewQ0o2C0bCxmCkLZyLCV+/ClfzKVPsyCwh2h4h50r59eum4Yl6KbXYz0Y5XoYg1b7oP86Fgre4z7b5lU7DkeU7XhaxOq03WN3zqD+5onye5THUN/m+JqMZ+ERQkWe/szn5oomE1/M1algWuTtHyoiPUto/c9tEX35nfPST2Xmo1Yk9xnMlJe7+raIGh9FmKhf2Z6NYFrjOKrStnn4+Vik5i3NLdnqHyganCoHK8kDJIbofBpFz6hjv69HSzPNl2irhiIvKflGFp3t5G+3eqgw4Txfkv9H3+QS6VIGXNxBNI93a6y4aARDE5P7CqkRhbgOxJkzTAuVnnGI1c6L1qPuljZ8b5orqTVxEh2/LN1skD9iwxkZmBF2/5PhGlvl0Q9OiPKGPvxRbg3tXurlyqRkpz2PGOa1L4n7cmo+CSA4XndENj5W+41wlTt8Zesr7JqhWmqdjpEP/tkYY8pQHPnGCX5PEkoH2juEafI46aWQGQsA6Iygy9KnOwgoB/oTdLpsLF6hpHTSn9b88R8UPXhux5YftQ1AUPnJ5Divwxuhd3n+U6uVjAw3tz7d6v8Zr1ZTdZYGAx0nqkL9qEApAaOL3p2knMT23PoJqp4EYdchedMwwuBskqrrsi82I4AkvHHxOZqb9BKS3NZCWX2m3dId0OHGqRVAafWZp/uCohva/KO644XIQdo/QHX7OBc2K71LgUcCzHVn5ZofUKvnq/i5Atq2O4PiaF8+7LEtGknMDR/TAx/jITnbdK9JlAzvfh4YHeHG1XAbTwyp9GGTS0Y/nUwUH1Gz25f5/0zfcG6tgXyfZv07ssdEh7vdY519CfHPP2b+20bC4gp0DauK+NWFlpigg54xiIRIctq7xPSFUrQ83XcYfpbiMWUrL2iGPKYNCQeXhwoy+NDDdwPBCa+SeKxofmCOQiCUSHwZzcOgtaUZgLWSh2VIB5+rqp4HA8xP8rUxKyFzEsXopzOzv6d83YCJL8eNX4vxnpGVMXCMeIO7XHhkOmRfDd364+sgnanKtt3SSD1mfWO6QOCIjs8Y6g9CpHGWvbEXMcEHR8frqTSTbBqhp2RXj+G8V/E/ZEtbN1KClfEBVQGIq0BQ0DDX7UxGOpK20ebc4PmeqI5x4yXi7IdcLbS5b9yN3JN1GKs7jmd1BYw1/GN4LH9/9/UZUuEQny4SxyEZoyjxPnqobocJzG0jDl+W76DuctxFz2w9k6raG3pRtjAFtnprEK2vrR3yHcraZ1PSpo//nNtU+X6Mo6LA02DTrJesK9zhC7DT6EgZTm9UNIziP43GyUiC2gLG1u1CxtQc7Ryn7CR9oXdyfoJRAhUWIBbdjKsW9jsLHUTgHuk6ZMWjSFcvw2TO3da4mJrufzt2y1pn68axrFWQALpVCR58S93E/vv+jK8DBn1uDuBPnuY+afndnqaVS84gz6Y1CEgdL60IAFlJQIZQ33yzfqXzIOBThU5EDybobCP5lZ0tP9bq17gx5etcNX9seehhvCVVkszzpXBUsZa88BTYcGT3RfFPgXkr5GOnYT+s7kC6sdCgPLo6AJkEXc+M4UO3ezXeAx3BpBCjWOY2XSISxAmlX6tvM9UV0e17M1xiUY9xxaNEsw29I61wjoT3g5ZBbLSz1+JjVywjFx/zyXW2mJvSbGtDv+FlgEK5uxiKE51QbaBpDYXGAmylawp4tG5us+mQJMFJdvJn+9CJAkytbMk9WW1ufvtTFSB/TEhh/2gZePcR6DwFWRsyiLgX7cWNKvRKyqdYSml7QlmoK/ZAwyxapVDI74IifTX+anBvp8hGz/XDh/6WUTyDUu2PcAf4Gy9dsrHCzi4O/oe8Tpxsaz9Kgkix4gzZcQmiQdIJZ+a9UzbD/iFT5QekGpA46+jTCTf1Yc8ytutbISKv0UwbMcNwT8rC2SaLm8+u1M1ieGet6MX3KLosdDvr/1JOVqP314cmn6BeCdfMHlqz3VbqQgmnKyBKlII3cnXzmn9eSCLjlfobah10CzEQriOD/tjxWfToMFigCL/aexG35A6lK2IIX55gZn+WLoQwg9xJjLcTMYxJxOHQWMV0PjdgeAONfCbTSav7/iS0iMl38EnOOnIGMw/sEm28C04Yfx/SZhvV4jeR8cw1WhYA8SWcQRsCUp8fVNzapvBWHMmw1X9DJ/sGfEhKsR/UGrACChd7ZHnH21PeEC1JSogosb0oDMWs9o0g1u8WHGkZGIE9bItkLc+zsCiM39Wmuhjf3LAh8BwxebHy5raABuy8qNbdrOjw55mMGYi1uBksa160m7hkjCtbIAYc1m59QYIY74+qYonoB9RvGsfpD5ncnycRRdlNP+7qpKAZp/EC0Q1Ef+ABErTxli7Fl+ummexXnkz1IjIltLQXanLjxPRc2mxsegYdivRykVNKQgArIwEE/b7nQT9rECjG7/U9iJVkUAlHJ9wR/pJf8o+YHUnrv5iAxwRDq3v0DMsrJR73SOnmeJNABl3v6AzJiLvCvzyBisbfhzeXFCrqDGwxulClNm6wd3iWXYrnIV9BGN/XNbzCQBSAAMaeE1+fTj4hpHjqfwVwKHb4pPijcaM1n8CaZc4uTM/nsI1QLlsM7ir2vaFB6XLtIA8dfWg7xeTAqRPxUc9FPjwnw8+SBRrhPA/pyvi4J2gsMrXXa1IEn2qEHm+nYlJFIhhRfuthC5Qo25o8nvQimBIAqYHvFECau2jKlSga43GfpSHOYuhA0GSeJmVPpAsVGJJVj619T+rHEVwB46uqq41tiKwqQ2BeDOursoWA2Rh/2wwJCpuI2w3yua4McIJXiHDB7qwj4BE1wqf0HS81a4T6/b0h8Rz6wZDKLW1AiCMo4EE4xRfZNQKgwqJjf6I8KqbTiFRNb+tcefq8w9zRwFzg454myI2Jo9GSRCsJ0t0MiOOCtLEvMZmhywr+/bRDdmci2NgG+MM9SO1zx+PKF08+E2J+8Hki6mGWzE+FYckqfvEcbJZdeUG169xRa2Pr1FNIBcvbyCsymAExXaAhstseAIcXOG2oNYn2sKfYNi8eK+ymDaPHsG36a4k23T2DuxUbXC8AIabhSiR399qz0WjBc9hdW569752uESuIKmm5peXfDOPFmwvY02c3yvEEMit88b8iMy62pR9k/tOy4p1QFY+piim8eKJNwZ+GT1m54he/KxPvYP1NB3vNGzdw6NYJuvysen40UWSCW9wGo4OPJxcjldPEIzD3D4hh0Y5Lt14lWRSAK0hFMzh1duV0yWLvPBzKAuyOc1EMGnih+b6rsTWIL8Qcbo15jCTuoYeiPsKsR+2xbiV1N29WLb6mMBRs8z+AU5jqRDbao+qkT0GOK3c/9O9/s3ViGfHeaVLy5KNiJ2mS2KcF/ZFCiJ45KF0qCeps5tFPCh3O26w9jSV3ywaKo84CvuDDVHT41t3ZvGMG3h1Euwmp05XiAn7GnTIw+sAgnQ88uBP8wD3MI89CtlV+AhLdcUs4+bcpOeav33d5UFx+g6k3mo4fmhu6OkfPkBwqN4ojiTR4279VQSItz8embLSIK4TAwjLFJ23iYOfqcpdCebytBKHsa1EjQio63KoBM4lW+wZYPdBOVvM84XRnQ8I15b6AVrqKL3qQaYl2i/wBEvHhzJp3SZEKoWTQLJ/Toh8rw3n4hI828neH1qmQXDvQyLXrEctQP6zkh+dTXDAMPObOpOQwTsDpZ0k4AUxE967e2g7vn/q/aOReRzOa8gsEw+g0LBfvC/PxIL92j8tggqtY38jrbqI26j8+uFksz0vp3Le4uxHDLM9/kiTjEDykTmuZnclEzgNzovRiejwhvEXNhp80VX6J9vfuTLZ/j7UNC+OHLQKNx5h1tqC3C57s2Jl3X5dYWFKzz1e71KuTmNWWL7yw4/CGuTodJ+JXTc06g2IGBss5bogawes2R/wvtXenyJrmRtWSVYtrVPizjh1UAUhJcN2rE464fWHqiciugp2NnQ/t+48ilKzYJ60axnWbZPGcrxeeoTnBEfhbBg9TV31lw/G82avLWzhFNQJScj4SHW3OxIzcnZxWZb6UufGQzC007GPlVkLBklVLgV2HETZ/1sRtSXqy+X+e38x635FvyqcKSmiuwdpOM+N+iyVAOaDc9Topw8JUn4lfVSEWdBcB8l+atBlXXDbkqpgyUsKbJHHklcus1uiszlthvWaAk+NcrH33DmP6SGth89TA2zwN+3SXEXXYDWHR0tAY02OXhjYlPzprwZUAdcIZLUhR/IX7OoKLSOnNRgLgWeNYZ/NrMXWvTg/uVHJD6wFFP+KCqwMo9PX1lHtjt9CHA8xZvlP7AG0OuvKDlvVpbc4Q02l/O5K7TaAA6jbcfd3bh0m/oL0GMb9w8DeQTsaQ83DvatjzQtQ1nLyICbIj5jl8zjnV9kUbCfOD/S9Cfu7vsS9fJUeTx1KVfhC5ZIp7yVnj6FFm+B6SO977lt+MzIMHydHuoHzAzPTAeZmgZ+9tou92DCwnugcTdEj/5Xfu0LDtBrEMIqoD/RF2Ua5F/bsHnvTjBCuZ+vqM+A+M3XHzXcEgePTViM2kFn57r+KlLJgi6ihMBixpEdlIcT5fasrB6KRkNqeRMlSgxtIH6IwDDCUdSNBSV4nN161ck16gF5JiQIxBrzc1tf2ap04v7iVT4kiN36Fng93zmO7vqgizV6X/HPW5QkUoSraCxsygfAebnoi9xtGPy6wv6KCbJFyj/VJAfMYZpOSPstBpyfKVt364hRf0Ixsu7DH8dm7CYiV0mE2WPEsQUBBDoOfy+qm23dyaRn0H7Id5hT+etIdUk65SA3B/tTQImVJg4WNkhG8Vzdr7Si5FKplIEy06fmOBeIEQ8Tw9YNsnafd9aD1E0MelRnt3aBdA65wtlMWl/AhYWg6DYb7gMCdhmhmntOCP84M96zYEE05BbvdkS/R0NQeDKDzsixmT7UiqzQu4Yvz03b4LBWzBb0sD5GLcrXpuM/SlFQRm53qNEljHWjVk40tImeSrkpvDeJiPdAvU5F+N9rpETAvu1YlKfY6z/QJ0Q/5986AVU//oryyKw4+rk58LFnp+ppfnOWnh1zg95gZ8OAs5jSy6NtRQy794Mnw/al3FZhA5K7UCF37aK1WIvfHX1AjO/RJGBgXDejX5AOFWPbWKY0X/lZGzINd2buJR3uNg//zdIaauYMSoxYhq0v4SIaaHDlaxdbgm6bogSg45xlJyh0FPxK1z0+dLAqZ/EXQWEv8TFhvLezB1PFHGk0Y0DtGNp4tMneesHn/n2IbVU6OzErycL2FOeaxAUFVcnMGRQxe3pU02RIg5f/3O1FyvvuF5n4UOQGUZ+5VBGhW8SaVQw+5XvWMjncJ2JY2kBOkTWnyjBwCk7Yu0Hw9cmDR7mayG8Pm7ARdcIBiXkZRSb5w+fWaqc43iScGTnjsrqkcGmmqo5zt8BYmF49LWS30UcwqsLoaDAtN4PhlkgmrzK0YOB37JsSjVvNy5Oi9KvWznzvD1/VHO86W6F5o/5KDUfleSOHudHtJqhmqGKJIQoPXzL6ecdfuqzsE3KvBLdC0Ls96HHnOlZMR5/NAga6UDpKwLeW0FzXlqmwymHqqhHU/PtQkUXtVqSfsxnBX+kkXfJvnhauTqwmGF0XXXwSkaWPTlnMaltP9fR89kChf4FbrAXNdHT5dDRudtO8mK1lJRaRvUNL4rJ1vUb13YPpoYjMRGWTY7M4SNqf8o1aUcZtH3UhhdpfbZ3yhbPwDXNghz6Mx1VqFyrPcwMBf9vuwa/uBvpo9xXVR/x7cvA43jBwr78GtIjhcarhbKlebfqtNhuQxDNjN3ht8MFO5I07pmDLiG5gR8/4PTVgp9H4l5sQ38a3sq2bbJVQzrjzG8MchOE1Y6ajwYx6rYUCKOeH/GelC7rCfCV7aaIFHcLYJd4nxyA2jOpKYtWlIg32R0erDkd/GIytntaG0NlpWIsTcy87bXbNcBy/SZ96ADeVIVNcIIcRh24XECEBMMrD5RUG8r+VpCtc8QTQXIThqInr6UkV8hsxv3URwFK0+wMIdA1eQ1f4XD5HSofEupuKC7vU5Pcxgur/Gz0Rr82R/e/IFVKwSMQFpezT9cmWfZwKNnCRuizwPdnnSQyxB6eRmMYfjpNMNVfD8X1rpS9WqtwhQYQFlMgiJfWXhBuGIeqWlGWdIi6P7jNzmIZEOXBak6uYcSeviv8l/6KbJB/hLtooZ54RqgJ1yYr6WThr+mn7Bs7xg+3XMgse0uLP5Ug7ireawvqno7GCxE6DqCDcYeeGbfLVy/HgE6UaTHCg/QC4bOWSZBf5TRy+RJ4lcTNDL8+ULd0hb6u5p+qbfVUI6I1qx2OPRDnKqjQcgc5gSmr8KpDawDEPUvvaQb5K1d2PLVMULaJefoBzay49CYAXgPNEzmIZK0K5aDfOQ564DdpJjs2C6ynmC+ulORKKPt9bIreCNwpToy2aOryhW5hQ1P1PhwboRUH62YequU+PChYwALORwPUsIbOlDh2hnIE+KxUXjgdXZDOq+4X8CkhH78gy8D7uoQFy3VgSQBNa8+unu6A2wjD2emw468H2sxJcrEmkKMrRrRUOaZwYKRqUy/qwSfP0O2Iah4v+yeSiYZpXroo6rSruHXYR5OolpP2ytb8OMVNxNCF8WHyb5ulwnhYjWlKoBCn3uGWbfqFb3oKPp8VEEktvwiD7C97LoYJtFmDbXwFur3lE4O9wlxQNcyErz3nt7EqWR+I8RyB/lZiawMqqCk993l0bNkNXxeAQu5BdH558YO4a3nQPmaRr4Iqbco6X24dJ+4iJ7DjFSYf/5+o/cBvkOJi6EBZGWWNeBtv4TRKtfFGjAVhW7PmVJcCCrbjZYeI//2ECmEqcm/nnc1T+OJSSpcStOXggiWwkMHcmDUOvLNRPyccOBcS4hQAaPUpWXbaR2mwyDdVruPyv00wB5ZBB7HPzHlY8MuD0g+/32xiNQGbFeyltp5JjkQ6XjddN1X7rkS3ysfaSrV/PBgDm0cp9QuVRRF2U9t8Vzie7EFQZy4j6wWyYl/3IaDJTXC6QPPZkU1EaBwlZUo42MaVRmBGe/nxgSCvEK3kYKCc91kUShzohx/aSG7rspVMFG1xyAH35y3wYiZhlFmG6eAb8Kj7Sh7kb7anYfnpumkn6UX1lHFKduSwM7J5aHiOi7uOhuImqgHWVt6fZeCYZDW/9fp7vLXlb/u87LC0jAwoXCtVfTGzLbJ9L6hV4uqPsfnELO3wcB+2LJzR7Z7hveW4H2U4I/B8PHwVql2/TiTA5nbZqG4g/UiW4njIEnRL1tKasDeu7phhqvlZUZDB1oBwqHng1g+y5Ee0CrLRIceFtUHzJeaX/n6Ck6b0ELK7CS3YQa+jzexk/TXT/KfouaB9bS9tjUt/kw0N8JqCPu7FCkUhoT64EE4cQ9lEUPiLoorEDfygxnrdpCyOWzxRcB6UrK09ZGFOP0Cf5p9F2N6MKUKl2WiBNMUU0gpAbD0zSUFEjb1GXVOp0PDxG9PO3xctsaCNfpxOZ6CPUiiTfM1IM3W//Eb7eJD3Bq0d4Imr+HBKvDz9JL8hZcuSFLQ02CZhKLPPc8SIHZt7mnkB2me+j8D9PuwqEpc0irMKXj9IwstIQNzsyssleRLn23IRs7Q7QOksEXKT8olCfN/2zgMSFMpNyYoNu86PUlhxBdUzQCHyn9QZ3WF/TQq3noav46wPW3FvRh8hyL5kG/D7YHt3ekNR63PGIJEd/tCQhnzkQYEsSZy+xWi7gVq3AA7R2ZvPAYvyGu8/OKQ8vNI8i1z65s2SXRx0oI7U5dUodBy3jWCGLvhzB3CVu5jMDBqfXL8wOiM29pwh+OTLOHXg00II2hK+QDTAbZD0LGWbH4Kcsg9pSMPzy9agEL9DqDVJTQ4sAvx+gTnIkdPkZZ4bwHv0BhPf5MNPgaHENvZSQ0LeHGbfBYqp+NbI+k9KmbtRLkXlf36fGx0YaFDW/c5j1GaWVEnoRxZ6SmkfOX5M8ve2idVa0el1Dy+Ghd4DSz7zsROOncORJs0gzfZBsSXRQoFyVd24kaXZa34FPKtTLpmDhieIz4ohgpa+IctpC+i4CN6qCNdLHPLzvNGWsQduYxewrtP2emUppZnC3SXz/8Fh9/XAw+1eZuykSbiUKipAVx39B1GJS2s+t7EHkDSCo2jqG8nlS3W5yZJx9aGM0Ku5N2sDn/ZxdcgJY5H8LcCm6iDqw33KVXoV3ydB1QVnluPveM0ASL7USPLDMqFPYr8i1o6fCCHMIfpJhoCjp1j+mGZjAB/3p6NhhEDQZ/9/0dXsynIPg8cDcvvwMyQm+YYGSN1tR/+hT0iLuR/UFy9MVbC6wbC1bJLkJtbGLMOH5EPafDdRxgAZt54K+EMbX5HbuwIU1nnspFbjzERqOFXXpxXVywrBFP2AhMSEo7c/quCbRmSismE/2jAz/69CWQM5KRBsC2yZoR9JrEo4llhSTQn+wtcZfBtqb2q/z5Wme3uUU5GS+w+/SZy5LkIwmYjEp7l+FbXWnomnArxOwRleNlu984xCFdIVTHfgC1d9PPDDdqJAfUdOqR60KbA+aRFKENLCmeV7alhFG9zDEAR7Pz0zipG+NxKpdCrTW8UD/Sj4b3Ehzxc7MmcoGexQTlRpSs8SbIu2bXxl7Qh4WR2EAzjiCIq65h04Pkw9clFPxlAmwS/k1XdYldg49YWYF5e7SL6QqU3OGJDLamzUWc5GwV9zz2Hz37jAxEUQxo/Ni+lLqZyWcnE3TPBSZyuQ6Eo1ecBdIyb3JUO8ie3csP0RWj6n3moB3TPU8OGteBLEgHxgjC9/68o3ZK5nDngicaY1b/W3M788UTVUS3oVibp8PnKYQ8c2Ef18UMS0+2ilsRjRA7chNcpQ3eTFkGh0Atbx4Ou0NiDHTZ+ZVRZhEQ0TuzfEtvXg0E7P6MT3E2mn0sgE2EwQbW+H6MSuElMLSORo+oH1WuACGHUJmwaJgFcuZDOB2v9iHGO4C81L8wEloZVlZfVnqvQR1oZTAK+AIoscLGEQ5Z30wxGZMxOmnv1c1APFv3xhxnHnbqgccQwMr8tMqp7ZsVrGFC2AZLAKQZ9dVz+DDyUDuxhKNgleIj8SAWP4OR64qXmHbOT+1B1kARlSCfF8DZ9PqepT4dB9YE4roz3lo4xVuB69bx6hNjXnc26hBXJBSZiSaARtwxI8f/qV7dRn84E/Hfbzoaz5oE964HphTc3z8gAnV0bVY+girEzcaaThlEC7cKaZ4ti91i/c3kdyGMDur5JJMpeb0miS6lw4k6xj3H7BJYLIlDLVrMQ3/U7D4kxw8W0FE6TpX2rtgmC2PUsZChkv/uVe5rWKbif1Z2YQHzE9c1N5S7VQ/UH7OpgqPI8Ih3AGeLWpwjz9NavvqIntpG/iz5lFNC0dMjXVRgPvSz77H+GETTFGkRqDyIXlMEB65e4n4JW94lBEirhTmnljFRUbhz+l5eflNw7ofiNhXc7IebkefoGgER3uJm08FMZtOzkMW8gudUAK1nup3+fH6wZVNlo+NGfhrN2Z3ot+AWNa2dcsfz6df0iQS9wcu1bCSIlf03A8dqPhpxegsOmDr3wRHbPIfr9NNTO+nedCLKDcBLkjDAdmKyjilmzSa9p8pkQBmjC7w297kwkpnN+wUcsuMANe0RQGi0y3BEVllaYQU+eI8jpTlNPVq3nFYqQLvy9NjHnsq47KC2A3dWAKChEH4Nv/S1Gl/edYtocSlhWOc6Ttc+5sXbntq46ff2uuKlDZwV+geGVQq/WXH70jycb7uFXMyO8ohgEVFRMt5yFeKxD1Ayg0uo63i1xSG0EfsdfqjB5fkH5IlFQyCQTuy7psdrvSdZwJs8W3qL0Lx6kwAFhrmLUcu0B1MWelPIiR+eDhLxaQcQCNRl3u2r7b3hXc6ituY1GiHYD1LvwU5CtCTaogb+ZaDA7RPq8mf7ppChFRVLru1w54uJxTMncMpanaJ211C60w+oV5FFgBQkCcL3G+Ot43y2+VTekK+NHsw2Ztf1Gf2R5CHQ9DASGhf/C1+wz9ybs9PA44yZbZVQVGB21kApspxiWmTyuXy7PrwYgVP2fRwbwYF6OcALpoTlWjewB0ORrAC/Slf7BEvQ1YcA3HD2lazlOTIfm6KuNPwe1xCQb8vuA3e9uIBc28Zpb5FnKhfXwh4buZx+fhCCOFdye+8dYj/6h9V98FSOTblXzqBlLBNoQl60v3aqIdKGH79M2kfm/a3O68yNnL1SNuYhCHvCHxCEDBrHZlA5TyUgpTV5fLS0tqdtNQiy1xe75cxDHxY4rO5jGL563Rqk6ARxhzfP7s4fFFL2T7BDDkiCGl7pT7BadxHQNKwtDtaisx2qO8kx8K1uY++zEHMxAl3QgCEe/sWUOajz+sIIYOCh+mvFsrTdEF4R84gwU+Md7WiqDIgnKNtqi6eWr9OL1i9NuF11EJeqA9YYC+VrunqAUwMSb/RCKEsO3CSxRjZ/Ia4YyvaTprrG/FxbPFiU6vOky7GeaHSKIBdTKTZ0MG8wzNb099dM77myTPwVaD93xsZxdPkXUt2uNY5KbNhItd7anxfIbVN2yO9lNn2H38OIyy4owRT9BRk/RG2AcsRk4Ty08ecLrrcGu5FTu0uD/87SSDwOsLeevjroS+ngo+d+bdmJC9A+tw3WBWMfoot2ILyns3nxsooqNqMg8D7/HvOQYrtbD41MITONT7elDxhRDTj3b5YjjRKH5gG4k7F2jUHitoEuMuerIfRQ649p4Qf+vhWGYJEANebN9mGQdfN+sGP3NOTe8sw2VGy6uYz+Qx3JD1F0iaIGwZI0OpDqZc9RX/GOPjH79TYdWZBrP2PFzCEDtnkTesX1nl6aaoQYpJ9LeGkl/dhwCf5/gQrvUtH7ksLhvPYKXQ05c0lOM9fC3jx3Hk6FFTXzwwNJi3AhiTS0nj7QfO9AjIzyzbIUdPrD4aCNT1JBdNgkRLtTdYABbT4P+XsI6oIQv82WissYGz2ouowqIdKdeNkEGcf5D+eiw2Uo82yaKSe8jSkGerh2TF6FIhdgbjyudo1JKA2C0QavXgPTlAUFqLEHL7bp6aglful6Ymb3W3dqnGG7L8OlgeVkolFxgOr6t/8Fa/3IrepoTuDWvBrX5kBYeowe4QKmRBiVwJmFNVTvdpVB1lJtnszI+K2ti3E9OKeDsp7J4THkP06ym9LYXR9Bwvydcc2YG4Z0mpg65qnY8wNC7vOL+h3E6wz7bgM9ROylqIfHsO0/l6UtvRmC5n9c3X3AuK3gq5n/YgSUlzqsmqKz1eQVinK5t0xxZ70HkSb7CrEnI5ab24XSFAZxLr5vxjg7hGghUk5RHNd72i1cRZ2JZNNBKsn6qXiNUaDKEVK8eF1uSvios5vpJL8cZg7w5jVhdxM/ykxyqghXRKmiiadfwmy0WbypND6O1gHgCAIKJdxHYirlsehGQhZRvJUeA4BLcPUrdOYKysNXDQo0nPxQV2EnOAOsXJiYq3PqmNosJ7ap2wiVWkgkdH/PbV13uaXiy65Xxz5WnTymb0D+aYGTrsb9z4GED8Za+qd/CLMhJgPia3XwXGAmm+j8fNFVuJdbegECQPmnGlTL8ppQsz+B31nUIiHkNhxBQfM/REX+fxT0XXS9HRts0y6WMJ5UY48kL6jOcwKYoA/kcuw33eMc68u9JOBuu+RVhwY0dEJZvC6oVaFOfnadEXMXsU13Mh6lIL9qT+A6/Ooq30eYLwZq8ES/qrvEFZedZKoefusgurj9Sp6vymiLXNUuw0Ds3z2iUTo93N+eKRCfZHGLkXzuew9DN6ByJf/3fvgtZJ5hkibVVry119i0Xflbzh78LqZo/AsQypeyCVHC18hNiwMf30W/aYVojeRLCB+yEeasHG5fTXwqmErm2a3fIafUWT+t9ax5DvyOPi0VAsp7QppQF/dIehmrSbroRVfv0sN2somiNRb02h9E/GhN9YXBl+vedSg4ueqXqjCMWkel/a9OxpkGuANxnQwRdKAWNtiWjv8T+5PSRgjkIfxSelSep0uJvoht2CGiAlX2CdAgGU6wsdmMXUAHALSnCDaYcb3/nROzO1OHVM9lhs1ZUsDus9Ou0urEUM93gn1Eaf/kP6cfkpOc5qGWIppFHA9pLo0W/7yhdFQce5HFsmeIXVmyqTHhl7T3zBfCoiSA5YFZT92uIglb/OfJReCgw0ly4EEz7OwYVpkI3qauCKkRlhsMFWAkWX8eHsDHwTGDouMRM8nwpptSnsOZOyqjfqo9fQV+ROM+UjW+knF19ggGBQ48RtWXJ8B2IvBL/nViPbfuCG7bHQqOYAwlpJO7G7yTZWxvIXmaLes0rYcIjDeitLRg/RMNSwIhZQFk+i+mMijI7XQKoVZtpmYc0AbuQqqU/BwahhubldSQJdVqSKSNgF7WNRQeiQdCENuBM+/MxTA0nEML6chKEWbbKY3kc6kVw5T5ofht5rKESgFEi/V4RwvVpuoDNx9fnlwRpzDlQugbFlliuYQRwbcNYgu0qrcg/hpTpJD7pdcVDzjgWr+xG44pbRU4NnzQpaFJm0V4FwT4P+rhW8B2K3TMI5fyLbYmzJj9pA9j7wTxMPcJq4TQRSEA+e1xUiiQCz8/KMiaQxd1yJyOTg2O5aH0fZuoZuECoshPQ8qkw1hspF3TvnIOgAB3FiyOfp4guhetxFPp5Qg78VaplOIlfa0k75JdB8datgsGlCVqY1mu4XtNT9o2edCkmy05tkHuj5zb9wRUepkECpvjyN8sbkXDAZZrcqjQm31ew/BVpmMggfLPR21gmc9/GRAGM+jCOLrgdBpNpOvx+F49P/+0rO6gpDBdRBAXM0yyhF5vB+A0PKMq3bvon5atYU4ViB6boL7IiIR2sLrbaqyaUy47kjXHk5LQdsha29CfjSeid0DZ09Yk7JA5nR95B/Cfn0FPe7R9xJmbwJEPW1To4h1ea3fNw3aVMWdjsRtYVHI33INNUEiTUbF9c9xZ/T3qZJ+quciK1S4MB7U18JLrUUkIjkIxg378lI87gxuNAYjIU7jXvHTLRY9a1s29cPklLOIhpl4elJFZkATz6zFAQnty5Xvs8AQ8YLpTDQMPyqAfPIi5eIQRj+4Q0wNzKFuuW0weOJK7wf6J+nYtcCAzPJdbRCY2mYerwH+O6PuxJ+NDAGIz4ZRwlixiCrHoM4i2ErZzKeVU3NK7K4qR/JCNEZ4PbqkuEuRDeodWoDmdnnF4l1ZKtOzp8x4jT0gH8xVWz704OnUV+cTJySYc1Iqdtj2UW7ot2548JiL8B+4U6fk3pVQtjHDjhkonp9cTea4v2TPC8qLVf0vSgeZdJepiDfRHXtVX36Or9xUgh9dYtFKmuocfOOTGuXnHfqgzLyEANzi/p8qZsUW9sbPgE2uga5iLzE/JvFNxOlEKYnpc+bErgRiTem6+Iaq4ZRcOh9NOxq/ldJmweHRiocLzkktL0Jw+7UyEcEVJd4YhUi9GaV3+gzPjoJCzqYXNUBwEv8iJAaOIqn4XtW7Ktt1qLdSk78VgK1KUyxOLyGV1jPpyTTHPfZxCP4iqlMOsqPYOXnNDO8FcOW5zcJSrKUhOgMog+KZqSapABVCnCD+ADKV9D6l3LDmkT9RlEmMt6K4sp71TbQdsQEZ5uJYBXNBGUrq+X9GvXNhFElv9vVXg5b556Rw3aL46P92JymXF93y7Xr2+Xz4UkX8EAL3t+/URXSttrc50RKWRe6F8qEYhfTgra0xONbPVSd36ltkX2lENJOo8BvHCQiARuLTUMCLH/Yzl9oOAQWOUc6FOI2v84tMQODXH72gnaJW4VcrmQLjwG9hsBgMVg1uAFQJnmJkmTp5D4KQuzulB1JcuyKogJ0/boZmqWYXpsiXW3rPdOn0NrwZ11XgNEb2erKEgmaOHWz4vR3rTR9C1JXVW1GycwX+Llxt5IgVZQ8qfg65Pj82kD6Eq1pzPlRQBt/qgnn6pr38QUqX+KMF4CwUUV810SjBF7llXGU8kMep84OoUimAALCbpFlrOohQi5Jf9tZ1oyxM6fzxzowcGW7bXqhjS+Lvcba96dox8cDl8Ym5fVR6cU2GZvsE8psn0kqzfWq1o+UgsrksyUscYOwPQrrJNbEfVRQZnogkG9xNX5XfEKjXaWa0wpcDXO8sMddIxsJIoWfgutIAXE97WbKul7QL195Q5BN4lIE81vTGA0ZxaGR/pSy5k935MD7HanBilpCYxA8qaDa6TdOtz59GWIgTQNAXXtkZ1LhybytWSnz8k9X3AQRdCVn4QXp8UbfqwPo/Oav3Gpia1/wASQdyCBygKthHPuLpuzib7B/vsrfVXBU36kpAr5TinGt0M+13CChXM5Li/iNMZX+nNtGKx/GSkakA9Pof3FaB9e3HlI58Dupzg6HVA/EH86PWNPS9KA6RRJ/k0xRto3uBpH4qFgV88HnduQSKyc3IzYmw4XM5hL26CAizEExrSv2LlmNzhmTYDCDFEciOXjMYVSRgwNxfuGV+HCaAavgT0ZX2msM/5FIEfqWOTweciIjEIwtZFxv5ehCvGvVVO/2N0/crkUKNvloEHCXzKLiy6/9ucT3a2S8G4tSdbVGoXxM1/q/p9rk1jt6aThwj8xGjwYQj7DoS28+yeluqARYl1zWPt9lLxhz6in8dBmXjdxafIfvvOh1FyyGjeRnePNn4Hf6NvJteD+hQKW6BYGQWFLAHlg7zRW9QB6N87Lq81VMhbQnHuGWHSWrpdqezmZJt7OyUBix5hK3jP1iIPbFM0EKv0wygkrfBfkXwqKfI4NfhS4ohQGU0C/JBsfN2EHZwB3CfT9eQdcoVj+0yMOwnQa8+FfYakgCwf89sk4eD5TOiWWlcwmG77XTROJNvR/s8r1dn0NOQV82WY33UtzAcrx0EX9z6c9QMYafWsZBWSuDoZlpbIHNlb7ECab5yuyZrLzdFMHRsIPrJvnc6itbk+nMdt2ceoUGNYh8Ty4BVItkb1mUxOKWtNt1kqklEqWE0argVixyX3vusV34aTC7H8ki64Ry43iIf5O5Hv2pND4iKiaEG4FWwAMHCQyYS4CMihf6B0Xgj3bvfb4KcyKHJhqx2UyDUTQkDnse92oP36f/7o1rjSxPqPYc4FqevyqJ51IDDsLZzONQPsnhu7WKhKL5W/6DXQgF76z8IPuwgElAjXwuZ0kP/V95W/YPJT1LHHqhLLyP+elfB5Sla8HgsRM/iM3BmBSgntkZwHAMayf1lFpgRIMkQhwtR0mN2yi4XfdmuyMNS0hbLEnpOWjsxT4vBl+s6hJJ9Ef6gOKHv9UHWinj5g7tgH5+5F8zhh+HsBOKGpfN3HkbL27jjN8xtaLu6lMVc688YV1dkGwLg4gdlbvwTweWX3WfNqv5uma+IXA2FOzCKLxv/fob4xqwfC9ThEwkxFnxMgUwjD2l12DMnOhkee4HtjtPwZHFw2+ITEPeiUPa9GkCYpDqxg08Bf+319AN9DcTizGtH+NwvSn43T0pqBpsUSVufobK5wBhZuTtLO9KlWdIFke3fXEqn1NM+mWDKt1LSPIH05kBLX8/+LMDXaCuU7juo8pB2iszP4TbD3jBlNVKY0wqUdPYoaNYjPLAVvEQeCB99twwAsaq7TIGesC1C2iicIc2APGPo/NIdhOKguiCGJDTUGSRc5qRcw4CVm++py6XheHe7nOqpAfsZ5f6ExjvsWLuk+vG83opotvfNicIlqBQWQIFjo2gFQgaqg21Ob6oajp8aUdGIURH2JfC+/P0OnVvQ58wMoTZeyMlzpd7eaqYQ+TjrvZhBz/QH0qFIE9LqYuvatbHymx+XmFPNL1Lbu4neAWIKKRdx780WFgzuuPWTKCg23mdQsxqX4DtJx38A7at8XEfrBf0mOsOdnaIn6/bphqy5dNtaBrxL5ri39ezETFTNc/5xe3GkrC6TUfWqm2WLnuWa8mZLyQI25EDfjzoqH64KbPJzg/iqXzTEc92wwQpIDMBpevqsv+wGOSXINk8cRKDkRtk/mAGLl3GBBPY0fdKiXiQXV7BEr/+4tMFYAgCofPfdztAMm8bdAlbxjd0NYALiYZ2gJ9nA2UPntFvwIDYahqdlvHABPEzWMr7dW408lwt2hCEVaSiPfIrkoxa1xWNC+hD9fT85bydHCbBS+vO/YxfWSoow2QTonY/Bw6nUkg9YM3g/K99zes3bgVS/B0KTCUdt8LrIH++uo01pX8UNZSyDaYLzTIS2OzyX8ra7YLBRyNuKlGjlbTOTziMckBi31gp9a3ua/NLckPIfKC82vjDGel2USXwNsSqXrXXRn89jjY/4k4cPuLDwxz79NULCLdoVdfHWZ89rUzasrRlK45rkOK/kUnaYodQzCK1iII7q9rXOmCqh7SI83yIi62cIGZhYXR7VkdWi2WpYpgINf1jEVCq2UqGdJ+pPld5+St2BmQ6LvCn/cXJ2YN1TGTmTuiga379oNBL+AenxcpG4p2AiuN7rrc3ArCSh8nDp4riOgtm81s0Xq9yV9l+qM6Mjm8BplACi7LbPCq8beXAquJm7ejuTaw7F5BtHmBcIBbU30xChv2+4xh+RIYXSfnHj62mL1PfzkGZBziPob28Q9yXOsfXA2udZ0Vg+c6DXcfLSgWqxwsZGMKY8hlbbQQi/sPMHwGA5YfKy+rdGzYvl04KbEKCvpALpD9EPVSkBNQywuLC9JoCMRnjYNAPXT3wRsLEN5IfUmwqt8Dl8XCuRX1lvd9ZkglINF6UgXNbSFTZEMTgMgB7dpnnjmfxnEiYpiTbIqzHKns/g/kiTa47Zp2CkSOwU/7u/tS6h3dA0Uesk8/zNtTLYJTLNZClbOXv89rxDxsHS+vt59nGrmVNE7tuR9xpS+nkjNvWPNJ3pXaymlxfQTp5IyEh6atxNK0MVWkqtcvk08Pz7U5+F5WfuBKFqk96xRlLuic9DUy0fzfDVlZMe11amkxQr+E4DL/NzuHVCKqqZoLTO7kQGwDdjc8YO+YO9bZrm1IxFKK5j9HVRCoRCklSQbgUC71ZZl8Lx//kXOKj/VqsNCulMqnR2QkmHxjAJA9YmY/UTjmU7EZQg2ZMDTC24EY6jddDhIIkxezODgBtLntexYiWtgRVJn/z32QvblbQ8i67fcx67qO28NLdWzyWHSSAzGr2KUiU1nnfxbOX5JHuUEPqGIYv9ai5eZDx2EcVdMGcw4t8haopSwFpc9EoD99KSTsD9GmZG0SoUS7zKDIuY0ZWn61mzYgjyODjEcUIVuVTeIEtBdCDaE2QvlLNXwZePYWUKQRX17uGbaCx6tfzyCVYztYNEYmVRLUUrr6tOaPqAeTsiDS4+3Id01aajqS8K8CmBhOZ4NutAgrxZKSb50Mb748UbqwPokGVabruRcU5U/ktrlAmn1nTw0Z7p1Cqyh/FCRmWcRZuRr+to21B3sDFLytXtbTgzi1LX39sKxm8RGJDHYx+v43Rz+UQTsu1m9cw7L9TvHGD3gOfZftDY4LYUNVesrHMbYcuJFD607f4gNDCNut5noYb06r7AmJB0VwuvCAq6OKBT7cdlwmydTYnvnfub0d2xCUbt0M1Hui0xGOPUYdF/5M+H/e9AWBdLPtsznrP2q2UZAAlXkFUTpgvDZgyqx+1+cAcsS1mVwMT0H+aX3ozDy5DoQlzKGN+TsDy1JZKxjXPqc3EunfylZpfKG7ArfQFju5FSvCJ38qdPsMJUPHZUqOf3Jsicr8QjXX1VYpw1zysLQyZ+VJH3UsTOGSFD9DF6g78rdzVRLs0HLiNiEuc/J0fM3BE9BYFpvCrUQrlWmDWkMPXh4kWJYnyzOjkCtNNAd9BgVZ6v7GR8l3sI+ja3iJT0VaOrrdscIw/K/ULQK6EbKA04oUT6y/Z7MwmknlUIhuxarphKsnDfZ787ZJ1XXR4IdCKmYC20YgTyyJV7EjRTN8YX9O8DGY8JpTA1RBrxUT1udNfen0c4UHJpxRLkb9vEVB0sWsTsxeaF4ZQ5vHFJsy6dOXKoYjSCxg48zvEyp3T8/X3G8rSWaLwljc9kOLavqlVgcXoa3/AzQ5NE6DHMUAXwq99P6ad8/68CqaygOSjnf7rN6PWoCuwgWyZyl/n1+5jaqnZcCzHm/l1JSGP/8ILf1pmDBH5zF+HmqeuTxP75tKYjFmZ9ilYOZsLrPvs+QZ8DDJcXfKo0+/PajQO0Z32e6uP3DvBoyH+Tga9/Kho1KZw7rAyRmyDi+Bbd5viVgXbfDMSq3q3RD8PKgLuAIZBWcLl0TsPUrVa8iD443tDmFj+RSlHE8bP7x1RTWMFL1qgyLoy11QcyDbMaUN5jYqMR6KequBTXfIh+hOBQZoaxvry1sT40EepO3YdgTj5WAUABuXZ7vVIVvKuJjGfmbE/DlsZfg0GfiAhGozc5LnkyoUtLju8RsKb5tq2YVLCsXonvVA6/+AnAHqubpngEXbyxbLf6b3gFm4Jl07upVY5HLODUgi0kYyAECYhusbWMZRXTO0WkqSdnzfM0FcH+99FYCD5gAC/6sAbjLaivbQP8rvi7qKxgzW41NlWN+p1mEZp4OBQp0C4VnY/MQ4ZB22lATYzoIbgpL10YBNvmEQdC9J3ya+QpP2Gzr+Tm2gAMiDImXYPkH79R+mUt9b7byV+AK0ThUK3euKggPZrm/OY1t6ZW31mcR9bBDWM1odaxxODB/jp9zGbR2rdrx8LKN3w864ik8rY4cr9qTWWzvUDj+0jXDmUnaaudA+o419rQfZJZDBd3jIG3EHp5n+0Zuiov5ps2Y9NxQBMR3zNd+KZQlaQ6ipxFRUZuo5PfQ9pdYRRZnV/qj6rv1ExxrAZ9Dxq+9yx01oqe2Jfpl1mNra1j8Y03/pFXt8s9Or3vNvkiGYWH3EImTWoW7w96jt8SZi6DDgtXLeQyj8Omc4U0U2weQa8i/G+pz+Y9mNO3e3oTXAXmuA5+FVgmHK18D4Ip8TE6k3+O3o8zI2zhelyex0zpYHwrTbNs+l+8oCCa3Mglsc9U1QEO7B6gmja74g5WAambg31LLXxZuN+12/hG6rFTy4z88FMQyPc1hxdvVq7RiRhfKaS972LNrlBquUDQsO4+t0UWUVD8+m61b3fjxUOBZGrhEOhw93XbaVvYzpL8AAt3UKgpb8F3Qb+yv0exEI73Y/phbOY5SOxA5zwLGSF1bMMYNcXrOllhZ1DP9VV8OPjZuOrJIVZyukPP3WJglmGwcUnImuKA1v6VE4OGBSE97Nl0M6b1+Fu93BFTCBkYGhdburMZ1ulK1clW7fBqpoptbsnSoJOkUJgkM6B/El/fmrRPpn4Ih5uOSum43YMs3jTZ7kKCBz233b+PoXqEizZ0FULf1UfayGQgv2dgGq7ihNKBZuPBtF7/PAqie4KU8eJfGOOl/obUpII2ugOnqU2tEkyxUg3Wu5MGAJoBmxs5WB9JHJwpQpZSc6aaVhitu81e2I9acb0U6m5kK+UGZLik6fIoYThAPH0ukloi35/gTP/IjN0pM3zsLWSO4Z6MfgMF/HsClA6TYKocCQd7ATpnLVN7A9mVlnYUkSO1SVFkOasQY3y2NIujNvnHQIb1pDPKihMLKe9qIx18GNHYfopGYWuNVCj1liMDWvVovBw/UM1gU2bfsdSH6nv0uUoFeujgk91RM8q004INiJL0L4xmxuFwaJbjLOmET4o+fWkWa4ygN64sYDpvcgazzauaZvsaJYdfvEN2NsiFmJ+VBmsCRPEtMwqtkNCAybDhW4xe0I5J8srlJeJbSCI6YUMD70JwYY4MAPG/GE3pat5dOzbBYUziC5WtwV9RPPy0DO/UjqTo3yxEw104r2RDBYmAGBz6YDP+48BJUT7lsgTO4qJzB8Jb+54dDH3U5jU6aClxhlrHUpg5f1oKrsqU8N3dVdUFNbv789si72jZ0yCBbLybqT++Cx3wLHPgj9ECv0NRrMbS+DW8k19BEJQpMTMt3jNMrue40F1b9wzeFkX6JCNtRYSij/pJ76xxvp2n5906Pac94WWl2rIBbEk3zQxvhFppiXsrckGsSFb4YyrZ/zgPN03eIB9OPG8je5SxKt24a8igL/UbiLCT9e0BKtdOeFbddjiqLfHvsEUwumdc5eRCcolQQMIqw4XKnXB1noqHl9orB0Me8Hm35LfswhI4NpS1EGxv9xXa/uR29qwh5/JTEW/3ceBInssKUPs1e1XyiP+4Y+WCqx68/5OI16xoPGbuI5N5nYz/TSXMgxjrr5/AqF22QF7oOLeXGmg9DchqGn73jWxLvMkxMyBhiOFNfwPJTvvpvOBTx4swoo4Nr52Sh8n9GoKVOZ4Lm8/3AbOyt0ZI/S5rPn9fVHRlkxtvqOgHWz0w5qQNIJ4tWtkpQTsNk0ciPqxKbmRLOCwlXa/nvr0v3knmYH4VgiUE96BggpRYeReZNDOzzEpn2zPbcPpwWuRA8jaE0KNrPaToZYEdmVWIDfeNrcanSYthO2G0HP3cuAUvmhHXRFtFWCOnsFi2ZUjM1ftfFWyn6NBHI6miyMR+P/yUIgBo2+j/XhLNwKjC2Y4xb8frf0+WitnduUqBzKRREYMCW670yAaHhy7Zrc4kAjl+CHwT0NGQzZmgaT2nRPCqXuQPLiuQbyeOgb7wrtvtRja4TA0SbIH6dpWz9uDARqgHuGlAXU1BNwhmt/2Dbnu2VB7wbqAj2jDfOpoheh4ppAQHJuHsWC+O7e2eY9vM4U2az8GF2juk2tUGL5GPMTlCgCQUjqXCZ6GoPxCLbPu1e5oyulje1ZNuD/M+oMcT2YqcMKvSwhhaZI6V+FAA1B/FWr/undJzVKh2XAzZzK3uf03zaTjV+3xoM67JYCX8nc+cAdaleHf3Ol8siIc3Nbq1y6mUAcd1pHBRhxXE4y/9ke7CXLuobrAoj3DGy1qpz22WYf29cL3m+JMtg1bWaGnEqj9AgFWrtOWMJ6vxxJ1tX/ncjZdtqN5wo+5l7KSnrdZorop8dvShlai+m2x15es7JFdCAoFP0+XxwkicqXrIoXFz5Qcv2tLVKFofyNc+nK0I7JMhYerLxuGm73Ldb81+cIi4k5uFkYPsNbkcuV8vcrFeE0yk25tQxjJq2gaNEJ4a+w+AOx7rB1fLUz8/F2VAKrH1cLm9O97zlc0BLSC+y9k8TfaebZ53+uSsfzZHHtWtPg3XvNWt730ao2+9KEbXm9ijfKHeq8DmZMlgfSNFnQ9CMg0V0k3XYf4Cp1nvZohYzhXBLGJtBYd0K9NKorgakOVZuXQRZAQCmqJyH5Ng+NB8CGb96MP/1e69yJkbRusYti3MKUiejOZENDbp542qeL7/J68lXHH+1KKP+fUtbp/McXaZlbPO9/s6E/iK/UyiiNq9c+Sg2ddPVB0B1cyMv1+ros7QXKF7oXEJ28EdT1yvkudFjtlzoSyei9fBQY5NjU7u0msbj6QzeMCHQ/69wrYWGx2rezP7xqsVCLJ3uwNp5mTUATBM2Twz0bHtbiKuIU2t5gfnK0WVi+qc5vOst4nLVWyP5RvpLvkvtKz99v1K/Ar7jPH67UJvkoXrvGHP5EEuI0rHhPycJUKSXtXkvrz8CmOjNUBnSQGWpWOiTQy+aF92X2obSf2Xvvl03LAEOHdg8cj31UdTr9cv5NYajMCi8FsLXQb/ZbIME5q2gfHj3MYZl7nIAdgFy41DKOAfGX9RvrfpH7JfbpNUmwrCKECLg5/v8ltyZRrc5FPCZ+8bdhdP6fdpd7pf/e7DMFpdjuEe6pdyYN7nRahFftAR+aDD4JVrcao3lf1mfM6zRJWqLVQcLZR13vom16RjBTPzAXyavjZXn9LB9FolLv5m9pr7VlPKO6BR59Neev33Pcw5zx1z0ethtIoNOmR5NgLf6fTjT+k4imODj4UIRBdAsARnq5hGyW5JZiOkW50mX3JM/CeCvxcBkKItSfCgpsneGgbi3w+m3z5idtRHJSR+Er4bucuiBcTFz3OVveF/CQCt/t8rG7Z7/5EWRHMpYYi7BCqY8CFJ1mOqMwPELryjo8Fat4iBGt3JWDYHN4lLHSPWHgkUjTM6JSpvXuoDZeh9skd6bt0CzM6OcCaqVu6xdaEFP3u4l0ajKpcoJk4yGkmhl9lxYsa3nXG/X0etc+Ua+i7Lwt2+IHM554tTWTPl+micbJakRCVCKpE4xCMYcS6QyBcZwyE9WB0nrj5mCpR1gGeydwuy35A8oIe/c+Yq7YYbI0p6/yAL1dehkSEN2UdhUrrPXob50g/v7uptLY3FIuxIF3yfH6krqWouMWFKufiaKRxjRWi7qdhGECmrMhJhiiUb5fcbTWIjkTBeVDJQpE/4mlAOHkGIoGAty4xYvD2zWIOwfZxKN/nkc/nRtvPo9U5YKPFUjVaQM+Pk8L3d9MKvV0bPD0CglLqdr/TxpvV/M7uYwcCnR6AUIjSVCnS3t7nF583zw9o2hAOE1u1BrlqQV2KIKaHLwHdax6VpUWcATL6l7Nutgv6vbJyupPNtAUQ8J0m7dH7Faa/bo2G2Oltl9FCpUp+0TFUv1d7l+kNkWHsxnec6ztUpl0ixsSRRBZ+Jm8VW8ad2nsVS4WUlJ21Kj9iKB0ClGvpfbI29VV6Y2/nBuopUPcOIZ1FX9aX+/Bj5bbXBCHyzDTs1PSt2ALnbwKvwS5TxO5NdqFnuSRuQqBJav0bXQlBsx+C3rR2nHA9BliEhg26FQ0kD3swYvizvYKRJuiKIPxy3xG5BUNjvOENYXCvJj+lwrtZnUoZ2VxFlQ27cB7m+EoKsricmHzvwCHgyJ1jA3TV2xP7dFjia8Q8h2hyJ9xtiVqfQ3HhgW9F3pxp2I1CZwurmpF1hewoFwH6TCgQ/4ApDGfhAtjgHll0rjEKNcuMwM1Noz6MpPqtbmHrI0aeyMrMP+1K83Pzi454sDCU/A+dqeSz7Ik+a2mvu/6ereINM3n8joYeKXuZrHpJY3lFwdubZHHriYd5Zyqu4WWxrm9orXTS+IjC4r6SbLsUMfupStBMr4EwtLb13PWzWsN+B3IaaihP+mis+6tjiGifGrDjj4yTB37Q6mRkhM6xt4kOCXi92dEJAyuSB/ZPTp417NBkTTOLpqlntnrPwssBuh3U69dAWaUyUFUIaYClml+hgkpX1OcUD/29pSW8f5h8fEwRE923KmZYtf1DOF3ZfniYCQ+U+9HCEV6mdAU2ZtaXYs9p2RfJQmB8gvezvyaOLu/JhBYMogVRnUop3nTciFwDoXRBtLmiFm/KRbQ2KYm+m5Fk6sjj/eZ07MSi74uTtxbmhAiro+FdTl9rHIt8B3Pvzg2SJ9OCIgMEcLi/vxcotLE//biAyIn8S+q+/122Yu937WV0pMHorRuBZCye018bW2VDDMeAuKKRSMLH5zOUMGuyRm/UAWlwyLL7OAHHJVKQga+354q7co5AByviFPLQccfN7mePuwPfdKRISdk+aiwniTueFQ+rjhxa7fjDQAMy/2Jk/e3O3DnSld9NXFUPHK/rAnv30XMmTM66/ia2x73scNXmdYqvLUQGPq8w/VAiKjn9etI2OyVeGYtZoIRNx7AU4jxXHe6vhqd6W/XhAEAHbtRmBG9HCMHmTGVbF/gqEZhOEyUNRiFXSBy7F/RA3NKH3Bw5YHeON6oiYqbphWd4nJYtYt5Hy8nxPRPRaG29VbQOv6xyfEqxYwFOREi5EgYRkSBQ/Pv90A6UuOAZS6HynlKZuCKiv0oxqy5L623eJv5XVrySX31sQs0ofSJxwS6M/AXs3wd8vjp2HF12EWPrVr/wHrf9pO9RpzIRIYuxHtj3EROO6GHusDQck5Col4upX6Oa8LyaAEw0ZIQcUIR89F3aYZ60mDr2vo5LaEg9QVREgrzOS1SdjWuNxfbm06HuMNkLZyjiQw3MZwrkabIlLo2SNP3M38zYGBCdpl4fdkUOeOx0HcXCoU0VVTWtfu66I8WJB1WaPfu4fP015fyF9KMsPQSB6zKxSIOK1B5aa22Zi/c19gXvse8ykSL4JPOYyJ7e3kC48Yml378D7paWwb58VtdaXhCtyJ77DV1uUETIEcTeHUJTnyEjMii7uYN6PMOxBczLmNvxKIVmEuK5YHZkSLBB3pUhq9VAPqhHoQ3LRGQ31rn6bTS14rfew+tl//PbHfY82js0Ms6nH7yj7C0QjLXWaa2aa8EK/s3YupFehp+6tidJqOtkuIodxOsxQ9JPhI5NI0whjTeAsYWZuVP4y9uhc4IbQr/0vy/z6GoAycnfFzRrcraXLyUR+ZC/T6spLmd+Bzs1dWTKLeWCj/RaGzRB+l7qnEZESs6W590NVEUKogJfJyrBkPVFcL5YYc18IIsmDe2s76SPlJhTs6ZohNyjLspI/ZIESjvkjUT5IUi3DB17DDXMAZqyFYVw9Gb91kaaBknRyEX2gRGFRhMilOGgOw1k3K4+fQMpOFYfP2jItdter/usBae2MewP1nJY9ww7P1Aju/MXpjcbDK+4IDvFIIviT41GDZVxtjWZPvalJkOurAaWCPACzfbTqbgeVs77aZHxY6kIbXeUvLMNdk/CbHBJ73fKyeVrjeBDBFz7T2TocWy8RjoVYxbpUv+WJtTtCe/5eI3p1ULEY+gYgO2IwTHnl0q2boByU05Bv4N0Ny9d/YHaEMjUu+NJAUqkSntYuFCZUJa+60xAD1K/gjcMT++hHjfCwjvHvLWPQ+R0y+j6BhE8L+fM1o4zKr7wezNw64Bjpv12ld31eWbh50JbetqqsiN5bdFQKemTDoyM3N8Rx2W4Rarj7CPHr9VUI+1oly16V6cPlQnJhK3vnDJdwKs7ZL9S0E/GxwJ4e+2gxvFuYJ2D8Y1MrHzx01s1+d2ANQ0oiGlkNhBp/pMqlssqn9aIST9zIxfIXMXEnTR3t0OhcX6eYHtTt3wZAzfx3Xh0toEa+sHopVxibA6EVCne6ogiVG/Mk8yfZMDv99s0efJQfLrWFueJlRjW2rOci/CXIXjgW/WM5DdPbqvvxLx3KufvQgtQwGhzkOcvTnRJlzruQ53tVzuMZSnZANZNtvSPpb72J/l9qNQND79P5mz024A6EAPf7dw/VFkyhFq09DdSLYcK18Np3BAtfbSOt1+Pq1HY4TKSKLWFSm51xseieoVu3Ds9RHBGzRhiR/4WbL2/nXQPB/pp1qNeiRKT3ZDXQRqYF8KlrCkzP3bxO63cSLgXfPgYzZHEZANGUDgPdfu0TaI+dnxo3F53yNMXEMnvBKNathAfZuAZgL+xnZqqJcl42wJ+yAEzdNTMa5mv8dX8SPOASej3KO0rKPGaAPuxfjfcXOdMtVBtdpRYTZsui+2BB3hcilwP9fvlTJVQpKe1MNgzQzu+8/CceoYOgH/LCtTc7ySSb85oNPyrf8LuWsn27IprZxkdRcBjk32fbq5d6VFSvYLnCwSc+h95FREmtgOVPFm3Ce6oDJHWF+3isQnYTLItWHs+4CuZDi7jtgZFsEUvZbGYzQrDy08l7QLV8YfglqKkH89mS7bAIPpld824Z0/f+/N4U6fOJwjxKj90xISfg8CaL1frX9BeMzMLRz84PLh/e9gQp5xLf9bEVpRL2m6ZcKlTCrYxj7IY1pNHkKHoNsNni9G7lFF1bKuXfNQ4Cb30wYfgesf0cNDxHrr5ex+IJg6QscZErGryC417X8ySxxTILjGa9rhpoPQplVVvoydaei8wIk2Pq4dY0BbztSpq1AqzTsLUAzTYuYrE9y3RZMDQ0W5aez1iyDD7MHTDAGQgvwM34oyoMV57sdHV7RnExveGG+CRUX+LlTy5cTY0r8VDIXiRLpVcXyno4XaCJwu7d2HxXDw35mzCBhB4x5s1Bf028zRK6MrEy1SYGYI6KGyTUAzbax5CP/J7xWQhZK1QJCSTywmFCiSMb3syx+/sLKRpcfOufZqbsxs9QbkQ8zIKuYnh1R0iRJRnPXw0Ovym6ACIW/HTj0IoCxB0Q0z3s5F9ZyfEd+Tgo539o4kOjXM854ECzBZvYkFLGJAuVDXiYHb8KSSFzSDuIcAuO2mQaCJ7Ic7CsHAjhyTo3FkOI3YnwpPHCVkajzjDfWrTnBt2ysDfdiV1Z5+JAgECDyqs8fLeJcjobtvnQpuLh2111f5IcAailovhCOL7A2z0gi+cJrJBVwhvQ9vs3FrhYbp2sz4XqIf8+hVKoulCV/vUBdxt+xv5GLNmcrfM5euts7kP6P57u9MkH36jEzlHiBV78MURdb8H3mqxS9RCzHeRnyv4QyQtl+zTD5oT/u+d8pn++SFa1fqUgq+a6TD4mtSO6YJ7L55PenqIL0fXmbXGHMgA6r+5nyLaXy+aU5KPeoxF0qBH+vWXy78ll6CGi9StN1KV+zav0P77ycmQB8Dvevo1sw+1J6+oPYjuPuBUQ4xlneCi4Djdt4A8ulOXyQisjXa68+jYW2DbqxLNd8XdaRt7PMan7O9ktV6z7Vno5yQO2hHJ6CbvOu7acck5foR6sjMxKU40uvvbbztiXUnJrYV7Q/hwNS8JAxOOQzIE/e2RSFSFiUuWGixnX1JLhbcvr6jWF2AeeBsJ/SBuVt8k3fk20nmaA7x078CifqGb0jb8KF+64ilsZejSZpLZ0v3iII0dT2LTw/FpcVordyA70i5ljxcUbrVRKd4udUS/Zw+3UAmkhUJbaB18yffL+1JfAKFmpWixDD5tKJXgrjl0JXL1mtjRfOk/se0/ZNyN5g7pe2+nq7dSJYpYWjmn6sWvmedL6T1YSKjPpBwf+rAYnDifGy7gK8rUug7qsi9sF6moPC2a8Buq5Z370Tbq3uO9sVwTjkZ2+sj9QhFdjLW532xN5HIgP1v6oWlYXBN6dPUYUNNiaamBoMiFILa9ieh1RGbW6vdw1ltsai27K0Vy5GZ5fF3mjNHP++C6+ku/syHacUq90Cs9gWc7753+gsVNpk2D+pLrUbtfjOYhK7g7hSpDHvOsLTZSv08UnlHDeLE9WqDPqgNyDfK3hKdBt7djRuuEpgMmAb39RmBi4TbsM8f93OLrm5XXi/0zGY/5c8bG/TpLY+6zjCbsMmJrz2lkodvHMD5E9opRB+rV7OvuF1DzdYy7UqUtWN1iPFa3b3WHHCm1mQ0X/SCnn+Ky9Ttz9RPWOWSSMsONUGedP+lSqxK+fg8ol7pNfz0kUDOYANyVC09nIVY2UVHV9VJaqqmiJ759QdfW/XjDQaMzGcQd+9aS1JPxTfv1N4GCO7hoiz7aK5u+Pra6zLdNxg0qdNVM0C19LlCKlp8Ot58FPyR7IvnUP2RvThmNyxJvyQd/kJ7CttbUHwNgZ0NGNoi/cz+T3wO3wzDtDxZi6IYtpt3DdeeNCA3sQtySM+7cA1o4yMucYgtGyIYYIDF2+KXgxXINaecHE95keuOC3TKFyqEJ5qzWffDxCyfwyVJOw3yN8Ae7Ph94Px9+9lIbfEFX9D3Vzhf/7K/+ClFOsn05KTLkvvggEjtk2CwPoH5DIhfHGY2cm+x8lS408dVRc442fVnTFYeVOVEaEjmiL/5odgj7CTzafbRlv9qfaH9IU8/1aEQOSMvASM5w14wYsnVMetugHJeBglSGCx9IxXP3ETXiriOOCLJ0ZVLQWCIUyjAeDrT5IWPWFfXyDOQBXTw8GfI47+vfu6Jp0mQ1/ZxJJTgk/+iS3dsFiIgBjJ/Wc8SVPohFKa5RF++o+QyU1e/v36hyNujrgYfFqhIjyYdcapQdQgtZe9uLciYh0AiHbCklA5ye8hzFkJrbDzTahDa6oRn+KqjvckeBPFGwZzavMFHzaYEhooNksUcxly1r4ET30Z3XU7Pi2OP67dxhpnAoIaY/uezrAGr1DQgH2UmEeBPO7OiiukeO2W5vEOlCTO3b4Fyvgo+IAJ7WnOLhthgd9PQ5Ixus3pZF/E3Bt/A70ORTwa+hHjvSlZeA3RCdMFc9Pz2QMKhj5xZXe3njUq2zryq3+tE8crHW0Cz0lLL/HGfJF5WDuyjJD3Npv6QU7DCV4exrm6AOKELtkj4fP5CsXvGyv26TPcX+MuKw7/pUWBF7ODt/gObLLpVGbfCgkBnei6W41VdtcHPDlcp8hGwEm6qrMbq74V/F6Lp734bAn3RxfdqjjeZgdh1Y/2XA0Pc6TktU15MB1Zq+am1EcGRu4kZq0yHNvvfKmzvHDm+uOZCjCPbHiV+nAvodzDeXJiY9vIZi9nrPJz/LgcVUgHqtpM7fNcH97NTpU5n9mx6xpD/3LYWLvf5Kv3fOCyWE+/AZv2yKDMV1dUotvCzXXSr/+jrZEjNkL9epQUkr88kQe2gae+4GJ8Dl+e8eEMOvadNVsmIP7M3vjuHV3lMrns3Hjp/m9UIe82uIw5/K2dpnPfTd9x9mOuKj/KpTVqTWf2Pr1+KgkbbzJ+xmSc+2Eb3mXsliNdiJM5dbYH34FPdnQhfzeDNbU0UymNKzylxTaF+lWO8CSD0gXA6WjLjKlEErMCPjAQKkmPatXnrj/Hd3QU1TO3UMsCcjsd7SPr/8lAfhrNUN/ECp53yhr7PP80Z/RmU4REicg5cAF+32s1DDzx4nYOEMtp3Y0DnKQ63J4U2l8+fyZ51rC/IvR5aJIiIXeZqnXFlnWFs2R+T2R6raNxvoMgZyecrOfjfmJGnMezPESBpWpqPe/3VHU2E8I3bX19vq4laOq6tuz80WmtkGLfhAN2MYHPpyxauamqEi2UFBnForqm30MvwNFUkRhklCIQ/qtYq2lTG4TdpOPMe4dWiD9nT0F/p7mVpngCkd/ZjseaOR+bmGrdfSeSTQPkH5LPBjb74V/D6u9kTgudtTa3QQEXxXjZRcNPWhvMq7otlDBNEWVDkga3z5VrpDOTC4xPxqeAfFtdGcghDzwvjF+sU55DbyXvaa46w5dblNTZjtN5jFBcoAyIF3WX1p0QUqx89Of1DAPPTinELw7ziTFcNI0x4FhdrsKBjBYweBHJjXzP9Ow1iq1+Did/0qxDlUSOzSKDA2yzQ4yyxz3q3ysK/wj19YCxoJjrZ82HtqgFsRt1e34beGmLx0zr4eWxkbW/NQhNgXZAz2Y4gNnPZmR1raszQHSIorBEIaDxJUtyVZ5hMtf/lH0IzkK0iWn8GJoyjXcYJku+fCz8JoTxo5XvTt36K5ueCJkFRH6i8q4On8TCK51SgFb1uLKea3bqJNui+rp4E18ZgQPZAFQ1G3AIM4YiE4DHLyR87jx9/Rs2+wulLvYwFXQY9Qu83OMX/RgIrSOUx9nqxPsdaSSEHbj+iYfh3TH50Fje8KQPemUeGsjcScudcWfkvjY69fIlU+T2bk0RvIR7MsHyn6gXZN1ORYaLpfZ3BH/1SmWbo3eD/KmvN+n+m++zkXK3J7U5o6u6tp7QA/yheo4HWyhEG836U2aptnAzKTVQ+1JJFaVVyuF568++dit/AaFjdhzqn2nsMurC1ClZIAAjKcQFyytXzKycZzufC92j6zZgRgAs3sIFkfpYBNb5KZAMq4E+OsjapEK8Xbocv/ZH0jhhS7xkOwHh/ZE12xEKHJPvhpyMefUQUtaldmFbNP0SSPLnJxWdmQvWtsfmE2ymiNJWRfb/+gOZliyqDdDetiP9PMdzo/UWjtnZH0JBWHiIDAnbRUVUIHeKjWdBvHYqdcllP54RpcfURpJ5mOVy7uHs5SrShiCu8bhFPbl6TWDDlr3ymJIEg7xcv0VzsEzQAcdVvbD3ipLlRU8vPjrg9iznzP1iNRphUi4raNFZOSycJX9n+0wyX6Rq+CE3NYMrGMj1HfCqskzAHOPPiVPU4D71buwp4P0VmB8s9RizX53GGnM8oZM0LhChh0Of5cip+AB6uAxMBZ54ES6FFjM9BhWzYq+34et12BBgLLa9DYSW9GADMIjyTVzM5NI65It1hkY/n1RDV0lfRB7Yjai2/POdW+iMrw42vQePejer7ItETMDZMLp21q37gx/F6CT0yCqntaWWrfCQaPfH4u5qZFjLC+Y87/veP4Jx94WlHTz73Ku7qFpS5F85wrYsK5nS/AZVmGZN8iyWr4Lmr7YhJwDXXlMB85yWHSr5K2fCCruC/yXfWjaGzF+SqTUSh7EmX7vSux4JRp8Yg0QnRzxn1DaCmJq4naYE5RveM6J5ppVUu4FzUuquwLkaL2fdqPexrxhlKfkmDwNBWBUdHVoHo+WnG4WycdxFRna+wi9TcnPwn3KUnYHATmg1fAW1Tts7gWs8XeFz4wmlrdtqz0u7jjnZkbIIWJJ+yeumNsWA8qGWjjJceN9WNpLv7rl19slfbG6onJhN93Vy/30CjR2slnUShpEnlJy4TPW+B/385ELdIKNP6ofKjvRM+W/k4y+r7NE5gx4wMlSymCaU5axAYV5AJNyV+yVaMZihStL1HSyINdhcYLUcbTOu2nSh7iuJyCApk9ba3lIybf6O/ghUR5L11nxZlyt8hdDzPivhn/USWDliSW4WsIUgOqkH7EwYQ2mzP09yfmLyDbJX/fxsyJGT/lmRX0KpYb45nRNVM+z/b3A4zzu0l9VTAeFZWbeJcSXZwfIaYtZmUSCaPmRbXxd1/NmQHAoqn1+kJuoEp/TQPg+r6LctgdGdhS1iI9bSVLuku16/pB1dJ0y0mcvuAgtneqfmvZ1DNyac1PCClo3MFEUy7MFyDYE8sBk41/0o+UOlFEm4TxjXYXeKmTFS+OVks9fq5GrA8lfJqMfTo/L1fBUiO/tTSeE8bMLFE0msDBNRSJDRiftkyq+5TaCh4fCINZ92VpNpORS/JkLmhUxwTozF0mrEI7y/Kj5Jczc1W17OedPHD7CEzREv1zODAOEu4dVtrcW4SYqNvl2ed6aHNjsYI9NWFrQaLZFdob9lTcFJ8VtC5k+/y8EixBoOIu6jkBBttxuoy0huHvxCI63PoY52/FZ5xSjedKIRFcHABFIuY3llD11SJVHu2M10z5ummoZLXloR15+q3Z2oapyG7NdCaW0XBBWRG2dBKMLTp8+dOiHRTRE6XV8sat6iUYVMcZtlILZhuxzihZkJsZbv0RXa+ecm80wPABMQmi52BpoGxDrVdcOcqnVM1DOqdD/KKXMl4R1gmYvAw47xT97KgRMS0GQtzBp+nLds95d8zYlfg70V0SETpztKvRQyGzlIjwTijBbxyKyP1ia1bXCtr3KyEmMAaOTADA130ngOWoBHHfpM6fzYR2JuekdW6Emgkg+rZ08VOiIPkFP3qU4vEJZXwEU6R+S+gxd/K4HuwAiAjTU99vp/bl8KEDHk0MbG0EDjdbsg4R06xFVQ+73EjmasYrUSitLODOFheAD4nPnep5Pc23W6Ll9qdIn3YrCY0tGvfn6Z/gg7eV38WLNpKzcJH4+lgfCx3AMeOl3WewEV2pMNzxnNF8YM7lpe+hYXxnPYhl9h11nQLr1VGxW9AiybsKzyl4gIRIHGUIbFMivWde0DGUUvx9lqhbXnWexkBaoxmsGJmzNYjifCN2oLj7VOHPUP0t6RuNZcJKQFl4nR+UIOWtrIwVoPm+L72zoEK8JLO3AtvovWGDviIQB0UNFcmdAv2GSURItQijJaNJqUhUGqZMmkowFkF4tNPYDvoW7APUZ8Q+hHRqwy/HDiYK+H2Lif79e0nI8U2jGir+TUhz0Lj8JBGIItDbeS3dCggjUti1eWKOsxhGm7Qi5XgiuUavFqgN0qi7my8vfDyNL6FNcw97wqY1XMdFk9lQjJHaqDcRmBT5DF0C9rUXnj3Uh5hM4kKvietlGKvbEZS57hZf8PEyWu1w+HpHWjfxcoparGCH8Vu7w4a2XgkfmHd9/Rf7kWzpSfW6p8a3rqDruTWqyvoVxS2uBgYwmKWwlY8Df3e1M91rjd7cZKUXs4T4Y2jOKIubk4LfsaHDeGfpCSX/jqgbvnCKkc5oQef7kLqXw+K8vd5+zRllEULnUNmaMKd7a9qiO1Hjd+7KawMeIPscg7REI7AXL04BjuEx9tXsDZca+/oBpn5RBvvp6kqEGC7TeKuFOJqljs4QuW9jWhf5YlIKMGij7/awzAozS8st81wo/HyF/V0Qd9eaq1QdS4l1h0HG8Fim3QbfpZKqFogAxITMM8vYk/yiFFBa2Ccyy89Dn99HGj9epoGQDOi+Dr1AYvOWbgqea60tsPGfjq74hgOB+qdd7Yd55Z6EUsnNgJFmR3n3c+/pb/acS0YBxy1umj3GELnurJ/O8RMjKTsu0n8/gqyXyJQ/Zw0P34Y5mpFqQdVetFcXfi5U9EUKOTI3Oy2m2jVcZTrzvNskg54mVo4Ou5vNwQbusbMTHq4nfPpFOMSurdlPxE2nyBp9dVFMp3x9cnl80RLVC4yik7FG6Wh38NKxqLJa+sJlQA5f0Moelu+ZFOXfP+dJamo4RErhKsFRsl+FnWYM1S7MCRjWETTtdax3KYseSwGpd8u4wNK0H+qyfjXv4wrbX3yaqu9TFWdH+58EMqI+UGUWxsxTlGMLflCE4bn9K1bhF+jDm2QN+ZsR7buvUNJC6o6hrtb+6LlSNjZtSIbrcOnbTefx/TRh+HycDN8Vy+gtSeDCwuzsBjP6AiqF7azacePLJqy80nFrG3TxGqOScaHEO51blFGbDzFswwers+nWz0CrfqBUvWBjyRVAImRFi0zN8udsWkAZG/dKewUVIU4x9qo+qpruxX5lb7OnbRXqndH3CBNh/DkH9VW/TTddHZtLCVBEY4JdLPj2FTQLYawRZU5tmOmOmSRVFIOqXXFiI1B69tOAEsMAGrafD24WNpWNEYIYgMQ4gyKjE4A/XPX7qVFcgEYgh/yKgRFP29dOYzh13nCXwizpmZvIzQm7N7rK/f5RdN7aDQJRFPwgCnIqyTkjAerIOWe+3rhw42P7gHb33hkb66UOtEhaGex7g8QKZ4vG2BTczyEp0rkINuZGb99RBiVyoMyrNyS5YEKpzrpcvTp9US1L2QCIiuGYQfFuaS5vqUlvUEguBfoyawS0vfbd2C55D2Uxb5hWY4q93xsbt6pScR9tqJVf6Jw5V7qwpJxpLIgJp3tCaejMYXCdE7eV1i/CMAgcI5BOgtfxaidsT2gWG7xfe/IyIbOEzhd29VL480JfReS2I0+DfF7sMRcvqNtKU1yuyU83aMFAMMw2A6DQq3yB6WWrCX6kiFV+J9n1/8OMC8wMz+i7f387/qVi3O1cyYQ2sgE/rvEI6ScjA17OEZVVrFIJDSGs50+BrFrpfxyR8gZNhWLR3hj2YBytlfBqvD+NWzYvKdMPJksqM0Cy6xijEq0J+7io5whaNCNn7kr+xsjWWwg6z8q6a3/HktmtGYPWL9DFjYFfmZO+tMHlWRZ6OGpEx3OaSq2CyTWSBU+WC7W5q7PRFt+qwieuls2qSHcbBcEN0oh6YZAJyMCWeTXmjRrBzsFRt8TFrWB3JOdTmPLGZ/253egaSqVDxyY51ULpkzJanc+IvrByF/zJfqw2vxwSyXYKdPtjVjkGMkyIlQ32hdd1eLpiSQSUbPGFvQw8fxfCXzZnyiygcdkxz57JLCLzvjUY72emul/biWLvbLsMYY5oD7qQcR9Ft4w8rcQVvfcq4x4vB+vQZZ8F/+q85mXKtzrEm5sS3nLQ1ocl0EHBwfHjBZIHusQEkXKYLNVCjvgfhYwhiX4/pFs+QP3g6YdSA6TYNSxg3lzbN5kr/ELf2ltXP4bIPfMpSHxk+NEo0jV71Xcq3vpQn0UZMeN9s33tsJJqMfAsU3akrEKjdAN+WUY9FYMNaeyFg5L80OAYAh/wJEHhVRpwjmasLwSHQcr9VmX4BMxdj1z1x+9RLMEagd/PMANoynV0hQ35EUdVyNZ2kBrOwCXWxyBdcnug/AM4a3kME5LYF95AQQ6NKIbly0wu122B+6n8unTPQWzElgJReW2T2JEwdgC6SUIR+/8ZQanfLQpDKPJsPUL2bornhZIDV2ZwxJkL1+s8FAqTA5MJlCuER7+ArdO1B1eulrX3GpH9/QXuyMLwnQLwpnsgJz9f9rORu7CcqMwL6n8YrPL9vp83zmd+IqVDuQz1zu+pgdvSeDmRTYVNThtZ70bznrc+CyMJB1CLRS31fGmuGN/oszOFoqwPaSqek56EimG+9fvPJ8siPlqdSgk3s3y0RlZsQk5Ef6/s8txBcbCPmQxnkhUs4TYcSIm9hl2JOD5NYTLigf1YnfZvhktMqlyhpHHjM0ZEczQ77hvIL+zxkI1wuniY2V4Chf++Quz54wJvgyyHFfYaGHLHoiAM0F2KmjicFIYrtYVA43uAXqYYDAPI5zl94tFu/UiH/sLvNM0XH7uE96JUrspnlLW9XPDggsC3fTGlBbRFonok85Keq7Mq7Dmru7b3R4LdGA9X+io+hbWy/YzcNLoDH++bX9AP9p3P9KL7DRa1jWltaNhX13VurVka68opAEqFLIVjUJ9tLkmVfYmHQjYaAw+rPjfEonjR1aDCAjZqNF1sVvJm5Mk686YA7JfYrHCOURp8PGXyVJAdcyUCzL/EvP6A4AtPYk6dIZRe9CeWFFp3jdqs0LKOi6VpdCJHEf5eGn3YlrZs+sJec0b26oZGgo2yX5fjCwSK3XN8yapXfaPfUZ1Kd1LicvU7yuR+PnTmFc1N2Zdc+qJgjiBGUaCDQVSHS9CUYPioV015wQYWFQx6KZPanOpdIfLuG2VCWGauCqNiTfLZf17VRk8+Tmg3/Ao4W1xV5jyi3cldnGSqCHRVCv4YPj5F6oPVP+fcxJ/yegaGZQ5IcDHr0m+ZWgQrS3b6P7x1dicWDHjcQTFBL9pCeAPbPSb6R260O3DqXbx7KONHB9gMmZ/5iwWcq/TQqbFJduWlgh3U/ubasW1PctgrY+3PadSJEZD4+ows4ZMrGmGBI7f/EETCyPUTnOAjrpdY2VicHYNwgTrauY1RcSeWxQ2O8QzptzAAAu3z5aDAqUqOxvIzkAzT2dCWCsyXKTfJy8t8BfCQtyEi4b9Nv4I1WFFJ/Mh2y+pbkMHEpo5lJpD8r++4T9GY7078UVc6Jg6jT/eZ0CWjE77ruMYLlWVqFTH0fNpHp1nH3rgzdNqVMVF7bMLnh/HLRGiBB9YfybfBsBEkAGJttyPckXfOAoprDlHGyFemH6h9f+yKmD1soycjVxBQ5YoVRkktPOB+OBn+UnmlAOto24a6+PLZOdYJVhlcohSxDIsDJ6JZAaw4K6+4vTfMo3uZqfipaxnPyA27t3oBmn5vK7HKy8KXqStI+thjaEcYvmRHZXywNEtb0hzV521RPazq5M4uC65VaQ5Ukvk5xSXCScyYuUuKRVSI8tnSXX+utX8VV7rrs9L0N7Q6XuAVdWQC0XyXqZIl5bmnNjD/BomAgKmVysdZRYATnUHJuwH7ggXZkIo8vI4KOOBwjR3lmR+Ucxx9ZhaJk24sPc4O5E71ojwuBLsNfcCxOuw1U0H2K8qkXCcwzQoxjW2DmUFcKSG3rZOn64eYv2uTYnbKV+aFL1CZQunZqJCdh2PrHHZ1Glbk+ZqbP+dLMezPm8bitLWxhA3I4QSXCpSOYvCCbS7ifzLIV3mMoDFg6ggO8ibBj4leSATnC3B9ApfK6Ti6nKDh1P/57Yw1u9xXBIwnBkqoLKLzReOauWDnzT/mZcphsU8hwW8NW0qN4CiCqRwbP0vJZDfnC4MuowU4pBbhFXm/gj6CEjW8CqZvZ+jO5/Z1htasSezw8nhciDF43w0jWVKMXn4DERM3zb3nZ0+Z/D4cwZBqwujyKf6cdHNEHvDyvfONlfs6U85pcw3TWy48yUW1yWj1LBLY4Vj6cXU5cG7Eb+zvGwzDY8I/fWOno2Hx7hqLBXJb3FohLrIuSGALWZaRBBKYWp5LZU4H20rB0hHJi94UvgA50LZNL8SQUWlidpw55lPDgmUyru3BsoerkTBRUpBZceUd0bWFtn2REJucCWO/6PD+2K/K1p+CVW5mYbo3PitzpXt9ghZ62VLKg+7ywwtWFWqnj6S6BKZTrp4nz2bmjxuJxmkPMPuMAxOj4NL2YZvkn7HdLFR7Bv8IT0r9mHwP479P/q1HK3SaodDBHLS7Q/hN/JcKgMH3Uphbi3QMQkRlcAq4JxjoObo2bzAmeuJmv3r2EVGHEqHfZY1N/xYxqXqqpcm5GezCJgFHP46JbRebpPliOn3VT1+g1VjpBIEDLdjudmeLnE7ATti0Kvj9HKTJzfGwKblbsZlLsZboR9qxsO/aAB4GAvtSVsWDPpPcPbkU6RFWTIWoJNLuA9DyLduVeivY+qnNziI346Dl8O6u68oYw1EIHDXbB86dbLc97fWftpiuKEcJuaHxlrn0E0i7oUJs6sGta/mh4vH28RyRFRi1rTm4a8JL7tezi5vTkNAYc2muyxDSMtxFzzzLHT2zw84OY+rzVkChiBXagzYT27V5DEWuD0xI5UK8T9bWYkahR+jS4oXBHCiiFJUMJASeVrgdmofPyI+PlaE/YeIHYqTlVtjpf+xCxJ5JPUhBDXxJtIkJIlkCn6KBomZGGxB5vXbihZlboha+aOGXXbiPA7EVi/TVrmgQH87GDXVPId5HqZGjuswVDJCRJLALzwoFkNpg9gj6pi21XLKPVAGv8j+RTh/oldk82Xe91ToUqlK5UsOOdJT0hSFQTg6Hci1Qu6591wIKQNJNRZ5O4CzbG1KAf1WjO10afuPyYTbIs5BcWwUGX8wZD+qtvcbR2fa7qMVn33SZvDvxf67xhQbCpd0GLgdAsqfbUYbTw3z2Zqc+sHcdKehS0SudQhJDtJSp24jCsIGTT1iTNsCl/imD1QpDsv8NdNhNxvnE50FjQkZz8A/F89NUS7XlVjlj/M9HJVGzpuWIIwrXxCdnXkMVWZnvrn0VFpOKZkGEgDzHf/cgZHutbsdRHgjxhvpzDZ2pSMmIfsuiJ6hnNUOFilgbKd7Ix/xesGq0kVmaBkwSbEpPJBQP2uFGKObstGTfxFO+PXmHIU/5afeUr71qyAv98UUpDewLdB9NdvCvYoOkUToRFSfiiaiCxX6TLRHJZSWXNMBfgi1rEPG9D5MzoLD6p/+NPBOIad8Ejs+AsqpPjK1mbRTzxfNO+WCIMPYDJyJdmxwT6u1pFamciUp42XKwzdwpf4pbuzaa902uT1n60I8BGyVnRpBMhCuw3R7ohUnlWEwdYtgCOv6jwfpUgA1ezDlzMIcCi3xzuCfgrT9OVRYP/zz3AjHMCq8r8RFdT+Y+zt6096ValFVux6QUhFznqD4tVLUO3JLuAk87au/DHlMxLshYmgrGCnaf4WNiAlXwmzrp1gZdJcHnEfO1QAn3GhPQnSgFJXP1unSkI84a8jHCH9iPzx/MSsMy+lbuYaS4arSbKpz8GvSs/SaQUtrGLy/pu4yzkwgpT3M4lq926IS4+0A7ZAoTjHw+4icf7eaTk5HtYMAxsp0xvRjLZP1CH9jFoouAJRW+LCAfFjd95lAMopBQaIsXk67/SdqE00NoAR9/6egaA5sFFyZD7Kf81wMX8aVcscTFwb1EFdMHtv9V4psDWPdN/ddJ4E8wG+GGTVful3AaVo6RC8Wea+folmOkrik1tD98m6H9XglKjaeDzr2eDLoyX6S66lTJbtQb1QVHTUNHVjxitv0HhVfaaPPPlv60safjiZ5i/sVJ4vxiFRL/8MsHGHzOf15TKiZLdqw7vgwtfIDU088HcXYekGeeZCjliHfxpQHtbhR88b9vLNMMheNcke88Ae+qetXODzLZ39viNN9gT5OhneN9CE+OrekLI32EEzpfQcUQ2cwYyWYN6FwTZf5Y0aBeB5woiAP6fqeY6sX2fLzr1OuF2x9iIlxVo0gxn1Uo3/0vVAfiI0SzzL1yI5AZqehH6jQ4R+eKqaGRj4dXjgMRPfRFh90agLKZh7fyTCixS9lm5foFR6BWYve2VUgqh35SDG8QwF5X/bb5gk47oFDmaPfqPJ3Lo3zD+AO9cucmJZbB4Mybjb6shmjWwj1A4EryynMOEAdcZpULXjzUJHH3v8xsRIyRjjy2knQ3P5+HhSiDTVH+WX68IiqMkisui6UcdaKPmfmkMxTGcDkpINQmaypQWBsu58KaN745taETNylNc59z9eBoVI+vEcoKeWDO43K5Af1ak357z8WrsPXt2HeY+/kB+cenvthn8ctlHDwMBUCUJiukSgouNNjwBDIddxHm/U6xc2FmvJVZ3H9EZTg8jmPtRUVWC0/Y03tjAZ1+1s6D8gEzC53P4QlJExiTtUdcf8PwKriUg0fPOUHm5HQ+nMfVjASVTfbyr8ukhx3l6y3xuQ9PdU9+J++gpWYzUqP+jAjfMBWGmtJ9DBsoXkeUBUXdQmPoMU+qmguZ2Wsk2Bof/RTPnEnTLCsSBRhsj4wO5vuaJVrKYzW9lKv8y/jU7jnNzSWfECKZz9mf3FGraDhFIFH48Nw0GvJE0ranalL2P2uTASV0QEd+Ysv2z3G6Q85YhaAGY60pXd0rhaIXtHwIJil1jm4UIqC24RsYxJCCeDapSn3wq0Le2K93tY//iPQcNCIxx96V5jUDKme76fslHzi/N1acW8HjPmhx+abiFapVUUG86usYWd6Ap6hcA1DhFVP1gEii6oNKddOTfWvvuNMNGnPxs3PKErUU/pYrsZdSZh6TqWlPlv7Oo5ym7RE/uMB3noqT35I0L+LY2m3sreP/wWLDV8g8Jy+MMMzYanX2/vKc33cJeELLTdAme6MLVGiuEzrzsKYPJm/NuNlVTC7oxY/2jNv1XAO7sR2h2B38ZIGROQk/LKqOoPAV9qWOaMH2HB3kH8TXG1ovIzPhfCQdmixIWXtDTKueBHlW64dro7milNt7ynoYeJJapcrR6ICib7Y6ro+WrIUaAuVifVXY3wdF8MvzFQPOfRncSvzo6yFle8HlQwjyPNY+YtE2G/RUySGGBi31a2YjL8OaWc0DGckvYjtO8SnPX5ky7Qqd8PgJ0ZH4cmWm7wrTc97DG0QifOgxa7q2Yxs1LhBu0R/CuU2YObvdpc9LDjz7xg3C+MGVA1mE0+Im2l4XcPwIfGuoJd/A8pO5opOYOh8cW8dwL/6uQd1UEv3206CbxzkhDMI4ro7ojo9+rS1FF2ZoRh6VF5X0/NBQ6cNnd7/0AQ6S0ZwMqc8o+shnCwfOUMBjA08DYxqexmm5kqntBGy9p/5/kTONXwE+IJXPdaEe2FBEP5t/BZ+w4UmHkvoyzE39c7b8cQ7EmGx0rOGayTC4ufWqSA7JgEcLE6T9PIOFYVKTpOboRD9KQUpUESSB0MkJ4BlhC0bXo7vvESOCDdjzjA9FMPa/3gc4YrwIuqMgDvGQOY/SHei0wEvcNmGpvrdZsXIGgnBjuA6GERLbUxHZPBXyCFukzI8efdgd23izeJm6DgSWqMFQQIoGSgrrOGs0nYv5oQdae2EaDyM1kZEZkXr0hsK1hhQKEBFKkdPK7xeWVFqcCmlbtW81RbOzjApUKdpo6wqGPSSsDAxTUrClGxoBPQMxBUIHFXkr3mtJOoMHqOgWW2oGW8IPJz/Whjomh9vs/fly9RH9Gtq37E+YtOFk7CqqLzqdCWBj2fEmE36OslVF2P5qR3ppfxP2MB9nsW8o+urrY3Nt+jX5pATBV4kjzjsNIi8+GiHCza3bqd+NoTbe4tx71cFdX6Plau9SU4cPUG1jm9tvBcoD/Tmkman+yNH/3D244ZnUtqDcsAxMeJIiaI0BJXPWpqgJB14YVKRa1lIyL65D6S8n4OwyXKs2mRqzAyclqdsOdyqVa3yVlB8axqMNU8FlgJgfj5CtTAT58NRyypXr/rWgEB/c/4etpmp/DWky4IXeBlX0NFQAatS2W0BVFWaG8sOSjxNWxOS+UPYSP7oTI77zbcXzEaHVM+lm3f3k1CJufTZQgn480MwcMe/uqmyq+h39hrEWGmSGgHoFsxYhittHY5xZdNzLaCO4ly6dPuPPABvDASz5h2FeJTqWBXuq68PvlzEFc07yCDZe0faYaA0gcxHISqUWfAO7zHnRAuVYLs0mE5gm3P559h0En/zAvIKiEvwyvBMYP0bKZkPkmqVjgvLGsNENsvQA/YjSIYn1I0vHD6NnFAHWEgoYatxOxbYf7RcCRWp/LO84mwR7AfLACCiAh2pHEn56Q/4LXjXgHfysZd+FYEdxLYRrd4IM+MIH6p48/kggLmck0F4Dz74X/uyzHm1TUaImhvhWDfxcNczb+cdHId3c2ivpQ///ptVKkTMLzVV3bLjaHP6A4bjBsJVq575R0KDd7buRZeff8LX6gJOFec6VYSAZwA4L2arlIxZMmcuzzhtsBlLPEPrRz3KeK4JpE42Tq6N2eLK5U9z9VNAYz0DGtJE4j8ScVPD3M5zqZ/FcrFXB9poyOWfZ1V4shIUkxtXauEi1HrcyNFXmOSjPWBVGBBimjEEtTuE6cu0mQXDKEdw9Wdkdp1trbXM4+cu/FQnuiNfW3LOGi8OgnZDTYTrnuZL/JG4c+HFmWlESQzWnRg0AbuNjqI0OaWmCssDvYPNB2lAqEpk9jxauCdlgHU5KJEvKfJMaWuVH4+H2pA8rFwy2UFzzGskMsZmP4hrpjbHM25NwmjJx0ZXK11ahFT65TwT2tGVcfnXJY77dl0fCDrx5q6tGL2tfGAWlimIoLad39kX6k6pd5M1yv9bvwivwGUz57sGa4rn07p4f+bVtWaYAecWm3LPg2ZX1lstz6JJ78REPIRunpYiN7XUSYiXb1yc3i5CRayPyEUGAEPN1QB7Ynbi/ZwF76fcZ6rLNfuxY3qI4EXYwgYT9Fj7RvfeTUeT3dhKICkC/U+8vVo7fLafz4OeyFkCCFCndDdLhvPWzV1FMZ1oOLwwc8tmPrAbOznm6CYV6SuNOOUAwtB99AtgunmfGTT8HUcc0DiOB8AI0wYRMm2EVfzQurMTfTJvLytk7TklLU5FW0A/VKOkR8fgc4abQDJ+Z4fZxihdOYm/dVkDaJBLZL7SqltUU/Gmh7oDZGSfA73ixcRafcTZr3U01aWj6MkEIPxuzXZaBXcx9i/XH/77FVb3gSPTaB5lsgUsLTNRryxCsy9xgOTqOmreL3FzzubtX8gDahkca4XdXZbbP09eewToq3wNZT/qPwcxElxlVEd9KfpO9RNZaYB4UYxY5q0cCgOoW5W2OGc/EAySppmmYegZDBU4OAGN36MBO58laXjuCO49jowIMUP0u7d4qqrBQ87NbcNeE2lExiy3ZfGZqScDrUzSpsk5gQVhJX/FANOogcK4AY1BeUUZgAjDrVSgNN+ClCDbn8oCc6jaY1NCjVJAjyYaZEe9N8ZgfEzVLgL9ck+v5OBm+XNyLPllcJ2xQaBETk0RzHC+SE6TSeaUDRsatEptaTXfmZduS6UnRDMFbvrUFniPbBO3agzZLh42jt+BT7kzuErWZoYNpEKiVB7SBBwxCDlocZlGTDtjYDrvEOtH9cI9RSI5NGWBDMbBlYSGUC0ZxIsEbN9pq2n63Q/2rGao8YNmlv/pgywyZQkakNzBGX6A8ytEri4NM1jxXfO7loO1BLNRmprcC5mXg4TbSwzN0lXmRWqzeMVePE4ew8740IbuGU8uHghtoj0pJVLFp/uhhqSEDzaOMsCkE/zjgTV7RAlGXyvL9DeqhwkNizyocuDBMloUC2F2IvQIZWuVS8BTlDwAwmIvlBwQSgwXRyrBDikJIq3Z9iqcxZoRYvxxAQCiu28TZmaN4+4wxi+r0LcxZL3SHD31r5PE6zBtCdsPWJcfZ0kqbYmfAbmHtzQR5Deh/lOPlFHCUem+hc23WaVHg+mi0ASwAs56eRT9itdAZ0KVyyDbbbx6vcv5w3vPqaT/wFkh8Q5k4ONeAi5ha33FfxDH6tRBfL3znx8KiTndGBt/NDyK+X2b9TVy6o+xud1DK/4YHOnBOJmf96UBK8rvfF07lUCDt4YY3PNgl7mJefX1xii8HWvV/lWkTSRPeXxLSAJH48rKnN1ubJUW/OV0Z0ixlgG8knuqRyijtFLdQvov70jSfg1UWSHhtozW4il1PA+FS9wQVHsOx6Mn9Wop4GIx+FNRqfVrpsvV3C7qQt54ADXz0wqhzD5es9cKNrcZAgzd+SHypVUTliz4keIVG+y2CA6IwNX5GNvMDVbA6vqTsxONNfh+ByrXcubdIxkzxtPloO6RfVqiHEscPQtSDavkLdraVp+QWlCx3dvFp4Ivv2o6AjyMEFFHKOtICMBjHUuYSmjd6JV2mGSS4zyhF/3MEiC/0hCyaykfUV+FGX65SHE2Amu5GEsBtSZ5IoFIwAsTQjC8THAWiZaFPXGFIZtcaeVrqxR0VyRmbPFSJ/PVWN+04zGXcUmGmj5vl9HBqAZwgoHGtfUddTMH0ONCDFdOEPWVYvuoYukK7PKYmGPCRQfqcvtCdkXSV8TewJdDqikB1YsjhPO/2CTc5JLaAV/aI5ShZo4Z8kpR8IX7r8M1/FSOGz0O+rkDO4ZljyTztSKbuIEZj/A8olKMQ3Vb8wuMwI/KD19YqvItQ+nRmDW5VmWTNnhTYJTdqQ01z466CPgpw9VI8xpvv+k+CEN2WS4Z7tO0I4y2CdB/WpkE26V4bC8gvqLMG66Idk9T1m4SRjE6OHaaUNW80MC0HlTuF7YFeNar9wKfAgLycQ4RpKeqKRDDHPSqeSE8wkSGOThmfCAAMABdUWxFKp+70Mk1RE5jFwta0SjP72ADy+DAzctH8qj2kPIWSMi5qEa1T/DdlqO1YHMkqF/M15+KtaJAOSZMPH+yglB0dz4tJJQsQr9Pe8l9qpTLDaomhGcf/k/C4bwfRarjdMRNco+czCI4gSIAgfoAAitCiDAwfEaO3ylMzTFFCHtUT1J9hOrQOS/tBISh6Ew9SCGxS8wSeF29riAE4lVLgXKaSfSzObXJ8B+5dIiI+W8r4eRG3N9BhLN4Z/4/8Y6QvxeAjfe8R3lHV5jFV5RW4hN77+Frx1h8PRS54QhOU7UQN1WRsNIvyPDgSWh6/9YtV0jD7MKCeb0GzzoumQ7JD9sVDhoKqpIEh2VXhqC13CMZG6pUdy8CI1w6K/CiAutldlhQeInv2vs3LK0caCAf+/22ZCd0w4b0fTKWNmBEiOpNGH6bcUr3bcDtmKAJDmFVvvtACu47IF3C+R01X5dEPXWbCmB7nfkhQ6KiBK56Nq6g3KScm0+PEkOft5nt9vpLt2ZHSsGsAI6xBVeb4/RNjWIk2ZZJHSrg7GjgHWAqQK/BAH2AQEcIFPG6HqjcJ8m7CwqcKNRdblyxBDZGKt12ovzhPsL1UQTB7zwjU8K6HPJQ10fwFgX08lGGz/46Sdyfg4Cf2EjJfbjM0YFhcwnyeWevInhYLKGJQKN+VQSnhpHeIbLxdK9oUjETkB1dAIeSzFYNQKzcVRswn830MeZlAWrq+WKdy7f9ggY8FVDJnkV6WzueBd5lI3mKfV5pVSdnlEmv+VRHRx4wFVe2D/YJCoFiaaLlQXTDN7FqRcifiSMtZMWtggR1TeJh6mCAk1i4/Jykc/Sny9bA8Ul8kHUM1FJ0+YeU3swnZAGp2ywfgPxC+ITfGoA+1wphRpj/9Kemi4HN7TLbeLiilKdsp6nA65K4DLXTarUS9l/SgHk7DIT8G3gMC32muS2uijEMJj3xmRQY+2hMa+unwY6l+M3wGp4RRt6cA1KGM+tETU7R30EOcPGXQptRWT7FFl2NNqtj2gB/ZGQsO73AxvFu6CHQ8zMJHCd/yHXE4f2yYmjawcFCT/vwWNyOU3N1I/j7342GQhDtc88dwGQ/QqaBDb6rsjI1GQEktthIMNal9ZSJ+Vvr89oRNhMTwyhmM5rWnA6c5pxRqrUGnfLpwln7N/2Nin54WruLkHZOPsXeBnlkyNEgobRdkWpaZmb38bJCpOQtePcsoKgRoIjysWUZeRRIFqd9P9N70xR9vyCCh2YSBSDglNjThuYMnSaPHRl8/ayfTFWJDx4b6iBjf4JFfxrE3jsAQ/WSPQw9ci2BQ6YU6kpZP3oKoR53CepVcOYFAXkfpe+xNTikUacGpMAEx7ikZzhDAev6QDzUanfV9zUcD3hxxi4d23S9rY8bgjx/EArU+XIXE5AU2t5TDN4KgpaTci0AhxpXEm2LnMzCwFsqxZIIuhIKlGUKQdnVP2ae9CBKW0AvV5fDS6AoqHYrHUA3WUCIdibHltDfNC1MVJcSOJKU0uWSOie7SXdZn1wIIvxrqaRHA/9SLdvYOm6TSTB3JljBYKc31Tia2ArWAmcQej1wYSbq9BHqlx0W5j9xpxTZhV3hPbUtHG3WMv90Msw7NTRHwBojYMQZLqvOGjtkBAI8CY/mDUcw3As911ZQYlKjZzH5SZLzyAmJlTWTRig64nManuO4nowamKkAvdpHJOvkOSTUGG9fB/i4b8cGERS4pfffRQ0pu/xCSDm+9RxW/+mfL1VDjW4ASCRAliPE+s+GgYRadwQgDCnWfMcC7Ges6rZVk2IuH78HJ9t+70i3aLoP7Xtre/v9zF1/JvwKDTIRK4LV+9Rnejt+zIvfwoxjPmbfjyagrhX4kwe/IraphslHLJbwEQJQZ+YWow5c3UM4gXQbSCaxMHVipddFSLa7n8haiRfs0xo8mA9DtPYBxPoHyCaler67LeDmAiv8fDeMcdbCb4SunuFJ3jzCKGFjZH6QPR70YzegIt6MlLv5tnor0EzdvWGuSD0/FkfPa9/vkGkiWragGhMrMD/FN9d7ir7wrX0G73tce6xDWSbpYS0M+hCbPbFrXssu3G0D2MRmLha228KS6VAJQoSiUJlR0aQqKm2uSL51zL3wAINILfXORXPkihPR77yIVqQVyI7eaOl2Hgza2CjRnw33ZSGaYwThGJgFHUdRkaOhnSY4rf9XqizKtH1P8VwlmVFQGh8i/xHbRVi+PREWvIpXeS7U2HuHBs7QomzzMSs6iNtexLtS6Rhk5EIFdhiLZ+Q/hqsyraV1lgaaYY77NCoPfW0bOQNLEgYbCL6SwSsjpAIxfutWh1mw+2E0nPfmqt5yYox3jyoNIS2tiYrbZGRA8NpIdZ5Z54gJzL3LWHh7jxB39hA6UL5CVsIifwTgSE4TzZud7aL9DKxcfmSz0nGFpgogV2WAV63axPITeFKOKvjRwC13xW5jLIbv1u4EBF335IPxCaD7aNNaQ3RsMr2UeqXcvJHLHr4JlLg8UXsYKt5V93Xj55E4jyTHW5c7s71zl5b+BwjuH3NN527nGTV+grBBMSpJryo7ycxbWpVCEiQ40rr1mkw5hbjSTsviYpyqLWYnm9zjz2aNm/fM6V4GOj8fkYveijsLhLpg2oFVoL7LXqDw1bH/Xx2MwCRN8jjaegzIpci9nPvt5VShgFo8qc1sGAvlQL20Jv4xRzCKls1WifSrtA8yo23/IEmoMg/qkS4xWRT8KvZF2n1rk1/PZTukS4TN6DQuCTfbxIlrfLYmy626xf8/+1jMGH5vfJfgPDm4OaoCzJazZniiMtGf/loZNWMYivCqT2kmAm/HaHUJAHwPhSzPI0DXl0h0k2j/PBH1WrtMQIYQ2hwQ1x204li4RD+EzJbvoUYUsYQMJsrG0ZIA+H4GewNhND4vmTR6jfhZsQDViG+2bEnGPEWOPB9ZlyvKNlVax6BVgIHISpQQAje+r+CwY59tAezakyFVw7qMqer+eyKCU3ENJGnItYKlGbRo/+2n7GIOkiR79giYYvP1MEl8ZURRqjfiE0iNRQicjrtevAuGjd4uJy71tAKviD150c5NEEzFzRZbw5eL8j1T6CnwhZiug4li8pzm5SwrYWcpGbct78M7jGtc5BdlNpQt8y7U9YHsSlY5qZdzZ64UXPJe7766Zt4hCLiBfp/A8Zq6A0+ReyMg9lsGiJORmIDpjdvX2cKBAU0pMVQZ8//o1je3FeviIJYc/dzasRZbZABu1M9GVlxZL1EtiX1zYWsfmhkgGv8DptTVpSMmlaFUtR/kEmzM7OaUOJzUMG+SbQwkJoa2sHviUpAl2RhcNT+6vwAXb3xYB0PFVsZrgsQvzeDCDLsylQ9nKNq2NdS+OtB6/5LoCLd/QZWrzPRIGCC++rL7ZpSu0MT7+cLPkeT8ezJVtAq+WJeCnIXbJ65erfBvYCgFYuX0BBk5mRjb95joCfI/Ry7MWdNSF6EEi8EvmHE3AXsVy0ij5PTwV7KooHecD5tCxh61rbQL2FPU1kG9VEcnBXot/YEWXX/LR/iXRpr7w1CXYxXCyx5w19rzECxbHr7ZOn8JNGByh+5dDMbv7l9wWGQiG3wu1+fAEkD7P8peYI0/p6sIoNkoKyJUMFsqph4LNs6jeXJvTUbQ70l7YDYyxw2tQYML1xHP1ee6TUerMNKnG7Wx0/dyYyCXW6Lh8ZaoJLjp5xjnE5IuEYrmBqII12uvDIkwxtqrv/dnbIAp1oTYiN/kw2BUcYX7V2OjZgvSsy1NamT/s5gvvSgbVgPO2url8sPwXhbNSAt9prhsWGhG0g1v+l/cgpuIOIGNRJA/oxqasGgm1nmusGZcltaNpTZfcb5WEQuMkTVVF1aIu2XKT37fQ3T4tdz1SHcZaUfyY7QiYV01mwBfske9ZD7Gezk2IWmLip9GOB6ve5aTACtzKdoNoceHiP1D8UW3fI24RMAliW5XyUCJKMwUZ1p6P9C0oT81x8Qc6Yc8cBrnLCUfwyPSd9uPyPS/0XqPaIUv15TqPof93fWKjdl/GWY/3UOnylTy6JnqI10vlK97ec3cOgmtTHjYvblIz385uO3URb1WvVKifSYv8fKi99waMDmqtDXEnuOlay+tUBk08Cb82TyC7pM7PSWlGY+CedmUtG/naZw5THAVGjdlwxqbsR5NHNLaX5YdyT9s9rk7L8Q51/Un9UN4/llhR8dTcaSZL2kRn3eWoVLuEcMLNMej3hjzUoI6JbIX0CWJvRZjdsDEifDVt6ysDHh6vWbHhyD/rsSkB/CWkZSQbQ6c+YYyU1idIvFoUYWCJD34EzibEDvJM4dgZPxT8br5gO19Y3rvZ1nMPMFxg9h4HjfWXy3fDDIMWZQmTn+9BNgffDWT924WOJKI8f62FFBrPwknYkc8Nn4vfXtjeiyQ/17VSvF5ZMcuXOxTGFRodXYda3dFNxjV24jiT/LsEADLlsYD0PMZrPt1Prs487mFzqQe6t/AD3GPd4Oj5bS663XrXfx6QnSHjSyS4XKpi1BbRvUS4tck9k493gE4zGpRmMhKv5P4UT95XXxoTmmUKpjxzMEo6gs+dU9PQ+OgTU3AKzl69Hm2QEijct2CRO0j4YDjdkRnCalFbyCfdkh9OSLZpEwsRWwR/qtnwn6g8Rewsiov+OCy+COxhZXXIBWgUR6/D05OZfs3x6Qx96QQ5WxhL2GXFySDTBXqk4fp2OXJDSxpaLN1gCtdiGNeAPFcyk4mM29sGwPqtT/Qfe626vEdyeYzIx/Qh30N6M9fT/oZb7ovzL+Pd2+hCubq223vdnypNgvMoBVINJiAfiY1OfskYBBUoBsFt///HNHNDsmR3q8/BZU4M7LfW5VHt9Hd/ihmeePPmdtw3qvHHFDN4AMroGT2E4kEthjHi92MPQ9Xj16dFMBfvAX31VsbP5ksccsTfAAAYkQHKYLV0AU4yg3vgy2xS0mLBu5FylKOEtO4o2Y6yJCFO15wi0ghZuI3MKCGqUOCDu4KeMNuvWAfXXVP8hqYjwuUbu2GpWZELcrbkIO59NIR4G+rewWb3FDHxvdQs/SFFm0JaosHFQjZTk71bFbEmUPjOd4Ys8neNwvLZg/T4VZ/xqOPH0OF7mtUTHM11iJdOoVAM4hevArcctxavOPCN+wSli08WQiEsLYJAQUF4k59fYvZYe2Xp/btyhbulrBn8AqQkigpDL9SJekOJ7ubtezJ7s4a02zLbnX5be5U2fqGuLqDV4/D11TIRmgkVPskdubblk0Id3plx4pyIOL1rT53QQqiD1EDfWIuOJw240/BlrL+5AaJCN68XTobLvt3zJmqDkdBA1LuAgBEzziMA6QlLIeFB4Qfu/HqQ300SuzPXlnHXXYlCW9R2A/+WY0Pk8rNASHVk7VKHGrlkKWX41pMp33RfMrrWHbOoc8Kr5/MQZezg5md4obV9CjH39Eb09QDtRmsDm7toxWSbkWBDaxgTe+v7S/VnLXkMWDIUO2DzkbXc4WEgmqPe74sMOKPfUv3o4lmSfYUDhwo+jXS3VtH9mPiJnjlNHRLZNc/ZWmdQAhnansu0xeYThJ8CXNOuBDZ197nmRpll5nP6g2AzKP9KXe24RpmiUd3033ryjdObTIoP7RdznmzFJeqn/R4u+4Esuv5wi5FwkRfHfhcldiv0Ck7lSaSsTaCRIVcGqHGnrhwfWCCt/1nEz8gdMURGvQQH/ESrEgfegbfm3M2XDVE0dso4gDkvXmgUfiADHtnKa73VY4KJ82XyctNPJULJuRBA2cGx08gWDGsmBL/V01d+prHsIxNjaPwFUSoNqBsSVptwNE0E9MK8v0qKRfJ5vSuo3TH768uwKt98LtQtC06D2vp9B6Puh1AfEAYRdHbINMAnAUeLEJaWqWmxTX1DlrGZ/yfSYs9lWniS1lYo+8li1qKBTZxQjuxTJVZBDp2NFiKYlb9s++hWgrywLkB9nHnYbRLa9yRU6xBkTDxEjkAYsB8OIPQokE9hCqKeMF6tlA5+vyEkbEL1AwDQP9TtFcAq+T+IkUc5D2jwt25hFS/0AwEhf184KKAQdqyAdLuAdU9EQB9yxoNwCv528x4NIMN+YVHzydh/v4d4cE9eoMwPq/atjR/nOHz6pSCaVMIO+NaDtwu2xloaqfwAz0Nr9QV2JXZQ0gXISD78tjjsTJk8I2XQOwQiiS7eK+q+QJz/YHTNRlqRNw5opbv84ZgfX+Ql0eSCthjtEmj3M4200R42lUqrXyzK/JGf2gccWy5iODNra2kQ79PLh+riiYELLhFOdMjlV1HKgK2tkYgOTI4u/I9q7DZc3ObpIHN/lUAkrheaoWqx7PzyK5xcbBajkeqIOVyHIUwuFne1MUWSfhedFXyR6m/yYyr1DKmgE/G05OQDDQ06skYS6JNq4QhkrSGCCSyNKc//X6J+34jNDe/Ir7x2c9F2p+GAYQV4MTk46AGMWhp6/Qzk2qeyl2srE2vM2+gK+8uyN2s/WJpdCXJNSSr2q59lO2jF2IqM4TQyQWBDapuQJS+LhpgqChTN0La/yGD/ai+jijlo/VbCeQQTWLIrvVfpi61gcjNTp27Ghxgu+wQYWio8sPkGK5cHJSQjDVhHMXrJ5pgUA5mm9QNEOaDRCvA9ykwkv7KeESDtHFaaMLU0xAqJGaj5xi5mHYSkFYFCYWt6mjFNIRLd8Va9wTO+J83zESEUiKwD7B/AxMVNb6RXJ/UOdSBoBFR1xMkIRvfIpIsNbvRXBn/0TNMNlYtZVjvHItTvByz3ewelv/1OqRSgULvA+90c35RshBLNzPgEsDI/JpO23SaxFxiLf2/IqwEyvtRJx0bRUDsRpcCPXsoBsmIbdTsfmuzv/kqNTSm/F2IocIlCA45VHyt+ouWEIZ8+JGz96DNqfMGWUqDvCTXb2uLzYmRBsRsfYxXM2uCVb/z3hzYHZk5bi0DurS7S8FD3fUJUAREfB5yY955PyF81FQS/88RlbjHhhReARPZMR+DGcYr8vvu9kTcdj8hWD/Te0Hhek/rXZPEHe/Em7rZsg9A9nuDvsS0gpC5kIsdUcD7S9CB2DlL8qV/AA3Ih00vnMc1HOmzHOZFpEkrMke17Zj7EY3wnuk81aS4uhNmWhd6Ext4/qk+8t+yLINUjtxqzNtJb6f+7UQ55ROdzgZrbUCx8kXWorTbzG4RoXwezzY4baFDhAe8Tk6eyo+GbHr203UiFQhC8IhJ2/ZSL8iunMNolLVHtRrZM39Zj9cB2EVCDyP6Cqd5OWQtf7iRrfKjRu0sGUX4Yvy2BiFbAn+nR0PGRxNTFtaUiqxz7MZm7XBP/W7O8QqcwdAPAPvPbJWAVJBVJ7Jun+X9saUzgoD78P47OY0FVIAqiH9QLclqKZMkgaUeUnPPXP+bNdkbF7rpVdUaERzErnBIxejtMnojdWDYlsRAN+NZnY9BGStaOkEa/EveXu4JiLxew05YxUj4zYmueA/Jz0lefAF57qJzybwbjuhQBMss/VMzFMXB32YN/fegZEwo9hzrfwJj0ZzBm2rkxYBPWxZx7/pMpUftBLvtkda3iomJ2AbEncUaC74Ce0uj/ONQvgIms71myff63jjnGsIn/Ipi2JMn2MdPhKQHKU9bX9xOoJDFrNL0f1Xkrz9JQnUYWC4mmjg6JPl+jSHESvPE0LZuQHj5C0Gp3YnoHH5xRUcafYVI+XOWQ4AXsyweTi4okGC9gY72zzMJNFAizg1HQd4TRPucap3Q1mrqkjGhqZjxOsqB7vUg56D+C98vjOCcwr1CUbH4b5GiY2nu61YZC4sAXinKWdz0WygHbd/C96iy6vFe+B1gRphFhL4tFKWdKjcx8u/kD8lxTQcEVg5AYcpoY3Nq6Tc0eTVK+1GFZZ/2NHtQXRpFvYk+LCKMdSowijaTUu18U6qegSV5QcjyRiUezTL95kh7X7ut+snl9MMM3NIFO6iVP5I1EGILi7ILk3CO0ubVh7hMrfqk1km8ztqn4KRO7rs91UI7Ul6XtNH6gBId7fDc5vzhMBfIqhfp0KEXl3JZLEQ3V4GLfkKlYg9cgywtD+t3SdkkhukgkwIaY2dmjG5cT5a+YoRMuP1DzAQWha5CJ98H9QcHyRiZPx/CgR/Y6whxRpYoapVS9LES7du2YSas8BY89tFVffmgl/bWURObEbBRW7jSa8yxwldAqjesbms4u9tAeQ/E/9074Hm4x+s1c8xrcJPH2WvpCUvLNsbUjgWo4zVW5X8uR5fXIqDQz9tf8S6K3mb2h1afh3uyN/9cYuT8Au83cwtpgCQ8EnykBlT3MMk23AMq9AE4G21WYOeMnC0AJWlj8i6dy2t2M5d1dsU5MzU5aKbF1GA0qxjnI35u4hvyZqiUFDUq1cxCFyk0lu0g3DQQbicr1lcsM1UaBMxl31EpfpmXWRfDIVM3fyFMBHiX11RZ1ICyaQN8IkUK1SEg2DLjF74sAZSSpbGyAY4crd/s3ngBdbKM5UULq5PJcIc+drM1oSyYrs3yHpGyI7a8x+xr7J29OIoffGR+SXPYYznZyXb3SnzHT0DoJ5607+sulawkZx3A7Lzgwk0hkfKtgssXquuWhtllpmWSoTb9Lg7tpFmxOtFVAdJaS/Wx39o85MdZMrLZJBXtTFhyeuJnKOZJ+oI8ghI3oWewTJro7iPtrxHthJqIVKpj+YawJx12qullbBG4fVURt6vJ7fbvg1S6GV5wqZJQr0DmaLKku0FcNQYPUpPtV0oUnzvbOG/Q+k1XwolAHAykVHxMY8F/d1hUyo0K/UFJK/qC3ntPdjVQ9Mu7tnFwzyenP+D1c5H3WN4lxJUNIemH0NuoYWQP9QnCwBuRKa0uk+OsBhAfxsHT0jRz3zNuTZvocQlrcP71qdkvaPH34yBm2Xz1eBTBNSAWu7W6H4fVe5kVVnEv7GLTp9n9fZ0iR6p5uOIP1lpv5XDeYO4HTwZeanGalmTwU4Lp7c4mEJ0Uy7UI2+PbE3v8okeG+rbf4U+YnONpvT8L83ZUx4gUpJknqtM17UVydNeuFqgLqTQk2rYbsHh2GwpzqSzknjNMyA9vaCRolOGVKgMHGultcMHR3fbtOATkFZjM5qpB7nkh+pjFw0U5uPTT3FzWrPKGtXEeobRR650V71CXx9KEUjchIT08iWTjImIGVGIibSyGGtuSuLuPSYcpUdwE9D10XIfEMAMd1bMY0EEJkD7/x1OxVpgN+MSTRuR+vhWmEY5EoxS2fqZhU58+8rw4LTouE4JvcX6TrxCSsGk96NHG9gzA87OTUgKIXYkIvJ/LKFslE3fMyBZYG6bKh3+Aw3ZFNvhrd07iH2ljtcnRA41CejVYvAi5W7L1hgyFiVDs6rywhuGEHctbDCL6iPwMq71pt1wcHInMVd22mHr+Xg6kXCie9PsWXn+mELPIqvK05JnMc4/flGtQ1xX2TJALG2d+S/5Ma4wMrxAcLC3AWKwi0xsIQvnJpkhLwYDARr4SxJ+4OI4t+AXTBTpwib4LVcaX3Bjn3fHGE4txj4PiwXDJgyhsoTGsqbhGX92uSN2+qVHR9tOzNdJrKZv4B5Yca/RjzDk84HRfG0Mqs1gjhbiNVIfpr7938VIwJLmAHGhVN8jKcekrAdhc+XZrYL3qWit8dTIwPfw734aZRqWBUUrKvK8AvdKOzmFb3RNga91zlrXox5BLA1n7VOLu1Qb2kJ7uWNuudErO0u4z2Um7IdRyRp/SYb+TOsA4z7J1mzysVx25RuZR87GB/G6+/dYXVvZwO9K7EPQETEgXrehZxXPUNieCumQNdpj47Cy4NEHbwiN0yqKpYfoudMxu3J23bZBfySMVcoDAYVvcdFGmv519mStjFwu7Hz9SZ88NiSFRzufVKfP66cCPZjJRiKWlURYhGl1Q5KMoG0/vGA5aWkPLnPrYX+YGjfmPWSZ1d4NxzJ/ut2+BU7JlandfOL78LgRuZxMYZplI1lnTQrOThNnsSmMLNIdrtLpWuDCsLV0VzhSEE4y7CZl6k4srT6oEPkzHTMc/3Xtsrzkog5sx00jcGjId2jqkDSv4Gne1Gabn/XeEFUkSbJ7vtOjnKMsa12uKJOlaKPCC8XadNZ6QRYw7IVCUMQhVIU5lKedJd2duPGPA5HVH1xjbES1ApbvdPyHo0hcaotb1Hr15RCsfsBA35sj/S6pKhYZe01THsgp/hDuK2k7wdnWHSF3g4odyWDnXGwg8RYgi2xL0b6XKaWb37WlhLFIhnHNMS7FV+sdReQvRFOC/y7jvBea3Z8SbvUihMrhZVUn3q0FeqIqCz3i4Saipz5CkjjYHtNTcYq35KV0fYWNSmZXF9ed+60wpNYViLmFzjKWeD1DABMvICP5zN/772pXtcf05wGG5B/WzEV9PSn5ZrCrhMVB/v89VjV00l2A8VS9+wkm4tibpotnx60ieqRDvBsum1ukiVVlbwoi2hjxXogRFxxz6Sdnd9kYppsoftRUCvnlnmUzjPdZ7odUdvO7mtPhrM+rHaCKUVEQplc2hx1DSRX46CfoD2FNuuhkYEajMzxWvOfowVBrMMnY8v2M2hZWv8vXwrApCIPUSgPr8WnFTs9zduJqpe74wwQEhtAJsV5NdOmNWPsvLudY1uaUarCiF9+Enzzo0NoNnHxOSiaB56LMPtIPu2jzEwHmczOQM6bUDbiX8YkbLn3WnqKPm6cZCHJ7meU15sG6E9KgPR4nkgZDr1Z3yl3oLwJ4J+KQNB41rYAxSYMYVMVYAQPcXufYemQoACeYYlgNt0Z99upHJxtqSJ7pFpAsVtkYwFuY6S7+0o7uGAviExU/3bDAwfP7AxVt83ibp183rk/BKl9B6bHj/0PqfDgGSRIcCWRGHvZyx/EpQHGqHox773/Ji3ELbmVCSZJgPPRf0E4T68+5RuySMsqSSSqMtyC3e6Y7s1oY/i58m8QHe8Klkx/DZQqgT5GC3BIPM6tY6j20ZOr2i7UUYy9M8h7jlvBykH2a5cXzfDA4gC/OpebotdpFwZuL+xWKlOGmZWFm2bM/J7IOhN9hrzAi3Gmppkvm04ZgaS0gO6LA8ElSGePPlcWBlvvl50063zIL3cdiNHFiFDJNsaZrz2hwdWd45gl/QCEq3Z3npWjk7WJI/V2/3eYQEl7L6RgSFA5qmuVNHUt7Rg93pjycIflei7Yn9t5EtvxPCZm2BBo8W6bqc30Iq+uAaif0Gcw5JMzLQA1ycYM7p24uicdpKl+I6A3w9p8uUkYH3dQhG6MptgFEj/dP3ahePdhATtiWn5qvZJvalMiQ+NPCEjR/1Rnyu/FagYCiSvgGj7flFr9ZBCoqC7dKUylA/29lSmmgp0lELRZPCZlKYz7eYwhijCb6j197MzooYjl5w6VIUTrS4thD/dio0A2O4xEHGlZDa71KMq/qJoBfTvHK4vSCb9Ht+OQIzuDyPVeOZcsznqC25qAGNPaHbd6/4lVxRaIqEbEST3jHgvC7MFw0H2Jq+4MVOnJDvt+K/ob2YlGSmnrH6jnCEXRT1+M2bxNDe9rgpyUuqENasN6egS/c07wRW/TOI3X0veqq3p7SBFhA7L97Qvase3hPjEgdr6pU6YzoYadAGE5CooNUDUHIJqjekvtUSpneW3ju5/EhprPkCNMC53BJsJzs37QpkPGALjw0r1G6GJtIrKDi6Bb079WJp6ztctU746TEePtDhc8zbgiYl0kMxrSEJzS179uV8Gd5npcbj6OCKjuTTnIvXfTvkufPoEoU82X6RHTvzG4LphAusd0hlhhsJJUmugT0YN2cnM7ie9qsSGVd1BocVlbDq9tRDSB0ELqVA3vM9TiS62JrUMVMUnSVuOYTKzhU0S2jUe+l2VZ/+dO4neuryBU7IwWwFm9lTG9sAMM0XwJ7YvudCAhNn7nB9+biwBdmQtf+OSgoUZvTEZMwv+urtA7c9gKVIIdTWMpaBt6Lg+HzeO5g5khaatHenauxLLsN7Ildyh4dYrHqmoV8DMtOhg3ugvlERzpEFxb+yro1Nnt6E1GZZ3i59iscEwizpuI6DX5F1fKpm/TENoJeznzNempRHp8x9Ez0jRRvCUKp5JVEuYQnRF77B2QRwCbrCt0m590X3I0/Fuuqwn3Q6Oz+Y89pCMIr0E7WKXllxYQvBpsPtlXsmIlpLWxvSAvJNKIhYX1SY4gUwuZg8nabhKurFl2aeuUclTvTFOKYfYEIoGd5r9sJlKn9TtlaTdKcXiCgtRY5wwifiEFXEAmxbxaCztlnzUsq6Z8N/ffZ8SZRPt1TGvOJb3JnZNDclDgs9omd3M1H4IbmAYBfOXcKHbYhwTw7l+F+baMjPHcTD+TOn7LkoMn4C1y9Jl5j7cL95lchRT//ZvTbkkx33soYPml5aiL/pUNs37ebCgcUXJTDqCtoT7wGCQc7jGJ+nUNPTU1OQn6wceRQqXn1XYvwSRDwx9++bNJGX+iagoxsUUIf7wRNQloa54YB4A8XCp/ZCAqfJtZ104az8z852Ql+cy0JsimP3zlOq16s3vTbzpwhGyR2OqQF1j8KOkV7D6IMVMpS/NAeu9dRsPu3dwyt+yX29vwv1V9KSwTLVGkCAxCg4e33AQHNAY2XTvfkV9mL0ofd/afffzBh5mxIanbUdhYaSAJ1Txs0adeixt0WjkWDjUcVtMT22TEMkkU36JVdkD68FqPIEh6QOS8jmWBKVmh77zRyfAbO4G3x+dCsLyMwhQiDFpz0YT5fYE93srdJBrls+UYwH0GFVfaE0xK759ZdvtoNddMCyJOg7KFYvawwkjZvyOYlQcDZBu+axL11/hXqxl0XAVFvPlcsmYeIAxpujaylglKU44gI5vzvZ0ykgS4sd/Nyn8XYz92xlDq1sgd0Er6mfc2RW4++S1EslSZzERuUsmwXnkh0LeruqzF2EuZf2WarsvSPn62IpD/8ztdZ5onJV2ClQgQe4Kcab6Wc/t7UFwOxfvOH8jFLz+XlD/9QhBZD76Qa2giF6nrasScUvitO7b0HBC/kG8UMMQNkM85+LIu3BiOgL5ayGwND2E5o0G00ec5hmCB6DuchY1vvnQtmVZL+Z4V3tlhm0I78Y7pXXB3j2tbaV54qIPxT0l0Pmamkf1DKS33iOY164wS1FpxMvpiaFAtPmIz1vglW1OC4TsFy3k6YEzfjzT77SLAUO9EcoNvCyT6MTmE42a04zsU0eJhDyWUooUg1OiPEj5Qu1sbHSK1GKW6TR7cxLW+kuEZSqsI5W47J5Qv/W0lvRtyboXxIGMa2WgWk8wEu338tZ24JbMH13+olKiwYm1XiD1+9hYT30ro+y7IPG/+2pPdE0NPjETkGeqzpYkmkVgGuT91HsmP6vvAQknZyS5aJ/PPZRRzusbPTDj4mumzkMao9H+d/sHtHsRO9Pr8c4LIKnhJujS06Rp+aPvCa8bwj6fdxZHFKrQ9x1xqApEOaKHBPw1pyR9RhQY1q6cai+xAk2DRfnO344JKfSXn61wAuiZMr+VjL//tV4CsXKpid1Gl1oJEyWvzOGgcaS8V9hR0yiCyTa/VZpPXvV+SYYRlN4mkusRzsZDP0t5Y13J/TigwuViFzjxocIA8cw1tBbFw2zrxGmUosMNVGZNGDTju57/jWuitNBT68aWVuPXJ/3ldiX2JyaxEeB7i4OkbbSElghvam/ylkL23PAcjemK5qAxdUZ3fQ77KN7tNjTIKGmS3woWnL5O0uXQ9qGUEEKQD0Yy2fj4skt7tB00oh66dN5dNzUetwNGFl9MEF8d4vV+l4Oh87Vm8uyb/RDLZVM3gkTSPbuj70FYQjcpMUOtvwZYkHcH6TsRnubXIz6CWe7sTKjvKe1KPXIum14M+ubO3luCERAaG+crlznU86OugzSP0syH0FJ/tgg8BdYdxp1PaNz9QNQggZX0Dp74WCX2JBZ26DQ3kplpQnltelmwLPzMSESoVr3y7ONS/Yx0iIuAdu8duGBlL9akGznx5Ow8IujsdQsG8/EURiyPqCdT4Sy41ZyqgsCFypW9iTKycttsZPhrquCzY3qFa86zUZldzCXJY9J4CneBexDjJYWjbfOGDVLat9XSzsP5AV+hsYLltdokoybSSijIdvVphtKbPWriZHaalCmoPGUkndWBnr16ux4LlylQ3OTou5pozFeTWcRSEmeASHPzZjKkEYzdF2vxp/VOy+jpGAE3c8+uSuKVd7nLbA/9mIQe7CK4kwQQYzt6+XKObNow77OO3RMokiEhV1BsHpV/oR0c5IvRlTFscRqrm6K4FvbL1WpD5GhoEdO3ay0kamDVXNIAUepaD6LRzC9LC2kO6QyA3+N78rykZWJ4bjwq3uKCJPyFolCNIH+nL+SkcuO5GBrbZCPQXjJpecNjkb3ucB77Eix6vxqnVMzUFmPB3Mt28fJRASM0muqkoJaoDbOBksavnhed+Sxwlq/NZ1vkxITsiw4IXDZ34r2mwYHnoVbcgtZuP4kQcZoCRYX1vtHgHqPYkObDqbsVXqVItK2a3+BGPzt/0ysZcRlZramZKo/ZxRiDPdE312BXwVUEbwntGAPV9swjfmpzcNgrvg6DbldSWlxsYbMIYR8UJGLGro+yMLCPMuyDRLzfZ0GoKGma894gnJ3ZvOe9pDUReyn7REZG4yxDeptPFsGLSas1k/w5M3uoRzb55+MbxPDpjsB7wna9dePrThzoFqJ0RwSBlGS22Dd+U2Mnjcz8sylP7KA1jHkKYh/XfFIgmWxuMIBGRZtNfNxOcLUknnt926DtEJ5Mq+61Y5iFgdc+ZqZH1uad5LR/uk9zXQocQeIoY3kYG7jtY04zOf+VYrOKYieg0R99HesJZNE5KQS+AZx/wqQ2P69HfH2QedeVYJOKGhr/W+DfUhTNT39FaMZuG7d5uRtJM0X1a4OJCORKU43/Os5MewFRdXkvnfh8pc8cI+b6O3GwJh6CBiev99xv9NSnfdhUYdS4jrzc5RlQkEL9y5yh4k0Jy9v9ScId3bgCKZ8kgoaCYN79L99bMwE60gTR78xPFjX7DAl5Kn6J3E6IhGuMAN8BobzG7pRp+kdAfcr1HuVYzxLoCOkbIMCtOmkJlDNNko7b4vKJdlgZYaJKwsWYWrPoKoVGcZntRPOh8bKkAazTvMYqPocJZUoDdKvq3bhGn4ZrZzhektLnWe6pyJvT9rVFEl33wkaWlLafpjNDbtENM22bvy2LMCG7nSw+BGcgCGJO6IKhiWoiQkupQ8RG/S4RfDNXCwuADpUElEWYkajvoT9kpPpO7NIuYrleJJJsSFUQ/a5bLkzB7dgHnA0DemRSuFZX3szPRQSw70uEmhzrYJl7scMkRGourIxivolXh9cPVQI/VPWh9zhxg0mjLlyprFHEAxQso6nF0U+e2ngDouIWRVPEIaTCFszsgL2RDe2XlqSgOa9o1hPe9W0bMX+Tk4urpsMp+0VXr6IxNCDc9T1O2lQAlIE4TJX39NebrhLp51wAJVOKAaFXgpCk4Qv1zAcguFg0yJ0EJQH/drOxFHxMWGy1CZVWoN/YWcC8LohXkP1FbMPnLNUH9G7KTh8+eyFw31E07hxYPOCodPtz6HrWB55RYmEarujBzIkRL6QoJBh4VmvIvHY4pyxvULxLSoE9Iln5/skqP1lkjNyw1w3V/k4dCwztmEVdK1fsFdlDX/r7mzf+eYXi+ZmWO4LGGoHmkOzJwOTtpL2rIv7tGTK/9kumxLzYNDuDn0eMawSY3l6f3m9Pcr5lJpP2C+TnY8JTcNLTC5ba8/Fh2hWR+yZHUXCpDNT0DAwVDBkYHs0AAdwDNWAFBCoB6rotg7GJCcszldEQbXbDIUfsebCFBVpvjx/DDeu93kusNASrNsoo4qJDgg5TwJp2jqpCNqTbpoiIyJD1hzOi+LIMQAs1ciEuDWEBGdtlnas3+q6xr5njfUuLj6gIE7Qc12DvTZbNWaZdwoThzILOpXKggHfIlz/5lU3HEoRIRUvKll+aNuQF+FJw4ZbCYUSPVJC/JeqZlx4mujXtjh5S4Z8QnZcPfmyds0a2yzMpIGK2uNQ8LcClpA+SNDkWmIpskMyiH9lIBj0E/3z9RW+/fg6LxkkcZ7U2OJvq1V+J4ksoQQzKWshtvcmRKnGSqoMpRXhwL9O75XgDrKa9XtvylDG6gAJ95GubLLUOsDsok4XGJ6ok3VD65b5BfIOI4BLYAwcHITuXM6keBh6G6l7dj6ts31G5KyNE12ZLblR4ZNt8p/Ft6I/KLnW+qGTOqcknXLOLV5bARq7fgg9OScmdzC/jChbs6tHb6SAE+/Zjfg0Z/AvpiRBWQK2x5JkQB/lmvL5ieTqufjiwoP6FSK92RfYmjZtJBPzZY/CDSZHgGfseJLJJQxIkRpfzN9GogbzCxRLkc8iKZlkSG5u8BerGClUYgiP//baofTK1DyKvesoBQms7npj+ewhn/4KonsLgHP4p5xtAbOwy+nv9RJyS6G8DcXs/btPAMwU7CgrKlVaXeRO+8DHDr1f778ScQj3Ne3/9UN+EdG8O1a9EJNbb1Gvs70y7EJzSKhYzaUBKvblTux1Jr7cp+Bx9me63DEU00sGtehloATQj/ZmvCPyxW2Y4P4h7bdOLWuH79ZSY/ZtNhksS7kz1BBJcj9FLAYLNlMmmOeTFO5ZmRZGFeVmvxk6piI5SbpqMG4YDm9iHUwfMyqcdnaBuA/QbcozvTNesfDYvNDYDpKv2uQLuAbVtXolUjZmfLouR2j/85kENk/3O60Yt3NMBLnkjU4jm6ciNPm9oJ876e0LITLqnLu4TiT+942G7jCnMuWTTbe2cZP0gJlKdKJdjhS0OGtUes2lORPV3u8TiJc6AdpYw75OiO3LtUPbzl+AKw50ykM0bXK5wQrQJ3F+DkpD2ksqNZOhol290/a69nSNUEuVWmnXyL3GJnZ3oHsXkeWEVSWEI4iSwIT6B0xK2VlgMTpG7HlDQY1ZUiZkxzCHYTTaoIoGIthyqu7O90+Knfs1RhKxijpguy4G+2JViQyIPfT0cCMPDDSXMkaxow4nELL6JqcrTAtrhhfr74CMOTj9x1Qzu961e4LjbG65v+npZzrLeo7XELnFjMgm5bxF4MiSFZvwUN/A2vkXt9LSBFIZKRjBFDV9YOm4gJrzD9FIokeSN9MFvz9mnx1HEKQEPm0zkzTLpiJHm5rQX94f0g9GvW3wTCTYvOoZ/hMg0oM1M7I2ltuNqu+EgcJ3R+2VSLrNysHDA3A3RR5LBaraI8A9mdxf02gAPKVYgM+m0U0xMtA+tZESP4EGpp0KPkH1m3pe7S2OOLv4zYr6PuR+Dyaan2f2KCLo2L7knMTi5DFA5HofQTSU+tL7SqQOfN8U2uBbUq0RNEynkBtLv3AkR2KQNf1+GtB2CB9SLbSIkLB6LNoiUQ6hZKyNR+b61o/Ef2uJBT6O4vgSzuEJlZtNjUGZ0xeTrlzpw8MJ3ajD7uCCwBL189GnwuPIAxrJOnMru/SeDqSf+dKsDjHEQGeQSF7bLPKXT0DJuI4eaEBtFi9+hsDvv1aWi6gEtIk0w33u+65xOjafzB/pNhlDouGQP2DqczJyeQPiL1eOLe8tr8HRmDLQqEbsjA/SvcERaKFxvKLBbFNbG4DqRfvqd9FIGLTz9I7JodLYwpYMchLeBChCiQg5xVoeEmmuht7DDPxyw7QGf98hXSb04DT/+KZ0m3vrxTd/n5A/gnRJ+UbO7jvtlaqFAWhD9BXn7NjLSdHAJIxWeA3OVCBxzEuzwM5MvbPZP6otydxjARSbj0WKORkWr9KmWRJK7MwgrdT7jQcudVMkTV6ST2t7w5Apy4eccyDAE7iv5/bgRmqFeMUj0QOdCkEER+nM6b1E4/53qv+/XhjQap75kSt3ufZ4FsdAdTA6EFyQHLfE6c2Rar2SIRNt4fk8ytya+QuXxefLvzsVthGuJ/9ZUDIy9ikmOb3IhQv7YH0ao3rmz0HQVMTGyPxKfWtMz9PI2nixaS0FlP3Szx9dJydjd85DfweP6ffBJB8N5qD/1jnd7/lwp3r5Nw3qBV6e0gMXD/UWNRmKhcf1gksgeg+sTzDY6FDmfkfCazXPpUtktUeShJ8WTINVKD8ZT8AC+hGWKcteth8CRg1EJz6I4BP9pxMyvD80KZwq5fjyhpQ1SA7QHzVrBU2BdgYfa6okiZQhxBvZ7ZzcrHtCod41+dlpit2bxRaJxi6VDKKji0MeT+/QdF+U/epUL/TDikO6i0ZVUtfhFWxJValmcD+91GBN2dZ/Z9aiQkYkQHXYy912R1T5GI36dFzAIspjDjo0bAe8H9XAkXZT/Lm1kh32GfaF5zDc11wRb5eT9G1ApdHWlZ3xqbhSdjct5vqRXBIU9/amQEA+U4yNSdpuOZ2o+wPgrnrXBfjUK7usM/k63K8S/z319dSuInVfdajzqIh5NpxX0h3XoiTPcb3MEoPj0qN7WRH82DJJyTC0EikEzckgQSshtqHs3JHD7unZGuEAs/6WFoa8r3Df4tQEh0Iy06rnWg7KIjsDBbWp/Oiy+VFoqk5EKD+bWL/RM7lxtcAGZSAJzUi7NjXhLEGQ+YuwqrJs0EFeibWqK+UxNYOzyqeF9tNajfx2EgAbbRRshJpBv6HiZmiFDfELgpc57z5rA9fIsfsUL6G97SQefyinqkm5xzdJnx9GfZlUph/INmGMv/tBh26h40lCHYiZignPrZJqdmzcQEnEHWmxK1ht7bIpR6WD9a3xBxXU39rd81Pg2m7Na43A8DtLpv7YMYtPUEKBe7XncakqTxZ0OKgYHBPzuogz7fbRd5Xzk3jmvV7PUmnaEOVLvcfMipBydFvuRk3whHtfC2/MmbOieg4um2d65Mtkw5k5s+97JLCq6t3ZH15QH8e+xeMkKq95BN9FUeaxntZhmNk3zuzlmRukpH15HzvkXNQ3aInInISFamfZw54/Coyp6Bnd6OFC5f2u87QKG+zot8HBo3VV3yxL7RvmvVJjMGUpRjJq3PHqj+9g0rJMsxr5i736FDx+gEN61m+QC6Qu1j03JMtn6rxj9BiVKbt9n2vSdhrjIYqYEM7qWfE1omR8Q/fuhRgN4SmGKBDXrL3ItAnEmS2eK0MDB6DpRRz3+TAvBB/2sH/OnNY6Sb9ZbWrEEsBwMKrf2+K1pFF/uGIV13/MneI13WZznH9bfaVR+Bz1F1UpUlUo/uKE1Z/9GYkCZy1R8u/zNx/q5hnTT/31Gm1b9Y/gB622GGag12q/30+szkkbe2JRzlZ7CKPpAYmrrP90qn8bS0q8vwLVZdMUhf+Vi5rkJOeUicIktLQkPKbtL2VGearzbGgcSvndTZ+9f/eo4gh6oIOMVeuHIuORx9MQodc/xHG3J92t3Usqhu7chQpSrcsVQk/AHdWbwkxpr0TafhbjVUHACp2+THr+uxnld7nOfpTn5mtLvhIyoPWx3B/oeDqqd40LLsSlfz8CJuxDB6qoGDkfKpKFCiJEO5NwK0bVZOYFUvgoRZy/Qz6Qh6eDMsG0zWCH4U3Qjkp6zbwPMYFDNWiXWpyrUzBCd71s7IJXClmM/Eb4yl16V6+vFlL20CymjI4ZAE/Cl1lo1F2zfYF6fgPQgt942HhAkKMaIHd3aV7/TBZUarE071uh1+5sWz1OJutly1iwfhDZ9SmMGQdnzBrt75bVVjzcou/jkK75Y3gRJxM0kcY8U9aaOl8+NDnJN13AvyY8raJsnIZz3xyyLcWWBPwTBwhEEPxrU+ln+8gXJ3nsl5BJQqyzfxTvraYSEkSuzUUq6KohxNfWYjW95JfPp6Ev2tgINIf2U1D1fBNIa/Br8VOlyP4PktVlb2r+NZcBAUi/tgMFWD3agQ2tMRtN9CwR0BkAHy6Gi7CanIn5ZLZO+rC8a+ZF2+GQgWTNfrn5ouzNadnm23haq91bDLM8SfoSmj90U/ZzTGIjcRO6wOJV4kXfQqZCuTKBZto55mSbdDenMW0NNIn2adb99H4gx49vOGaMesIbZySHtZFO/4Z4xs6lfEYqpPfKhYw0SWnaRFU5iaQQiXtv4Sb97aoqApkcsatuaheVkwbV861eTf7p6+DxPsmD8zrnwnvxQXIEzkqxFH3z7Z03PHXvRx30+5MrmpUKP6UxFYCngmEMjV17VMp76AZkFF5OFBa25T6faKj3vLrnCHe9PRKeZzh618KzkaYJ/KR+p9/r7UBx/TvvDvO1QifRSbhkR3yvtJfug2p5B5qVOdhzzgUZktzko9TzI5PMjk1RZcN2YGSScKwRdWleFMZwHdBCOS+gj/qFfN2P5eslfVPh4YJWoGaWoDv2mSDkntrC8fzyQfLl4kVZNjf3T6zDwboEQDWuRhsLnxhpl3vOuYs/XYU1x+17N2JCb00wpAvp2TPGRb55KM37bRrCBVMoeg9tJkCYMu6t5cSqDsxacD3/13clG7Ixp8pv8XVuQ537vXjD4/tW+lE2GUhnuu8+v2Ypj6oxMtFcWsFTTrifU1zYkSCSFs3n2pTVcuMe+pLOVLA6zkTD4eWGd3/I4lb7WAjMMxdV9TRUkpzkU6vcJL+FgNIjZl7lb/ODH2ylqL/GyY/Yivy10hJ9n/7ZTjny7xM1bqtc75NH2EMzbtdpEf1fE4mmnReqoMH7Jh4syAgoB3mOHnZUuOphvvkY+kNcxu7J7DgQNphemyl1v/a4F1N1ZQfduNghbEExvBwQns+FDA2x49h9Dqs6ymPd7bL8UBoSxoUULaRF9J0kVhTKFSf6u9A4RJKLOsMkWYcoV5tFjb4HqoNEEn+cdkiLIBIZFq/V5zsvglJUpOpfIQ8nUi4mS4gRQYwuL3DWmwQGXKq12Ac6aGpn+NshAr31JcJRivjP59pD3QzVBdS82hH7GVVUTJ23stzsXCUW6OzlubH1qcXJihrC2uzQw7zNABDInBFz29RGPsDOotRtxd5EWmRNl+1mV2TWgO4pJNoQwugJjejwXLqyw8BMW+p1YKTuMMcZUdRHca69laFFjZfOFOuNdE7V66/kv+6F9tePGudW+Zeas5HITHWXkNRU8WP2eaRyU2UF/jX+fE0/qetUGOB4ZPsh7eoVXz2YE9pgvUHiOIBZywfYejDh79zASYjBts/VneLYLQ43v3bkFh3c54mHtIAj9ohjCdf0G+hdQJS+ZfULQNYxBTyvhZbpRvfVrRkm8YHZqFAj0vAT8BC9QBfTicgAM2j0jCFqXfmlz27JmIgE917Qp4ZpCSi8qQfkylvuBXhTw5/HjVut38IovwUcxSl7NZd7AZycIx96mYvcGAJjaTCvx9cvOlX0qkL9n6W2V5ywFbK69NSvdrOyU3AeUk8ljPncjLZMmpycspl9nlBIxUAkjtomcenAoFeGK7mC+hhNSoV/gAXARdH6Esm+G1yuq+uhmugUgk+45QVhAlG9uZlZnU07bxP0Dgp2rxT8pCFqGhncpuIUC87U3VJOCAE+wa2Txwmffx5MHiZvG3TIL8lhRg0kWZj+pZBF7QL/MXyY4dOVgP/ML3wnjuSQFo/ab9O4qeywrmqqcDTn7CCbmVFHqqneEq2eJK4pzej81csnTjnbrw1lfJ/Ng/+mWWP3xHqJwVeTSRVrZV2AKQUT50KpzxSi+CgH+9n36dwtAoJPQXsO98o15FePWp1r3yGvVg+3paRAznh5DCmnJU74pqgyzyuYonecvSNscLuk+xSGmcmGayWGOw38qQikmTowpBKWCyGiPmTrUBVf4Uyw5MsLPl4QU1jQTy+uM9Rlqr55Up+4W1iFXetn6fnIukOsm/+6wSaKeAHs/8SOZHopK0ma+snGcC2OwUmh/a3mN0wg27teb0YXZaxUw8VBkwWrlZpCIL1AZ/hQcXqNw3YyXYhqQVRJB+UGsU98T7uyVFd6ekpDiHiMNRRFc337cK8nG2IIoMFLHz1mgZ+5jY1LI/FBESnpsWEZpj2ZHIkdjzzm0LfqyuEPoQ7QItbf+x7yJ/i2LUQ5vPMBsBXP34oUql7cvwtwEhFQ+YjxnqwspM+1rVxujbvaNqIM5K27tkAnRM5IvwzXpgGSMVzrqoMzf+YFQbWEaTR7RErrlYlJiC/15kmDHuqw3t98q3zRS89mHsO3FRUygynAdWrCOxYhUTm6R82TxEYpb2BClyIs5LtqvUVzX3r1HZ0+iwv/e1LxBjayddHtLVCUJdAzeJuw6PyJC0IJPV+XC3bhb89taI+QVOksZNRc8masz7cdKpJmfVcW5GSXdRJguagTEP9wEUTf743cMnickp+Z61ikdTlqNrtBWJSFKYvetLoz46X+Q03tSDwB8p8+QiNaaKFHWPttAXnc/50OwdMnYuTz4iFnBFMjLFbFEfS80TZ2Z/4nuWXgXKxpm48HREzqlf9/FllJTjnbs3ezHMQeGsM3tD4ZrQwDDK/g9lZ0v+wEVs0vGR/GCGYSwUlpIVHcXvqTtTCw2b/0G44bLlCbrMqOIffky5CWaysCMJ61KpNI9uTHQz0tq708ft3lRef35zBbenEpK1yGFRddK/9ZJEpsEU3r4xvzOWmomO5uBQS4uNuZIGqhaTJrHwxkFt4Pmou01ScLpjrIPvS9oVT6g490X6qwMe3t4LfEp2D8t8TbajWoHqLJJbyc5k6eosseynARNjatQauewt19R7PHIYpoDnPiQGJyfyPXNujLuqSfpN9kzM9l8wZv5RrsMHQyc6Orl1XFDSJEJfXvku0KFBEHR1pFkG8vVCXb9wtt0nL6JFQDam/ssZ9PV6oMUthiqCgoamHqcaPkTpTuBWACLY2NNTUjeqa3VoebHURocHTWGvr8Y/mTo60m1xkokhTahUMGeoz2l562RmFm4SsgG5LUHqq6BaG2KpoPyzEreY4l9+lxmei7AbTzhKiTstFQTKdiu8MV1s7uakJShasMQ91BDiZkSMqhRyZcfdEcT6kL1qGjCfBNzPDzF0NyLmuBrgJgcXOZD5FaXwvCslbSHHmqu0vj7pG0nPSBGFCajdBVn4X8e0sVkQFr0jmA3FQxEw94jWZP+eZgJ7cYYLoa6ga4eTEDeekDUDALkvrlATfud74WCkg1jhl14SnCVdD/aj7nDcJdCzUxPKD4grLpEE+GGmQ02S7YpmB0OpFkW7LipGrlCnfoQaY21Cs5c/CP5vKUGmkiocO6Jm0wGaruKYcckY6rNo6zio7s7Q3B7sPF2gCBSXkDcIucJ+HgX+Sn6T3G5iXChihBlBhsL3rOL9eONtUYLT0odTm8B0bB/8Y5HRuCfJh+wJb97BLxnVjlCsLqtKwzh+mngo3z3ci8+QmvzyqsoX7lZy/4762IsyALuARekFKomLzY9U44K1CwPGKbEhXeUrSqU4QVloC8HavSwm2Y/zx5KZ8riJ3QRTfXY0wKWsNyfTiY3dknUImwUr/us+w9P9I9mZtwYRrGBbNIofyYc1W1RpIxBPSz6uMa4n0ucAvxum37K9v2lhYX7gYR9DBYIGHe5UzL+drt0NN1M2AyM2hGmqIu0vz/ZL5hSECKVGIgWGCyNNtKTBBpe7LWwT/6WOccRPfwsZy36mqBXWb/6IifIKn9tM+AwFHLQ3I/pH8hv+hDxNlD2Ms9MrDfi4JSWHX6eB0iaIcTBg71UQeQjrtKn/vaLVCm7Pcuj6p4n/kin8JRUAYnTjEpPRk1/frGaNu8hpYfe1x7b0N23vRXBQlJN+ddFJ0abX5fo5MlNb7Qs/aQwOcfbXwEg8SyTCCw7ChPHxW2A+OPsy5J+V3ALTVoc0hB97XnIYZqoZFCfZocIkoR7QNn+DVGPFsbn0NyZ4PhT3R47w1WR1lLH58xiGLiK+nmAvLn+NcbDTSnr/DZiOUyf9ADX+5VUd/CmpTvnhmpj3e3RkKgJ62S+OQZuhra9DAYqbRzCmVKsWB9+i+tRYo7fWOsGWc4+qnx25qmMKcXl+9rfCVU+1sB0NtY8rlsE/0XoE7tsgK9wAo1JACv5gG1sCfJWz+q4V4yCeZqHXxXwlPs5v2grchYTVn0//YUixfQpKDtKoEe86Qd61vG2E+B+FphE5QBzJPWg1IKRwxO+pWv6/mzeFdU1/Yx4R6Kkc6dxqDSBr7smmZZTIkCOMfUGVLMzJqKQmL5JZpaIn/FZfBLvditXwSulxmESSJUfTDu1A09jqGXiW+LGsVx5OiXRMeeqzu4CGISiD6OIjG2EZCy5eSx9Y2/ik9Ruq1V0wQdjN92nv2IhcT+MIEqQrVOLvbSrnVZ9g1l0vo7mlEupBlRFBJNho9+RPn7raF2BiVo0b25V5dRZGoq8cUOcdalkphzEFL6KbVVhGzs4DMsRcrVrR4UaoQfKCWOzYgeYmOfbkL2uzNRGdsEI4ndT5h5SlbC72btwo+UiUT0NOE0rniygrP3tCsyAdAm3pAgPjT95yXdsLQgfu8UtzBISegGF2uU6UMxiCch10+96bdgY1+d3uGVCYaeUteakMgvbNrGwFCkJ9j25/Rep+Glrvp6/7Kmo+Hvz6Bs22BldqO4cK1NtzCvm2U0HtJgLSxDriedP1GvPouVkz7d6Fd/ieNTIqJiWhjDz0+k35LBy8RNVIqms3FyeXrRTBrMzxFMUJqgg1O2QaPYfR+exoCoMhtEHYhF6Wao0kSYddrRI7/3pL3NX42Ich5D/+88RSNZD6e54m2qzubWEfysp+gBfB1U3NvcFiZd1AjHiSLflUkE+7J60xNNg8iSe6ACzjI+Tgt045Bt7UMvnGLeW2eM5LU3vs/VJ8uPdFVW0MGT6Rhjti1ygKHaOGn45lbislQFVJFaPduHf7sHsewkSbT0iAmQGI6nsyznHEwSXtYq4891qy4ReSrubWw+Ux1Gkhw0CUK+Q5g+uIpeBPjbrSgtE0xDBf0rsa3sSm+zW8DMNLWA5as+YjHs0o53i97yL4TIBWU8kGkMnWILDl0YOcngZiV9WthATSykmTiArEBYrU5RDGebwOCqBNhHU8dRNSDXa+LgXeIBpeQTgKnzbJOLjfWVdZd6a5QdQRqzgIS3nEbCjyrYP/Z6o1GVMx9GJFCRDXMwhqQmU6gtAR75tX+BkQY3HdEb+Oserl+Vsdky5JfWtN/Xzh7yuil4YrXNG51h9tjcy7MfNrLV96XdBU4XParrX7bf532qR5lrR8Nuxye+yT2dSR/wX4jhzgQH9OXDMLZr+1T1dDeahwU3JezhaQXfaMjjgYPRauBE590x7NA5eUMtif+UaUY53F7am1cZhFDby1lPhryNdKNvsB3E7J+tbYlkHQZeAWyFtpMV3Wr8lC1ZYelSSUw1cHJFarmlvMUD7u4r5X8BhuooOwXtTNrOu7sn4NfRw7wJxPSfq7tCslp8b8WtAq3r7qfyteR5n3BXlH5MmyW+4Xjf87kxH6a1NEc99L/ZgqPS7TTe7jsJNZQMETD5ywvh612wKcl6KvN4MEY48OiqOlSPHuMCpKZfJlLXzZ/bVVOEef7GNWwq2vfCSaBJ6ZMizcyuTqF6BCbSuG7m240uIy9zDGZt4oV3iRR58hu3cL4Mnh/aErlamjx/GM3PS30SC+oGk4094NLPypic+cojKBo2DGuD+h1xRRvOUQIJykEVHWLIVLX63NDi9Y8YJ0QJNiLAWo3y8lXKrAkT44virIHo+ylLsQ41qcOcTNG2t06JnuAKRHK2icOgT2etHZ2TVKiNMY70T5gM+v5bypwmxH0Ezc3evlHc7pTzmzmhD+BUYBzjqc/C4yCqmhdEyOVcffD9H5/rK094vEUS6vDkucRcQYxoIBeABO4d7BTOUID8wuN7N8Z7+Fif76vMvvMid/1u1yM7RvkK1nE7OrTtvXh8kfD3VWAvL3Dnv0bRLfWmqQ8dOfdxSR/MpXknKH53shlD7p1Q6DPa3+fRR2TsNiPcMyUwukIW5SAYsUkpo4t1Z6CfzgmKI7Smmbi9lfsYZSDA7JuhRUYATXcd+Po/fD6RtJlH4LsnDg5kH18zBe7/faCEv1DxmWce3tBR+HKGene55KBRLSZJvvaSrmkUyMti8zXk1xShRc9a0MkLx5nG/0fvBnnDATc2adW6YkHYpjJqta0uP4+su/7woFpjmPdCQc3XY0EOADNQ2RU6ZI0Wj2S+a/j4BkmB8fMWA/f5lzusibobiNve8ic0TIvAZ7ymMnRWujYcA3vrE/MjoFqQz9OD8ItuFPkfMG7Kge7MLQ2/p9xrbs4PRhbkQY116weCB0evoRSmr2uzwYtX4dfhTYTP4xdfc+wdcFmXxtJnGujZ3Rx4ltFyDizJTbfkuNeFekpFFHCka9CNirXkNMEIuoTEQNMRdPYQw8UIVow11U/DfpMejxTvXLlbKqeLUEfsF9BlJ08QkjNGQ42HoymvxJlFMXj1ZIgH3xXvEmFnFN1T7d/QUUR13cwzAK9lbz1nD2368E3l0qdWuWZipjsIleWur6YfLsYw9g17nQ/ys2dwlLhEhRqd89p0nophCDEaeljy3X0ZKq9/9ns9J8zhSDfadaU2yjBPa99gwXhppPwTyW5EJODUabU7dh14EbMuZW3HzfkArH3kH5hmUDPdlGHb+SYxb3YG2MTj+5fzV/ZaAURAi4R64ckcHeYc97dB0vswt2hqQX12cs7PCQuBw4PWaby+dG54Xk1mPs/LYKv9yHmxwoxmhfo6IgSUq0ZLZ7h6/g5ZhIlF1DhYW2943RFKANSNxwOwgUo34eh46EL/hKx7IK+58nO3O60Bt80Tpz7Ww1s31BszxtJ8E012qxEJdmPNNSCx+PVbEOSHRTPtcS8O7OCRxWzsgOuHKKmAQEEh2HXdC6f3d4MGRnwktoRKJB38dZk5lh1joJ5vYGE1dVf2mm5K40CXYY8JMzDK8uwrwXFpApOMoOCgL7XjWmSHEQQVqVLaj63FHRbUyQUpu4vrxzSkhGvk97vp5E13m9k4dn6An0CpWxxhjyxzdzuLWdVx4w49RChwRcDg+E269YD0wVJXqKJt/m4cQIjpus0fHf9dcGoseTl392/I0DRsdFTt0OwbPpW7rnwUM5QsgtQFSSjQy/ERkjZ+Ly8ttplOnDhWD1SQef+thCZfvzq7Mw5wzm4mj7pZ4LBnwGZQ86xdCtsvzM8K4/eGjEzFiGeePoHfSDWt/HlASb1usiz1vqKkJrB7hhfLB42K+KuFqCLfrKZMFnkl8LGjf5PdZ80SL+JDb34m7jmMpwhV+qMuZUD7Xh8CDHEgFI6lNd2ch6rdbwX6I8sGoWZB5Qb99be4SvsupyMzRrdiAXHSbJ5iVw/rao4LAePexrshk/IKjqgX2063I+gHD5tpBIzg5JnvJZrWBulrdb9npgOhP9lFbEteEklVcN/t6Mm7cafkJiGgYYfRE0fHdIHIZ6Iz2o8gORJBC/H5zM2Sn8zYnVf75e8jeyB962yu8MJuGbTpSlkVMn7NuEjece3myUJorlmoxs+JZ25vlC1zlt0A6I9dvMcQn4u/OVojyU2j2A1uoFfNSv28wf2mFKrbSUWFSkHcy2qi9rlg/IUZOFdXprdSmyQh3BFwlmHqTb6ZbEZvg/ZAU/aCO6qx2EILdpES5p/ar0hujVO6eVHG/5Ghk6ot+kl/XJoj2txjLSoVyUeP6h1KVJUv4ahvaPNyb6iIwLNvo4ITV/MnIyRQ3dV2/EZM+eP+58Wz1SrIfMSb34cTRC4QhkyIyy706j0uI2ERJ5WViVu0UrV+8sCXucI8j2jfaywaRDx3WHJinYBlP0B+e/QA77a/Uq4ZqXxHJRsjAJuLpnPTXtqmHnh8Y4ewjMW5sQ3UbnpmxLBlUpSEOnzNczxP4QnPOVgFjx9/sSH6xddECg9IlbGmoHt66kWHL/VJg0SmYDtxGuqR+YjyaVdYKbfu4UNtAq8KVX0WxEq+74VArziOq86pkKvWUY19enSOjhwdQyS11xNpoXLbRGbB6VgigYRmAgp+NrIIDBXmQMJBYasvNvsTST+w0kyKAnwJ8ZFxGPkzLEI5PP3Z9jViGLNJ62xk4mVK7euMvv5A2oH/0HY7J6vpHNvyCOjdXjQyd8yCakiGKHsA8venzo+/dVKI/P31jA4e8y6hSkyrMbq9pWPxQia1SDg+pOdGwMvqYPLYxSOUUO26XXUnBtgX9bvQsGi2GdILQrRXwLN371QTKt+DFLA6TvzjIeKFydw/xgjMVK7Eq4+pCdPJa5Ysx1zxkmfViTaKVJxZ0t56gR9A6o6SzbZhwPyyAXGvNXBZ3ORgaRq7YzjCfq7/tSs7a0HlY8pFEKEt3jNl/wn5/crioU4/GR++56oEvwhReCEnCSAfVPAz8mcn778HNJBktztb09IZowjGYJDj1vDNrttmED3cGz+H8AOYKZjePFLMj3JLEmBXhsI2ROz895U1rty6MDTPYQYAkCfAUT+b3S0a6KZfDhmgM7O4BBhe/02tZ82q95HLNAqUdqBgYCpIJYRvqyLhB64uFpj/qOlALb6uY5afnkMWYuKeua5XBJmZ4KVG388dPbR3AzUtI5Y3xK0IRVw3WT/gtGN+pqLVh96u2S3jJO7OYXB0tKcEs2fKaRATgt/abx0pi0ayHK+4MK45mUDxQszRTVJ/1dGssQBXy+ZLyim2deJOviOJ+ZeCpA2WNgQnp2U6k68HSHNOm3om3DLYDKoApnLHarMwM9bZ53gLtdUPUxsmqnyLP+HNunxy9iMxl0IfKXJOJ1MQMH+rq0+WTBXBCZb473oKNVxGuO/m4jG3jcw+ZQx+r6lShQJ2U2xllPNCDrgqtVrexxQx6yLw9+tfDgxmNFL2b/KQrEdl9ZfrYWzxUCR8KdweBzokSxALaAQbwN4a5OcLH9lQsDVjOYXB5FyqjBDHxjHd+WRW57wCFH1sKcaUhoWBsuoREd/nNKNbmwQ2QFodEWR2SWN7pe7MOYbJD6vn+KazeLUiYG3h8fc1l43rHG6u1T5bBy2vgdrRFj9mtdumYvJDqkpBw3Qh6CdRqepzU9CyahZ6zM2dNJowokBsoIHZ9w3Y8q6GSW/H5OuzZIekIfV4+dDw4iOLtLeyGTliukdwTnoAxdgoVewfgdl6/DIRNzoaq8ATfa+p9iGDC3hZ77jhhsdwI/RqzkEAYQMXQ5p39YmKKJr32WNa/PtgpbHpTcNWMStL59l1kaZGqlplmneVe9r/GPRx6Hne1SRdPQ9Cj4phUGcXLT/CccFsnTD+4abNt13ToKKRPZCFaNY5iOVRMQxfNG90siDHMjkFghA5ftjjzopCKeScym3dqoCqU+D47+NazrYONHgk2LB/5SmqFqzCp7YtSzmCqUdzJv2WOHrHZ6qfQyN9TbdDrp/esinTSVxGwrHKeMPMWyAbGgxwDOkeMwjTHodV5f/j0fno5P0iK5K0J/PHgak8w3imC2wsDHW7sY6wdLvOzuoTD4CvVm0pld2VLPkbC6OoANuu28Paz+CJaDAoxO1YPR4aX+NPUwkyjraZoGTGpLFv5UCTDLUUsSE2WTzqovDngfsMORFxHZkvlG8IVKTi9RxP5xLdfxSqHOvXNIPB5BVjMAe81KTD6aNn08K9HqPoni6lOew2M/DC8GVZHPuHesdbo0n2QZLXDvCNnOIUdkvwtapqDL9BV0rQS8XArKEfxO6ZFdnXZfFz5OThWyWFn+htw6GsOTfLsknarPAu0NKHoZEjv/KFg/IzkhGI2KKtcSmOiG0POoo/I4B0bFkgdNTb89IuCmDOcjPuuKu4Qf4s/jdl4qhRidvXfk71+lj/V+obhfCBkAk+jX/ckhpx6d/mghk/4fpGWaSwLy2QP5gz0W6pFE9PnzQZtoJHAUeQFj+nA/eSg++AflTYWG9+qlyHPNIZumZNveLlYIvQj8fK9zCDzH/e34Cx7dsNEIs2TFT5SyfBrXdkEkosC18o2dsmmFfQZvuudb3H2ODu03nMrjF5Itzk9gb0m+qpKeqDoK5xuL6gDHFHxSW2L3EHGeUGC9Z1kMUPYAQKYNok7Km/2aXK3F9SsPcirxfChyr2PknNIgJKofLiqtZr+/dupz6GMJ9Lqp6F39kr1VKbcamoCPZAlXM7EtYvGGhr6m6OBjO0fcp3Gj5hU1uhZ9Db0O+tVpClJgGzb5fomwMYDQuCeZlpIYkhb9tLlTGNT1CjieM/uUlhs4WbU2s/eA7wfrQPsGWanq6uZOxhSXEI859hs4nNTHaDz+EdA5WYUr5CC77Xz2wEHbf6abLFRmEZ/EEK/UDJf7N3z23xC9xqZloN5OUJB9p5ZfCl6QJDH3/ds7fxmExpZGP95XvzgLHJW6zRB0ICipceeV9nhzN9kztLkx8Tc1NxWheI14lNM+pvYIsinjuRHYBhEoyJ38shW3k1xf8SLO3e/F57hPfotchc3bKLc9J7PsB9o0Mx40pgG9SJmMi4f+bxjT/VBEtQikdxvvf8iSj7WKD42sxsMs0ASNIprmd1kM4PASRZPKfnB9KjEy3nYM0hxsNPPn0lN9omZ4Q3o/AbSmVtkB8/uTuSrmFQqhNPuJxHPDOwvAArbHRWdRneUQDoZHwMIWLQFXZuSX5xw4kjOncrlmS9QncEUQmqX1xej5m7Sfs2HjIMZ5Hmh/T1Db2BjcNWvLPJNQuEOn8QQQ8Gae8BQ2TzxYFH9nsDl/3cxKTm+bnts/urLMq4pUpCxwQYfHkQ17aYvmdP0zo/WqAoNubjyOfG+v6A5e0ACL6IT/ywPgNG/lAu5ekM3M470ZZPAgoBAvUckNrfAxzANz3eGBjaNwGc0uB3T2TZojgD5AW8y8ZqNuXO09L5bxXs2A2FlEXwweQnetM1UmvQ2tnwlAuT8mCuFYuZqalpp96Vz9B365gDeTDJCROyQ6UBAtg9uABHtuwJuKMpRCCL+KmY0r1auERxm84NBspT8SThBFc60dED/oICx1rvzXGCnOD1L8B4JCB9oKrawz22MA+oyW3Rbc7yDfVKkQL38VGR8+cecl3Q8gSHuPwmTIUt96QdXmY4ypr7STUShRWMl4/3demv7AITI/V0tnKo607igWwIwmk7boYY5SRqZgua7txu8BG3zMYHngmijh1OVN4FGITlRpUmTZvDmdBJ7hc7S3GFBgn7TLOoNcEyL2NdREuSiB3PdcEh/dft0rLxMP7op4TuAHWNU6QH2IMKF2PO1GGcltXZs/clT/A66mQd4CLMtI88eZVf9jsWOsRAIog4RtXAkuMoTYPKIHBb/bCPDnoi0IXKBvNlwf1C4v6+sfrexzwJDPCe8E4iinZ+2qXRsNrJxfVwfj8oEp2tzbYCtxkYODYRrqyUUPNBR/Xv0OFp9ePVF8AjAC605ShnkpUZ/6q2t5vZRZMN2voQMKVLsz1Lmalobyah3E47M/YO9Za30FuSRsVQmrROurCU4s9nSukYQt8DUXyEHMGXpmcpUkqk8VdZRv3Libh65hGFNPUkRONSVLyFOBH1CGzv70oBBvElHo8DjQ/nZhszmLe3liFawdW7ysxH+/WYM1RrlLLR+jlEnnys0HSHF8BEnRDOcZp7oK6G6UFM+QLbFuKZUr0tgCiIcUQK/qYYiKmRNklJ+LLdWJJiIVevHbQyJaOsMf4ly6SCSJIXT/l2v85cgxNCz6lFfqDserwXL6b2KFv2dI4pqBvYn9n+JSd/cxy5LxE+e3pK+6rsZCI3viinPoDdi9p0N6XPo6BszKphK5HOGX7FWtSqNpQtvU9QqER2N+QMvBmJ35KErU2XN9sUV7uZydCCS5ZXRe0kNnrvYNgsEuunjKlbIeOHpX241aX7DJIIzKa0jfw2qJgcQWD79bvYzYpeSDL7I1oRX3sD9eljoh8vdF7tdSARx57OrkrP6ZBvkmWAosQIn4cMSJY+MlJimOvWE2i8PUYY89n67VoOCR9MlwUJ/T80ZKTUmdHPlvV06zdlhqYhtBNm5y/iETaIRLiIGpIsj2lVy4V6BKXf8MJXl7ZKDXoHuju0JTVNdspuE+8VxmJaauPkteD/BI3hcUbIwTGT6nKvixvDYeUTTJbzNW5nWEzUxFkyhIIF8yeONPNoop4+jNUGY6fkoSzKYHgdCn37B5eV2YwtRmcOzpb4jbQbOlFEETwQtiSlJ+zQmb3SuqiDvoDWa7cKcYRZpT3p9vJcBWioc+HlXymupv24UYqUOZRYH26/Zeodzuh0N64Uop+Y2G0YisZlzULilnKeOauZtRXpBLUdcvJrXwXTGKcvQAF5l62HIImJizorb0LZ/e4t4GEngWFznpNR9TNzt5tw4P11JGoXRuQccV7nZ3vs9opWjILdhBqY490AqnCA1LTdWPizC/23A5YJqcl73zO67Y3v3lTb9nvkhi5+9ZnzoL7aBcJ/WWg1JU4Uq8DlCaH0TQ/sGwUZrC8KS6AlqJad4udINDZ02fsCVj9m2MttdR7sXdZDE68kS0ZQIFP049PPBqshHZzdPD6fo9KeiSX0vqmA3jhgyOoFBvqeH9TO5UfuxWAdOC90rNxn3IAj7CtaG7r3Wpe2rp5XXgVLlQXrUS5jRzFX2SJ/FFpHmaMl2aJReEzaJNIdsD1azgf29Sh9lBL6Z9b4iGLtHE1FqSaRtkzDEJuJVPpho67/UVBcVqZKiZBC0fGKgunmF3Zi8G6Ompj4cdsWHsixUraUjJh5IHsec7obPKlAWL+53cH0kYz0ZKjAExBH2NirgoEqjlYNVCyvNMEkxR3sMvSaDm9q6ONlZYgka5/cxWijANuOkDP5OICnlhtjIyT9jUVyIE8/+ODd7bOKxegZlUElV6+YcST0BqvxukZpRfg6JU8BtFiSvLP6RhLuWARMPPMsgJ6M/oJTkCLtvwhJySLkHGE89Zte01cQ/qLtj55S+cU3N/AxwgofQYNlZnoRkZiJzZZVZ5YlTGnkGSW5Pnt56C7FpazH3e3fZ045GFP2wr6pzjAT+pkO4viEbXBUO4/HUSzOmHAw58lLhGPKbyuxXfMZZnla/i4GIHxwPjdB/pHwDuNw+moJBQyuj3hfvP2lrG/Q7I/vsw93Ya7309I0En2lN+yU9jZgsig/S7OPdHBQrY360kDFsBvv1ESepFlzxA3xenKqUXmiw+JGJxK9h1LtsSXN5eBp5KLXg1J+z+WUUt8v7b9LAxkKoyOwPbyFlUmFAt8TLfN9uEd/ldnV5Sw9Dgs6badoe2lQR8dbWQ/shq5PemFZdlQHUUZjNkHKJLQrmyWLJuoPPVp0etLCzElNuYx1ZYcpL3C0egqeF8zgFzzfHWBkyrYNUdxjHupl6ZyFtbKmKe15JDCe2Cy9bDlkS7dOEsizuhPR22F/cyglWpHCe8e/eCzRn51ny88Hfm+5ZZUxHNDEHbaYImL0EdixSCjdjRZ9Pe5FBI0sAmnw5jnZqv89SgjGhB4IvF5u4ZrsMrsUzEXaz4ciJ0rjZxpuWZElA8e2eMD6LDHwdQ9yDiUO9G4Fk83JByk12OfQXNz+onFSJz7ANiL5Xdh5SaMq2UfUfrmwq7MB8KHBBYtrttHMlaoOPH6lzQP6sIY+PyVRUrn25rWoyUmQ5SZZ27QBF5DD17caGbwm1WsuIGk9RtjzR7o0hNglEQaJiaLaG9g6PXDuUwKCTPrzrsOsEQQvJsOlotrnrVMMfrFBv1ff2fOWz+I+gmvh5UUdPOqblvfXJCOozhd3Woa1LVVbymUUefUs88bjnqD6BLUVpp4VjbszNti2a243mTq6oZHGJiE6shW773WHu+GAnNF8/RcMbtbX1LscKCIO2+vt24PCx38PQFSAKQbmaFcx3UO1WN2/E7/MedrkvzVJ07l8n9bzDiwU5mlMEaHHWSH0yb8OGK25NuBckLKdSn67Oy4hQ0YRArzI2rgeKG2fucCZTwZM/KuKYmJwqG8Wxb4o5v/5NZpsQPLc7FgH8xgJR6Ke2zuklvsl5fpnZHB14bOzeMnwA+eMkMC+trvMO+A5z7yVixhegnKke9j2oTaVvziDGsWxpspLz9gSd/Ds5iMC0+5wT/S3yvK1lk05cuLA2zih7m9t5Tbq9EqIFfefWKPbMalSfTqOSCBkMuSBH5nfxGZMGGe3SENW5r9Esqbp0UDU4/1INSyTYagIzjhFhCVKAn+eTOCyce3zoZ5dlJFYMZgGTTh7XzHcQF2gL8uwwZaRVeoTMJXZmwU4MfSTl1s6nzTzmmKyDRux2NwLu37bK+4LnLwc8ER9hiTQDUZvg12zqKRw7rQBCV/JPcXvJXZ+BeqG7BpPbsg+Io3NId7Xr1aEFaxZmSnx3DLMHPz2TYsL62y/WhC+sVzYudLAz5wuCkkwvZcfXO6yRsS8UQtW2jhnIGzC2bBTHZ/bGX+vB36H0UL9dlj/GAVkc/HpWas4VWyeuMoVZcwNLM5d/CP7MKDr0EZ+EdpQUnclpITEPx8xJjyalE9bIOcE2jk76YVmrILU725G1Mab8vfh8CSSXvZpc+gLbe09Nm5bMSbeYT4pXsmDtbkCTzCKw5GuKqlySKzL4fjdAEAyxPMyaC3Oy5QQjmQPpa7AD0jHEywodcBeTtgjcLqTClPMoGA/sputENacdoaqD0a9iT7rPHJXOaMT8idwYLsOhUEmVycEsglWU0gduoehwn+XP99WoldwK0d+mdrivs4XwZavOfOBk5aQaObDOhA59R/hGiIyFX90hisLka7RcRVCZpsIj8fkGgWroYbj7AfRXzlzQLuZvu3b8g+nZQxU2hF8akicVnpQRyqVH4rWZVFt+OGVeYzOVXSfPjN70bBK68w2HAE47KIMHjFK287yOg4aZSfDdzTQIjluuC/YoSrYl7y6Gv/yhr6iFPXWWeJ7yB14pMVz+jl6OuCO36feFaag38xqyWqUCrfClDdRPz5WrRC1eODWzKb7M9RoZyrw9h+DI52YsOtJvQiaoxjEIHIOecvaQO7TkMRx6buL9IFLffeX3uzn+BjrMpkhrnaJO1XKs4PZ7bu82L+bDJBLcmx+vR8gb86rkw+0+sPOTi0rvF1LryPzTROTcO9wMoRE2gA9UejJkKyuSsFK+gEX3OauykSh8C+HkjFwQXj+ZWYvValSHv6UX+P5oJuTdw4GTfj5ih6epZOF4uki5OtvB5mOae6Qp56mJePMZFWJhhAGa7l3ANisdOQsidp7Blr5+YY0CILJw2RN7auw1Oh6aaYD2FRLncNHkZsvKSfMajSznLBXjE3hqoV/IMxeEr6sI2BCfDFwLIx1P2sKD70HzL84LJmmmnLgKCKlN3uh+fLSU2qfhNxAfDyxPICrzi7OF8n1Uq7NGfEkf+AxDROmZPl5P0sjYNUOyl5AhI9I2Ltp5hA2lK8EzUcAEji2ZnBHj2muf+QV3pByihv2Uw0VAP57F8Dgtp7dyCwbGGxnxM01UKcWe14DaCf6lPOB7G6+JHukAZ7UJCQRphYNhKFbRZVns7JVjLyqowpf4QjTfXjgBzlkcug6saBkesh6EFkXrR8xEXKtpTkg9KQIK7NjnbU2hwS02RCd7rbW3T23ZQg7btigiXes+JWC3LjQz6bajYFtkFe7u7LNENRDApIlJj7pu1uXwDaHxYs6M3fd39XObk4B353nhEWieSPIea8xlnhW5YB9w94wTNVZmDKTb6vkXR+5+7PRNTiGbmBFeww8XWSz8jO/6FbKEdnEjOm6muxhlZtMGm1x6SeovaFC4xMPWWEfMpY7uqlYX8QeW8F5INkz+sLTdGg3VDN6CnDViIgQe3Xv0c2Ecysim3CKGYsar7JoNhESPZ2FJXSIdQ/UlSuAQV2kFxqaxTZVVZd4m0rjanDytOI5z5Rcn7M19VbBAHpvOQmlhDjNGkAuADoBsun8ySNzjLad1aJIBjLiVrIcAWQDQuJxVH7Mch9Xasudt36wyhxVrx4qdBuicm3AAeDdNbsQsHLPHZoeTRLMh4U20NH+3PK4gMoRjSlp+fwy8NoWTyr+vPPGF/vw8K/62LqikvsFgtQFd3ZLmHel/FnP82BuaTJZD0JS0isktfpvUZepGqQ0WIjNdmerxfC+ttgURx7A9zndoJT3Zk+eRgKtt2RHaiRgh92Gn90T1QbAUW02H4m0GTs8xvMyb6y/ep+9ta3A5bP6vI3fPOePEhyNN9+xiaj2tfywFJ5ygu3tEtuQsujPcy6yC/P1R7JC6hBfzYDQsBkVjmcGVGnL3wLChFtc+DbvAzGLtusFz2LDajKqrOZFXxiXrRqTcHqYvWGxbkDzA0fYqAmfgY/BpiyNqvcD0CkKIfplpmTNxz9CDaJqDVFedZ22v6vcDm4a9emfkN6uSEtpPwNjcXTDFOLES6qtIz8tS/DkYl7hCRudOnzyZD1MXaLWpFDepePxicTO8qGmi2sQPBnGe1Qiv8OxDbdllRmOw0/2PQN7SgnTKe9p5Q4lUJPKtDdX72/a6Gjxk9YsPCkNzU4Kdif2ilgubM/IBiCFESqo29+/5BKEXOgw/kVmzCTweVoXfaqnnhixWjKoTQbS82jgeQgGZ6JrXavPxItP0pZSEgqz1CZP5ERbdfTj9Q+YDXqqqvn0HmBjoQJJMks/N9Y2wj6r5NRyWIbYTUTDhQYjtMHtCZvA16tq3/IdgJrpJ4NqekJYgA0wCDH9PjX/LWYLjPSYUleup+H59AMWAyGFCBbdhhrxN1Fuj7UnTXxYNOvyOhXKpMvVYbzTq3jRx/oaM5jfepjU0VShWK8UrRlIij+QABj/SOzo6mQ0fw7me058qNdHMUurIxbc/6DRFQu5CeKkBmqhcJMvFHT03XfiCd41AHweK8LKfmdfpGYhms07b/Hl/XAwjrraC4deUZu4B8982dz7pTD9wlwlNI0N3XfwAn/R1DOreowzTfdhbj3MbeuRFLKjY/T4ZFUAUBHaHZDqLlTVI8M9BHQn9eUmwSsSPEIP8oeVy6kRVTj9LDM/XIJNN32JeWtzEERcSBSORb+IlaUsCQ25lR/jM7/iYn9WBADzm/AEjcENvHQO+2w7+LfOo/bj8twz69GQuP4TIDa5zO6WT0UxV0YD5JHZ14wm6tGXumFemCsqeoFhFUEuV0JTzA09C/DCWPhHmgH5YVdKxJ090KBnoH8L/GWiLvKaGZRzLvwi/ALd3Mm3DJIfsohSC8R/RlHdF0+aZVeg+PJkFI+7GbQa5lSB3R2I+zwB3KgK1QEfflPZhiNV3rE6XqB6YxkFgJzDl4/QWk3tcZk97T4UFwJqe+o+nPOTKl6/RnxNgIHvKPduL2XqqnH51dTKFPGOAUL4ObTOvMOmUjNPil5lOZIFdlW0k+So1s8CtA7eWkMvu/rAOD4y59ld88vWXxb7V5UUiGqY/vyx0pHUcz9VBLj8SW4ldKHwRWT8xwMQrdKazBx6rIe+R0lKJzEgU6akfEaCdVrum30/t3g2JbQzDbmUdGIKeewJMJfivp+G5gUoM6ppHVl6PDZ/TqCTu0xBj4LI3vIxtmj7Y52ir1Ek8FHxPi8+cwMqIpOtzTay9cZ2xelkZ0h3jJn0p0hbitBU5KSR1Qzv2DLkC4O1b+Cq5f5w3/7THQRTA6xuSc4NLq1yJ/lQbV0T4HQ0RIqXxwZhtlSFfliUCcRPSPfQys2sVwJiUf4dTXFbY35JPWkI5Z/5eeq4ZE3uOcAbjnqse2i92JX1it52qjx0nD4U9j8ecnrLXPU1fCOhfUMqK34VMyMDOy8Y9w06IqxpNU8kZnAUXKusHGV7/IU/mrV6GB46IG5uGtK8aKwNl746rOQJHD3JbZfxcnrCF6W5UYL+naNby/r15U35m0kfCGMYMMItzkI0G98c+E3vCz+H20VdDK2cwvBBjoXu8hGj2eV7PbImod1LPukDRKPnpAvA6OGRJCEr0Xw3yDVTajbSdXHavJ6Qe9WopWo8kfnNqQK2XGZh9kNryMqOniefRJ9E8tW0EhU5sIVmtS/9wAvqmnVwYZSYw6mPivS14VKZlcDVRezRTl6Uu08/qc2yXIkI66Qhl85Gus0wOFDKDWs9zuwKv35UXZZkqyb4uxiCtNPB/s7d6DoboMlzgC/9EaGjUS52q2uT5ObmCujNtb5/T/PY9PGzTTLyLkMWYF7djkJrsyGWBgwHqQx0e4RKmDvXYxeqKuvSAxWS6EpkGczuZiOnfRkMqSZPp0xHVHWLEbzsLP2HTEgw1z2R/+xbbjXa9/HV5T7TyDEv6Z/wCfEWqLeTtmzigkc6PY/bz0tx60H9BFrz8elssNpjs5erIMGhK5KfkradCnCw25I2UuBHJhPxOiMEQniXv/vwnPiz3sXTmJwe83qvTILtsuCyGGQMbXWrzkMxWZuroBXQNaUgPBMQ3DesLy6jPY5QNHgfzdiEqWsvLi3PykhuVyU0xFae/0/CeSkCkoZiJxbxRV6Y6rKOZEenlNqFcxS/7yYHOUE8k4kCYXJjEvfj3PviB6XYxpnagNl0xAeSv9WS6ofDLkZl04h+bUuEmExfDOx8Gdifyy1wGh1rSlPLFIGWYFrsIyrth/7Z9jyNkbHMeppXwrKMjhEf1MdCmlWJH6ubMV7dWENNbvm6DLmVxyNiIFgy8aeq11RE76HC0i0txRTDCQdb8h3FWmCAOmLvrXIsD3I0nYxv6yYL7HFimFG3vc/2pnMVdcPsiwBLBOHYkuZuymwU5X3oGf+1+9+gE+0riBSwBNxCNuLZatVhoDNAjPWhLHTvmbScQHKcbujmyHY62QXIdvPwL2noWaTsZK1PHwBdPf9R6U08AoZZCKvft+xWgkLb0HgHGRK7/MYOtwZP8PnxRQ9QAbNPScg9/ofp23t5B7E01EfP0nFu+miFAxqK8zs7uO3qmocwXxmDfdu2RYR26sozFJtiWrOAyouxv9y34E6BKmCIfOmCe381tq0jGS+TvmlhdJOBm3xDxnGjcBLJmVr1NdFfieAgA/2FIHHlTWuhQt5oycWrkkdYYbw4i9B2ll2Xn6xiAdQwZo6+TPATrBqMuxB9nHDGC/P/BN0OLTv8itzK+qaaiRgRjyW3ZcJk2icfg+uDBfCjvdWbcGhOmjT+VXt646fmNABIhsh/iCJ9x7Crr2jZ9uz03IgLDh8rnKMI4lj5HOc4RgVx89ZtJMnjuB2nMQScCm7dkDdtQJmkSPgPfMQPwGUmfgDh4jsR+MhJoMAHVJ5peCElgzA53tLs97+2jZlDV+aYOBydjFhQamblEtnuuMoU2IUORXDvdmY6kJ7dmJCAOSYGui+gm128mM20V8tHVtwkmZx/yBiJfOZQPNgdfez4Qm6G0VoTNCLbkK0HyqlOWg6xlbn+bxwPpO9yE+AIFe2mckY7Q6vEbjvN6rqz0kKttLSmUcBkPESNo53jyGrUFF1GC4VxmI4+J7MrbLEydvyNIgd2n6kPdezqLXtHOQweKDwsG+SqDznjPC0VmCp/DNdaj9jF1PF/j/JJ4gH/PrTqQ3EtC8jclObK/nfekYCPK4xUz7KC13YjBElK5PXd6pC81RNDlmuss5UFkwHxOAzwzOP6KC9N4UMd5ExqNTqxjBp67+YR+idCsSax5D5TIEebsrGeC5mPzVluKTYo1krbb6d3tbRxMDriYUj4Buepi4GqpTF7Ujx0Gorxnlndt1MR9Kq7+JjhmzTfu5e+npgdGJa+fn96OtSCvTGQ+dtFlMSVmQwD99bOxJdZqpEZzdEjoq93GWopAIaX3jf0xv6pN6p+hxmWuKFn6tfNjnSz1vTqIMRhuAMwH4j/ZO1vfJKd7pNdxLv3sernf03vaiLTXpuRTZMR7plzsyNzl55WcTdUcQt3Nn+0BjHuS9XsTe1Gn4eVexjS2esXZ1eTPgxGXcJELH3VOjrDTyLKcxXgsBRswKQ6POzUv5DpZwddUR5Ojqp4KmQPp37YgcH2dRRX86ETvtsd3qrgXEU+f9vvxP3p31gvrskll7Bl+XnOAdWPfxYguYl/h2G5HrxV7baiHeXFvqLDnE1nfmeZQ2jwV3x5qOPtBvwngnYiFzF3HmZ6Obgr2tcoW2rT7efUHia9NFIm/fdpfE0WbrPqh1ai7+l610Vdpq3934+7qsF+cICEjxhZ857Ai8mvYQs0Jx9saAQGYoONid27Mz3xLxqXKSa84cnxiddAJ169/D+uPO0Xc/DlIfcRX5XrUesrNuqDB4Gj5uS8K6Z0QE/d5s01V5rridyQH1H4d4ZsGMclK1hGf1eermeQR5I6Bg4TgJ+bPbheUbK7k7+vouL8NFrMXME3nnMIkx1h6G5vxJaiA6yu/iEH2HthuKSltIU7fneyrnX+YusL0HQCLTSeT3wxIdQKbpaB/uhu9X+5tzL+btbRvyXXgSExyOu6U4Y/8zbEVye0s1M0VoeS/tZmAm7ssbJGb4mg/bylncn2DvuRvd159Er4mptSC0dcCVDHvTLbShqpMje9N16NVJahjQHvcR4Ynfr7zevkW/YwogBvs8BB3IvrMlsOMzM7M4/vvSzcSbWfzWD+OwWvLZQV5e/T83xX5gaXSDKMUWjYoOY7fqz73iedUc0m9IKyf/v4KH01zpSpIZSgQiqS1W0nsKQ/tJrLQEvVZ4k4SFZSk15CdPNtvpC3q7Q3bEuSvnjgTqjNOZdx2vIfIA1stVWbJ+q4a9gWb5dGmV/Vcxex3HZxhx/xmkft2hooWNbFmtsqLZc/JVyoC6RHdu7iFAaGOUzI0l35IBzr+vFqYiWrtTmWPjcQgRE9yi1J/ms/gb5MppoqT9pHlx120X451fBXy5dL8baWVB66pM1KZI0ts7yYFjNDJYqauJAg9ZS28UvVzTq/iHPpD/pXRfo2QOyYFwKC8p0eaxbpLigPiMurOECnUOVD/m2fUaGhL+sgTHWVmIyedXjoTH1TpFxkQ0/ChrldGlpu86sLjTR8SPgOR1qhFx1xI6eZLSxRUDuIXT0S1RYMa+rrdQgrHDDsNuRH+VObXBcx5ddUrzt2IBXfbeB61r9yoe2yDBSSEU7veuGtGyatmwLwQhs+QfCC7K602rSN3FZDfQQ/5l5yWEeV4nTWiM11hvhNj6XgQL6fqspZs3tc0y1h6oBU6BBq4EgRzf2ap57pifv9uMzrkHbxrvqs0RtOnVgmUPNjKYPeNNZ6A3RiJQbS3wm7rwYGLnLjVk2/J2hYsoIvkV2I4XfCDjnSaGZ7n3hnCRVzP5CfuqorV8raiVNd0s++hZjQAekErt9yYNlE9OKwpuAK6VMsV7A5E3AzY0t8G9MEp2pSp1Qhqg8csNEWIuvTXrng4OuaCJF7vX/rVQ3JDyVZBrhd4NwiCU7ZeJ1ABO3ey3DWXOy0RP6OjxIQoh+PVkSZ1OhmhIIZN7J2Fr3avEGGe3iFT9QZgTxIPhCgNFpOS5q/Kq6IDyJZnwMZxN22Yi1UZGjtFsUoObQTeBJrfWJbk3LQcg1z/AoBhZp9L1IZj+o9/Op4D3TNjhVB7/vilk56tN5rJY0l8JUmb3xlO09DJ+AemCle/z/c1uPugWOuYr0xuuCtU+3MG71GrDORNPKbJoa6vvPV89U6puMoTj1IQcbkz3sVj3AfNbDECkRPc80mwvf7sj5AeTnuzsDx4+K986RY2jdeaJxu91pkKcZEyirSMqQKWQSsT40T4ssg+O6wxhUPZJQg4/UqGE5YNJHY2kuIkikF3Z8aMrX1z/vLtzSaM5eylD2m48ERwpvNIzrCe5zZoRGVdy88tMmFm8cIvYahNwJuX7nEa/bKzo4qW8XpLklfI2ZvC3OBiF2bWtaPgRrz+HU+hSN7E2OcOVFJcYQa/dv6WizhjumQE4TqXJvr4fxf9fx1gvPKpk/NBfJJIrkW8I1MkyqyL9ePu+cmq2Tu0pvWZ8qNFxosMnuvv2rkpceuT3vhZEYufydMbjlYs+VCaUIug7xNlzRLZfABRYEpTEf4V9h47D+tgmua9nK3qtHKqnWRZOVt5MCgo55wF1L23/urBALMaLwwHkaLILzyvTYq+7+TzQjjiorVwiO9p8QtIgCTjhAgqzi6xD/rr84ejpc3jwQUhQf7tvDrUmd4dcAAIgomBQCEBPvqxo1AU+wUYxyCTwtmQO3HfgDGVUqRC9R6l5CMDeNevzpqGRTWgfSvIfu2CjsfkS0NtZrHqKSImLzjwKolOm4xxVZpk6zPIwq01oiy7VUMU550lxmwI/UZMQ4sGICx1D7CNa5p7WIjqNyxDfTlkiqCFnrbFDbz8E3c3TEVdX90cbjKnMacCYWWyCtPVIk7Jm7SOLM3xOEI/9st0YA5/aMvpp22gSQZo90xf9gCQbn1OhkLepGhlQx4eH85AM1y1fJOIdLP2HhBp6qjHaPjHHivX0n97tOynMmbYm1AKtgZmYCbk9NPIQeSH0V6a+ix5zXzKCAHhSwkoW/Zh4IUI5QQ9XpkH+BpeoSSOsOcBWSl1Ocd3CfsxctgaLJO+Qwrzms9+6JYHE7qQy78j0eiuBnoD3hSML3O2BPi3zX1CCn0kVwawi10cZis2LRNVV38NHRcBEj7bFPOHeKHDmjbZQ0pCsHklTxVxPiBMNtqAdrAp+QTSl9A8tQ360SvFpGNLLfQYnAJx8dwswSz0sB9o3+JPrxLvS+70wUEssgzb336PeSzW9BIfrZnecTbz2m0oS8Z5OC2gZ1H1FIE7j00mIAxGvLeh4EfIX+BGXCBpot5ZOUP/tbuSP4IJ2G8uIrJRvCy4GbToNyEFcvXdDLgBVkNque07ndeeV28+sC8TaOL2BAGLiAdJ0EFES9EQgQODKAOgiRXClmj7E/sMjX/i09nyME8gPcH0I1bQ4GyGN0KdjgOsc9lnRUJahYBDIYMSeev8EAMGVTpemaGnsq1ViiuoQUih7eEHcLitPq2JCHliR0FbwktHeT2cJKHpKofJ5is6/GRkmBgBMYBHeS6iq5d0C67qQ3V6TSJUejXgVWvSQCK6+njI2+rNEVABuVEeR5cRQJMHIifHsD4RDnb3JzrX897T7tHVjXxcfvRYzKKkrUDiTqTkGbuKlD6UGO9ROJlbARffsFtoDCgHnTQMVjeFzqKdL8a3Bof8TI9z984COQzYGqASt49PZtLL5ZmJHIC7+Tea2GJy4L99durr46gXPr+IOsU6XWxBWRZC0uKYmTLIJhToq7kj6glgb1NNCVR/M0Om7dD9bSwbvZHTw69l7/0GVKZTzjIw5jeioLuI+qQpwCQPENGSshVk5oJxdCX7AqCcv2sQupgoGQEs7w2gD5ES+XXYwJwvXtV91RcRLWE7s4UOjaDUc9BhTI0Zj7zmSijhUQIj3Aw5jzy20iiIsqCTRVDXkdg/1oCSU+BBNQ8FIAi+WbxGvYCxwwx/8qIJDdsRmf0GTh0o3Om4zKneKjXKl0fkr8QvVnP6EtCpvXSYFiu4QXOvagExer8wVei454IILVLYy/osdmceQEa8FYkBrXrjBH5ejHL70VbmrF4tcAmgBirczyMeQN57JOsJof7cgYmVomANh5c6DsoXFuptqz5M6DsqsxHiHsoN/bYN0whBLniu8ImW07LtXbVofhA/YbBUL2rk5pBKV4iq2kfCLv6goZhbQRcYGqsYO0AFerQQ6SvBKsFndtZHbPRrrnxO0RUNmP6gMoVsrI65BsLvqMfuaMFfg6zMD+RFEA2Wv1tgy/Ittt640MWCTu60EWnxZYAgLNOmeNXoUb10nhESJg7um7T34NXGlQgxT1pgtCce+HYDcY4iPyap32yYZDq1zW9I2rMaJ3tEMSzA2cpH458m5gpNjEeiH86sCJ9dgRFRn+d0gC3AvqDF1Wmyok9D14OingevWYPQyMEUOvLQRh00MZgLTqMW1Q8PNtqfpqdP56ojJyAb9QgebSMmWPBcsYCZmztTM4xz+vg7snIj5JmAEumTIgaQmuz5M38HIeKuDY3wVZAOaqiC4Kstvt+0CuEsK5t3m4d89aJ3dWSZbPcgFZPHnJ0LhX5pYYs7IE/UzF2dc8cDfgppnc3qloujACoH7gsTD3U2CZ3lez3D66K949lgIIuyVLsDX/y1bA2q+J2zmBQcKQ+rrigchQg+BEMkGqWnNEcef2mhkp/oqBRVso2/2fsmHWRVsS226I/IwooNDvWvpEi9Jl2G0VzUWnRGKSDNV0/5bLQPeD7fHh6sk3iDUP66uxAuOHRM3yD34SmLpnZ4M3ieA6PZUpn5C8HXVotOBxjz7qkSkRbAhNK9eZNhM3VpMDbA2GeaByce9l0QinJwr/Mfds4IYNYx0SWn1yfxZMvoCWErNDCXfcjH/uhIRqfSnEJzh2zrK3kdMfFxpPjL5qFZfNtnRCe1NuYLujAwVvcutoNBS1a0vYdcWxDnrClfkg7+7gGKqIUcTciFe00BQu6IzTqUIn+gwUdGR0gooutHypzdk0CAtSSSql0puRvStHfwFTS7NVJbbREOoe6hdBehQrxGbX2yOB7NdOt4sncokkVIVv1bk6JGkiaAu/eWtTXo6aBCErsqLm5GENU3LcW4ACU3oGDnIFacVuPceA+ter05yXzP0CUKMtQNX/QycmucTrJgyKRHZ0B79iHv6sJz7O0W7ieQOW2ME+GbPUZE2SWrOqDeKDQVccFUCo2K0i63f38mg/FGcIb/OyWC4hKf0nEweND0709kuQiKcHH58BG0e3i8o6OgXEFSxQuT7u+2EG5Kahd2r/Vw5lAjwehnBcaE64dFJ7RbjsBsot3XRz2zTmeiTolqaQfngfQ8n51MOaYlgH5FVFDy1C6YsCd2v8hmBgTXV7Pm6lDZUv8u1/WUNd8DMKo6x9R9d3waz9yQqLgku2F2fvIVoSoJgXI1B7lJ5+GdRX4WNoj2guWwp1kb5kgw+HBf8AC91NkryAn2gGXAVWPB1iebGHl13c77VjYIadL8phN1rvMzg6dTFDIWBwSZGCBX0B7UpowrRm+01c8Am8xMSBkbK0B7IqR9GPCPvhvKtHnE3fHKxklCNaAsicoNhW/nt00sn0gv0l63oB2gpyC05XZ558CMd3BKnjZ1keaQHub5+Nf4FeiB3DCZ3QHxQHMtkCpYxaAj9IALXXvzidv1v2UyCLRHE8HbeI9d8zMC3MIaNyWWgbHJgqNYuXTSZ/0Gwu4q2iWFJ6MBq7+Z7KEmA42/EFktIhLu1hP9Zg3C95XmlR/+fTSyRsoZ/W0B/1xbtPulUAQczA1Bhp/ZKqtA49jpwjahyrZm5Isu0qNA4QHneVa9oEe+2ZJkkjuQfPPacTg+TBwhpBUMh/yGSNjk9ij4gZ7EPT7UAqlzH3Cmrg799Xm9A7MB90wtJV8/a4RlT9CPH9qX259BAn71NasBCbsd81yImsgqOBzOdlBfVnQCJ15QkaCc0vn+7asAA8CHIDHyejbNppqZms+AjoXyIaQMLwf7gK2V9IFUQWkz3PYA64aBxMXfsGauT6MdZqp5RE6SiXu3HdBXinrpgHmnQ6B6FSQ9IOCa2XSsbxezeYA+YMQnvjny8W2IUhMAmzrg6JBqqNlG7OGGk1EiNYQ+UIj4K/2bNdrjpiY6k88zG9cMUi948f6ynwIW4aTVxt2rSYoROfRmz21VdX5Bh/AayIOxN+Um46IVJWX8cKkkFUcNGFbELvs07WHPetrEV0mRcrVkSleU+G8VRd5wU2IjDmlzp5tFwlnNU1pCnx4MAET91tCoyvJqjQwK1xvOCo4Cf4JOrNzFvWFWdBDAcWhP24PaKmwx5yGOINeHSGPkvs10vGBWUy7ZaetgS3HTC1txBoC4uly5gittkt0CI/UsGPQGpv1GzuUBT8+nPjnvmB8wonn3kZvxVVQc2ANnPl0AZUY+GM7liS9Y67mgOHWDVqGvBuf1RMQp4MF6/4yLAPCG6bhH5OdDL2kWbM6ILAivwfTRfzoyg1HYoUDg2vlu1i6YgEZZOFD+e5yjX9fXfCvnxRJEfHrUp74qEsSGgtnPBnELpcIIAP6gvL5G+Bn8n9TM0lrCXIudPOJim5pE/U4kPm+2H8GJoBewKVS5lpWC8XlnwUEj2OVMg6wGw+O5LQQkM/0qSBOvi55khNLdEhIcUfCAgeKpUB7rWDhGIlCJ9fzMh8CORd1jWtOZfREKEh96vBVEGZF7PjsoKtOrQsBgLZIcwbiOvghVwJyAqHgkf/CuO8jq07coRH2d+gNhWUy6zPcICwcxcCC8CskG2UDlhB9cJrKO971UdnURuxuB6AOO5hHDLZIKeVQImhGQpoSsqfmDeGk5hmiITgxVqaMPUBlCS9paVGANeiHByHhoQpSF07meF8vrRnOzZ4J4njByne4ORKTjFI9RdxTZgvij3j/0UEvHNRJ/swdHoUXzSA3rxa7i2Y+u5YswuBTTfLiN6GxwpRFNIcLBpyK0nsAkZPey+BDSQxSETLd5MnuXAWsyFBzsTrNOaYanlKX0md91EvDf3KDOYZJGOgN+Lux0yszdXFHcpHghQfvYdHTq2zF7mIm7iDnfxdqI2Y68iYUR0KX0SS37odYLHQYe4wqAyRtbZ1L7UOMWlfFjI2jUUNOmtIQVbBLu61uZSCE+l2zRnyJE4fJtR9ALcwRnjtYyDXtB92jpguHr3ECREfNRfnQkgPml30eCCHxDDlZGY4c1Ij8n8JEGSpOcNy+SUlvjdwd7j1qT3ie4+KbEHS8YwQ7DVtyf6jRTEw7xr8mIC6n+Apm7RVv6PINOQVhwkDNhUN/a5KhgbT/1m6KFL/fqa1Dz7+8nI8NXxg2IfLUeFNdPNw8mCACvcuHgOPgBVuLalfNrWitlAk2OzItfAekm6+Ajhx2WDNm8aHchXFBkkkclEHJYNPgND5Qyh+RY+W+LwcGiWdhE+zxwdE0FU+EH4Are1JwO7trFwbZaF+56cYhG789U8CNVHNCLBNKNJ06ZZmU/2am8wztrdg4povUTCGTxm1brSTsiNpGLO28MK1oK13c1HsnWa2aXOrh3HANMh39drE+ROEDElzJVtdHE87Nv1NBD3+9IlEJd430utjlHaeah7/2UprbYpisQTKfp3MCv2heqikAN2B7bBkx3oA/o13WkCuwolmm5+iFK5mP2tZlRZEk1Z7PMBYv1q5VV40R16mwkjovYxiPHqK1cSbpiP6BgKdyGPsoW/B5c1R7dBRL/R51L1OZOFsx81id4R2kY8YBcdL30PfmCHhBpc0cpTjERyBb3c1bxdwthDJUxkQK9kwAJv2qgpHMHBIPrLIywpg2zEGwRSKXGwqKHzpgyO9j53f6bW7tUAjBDH/3q6MjOg5jq0HfUreRMAlQLQwLy1yKn5O2xDq4tfkfuEwMc4z8jGuBXKFrFE4ADTYySqXtlOgOq+XUu3bqAJyZai+uTv3X8NeDYwBac3XIOh4xP1rEhVUWG4ScmN9S36H53IhsEXHSgWrhWr7gjQaJG4B9kv8zwKgHXRoVOpHHqK5G/1H5wm7IfxVTpN6hhG7FC7DB8Dh+udFTq6BYvdv4NvCco5fhX2Xce5fWHP75yTirx2XVfI+J+2deDerM0bEiLqR8POM0nKkcMQKErvPvbG+bVrv/+7LKXSpVDacBXQkUmc8ylEAQe6rq6Qy/CVdPj2paK756/gjVIDzAWka55o7ivkACg4zhaRGnwli4EaMtwaPUgsdEAGZh4+znr9SQlIQUz8ZHimeiKLiACtOLoIx5QS6upGyO9YFD44D1Y3MOtiY+pAuRVImEkz8837NNrk6OQLyc2Bl4wj7IF2GCXTrTIgC8mHb/9HP6lIBOXEurFCuFLrJGsLcKGAQXXJjW3GCEzJJQgDMsXGzhzUl/l/eN43AQi4uTww4HQDePAJIDLNSW/IKHiKJc6GWZ+Q9I1qRiLzZxuaPon9+LfFpJhrd9WbuJCj51HLB8aJU5b7r0a76s2iM6fXVbLMk7YxMVvYrHTUnLlajw1rg6uA4vRdIfWp/uGiHyHesSHyDfnEHAeAzeb2qDB8ojwBsyL1mYfm0hu8DERtJtRQ3YNHIHX79HEEfE9K4qf11c6ovJTiUrXiRKH8SKazBQ4vgAEhH1hEoWkY7e8ZDuVL7h5D+1z6E280mU5J7Ajjqc/UJY9RvyQBPzMU7wwYzi8+Q3hsGJdoIRJCCTwGlAwDDVZ0iQ3Uvv6fcrkciBTboJQ4mF61UmlBcMgYKZtRC24P3JFzCQQIhEpsVSxpfHho5DeiUOa7NhaisvIZ61RVODPH8zbOJD+DhLV2MiqW73FsO4S2htMzM1U5TwJl82u6CKYKQJxMpXOt+KXe1VPwwvrVAr3KdQB0R8nPOJmUJhAsvaTLqtFpX9H8ua3AMX5oFG3DnK2Dx8trbYXcRAzOldbamqkmrgzt9ZxexI5vxw/5E9xgyrm1D0ob9p3xEFqjM9HCXGHDH69McfGhkUKQZJKQYfGTBA4xW9sbgKIrngYHD/gRFZMLzy3iZlXBnVYToIqSRdT/kEZg9DHlNCob2RIz8LyhYC9ipQaftYXPAvRAl43EezAC5eBCFuIwRznhGkWACN9HoQvzJiHec/N1/iRPLmBDvglHtV7XYMHPmIcHI3E0dH8ghjNBCO7JlWo4mcdKPp5ldLqghVYfg8WJRRT7zcTTdL5GTyR9NBmD0gfFnvyx+lGjw8wGRATzbzUR6hAy6z2hXcMDj4cETde1mYD8TqzZg/ikJk5upppq/fLzxkf8p5SEmZmFzmNFrURK+2GsMhC17uLbqa+QPsJM/xvc18hk/k7Nlz6q3ZhBzw7VdpbIXkGzChEJXa9+lyAXXWDHkBnO0E3huOGN18mRY9xyA64KIvUmNl/s4Yn1eEjJelAN8M+N5dBwby5A6bTUW8UXUtzvrfYhYcz2Ub8aPeG3s4SeiWoNSAuq6cskSyFAXX6Hb7Si+D7SJ/QQaO9uQaNyjFGzpKd3bXh13eQ/NlEf/JFp2MRyLCu6TXRegvmfNgzte1MiK5mt6/8bHsqARl+L7Dh75CEG/jZNtBoqSmwwAtdhL/FlajBotB9bQcHKmDtuGuxaLqlKrdh+RY28nsPgiICSk0yK8lUlBkMlqDvUBJ+Agc0koP0LWSofqDDuSnU7JFyYOXp3PQWzyoCTyq0m7x7wiAHIhnz5QF9aYDluJQVz1giCdS/3+cpIL5wDfrisRkIJYhMEE/DluhnJ2gcJzz4ebLzGpZdJVgKJuQ79z5bx2uD8fymhkDgsw8pP95SUa+81kWzyvq+yIGr4OtvDNFnY/5q87s+5ht47lSiYX3OGhFtCRKI7s5oxKtX78zCzus0a8wnVRFaXkZFfWbPUhbi0yQmSV8kCKt7gFJMOkdcaIC03cHSQc7LKpBnN9J4OoJI7P2HwU2r5rFDK/SLozvOb+VJF1+C/alMbkFU5TQQmcx8sAjEePF5HlDiryuo+zcjOCA1FxloPiGCmu1+8MOrR7C5D1Zr+CHPxNFp9FUoYgeXCmMfHFLF0NsifTyIdDCG86+FEpnA+loYgwspOIJIJLD2BQMcYaX0njPKsR7RWGzRlNNy6wFiEA88aZtJnWqNQuNv2lWngfTm141v8QfcO8Ht3AIWDEdND8SIFh4lX24PtvAm1a3FEcRHGPI9SiWjYra+Ax74Sb8tHdShYB94iHTMjsmkVgTtezriP6VjO3s4bgBX1UUj12bRn3CwnkcQf7v7eFfJNYm4/7z1tVfQD4/CvcHc9UKKrGncrwNJ6fUzRl0Qsg/iTOv7jZuAjbLN3NFfOsj5ON5dqIePr0BI5Buldr+LHCWzaamCgPMCEJil0jNKJvdQKZ1L1B9fBPCbHtYClLNQbP1eqcmq6f0ROcLmb+tikMg/zKQ3xbL0HqJSV0+R060euwBwiAE+MuwX7pvewvU7QaRq43yWbYWPGzYp1irYCEcMKzt2wO624P1Q6zUesHvsWAZ+Nd5PE2lvJ2yFRGNwm2NSw0iFDh2oaH+4U70yD/PvTmyaelE/LPA3YXJEEU4G00QtonFlB2i+yqcxdubB6BRMZMglQIyDoQS4IbxloCcoH5dQCL3ifnkdnLDYIGYFMrb5RUGw5uZ8++JZw8kJjHQa/Y5YXGTbMSR0ZtIr+sDYl3uvtkArxfX8XlriTSofY+ubkWbJqz/cHFK7fJ2bmiL1UbLhBp2SwZM3UwmosYyh03sYJvcMEn4YGsKRJOEMiSYT23lVQ45h5TkQQjLouFO33vn4yLLdGVCEF+B/QLNnVjrN4axCT7CM4S6ObxDxNjx7q4OOAE1M9SRIvEDvXxqEGkhKTnKx5KTbNPwsyIvE5Jn4RyZktFJkY+4hWLzjIeCqA41FlGyquD/nhvP5tL4XtjgGC3zJMTDxRH1SPtaTcM7DZQya0Nf5lO/gxJQGv6Id1IvD7w++ZW99dTY0e8gzuJ9AKTDepLTZ0a+NE0/aF1/6XBoeHiW0Qu0Nwdg93x/iBJPvtVIXC/3qBIy+sKIp3/mTJtN8rwSG+bTl9+FS5ZawNT/qU/R2oEUEAbD5tmuH15f2d52m6OhV0p5en+gccGGomzhCqqjfuH4aE8ncm2nacEC8dNVclGIX2Kmf4A6joM5n1W+A5Vh0AuS590K9poHwUTBsrJUt5++OsRzLKd8f04QxDxLDvopTtbpTMHAH5UbEfRblbg4xQwQv+zm5gf64b4InR5Fn87VvMPc9lh2rizbFWhdLlzfgnCO4QG6W/Y6BxQPupKZq+zwj6ReNmV6XsR6FeQUlRtFgdmkcdpBUwJevcmr0HEti+xJYiEFW/GZfyGQ/yIXunx+naLhNQtrtP+f3ZBJgePV2/r0UFBM1gAWKD0kuvkunRe8Zi4Jwuk5NxHYs+NHkEbM99ypJsES67MsBbxunxeDr6607BC22dAp0dIPWRNFzwH6vpM/xDH14+tS5B1x+sgU76ZhDn2QRC5aIDtvP0eDo1o5DQjG6pahhCoTFtdxf9IT5RFFumaNSlKe4ImWdHWJInqbK0DD2wQXOecEppVbW5CYDE+jX1WYnSzBzoAofI7KFDVncUqM+BLXvWX5a/tobxqqKE7Z+2ooRcl5G5nbqjj/65vyxZxyWvaOSDGC6UjbZd0p2iNaZ/YAaUHHqCwGWn+oN827w4ld0ogiV7D7+dEKBWGT5BBwzS7aTQpBaFezHXK6LTBpBRXADZVaEoTBbwS5Gf15JKOJLQesOIwFotu6LOfKMmOLk0yMmPaGDvMsMaoDFe43SE96OQNLoRP7BUW7MkwO2CgnNZc6E3u79wNmeMHCzwnNJh5TDLvLCSaDqDH3fzrmzHqe0NO6SUMI6JXQI+pOjGcVsntgcGdFZPwSJVma1uwAwBrWBLvAln7pqPgohd420yMzqGWNuEyTTcZaB6MfKVmtB3yyUpMAyZYBiVTPQpUahg2MefpzXR2VIVP0wy2jkwyEdCMq7uf00kzRBcClWWfEjF6coG9fUknHzRRIsCC+ouBisIGPAV14Ar9014nZEDRxrgCZvdxn2oVj5pC4KOIuGDPxqW+4uzn3gfSJJ/QYHo5aWo7ddjxKdjVy9+ZEU0W+sQawpiAwHrnnzMj7vmAq7Q5eGdUe1KL++JxkeCL+erxoymU1AaOY6kJ05ydZs7KyAfw8rpH9GOCWDx+lKxDrjeYNxxkyiFoCTq4GgsYXLvxsLWc3nNoLwozJZH7KzAfplpaCW/2HptaTSN+otYdTUn5WvivdSpHSOBKSkNKzaJMMcVMzju5khvrGVtLmAifCEXzYJVq0FuHkioldSJ898kQA6HOhSVBwCGsEB3k/XAMxdjLEV01LBilDMA397nImK+IDFAhczmiS8u/eUZ2vi22O2DKDV7tEDufUj5qxKJuYMR8Y6nRQdS1Ecgsa6dQDGd6dqMgrAchIJMhsYmMZ578z2O8IhjPmqHGHudx3c598c/S/msiY9qhHKT9f6KnCn/2AvWgIyY0MPg1ftKbKFu2ncyyUk0t13Z4XFENN+lB0l98P5POVQ9uVGzrK3nR1Q/CM/6NFhqhh1ovB1qAT7xDwHs8V1Xvj6ChaADTRJL1VVzzv8DD9NQvEsIW8GlLxEIi53bOfjjj5JZiRMcNIHAR4DHCjPB/h1AFzkr+5MdJNktz0sFM3NvGnersHHPR8OUjO52criC8SUHFBeeArrKP1vqfyAVm5znw+g5gzB9kDkvpEsASkvrC6AG4VuFRjjkoKfhEk6G9jKoBGih3FpeVAsX9oWo0NsyiwPK87K5PKFG48o50yThUKRXD7Qzs1QOZwHe4+uou8IANaQkO6DLul8sbPoz3+0Utqn5Dsk3acMLafo1FxHkgecfZjRJFSrEKqpQOhCLe6lmOYDbE1tF4RwK/BnPP5W8YzOyru20Y3yKTiBvChJswKut3qnM7FWnDGXKeEg3oxP+Uy0tp94vyPdt9LrHqg+g27ko/5T+2JAllzOOIOf6N9Dh80pm2N9moSbEYlfk5CLsEsUlIa0UQV6LjH3CtujcfWGWeiyMgKzvOshR3qIvYUfWB6ledtNDKXLoGz+3KP7FnCDiOWchp4ocBr9K5pGWlaI0K5CmQFqOO6OiYI/2Gv0Aq2wGKxQgEK4MdFuUkbDPtsZ7UWO3KyhSM9+5IblqFiBeKvcv8vCfkqPEgJklIy3SYcGV2OZLu4HXgjhBzecH19VdL1XmJzXyIVNtLbBFJkOg33tqVEKIySzEjR4k0EByQi0+wAqUoq+1ENcQW9CpK3pIxmyuUXnFuvqR5UcEoHw6FUK4kfLjQQ8oHg9n58iYTVj4YOWGH86zoKtHQD13Tbbo/KVQgp/viJ3j/IU+F3Jp0xDl2CYAnChQQVjPGM7IG0K1a6x/SvdSJPUKPJFu4+2zUx541RkgmMsurvqX7vur4nNahr29yN72CWEJQBQFfG8vv5S/8NfpAjtsmidchsBResrqXo5e9rHIAdJOEKJKY90JovRlIXk47yKaHwmP4tmNTViUxZ9+ZHiLN0JMWUfeSRS7/ySCL/hxlPADdJC1yx/6Y+s4dY1KobKPGSES2BlEfrlUzLS0iQBLG2syKL/sHjzfVYWNvwBZFKCMZhy1eBuTV2MFQ0xLoxtkMJGwT+XI8ArqONPrD1YQbmfuyJWAqgb2iT8HGwQOzNAC90sRNTBg2ciYnjsR5Nho/AkRrIi0Wo9qUSSOqS+v0SWBdcwTOUUGsyAlO2Jkd+vlwd5mi/2S/L0lFkJnEDMY4TMRXbR74QGpCYQjoixZA1BQHfWPnwSOKTixN0VsJRJH/RlGg5zsRSkLwi2sdYzgqA+0B1C1ssAD+G/0Qn4pY2BG9j3HM0Y8j2JxEv6xr8ykqZmu/cGg1NapMh6ab+CfjwYahfaKnwlvuT3xs80GFMaxKUacf72os1pP9sHOFCOrAUj4CGIyhxeyS3xoyidDt/kPEH64sok+cJcdVGSKKk2I0uk/Tf/AzAe/Tpyg8bsQ7QEufoOXWdE4jbqA6uHEYFx+lvh4kX893wl9EjiySVSwCkroBJKlTql53f0gcWTpycr5+L3qdrWEYQA+7hhecneclyRk+QKR/amBVNhKulXecETtxmBS5YoCjDmQal1KOBM9GT7ZxU1jN9LmSoYuXJ/ZpVG969frVN8AvjaHn6FeKxPQRpn1u2ZQFQeIqZunhEo+qJkv7EJdtJ5GF+nX1PWZwRoGaBpqENykso3+3/OQQvwk9SSvukyaL/6XF/rBW/8zKRs0KWy8buZaE3z8vmkbmVyxtA0JkijAMvPF7iulq59cYw5TyY9MQ9zSQ8Uz7e0hJXJ3xyzOk5PHy/rB2523DJylDImXf5QRN2rP9Wh9zheE6RDEuT1dRGrNEv5NKP7cwUn+9gR4wn+ewFc+zKF83G+t0CYHPQlBqYIB/671Al+yQmmhj0QCBb12xgCAn/YI2nlp78Ahiyn8pC2kv00ruN+yyu3pvbeZZ7/mLbPEl1zSCAucib+VeVpvCeDh6Yf5XwhG9Q7M+3VbcgPVps/zMY0aUqG+9mldGHWnnG+wBms4wzpTIg1KBVaIICQYIac2Eihu81mDCPkxTCAd5FCq648wITt5JHewEnNd1MOYyqOIoEdfbWnAwaMNSHN+pydHVHtluPfoa2dqNtmbjj9LIS3h/pN+DO9EcmOGandgF48nbTbyacy5J2KpnjZXcaQYxCDthb5rV5FSvAaf1IB8xnJBC9UrjBqWoC+qUdOLDtS0v5CR7jQTFn9oCMU67+YjLbfG6Kou43Tgm4uvAnV/pNpsizKNT1/eNBgqK6cCQHvCbc91YVWnapeVV7lK7AefBvBqHUjlModjtlNXW/vv8oamR8I6m9vLlUqHhzFYEN7rL6veMs5An8QIv0Jz4vlb1qxDaIqNsXq8AJ6IT6/x0Rl8oPwXakb7XDmG/qQPN/Mkg/h+mACByWpFyOLFiC8nIM9pBPJoesvC39UULePrlglIK2bYGvNPW5pCjb0wH3HBWukL1ESVLGkSdEAUCDbEnbjxONwH3x8OEdDAYHJPrz8JE/NPrb+tdRcqWBPehjOQMII0AzfQ+6ONAhWfQ3safyk15KmCmowLQFVnuECfluAXMSD4MXXkNtqwyuTDta0PhJBLvw0/1r71dUxIjCCGEoxzZ5lU2lSG3mUOfwyYyZdcgCVXUoIxZGzkDfdFaEB8an45/ll26qz6557WuGvnFDyoQb+PnvlR+dt81+v8W52d38UDrF+9KDUYqZvR6UBAITEDXR0Bh2idlyjzpKsN3FLOyy167wmiO9od3/8Jj/lTofk6zXSkweewQxYym2/HFLnyYmmHSQLGseNXhZaaj2qCzL4dfHh45cN/lZzsVmuPmECVnExuiMHJKebPxl5bUtPDhDpwVzSygD2Oc3wjPAaJ4rhMdo0oTSqBEaMZNuCBRFxd9W6Ns+KCl7AlCbpa3LAxFPBCFSpQwV+BuIZNzklyqb9LItnok4o1GzF0ddE+7VQUvrFFOt/NE1M74y7g0xBOwwAHePDZpc4dDHVEoaP/c7ua2twO+pBmqlzennfgqrNDNTgKNQproq5CL+U/Df+WmJ0vjI2BtqchzJXZY8irTOjsh9POkt0YEKR4oezg8nqejuDexn2GsKinSKuL2L4ZyzT7lmo3Vsg/YzibApGVn3tISwxrQM+LNo20kw++jB5WPm0LuAoerVYuhhZX7NeM8OYWVlBpdHgRLMPI29S+5xQs7miiDIdLr3RwoncAtTenbQRV7hxnnJfo8j7VQLF1n/sp/yEwSzk7bMVy4lMM9u6HMFaV5fXw2eTIhRLBtodStgJsK65B8mu0YBM1amC+FOv1hYrhe+NCJgj5o+PqaA+bpKEfSbtGI/U3bL05WE/C13ZaK1zPZux4Pn7S9i7rVuToH8BvekpqFzvYsDr36B8a/iraXzBRkgpEHp3Pkd32tlvc7nT/kqsDRMZxKIg2W4/yIjjorLxjt+SebiUuHHYyl4JiXqNiq0Ij1CMD00pC44FMimB4RfT2DfYXU6XXv1j3RbxhA48PexlLyC/KR+L9PyS+pT1ZWOtELZM/KhRaMnkZHD80LxBDWdsnt6pr/yxfcHbXonu8Mco8BZslLtbfSlcUqZeXJdvLq/3yz88up75OqqwrMhQ5LW1zfth9fkJMqtc0+8LC2XwIduYoGqw+CVOYMHqyjSJaqcS2/UtCppWq7fxQRHxYcXtZf3QJJC+i9vHxV2NvyVRTS+PcFWh8tIzbxBuwtEmHCzNJTdcyc5ZMoluG/tH8tmiCPcESZkhi+OPG4+8ag48IX4RVh6+nGsUkdrCGhrfxXaa+zPrazwMRtBlACWhjf3ZsGt0NKA2sQ8lWCSROTIpQOYMltJCYihR7sge1LLA7mVrJCkM0Gy5HnIlcolRYi8RDOlvpM68T8BiCq8X7Aw+lubGGChw14JPVo5cD5Y1ZwiafX+eHW7B70EKUlzHUrqzjcQrloUI3mG6PMc4DRNzC4QPG70jE2GXAfFpBEW/1Wg9LEPPtUIxfwnrK0KeCdeXignZFa9MM+GeBcDKMSI2R8QCbaLvFZ2XxXfncb5gi5FJX0YSQUmC8a1697NngtRa1syveyAcgN8hwZR++BFLB748HmQ+C5JhXMxfyfqK5g2kUDiqDMUfE9O5yiNKEcJNmyMHtAL6tm6jDRjt0D4zBYUOiZ8hm5wPoMXw+vvbthKbGAtRkisGYf1igZ3dTrI9+2YNYCw+7OGnwBy5F5+rtMRx/0rVdQ3dtAvxrAKnjj3U5QbL+SkLve5SfXyDX0/miSw440tSMJa7GysJtaah+mvfXyhUR+ob5iHfcFAx3qRDjtjl6QK4LJGuzPCyizuB0r2wf0/K6tpzTuE664z9UztmSAW20tuHY0fRGTlIQ1CtMe76ixpnkF6kL03dVSRWWJZ4I6RsATnOTNEc0oikieA5RrBLiZgbNwjHGamrS1AYb2IXYSMrnhxj86FGsd+0AnvWCAxHy8NOInKxTdcXxPoKaf4q4qJXMoazo99n2eBrrGEToXHEiqrZZ4I30UJFXDVW47TMxI8Qdl4UugZdeCikNx+ZQifb787b+HMVOf25L4i7dV8aPg+ls9Tr0z/xy5KaR2n1DrDNbX1S8Umy6/SJD1JHcyY5oWk/8mraZ2wefqGJR5y5ztaQvQyBOhMfnH96rrGlwJx87/VUgqhVL7w8xe5AeGr9Cox1ZSrn08iuCRu0o4WSPQL58SZ45AzLw5kEnARofrODOgOiDSmNv1svfLIhm8QdiYl5aHFfktIMyE4Obup9HQesK4yxj2q8XEOzX5mlaaqdHTrB1Xsf9XuEZsFgFFUKzFyzEWus1nuh3o56u/4DEoAX8x5TTuL7JsAegHmqzctsZWXNrsAsIuKlSuPlSx6rjZ0MZ6AbFjey+4SvryDcMSvGGokdDVA7HcO0T+7Rpg4N3YY8kJ3h5k/JbAqD/Resog5a2ZCgU1McuQLlc7PyIoNbqAv1xojvn9vFsXht5eH5o61F/vykl+vs88d8Q/15ZroGFvxCixKOIrr0HBiWhmRqF76bgBamCsxkhdyy5G9HKXptRaHBzpwC7bLX2h57CUcmPzbQNB0rDaMyp8kGBofxctnPfGCa+VJSEo2fyseScgfK3we765OPIYPwTQW6D2qqRwOu+/lq3fPmt8ek2ThEv8btEGvziLvxile5YwmIKvqn1xRhAqaf2+T2d4HLzZ61m4XGEFLcsugQ1CCmgxaiOq9ytvs5ODWfsZ2wXQxlpuhx/urdGMKI+HL/lB8sr+zDU+RiRHayJmiDXRhxFD/iHWwIWN3FjvjKc59gHm8UU5WW3Pzu0axGwrXidavKjJeao8cDiL4CCdQkiIkR4au3gehYMl61Jevue5UWk73ZtYS/AIVgXOoYYpnHm2SrpCf1J7bqvoZ8pEa7HVbKfqAO1u4wa2vP3OgPX+Wqf74FU6Ca4XrJxFSDDZwXRHjORKXJBEE23WRNvrwu4+kNwfLmS+cZp557HWujMojkuO+VB1eI7our3oY45hRjByIkgKaoB7C+yRLLoB08S03OChaHLovpJxF8rUboSYUqDlEQM+Ft0MxekSAjQUTFaRtrRt6XYI9XRROLCfGVIGg1BHisPlrPW8CziTztoTj/1Y6puFksW50xBYOgLuflDZ5pGc9YNI9KaiYLE1AYTh8YKScm8CQVZwWCiWu/w2pJKlyd1lPeCL+qY04IbVlaiTKtVxg48sOytEU2o+zAmzJvNTF5KKvEJtNjLRRgd9fWkN3gydi4NRT5bEIM69zBt9s7pRXtqUW0u7dJ9JJnZdQn03AgNk5pX+H32Kq92qG/Cus6f0UEM0jpOhVpFy3022Wjd85fO2cqRoipAJsZu5Ja2f0ZnRGLl73zSgjjbb5fVsE06xSObPg3KRxKqlyxP7kSJcC6ExWcqLnm4EqsHNFQCGjdS04HIZFCEsyCORb/Eo+hg89wDE9WJHzbeox59epPwENymsQIFVbrl32/EWSRBv2t2zqU2i6SUsp98o448O20hd1z+84hQM6mJOQVRefB9q5ViWKYfB2GFv7uC1OZ1fIbkykvmzE0EABGjKzhCW8/iYY7ARyRPt8b7lQDbuVfplOGfiYRX+pOg/5CfnVqX3igRRCp50XTJBLyiTJIkKnpe1qwmmJC5p//+Keou3yI+/yf//wnHae6G7f/Wrc9q8f/yvKpG+//ist82P7XdL/HrlWM4MR7JJ3COIxRWVoUr+GREBGjMUbHNAZnKYbkaELDeEzldJpAMZFQMfxSCPQeQ0AoRME4+s9///d//DMtL7UN8ZC+5/6//lnyOPvP/znXf/7/tOP//o9/lrR+WwH/L+ivUd1evm+WePm3HbP73/Pf/6f8v/+n/L//p/zfkfe65f1/peOw5df2z38Oe9f9xz9bXK5/Dfj/lnoP/3/LZfEWH/my5u/rv8VIy79TF2/FuPR/H8Tp+1z307i8Zcdu3+px+J/S67bs6VYff8Xida37+i2VZ399HqfbuPxVPe9xV2/3v+X7zf+0cNiqfKvTf//O+Vd7PeVdPfx916fT+zzk57/vMEx/nyRdvG5vVHtfvtc05Olb+7//003rXyf9NfmvLX8dhbxd9d//G/rtNhkNsgQA -->
