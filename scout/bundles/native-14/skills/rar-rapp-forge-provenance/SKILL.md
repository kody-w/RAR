---
name: "rar-rapp-forge-provenance"
description: "Stamp a forged artifact bundle with the fingerprint of the RAPP agent it came from, then prove later that it never drifted. Reports per file: current, STALE (source moved), HAND-EDITED (derived file was edited and the edit will be lost), MISSING, or UNSTAMPED (provenance unknown, which never renders as healthy). Fingerprints the agent's declarative surface, read with ast and never imported, so a comment change does not cry wolf but a description change does."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/forge_provenance_agent", "rar_sha256": "9698949e8248472aa11df8dd58192826b3cbdab56ee3fd8c2ff5fa6819d9f14c", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "Kody Wildfeuer", "tags": ["copilot-studio", "power-platform", "forge", "provenance", "drift", "deterministic", "verification", "m365"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/forge_provenance_agent`. The original RAPP
agent is preserved byte-for-byte in `forge_provenance_agent.py` and in the RCI capsule.

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

forge_provenance_agent.py — stamp a forged bundle, then prove it never drifted.

THE GAP THIS FILLS. The estate already forges Copilot Studio / M365 / Foundry artifacts
from RAPP agents, and does it well: it reads the source with `ast` rather than importing it,
so inspection has no side effects and the emission is deterministic. What it does not do —
what none of the forge, transpile or deploy agents does — is answer the question that
matters a week later: **is what is sitting in this bundle still what the source agent
says?** Generated artifacts go stale while continuing to look authoritative, which is the
same failure as a specification pin that was correct the day it was written.

A header saying GENERATED is a request. A hash is a control.

FOUR DRIFT STATES, EACH NAMED. Aggregate verdicts like "mostly current" are unactionable,
so every file gets its own answer:

    current       matches its source, byte for byte
    STALE         the source agent changed after this was forged
    HAND-EDITED   someone edited the derived file; the edit dies at the next forge
    MISSING       the manifest expects it and it is not there
    UNSTAMPED     no provenance at all — forged by an older tool, or hand-made. This is
                  NOT "probably fine": it means the question cannot be answered, and an
                  unanswerable question must never render as healthy.

WHY IT HASHES THE PROJECTION, NOT THE FILE. Hashing the whole source agent.py would flag
every bundle on a typo fix in a comment. An alarm that cries wolf trains people to ignore
it, which is worse than no alarm. So the source fingerprint covers only the DECLARATIVE
surface — the module-level literals a downstream artifact actually depends on. Rewrite a
docstring and nothing is stale; change a description, a parameter or a tag, and everything
downstream is.

TOASTING. When a derived file has drifted, the fix is to discard and re-forge, never to
merge. The source is authoritative by construction; a hand-edit to a generated file is
already lost, and pretending otherwise just delays finding out.

TOOL-AGNOSTIC ON PURPOSE. It stamps whatever is in the bundle directory, so it works with
the forge agent, the transpiler, or anything else that emits a workspace. It is a
complement, not a competitor — the estate does not need a second forge, it needs the one it
has to be checkable.

    perform(action="stamp",  bundle=<dir>, source=<agent.py>)
    perform(action="check",  bundle=<dir>, source=<agent.py>)
    perform(action="toast",  bundle=<dir>)     list what a re-forge would discard

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "stamp | check | toast",
      "type": "string"
    },
    "bundle": {
      "description": "the forged workspace directory",
      "type": "string"
    },
    "source": {
      "description": "path to the source RAPP agent .py",
      "type": "string"
    }
  },
  "required": [
    "action",
    "bundle"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `forge_provenance_agent.py` and embedded as the fenced Python below (sha256 9698949e8248472a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `forge_provenance_agent.py` first:

```bash
python3 forge_provenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 forge_provenance_agent.py   # or on stdin
python3 forge_provenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/forge_provenance_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/forge_provenance_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/forge_provenance_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""forge_provenance_agent.py — stamp a forged bundle, then prove it never drifted.

THE GAP THIS FILLS. The estate already forges Copilot Studio / M365 / Foundry artifacts
from RAPP agents, and does it well: it reads the source with `ast` rather than importing it,
so inspection has no side effects and the emission is deterministic. What it does not do —
what none of the forge, transpile or deploy agents does — is answer the question that
matters a week later: **is what is sitting in this bundle still what the source agent
says?** Generated artifacts go stale while continuing to look authoritative, which is the
same failure as a specification pin that was correct the day it was written.

A header saying GENERATED is a request. A hash is a control.

FOUR DRIFT STATES, EACH NAMED. Aggregate verdicts like "mostly current" are unactionable,
so every file gets its own answer:

    current       matches its source, byte for byte
    STALE         the source agent changed after this was forged
    HAND-EDITED   someone edited the derived file; the edit dies at the next forge
    MISSING       the manifest expects it and it is not there
    UNSTAMPED     no provenance at all — forged by an older tool, or hand-made. This is
                  NOT "probably fine": it means the question cannot be answered, and an
                  unanswerable question must never render as healthy.

WHY IT HASHES THE PROJECTION, NOT THE FILE. Hashing the whole source agent.py would flag
every bundle on a typo fix in a comment. An alarm that cries wolf trains people to ignore
it, which is worse than no alarm. So the source fingerprint covers only the DECLARATIVE
surface — the module-level literals a downstream artifact actually depends on. Rewrite a
docstring and nothing is stale; change a description, a parameter or a tag, and everything
downstream is.

TOASTING. When a derived file has drifted, the fix is to discard and re-forge, never to
merge. The source is authoritative by construction; a hand-edit to a generated file is
already lost, and pretending otherwise just delays finding out.

TOOL-AGNOSTIC ON PURPOSE. It stamps whatever is in the bundle directory, so it works with
the forge agent, the transpiler, or anything else that emits a workspace. It is a
complement, not a competitor — the estate does not need a second forge, it needs the one it
has to be checkable.

    perform(action="stamp",  bundle=<dir>, source=<agent.py>)
    perform(action="check",  bundle=<dir>, source=<agent.py>)
    perform(action="toast",  bundle=<dir>)     list what a re-forge would discard
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/forge_provenance_agent",
    "version": "1.0.0",
    "display_name": "Forge Provenance",
    "description": (
        "Stamp a forged artifact bundle with the fingerprint of the RAPP agent it came "
        "from, then prove later that it never drifted. Reports per file: current, STALE "
        "(source moved), HAND-EDITED (derived file was edited and the edit will be lost), "
        "MISSING, or UNSTAMPED (provenance unknown, which never renders as healthy). "
        "Fingerprints the agent's declarative surface, read with ast and never imported, "
        "so a comment change does not cry wolf but a description change does."),
    "author": "Kody Wildfeuer",
    "tags": ["copilot-studio", "power-platform", "forge", "provenance", "drift",
             "deterministic", "verification", "m365"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import ast
import hashlib
import json
import os
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    try:
        from basic_agent import BasicAgent
    except ImportError:                       # standalone: verification must not need a host
        class BasicAgent:
            def __init__(self, name=None, metadata=None):
                self.name = name or getattr(self, "name", "agent")
                self.metadata = metadata or getattr(self, "metadata", {})

            def system_context(self):
                return None

            def to_tool(self):
                return {"type": "function", "function": {
                    "name": self.name,
                    "description": self.metadata.get("description", ""),
                    "parameters": self.metadata.get("parameters", {})}}


MANIFEST = ".mcs/forge-provenance.json"
SKIP = {".DS_Store"}

# The module-level names a downstream artifact can actually depend on. Assimilated from the
# projection tooling rather than re-derived, so the fingerprint means the same thing here as
# it does everywhere else in the estate.
DECLARATIVE = ("__manifest__", "EMBEDDED", "SIGNALS_DEFAULT", "DEFAULT_AUDIENCES",
               "DEFAULT_PORTS", "CENSUS_ASK", "DOGG_BASE", "CENSUS_PATH", "NEURONS",
               "PERSONAS", "ACTIONS")


def _canon(o):
    """Stable text for any literal, so the fingerprint does not move on dict ordering."""
    if isinstance(o, dict):
        return "{" + ",".join(f"{json.dumps(str(k))}:{_canon(o[k])}"
                              for k in sorted(o, key=str)) + "}"
    if isinstance(o, (list, tuple)):
        return "[" + ",".join(_canon(x) for x in o) + "]"
    return json.dumps(o, sort_keys=True, default=str)


def source_fingerprint(agent_path):
    """Read the declarative surface with ast — never import. Importing an agent to inspect
    it runs its imports, which for a fetching agent means network calls and cache writes as
    a side effect of *looking at it*."""
    src = Path(agent_path).read_text()
    tree = ast.parse(src)
    surface = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for t in node.targets:
            if isinstance(t, ast.Name) and t.id in DECLARATIVE:
                try:
                    surface[t.id] = ast.literal_eval(node.value)
                except ValueError:
                    surface[t.id] = "<computed: lives in code, not in the projection>"
    return hashlib.sha256(_canon(surface).encode()).hexdigest()


def _files(bundle):
    root = Path(bundle)
    for p in sorted(root.rglob("*")):
        if p.is_dir() or p.name in SKIP:
            continue
        rel = str(p.relative_to(root))
        if rel.startswith(".mcs/forge-provenance"):
            continue                          # the manifest never stamps itself
        yield rel, p


def stamp(bundle, source):
    """Record what is here and where it came from. Non-invasive: it adds one manifest and
    modifies none of the forged files, so it composes with any forge."""
    fp = source_fingerprint(source)
    entries = {rel: hashlib.sha256(p.read_bytes()).hexdigest()
               for rel, p in _files(bundle)}
    man = {"schema": "rapp/1-forge-provenance",
           "source_agent": str(Path(source).name),
           "source_fingerprint": fp,
           "files": dict(sorted(entries.items()))}
    out = Path(bundle) / MANIFEST
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(man, indent=2, sort_keys=True) + "\n")
    return man


def check(bundle, source=None):
    """Per-file verdicts. Never an aggregate 'mostly current'."""
    p = Path(bundle) / MANIFEST
    if not p.exists():
        return False, [("UNSTAMPED", "<bundle>", "no provenance manifest — this bundle's "
                        "origin cannot be established, which is not the same as it being "
                        "fine")]
    man = json.loads(p.read_text())
    rows, ok = [], True
    now = source_fingerprint(source) if source else None

    if now and now != man.get("source_fingerprint"):
        ok = False
        rows.append(("STALE", "<source>",
                     f"the agent changed after this was forged "
                     f"(stamped {man['source_fingerprint'][:12]}… now {now[:12]}…) — "
                     f"every file below is suspect regardless of its own hash"))

    on_disk = dict(_files(bundle))
    for rel, want in man.get("files", {}).items():
        if rel not in on_disk:
            rows.append(("MISSING", rel, "expected by the manifest, not on disk"))
            ok = False
            continue
        got = hashlib.sha256(on_disk[rel].read_bytes()).hexdigest()
        if got != want:
            rows.append(("HAND-EDITED", rel,
                         "content changed since forging; the edit will be lost on the "
                         "next forge — re-forge from source instead"))
            ok = False
        else:
            rows.append(("current", rel, ""))
    for rel in on_disk:
        if rel not in man.get("files", {}):
            rows.append(("UNSTAMPED", rel, "present but not in the manifest — added by "
                                           "hand, or forged by a different tool"))
            ok = False
    return ok, rows


def render(ok, rows):
    order = {"STALE": 0, "HAND-EDITED": 1, "MISSING": 2, "UNSTAMPED": 3, "current": 4}
    rows = sorted(rows, key=lambda r: (order.get(r[0], 9), r[1]))
    out = []
    for state, rel, why in rows:
        out.append(f"  {state:<12} {rel}" + (f"  — {why}" if why else ""))
    out.append("")
    out.append("✓ bundle matches its source" if ok else
               "✗ DRIFT — re-forge from source. A generated file is not a place to keep "
               "work: the source is authoritative, so a hand-edit there is already lost.")
    return "\n".join(out)


class ForgeProvenanceAgent(BasicAgent):
    def __init__(self):
        self.name = "forge_provenance"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "description": "stamp | check | toast"},
                    "bundle": {"type": "string",
                               "description": "the forged workspace directory"},
                    "source": {"type": "string",
                               "description": "path to the source RAPP agent .py"},
                },
                "required": ["action", "bundle"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kw):
        action = str(kw.get("action", "check")).lower()
        bundle = kw.get("bundle")
        source = kw.get("source")
        if not bundle or not os.path.isdir(os.path.expanduser(bundle)):
            return f"no such bundle: {bundle}"
        bundle = os.path.expanduser(bundle)
        if action == "stamp":
            if not source:
                return "stamp needs the source agent path"
            m = stamp(bundle, os.path.expanduser(source))
            return (f"stamped {len(m['files'])} file(s) from {m['source_agent']}\n"
                    f"  fingerprint {m['source_fingerprint'][:16]}…\n"
                    f"  manifest    {MANIFEST}")
        ok, rows = check(bundle, os.path.expanduser(source) if source else None)
        if action == "toast":
            doomed = [r for r in rows if r[0] in ("HAND-EDITED", "UNSTAMPED")]
            if not doomed:
                return "nothing would be lost by re-forging."
            return ("a re-forge would DISCARD these local changes:\n"
                    + "\n".join(f"  {r[1]}  ({r[0]})" for r in doomed)
                    + "\n\nCopy anything worth keeping into the SOURCE agent first.")
        return render(ok, rows)


if __name__ == "__main__":
    import sys
    a = ForgeProvenanceAgent()
    print(a.perform(action=sys.argv[1] if len(sys.argv) > 1 else "check",
                    bundle=sys.argv[2] if len(sys.argv) > 2 else ".",
                    source=sys.argv[3] if len(sys.argv) > 3 else None))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
