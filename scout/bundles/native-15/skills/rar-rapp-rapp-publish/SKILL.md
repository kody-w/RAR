---
name: "rar-rapp-rapp-publish"
description: "Submit any RAPP artifact to its right home. Pass a path to a single .py file, a rapplication directory, or a .zip bundle, and the agent will auto-detect whether it's an agent / rapplication / sense and open the matching [AGENT] / [RAPP] / [SENSE] issue in the right repo. Use this whenever the user wants to publish or contribute something to the RAPP ecosystem and you don't already know which store it belongs in."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp_publish_agent", "rar_sha256": "fc199e9cd0c478971f5c67d818d6405d32e0035974da2187e29292bf36adc6ed", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "0.2.3", "author": "RAPP", "tags": ["publish", "submission", "router", "ecosystem", "store", "registry"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_publish_agent.py` and embedded as the fenced Python below (sha256 fc199e9cd0c47897…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_publish_agent.py` first:

```bash
python3 rapp_publish_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_publish_agent.py   # or on stdin
python3 rapp_publish_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/616aZOz2JXmX1G8/cF2U1XsW3V0xIAACST2RUh+O6rYQeybWDz+73OVmVW22z09MxFDZihBnHv285xzM+5fvgXzlLfDt5+/WZxhfPvhW5yM0VB0U9E24Et7DutiOgTNdni/PwTDVKRBNB2m9lBM42Eosnw65G2d/HQwgnE8BIcumPL36+AwFk1WJYefuu2QFlXyA/hqCLquKqLgzf4QF0MSTe2w/XBoB/Dyp73oDuHcxB+0TXyY8uQQZEkzHZaiqg5A1fbHOJnAosOSJ+DtAJT4AxDafJHB/ygAPoxJMyYfvNouaT4Y1sEU5UCzw5+5k6g5/wGo/vy27ePGFjVb/I9DMY5zcig+F3zaOCRd+9PBBdymvBjf8pvkBRR4U8wjuFmCBjgEGN7NYVWM+dumqG2moQjnKTmMwEfTh1xA8l704c8kasdtnJL6Q8etnQ9x2/wBOLwakiDeDmXTLkBWEeWHEXgK6DQdwqRqm2wE6v0E4pWsQd1Vyfjt5z//xw/fCnD/7ee/fIsqEIx3UIE7jE99uLeHwIIqaDLwpttA3Bvw3CVD2g41+CpO0sPX0x/HpEp/OPzrv5ZLMGTjn37+3hy+LhD9t2///fD56qcsmf74/dvnt9+//XD4/m3skuj7tz/9bck0bH/H4H0V6e98/v33Ff+J5n0NyTQPzeGtzU+/vKn++Kf/ltFndvyfWX3S/fHLuv9et48S+L/Q7oPuv2b5Rfgc2+aneK678Y9/+f4tGYZ2AHwP6fdvc/OOdPMl+OfDXz5v/vr921//jlWyRkk3HcSPP28Fg/GQ/Pz/Imqchj8mf/rrn779FeRKA57mDznvVPmXfzmoRTS0Y5tOBztqZ5DzczMVdfK9+d4476QHvx8F8U78sQhBbX/SdUP7TD5d1qaHX//Huwjh98cvX7Xwy0d5/vrTwQHLW1BQRRNUHxXwvfmsXMC6GxJQR68kPoTblPwI0vDH9827DH/9Z2YAVX79KJqvKrWO8iEKunGukp/eCt9AgX6pFwF8SNYkepdh1UZA8huOxh+AIWNbvb4qeizfGPM7Jn3wBg74+c3s119/DYMx/958Vg1++MTIEQYEv6tz+PFHYEJaveHie5NEeXv4w1/++ofD/zz8d6s+mL9lfMDnp3uBhoqtawBts7lO3rDyjhUAhA/3/uWvX44EbBoAPCAYRVokn4uroimT+Dev2mfuR4ykAGSkH+BRdy0AcIBBxfTTQU4Pv+v7AW/D9MbvvB2nQ5wAuIyTJtoA1wCY87snm3Y6jABexxTA9vwBh8nh13AIPlSsf4kA+a8H9WgAnGurN9gBNT+IwOK2AdBc/R7z5nf0BCDO/8bip4P2gaxdAKKeD8GXjHfbecfl3Sq+ln90mSZZvjdv3EvervoA/k/3ACLgmegrpD++Yw4Aua5BYMffZH/QBBPIOacNgPDhO+gXn5kcDO9QRC1QZTtkcxEHTZT821dKjXk7V/GH/756wFcU4q+ofOTgf5m1h+8zhqDEYfy/b61vXtxv7TR8K/bpgXdo/r4rjr+3xeX9BrSTP4Dsztp3eX3k8eHwr8Bjf+PwVufrAlqhLPbRJsffWyPwUtnG248LbHHWb8v/ocV+tuv/vPyzn/7DcsP4xX53sN+4fHbmj6D87fpHLr814//E5b3wN14gXJ/d9MvLwPS4TcZ3C20SEAzgy48W+iaZ2q6t2mz76WAHdXJw/Td8/pqBGHTzmP/6FZfvIEl/z5MfgPAUZOAHTs7vhADB/6q0NzaNH6GRf0s+ACJT0h3Ed5n+k+H/gqKHPxoDUGIE9Y0gCPZbJnwolw9J8uP4adXvU8GfwFQFTDoChJ6Kaf7wOAfyJAJe833Z/+GQfKTnG7bHH981/JlW4/imzIAnvjeAcztn+YcUMNyB8v+M3JsalF3cRh8YA5z1Z/+3ySet2uVdRAAWPzPtOY8ABD6mik+seaMjwBTQ7OJPJ9hTXBXhoW0q4GALYNV4OJ1/cfSLqIHB6iQ7Z5f/ekyHtj4kzevN4EtgBEDvo3IBcBcALEGJgTD8cIiH7UdQUJ/yuqH4GLHe4Q62qgV4CH08udb1HemPZHo/f/D83oAIzkEF9HlPPUX0zptvPzdzVf3wrQEZ8I/j0XsSAoADhjTQ294jFGhqYBiaiuTj6bMfv+/+cUD+LLyfD1+u2T5n1t9Kefmy5bPW38j7b1/3f7fiH6bTz6r/PRKAHAw9P3+a/kkA+L0RfACNbvwYAJsZDG9//tIEfPEp4H0Dln4DQ+G0dW9jQRaDhe/OD7z6C/DqP1sDWgJIdeD3f1DuU/hvLv/NprfKb0VAc/1Q9a3Ll6QQIH8SNG9R793AP8u5/q0Lf06/f9s0vCEJfmM2+HxvCP6O7W8GALZD0s8A1uO34V+h+ZuhbfieRj6kV8H0Odz+5RuIbBAHU/AV26+BBZAPwfDj+EZ1GP0JAdLA8ydYg3f/u1Hmi2zMA9BeAV0aoSybsFGMRATNsDSakhFFxwzKxBSBkDGOJQiCkyxNxAGGMnSCseAnTHEqiCMK2AGi1c5DlPzyRp7iLRrBqBRlQgJh8QRPIoSOsBRwiGOWQhkCZxIEQwIkTP62tCya+MueTyXfnvp9qvrI4k+z/vItpAhAeSZGmfu8jjCEML5vPK3m+oJ51+mvdzEQqwXFU6y7PR3Vj322GB6+XdoaW0dXUc1U28oz86hytmMJl9d8AQz6dJbgwu/oruT5gpft9OERbdruxWjXetNRoPCp+M5v8ILQMU651pNIHrJW86y0eciLZEaEaYwkw6EmVSSRixhxhDXpomXjU3g+t6U0eHX0X2eDe4qSSkrlfUdLt+h2Misx56ZbUKPqiHLSLPXlPrvqfi3ZZ3dTAul0zjv1LnZHBkqZPceR1adJm4Xv1OUO7OFECr5DyXN8GtXjPNJMENFbLrucmr2aglymsvBwnUQskeaWVghXlSFkoReaBTYLB2/5HS7dblomXT9Gy40lRqS/LOhLJ8tGN5/nNuYz+j4Q6xmWTIOGGRSHdkW/rXcledIEAT8v7P101UNFeqL0a2haXEWlMLJzzwhO5OhGptDWkrZKaDJqL3/cryO3NKpkRhxxLasItjLz2hKwz69p6J65m9np1mYRV3G1JOMeKNIu5nt91U3IjIV4jcpYYApLa2sbiqZaekHOSGwRMyYjWQrLtOpysFNHZ+UXPQobhKC468YQ2xmhiFq/S+Kxuhbd4oi0oByfNH95LBwOc9W6qL7uwg/VnWqMHNnEqG3sFj2uR4g7oxSTGOKjcdJ8UjOCXprg2DH1PfOyqqWve809B/L0WIYlY1qKOwUPriuh1HmS6CmEK+zeaSNiy/4YOpZx0UUh34TX68VpW1kf2fZ554RaKhIxIyCg4DO4Sy1HuLOxSGxuP7OTyLm+8Dh1XcqwJzVnRgJhsvN8le2YQ0/mAMHMVRU0H7J4SSTvYhlzSGPMGcEzLHsPG5i+MmZ6e7BQ/NRYKL3coH1Qys3PGRuTc4+c6kbiNx1mEjIbs6spFL71KHuUvK3nyyrJ5lCtlgF7NxfiJNqZGKgZYKHd/NOSgFzP9MZreW5AN3dcqIny653LYINBC8JRVHW1Jz2qukcsDNQpWZ30sRNZA68WjE7EfZRoSYIFy2ApN7FWo9vll9noooP2UVbUerpdxXlbB12FUWcJxlO6rDYux5IGW7uP0EWyxLGuMOwtW4gLn2F5u4ozwVd6l9Jmi8LvZ/ZuxhfIXTaD2KxuH5h0HJxGwU3sZIgBIQjIuKVXGOGL1cgSiOtvfR6N3o4uib95UXu+KvvZHbJHgNYvIVeks+DJ+9PAx8fcD/G1S3giSpxMCMYrKUx1IA2CGKsn//X0su40gUSjYaRB8zjx6dPFTHGcEgb4FUJVYRwRme8buqLSc6MaiipMlpCduDaCn1iezg+IiLdLnjqgJnYoImYNo1itt7s28abbsIYI1cX8Sznak5xnD74XnQqiktThH21iwpfqLp82QSxTJSh2V2ii/ElrkE2r+Hp3tGdLRzZ63Lxzm43oXeGbSfQEu2ae7HznmwoNem3BkKuXCiFlWiq8ulRBBLn4cpKdOC9kMQ3HURKbUCKXkskuvkm0MnXThyrNrg8h1b2KSCJXrOoR5wKok6AnLjuPaiVaMTKHYLbR8uhmauzIxz6/MLBHXLwNuOnVMlfMFOTidO0xWN6wIw/VVL+XQmOI59a1GthZzZ01oHICBVTNoRPGexYSNCGwzJDAiwE/dIs7CpS+wfBVouEQbiIqJIhpVRzddjID9WKRdnyBruLKVxDpVcQJo+n6zvDk+eLA/Pmo2Mbo+cW+GmsgpDwy05fjfa61FJLGTQMwIUAWy1noy395hXWEFbcTnBIurIvyQqpAE6A1btYAjx7alas2fxHr7gaPefygEpw51dvAp2EuHFc6bkgqbto1mZOct5B+Ty333gq4bPQAbWLxvGJgPDzLR2lDCNxKGpwiTgqkGgRpOE+WoK4RE5fS82KppyzwO56mkbwZcBaS2AGNZGF+7X53Oo7zGXJfDreoFnlFcq43xSLvj5AcJXfjIhZc4Y0eTnsvEosy7bUdLb6ydzLOThLPLR3kz9SiMO3tHFh4+tpeZwTWnyxLrCSsOyN8luicDfyN6q+3QjRsFVVIbtwdXqb3/AKvUI5dOXVhEFWvHGAld4nKbbexRsUHFnrloyDz6dMmdb8ZyySmFQiXLTuwzskyBYtDjtRpfDZYD98dObEivnHke9M8H+y569AT7Y+ZtCQ5fIMeTcnXr9YWBvtqxoEX8zQ34C+hw87cw7X2p6/PS0Ll8FLN5yk/QdtDRFccoPGCrBBuauf9lL6awWcbqlQ4mr4qgssaWUwqFSwJ4kk4i/k6+Vekhl2KG+UyJvT8OnP+WLUrQXPqiPDJIx2dKQuCMBbzlLXkqDg1Knt06miMTS034z28NQltmQRy6bQpX6IspwraM3VPRfmFZED9poLv23YeI/pRzuxEqOEdw899hJwcBWxndTCbdUik5WvPUtWxJrcWGgaiXM/diW7DW7iVx/BpxQ9FvoyNlPf4tbqMrUHKGMswfrfCGazonLauF70QlsGw11nnPZG9PZVryT+RjNvw9fFE43xfBTKLzjriqqeQ2k53AxMVo6ps/XLh8s1JNtm81sakW37Q+dcFd6AzFUaygrsL/VrJqUTlY0sXt7s84yqzSztb3EeRgdSgIyzObwMtiCJRE4eixJ2dZF8VvddkLZvSlejXgcI2TCjjF/Nw017Cbx5rDxftVPBx0NkMzyXFmcj4XFXK1qwqN7nTva1a1Glj9bLgZIwIbxGfDudLiy/bUbt6TKAUt+WSdWpQZhL04C/cZU+QotlvEBJz1U0mVNe5Ptsy3diKxcHQp6tHIdIUDXbX5QRxtHNT4gGAF8s43Mblhmz5lzIQumMxLUbKEXaWnZ/SwvOtjL7Ms/2wL35ve0xRi7BSBpi8zaU4wOduuZdPPoMezFhyovEo4Gx6ojZm01mcLf5KC4viNsWJC46sRpruEiiA9/FhGF5sdjcjtJ28auRjzCIndoWrNrsLvHtnwz0hgQ8nxUdwQUJbgjmK3FVJ6/kGBQ+DzsvzjFLYavuT4ogV3QltUjFMCyazcndFRnXvC2VQEecd1ey2NdaknZFcx8+Euq0G8sTjRYEkIdSROyu78sW5hNGaVfG9Ol2sGF7qh2mnOoGhcoFgBI7TPMs9uW3HezJSZeiY01syHwU3tsw6eiEGp665wStMh/fFGX8VUAM2Qqb6WB7TwtWnNldNSDmfhBQtwrpDsv2WX3M9rytCRjWicwLDmuN7z5x6dizZNT7qC79jEEjLVW+v8fHMWWTwXFFJKaunJ3mXmFrYmT2N7gk9Q0feMIdU4k4ebXKajFeI/6DXtacx2s12r7n091c1WTdfsiPjgm0Z5uSJYy+hvzFeOZc6VJ2qTLkXtyhX8GMkcqh1JAtFLQvzXqulQz/uPWKqqM5WFgS2SVtAsUi3EwEin9iOTpBRF8hHhHTpje3toA4fgpzQD9MkHDBpxm2XeiN3HAPD19Hg/lL2QuSnLSyNzXDnxAJIUiCU3MGN4r/KNAv0psllm+FcE3mG2K25gqSDJ6bV+wGlzpeFJpLhmGMXo9DCdT76L3iRIP7Vk2nOZUjPjxjITgKf1BciFHGpMnddLblu3YeRucJHXvXV0oUK1Rroe0+lWf8UWeeSXKaWXUoviO78lS1mBIy0ivugH2SW96czflR3Fy+cLKRf9FYa1kM+o8+zYF55laRkFb27cdqlRVw9RNHRnReZnHX9DHbyTdSEo7mqZUQcV0XIsUdoPZTSxcgohcx8r4hBakXVpy/zcSYaBPHj5tFyLzY5c3j+gmC/2tlxaGnIvocLc+I4GG0w0oRvqG+cwfhrIarPITi66znFJmhES0Qxj70l049IX73B9qS66iYjVHYAJxCraWeGk85HwhxErYajFCdQA+9QRj8TF/Mlb8KmOVeEYSK1UkpIw2Xk0tj7sUpZLzzbxkBjncZwxxNpZZtqWIw77lnyKIhhFewtqOyUQi2R2KWVK+51etW2R4OTr2cYb5pJoWMuPah94rTMbHJTnq2a2YoHpgUW6djlwBNECCZ0/mThJzvb9e3mn40AoQJmjdqcu8br1kogkdjI97teZjQS08DUQg+cJlwthTxhjdyAGMbXYxLZMZlKOBogy0USX/b8yB0RfqRICz+wJLGM1kwg57JEggKV9wcN5g9ed8CGrZV2Be+qI0Xwnm9aYKMdaGu7X7YrlcnH69rPMYoNvqDRJIHVxH69goGupwfBCtsOdJmUUMosplzqbpStcCrCBvW8pfbDUxtsNwianuQIs8aLgLQ5mQ2fYzP/WEIDqlTi+qKFyxkVsqB81j5X5vMZvRKJ/IQEbzCfZoNAr5byk9uV1x7BQjoau4sMkrxumOzqLTK5A6xeSi/ZjsXjyqPyfaZ8WLvxvK7ieJQxEUHp9/7sdBdRcvFBfy5USvLIRSSZvb/B/Cv1zTvYYhAo1mxVv2jlZZfCKQHFm/a3DNsjm40gDcq7jr1DAh/jUU8xOrbvNJNxz+ecTcyZeCxX2rW01yt7CorvzzbJuElU8EviWld58pFdcI9ic9931+ODKE+npzjeMbDfVvntPFIIm/pi88zctgLNlpxQFrlFVico+9bQpKmHbrXD+OaXbg0SkG9dsyFfepX2aMxnzpLKE/F8noq5nkeBNYw9PHsXE1jUMaRfoSvapraJ627kT/4ZrSFVTAaKMSj7PNwfj9gny7wK74V0N++WdGe7hACOszLhzNro+oKmW90OWSiFbofUtYB2DloslvfqLuTzHATx6d5MV9uWOowGUGuKtIbHjhgeSVoTrVWYmOhsl/G0MgLbqvFCB0/v0pmhpOZ3dMtsF+VinoGU+ll5JEtWMec7kLpqcVrcLiR7NTx0H/hrdiMV6nYfW0f3cITtOZd/xlVQ+F68BYMHNT3ZbVVKBY/plAx2ko5TNcz9HZFRKMIo7mY928Cwk0vBTKgc1mwbjkQUKEI2So9LePX1V9GjEJgykkfmjMmscEpmU6GYnvbMIWd9j8PmNFwrM1Vwh2LnHMY2tzVp1Mot9dkoRayUzY1DUeQCti9UJJ/9vuwFXx/9ZW/UcKs1YRbnxnF6P2cTMiae6X0J8RjnA5ZoTOF8M9qeuBaSvZKuPKgeSaJPALWnOnlayXllVIvOjVAIzqxXtgXJcQFPzad797wO7Akz+HOJPRYuEIGST0+tc2R31iIbYFjJ3OqyNFugehwt5KHgm3ZMJaZTxUuQXILezMSnzZzE2w1pvG437s8yEkjnoarMBZnPeHZizhOhEW4jcxJrp1p2lZNMrjXc9gMhBpsBOEquo3s5594taMaem0+CH42qtJxN5f1v2ZbdnVxKby6V1BJaDLb8IuMt7B4n5Om62BMJyi3fsagP2sxzFy1C7YixXUGWbftlXEuDUOQZW0XyiPGQ6Jru4KrVtNbW+VbujizZtk3k/CrRlqvZlkFGrstimjnuumnOYBsPYUdjeC7MoHNqEMJ+XconzdywCwKtqCKxouXtc/ja+quYudOSrVXG+SeATioUyxdsQduqiQxZimoszgZ/Nzequ3ZSvwZzixmcqUsPYQkliEE9ARmI0+ve+hYlmLC4unok3q8sZ6ZqIYC2Khi84WmVVqkzYdNYdfQD4mJfSGLoYRDlOtpamy64rfWDqrlM9C2+3Rb3AQFfhWK2N9mRPm6VN19u93Kk+IU9uW63S5Hq6cSU8tK9DXfugWpM0EM2VzWZK8ni456Sc2dqAz3bips+FF7Du62TSq/mDOdoWXVkc+WpRihbjqD0+iyCnmgGxUn8YuRGKN9zSDE9Tb3rSNX05kssSiw6Mm5gInwZZBMt1MrlqoZ8n+ujdzWZwUGfBbofR0taUo7cy7HF4IQ9J5kG7/RIBho68yf6JtOvvrkze0Qdm07l+Da9n5rS5/M8gPdI7hjq2j/rk0Otwy2FEX/GaAG5riOcCB3FnveNhs4qu98k15CVMIiLen5K0ggl4RXBnMsF104NO1E1fPGj88C8dF0Ns+G+5lB438aaOqFQ6JJj/zgDWDyGy2bp1uKVGX6fqpcLJilLQpBCU/NNO1Eo5/ZQFZ+o6xAnl2dTmJmmOz5ZlXZctbrHRFTqy9fjSeovgcbrNlLG6OuWO2ruo8ZOp52P9ntO3WMt9+remBjfG3g1T3ff9rv8qslZR5nP1kJlhreVTrl5UP9QasToRgGxIpl/QNbgnp80T3rahfTyKxI/GWjxDWySJ6OlZYf16xHbbFjAno16nTtX9u7RpWdVKWoGUoQS3DgSTL8vrW9PRbEUQ3C+MsaCxDJqG7LZQvWLmRKwdS9lWxjpC0p4J7XvnMs+BCvrBcQxuns9i8cMXIXrmMRLY4sG3N1HpSxNS6CgHbnXK4rdrzR2RnaNl1sZukbMKY4lp9+DUzw6IYM98q7SwDB4dre1Vs5oaG0t7GBNlufPpUyX+jz0cjV5xrEkqVNFprf3fxxR1DxBI0DcWs3C8RlqsS1CSsY9LOI4B8ZlnUvtzu3aaxE2pm1IDPXa+93ziAca4O29INEF87Dz8JTxE+YpRT8TS8fVJuxoNuuN5hSIDq8knPSK8CHnyYeD54m7GWVuCNn5uKx0y/tT7flejYzdDVf9iq05sjRFrQuoGhKp15UMFYPYJn5iboQLxgisoGswwpqbHjby0O+YhfuEt2FY1OGGuDFQuvHihiGPE071q8WMUs9dBF64e+0qESWZ4snGdsqCdNdFV50MDzKp0WQj1mg9kFTXVJoCJTRBm1PjOPTjpdVw3LUw/mhvjchnegemMaVjxGUmO2HLRP+JMeLjlBA+yQT5+iTfm3m5C3tJc7xYQ2t8kEdU3y/Rs++bzlSmExEaOpgS9fk+rxzzuBjDeFoowdDA5lKzF7ibylPXspJ/s/aEQo0pYk+o68ORN7XC4K2YMOe3E87ZhUS2e4UjrmSA/SBmq8FdP+2oczRznKf7wuegog+5q83TKHfzFXExm0r0OXnpz09g+G0aU5N8CmUZeETaOtvcyWzRJFeRUxosjIR1h3P3Lj+KJ49R6zHmn1CVZg+Vz6hHf3ULT6FstfIVXtXWYB/hOyZOxhLVBISY5EUyJrzd4p4oqS0Y6ZmyjCN1Qy/LMwke4/VxSUf9lQcjPOab3apW7p8EwduuhT1cJsluQa70ozRd2RLa5lm6yKeFHwS7vg/z1qZ5FoTnKNetvUonS7FS4kIn9NVxOlaDMCPeDQvXw4WCAhRHT7Vcl/6aXG6qq/uIG8Lci8o9X5+6G5c+tnG+WLgMgEdbDZwAG9loj47BYvYxVhnyGKt698g55i4sfvNYiaV6BOe5mqf2KJpqdcugmxZ4HtsWOeeO0vNCIP6py/PHrb9r5UuoO8kWTLBVbMz8TNOvsdef9f4as6cxNox52kFGySii5MHltj9RCZEyobc5NTZTZyi6aJnOghoGO0/ktphBHNhYjNODZXWx0piVv2mX1mv0iticvA0fZ8GJqWLrqVa6Syh5T7Qprnvehtgxxjzigl2PhnNq7ujadxdZcKGadx0h5s1Hfu6YfB0L3Lw/NSWG7kqfpRKft86DtF6Rf8GwGMPuigUFqUJl0Wnl83LAtpWm2DTEtfzBxXTqYmz5IEH/bXhka92hn5IyrEAXb3yc6wwUzXPqOeN3/TzdKKhH0CEi0tEJ5PCIbXAs6llZ5wtch9cbasbBSgK97g6OFaEmda+75PuU7nFCGopOt9zI4EZbAbaZrlZrQ3rBKJdOB6fKhfhaVK8bcsU81GqRDiee0HVPGvg42K8c9QjDw/1RdyF1E0kPO2IzDvKooF6oXmXy4I8JvBNC8qCQx8T58mYngX/iq4mDdCIN0vDJlSJZQ1xC9ZQd9HmJcvi8HLX7pkYO+rrwQeX1N3K+ljvKvR6JYzr9YIoAuxrMmo6hjxlevYjW5c5VPoJUp4DlI7hit7oVDMcJk3USkQrZIHxib1J0OV+tQW/CgVEV4bFA9tLaMG3XrxGpTWZ7TPB910vYXFiZNulbojWuM2T+K1DrE9pfUeKBMyOP1sGAKCbyTAlBUlAtCknmJHgL6NZm8mqEYHxlF2PXgud0hBtYgK7TlZNbUYn7uUgBZj14WuqOjomWNxs/XxQfCh99GLy8c4wL9qBUOmn2PsRrJ74uCftMneWkUlbBTag5hCa7u/VeadS4LDbynPhgFIHb14rmbn3rIdWg9KcqleTL8683Vj65M8kd3W5CTprfssa+IcL5YWBpORkIBg9isQ3htaXouEtobHQ9K4futVl02F7ga032RShf+XpGqavTB+Y8++6lqFHyYcLxnQ7DXmm3I3VPxvRG5bTeRK8Xf52QjV+JqiS6zTO8LIQT/SzwvQYCL8J+319bJb7MMkvVItiNBbf1mGCcpXoWQLboQTTnxz2eyJsUFCg7H8+n0XIjpn2e2ltMd8QJYOxp8h77Ilvb3tq7zI7K8YzZr8aPxejR6AhUdMmY4VFQnu9jow0brtbFsxvavptovmllePV2cXJg27LnIzMpYMoSkgid66q3YdxRyw3HlJBiEVI6O742BO7IAtCkmaYmiDJ/cVG7K6VKJVd10zlniqvL/Un0ZXZsIPR5sZ5ZnG6J8bj3llyVy3VzsqEdTqjygu/4dhUYOSQnFac3mgC4YIWWHfpM9LgG/i2DySae7soxVLkjIyRnNlOeQ/QSyGKNffES3qt5pvIj6mmYbiivOVjcCQD8HWkJqLbZIAgYUebXmqBd4t5cl5Np3y7H4aaBbSK0O6VCdOsrjfNTtbu2pCEBKP2E4IXXXY3Y/XV8zuJ6olLr0l2Gy8vLdWryF6qA3avgnb2Tcc0Z3NLXp2+oPsyZhsmcJMbNOO7bD9/e516+DiD9lycE3yc6/r8dLPk8A9K+gMQmSt7nZd4ny3/+kPXzfy3+P374NkQFEP55Hmas5uzrWMmb/vOj+/3U1OcJnl/eR90BlPx2wGoKsveR9G9/R/f7wbT34Zn3ObrhfXrpt6Nub4r36bf3yyQrxmn4UOTjpPHHMR3kJ+wn/Ntf/xfIOP7BsjAAAA== -->
