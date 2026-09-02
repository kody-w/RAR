---
name: "rar-rapp-rapp-publish"
description: "Submit any RAPP artifact to its right home. Pass a path to a single .py file, a rapplication directory, or a .zip bundle, and the agent will auto-detect whether it's an agent / rapplication / sense and open the matching [AGENT] / [RAPP] / [SENSE] issue in the right repo. Use this whenever the user wants to publish or contribute something to the RAPP ecosystem and you don't already know which store it belongs in."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp_publish_agent", "rar_sha256": "fc199e9cd0c478971f5c67d818d6405d32e0035974da2187e29292bf36adc6ed", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_publish_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/rapp-publish:7f62383e691ef4c6eff9955b250fdcd251d028676bc5c59cf17ec5a251147465", "kind": "skill"}, "version": "0.2.3", "author": "RAPP", "tags": ["publish", "submission", "router", "ecosystem", "store", "registry"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/rapp_publish_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_publish_agent.py` is
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/616aY/jSJLlXxFiPnT3MCt5XzUYYEmRlCjxPiRKnYMq3qR4X+JR2/99XRGR2VXTPbOzwDIBJQ93M3M7nj0P+G9v/jRmTf/285vFGcbbl7coHsI+b8e8qcFLewqqfNz59bp7fd/5/ZgnfjjuxmaXj8Ouz9Ns3GVNFX/dGf4w7Pxd64/Z67O/G/I6LePd13bdJXkZfwGver9tyzz0X+J3Ud7H4dj065dd04OPX7e83QVTHb2PraPdmMU7P43rcTfnZbkDpjY/RfEIJu3mLAZfe2DEn4DS+nMY/EcF8G6I6yF+l9W0cf0usPLHMAOW7f7KHUTN+Q8w6q+vtb3f2KJmi/+xy4dhinf5x4SPNfZx23zduUDamOXDS38dP4EBrxHTAG5mvwYOAQtvp6DMh+y1prCpxz4PpjHeDcBH47teMOQ16d2fcdgM6zDG1buNazPtoqb+E3B42cd+tO6KupmBrjzMdgPwFLBp3AVx2dTpAMz7CuIVL37VlvHw9vNf/+PLWw7u337+7S0sQTBeQQXuMD7s4V4eAhNKv07Bl3YFca/Bcxv3SdNX4FUUJ7vPpz8PcZl82f3rvxaz36fDX37+Vu8+LxD9l2//fffx6Wsaj3/+9vbx9tvbl923t6GNw29vf/n7lLFffyfgdeXJDzn//mPGfxrzuvp4nPp697Lm6y+vUX/+y38r6CM7/u+iPsb9+XN1/71t7yXwP7Dufdw/F/k58DE09ddoqtrhz799e4v7vumB3F3y7W2qX5GuPxX/vPvt4+Zv397+9jtR8RLG7bgT3/97GegPu/jn/xdVw9j/Of7L3/7y9jeQKzV4mt71vFLlX/5lp+Zh3wxNMu7ssJlAzk/1mFfxt/pb7byS3ml8kKvR7lf7LCvK1yr6FVTKezKD1PGnctwdej8vd23fPOIPFzbJ7tf/9SpK+PXzy2dt/PJerr9+3TkZkN6ACstrv/yEmPdKBnLDLA6LYap+er5EA7Wf9Wjt5V3ot8NUxv+2+/UfxQK8edn1rQau8PMaTAT11Ta93+fl+nKZvwvWMf4JVA4Akr4py8APi93rZ2q/vhZ7BcX96YIQYEu8xOGrhMsmBEa+oGz4Avw8NOXzEw2G4oVPP/DsvZiB835+Cfv1118Df8i+1R8Vh+8+8HWAwYAfBu9++qnt46R8Qc23Og6zZven3/72p93/3v13s96Fv3S8Q+87VsXAwpOtawCp06mKX5D0ijMAk/dQ/Pa3D6e/rKsBaAEEy5M8fp8MpP09rq8VfETiexjAml8mxv2npj/67QVS5Ts8xUs+jMOXb/U76r5Aes4Ban468WPyh+u/x/VDzysmw6cPQZySvqnex76n1CuYYdNHX3dysvvhqXdQ7sdXRLNmGEEWApCP4jpcwUx//HsI62bcDaAnDAnoNQCtv9Uvyb8GQPTLOdUvIRj+607dGwCdm/IF0cBB7+rB7KbOX4H/TMz6B+T/CeQY/13E15323g9aH2Rk1vvvjSLevZrlKyNeDe5z/ntvrON59wLr+BWj9271nnn/NJt33yYMQYnd8D9vxi9Z3PcGHPj99z767pbf9dHhRyOdX19AA/oTyOm0eRXge/budv/6qpcfEl7mfF7AKpTF3hvr8KOZAvcUTbT+NMMWZ32f/oem/NHg//P0jw78h+mG8Yv96nnfpXz08lf5/Q7u/ijle/v+T1JeE7/L+lYPH/3308tg6VETD6+mW8cvrGg+mu5ryNi0Tdmk69ed7VfxzvVe6PFrCmLQTkP262dcAIDVIE+aqgIZ/wUoT0D035F16l918iPr3zP8PTTy98gD6Bjjdie+ivMfFv4vKLr7s9EDIwaQfgiCYN8z4d24rI/jn4aPVf3gEX8BPAwsaQ8wfczH6d3jHMiTEHjN82Tvy+6VpevuBfTDT6/6+UirYXiNTIEnXrUBjE6zT2AHcuqPyL1GA7YVNeE7sgBn/dX7zpWSsplfyALA8CPTHtMAkOydh3wgzAsOALUA7TH6cII9RmUe7Jq6BA62AEINu8PxF0c/ixqgYgfZObr85+M7GMT18yXgU2EIoO6zbK45gEhQ6CAMX3ZRv/4EavdDX9vn76TsFW5/LRuAgtD7k2spr0i/J9Pr+V3mtxpEcPJLYM+LJ+XhK2/efq6nsvzyVoMM+COhenEnUOyA1gFMfJEu0PYAfRrz+P3po4O/7v5IqT8K7+fdp2vWD5b7vZTnz7V81Dpwffpvn/e/m/EHPvtR9T8iAYYDmvTzx9I/kXp6yQGIBhrXO2WsJ0D3/vppCXjxoeB1A6a+ARo5ru1rsSCLwcQXVwBe/QV49R9XA+AYpDrw+x+M+1D+3eXf1/Qy+WUIaKnvpr5s+dQUANSN/fql6rV/+Ec9yt977wdf/vs24wVJ8KtxgN/XFuJ3Yr8vAIjt424CvSV6LfwzNH9faBO8+Mq79tIfP+jwb28gsn7kj/7r/qPLfUAymPBPcRro/dEtfnkJ8V9D37nB+8bqnSL98j3Uv/uUvlrcLx8d7u3nd3++gcmgN/tlvr1z+7cPzcDkv5Ordzv6n4ZXl4PRrwiQ9LLrZW6R19HvFLxe59Gn3Xn0898Z2U+fi/iZTigMZ/CYYtE4IUIqThKWJckAI5EkCiOMRCMEYyiaCkIyJNkwQek4JH3wHiVogiJf2QOoQuV/aoHRlzuBfT989l/RwLePYUMGhFFgXBKiLBuzYYSEBM2wNJqQIUVHDMpEFIGQEY7FCIKTLE1EPoYydIyx4F+Q4JQfAbujl7xPcvKh4JfvRPC7b4dm6sP4lxdk5y/LEIxKUCYgEBaP8ThE6BBLgIIoYimUIXAmRjDER4L47cfUT/++3P+xhleKAV4CWMHzpee3z3i9MociwMgjMcjcx7WHIYTxPONh1coT5l2nU26iL5YziidYe304qhd5bN7fPbuwNbYKFVFNVdvKUnOvcrZjCefndAYCumSS4Nxr6bbg+ZyX7eR+IZqk2fLBrvS6pQBiUtGNX+EZoSOccq0HEd9lreJZab0gT5IZEKY24hSH6uQkiVzIiAOsSWctHR7C47HOhcGrg/c8GtxDlFRSKm4bWrh5u5FpgTlX3YJqVUdOB81Sn+6jLW9KwT7a68mXDsesVW9iu2eghNkyHFk8mrRZ+Eadb2A9nEjBNyh+DA+jvB8HmvFDes1kl1PTZ52T81jkF1wnEUukubkRgkVlCFnohHqGzdzBG36DC7cd51HX9+F8ZYkB6c4z+tTJotbNx7GJ+JS+9cRyhCXToGEGxaHtpF+X2yl+0AQBP87s7aDowUl6oPSzrxtcRaUgtLOL4R/IwQ1NoakkbZHQeNCe3rApAzfXqmSGHKEUZQhbqak0BOzxSxK4R+5qtrq1WoQiLpZk3PyTtInZVim6CZmREC1hEQlMbmlNZUPhWElPyBmINWSGeCALYR4XXfY3au8s/KyHQY0QFKesDLEeEYqo9Jsk7kslb2dHpIXT/kHz5/vM4TBXLrPq6S58V92xwsiBjY3Kxq7hXdlD3BGlmNgQ77WTZKOaEvRc+/uWqW7pJS0bWtkq7tGTh/vczynTUNzBv3NtASXOg0QPAVxit1YbEFv2hsCxjLMuCtkqPJ9PTluLas82jxsnVFIeiykBAQMf/k1qOMKdjFliM/uRHkTO9YT7oW0Thj2oGTMQCJMeJ0W2Iw49mD0EM4oqaB5k8ZJI3sQi4pDamFKCZ1j2FtQwrTBmcr2zUPTQWCg5X6GtPxWrlzE2JmcXcqxqiV91mInJdEgVU8g96150KHldjudFks2+XCwDvlxdiJNoZ2SguoeFZvUOcwxyPdXrS8NzPbq6w0yNlFdtXAobDJoTzklVF3vUw7K9R0JPHeLFSe4bkdbwYsHoSNwGiZYkWLAMlnJjazHaTX6atS46aBemeaUnqyJO69LrKow6sz8cknmxcTmSNNjaPITO4zmK9BPDXtOZOPMpljWLOBF8qbcJbTYo/Hpmb2Z0htx5NYjVareeSYbeqU+4iR0M0ScEARnWRIERPl+MNIa47tpl4XDZ0Dn21kvYHJXTdnT79O6j1VPITtJRuMjbw8CH+9T1kdLGPBHGTir4g0IKY+VLvSBG6sF7Pi5pexhBotEwUqNZFHv04WwmOE4JPfwMoDI39ojMdzVdUsmxVo2TKoyWkB64JoQfWJZMd4iI1nOWOKAmNigkJg2jWK2z2ya+jNd+CRCqjfjnaW+Pcpbe+U50Sgj0HYe/N7EJn8ubfFgFsUhOfr65Qh1mD1qDbFrFl5ujPRo6tNH9ejk26YDeTnw9ihfBrpgHO934ukT9TpsxRLkkQkCZlgovLpUTfiY+nXgjjjOZj/1+kMQ6kMi5YNKzZxKNTF31vkxS5S4k+qUk4tAVy2rAOR9qJeiBy869XIhGDM3en2y02LupGjnyvsvODHwhzpcVuOnZMApmCnJ+UDoMlldsz0MV1W2FUBvisXGtGnYWc2MNqBhBAZVT4ATRlgagjQos08fwbMB33eL2AqWvMKxINBzAdUgFBDEuJ0e3ndRAL5FIO55Al1HpnRDpmUcxo+n6xvDk8ezA/HF/so3h4uXbYiy+kPDIRJ/3t6nSEkgaVg3AhABZLGehT+95ya09fHJbwSng3DqfnkjpawK0RPXi4+FdU7hy9Waxaq/wkEV3KsaZQ7X2fBJkwn6ho5qkorpZ4inOeAvptsRyb42Ay0YH0CYSjwsGePVR3ksrQuBWXOMUcThBqkGQhvNgCUoJmaiQHmdLPaS+1/I0jWR1j7OQxPZoKAvTc/Paw36YjpD7dLhZtUgFybjOFPOs20NyGN+Ms5hz+WW44PTlSWJhqj3XvcWX9kZG6UHiubmFvImaT0xzPfoWnjzX5xGB9QfLEgsJ684AHyU6Y31vpTrlmouGraInkhs2h5fpLTvDC5RhCqfODKLqpQNWyZ3DYt1srFbxnoWe2SDIfPKwSd2rhyKO6BOEy5btW8d4Hv3ZIQfqMDxqrINvjhxbIV878q2uH3f22LbogfaGVJrjDL5C97rgq2djC72tmJF/iXia6/Gn0GJH7u5a28PTpzmmMngup+OYHaD1LqILDtB4RhYIN7Xjdkiede+xNVWcOJpWToLLGmlEnkpYEsSDcBSzZfQUpIJdihvkIiL0TJk4byibhaA5dUD4+J4Mzpj6fhCJWcJacpgfapXdO1U4RKaWmdEWXOuYtkwCObfamM1hmlE5fTH1i4ryM8mA+k0Ez7PtLEL0vZzasVDBG4YfuxA5OKdgqnVA3Vok1LKlY6lyX5FrA/U9USzH9kA3wTVYi33wsKL7ST4PtZR1uFKeh8YgZYxlGK9d4BQ+6Zy2LGc9F+besJdJ5y8ie32clIJ/ICm34sv9gUbZtghkGh51xFUPAbUebgYmnoyytPXzmctWJ15lU6mMUbc8v/WUGXegI6C68gl3Z/q5kGOByvuGzq83ecJVZpM2Nr8NIgOpfktYnNf4mh+Goib2eYE7G8k+S3qryEo2JYXolp7CVkwooidzd5NOwq8X1u7P2iHnI7+1GZ6L8yOR8pl6KhqzLN34Rne2alGHldWLnJMxIriGfNIfzw0+r3tNuTD+Kb/O57RV/SKVoDt/5s5bjOT1doWQiCuvMqG6jvJoimRlSxYHpE9X90KonTTYXeYDxNHO9RT1ALxYxuFWLjNkyzsXvtDu83E2Eo6w0/T4kGaeb2T0aR7tu332OvvC5JUInwofk9epEHv42M634sGn0J0ZCk407jmcjg/Uxmw6jdLZW2hhPrl1fuD8PauRpjv7JyB7fzeMS2S2VyOwnays5X3EIgd2gcsmvQm8e2ODLSaBD8eTh+CChDYEsxc55ZRU0xXy7wadFccJpbDF9saTI5Z0KzRxyTANYGbF5oqM6t5myqBC7rJX0+taW6N2RDIdPxLquhjIA4/mEyQJgY7cWNmVz845CJe0jG7l4WxF8FzdTTvRCQyVcwQjcJzmWe7BrRvekaEqQ/uMXuNpL7iRZVbhEzE4dckM/sS0eJcf8WcO1WAHaar3+T7OXHVoMtWETseDkKB5ULVIul0zJdOzqiRkVCNaxzesKbp1zKFjh4Jdor0+8xsGgbRc9EaJ9kfOIv3HgkqnonxcpMs5omZ2Yg+De0CP0J43zD6RuMOFNjlNxkvEu9PL0tEY7abbpT53t2c5WldPskPjjK0p5mSxY8+BtzKXYip0qDyU6emWX8PshO9DkUOtPZmf1CI3b5VaOPT91iGmiupsaUFgm7T6FIu0G+Ej8oFt6RgZdIG8h0ibXNnO9qvgLsgxfTdNwgFMM2ra5DJw+8E3PB31b8/Tlov8uAaFsRruFFsASXKEklu4PnnPIkl9va4z2WY410QeAXatFZB08Mg0etej1PE800Tc7zPsbORasEx77wnPEsQ/OzLJuBTp+AED2Ungo/pEhDwqVOamqwXXLls/MAq851VPLVwoV62evnVUknYPkXXO8Xls2Lm4+OGNV9h8QgClPbl3+k6mWXc44nt1c/HcSQP6Sa+FYd3lI/o4CqbCqyQlq+jNjZI2yaPyLoqO7jzJ+Kjrxzkf67AOBnNRi5DYLychw+6BdT8VLkaGCWRmW0n0UiOqHn2e9hNRI4gX1feGe7LxkcOzJwR75cYOfUND9i2YmQPHwWiNkSZ8RT3jCOivhageh+DopmcUG6MhLRH5NHSWTN9Dfbn09kWqynY0gtMG4ARiNe3IcNJxT5i9qFVwmOAEauAtyuhH4mw+5VVYNUdBGCZUy1MBabiMnGt725cJewmOttHTWKsx3P5AWumqGhbjDlsa33OiXwR79Us7oVBLJDZp4fJblSjaeq9x8vkIolUzKXTIpDu1jZyWmnVmypNVMWt+xzTfIh276HmCCABD5w8WfrDTTV+v3tHwEcpnlrDJOCVa1kYCicSGntd2MqORmAZYC91zmqBYJ/KA1XINYhgp+zi0IzKRcNRH5rMkPu3pnjkifE+QBr5jcWwZjRlDznkOhRNU3O404B+87oANWyNtJ7wt9xTBXzzTAhttX1ua7bwqVCrvlaWbIhTrPUGjSQKriE1RAKHr6F6wgqYFXSYhTkUaUS51M4pGOORBjV4uc+UFh8ZfrxA0PsgBZo0nAWlTPBkex6bevoB69FSKy5MWzkdUSP3iUXlckU1HVCFi+QEJl958mDUCPRvKi68Kr939mXQ0dhMZJH5eMdnVG2R0e1g9F5d43ed3hUfl20R5sHbleV3F8TBlQoLSb93Rac+i5OK9/piphOSRs0gyW3eF+WfimTewxSBQrF7LbtaK8yYFYwyKN+muKbaFNhtCGpS1LXuDBD7Cw45idGzbaCblHo8pHZkjcZ8V2rW05zN9CCfPm2ySceMw5+fYtRR59JBNcPdifds298L7YZaMD3G4YWC/rfLrcaAQNvHE+pG6TQmaLTmiLHINrVY4bWtNk6YeuOUG46tXuBVIQL5xzZp86mXSoRGfOnMij8TjccinahoE1jC24Hg5m2BFLUN6JbqgTWKbuO6G3ugd0QpSxbinGIOyj/3tfo88ssjK4JZLN/NmSTe2jQngOCsVjqyNLk9ovFZNnwZS4LZIVQlo66D5bF2e7Zl8HH0/OtzqUbFtqcVoALWmSGt45IjBnqQ10VqEkQmPdhGNCyOwjRrNtP+4nFszkNTshq6p7aJcxDPQqXqUF5Ily4jzHEhdtCjJr2eSVYwLuvW8kl7JE3W9DY2jX3CE7TiXf0Sln3uXaPX7C1R3ZLuWCeXfx0Pc23EyjGU/dTdERqEQo7ir9Wh8w47POTOiclCxTTAQoX8S0kG6nwPF0595h0KAZcT31Bni6cSdUpsKxOSwpQ456VsU1IdeKc3khDsUO2UwtrqNSaNWZqmP+pRHp6K+ciiKnMH2hQrlo9cVneDpgzdvtRqslSZM4lQ7TudlbExGxCO5zQEe4bzPErUpHK9G0xFKLtkL6cq9eiFJ9AGg9lDFDys+Loxq0ZkRCP6RvRRNTnKcz1PT4dY+lJ49YAZ/LLD7zPkiMPJxUasM2ZwlT3sYPqVueZ7r1VcvHC1kgeCZdkTFplNGsx+f/c5MxYfNHMTrFakv7WbcHkUokM5dVZkzMh3x9MAcR0Ij3FrmJNZOtFSR41SuNNz2fCECmwE4jJXBPR+zy9Wvh46bDoIXDqo0H83T6+/ZDbs5mZRcXSquJDTvbflJRmvQ3g/Iw3WxB+IXa7ZhYec36cWdtRC1Q8Z2BVm27aehFAZxkidsEck9xkOia7q9q5bjUlnHa7E5smTbNpHxi0RbrmZbBhm6Lotp5rDppjmBbTyE7Y3+MTO9zql+AHtVIR80c8XOCLSgJ4kVrcs2Bc+1U8TUHed0KVPOOwB0UqFIPmMz2pR1aMhSWGFR2nubuVKt0krd4k8NZnCmLt2FOZAgBr0ISE8cnrfGsyjBhMXF1UPxprCcmai5ANqqYPDGRSu1Up0Im8bKvecTZ/tMEn0HgyhX4drYdM6tjeeX9Xmkr9H1Ort3CPgqENOtTvf0fi0v0/l6KwaKn9mD67abFKoXnRgTXro1wcbdUY3xO8jmyjp1JVm83xJyak2tpyf75Cb3E6/h7dpKxaXiDGdvWVVoc8WhQihbDqFEeeR+R9T9yYm9fOAGKNsy6GReNPWmI2XdmU8xL7Bwz7i+ifCFn460UJ3OihrwXaYPF8Vkegd95Oi2HyxpTjhyK4YGg2P2GKcavNED6WvoxB/oq0w/u/rGbCG1r1uV45vkdqgLj88yH95CuWUopXtUB4da+msCI96E0QKiLAMcCy3FHreVho4qu10l15BPgR/l1fSQpAGKAwXBnPMZ1w41O1IVfPbCY888dV0N0v62ZFBwW4eKOqBQ4JJDdz8CWNwH82rp1nwpUvw2lk8XMClLQpBcU7NVO1Ao53ZQGR0opY/i86POzVTTHY8sCzsqG/3ChFTiycr+IHVnX+N1Gyki9HnNHDXzUGOjk9ZDuy2jbpGWXarOGBnv0vNqlmye7bWZoslpS5mPxkJlhrdP7el6gbr7qUKMdhAQK5T5O2T17vFB8+RFO5OXTEGiBwPNnoGN8mg0tOywXjVgqw0L2KNWlal15cstPHesKoV1T4pQjBt7gum2ufHsMc/nvPePCmPMSCSjtiGbDVQ9mTEGW/dCtoWBPqPE5aB2rXPeen9hLz6xD2+XjsUjBi6DZYijubZFA25vw6koTEugoA25VQuK3RQaOyKbxsuNDCkhc4giyek2/xANTsBg96wtNUAGj+66VKcjGlhrAztYnWbZYy6SuTr2nVyOF2NfkNShJJPr6y+OKGoeoAEgbqWmwfAItMgWoVPK3S1iP/nGeZkK7cZt2nMWVqapSQy9NLfb5ULcUR9vbjmJztgFO/YPGT9gl1PeTcTccpUJO5rNXgZz9EWHP8Wc9AzxPuPJu4NnsbsaRWYI6XE/L3TDe2N18S4VMrRXXPVKtuLIwhS11qcqSKSeChmcDGId+ZG5Ei6gEVhOV4DCmqse1HLfbZiFe8RlxbCwxQ1xZaBk5cUVQ+4HnOoWixmkjjsLvHC7NItEFGSCxyvbnmakVWZddVLcT6Vak41Io3VfUl3zVOcooQnalBj7vhvOjYbjroXxe3utRT7VW8DGTi0jzhPZCmsqeg+MEe+HmPBIxs+WB/nazMtt0Emac4k0tMJ7eUD17Rw+uq5uzdN4IAJDByxRn27TwjH3s9EPh5kSDA1sLjV7htuxOLQNK3lXa4sp1BhD9oC6HhxexkboLwsmTNn1gHN2LpHNVuKIKxlgP4jZqn/TDxvq7M0M5+ku9zgo7wJOsXka5a7eSZzNuhQ9Tp674wMs/DoOiUk+hKLwL0TSOOvUymxex4rInWosCIVlgzP3Jt/zB49Ryz7iH1CZpHeVT6l7p7j55UTZaumdeFVb/G2Ab5g4GnNYERBikmfJGPFmjTqioFZ/oCfKMvbUFT3Pj9i/D8r9nAz6M/MHeMhWu1GtzDsIwmVVcrs/j5LdgFzpBmlU2AJap0k6y4eZ7wW7uvXT2iRZ6gfHMNOtrUxG62QlxJmOacVxWlaDMCPaDAvXg5mCfBRHD5VcFd4Sn6+qq3uIG8Dck8ounj62Vy65r8N0tnAZAI+2GDgBNrLhFu792ewirDTkIVL19p5xzE2Yvfq+EHN5949TOY3NXjTV8ppCV82/XNgmzzh3kB5nAvEObZbdr91NK55C1Uq2YIKtYm1mR5p+Dp3+qLbnkD6MoWbMwwYySkaRU+afr9sDlRApFTqbUyMzcfq8DefxKKiBv/FEZospxIGNxTDeWVYXS41Z+Kt2bi61XhKrkzXB/Sg4EZWvHdVINwklb7E2RlXH2xA7RNiFOGPK3nAO9Q1duvYsCy5U8a4jRLx5z44tky1Djpu3h3aKoNupSxOJzxrnTlrP0DtjWIRht5MF+cmJSsPDwmdFj60LTbFJgGvZnYvoxMXY4k6C/lvzyNq4fTfGRVCCLl57ONcaKJpl1GPCb/pxvFJQh6B9SCSD48vBHlvhSNTTospmuAqUK2pG/kICu24OjuWBJrXPm+R5lH7hhCQQnXa+kv6VtnxsNV2t0vrkjFEunfROmQmRkpfPK6JgF9RqkBYnHpCyxTW87+1nhl4I44J7g+5C6iqSF2yPTTjIo5x6onqZyr03xPBGCPGdQu4j58mrHfvegS9HDtKJxE+CB1eIZAVxMdVRtt9lBcrh07zXbqsaOujzzPvlpbuSk1JsKPe8x47pdL0pAuyqMWvcBx5mXKpZtM43rvQQpDz4LB/CJbtWjWA4ThAvo4iUyArhI3uVwvNRsXq9DnpGPQn3GbLnxoZpu3oOSGUy632Eb5tewObMyrRJX2Otdp0+9Z6+Wh3QTkGJO84MPFr5PXIykUdCCNIJ1cKAZA7CZQbd2oyfteAPz/RsbJr/GPdwDQuQMiqc3IinqJvyBGDWnaeldu+YaHG18eP55EHBvQv85+UY4YLdn0qdNDsP4rUDXxWEfaSOclyeFsGNqSmARru9dpfCqHBZrOUp9gAVgZvngmZude0g1aD0hyoV5PPiKVdWPrgTye3ddkQOmtewxrYiwvFuYEkxGggG92K+9oHSUHTUxjQ2uBcrg26VmbfYluNLRXZ5ICt8NaGU4nS+OU2ee84rlLybcHSjg6A7NeueusVDcqUyWq/D55NXRmTlF6IsiHa9GJc0gGP9KPCdBgIvwl7XKc0pOk8yS1Ui2I3512UfY5ylXiyAbOGdqI/3WzSSV8nPUXbaHw+D5YZM8zg014huiQPA2MN4uW+zbK1bY28yO5z2R8x+1l4khvdaR6C8jYcUD/3ieBtqrV9xtcofbd907UjzdSPDy2UTRwe2LXvaM+MJsCwhDtGpKjsbxh21WHHsFFAsQkpHx9N63x1YAJo0U1cEUWRPLmy2U6FSsaKuOueMUXm+PYiuSPc1hD7O1iONkjU27rfOkstiVlYn7Zv+gJ6e8A1fFYGRA3JUcXqlCYALVmDZgceEd8X3rilM1tF4O+0DldszQnxk09OjD58CmS+RJ56DWzlNVLZHLxqmG6fn5M/uCAD+hjQEVNms7/uMKPNLRdAucauV+WDa1/O+v2pgmwhtTnEi2uWZRNmh3Fxb0hAflH5M8MLzpobs9tw/JnE5UIl1bs/9+XnJdGr0ZiqHXUW4HC8HQ8kY3NKXh2eoHsyZhskcJMZNOe7ty9v7kbu3nzEURakvb6/jQ5/nuP6rAzzplre/fM6iCAz/8vb/71zKxxmR5glsqMP4dajndcj/53ftP/9zg/7jy1sf5kD5x/GeoZzSz2Mn74d3fn+C5/V5/TjM2tQjgJrvJ9dGP30/QfS7cT9O/L2flZnGuH8dC/t+hvA14nWs8PUxTvNh7N8Necb98HHqCPmKfcXf/vZ/AIt0sFw9MgAA -->
