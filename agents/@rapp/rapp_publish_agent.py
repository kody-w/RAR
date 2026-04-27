# rapp-validator: allow-template-placeholders (this file embeds the
# placeholder string list as constants for local validation)
"""rapp_publish_agent.py — submit any RAPP artifact to its right home.

A single bare agent that auto-detects whether what you've got is:

  * a bare agent.py        → opens [AGENT] in kody-w/RAR
  * a rapplication bundle  → opens [RAPP]  in kody-w/RAPP_Store
  * a sense file           → opens [SENSE] in kody-w/RAPP_Sense_Store

so the publisher doesn't need to know the topology. Same UX as `git push` —
one command, infrastructure routes the bytes.

Implements step E of kody-w/RAPP_Store#11 (Proposal 0002 — the three-store
ecosystem). Per Constitution Article XXIX, every cross-repo submission goes
through the destination repo's documented [X] issue flow. This agent just
classifies and forwards.

Stdlib only. Reads GH_TOKEN / GITHUB_TOKEN from env for issue creation.
Without one, dry-runs and prints the payload + the URL to file the issue
manually.
"""
from __future__ import annotations

import ast
import base64
import hashlib
import io
import json
import os
import re
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent  # local brainstem
except ImportError:  # pragma: no cover
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        from openrappter.agents.basic_agent import BasicAgent  # type: ignore


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/rapp_publish_agent",
    "display_name": "RappPublish",
    "version": "0.1.0",
    "description": (
        "Submit any RAPP artifact (agent, rapplication, sense) to the right "
        "store. Auto-detects type and opens an [AGENT]/[RAPP]/[SENSE] issue "
        "in kody-w/RAR / kody-w/RAPP_Store / kody-w/RAPP_Sense_Store "
        "respectively. Replaces the rapplication-only publish_to_rapp_store "
        "agent with a unified router covering all three peer stores."
    ),
    "author": "RAPP",
    "tags": ["publish", "submission", "router", "ecosystem", "store", "registry"],
    "category": "platform",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {"args": {"action": "submit", "path": "/path/to/my_thing"}},
}


# ── Routing constants ─────────────────────────────────────────────────────

DEST = {
    "agent": {
        "repo": "kody-w/RAR",
        "issue_prefix": "[AGENT]",
        "spec": "https://github.com/kody-w/RAR",
    },
    "rapplication": {
        "repo": "kody-w/RAPP_Store",
        "issue_prefix": "[RAPP]",
        "spec": "https://github.com/kody-w/RAPP_Store/blob/main/SPEC.md",
    },
    "sense": {
        "repo": "kody-w/RAPP_Sense_Store",
        "issue_prefix": "[SENSE]",
        "spec": "https://github.com/kody-w/RAPP_Sense_Store/blob/main/SPEC.md",
    },
}

PROPOSAL_URL = (
    "https://github.com/kody-w/RAPP_Store/blob/main/docs/proposals/0002-three-stores.md"
)
CONSTITUTION_XXIX = (
    "https://github.com/kody-w/RAPP/blob/main/CONSTITUTION.md"
    "#article-xxix--use-the-upstreams-front-door"
)


# ── Detection rules (Article XXVII / XXXI mechanical test) ───────────────

SENSE_REQUIRED_EXPORTS = ("name", "delimiter", "response_key", "wrapper_tag", "system_prompt")
ACCEPTED_BASIC_AGENT_IMPORTS = (
    "from agents.basic_agent import BasicAgent",
    "from basic_agent import BasicAgent",
    "from openrappter.agents.basic_agent import BasicAgent",
)


def detect_artifact_type(path: Path) -> tuple[str, str]:
    """Decide what `path` is. Returns (kind, reason).

    kind ∈ {'agent', 'rapplication', 'sense', 'unknown'}.
    """
    p = Path(path)

    # Bundle (directory with manifest.json) → rapplication.
    if p.is_dir() and (p / "manifest.json").is_file():
        try:
            m = json.loads((p / "manifest.json").read_text())
            if m.get("schema") == "rapp-application/1.0":
                return "rapplication", "directory has manifest.json with schema=rapp-application/1.0"
        except json.JSONDecodeError:
            pass

    # .zip → look inside; rapplication if it contains a manifest.json.
    if p.is_file() and p.suffix == ".zip":
        try:
            with zipfile.ZipFile(p) as zf:
                for info in zf.infolist():
                    if info.filename.endswith("manifest.json"):
                        return "rapplication", f"zip contains {info.filename}"
        except zipfile.BadZipFile:
            return "unknown", f"{p.name} is not a valid zip"

    # .py file — could be a bare agent or a sense.
    if p.is_file() and p.suffix == ".py":
        src = p.read_text(encoding="utf-8", errors="replace")
        try:
            tree = ast.parse(src)
        except SyntaxError as e:
            return "unknown", f"{p.name} has syntax errors: {e}"

        # Sense check first — senses don't import BasicAgent and export
        # the 5 module-level strings.
        if not _imports_basic_agent(src):
            module_names = _module_string_names(tree)
            if all(req in module_names for req in SENSE_REQUIRED_EXPORTS):
                return "sense", "exports name/delimiter/response_key/wrapper_tag/system_prompt"

        # Agent check — has a class extending BasicAgent + perform().
        if _imports_basic_agent(src):
            for node in tree.body:
                if isinstance(node, ast.ClassDef) and node.name.endswith("Agent") and node.name != "BasicAgent":
                    bases = {b.id if isinstance(b, ast.Name) else
                             (b.attr if isinstance(b, ast.Attribute) else None)
                             for b in node.bases}
                    if "BasicAgent" in bases:
                        if any(isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "perform"
                               for n in node.body):
                            return "agent", f"class {node.name}(BasicAgent) with perform()"

    return "unknown", "no manifest.json (rapp), no BasicAgent class (agent), no sense exports"


def _imports_basic_agent(src: str) -> bool:
    return any(imp in src for imp in ACCEPTED_BASIC_AGENT_IMPORTS)


def _module_string_names(tree: ast.Module) -> set[str]:
    """Module-level names that are assigned a string literal."""
    out = set()
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    try:
                        v = ast.literal_eval(node.value)
                        if isinstance(v, str):
                            out.add(tgt.id)
                    except Exception:
                        # Tolerate string concatenation
                        if isinstance(node.value, ast.BinOp) and isinstance(node.value.op, ast.Add):
                            out.add(tgt.id)
    return out


# ── Issue-body construction ──────────────────────────────────────────────

def _extract_manifest_name(src: str) -> str:
    """Pull __manifest__['name'] (e.g., '@rapp/foo') from source for issue title."""
    m = re.search(r'__manifest__\s*=\s*\{[^}]*?"name"\s*:\s*"([^"]+)"', src, re.DOTALL)
    return m.group(1) if m else ""


def _extract_sense_name(src: str) -> str:
    m = re.search(r'^\s*name\s*=\s*"([^"]+)"', src, re.MULTILINE)
    return m.group(1) if m else ""


def _bundle_dir_to_zip(rapp_dir: Path) -> bytes:
    rapp_dir = Path(rapp_dir)
    rid = rapp_dir.name
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(rapp_dir.rglob("*")):
            if p.is_file():
                zf.write(p, f"{rid}/{p.relative_to(rapp_dir).as_posix()}")
    return buf.getvalue()


def _build_agent_issue(src: str, submitter_login: str | None) -> tuple[str, str]:
    name = _extract_manifest_name(src) or "@unknown/agent"
    title = f"[AGENT] {name}"
    body = (
        f"Submission via `@rapp/rapp_publish_agent` (Constitution Article XXIX). "
        f"Auto-detected as a bare agent (BasicAgent subclass with perform). "
        f"Routed to kody-w/RAR per Article XXVII/XXXI.\n\n"
        f"```python\n{src}\n```\n"
    )
    return title, body


def _build_rapp_issue(blob: bytes, manifest: dict) -> tuple[str, str]:
    name = manifest.get("publisher", "@unknown") + "/" + manifest.get("id", "id")
    title = f"[RAPP] {name} v{manifest.get('version', '0.0.0')}"
    sha = hashlib.sha256(blob).hexdigest()
    b64 = base64.b64encode(blob).decode("ascii")
    wrapped = "\n".join(b64[i:i + 76] for i in range(0, len(b64), 76))
    meta = {
        "submission_type": "bundle",
        "id": manifest.get("id"),
        "version": manifest.get("version"),
        "publisher": manifest.get("publisher"),
        "name": manifest.get("name"),
        "category": manifest.get("category"),
        "tags": manifest.get("tags", []),
        "bundle_bytes": len(blob),
        "bundle_sha256": sha,
    }
    body = (
        f"Submission via `@rapp/rapp_publish_agent` (Constitution Article XXIX). "
        f"Auto-detected as a rapplication bundle (manifest.json with "
        f"schema=rapp-application/1.0). Routed to kody-w/RAPP_Store.\n\n"
        f"## Rapplication Submission\n\n"
        f"**Mode:** bundle\n\n"
        f"```json\n{json.dumps(meta, indent=2)}\n```\n\n"
        f"<details><summary>Bundle (base64-encoded zip)</summary>\n\n"
        f"```bundle\n{wrapped}\n```\n"
        f"</details>\n"
    )
    return title, body


def _build_sense_issue(src: str, sense_name: str, submitter_login: str | None) -> tuple[str, str]:
    publisher = f"@{submitter_login}" if submitter_login else "@unknown"
    title = f"[SENSE] {publisher}/{sense_name}"
    body = (
        f"Submission via `@rapp/rapp_publish_agent` (Constitution Article XXIX). "
        f"Auto-detected as a sense (no BasicAgent import, exports name/delimiter/"
        f"response_key/wrapper_tag/system_prompt). Routed to kody-w/RAPP_Sense_Store.\n\n"
        f"```python\n{src}\n```\n"
    )
    return title, body


# ── HTTP / GH issue API ──────────────────────────────────────────────────

def _http_post_issue(repo: str, payload: dict, token: str) -> dict:
    url = f"https://api.github.com/repos/{repo}/issues"
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, method="POST", headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "rapp-publish-agent/0.1",
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace") if hasattr(e, "read") else ""
        raise RuntimeError(f"GitHub API HTTP {e.code}: {body}") from e


def _whoami(token: str) -> str | None:
    try:
        req = urllib.request.Request("https://api.github.com/user", headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
        })
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read()).get("login")
    except Exception:
        return None


# ── BasicAgent entry ──────────────────────────────────────────────────────

class RappPublishAgent(BasicAgent):
    def __init__(self):
        self.name = "RappPublish"
        self.metadata = {
            "name": "rapp_publish",
            "description": (
                "Submit any RAPP artifact to its right home. Pass a path to a "
                "single .py file, a rapplication directory, or a .zip bundle, "
                "and the agent will auto-detect whether it's an agent / "
                "rapplication / sense and open the matching [AGENT] / [RAPP] "
                "/ [SENSE] issue in the right repo. Use this whenever the "
                "user wants to publish or contribute something to the RAPP "
                "ecosystem and you don't already know which store it belongs in."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["detect", "submit", "spec"],
                        "description": (
                            "detect: classify the artifact without submitting; "
                            "submit: classify and open the right [X] issue; "
                            "spec: print the routing rules."
                        ),
                    },
                    "path": {
                        "type": "string",
                        "description": "Local filesystem path to a .py / dir / .zip.",
                    },
                    "dry_run": {
                        "type": "boolean",
                        "description": "If true, classify and print payload without opening an issue.",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get("action", "spec")
        try:
            if action == "spec":
                return self._spec()
            if action == "detect":
                return self._detect(kwargs)
            if action == "submit":
                return self._submit(kwargs)
            return json.dumps({"error": f"unknown action: {action}"})
        except Exception as e:
            return json.dumps({"error": str(e)})

    def _spec(self):
        return json.dumps({
            "purpose": (
                "Single submission entry point for the RAPP three-store ecosystem. "
                "Auto-detects artifact type and routes through the destination "
                "repo's [X] issue flow per Article XXIX."
            ),
            "routing": {
                kind: {"repo": d["repo"], "prefix": d["issue_prefix"]}
                for kind, d in DEST.items()
            },
            "detection_rules": {
                "rapplication": "directory or .zip containing manifest.json with schema=rapp-application/1.0",
                "agent": ".py file importing BasicAgent + class *Agent(BasicAgent) with perform()",
                "sense": ".py file with no BasicAgent + module-level name/delimiter/response_key/wrapper_tag/system_prompt strings",
            },
            "constitution": [
                "Article XXVII / XXXI — what artifact goes where",
                "Article XXIX — use each repo's documented submission flow",
            ],
            "proposal": PROPOSAL_URL,
        }, indent=2)

    def _detect(self, kw):
        path = kw.get("path")
        if not path:
            return json.dumps({"error": "path is required"})
        p = Path(path).expanduser().resolve()
        if not p.exists():
            return json.dumps({"error": f"path not found: {p}"})
        kind, reason = detect_artifact_type(p)
        return json.dumps({
            "path": str(p),
            "kind": kind,
            "reason": reason,
            "destination": DEST.get(kind, {}),
        }, indent=2)

    def _submit(self, kw):
        path = kw.get("path")
        dry_run = bool(kw.get("dry_run"))
        if not path:
            return json.dumps({"error": "path is required"})
        p = Path(path).expanduser().resolve()
        if not p.exists():
            return json.dumps({"error": f"path not found: {p}"})
        kind, reason = detect_artifact_type(p)
        if kind == "unknown":
            return json.dumps({
                "error": "could not classify artifact",
                "reason": reason,
                "hint": "see action='spec' for the detection rules",
            })

        token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
        submitter = _whoami(token) if token else os.getenv("GITHUB_ACTOR")

        if kind == "agent":
            src = p.read_text(encoding="utf-8", errors="replace")
            title, body = _build_agent_issue(src, submitter)
        elif kind == "sense":
            src = p.read_text(encoding="utf-8", errors="replace")
            sense_name = _extract_sense_name(src) or p.stem.replace("_sense", "")
            title, body = _build_sense_issue(src, sense_name, submitter)
        elif kind == "rapplication":
            if p.is_file() and p.suffix == ".zip":
                blob = p.read_bytes()
                # Pull manifest out of the zip for title metadata
                with zipfile.ZipFile(p) as zf:
                    mpath = next((i.filename for i in zf.infolist()
                                  if i.filename.endswith("manifest.json")), None)
                    manifest = json.loads(zf.read(mpath)) if mpath else {}
            else:
                blob = _bundle_dir_to_zip(p)
                manifest = json.loads((p / "manifest.json").read_text())
            title, body = _build_rapp_issue(blob, manifest)
        else:
            return json.dumps({"error": f"no submission builder for kind={kind}"})

        repo = DEST[kind]["repo"]

        if dry_run or not token:
            return json.dumps({
                "ok": True,
                "dry_run": True,
                "kind": kind,
                "destination_repo": repo,
                "title": title,
                "reason": "dry_run" if dry_run else "no GH_TOKEN/GITHUB_TOKEN in env",
                "manual_url": f"https://github.com/{repo}/issues/new",
                "body_preview": body[:500] + ("..." if len(body) > 500 else ""),
            }, indent=2)

        try:
            resp = _http_post_issue(repo, {"title": title, "body": body}, token)
        except Exception as e:
            return json.dumps({"ok": False, "error": str(e), "kind": kind})
        return json.dumps({
            "ok": True,
            "kind": kind,
            "destination_repo": repo,
            "issue": resp.get("number"),
            "html_url": resp.get("html_url"),
            "title": title,
        }, indent=2)