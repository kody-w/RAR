---
name: "rar-rapp-rapp-publish"
description: "Submit any RAPP artifact to its right home. Pass a path to a single .py file, a rapplication directory, or a .zip bundle, and the agent will auto-detect whether it's an agent / rapplication / sense and open the matching [AGENT] / [RAPP] / [SENSE] issue in the right repo. Use this whenever the user wants to publish or contribute something to the RAPP ecosystem and you don't already know which store it belongs in."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp_publish_agent", "rar_sha256": "838117db87ab4909829de672e666504941b99c348d8bd5a9e3eb5a5542c69688", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "0.2.3", "author": "RAPP", "tags": ["publish", "submission", "router", "ecosystem", "store", "registry"]}
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
