---
name: "rappstore-rapp-pii-scout"
description: "Scan a folder for things that must not be published: secrets, credential files, captured sessions, email addresses, home paths, and any names you supply. Reports file and count, never the matched value. Use before pushing anything public."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/pii-scout", "rar_sha256": "fcdbbcc12a04f5f7aebc69d619895c2edf7872354ac03821c0665b7818683513", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "pii_scout_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/pii-scout:142266d387d2e31bded7277de1d74920886647cc47119e3b005fe7c85b368e81", "kind": "skill"}, "tags": ["security", "publishing", "gate", "local-first", "singleton"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/pii-scout`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `pii_scout_agent.py` is
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
