---
name: "rar-kody-w-copilot-studio-deploy"
description: "Deploys Copilot Studio agents into Dataverse four ways: REST ImportSolutionAsync, the pac CLI pipeline, the quality-gated FACTORY chain, or the NEW-experience MCP shape (BlastBox two-solution: inline-MCP connector + new-generation connected agents, channel-less parents, publish-verified)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_deploy_agent", "rar_sha256": "9c15148dcff8ac706a3a49a941dc42e3b915a8e9cb0a6b8a147b0a3a60308153", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.2.0", "author": "kody-w", "tags": ["copilot-studio", "deploy", "dataverse", "power-platform", "pac", "import-solution", "destructive", "assimilated", "factory", "quality-gate", "synthetic-data", "pipeline", "mcp", "new-shape", "blastbox", "connected-agents"]}
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

<!-- rci-capsule:v1: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 -->
