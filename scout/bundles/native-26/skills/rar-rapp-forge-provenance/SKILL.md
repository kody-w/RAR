---
name: "rar-rapp-forge-provenance"
description: "Stamp a forged artifact bundle with the fingerprint of the RAPP agent it came from, then prove later that it never drifted. Reports per file: current, STALE (source moved), HAND-EDITED (derived file was edited and the edit will be lost), MISSING, or UNSTAMPED (provenance unknown, which never renders as healthy). Fingerprints the agent's declarative surface, read with ast and never imported, so a comment change does not cry wolf but a description change does."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/forge_provenance_agent", "rar_sha256": "38ea315503f3d7085e5d27c93efbf45c96b2f1e07849a43614749df2b7cb4d69", "source_kind": "rar-agent", "source_commit": "e1c2dbed7de3fe2e7a6deaf6a8f82a0d20f860f2", "author": "Kody Wildfeuer", "tags": ["copilot-studio", "power-platform", "forge", "provenance", "drift", "deterministic", "verification", "m365"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `forge_provenance_agent.py` and embedded as the fenced Python below (sha256 38ea315503f3d708…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `forge_provenance_agent.py` first:

```bash
python3 forge_provenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 forge_provenance_agent.py   # or on stdin
python3 forge_provenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
