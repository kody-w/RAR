---
name: "rar-rapp-rapp-publish"
description: "Submit any RAPP artifact to its right home. Pass a path to a single .py file, a rapplication directory, or a .zip bundle, and the agent will auto-detect whether it's an agent / rapplication / sense and open the matching [AGENT] / [RAPP] / [SENSE] issue in the right repo. Use this whenever the user wants to publish or contribute something to the RAPP ecosystem and you don't already know which store it belongs in."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp_publish_agent", "rar_sha256": "838117db87ab4909829de672e666504941b99c348d8bd5a9e3eb5a5542c69688", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "0.2.3", "author": "RAPP", "tags": ["publish", "submission", "router", "ecosystem", "store", "registry"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/rapp_publish_agent`. The original RAPP
agent is preserved byte-for-byte in `rapp_publish_agent.py` and in the RCI capsule.

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

rapp_publish_agent.py — submit any RAPP artifact to its right home.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "detect: classify the artifact without submitting; submit: classify and open the right [X] issue; spec: print the routing rules.",
      "enum": [
        "detect",
        "submit",
        "spec"
      ],
      "type": "string"
    },
    "dry_run": {
      "description": "If true, classify and print payload without opening an issue.",
      "type": "boolean"
    },
    "path": {
      "description": "Local filesystem path to a .py / dir / .zip.",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_publish_agent.py` and embedded as the fenced Python below (sha256 838117db87ab4909…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_publish_agent.py` first:

```bash
python3 rapp_publish_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_publish_agent.py   # or on stdin
python3 rapp_publish_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/rapp_publish_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rapp_publish_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/rapp_publish_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
    "version": "0.2.3",
    "description": (
        "Classifies a RAPP artifact (agent, rapplication, or sense) and opens the matching submission issue in its store repo via the GitHub API."
    ),
    "author": "RAPP",
    "tags": ["publish", "submission", "router", "ecosystem", "store", "registry"],
    "category": "platform",
    "quality_tier": "official",
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
        f"{_attestation_block('agent', submitter_login, src.encode('utf-8'), name)}"
        f"```python\n{src}\n```\n"
    )
    return title, body


def _build_rapp_issue(blob: bytes, manifest: dict, submitter_login: str | None = None) -> tuple[str, str]:
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
        f"{_attestation_block('rapplication', submitter_login, blob, name)}"
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
    name = f"{publisher}/{sense_name}"
    title = f"[SENSE] {name}"
    body = (
        f"Submission via `@rapp/rapp_publish_agent` (Constitution Article XXIX). "
        f"Auto-detected as a sense (no BasicAgent import, exports name/delimiter/"
        f"response_key/wrapper_tag/system_prompt). Routed to kody-w/RAPP_Sense_Store.\n\n"
        f"{_attestation_block('sense', submitter_login, src.encode('utf-8'), name)}"
        f"```python\n{src}\n```\n"
    )
    return title, body


# ── Attestation block (poor-man's blockchain — submitter signs by filing) ─

def _attestation_block(kind: str, submitter_login: str | None,
                       content: bytes, claimed_name: str) -> str:
    """Render the ATTESTATION block embedded in every submission issue.

    The block binds three things that anyone can independently verify:

      - submitter — the GitHub login that opened the issue (also recorded
        server-side by GitHub; the receiver workflow MUST verify it
        matches `issue.user.login`).
      - content_sha256 — hash of the raw submission bytes. The receiver
        re-hashes the source on extract; mismatch → reject. Anyone
        auditing later can recompute the hash from the issue body and
        confirm the file at `_first_commit_sha` matches.
      - claimed_name — the publisher/slug the submitter is asking the
        artifact to be registered under. The receiver MUST verify that
        the publisher portion equals `@<submitter_login>` (or appears
        in a verified-brand allowlist — not implemented yet).

    Together, these turn the GitHub issue into a signed ledger entry.
    The submitter's GitHub identity provides authenticity (you can't
    open an issue as someone else without compromising their account);
    the content hash provides integrity; the claimed name provides
    intent. All three are visible in plain text in the issue body."""
    from datetime import datetime, timezone
    sha = hashlib.sha256(content).hexdigest()
    submitter = f"@{submitter_login}" if submitter_login else "@unknown"
    submitted_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return (
        "## Attestation\n\n"
        "```attestation\n"
        f"kind: {kind}\n"
        f"submitter: {submitter}\n"
        f"submitted_at: {submitted_at}\n"
        f"claimed_name: {claimed_name}\n"
        f"content_sha256: {sha}\n"
        f"agent_version: rapp_publish_agent/0.2.0\n"
        "```\n\n"
        "*The receiver workflow verifies that `submitter` matches the "
        "GitHub issue author and that `claimed_name`'s publisher prefix "
        "equals the submitter (or is on the verified-brand allowlist). "
        "Receipt of a validated submission is recorded by promotion to "
        "the registry; the commit graph is the audit log.*\n\n"
    )


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
            "name": self.name,
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
            title, body = _build_rapp_issue(blob, manifest, submitter)
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
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
