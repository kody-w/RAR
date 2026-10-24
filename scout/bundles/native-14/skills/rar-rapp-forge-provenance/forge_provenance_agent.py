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
