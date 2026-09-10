"""factory_agent — plant a brand-new rapp-workspace/1.1 vault from the starter template.

The meta-agent for CEO / chief-of-staff style workspaces (portfolio, strategy,
projects, meetings, people, the rapp-projects frame authority) — the private,
local-first vault an AI keeps organized for ONE owner and ONE world of work.
Newer shape than the neighborhood-starter stack: this plants a *workspace*
(solo or hive), not an agent-team neighborhood. Drop into your local
brainstem agents/ directory and chat:

    WorkspaceFactory mode=local   owner=alice name=my-work   display_name="Alice's Work"
    WorkspaceFactory mode=private owner=alice name=my-work   display_name="Alice's Work"
    WorkspaceFactory mode=egg     owner=alice name=my-work   display_name="Alice's Work"

The factory:

  1. Pulls the canonical rapp-workspace-starter.egg from kody-w/RAR (or uses a
     local copy if airgapped — pass template_egg=/path/to/file).
  2. **verify_egg()**s it first — a rapp/1 §9 organism egg, integrity-checked
     before a single byte is trusted or unpacked (see `_verify_egg_bytes`; a
     stdlib-only reimplementation of the reference `verify_egg`, since this
     agent must stay dependency-free).
  3. Unpacks the template into memory and substitutes template tokens.
  4. **Re-mints `rappid.json`** — the template ships a placeholder identity;
     the factory always mints a fresh one (never reuses the template's) so no
     two planted workspaces ever collide on identity. Mint-once from here on:
     whoever owns the planted workspace must never re-mint again.
  5. Materializes the result based on mode:
       local   → unpacked at ~/rapp-workspaces/<ws_slug>/
       private → above + creates a GitHub-**private** repo + pushes (a
                 workspace holds PII by design — public mode is refused)
       egg     → packs a fresh, re-addressed .egg at ~/rapp-eggs/<ws_slug>-<ts>.egg
     Modes can be combined: mode="local,egg" produces both.

Unlike the neighborhood-starter factory, `public` is **not** a valid mode
here: a rapp-workspace/1.1 instance is meant to hold the owner's real,
PII-bearing operating data from the moment it's planted, so it is never
publicly hosted. The starter *template* (this stack's own .egg) is the
PII-free artifact that is safe to publish; a *planted* workspace is not.

Self-contained. Stdlib + `gh` CLI for the private mode. Default
dry_run=True; pass dry_run=False to actually materialize.
"""

from __future__ import annotations

import base64
import hashlib
import io
import json
import os
import re
import subprocess
import urllib.request
import uuid
import zipfile
from datetime import datetime, timezone

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


_DEFAULT_TEMPLATE_URL = (
    "https://raw.githubusercontent.com/kody-w/RAR/main/"
    "stacks/rapp-workspace-starter/rapp-workspace-starter.egg"
)
_RAPPID_RE = re.compile(r"^rappid:@([a-z0-9]+(?:-[a-z0-9]+)*)/([a-z0-9]+(?:-[a-z0-9]+)*):([0-9a-f]{64})$")
_LCLABEL_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
_MANIFEST_KEYS = {"schema", "variant", "rappid", "created_utc", "contents", "payload", "sig"}


def _now_iso() -> str:
    n = datetime.now(timezone.utc)
    return n.strftime("%Y-%m-%dT%H:%M:%S.") + f"{n.microsecond // 1000:03d}Z"


def _slugify(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", s.strip().lower()).strip("-")
    return s or "workspace"


def _mint_rappid(owner: str, slug: str) -> str:
    """rapp/1 §6.2 mint-once, keyless: Hb('rapp/1:rappid', uuid4 bytes)."""
    tail = hashlib.sha256(b"rapp/1:rappid\x0a" + uuid.uuid4().bytes).hexdigest()
    return f"rappid:@{owner}/{slug}:{tail}"


def _gh(args: list[str], input_bytes: bytes | None = None) -> tuple[int, str, str]:
    p = subprocess.run(["gh", *args], capture_output=True, input=input_bytes)
    return p.returncode, p.stdout.decode(errors="replace"), p.stderr.decode(errors="replace")


def _http_get(url: str) -> bytes | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "workspace-factory/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read()
    except Exception:
        return None


def _gh_repo_exists(owner: str, name: str) -> bool:
    rc, _, _ = _gh(["api", f"/repos/{owner}/{name}"])
    return rc == 0


def _gh_create_repo(owner: str, name: str, description: str) -> tuple[bool, str]:
    rc, out, err = _gh([
        "repo", "create", f"{owner}/{name}", "--private", "--description", description,
    ])
    if rc == 0:
        return True, out.strip() or f"https://github.com/{owner}/{name}"
    return False, (err or out).strip()


def _gh_put_file(owner: str, name: str, path: str, content: bytes, message: str) -> tuple[bool, str]:
    payload = {"message": message, "content": base64.b64encode(content).decode()}
    rc, out, err = _gh(
        ["api", "-X", "PUT", f"/repos/{owner}/{name}/contents/{path}", "--input", "-"],
        input_bytes=json.dumps(payload).encode(),
    )
    return (rc == 0), ("ok" if rc == 0 else (err or out).strip())


def _canonical(v):
    """RFC 8785 JCS restricted to str/int/bool/null/array/object (no floats)."""
    if v is None or isinstance(v, bool):
        return json.dumps(v)
    if isinstance(v, int):
        return json.dumps(v)
    if isinstance(v, str):
        return json.dumps(v, ensure_ascii=False)
    if isinstance(v, list):
        return "[" + ",".join(_canonical(x) for x in v) + "]"
    if isinstance(v, dict):
        keys = sorted(v.keys())
        return "{" + ",".join(json.dumps(k, ensure_ascii=False) + ":" + _canonical(v[k]) for k in keys) + "}"
    raise ValueError(f"non-I-JSON value in egg manifest: {type(v)}")


def _hb(space: str, b: bytes) -> str:
    return hashlib.sha256(space.encode() + b"\x0a" + b).hexdigest()


def _verify_egg_bytes(blob: bytes) -> tuple[bool, str, dict, dict]:
    """Stdlib-only reimplementation of the rapp/1 §9 `verify_egg` integrity
    check (contents hash-match, sorted paths, no zip-slip, schema/variant
    sanity). Returns (ok, reason, manifest, files). This agent refuses to
    unpack anything that fails this check."""
    try:
        z = zipfile.ZipFile(io.BytesIO(blob))
        manifest = json.loads(z.read("manifest.json"))
        files = {n: z.read(n) for n in z.namelist() if n != "manifest.json"}
    except Exception as e:
        return False, f"parse error: {e}", {}, {}
    if set(manifest.keys()) != _MANIFEST_KEYS:
        return False, "manifest missing/extra keys (§9.1)", {}, {}
    if manifest.get("schema") != "rapp/1-egg":
        return False, f"schema != rapp/1-egg ({manifest.get('schema')})", {}, {}
    if not _RAPPID_RE.match(manifest.get("rappid", "")):
        return False, "template rappid is not well-formed (§6.1)", {}, {}
    contents = manifest.get("contents")
    if not isinstance(contents, list):
        return False, "contents not a list (§9.1)", {}, {}
    paths = [c["path"] for c in contents]
    if any(p.startswith("/") or "\\" in p or any(seg in ("", ".", "..") for seg in p.split("/")) for p in paths):
        return False, "bad path grammar in manifest (zip-slip guard)", {}, {}
    if paths != sorted(paths, key=lambda x: x.encode("utf-8")) or len(paths) != len(set(paths)):
        return False, "contents not sorted / duplicate path (§9.1)", {}, {}
    if set(files.keys()) != set(paths):
        return False, "archive entry set != manifest contents (§9.1)", {}, {}
    for c in contents:
        if _hb("rapp/1:egg", files[c["path"]]) != c["hash"]:
            return False, f"content hash mismatch: {c['path']} (§5)", {}, {}
    return True, "ok", manifest, files


def _load_template(template_egg: str | None) -> tuple[bytes, str]:
    if template_egg:
        path = os.path.expanduser(template_egg)
        if os.path.isfile(path):
            return open(path, "rb").read(), f"local: {path}"
    egg_bytes = _http_get(_DEFAULT_TEMPLATE_URL)
    if egg_bytes is None:
        raise RuntimeError(
            "Couldn't load the starter egg. Pass template_egg=<path> or "
            "ensure internet access to kody-w/RAR."
        )
    return egg_bytes, f"network: {_DEFAULT_TEMPLATE_URL}"


def _substitute_tokens(files: dict[str, bytes], tokens: dict[str, str]) -> dict[str, bytes]:
    text_exts = {".md", ".json", ".txt", ".py"}
    out: dict[str, bytes] = {}
    for path, body in files.items():
        if os.path.splitext(path)[1] in text_exts:
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


class WorkspaceFactoryAgent(BasicAgent):
    metadata = {
        "name": "WorkspaceFactory",
        "description": (
            "Plant a brand-new rapp-workspace/1.1 vault (portfolio, strategy, "
            "projects, meetings, people, the rapp-projects frame authority) "
            "from the canonical starter template, with a freshly re-minted "
            "identity. Modes: local (on-device), private (GitHub-private "
            "repo — a workspace holds PII, so public is refused), egg "
            "(portable, re-addressed .egg for sneakernet). Combine with "
            "mode='local,egg'. Default dry_run=True."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "owner": {"type": "string", "description": "GitHub handle / owner slug (lowercase, hyphenated)."},
                "name": {"type": "string", "description": "Workspace slug, e.g. 'my-work'."},
                "display_name": {"type": "string", "description": "Human-readable name, e.g. 'Alice's Work'."},
                "world": {"type": "string", "description": "One line naming the single use-case domain this workspace covers."},
                "mode": {
                    "type": "string", "default": "local",
                    "description": "Comma-separated: local, private, egg. ('public' is refused — workspaces hold PII.)",
                },
                "template_egg": {"type": "string", "description": "Optional local path to the starter .egg; else fetched from kody-w/RAR."},
                "dry_run": {"type": "boolean", "default": True},
            },
            "required": ["owner", "name", "display_name"],
        },
    }

    def __init__(self):
        self.name = "WorkspaceFactory"

    def perform(self, **kwargs) -> str:
        owner = _slugify((kwargs.get("owner") or "").strip())
        ws_slug = _slugify((kwargs.get("name") or "").strip())
        display = (kwargs.get("display_name") or "").strip()
        world = (kwargs.get("world") or f"{display}'s work").strip()
        modes = {m.strip() for m in (kwargs.get("mode") or "local").split(",") if m.strip()}
        valid = {"local", "private", "egg"}
        if "public" in modes:
            return json.dumps({
                "ok": False,
                "error": "mode=public is refused: a rapp-workspace holds real, "
                         "PII-bearing operating data by design and must never be "
                         "publicly hosted. Use local, private, or egg.",
            })
        bad = modes - valid
        if bad:
            return json.dumps({"ok": False, "error": f"unknown mode(s): {bad}; valid: {valid}"})
        template_egg = kwargs.get("template_egg")
        dry_run = bool(kwargs.get("dry_run", True))

        if not all([owner, ws_slug, display]):
            return json.dumps({"ok": False, "error": "owner, name, and display_name are required"})

        try:
            egg_bytes, source = _load_template(template_egg)
        except Exception as e:
            return json.dumps({"ok": False, "error": str(e)})

        ok, reason, manifest, template_files = _verify_egg_bytes(egg_bytes)
        if not ok:
            return json.dumps({
                "ok": False,
                "error": f"template egg failed integrity verification, refusing to plant: {reason}",
                "source": source,
            })

        # Re-mint the identity — never reuse the template's placeholder rappid.
        rappid = _mint_rappid(owner, ws_slug)
        plant_ts = _now_iso()

        tokens = {
            "owner": owner, "ws_slug": ws_slug, "display_name": display,
            "world": world, "workspace_rappid": rappid, "plant_ts": plant_ts,
        }
        files = _substitute_tokens(template_files, tokens)

        # rappid.json is not token-templated (it's the placeholder identity
        # itself) — replace it wholesale with the freshly minted one.
        files["rappid.json"] = (json.dumps({
            "schema": "rapp/1",
            "rappid": rappid,
            "kind": "organism",
            "name": ws_slug,
            "parent_rappid": None,
            "workspace_spec": "rapp-workspace/1.1",
            "mode": "solo",
        }, indent=2) + "\n").encode()

        results: dict = {
            "schema": "workspace-factory-result/1.0",
            "ok": True,
            "dry_run": dry_run,
            "owner": owner,
            "name": ws_slug,
            "display_name": display,
            "rappid": rappid,
            "modes": sorted(modes),
            "template_source": source,
            "template_verify": "ok",
            "file_count": len(files),
        }

        if dry_run:
            results["files"] = sorted(files.keys())
            results["next_step"] = f"Re-run with dry_run=False to materialize. Modes selected: {sorted(modes)}."
            return json.dumps(results, indent=2)

        ws_path = None
        if "local" in modes:
            ws_root = os.path.expanduser(os.environ.get("RAPP_WORKSPACE_ROOT", "~/rapp-workspaces"))
            os.makedirs(ws_root, exist_ok=True)
            ws_path = os.path.join(ws_root, ws_slug)
            os.makedirs(ws_path, exist_ok=True)
            for path, body in files.items():
                full = os.path.join(ws_path, path)
                os.makedirs(os.path.dirname(full), exist_ok=True)
                with open(full, "wb") as f:
                    f.write(body)
            results["workspace"] = ws_path

        if "egg" in modes:
            egg_dir = os.path.expanduser("~/rapp-eggs")
            os.makedirs(egg_dir, exist_ok=True)
            ts_short = plant_ts.replace(":", "").replace("-", "")[:13]
            egg_path = os.path.join(egg_dir, f"{ws_slug}-{ts_short}.egg")
            with zipfile.ZipFile(egg_path, "w", zipfile.ZIP_STORED) as zf:
                for path, body in sorted(files.items()):
                    zf.writestr(path, body)
            results["egg_path"] = egg_path
            results["egg_size_bytes"] = os.path.getsize(egg_path)

        if "private" in modes:
            if _gh_repo_exists(owner, ws_slug):
                results["ok"] = False
                results["error"] = f"{owner}/{ws_slug} already exists. Pick a different name."
                return json.dumps(results, indent=2)
            ok, msg = _gh_create_repo(owner, ws_slug, display)
            if not ok:
                results["ok"] = False
                results["error"] = f"repo create failed: {msg}"
                return json.dumps(results, indent=2)
            pushed, push_errors = [], []
            for path, body in files.items():
                ok, msg = _gh_put_file(owner, ws_slug, path, body, f"plant: {path}")
                (pushed if ok else push_errors).append(path if ok else {"path": path, "error": msg})
            results["repo"] = f"https://github.com/{owner}/{ws_slug}"
            results["clone_url"] = f"https://github.com/{owner}/{ws_slug}.git"
            results["files_pushed"] = len(pushed)
            results["push_errors"] = push_errors
            if push_errors:
                results["ok"] = False

        results["next_step"] = (
            f"Done. Modes materialized: {sorted(modes)}. "
            + (f"Workspace at {ws_path}. " if ws_path else "")
            + (f"Egg at {results.get('egg_path')}. " if results.get("egg_path") else "")
            + (f"Private repo at {results.get('repo')}. " if results.get("repo") else "")
            + "Identity is re-minted and final — never re-mint rappid.json again; "
            + "reuse it on every future read."
        )
        return json.dumps(results, indent=2)
