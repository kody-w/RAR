---
name: "rappstore-rapp-markdown-medic"
description: "Check a markdown file or docs folder for broken relative links and images, skipped heading levels, duplicate anchors; or generate a table of contents. Never makes network calls."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/markdown-medic", "rar_sha256": "68c349d82161b59278bb31dbbafad199f23d1cabba2487c9d0d79f0dfc68882f", "source_kind": "federated-rapplication", "source_commit": null, "tags": ["docs", "markdown", "lint", "links", "local-first", "singleton"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/markdown-medic`. The original RAPP
agent is preserved byte-for-byte in `markdown_medic_agent.py` and in the RCI capsule.

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
