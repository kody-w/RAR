---
name: "rappstore-rapp-markdown-medic"
description: "Check a markdown file or docs folder for broken relative links and images, skipped heading levels, duplicate anchors; or generate a table of contents. Never makes network calls."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/markdown-medic", "rar_sha256": "68c349d82161b59278bb31dbbafad199f23d1cabba2487c9d0d79f0dfc68882f", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "markdown_medic_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/markdown-medic:cd5ee46b6da3004408957a50ff197c0f5322958d457de6183b34db1312d9edfe", "kind": "skill"}, "tags": ["docs", "markdown", "lint", "links", "local-first", "singleton"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/markdown-medic`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `markdown_medic_agent.py` is
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

Markdown Medic — find what's broken in a docs tree before a reader does.

Four checks that catch the things people actually hit:

    links      relative links and image paths that point at nothing
    headings   skipped levels (h2 -> h4) and duplicate anchors
    toc        generate a table of contents with GitHub-style anchors
    stats      per-file size, heading depth, link and code-fence counts

No network by default: only relative links are resolved, because those are the
ones you broke. External URLs are counted but never fetched — a docs linter
that makes network calls is slow, flaky, and fails in CI for reasons that have
nothing to do with your docs.

WHY DUPLICATE ANCHORS MATTER

Two headings with the same text generate the same anchor, so every link to the
second one silently lands on the first. Nothing errors. The page just quietly
sends readers to the wrong section, and it survives every review because the
link "works".

WHY SKIPPED HEADING LEVELS MATTER

h2 -> h4 renders fine and reads fine. It breaks screen-reader navigation and
every tool that builds structure from headings, which is most of them.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Which check to run.",
      "enum": [
        "links",
        "headings",
        "toc",
        "stats"
      ],
      "type": "string"
    },
    "path": {
      "description": "A .md file or a folder of them.",
      "type": "string"
    }
  },
  "required": [
    "action",
    "path"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `markdown_medic_agent.py` and embedded as the fenced Python below (sha256 68c349d82161b592…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `markdown_medic_agent.py` first:

```bash
python3 markdown_medic_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 markdown_medic_agent.py   # or on stdin
python3 markdown_medic_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""Markdown Medic — find what's broken in a docs tree before a reader does.

Four checks that catch the things people actually hit:

    links      relative links and image paths that point at nothing
    headings   skipped levels (h2 -> h4) and duplicate anchors
    toc        generate a table of contents with GitHub-style anchors
    stats      per-file size, heading depth, link and code-fence counts

No network by default: only relative links are resolved, because those are the
ones you broke. External URLs are counted but never fetched — a docs linter
that makes network calls is slow, flaky, and fails in CI for reasons that have
nothing to do with your docs.

WHY DUPLICATE ANCHORS MATTER

Two headings with the same text generate the same anchor, so every link to the
second one silently lands on the first. Nothing errors. The page just quietly
sends readers to the wrong section, and it survives every review because the
link "works".

WHY SKIPPED HEADING LEVELS MATTER

h2 -> h4 renders fine and reads fine. It breaks screen-reader navigation and
every tool that builds structure from headings, which is most of them.
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
    "name": "@rapp/markdown-medic",
    "tier": "core",
    "trust": "community",
    "version": "1.0.0",
    "tags": ["docs", "markdown", "lint", "links", "local-first", "singleton"],
    "example_call": {
        "args": {"action": "links", "path": "./docs"},
        "note": "Find relative links and images that point at nothing.",
    },
}

LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
FENCE = re.compile(r"^```", re.M)
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "dist", "build", "site"}


def _md_files(path):
    if os.path.isfile(path):
        return [path]
    out = []
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        out += [os.path.join(root, f) for f in files
                if f.lower().endswith((".md", ".markdown"))]
    return sorted(out)


def _anchor(text):
    """GitHub's rule: lowercase, strip anything not alnum/space/hyphen, spaces
    to hyphens. Reimplemented rather than guessed because a wrong anchor makes
    the whole TOC subtly useless."""
    t = re.sub(r"`([^`]*)`", r"\1", text)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = t.strip().lower()
    t = re.sub(r"[^\w\s-]", "", t)
    return re.sub(r"\s+", "-", t)


def _strip_code(text):
    """Links inside fenced code are examples, not links. Counting them produces
    false 'broken link' reports and teaches people to ignore the tool."""
    return re.sub(r"```.*?```", "", text, flags=re.S)


class MarkdownMedicAgent(BasicAgent):
    def __init__(self):
        self.name = "MarkdownMedic"
        self.metadata = {
            "name": self.name,
            "description": (
                "Check a markdown file or docs folder for broken relative links "
                "and images, skipped heading levels, duplicate anchors; or "
                "generate a table of contents. Never makes network calls."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["links", "headings", "toc", "stats"],
                               "description": "Which check to run."},
                    "path": {"type": "string",
                             "description": "A .md file or a folder of them."},
                },
                "required": ["action", "path"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action, path = kwargs.get("action"), kwargs.get("path")
        if not path or not os.path.exists(path):
            return json.dumps({"status": "error",
                               "message": f"not found: {path}"}, indent=2)
        files = _md_files(path)
        if not files:
            return json.dumps({"status": "ok", "files": 0,
                               "note": "no .md files found"}, indent=2)
        base = path if os.path.isdir(path) else os.path.dirname(path) or "."

        try:
            if action == "links":
                broken, ext, ok = [], 0, 0
                for f in files:
                    body = _strip_code(open(f, encoding="utf-8", errors="ignore").read())
                    for bang, text, href in LINK.findall(body):
                        if href.startswith(("http://", "https://", "mailto:", "#")):
                            ext += 1
                            continue
                        target = os.path.normpath(
                            os.path.join(os.path.dirname(f), href.split("#")[0]))
                        if href.split("#")[0] and not os.path.exists(target):
                            broken.append({"file": os.path.relpath(f, base),
                                           "kind": "image" if bang else "link",
                                           "text": text[:40], "href": href})
                        else:
                            ok += 1
                return json.dumps({
                    "status": "ok", "files": len(files), "broken": len(broken),
                    "relative_ok": ok, "external_not_checked": ext,
                    "findings": broken[:100],
                    "note": "External URLs are counted, never fetched — a linter "
                            "that makes network calls fails in CI for reasons "
                            "unrelated to your docs.",
                }, indent=2)

            if action == "headings":
                issues = []
                for f in files:
                    body = _strip_code(open(f, encoding="utf-8", errors="ignore").read())
                    hs = HEADING.findall(body)
                    seen, prev = {}, 0
                    for hashes, text in hs:
                        lvl = len(hashes)
                        if prev and lvl > prev + 1:
                            issues.append({"file": os.path.relpath(f, base),
                                           "kind": "skipped-level",
                                           "detail": f"h{prev} -> h{lvl}",
                                           "heading": text[:50]})
                        a = _anchor(text)
                        if a in seen:
                            issues.append({"file": os.path.relpath(f, base),
                                           "kind": "duplicate-anchor",
                                           "detail": f"#{a}", "heading": text[:50]})
                        seen[a] = True
                        prev = lvl
                return json.dumps({
                    "status": "ok", "files": len(files), "issues": len(issues),
                    "findings": issues[:100],
                    "note": "Duplicate anchors silently send every link to the "
                            "second heading to the first one instead.",
                }, indent=2)

            if action == "toc":
                out = []
                for f in files:
                    body = _strip_code(open(f, encoding="utf-8", errors="ignore").read())
                    lines = []
                    for hashes, text in HEADING.findall(body):
                        lvl = len(hashes)
                        if lvl == 1:
                            continue
                        clean = re.sub(r"`([^`]*)`", r"\1", text)
                        lines.append("  " * (lvl - 2) + f"- [{clean}](#{_anchor(text)})")
                    if lines:
                        out.append({"file": os.path.relpath(f, base),
                                    "toc": "\n".join(lines)})
                return json.dumps({"status": "ok", "files": len(out),
                                   "tables_of_contents": out[:20]}, indent=2)

            if action == "stats":
                rows = []
                for f in files:
                    raw = open(f, encoding="utf-8", errors="ignore").read()
                    body = _strip_code(raw)
                    hs = HEADING.findall(body)
                    rows.append({
                        "file": os.path.relpath(f, base),
                        "bytes": len(raw.encode()), "lines": raw.count("\n") + 1,
                        "headings": len(hs),
                        "max_depth": max([len(h) for h, _ in hs], default=0),
                        "links": len(LINK.findall(body)),
                        "code_fences": len(FENCE.findall(raw)) // 2,
                    })
                rows.sort(key=lambda r: -r["bytes"])
                return json.dumps({"status": "ok", "files": len(rows),
                                   "total_bytes": sum(r["bytes"] for r in rows),
                                   "documents": rows[:60]}, indent=2)

            return json.dumps({"status": "error",
                               "message": f"unknown action {action!r}",
                               "valid": ["links", "headings", "toc", "stats"]}, indent=2)
        except Exception as e:
            return json.dumps({"status": "error",
                               "message": f"{type(e).__name__}: {e}"}, indent=2)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--tool":
        print(json.dumps(MarkdownMedicAgent().to_tool(), indent=2))
    else:
        raw = a[0] if a else (sys.stdin.read().strip() or "{}")
        print(MarkdownMedicAgent().perform(**json.loads(raw)))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
