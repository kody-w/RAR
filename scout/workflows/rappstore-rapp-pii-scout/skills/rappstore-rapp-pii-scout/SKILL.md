---
name: "rappstore-rapp-pii-scout"
description: "Scan a folder for things that must not be published: secrets, credential files, captured sessions, email addresses, home paths, and any names you supply. Reports file and count, never the matched value. Use before pushing anything public."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/pii-scout", "rar_sha256": "fcdbbcc12a04f5f7aebc69d619895c2edf7872354ac03821c0665b7818683513", "source_kind": "federated-rapplication", "source_commit": null, "tags": ["security", "publishing", "gate", "local-first", "singleton"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/pii-scout`. The original RAPP
agent is preserved byte-for-byte in `pii_scout_agent.py` and in the RCI capsule.

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

PII Scout — find what must not ship, before it ships.

Point it at a folder. It reports secrets, forbidden artefact classes, and any
names you injected — with file and count, never the matched value.

Built for the moment before you publish something. That moment is where leaks
actually happen: not because anyone was careless, but because a tree accumulated
an archived copy, a captured session, a vendored fork of something already
fixed — and nobody re-read it, because nobody re-reads 40,000 files.

DESIGN RULES, all of them learned the hard way

  * Unconfigured is a REFUSAL, not a pass. A scanner with an empty roster
    reports "clean" precisely when it is checking nothing, and that reading is
    trusted because it looks like every other clean result.
  * Findings name the file and the count. Never the value. A leak report that
    quotes the secret is a second copy of the leak.
  * Whole artefact CLASSES are refused by shape, not just by content. A captured
    browser session carries identities, tenant GUIDs and key material that look
    nothing like a token; you cannot pattern-match what you did not know to look
    for, but you can refuse the file class that carries it.
  * Short ALL-CAPS terms match on word boundaries. An acronym that fires inside
    unrelated words produces noise, and noise is how a gate gets switched off.
  * Long base64 runs are skipped for IDENTITY matching only. Random base64
    contains short names by chance; reporting that as PII trains people to
    ignore real findings. Secrets are still matched everywhere, including blobs.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "max_findings": {
      "description": "Cap the findings returned. Default 100.",
      "type": "integer"
    },
    "path": {
      "description": "Folder to scan. Defaults to the current directory.",
      "type": "string"
    },
    "terms": {
      "description": "Comma-separated names that must not appear (customers, internal codenames, your own handle).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pii_scout_agent.py` and embedded as the fenced Python below (sha256 fcdbbcc12a04f5f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pii_scout_agent.py` first:

```bash
python3 pii_scout_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pii_scout_agent.py   # or on stdin
python3 pii_scout_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""PII Scout — find what must not ship, before it ships.

Point it at a folder. It reports secrets, forbidden artefact classes, and any
names you injected — with file and count, never the matched value.

Built for the moment before you publish something. That moment is where leaks
actually happen: not because anyone was careless, but because a tree accumulated
an archived copy, a captured session, a vendored fork of something already
fixed — and nobody re-read it, because nobody re-reads 40,000 files.

DESIGN RULES, all of them learned the hard way

  * Unconfigured is a REFUSAL, not a pass. A scanner with an empty roster
    reports "clean" precisely when it is checking nothing, and that reading is
    trusted because it looks like every other clean result.
  * Findings name the file and the count. Never the value. A leak report that
    quotes the secret is a second copy of the leak.
  * Whole artefact CLASSES are refused by shape, not just by content. A captured
    browser session carries identities, tenant GUIDs and key material that look
    nothing like a token; you cannot pattern-match what you did not know to look
    for, but you can refuse the file class that carries it.
  * Short ALL-CAPS terms match on word boundaries. An acronym that fires inside
    unrelated words produces noise, and noise is how a gate gets switched off.
  * Long base64 runs are skipped for IDENTITY matching only. Random base64
    contains short names by chance; reporting that as PII trains people to
    ignore real findings. Secrets are still matched everywhere, including blobs.
"""

import json
import os
import re
import sys

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # standalone — no brainstem required
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            if name:
                self.name = name
            if metadata:
                self.metadata = metadata

        def perform(self, **kwargs):
            return "Not implemented."

        def to_tool(self):
            return {"type": "function", "function": {
                "name": self.name,
                "description": self.metadata.get("description", ""),
                "parameters": self.metadata.get("parameters", {})}}


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/pii-scout",
    "tier": "core",
    "trust": "community",
    "version": "1.0.0",
    "tags": ["security", "publishing", "gate", "local-first", "singleton"],
    "example_call": {
        "args": {"path": ".", "terms": "acme,globex"},
        "note": "Scan the current folder for secrets, forbidden files and two names.",
    },
}

# High-precision only: provider-prefixed tokens, private keys, and explicit
# credential ASSIGNMENTS with a real-looking value. A bare `api_key` in prose is
# deliberately not a match — flagging documentation is how you teach people to
# stop reading the output.
SECRETS = re.compile(
    r"(ghp|ghu|ghs|gho)_[A-Za-z0-9]{30,}"
    r"|github_pat_[A-Za-z0-9_]{40,}"
    r"|AKIA[0-9A-Z]{16}"
    r"|-----BEGIN [A-Z ]*PRIVATE KEY-----"
    r"|xox[baprs]-[A-Za-z0-9-]{10,}"
    r"|sk-[A-Za-z0-9]{20,}"
    r"|AIza[0-9A-Za-z_-]{30,}"
    r"|(AZURE_OPENAI_API_KEY|client_secret|secret_key|access_token|api_key|password)"
    r"""[ \t]*[:=][ \t]*["']?[A-Za-z0-9/+_.-]{16,}""")

FORBIDDEN = re.compile(
    r"(^|/)("
    r"\.env(\.[\w-]+)?"
    r"|[\w.-]*\.copilot_token"
    r"|[\w.-]*\.pem|[\w.-]*\.p12|[\w.-]*\.pfx"
    r"|id_rsa|id_ed25519"
    r"|[\w.-]*_token"
    r"|secrets?\.(json|ya?ml|txt)"
    r"|snapshot-\d{10,}\.html"
    r"|[\w.-]*\.har"
    r")$", re.I)
ALLOWED = re.compile(r"\.(env|settings)\.(example|sample|template)|\.example\.json$", re.I)

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
HOMEPATH = re.compile(r"/(Users|home)/[A-Za-z0-9._-]+")
B64RUN = re.compile(r"[A-Za-z0-9+/=]{120,}")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build"}


class PiiScoutAgent(BasicAgent):
    def __init__(self):
        self.name = "PiiScout"
        self.metadata = {
            "name": self.name,
            "description": (
                "Scan a folder for things that must not be published: secrets, "
                "credential files, captured sessions, email addresses, home "
                "paths, and any names you supply. Reports file and count, never "
                "the matched value. Use before pushing anything public."),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string",
                             "description": "Folder to scan. Defaults to the current directory."},
                    "terms": {"type": "string",
                              "description": "Comma-separated names that must not appear "
                                             "(customers, internal codenames, your own handle)."},
                    "max_findings": {"type": "integer",
                                     "description": "Cap the findings returned. Default 100."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        path = kwargs.get("path") or "."
        if not os.path.isdir(path):
            return json.dumps({"status": "error",
                               "message": f"not a directory: {path}"}, indent=2)
        cap = int(kwargs.get("max_findings") or 100)
        raw = (kwargs.get("terms") or os.environ.get("PII_SCOUT_TERMS") or "").strip()
        terms = [t.strip() for t in raw.split(",") if t.strip()]

        rules = []
        for t in terms:
            anchored = t.isupper() and len(t) <= 4
            body = t if re.search(r"[\[\](){}|+*?\\]", t) else re.escape(t)
            rules.append((t, re.compile((r"\b" + body + r"\b") if anchored else body, re.I)))

        findings, scanned, skipped = [], 0, 0
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for fn in files:
                fp = os.path.join(root, fn)
                rel = os.path.relpath(fp, path)
                if FORBIDDEN.search(rel) and not ALLOWED.search(rel):
                    findings.append({"kind": "forbidden-file", "file": rel,
                                     "why": "this file class must never be published"})
                try:
                    with open(fp, "r", encoding="utf-8", errors="ignore") as fh:
                        text = fh.read()
                except Exception:
                    skipped += 1
                    continue
                scanned += 1
                n = len(SECRETS.findall(text))
                if n:
                    findings.append({"kind": "secret", "file": rel, "matches": n})
                # identity checks ignore base64 blobs (chance collisions)
                clean = B64RUN.sub("", text)
                e = len(set(EMAIL.findall(clean)))
                if e:
                    findings.append({"kind": "email", "file": rel, "distinct": e})
                h = len(set(HOMEPATH.findall(clean)))
                if h:
                    findings.append({"kind": "home-path", "file": rel, "distinct": h})
                for term, rx in rules:
                    c = len(rx.findall(clean))
                    if c:
                        findings.append({"kind": "name", "file": rel,
                                         "term": term, "matches": c})
                if len(findings) >= cap:
                    break

        clean_run = not findings
        out = {
            "status": "ok",
            "verdict": "CLEAN" if clean_run else "DO-NOT-PUBLISH",
            "safe_to_publish": clean_run,
            "scanned_files": scanned,
            "unreadable_skipped": skipped,
            "names_checked": len(terms),
            "findings": findings[:cap],
            "note": "Values are never reported — only file and count. A report "
                    "that quotes the secret is a second copy of it.",
        }
        if not terms:
            out["warning"] = (
                "No names supplied, so only secrets, file classes, emails and "
                "home paths were checked. Customer names and your own handle "
                "were NOT — pass `terms` to check those. A private tree is "
                "usually full of the owner's own name.")
        return json.dumps(out, indent=2)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--tool":
        print(json.dumps(PiiScoutAgent().to_tool(), indent=2))
    else:
        raw = a[0] if a else (sys.stdin.read().strip() or '{"path":"."}')
        print(PiiScoutAgent().perform(**json.loads(raw)))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
