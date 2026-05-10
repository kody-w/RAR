"""factory_agent — plant a brand-new neighborhood from the starter template.

The meta-agent. Drop into your local brainstem agents/ directory and chat:

    NeighborhoodFactory mode=local owner=alice name=my-team display="Alice's Team"
    NeighborhoodFactory mode=private owner=alice name=my-team display="Alice's Team"
    NeighborhoodFactory mode=public  owner=alice name=my-team display="Alice's Team"
    NeighborhoodFactory mode=egg     owner=alice name=my-team display="Alice's Team"

The factory:

  1. Pulls the canonical neighborhood-starter.egg from kody-w/RAR (or
     uses a local copy if airgapped — pass template_egg=/path/to/file).
  2. Unpacks the template into memory.
  3. Substitutes template tokens — {{owner}}, {{nb_slug}}, {{display_name}},
     {{neighborhood_rappid}}, etc. — with the operator's choices.
  4. Computes sha256 of every agent and writes rar/index.json.
  5. Materializes the result based on mode:
       local   → unpacked at ~/brainstem-workspace/<nb_slug>/
       private → above + creates GitHub-private repo + pushes
       public  → above + creates GitHub-public repo + pushes
       egg     → packs a fresh .egg at ~/brainstem-eggs/<nb_slug>-<ts>.egg
     Modes can be combined: mode="local,egg" produces both.

Per the kernel sneakernet portability invariant: this single agent
covers every option an operator might want. No second chat needed.
The factory does workspace mint + egg pack + GitHub push internally
based on the chosen mode(s).

Self-contained. Stdlib + `gh` CLI for GitHub modes. Default
dry_run=True; pass dry_run=False to actually materialize.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import subprocess
import urllib.request
import uuid
import zipfile
import io
from datetime import datetime, timezone

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


_DEFAULT_TEMPLATE_URL = (
    "https://raw.githubusercontent.com/kody-w/RAR/main/"
    "stacks/neighborhood-starter/neighborhood-starter.egg"
)


def _now_iso() -> str:
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z")
    )


def _gh(args: list[str], input_bytes: bytes | None = None) -> tuple[int, str, str]:
    p = subprocess.run(["gh", *args], capture_output=True, input=input_bytes)
    return p.returncode, p.stdout.decode(errors="replace"), p.stderr.decode(errors="replace")


def _http_get(url: str) -> bytes | None:
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "neighborhood-factory/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read()
    except Exception:
        return None


def _gh_repo_exists(owner: str, name: str) -> bool:
    rc, _, _ = _gh(["api", f"/repos/{owner}/{name}"])
    return rc == 0


def _gh_create_repo(owner: str, name: str, description: str,
                     public: bool) -> tuple[bool, str]:
    visibility = "--public" if public else "--private"
    rc, out, err = _gh([
        "repo", "create", f"{owner}/{name}",
        visibility, "--description", description,
    ])
    if rc == 0:
        return True, out.strip() or f"https://github.com/{owner}/{name}"
    return False, (err or out).strip()


def _gh_put_file(owner: str, name: str, path: str, content: bytes,
                  message: str) -> tuple[bool, str]:
    payload = {"message": message,
                "content": base64.b64encode(content).decode()}
    rc, out, err = _gh(
        ["api", "-X", "PUT", f"/repos/{owner}/{name}/contents/{path}",
         "--input", "-"],
        input_bytes=json.dumps(payload).encode(),
    )
    return (rc == 0), ("ok" if rc == 0 else (err or out).strip())


def _load_template(template_egg: str | None) -> tuple[dict[str, bytes], str]:
    """Load template files from a local .egg path OR the canonical URL.

    Returns (files dict, source description).
    """
    egg_bytes = None
    source = ""
    if template_egg:
        path = os.path.expanduser(template_egg)
        if os.path.isfile(path):
            egg_bytes = open(path, "rb").read()
            source = f"local: {path}"
    if egg_bytes is None:
        egg_bytes = _http_get(_DEFAULT_TEMPLATE_URL)
        if egg_bytes:
            source = f"network: {_DEFAULT_TEMPLATE_URL}"
    if egg_bytes is None:
        raise RuntimeError(
            "Couldn't load template egg. Pass template_egg=<path> or "
            "ensure internet access to kody-w/RAR."
        )
    files: dict[str, bytes] = {}
    with zipfile.ZipFile(io.BytesIO(egg_bytes), "r") as zf:
        for info in zf.infolist():
            if info.is_dir():
                continue
            files[info.filename] = zf.read(info.filename)
    return files, source


def _substitute_tokens(files: dict[str, bytes], tokens: dict[str, str]) -> dict[str, bytes]:
    """Replace {{token}} markers across all text-y files."""
    text_exts = {".md", ".html", ".json", ".txt", ".py"}
    out: dict[str, bytes] = {}
    for path, body in files.items():
        ext = os.path.splitext(path)[1]
        if ext in text_exts:
            try:
                text = body.decode("utf-8")
                for k, v in tokens.items():
                    text = text.replace("{{" + k + "}}", v)
                out[path] = text.encode("utf-8")
            except UnicodeDecodeError:
                out[path] = body
        else:
            out[path] = body
    return out


def _build_rar_index(files: dict[str, bytes], owner: str, nb_slug: str) -> bytes:
    """Build a sha256-pinned rar/index.json from the agent files in this set."""
    raw_prefix = f"https://raw.githubusercontent.com/{owner}/{nb_slug}/main"
    required = []
    for path, body in sorted(files.items()):
        if not path.startswith("agents/") or not path.endswith("_agent.py"):
            continue
        base = os.path.basename(path)
        stem = base[: -len("_agent.py")]
        cls = "".join(p.capitalize() for p in stem.split("_")) + "Agent"
        meta_name = "".join(p.capitalize() for p in stem.split("_"))
        required.append({
            "kind": "agent",
            "name": meta_name,
            "metadata_name": meta_name,
            "file": path,
            "raw_url": f"{raw_prefix}/{path}",
            "sha256": hashlib.sha256(body).hexdigest(),
            "schema": "rapp-agent/1.0",
        })
    rar = {
        "schema": "rapp-rar-index/1.0",
        "name": nb_slug,
        "rar_for": f"{owner}/{nb_slug}",
        "purpose": (
            f"Required participation kit for the {nb_slug} neighborhood. "
            "Joining brainstems hot-load these agents (sha256-verified) "
            "into their local agents/ directory via EggHatcher."
        ),
        "version": "1.0",
        "created_at": _now_iso(),
        "raw_url_prefix": raw_prefix,
        "required_for_participation": required,
        "kernel_base_included": [],
        "optional_for_participation": [],
        "organs": [], "senses": [], "cards": [],
        "rapplications": [{
            "kind": "rapplication",
            "name": "dashboard",
            "directory": "rapplications/dashboard",
            "entry_agent": "DashboardRender",
            "_note": (
                "UI hydrated by DashboardRender (composes ProjectPinger + "
                "Twin + Pm with static inputs). Per kernel rapplication-sdk: "
                "agents drive both UI and chat — no duplicated logic."
            ),
        }],
    }
    return (json.dumps(rar, indent=2) + "\n").encode()


class NeighborhoodFactoryAgent(BasicAgent):
    metadata = {
        "name": "NeighborhoodFactory",
        "description": (
            "Plant a brand-new neighborhood from the canonical starter "
            "template. ONE call covers every option: local-only on-device, "
            "GitHub-private, GitHub-public, or just a portable .egg for "
            "sneakernet. Modes can be combined (mode='local,egg'). "
            "Default dry_run=True."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "owner": {
                    "type": "string",
                    "description": "GitHub handle to plant under (required for private/public).",
                },
                "name": {
                    "type": "string",
                    "description": "Repo slug (lowercase + hyphens). E.g. 'my-team'.",
                },
                "display_name": {
                    "type": "string",
                    "description": "Human-readable name. E.g. 'Alice's Team'.",
                },
                "purpose": {
                    "type": "string",
                    "description": "1-2 sentences on what the team uses this for.",
                },
                "mode": {
                    "type": "string",
                    "description": (
                        "Output mode(s), comma-separated. "
                        "Options: local, private, public, egg. "
                        "E.g. 'local,egg' produces both a workspace and a portable .egg."
                    ),
                    "default": "local",
                },
                "template_egg": {
                    "type": "string",
                    "description": (
                        "Optional local path to a starter template .egg. If "
                        "omitted, fetches the canonical from kody-w/RAR."
                    ),
                },
                "dry_run": {
                    "type": "boolean", "default": True,
                    "description": "If true, shows the plan without materializing.",
                },
            },
            "required": ["owner", "name", "display_name"],
        },
    }

    def __init__(self):
        self.name = "NeighborhoodFactory"

    def perform(self, **kwargs) -> str:
        owner = (kwargs.get("owner") or "").strip().strip("/")
        nb_slug = (kwargs.get("name") or "").strip().strip("/").lower()
        display = (kwargs.get("display_name") or "").strip()
        purpose = (kwargs.get("purpose")
                    or f"Workflow + tooling for {display}.").strip()
        modes = {m.strip() for m in (kwargs.get("mode") or "local").split(",")}
        valid = {"local", "private", "public", "egg"}
        bad = modes - valid
        if bad:
            return json.dumps({"ok": False,
                                "error": f"unknown mode(s): {bad}; valid: {valid}"})
        template_egg = kwargs.get("template_egg")
        dry_run = bool(kwargs.get("dry_run", True))

        if not all([owner, nb_slug, display]):
            return json.dumps({"ok": False,
                                "error": "owner, name, and display_name are required"})

        # 1. Load template
        try:
            template_files, source = _load_template(template_egg)
        except Exception as e:
            return json.dumps({"ok": False, "error": str(e)})

        # 2. Mint identifiers
        nb_uuid = uuid.uuid4().hex
        rappid = (f"rappid:v2:neighborhood:@{owner}/{nb_slug}:"
                   f"{nb_uuid}@github.com/{owner}/{nb_slug}")
        rapp_uuid_dashboard = uuid.uuid4().hex
        plant_ts = _now_iso()

        # 3. Determine visibility / join_via / license per mode
        is_public = "public" in modes
        is_private = "private" in modes
        visibility = "public" if is_public else ("private" if is_private else "local")
        join_via = "public_link" if is_public else "github_collaborator"
        license_str = "MIT" if is_public else "PROPRIETARY"

        # 4. Substitute tokens
        tokens = {
            "owner": owner,
            "nb_slug": nb_slug,
            "display_name": display,
            "purpose": purpose,
            "neighborhood_rappid": rappid,
            "rapp_uuid_dashboard": rapp_uuid_dashboard,
            "plant_ts": plant_ts,
            "visibility": visibility,
            "join_via": join_via,
            "license": license_str,
        }
        files = _substitute_tokens(template_files, tokens)

        # 5. Build the rar/index.json with fresh sha256s (after substitution)
        files["rar/index.json"] = _build_rar_index(files, owner, nb_slug)

        results: dict = {
            "schema": "neighborhood-factory-result/1.0",
            "ok": True,
            "dry_run": dry_run,
            "owner": owner,
            "name": nb_slug,
            "display_name": display,
            "rappid": rappid,
            "modes": sorted(modes),
            "template_source": source,
            "file_count": len(files),
        }

        if dry_run:
            results["files"] = sorted(files.keys())
            results["next_step"] = (
                f"Re-run with dry_run=False to materialize. Modes selected: "
                f"{sorted(modes)}."
            )
            return json.dumps(results, indent=2)

        # 6a. local mode → unpack to ~/brainstem-workspace/<nb_slug>/
        ws_path = None
        if "local" in modes:
            ws_root = os.path.expanduser(
                os.environ.get("NB_WORKSPACE_ROOT", "~/brainstem-workspace"))
            os.makedirs(ws_root, exist_ok=True)
            ws_path = os.path.join(ws_root, nb_slug)
            os.makedirs(ws_path, exist_ok=True)
            for path, body in files.items():
                full = os.path.join(ws_path, path)
                os.makedirs(os.path.dirname(full), exist_ok=True)
                with open(full, "wb") as f:
                    f.write(body)
            results["workspace"] = ws_path

        # 6b. egg mode → pack to ~/brainstem-eggs/
        if "egg" in modes:
            egg_dir = os.path.expanduser("~/brainstem-eggs")
            os.makedirs(egg_dir, exist_ok=True)
            ts_short = plant_ts.replace(":", "").replace("-", "")[:13]
            egg_path = os.path.join(egg_dir, f"{nb_slug}-{ts_short}.egg")
            with zipfile.ZipFile(egg_path, "w", zipfile.ZIP_DEFLATED) as zf:
                for path, body in files.items():
                    zf.writestr(path, body)
            results["egg_path"] = egg_path
            results["egg_size_bytes"] = os.path.getsize(egg_path)

        # 6c. private OR public mode → create + push GitHub repo
        if is_private or is_public:
            if _gh_repo_exists(owner, nb_slug):
                results["ok"] = False
                results["error"] = (
                    f"{owner}/{nb_slug} already exists. Pick a different "
                    f"name or delete the existing repo first."
                )
                return json.dumps(results, indent=2)
            ok, msg = _gh_create_repo(owner, nb_slug, display, public=is_public)
            if not ok:
                results["ok"] = False
                results["error"] = f"repo create failed: {msg}"
                return json.dumps(results, indent=2)
            pushed, push_errors = [], []
            for path, body in files.items():
                ok, msg = _gh_put_file(owner, nb_slug, path, body,
                                        f"plant: {path}")
                if ok:
                    pushed.append(path)
                else:
                    push_errors.append({"path": path, "error": msg})
            results["repo"] = f"https://github.com/{owner}/{nb_slug}"
            results["clone_url"] = f"https://github.com/{owner}/{nb_slug}.git"
            results["files_pushed"] = len(pushed)
            results["push_errors"] = push_errors
            if push_errors:
                results["ok"] = False

        results["next_step"] = (
            f"Done. Modes materialized: {sorted(modes)}. "
            + (f"Workspace at {ws_path}. " if ws_path else "")
            + (f"Egg at {results.get('egg_path')}. " if results.get("egg_path") else "")
            + (f"Repo at {results.get('repo')}. " if results.get("repo") else "")
            + "To share via sneakernet: pair the egg with `egg_hatcher_agent.py` "
            + "from the workspace's agents/ dir; recipient drops both, then "
            + "chats `EggHatcher from_egg=<path>`."
        )
        return json.dumps(results, indent=2)
