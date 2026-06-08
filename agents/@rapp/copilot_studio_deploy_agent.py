"""
CopilotStudioDeploy — a RAPP rapplication (agent + local UI).

Convert any RAPP agent into a Microsoft Copilot Studio agent and deploy it into
YOUR OWN Copilot Studio environment, fully locally. No PII or secrets ship with
this agent — you provide a local.settings.json (service principal) at deploy
time and it is used and stored ONLY on your machine.

────────────────────────────────────────────────────────────────────────────
HUMAN — two steps
  1. Hatch this rapplication:  ask the brainstem  "hatch <egg_url>"  (egg_hatcher),
     or drop this file into your brainstem's agents/ folder.
  2. Open the local UI the brainstem serves at  /rapp_ui/copilot_studio_deploy/
     — pick an agent (or paste a raw agent.py URL), optionally import your
     local.settings.json credentials, and click Deploy.

LLM — procedure (the agent IS the API; drive it via these actions)
  deploy_template     -> {query_or_url} FASTEST PATH. One call: search (default repo
                         AI-Agent-Templates) OR a raw URL OR a local path -> fetch ->
                         derive instructions -> package -> start deploy. Returns a
                         device-login code to relay (or deploys via saved credentials).
                         Then complete_deploy with the device_code. Don't re-search.
  search_templates    -> {query?} (advanced) browse kody-w/AI-Agent-Templates raw_urls
  list_catalog        -> pre-converted ready-to-deploy solutions
  fetch_source        -> {source_url} a template raw_url, ANY public GitHub raw agent.py
                         URL, OR a LOCAL file path; returns the text; YOU then author a
                         display name + Copilot Studio instructions from it
  package             -> {agent_name, instructions} -> packaged solution (package_id)
  deploy              -> {solution_url|package_id} -> begin device-code sign-in
  complete_deploy     -> {device_code} -> finish, discover env, import + publish
  set_credentials     -> {credentials: local.settings.json} -> save SP creds LOCALLY
  credentials_status  -> is a local service principal configured?
  deploy_with_credentials -> {solution_url|package_id} -> autonomous SP deploy (no login)

  Boundary rules: never echo a client_secret back to the user or into chat; creds
  live only in ~/.rapp_deploy_settings.json. Prefer deploy_with_credentials when
  credentials_status reports found=true.
"""
import base64, io, json, os, re, time, urllib.request, urllib.parse, uuid, zipfile
try:
    from agents.basic_agent import BasicAgent
except ImportError:  # alternate kernel layouts (SPEC kernel/SPEC.md §5)
    try:
        from basic_agent import BasicAgent
    except ImportError:
        try:
            from openrappter.agents.basic_agent import BasicAgent
        except ImportError:  # standalone fallback so the file runs anywhere (RAR rapp_sdk test)
            class BasicAgent:
                def __init__(self, name=None, metadata=None):
                    if name is not None: self.name = name
                    if metadata is not None: self.metadata = metadata
                def perform(self, **kwargs): return 'Not implemented.'
                def system_context(self): return None
                def to_tool(self):
                    return {'type': 'function', 'function': {'name': self.name,
                            'description': self.metadata.get('description', ''),
                            'parameters': self.metadata.get('parameters', {})}}

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/copilot_studio_deploy_agent",
    "version": "1.0.0",
    "display_name": "CopilotStudioDeploy",
    "description": "Convert any RAPP agent (from AI-Agent-Templates, a public URL, or a local file) and deploy it into your own Microsoft Copilot Studio environment, locally. Device-code or service-principal auth; credentials stay on your machine.",
    "author": "kody-w",
    "tags": ["copilot", "copilot_studio", "power_platform", "deploy", "integration", "automation"],
    "category": "integrations",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": "Deploy the emission tracking agent to my Copilot Studio environment",
}


REPO_RAW = "https://raw.githubusercontent.com/kody-w/rapp-oneclick-deploy/main"
TEMPLATES_REPO = "kody-w/AI-Agent-Templates"   # default source of deployable agents
PUBLIC_CLIENT = "9cee029c-6210-4654-90bb-17e6e9d36617"   # Power Platform CLI public client
AUTH = "https://login.microsoftonline.com"
DISCO = "https://globaldisco.crm.dynamics.com"
REF_SCHEMA, REF_DISPLAY, REF_VERSION = "dealprogression", "deal progression", "1.0.470.0"

_CACHE = {}   # package_id -> zip bytes ;  device_code -> {"zip":bytes,"env":str|None}


# ── http ──────────────────────────────────────────────────────────────────────
def _req(url, data=None, headers=None, method=None, timeout=300):
    if isinstance(data, dict):
        data = urllib.parse.urlencode(data).encode()
    elif data is not None and not isinstance(data, (bytes, bytearray)):
        data = json.dumps(data).encode()
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode("utf-8", "replace")
            return r.status, (json.loads(body) if body[:1] in ("{", "[") else body)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try: body = json.loads(body)
        except Exception: pass
        return e.code, body

def _search_templates(query="", repo=TEMPLATES_REPO, limit=60):
    """Search a public GitHub repo (default: AI-Agent-Templates) for deployable
    agent.py files. Returns [{name, path, stack, raw_url}]."""
    code, tree = _req(f"https://api.github.com/repos/{repo}/git/trees/HEAD?recursive=1",
                      headers={"Accept": "application/vnd.github+json", "User-Agent": "rapp"})
    if code != 200 or not isinstance(tree, dict) or "tree" not in tree:
        raise RuntimeError(f"could not list {repo} ({code}) — check the repo name or GitHub rate limit")
    q = (query or "").lower()
    out = []
    for b in tree["tree"]:
        p = b.get("path", "")
        if b.get("type") != "blob" or not re.search(r"/agents/[^/]*agent\.py$", p):
            continue
        if any(x in p.lower() for x in ("copy", "experimental", "__pycache__", "disabled", "/tests/")):
            continue
        if q:
            norm = p.lower().replace("_", " ")               # "emission tracking" matches emission_tracking_agent.py
            if not all(w in norm for w in q.split()):
                continue
        m = re.search(r"/([^/]+_stack)/", p)
        out.append({"name": p.rsplit("/", 1)[-1].replace("_agent.py", "").replace("_", " ").title(),
                    "path": p, "stack": m.group(1) if m else None,
                    "raw_url": f"https://raw.githubusercontent.com/{repo}/main/" + urllib.parse.quote(p)})
        if len(out) >= limit:
            break
    return out


def _read_source(src):
    """Read an agent.py from a public URL OR a local file path."""
    src = (src or "").strip()
    if src.startswith(("http://", "https://")):
        return _get_bytes(src).decode("utf-8", "replace")
    local = os.path.expanduser(src)
    if os.path.isfile(local):
        with open(local, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    raise FileNotFoundError("provide a raw GitHub URL or an existing local file path")


def _derive_spec(source_code):
    """Deterministically derive a Copilot Studio agent spec from agent.py source —
    no LLM hop. Parses the class docstring + public methods into instructions."""
    import ast as _ast
    name, doc, methods = "RAPP Agent", "", []
    try:
        tree = _ast.parse(source_code)
        cls = next((n for n in tree.body if isinstance(n, _ast.ClassDef) and n.name.endswith("Agent")), None) \
            or next((n for n in tree.body if isinstance(n, _ast.ClassDef)), None)
        if cls:
            name = cls.name
            doc = _ast.get_docstring(cls) or ""
            for m in cls.body:
                if isinstance(m, (_ast.FunctionDef, _ast.AsyncFunctionDef)) and not m.name.startswith("_") \
                        and m.name not in ("perform", "system_context", "to_tool"):
                    first = (_ast.get_docstring(m) or "").strip().split("\n")[0]
                    methods.append((m.name, first))
    except Exception:
        g = re.search(r"class\s+(\w+)", source_code)
        name = g.group(1) if g else name
        doc = (re.search(r'"""(.*?)"""', source_code, re.S) or ["", ""])[1].strip() if '"""' in source_code else ""
    display = (re.sub(r"(?<!^)(?=[A-Z])", " ", name).replace("Agent", "").strip()) or "RAPP Agent"
    caps = "\n".join(f"- {re.sub(r'(?<!^)(?=[A-Z])', ' ', n).replace('_', ' ').strip().title()}"
                     + (f": {d}" if d else "") for n, d in methods[:14]) \
        or "- Assist the user within this agent's domain."
    instructions = (f"# Purpose\n{doc.strip() or ('You are the ' + display + ' agent.')}\n\n"
                    f"# Capabilities\n{caps}\n\n"
                    f"# Guidelines\n- Confirm the user's request and collect any required inputs.\n"
                    f"- Be concise, accurate, and helpful; stay within scope.")
    return {"display_name": display[:60], "unique_name": _sanitize(display),
            "description": ((doc.strip().split('\n')[0]) or display)[:200], "instructions": instructions}


def _get_bytes(url, timeout=120):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "rapp"}), timeout=timeout) as r:
        return r.read()


# ── packaging (rebrand skeleton + inject brainstem-authored instructions) ──────
def _render_gpt(display_name, instructions):
    body = "\n".join("  " + ln for ln in (instructions or "Be a helpful agent.").splitlines())
    return f"kind: GptComponentMetadata\ndisplayName: {display_name}\ninstructions: |-\n{body}\n".encode()

def _sanitize(name, fallback="ragent"):
    return re.sub(r"[^a-z0-9]", "", (name or "").lower()) or fallback

def build_solution(skeleton_bytes, agent_name, unique_name, instructions, version="1.0.1.0"):
    out = io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(skeleton_bytes)) as zin, \
         zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.namelist():
            data = zin.read(item)
            newpath = item.replace(REF_SCHEMA, unique_name)
            if newpath.endswith(".gpt.default/data"):
                data = _render_gpt(agent_name, instructions)
            else:
                data = (data.decode("utf-8", "replace")
                        .replace(REF_SCHEMA, unique_name)
                        .replace(REF_DISPLAY, agent_name)
                        .replace(REF_VERSION, version)).encode()
            zout.writestr(newpath, data)
    return out.getvalue()


# ── auth + deploy ──────────────────────────────────────────────────────────────
def _device_start(scope):
    code, r = _req(f"{AUTH}/organizations/oauth2/v2.0/devicecode",
                   data={"client_id": PUBLIC_CLIENT, "scope": scope},
                   headers={"Content-Type": "application/x-www-form-urlencoded"})
    if code != 200:
        raise RuntimeError(f"device code start failed: {r}")
    return r

def _token_from_device(device_code):
    return _req(f"{AUTH}/organizations/oauth2/v2.0/token",
                data={"grant_type": "urn:ietf:params:oauth:grant-type:device_code",
                      "client_id": PUBLIC_CLIENT, "device_code": device_code},
                headers={"Content-Type": "application/x-www-form-urlencoded"})

def _refresh(refresh_token, scope):
    code, t = _req(f"{AUTH}/organizations/oauth2/v2.0/token",
                   data={"grant_type": "refresh_token", "refresh_token": refresh_token,
                         "client_id": PUBLIC_CLIENT, "scope": scope},
                   headers={"Content-Type": "application/x-www-form-urlencoded"})
    if code != 200:
        raise RuntimeError(f"token refresh failed: {t}")
    return t["access_token"]

def _discover(disco_token):
    code, r = _req(f"{DISCO}/api/discovery/v2.0/Instances",
                   headers={"Authorization": "Bearer " + disco_token, "Accept": "application/json"})
    return [e for e in (r.get("value", []) if isinstance(r, dict) else []) if e.get("ApiUrl")]

def _dataverse(env, token, action, body=None, method="POST"):
    # JSON-encode here (pass bytes) — _req form-encodes dicts for the OAuth endpoints,
    # but the Dataverse Web API needs a JSON body.
    data = json.dumps(body).encode() if body is not None else None
    return _req(f"{env.rstrip('/')}/api/data/v9.2/{action}",
                data=data, method=method,
                headers={"Authorization": "Bearer " + token, "Content-Type": "application/json",
                         "Accept": "application/json", "OData-MaxVersion": "4.0", "OData-Version": "4.0"})

def _import(env, token, zip_bytes):
    code, r = _dataverse(env, token, "ImportSolution", {
        "OverwriteUnmanagedCustomizations": True, "PublishWorkflows": True,
        "ImportJobId": str(uuid.uuid4()), "CustomizationFile": base64.b64encode(zip_bytes).decode()})
    if code not in (200, 204):
        raise RuntimeError(f"ImportSolution failed ({code}): {r}")
    _dataverse(env, token, "PublishAllXml")


# ── service-principal credentials (import/export a local.settings.json) ─────────
SETTINGS_PATH = os.path.expanduser("~/.rapp_deploy_settings.json")

def _extract_dyn(creds):
    """Accept a settings dict {IsEncrypted,Values}, a bare Values dict, or a JSON
    string; return {client_id, client_secret, tenant_id, resource} or None."""
    if isinstance(creds, str):
        try: creds = json.loads(creds)
        except Exception: return None
    if not isinstance(creds, dict):
        return None
    vals = creds.get("Values", creds)
    cid, sec = vals.get("DYNAMICS_365_CLIENT_ID"), vals.get("DYNAMICS_365_CLIENT_SECRET")
    ten, res = vals.get("DYNAMICS_365_TENANT_ID"), vals.get("DYNAMICS_365_RESOURCE")
    if not all([cid, sec, ten, res]):
        return None
    return {"client_id": cid, "client_secret": sec, "tenant_id": ten, "resource": res.rstrip("/")}

def _load_local_settings():
    for p in (os.environ.get("RAPP_DEPLOY_SETTINGS"), SETTINGS_PATH):
        if p and os.path.isfile(p):
            try:
                d = _extract_dyn(json.load(open(p)))
                if d: return d
            except Exception:
                pass
    return _extract_dyn({"Values": dict(os.environ)})  # fall back to process env

def _sp_token(client_id, secret, tenant, resource):
    code, t = _req(f"{AUTH}/{tenant}/oauth2/v2.0/token",
                   data={"grant_type": "client_credentials", "client_id": client_id,
                         "client_secret": secret, "scope": resource.rstrip("/") + "/.default"},
                   headers={"Content-Type": "application/x-www-form-urlencoded"})
    if code != 200 or not isinstance(t, dict) or "access_token" not in t:
        raise RuntimeError(f"service-principal auth failed: {t}")
    return t["access_token"]


class CopilotStudioDeployAgent(BasicAgent):
    def __init__(self):
        self.name = "CopilotStudioDeploy"
        self.metadata = {
            "name": self.name,
            "description": (
                "Convert and deploy a RAPP agent into the user's own Microsoft Copilot Studio "
                "environment. **FASTEST PATH — use this first: action=deploy_template** with "
                "`query_or_url` = an agent name to search for (default source: kody-w/AI-Agent-Templates), "
                "OR any public raw agent.py URL, OR a local file path. It searches, fetches, converts, "
                "packages and STARTS the deploy in ONE call — returns a device-login user_code+URL to relay "
                "(or deploys autonomously if a service principal is saved). Then call action=complete_deploy "
                "with the device_code once the user signs in. Do NOT re-search; deploy_template handles it. "
                "If the user wants a service principal so deploys run with NO sign-in, action=credentials_help "
                "walks them through creating it, set_credentials saves it locally, and verify_credentials "
                "confirms it works. Advanced/granular actions: search_templates, fetch_source, package, deploy, "
                "deploy_with_credentials, list_catalog (pre-converted solutions), credentials_status."),
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["deploy_template", "complete_deploy", "search_templates",
                                                       "list_catalog", "fetch_source", "package", "deploy",
                                                       "credentials_help", "set_credentials", "verify_credentials",
                                                       "credentials_status", "deploy_with_credentials"]},
                "query_or_url": {"type": "string", "description": "deploy_template: agent name to search, OR a raw agent.py URL, OR a local path"},
                "query": {"type": "string", "description": "optional filter for search_templates"},
                "repo": {"type": "string", "description": "optional public repo for search_templates (default kody-w/AI-Agent-Templates)"},
                "source_url": {"type": "string", "description": "raw agent.py URL OR a local file path (fetch_source)"},
                "agent_name": {"type": "string", "description": "human display name (package)"},
                "instructions": {"type": "string", "description": "Copilot Studio system instructions you authored (package)"},
                "unique_name": {"type": "string", "description": "optional lowercase id (package)"},
                "package_id": {"type": "string", "description": "id returned by package (deploy)"},
                "solution_url": {"type": "string", "description": "raw URL of a prebuilt solution .zip (deploy)"},
                "environment_url": {"type": "string", "description": "optional target env https://org.crm.dynamics.com"},
                "device_code": {"type": "string", "description": "device_code from deploy (complete_deploy)"},
                "credentials": {"type": "object", "description": "a local.settings.json (or its Values) holding "
                                "DYNAMICS_365_CLIENT_ID/SECRET/TENANT_ID/RESOURCE — for set_credentials or "
                                "deploy_with_credentials (service-principal, no device login)"},
            }, "required": ["action"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "").strip()
        try:
            if action == "deploy_template":
                # ONE-SHOT: resolve source -> fetch -> derive instructions -> package -> start deploy.
                q = (kwargs.get("query_or_url") or kwargs.get("source_url") or kwargs.get("query") or "").strip()
                if not q:
                    return json.dumps({"status": "error", "message": "query_or_url required (agent name, raw URL, or local path)"})
                chosen = None
                if q.startswith(("http://", "https://")) or os.path.isfile(os.path.expanduser(q)):
                    source_ref = q
                else:
                    tpls = _search_templates(q)
                    if not tpls:
                        return json.dumps({"status": "error", "message": f"no agent matched '{q}' — try a different name, a raw URL, or a local path"})
                    source_ref, chosen = tpls[0]["raw_url"], tpls[0]["name"]
                spec = _derive_spec(_read_source(source_ref))
                zip_bytes = build_solution(_get_bytes(f"{REPO_RAW}/pipeline/skeleton.zip"),
                                           spec["display_name"], spec["unique_name"], spec["instructions"])
                creds = _extract_dyn(kwargs["credentials"]) if kwargs.get("credentials") else _load_local_settings()
                if creds:  # autonomous service-principal deploy, no login
                    token = _sp_token(creds["client_id"], creds["client_secret"], creds["tenant_id"], creds["resource"])
                    _import(creds["resource"], token, zip_bytes)
                    return json.dumps({"status": "success", "agent": spec["display_name"], "source": source_ref,
                                       "environment_url": creds["resource"],
                                       "message": f"Deployed '{spec['display_name']}' to {creds['resource']}. Open https://copilotstudio.microsoft.com/."})
                dc = _device_start(f"{DISCO}/user_impersonation offline_access")
                _CACHE[dc["device_code"]] = {"zip": zip_bytes, "env": kwargs.get("environment_url")}
                return json.dumps({"status": "auth_required", "agent": spec["display_name"], "source": source_ref,
                                   "device_code": dc["device_code"], "user_code": dc["user_code"],
                                   "verification_uri": dc["verification_uri"],
                                   "message": (f"Converted '{spec['display_name']}'. Tell the user: open "
                                               f"{dc['verification_uri']} and enter code {dc['user_code']}, sign into "
                                               "the target Copilot Studio environment, then call action=complete_deploy "
                                               "with this device_code. Do NOT search again.")})

            if action == "search_templates":
                tpls = _search_templates(kwargs.get("query", ""), kwargs.get("repo") or TEMPLATES_REPO)
                return json.dumps({"status": "success", "repo": kwargs.get("repo") or TEMPLATES_REPO,
                                   "count": len(tpls), "templates": tpls,
                                   "next": "Pick a raw_url, then action=fetch_source with it (or any public URL / local path)."})

            if action == "list_catalog":
                cat = json.loads(_get_bytes(f"{REPO_RAW}/catalog/agents.json").decode())
                return json.dumps({"status": "success", "agents": [
                    {"id": a["id"], "name": a["name"], "category": a.get("category"),
                     "status": a["status"],
                     "solution_url": (f"{REPO_RAW}/{a['solution']}" if a.get("solution") else None),
                     "source": a.get("source")} for a in cat.get("agents", [])]})

            if action == "fetch_source":
                src = kwargs.get("source_url") or kwargs.get("source") or kwargs.get("path") or ""
                try:
                    text = _read_source(src)   # public URL OR local file path
                except (FileNotFoundError, Exception) as e:
                    return json.dumps({"status": "error", "message": str(e)})
                origin = "url" if src.strip().startswith("http") else "local-file"
                return json.dumps({"status": "success", "source_ref": src, "origin": origin, "length": len(text),
                                   "source": text[:12000],
                                   "next": "Author agent_name + instructions, then call action=package."})

            if action == "package":
                name = kwargs.get("agent_name") or "RAPP Agent"
                instr = kwargs.get("instructions")
                if not instr:
                    return json.dumps({"status": "error", "message": "instructions required — author them from the agent source first"})
                uniq = _sanitize(kwargs.get("unique_name") or name)
                skel = _get_bytes(f"{REPO_RAW}/pipeline/skeleton.zip")
                zip_bytes = build_solution(skel, name, uniq, instr)
                pid = uniq + "-" + uuid.uuid4().hex[:8]
                _CACHE[pid] = zip_bytes
                return json.dumps({"status": "success", "package_id": pid, "unique_name": uniq,
                                   "size": len(zip_bytes), "next": "Call action=deploy with this package_id."})

            if action == "deploy":
                if kwargs.get("solution_url"):
                    zip_bytes = _get_bytes(kwargs["solution_url"])
                elif kwargs.get("package_id") in _CACHE:
                    zip_bytes = _CACHE[kwargs["package_id"]]
                else:
                    return json.dumps({"status": "error", "message": "provide solution_url or a valid package_id"})
                dc = _device_start(f"{DISCO}/user_impersonation offline_access")
                _CACHE[dc["device_code"]] = {"zip": zip_bytes, "env": kwargs.get("environment_url")}
                return json.dumps({"status": "auth_required", "device_code": dc["device_code"],
                                   "user_code": dc["user_code"], "verification_uri": dc["verification_uri"],
                                   "message": (f"Tell the user: open {dc['verification_uri']} and enter code "
                                               f"{dc['user_code']}, sign into the Copilot Studio environment, "
                                               "then call action=complete_deploy with this device_code.")})

            if action == "complete_deploy":
                dc = kwargs.get("device_code", "")
                pending = _CACHE.get(dc)
                if not pending:
                    return json.dumps({"status": "error", "message": "unknown device_code — call action=deploy first"})
                # poll briefly for the token (user should have signed in by now)
                tok = None
                for _ in range(20):
                    code, t = _token_from_device(dc)
                    if code == 200:
                        tok = t; break
                    if isinstance(t, dict) and t.get("error") in ("authorization_pending", "slow_down"):
                        time.sleep(3); continue
                    return json.dumps({"status": "error", "message": f"sign-in failed: {t}"})
                if not tok:
                    return json.dumps({"status": "pending", "message": "Still waiting on sign-in — retry complete_deploy."})
                envs = _discover(tok["access_token"])
                want = kwargs.get("environment_url") or pending.get("env")
                env = next((e for e in envs if e["ApiUrl"].rstrip("/").lower() == (want or "").rstrip("/").lower()),
                           envs[0] if envs else None)
                if env is None:
                    return json.dumps({"status": "error", "message": "no Power Platform environments for this account"})
                if want is None and len(envs) > 1:
                    return json.dumps({"status": "choose_environment",
                                       "environments": [{"name": e["FriendlyName"], "url": e["ApiUrl"]} for e in envs],
                                       "message": "Multiple environments — call complete_deploy again with environment_url set."})
                env_token = _refresh(tok["refresh_token"], f"{env['ApiUrl'].rstrip('/')}/user_impersonation")
                _import(env["ApiUrl"], env_token, pending["zip"])
                _CACHE.pop(dc, None)
                return json.dumps({"status": "success",
                                   "environment": env["FriendlyName"], "environment_url": env["ApiUrl"],
                                   "message": f"Deployed to {env['FriendlyName']}. Open https://copilotstudio.microsoft.com/ to use the agent."})

            if action == "credentials_help":
                return json.dumps({"status": "success",
                    "title": "Set up a service principal so deploys run end-to-end with no sign-in",
                    "steps": [
                        "1. App registration: https://entra.microsoft.com -> Applications -> App registrations -> New registration. Name it (e.g. 'RAPP Copilot Studio Deploy'), single-tenant, Register.",
                        "2. On the Overview page copy 'Application (client) ID' -> DYNAMICS_365_CLIENT_ID, and 'Directory (tenant) ID' -> DYNAMICS_365_TENANT_ID.",
                        "3. Certificates & secrets -> New client secret -> copy the secret VALUE (not the Secret ID) -> DYNAMICS_365_CLIENT_SECRET.",
                        "4. Give it access to your environment: https://admin.powerplatform.microsoft.com -> pick your environment -> Settings -> Users + permissions -> Application users -> New app user -> add the app -> assign a security role that can import solutions (System Customizer or System Administrator).",
                        "5. DYNAMICS_365_RESOURCE = your environment URL, e.g. https://yourorg.crm.dynamics.com",
                        "6. Put those 4 values into a local.settings.json (template below), call action=set_credentials with it, then action=verify_credentials to confirm, then deploy with no sign-in.",
                    ],
                    "local_settings_template": {"IsEncrypted": False, "Values": {
                        "DYNAMICS_365_CLIENT_ID": "<application (client) id>",
                        "DYNAMICS_365_CLIENT_SECRET": "<client secret value>",
                        "DYNAMICS_365_TENANT_ID": "<directory (tenant) id>",
                        "DYNAMICS_365_RESOURCE": "https://yourorg.crm.dynamics.com"}},
                    "note": "The secret is stored only on your machine (~/.rapp_deploy_settings.json); it is never sent to any cloud model. No service principal? Skip all this — just run a deploy and use the device-login code instead.",
                    "next": "After set_credentials, call action=verify_credentials, then deploy_template."})

            if action == "verify_credentials":
                d = _extract_dyn(kwargs["credentials"]) if kwargs.get("credentials") else _load_local_settings()
                if not d:
                    return json.dumps({"status": "error", "message": "no credentials — run credentials_help, then set_credentials"})
                try:
                    tok = _sp_token(d["client_id"], d["client_secret"], d["tenant_id"], d["resource"])
                except Exception as e:
                    return json.dumps({"status": "error", "stage": "token",
                                       "message": f"Could not get a token — check client id/secret/tenant. ({e})"})
                code, who = _req(f"{d['resource'].rstrip('/')}/api/data/v9.2/WhoAmI",
                                 headers={"Authorization": "Bearer " + tok, "Accept": "application/json"})
                if code == 200 and isinstance(who, dict):
                    return json.dumps({"status": "success", "resource": d["resource"], "user_id": who.get("UserId"),
                                       "message": "Service principal works and can reach the environment — ready to deploy with no sign-in."})
                return json.dumps({"status": "error", "stage": "environment", "http": code,
                                   "message": "Token OK, but this app can't reach the environment. Add it as an Application User (step 4) with a solution-import role.",
                                   "detail": str(who)[:300]})

            if action == "set_credentials":
                creds = kwargs.get("credentials")
                if not _extract_dyn(creds):
                    return json.dumps({"status": "error", "message": "credentials missing DYNAMICS_365_CLIENT_ID/SECRET/TENANT_ID/RESOURCE"})
                obj = json.loads(creds) if isinstance(creds, str) else creds
                with open(SETTINGS_PATH, "w") as f:
                    json.dump(obj, f, indent=2)
                d = _extract_dyn(creds)
                return json.dumps({"status": "success", "saved": SETTINGS_PATH, "resource": d["resource"],
                                   "message": f"Credentials saved locally for {d['resource']} — deploys are now autonomous (no device login)."})

            if action == "credentials_status":
                d = _load_local_settings()
                if not d:
                    return json.dumps({"status": "success", "found": False})
                return json.dumps({"status": "success", "found": True, "resource": d["resource"],
                                   "client_id": d["client_id"], "client_secret": "***", "source": SETTINGS_PATH})

            if action == "deploy_with_credentials":
                if kwargs.get("solution_url"):
                    zip_bytes = _get_bytes(kwargs["solution_url"])
                elif kwargs.get("package_id") in _CACHE:
                    zip_bytes = _CACHE[kwargs["package_id"]]
                else:
                    return json.dumps({"status": "error", "message": "provide solution_url or a valid package_id"})
                d = _extract_dyn(kwargs["credentials"]) if kwargs.get("credentials") else _load_local_settings()
                if not d:
                    return json.dumps({"status": "error", "message": "no Dynamics credentials — call set_credentials or place ~/.rapp_deploy_settings.json"})
                token = _sp_token(d["client_id"], d["client_secret"], d["tenant_id"], d["resource"])
                _import(d["resource"], token, zip_bytes)
                return json.dumps({"status": "success", "environment_url": d["resource"],
                                   "message": f"Deployed to {d['resource']} (service principal). Open https://copilotstudio.microsoft.com/ to use the agent."})

            return json.dumps({"status": "error", "message": f"unknown action '{action}'"})
        except Exception as e:
            return json.dumps({"status": "error", "message": str(e)})
