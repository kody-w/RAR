---
name: "rar-rapp-forge-provenance"
description: "Stamp a forged artifact bundle with the fingerprint of the RAPP agent it came from, then prove later that it never drifted. Reports per file: current, STALE (source moved), HAND-EDITED (derived file was edited and the edit will be lost), MISSING, or UNSTAMPED (provenance unknown, which never renders as healthy). Fingerprints the agent's declarative surface, read with ast and never imported, so a comment change does not cry wolf but a description change does."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/forge_provenance_agent", "rar_sha256": "38ea315503f3d7085e5d27c93efbf45c96b2f1e07849a43614749df2b7cb4d69", "source_kind": "rar-agent", "source_commit": "e1c2dbed7de3fe2e7a6deaf6a8f82a0d20f860f2", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "forge_provenance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/forge-provenance:a6a5363a88b7ce466218fb3b6dcee0c2cdee97ea397d32dbdb4a61c9f6d8075b", "kind": "skill"}, "author": "Kody Wildfeuer", "tags": ["copilot-studio", "power-platform", "forge", "provenance", "drift", "deterministic", "verification", "m365"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/forge_provenance_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `forge_provenance_agent.py` is
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/616abOjxrblXyHO+2DX1alCDBJQ9/l1IwQSSAhJgCTkctjM8zzLz//9JaBTdcr2vd3R0YqoOgIyd+7cw9prJ/r9Ra8rLy1ePr/sUquHrn5kOXZtFy+vL5ZdmoWfVX6agMdypccZpENOWri2BelF5Tu6WUFGnViRDbV+5UGVZ0OOn7h2kRV+UkGpM94608cjpLs2uONXkKnHYFSRxq/DwwTKirSxoUiv7ALc0Mcxid2AK6vwncq2PkFnO0uLqoQycNPxI/szZNZFAeS9QrJC71noxzKtC9OGYiDK+vAKbenD+iO75hV2Df1o2YUPbo8zoVYvIdvyq2ELiTWqN1wC/aMIMoAeaVkBASIvy/xh8wqlBaQewCLicRA16proCViqTsIkbZNXqPV803tqDHQCq5UQWMSz9ajy+g+fIO6bRcpxwdEUP5SQZZuRXugV0A4q6wKY034FInRrsqZeVqOOk2g/HmxgW69QmQI3mGkcDwY1PR1Ih6zULqEkBddFD7Vp5AC/gNnQOx++H/oJuNfugEMju3z5/PMvry9AfPTy+fcXoFEJbr1wg5uPX7dLDyqDSREQAZ5mPQiaBFwDj4CAiMEty3ag59WPpR05r9A//hG2Hz5/SaDnB0TLoMZPUFkVP4btJ9eufvzyMt398vIKfXkxPdsMv7x8+PApSlu7+PHDt8nPMPsJ+jpxugNGfxv0jIJ3g6Y73w3yndFQT4HAv8NVWn7K9Mr75JeWX/z4dmV3GXBAXQJVpuEf3u9n+BR2VRcJ5Hx5SVLgQxAI08DP0O/Tlz++vPzNJv71At/p+Waxn4BtyiH/vrz8af3nZqZt/unZO/2e00Eo2dYUg09TTVk56PJez+ETj44Ck56avf6d0pOUDx/+1ig/Os9lQa79HtnJj/HPPww5WP7wy4c/xmz8sfwwIgH0O3g0yfp1So5f/vjyJfmzSm8fIBf6DmfeTX93+4dffv6MLIGkGp2jy/+TvFhPfMcGKQc+v4v0gedYWfnju8hJQ5CeaVsCy4yR+n9hmcFBT1PbUWlDhzT5Nz6uUpDzf/GxlaYxMOFP0M/FgL4QwIJk0gNML36e/zJcg1h/B3pTOn0FLrCLX/42bibR/y5uwCgPmBRgSh1ZbwAJGT0Y8XEoBeDZpz/b9c3/ILnfhtlPAWteZujzegjBcpBl6tETl8rP/8ZDM6DJ+PhTkPrJj6PDfi9+Rn75A4J+/H2wwR8fwL2v1pn29eHfC/uSMGnWA4jt37ZYANQNbTsbrkAApWOmyJJ6Zthnpjh+UVafvouK524n6P/xLUY+vPwBQDUBUFePDh4w9T/+AxJ9s0jL1Kkg2UwBQhd1UvmxDbRJFM8vIWWIAODs3+Qdv99/iq3fIH9KWICveh1V0KbQ/WgomoE9RQ4osr/970LPMng09K/fatSUS799ghQPrJAWPvAWsPf7clxOkVzW8cdmEA+WBuYbizbDg1KdlXVk/xP67e9Ff8r6Qb8vCbCB7idgcmUPZUov/KgfiqAOIqWyP4JSA5hCkUaRoZshNPxXZ5+GTV8HBjCZwtQTyO5ss67eAmMEi6EilmkESmQ1GKgMh0INQBrsPi36sUACI34ehP3222+GXnpfkqk8YdBU+0oYDPiqMPTxY1bYTuS7XvUlsU0vhX74/Y8foP+G/t2sUfiwxhGUx9E+oE5HkCBLB0CF3HqoxSAfgb+H8j245Pc/JsMP2iWgfoMa7ju+PU4G0r75d9jB5I03V4A9DyoORGJc6Xu7DYQDFBHAWezOL6vy9UsyiAB5ahetD7LqacRp8mT6N99O6ww+KZ82BH4aEXgYO4bW4EwzLQDr4h3oq6XAdicKpkPeAACWnQ3xnpj9xNm+unCsRoDSlE7/CgEk/JIMkn8zgOjBOPGvINur3yCROUJVmkbgv8FA4/Jgdpr4g+OfwTndHuD0BxBjqzcRn6DDyIgywJ0yr9BLeyKe+hQRAAPe5lcDU0rsdiBPkT34SB9SZoy8fxnR0FAvEHwqft8I7xvWv+OsfyGqYxpvWWhDHyFly8sQB5wsT2EASguguJAeDQSvn6SWEEAgPwImk6va8lMIhkRsuQB/uBQsN4T3k2aD/Y9u+pa7IEgGt4/Eb+CvdhR9Hr4M4r8r8SOX/A3Aym8Q4JrexLKTJ58cka4CIQRIJbBu9sQUTx/YJFT6FlDcccDd8htdjv2yHAb5A4MFrD32ExCHvvkJuj7p+1c2aqVPa35J2uEZcLD91hWMFgD2LHSwrj9RMRBWUdo/NziJeXrDHxQo21F7G8prYM5BhyH4viSxXlUj7QZmsMOpl/gM+CeYNC474IZfTZtNJhx5UjEgBcDJOOjPrAjYRO/L//WPf0AbGySwXr3rekrITYcAGRqKMRvNFOB4Ug8rgKCL0jSEpsbKr0Z+/9Ym+M/8L8cmCKRbXdgTUA62BwBhjhEKZf60t7FfAek4pOpUBvR+dDe43QLhlT1FMz30G6D+gNzrByU27IE900P7MxgOBMVosU8QPbjWm24OOgNsGedzoMhB6zPPKUNHpbDyK8TSzBY60CK7BtNct7DdIX5BuFv+YIDID21QSGOABgBDnv0YqMF6MfRGE6vRDZAxY2wNadJPHRgg5kPElhDonp4+HdF7qKVPMW8UVK8AJE6DJ8+8jtg11vnhyzRpagHfPn8htxO9AL5zpg5zCApgvSmtJwnv28Whi4jtIU6fbeJUfL+1kP/81jRaA54/Qyexu2oSOsl8dpDvtPrKMAFNHDPKn/o7fwzQIV2G7HxO/9Z0Dh+Qi+9aT7CiDqL2mRlv+DTUQiiNhiAYkHVsXcHWrY8xCIwBg8AiQ63+KyE6SArwJFjAAA4bvJSAjmkEk9gGDvo+454YD5jg5LuhIx1LWPJ3okEkjKOGSPgmI67L6ruO+V3DPNGCrQbxCvCLvGVlaIDU41kSWEbhpcPrqO9wD6Ar+wnagoAe884bkjGNvnf/AOgT9XQi3f2STIH41vyBAISqPkvBnrsBGr721SDkwRXozuMpDQElAK4eG+tqrEOg101BTRmy3XcBtwJuAzj6LcsBmRzrEvAJcN4o6RMkp+/D830HYwLnAgBLk6gfh6xZZk+DBOYvLMif6WzgzeFjLKUWIGYfI7CdCKQiiGw9GnLaAkkFOKetx99OaMC/GsRL/yzawyrDkcoAH8BIXxIrNcGUwYTjacOT8A+YOQDcP9/ODb47TAA+H+tvPBSAseRCle5OkTCaeBQyyP6qj19O9VGiZQUkxlAt7GSU+u54Zig8z2r6+jxO6kbQTEGylaZeTMc2b13F6zOKqhQUARvcmGrt08ADyr0H4SFHAOh95eT/HNjMkCFjMo9kwf0K9aM6Q768Veyh8Zk2CFgRwF1rsNI31hXUIy2KQM0YPDs9ravnnqX9R3pzkMDOGQhQxqN6PkoyCF6+mnjGVKimg57yjfk8o/Qr2R2PfgbwT4uwHOv6xK6mBmsM98loX2tqMaLA1w5nbEHHeAZFfCRzo6gMBNeoymCwLwlIgSdbeh1RaUyKzK58oMP7GHwymq/FfjhcGAoZoI/ASE//+NW7Q4cBVX1QWAcvA3MDDBkp7wAOn95KwNsZ0lRBfvp68PH6dnzy038Cg/zX69PJP/3nW5r/14d/IeB5qvT/LuDZlv9JwIcR4CJAfSb+8Jde9xmww6mZb9pJab98Tuooen1JQNqAdvDPDHQ4TntLqXI4iwOPgC6Vb49XkzrDt+8PZiee+t+TKcHfUVsgC+CaPT4eUnvoRifl/yrgawhZ38LhW9D9naTJcn+VNByCQNV3IPeu2QQm/qswIG0gJ2A16+Xzz2+b/KrsL18npMbQ8A6rZ4DfTYeOv78AY+mWXunD96k9mnj835j3K8EH0r+2Gr8OgvRh+NhYjqfeY5/96xt8vnvkDv3Rr1N79PIZoIj9+hIPXNPXI/8xnqS+TKsDtb916EAC6Ig/lkOLBCOf5kDS0K4PKocAKN4tMNz2rXH88OXzu7b+47eNfNaX+gJbYjpJGoRp48slipCOgRlLy7TtuYmalm1ThK1jFGFhqGVYBq4vEZNylhY5JxYGWKkE0RLrz5VgZDAr0PGr7f7decLLNLT0dHSxBGMxEqyELBZzzMEsYk4u7IWFEiaF2Y7h4AuTWhqog9hzgsQpHceWCE7glOWgQHcDt5bUIO/Z4U4L/Pp2mvBm4+fR3lCa/UE7GzHBrmyLsGzMsVGb0JeWrTtLnXRIVJ9b6Nwhl3MHffk69WnnwQ3THoa4AzAOWstmWOf3p9+GKFriYOQWL3l6+jDwEtGxK2HIgj5bIEe19Enfjs+oQGBKuysCYpdVksOhvFdfRRzlOmp90sLI91GhuwqnSysfXCxmr6hQLzDXKQQqaRIml8/OHHdJVVvyC/aSobkUwM7MxLOZgcMX8yIGzYE5mmHZ+/d+KyLhJTUW5+aBIjB5rdP+WmsuG+AFh/f5XqXCy+LSxW5t89lKvjvCjvP5KryWKU7te2LdHrsmIQMiWJiBqUSIaR9TZG0+9Osp5O47Vr9ygbQ7hHrC1WauXISLf9kR/pmPmk53Ggd2KbiI1Ovuofk7Nw3RcL4zVGxvnWXseG8MV2nUm8VFoupfPIa56V0UN0ZKz5NbxV49RM81ec9JfZHg6lLZH/HQbxuR2S8PoiBW5ummoe1SrrPFhRczbC/f41QR22Cv8JG1EgKUErMEFKFgp+zuOo+s1Xzub9TMR6+yYGSikG/x+3l5qeibrS7BusvkfKWOD2VzkXMm2eP7wzqYX9nDXVQfS44GnDjXSCo+C7TARtm9wJKb2nSLlYzJeOAxSxkN2LoKaBZvuH7H2WltS+tkteVwGZ7l4WFjhzvHqxU6WAtxlK+CWMcLldpesXmzmJn+0exDhNYIjjBOYqvOTie2kEASaMmO3yIcszjvMjatzvtTvlhmvCYVIaM6bC3G5iEVIn4bC+XcEmo/bzcSahyEhRjOE9YjU8V8MF1X1gJwQ5o05u3c1ah4Xja8Uasbpy/3M609nOX12hIlzJ1tXKqZYTbDWCcN1jZXLg3hOBHqbSVxTHb3KNvBFpfoYd4izPYt1rqn6FKraBjumQ2sztbMvNcfp3TBYzPOJE0hUZADF+1xeXnbW4wY72ZtvcOw9JxmF67YOmd+xq8Tfjg3wqVdlAph0ys9pkqFdCW2sd0K5IU3W8dYx3f5cVTjnVhsAzOatRmMrxNtWdqr/LhAFdmMzU27Q2jfu678dUguxNl+R69hzOvsxMXTQhXWq8XODKv7vT8ll+RSpmtPqwgyIA1Pw/bZals/sGwv7JfXcy/z8E1DNhfyiD2y5VW938X0VnrN7GRK3YrG71IrI4Krrnwdvc+20kFKNtRSSnerouSDqz9jYo7WLrTP0WLOyWJSZ5dDHvXixsMpMbrxXLtyyxD1DoRDHgtpxq0pXxLPO0PIRKot76dWDmpUiLiNjfUqEuH9IaKV+8kJ20Yj/c3D8Tm/tuirWK63FRfrdL00Ioc+JrPZbe3gcSF1XkBt2JZ1ZQ2scoMfId4Q9XKb3Bc5fBLRdch3JxPftw6INEHKrqjCIrsGkXOutYR04SXbcr6RHFX2Mem062CEYdj1rEEe8v6w3VaPUx75hi2417u1xOTdlZVdbh2qtXpydU+6ZzFTnBhZUZjmom8i98JpAX3ltPxseri8uRN73scVk/U0TtmFYpybHocfHwGGsstKdVbZwuY0+tqr9xhDtt0uuyY7dSnzteJ2CLcLz2XgJCfB5OCrySgt1qZS6W9LT7hn3mVtyinP56K9R06nh7y1wuPdVynVd+XVGk3x+TX058hBYJTFdZWFqsm5fOozIs6tVe2hYdR17zZdcpiHcbK3rRs193rG3TL0g6tiltVNJe5mxKqBhW2Wzze9tWQ9tet7OMzVuQgm7hbyPGqyZq47l50o3Zk9r7IqjRpXhd3AWsBJMo0be45Z0X7uCh3mwkxqJvROXB+Svi1Nia+Ek5Yz5gKj2/1M5kizP6u8ay9yLF/sjzaMddWRmtk8oiR4A1ryYOEArxy1HXHLrpvD3VU7yXZD8YFjB63Dcfl0O1+NImfI64KH98op0XNKCkgdDgwiP3NR27L2XdSkU37brsNC6HstPgnSpd0dcGFn1usHKV2ivhfxLA94wYpcD1ON2BHkO7oQ5yEocTJr1GJ+65241th9W6IhJfrofL2n6Yamrmda9GjDMZHIxQohMEvp/kCLriaFHLfbCjkytT5DllSh7RaYs2qtsIQdkqoRxT0S9YNu9ZaTFE7kNykV0vudpS2OFowdryRZxCvquLoneJbcSOWGVlpLZzf8vHDCzJgdDWTGYaBZJB/dSqCOGrw8XjGPiuLD/U7TRR3h9/WpF2nUbAK3FgSkv9Rkrt9UfJG2XbGS1pYxy1kk0OG+JUqXnWvnyEXiK6iAZLhsYf60Dw74TggLIxU5scUXHPFYBfyZ75Vyf3NlqbtwAB9IIg3q63HtnOLMtFbVwkYkBmnT1mrI2+WgMs0cEZUeF0wVX6393jD3sbopZIO0hGZXleFp6+3KM8YuIlSMwlMd881mht6ZzQZpQBYe2c0GwEyEG8T+cEDSbbbI6ENOr6xDT4cZAIv7gcgzt26Ji2ywXW5X3cUwVthqrs9SDmFbyVmwLrxD1+5+HurK7LLjMtWgbRLBKoJgEUlPNmmtnGnKyZenpQp7AXPhuAfiRTPhFgQNw5lJfInX1IJwdqtzvgEjy4jAG9Vp8DWmOTbTJTSb6DvTawn7Dp/Lxb4vUVxhZOcUzj0+TeRlMD/fWqbclk3pm0Sn8uZWUOO7cl8Xs1sbCx4ZJGpX8pt9ijSSyJhujaimP98k/XWLURe9Lmd5V2p3PahE/qQ/qM5dzuxLpxtbH5ZO8y5jH+n+kh/gNLQowM7CCE9EGdty+/bOpac0SM/3i49V97U7J3i2NOGm3oSRBgpEdGpkyywRN0eWMivZuwxzXfOKVgl6IfZ4sTH9htUo9x5axVnM5h59EpgHfzEyN4mv6rm/sDfyYIOiHPo6e1gt0h4m3RvHHVJJK4o1sy6a4HZlSHy/E/QVus8DGFT4yDxRRHto9shjyc/rxU0QV2clPZLkstzYrc9dz4xSnJvUkwMtfjjorS5beNcHLny7XpVdsM8fD9Swbwach50CuD5hcy4hGyeVY/kosTR6zz1WXbZ0Y/+Wt9gOkHKA9/J+P6NOzi2aS+fEbr0zWQtUFnYHcXNkd7u9RRrwrUNO8+S67qkNjnDCXIMz7EGfjTUXSnXY2Wm7vGemL86Ptb6YlyF1ak9pGuYlCqenB5rPEDgUYv5GJBSb0OsYs7XKxuJ+qUu4XzjkWsrJlA5YboGc7966gMNF+LD2axqjmABNQCHsJGKxl0pXd+ckvJbxeuU5c/umIE4VwNIqc9YMQSQP2J7LR8K0HrCzZZGNgB/PzdIm7bQ7UDZm9ZJurXEtCJaACGPnR//wZw1GkCpMzc3VwrIkeDZfOR5+PFaUsz7NhWZV2MES3TgL57oIVqW3XaNH9rRCVS7aXu/mNj7xTnrNu2qrzkkrzpF1nKKP4sKeaxfQbp1NPa8MTZTBYzu0zyFT7vZ4Pg/Pszzdu9SDBoU4PsKlT5FCM6u3zTINl/MHdYd3C5Fbrqqt454WCMduOuJBXVGiM4+tZWAdX8EWn3Kby+FB5gbHYcJjFUerE19VwaxvT7NWWW9SzvNwE5UySl9WqIyQzC2l9tfy5m/xDpfIchHURR+Uhhasl8QO0enb3Q2vuRoRJKL3W6Yq9WO/9o95LAi6RtyN1O/jMyFs9VWan7orJ6MXJsYocXvNF3cuxkCA2HK0KcXqSIrGYd4ZmHYkz2rkSdJufbRWXBnLfYaxkpXpTa4AosTcTrsc8JqktB+8cRXlQkG9o4ft+UxYqkV93Ps6L6mFSdTRmo+zoGsetAAU2pyi7frEdddEax9En13orYkm+eWCnvJDtJF0mw0YzgruW3ctGbeAVWS8X/JCihp3JdNbQjWy+rq4hYmsb4T7+WShKJX1aL+4bGYgrbmzv9wyWsfcGPr+IB+V4W13xExnqZkS0XbBrRpeg0M1u/Uuu6KuZkAurpjRr7CiYAW0KewNnDkCAjK2oBXZFlbOjUU0U6dEWnePMYHknXaPzFxyzjEFwyp7VW+yyLcn3MvPIotfupl/F+/u3lLwzr9siCzw/XsRq4In2+UctHvVzHqs6C69ccVBPd4MEuh2sA5usu5E6hxudUbzbwveeGgMHrU6iZ94VrUZja+2PK6Xqcfc96tle13VbWB7Cc2cV3dOr62Waq5H6dB1+LGOMYeeu1fS4HkvnvOCjjP6eadcFu6RW6yUdl5yByvvXM1s2E21ntVXOIzjqzF314vLQvYiUqA1BI3lo7bhj2FS63Oto0jJbK5sLrd3mN43UbAXHjwKriMEuZvBMRIMXYuqmEC7vBWCOAMZSeyVRFydyB0RYwz7oPtbTcCZadi77ayqCKR2xazz/aOzO4Km7V6b3D5WJNTu9najwI6IsYXbBCjDWyxF+XdU35YSVTouvlISQPnxh1Wvbb7ClTjGtfa4WvoiKzOPrNsahV6oxjk5Kfcy8g/avo2KlOxblfPhSL4rt8VKi+bFyiAPupeYDABECQnPsp8z/RXQ+ccRq7tYZpepQ3bl4cp59EMqe4x39NKKsFO6eSSb9SaLDJa6XRirV3B8r9ywa0PmGRXCu9zKG3K3yFtdFo8zswMRsqhqvqP3RuM39fFGnOb+PZ4d2q0zr2/YWRVtXj85VwqVm2odSM62uwj7I9vIuMs1JX8OxCSIWqyfIZQ323LsZQbwvtg1/YxfNLWAi1ynP+5OngvaZc4FZsEjIZIGBqAxNLJtGGIX3GcLBfHhzY5JFCvLAa7a3AatFobSJDrMNnfidFSp0DS3xHZVtEIVrgKubusz4/u0FM0daYGUCiqmW2eGn7K9ckSXPqz0D0vrFJWg1r5YnoMuoGC7oRJntqw3MwouDi2sYw2MNwks3uFl7ayk9njGVaLC+qNYXsI6yjRRL5WFdOKOrFecqiCHU/i0ppKjznmRvM31SlTpuarPhXTeL3I0CLgDaNKl9f7SaZcokNF5hHFntF0Sp8eVKsPKP6YWieRNEWMibFVGgj84Xtyze6x1H/fN9rEm23tLaWTehm1QCvWsg0sRDleH9uTx66JXDs32NM8wLg8wm4yOm0U94/ANHgSddN7YYg8gry5OHmg31Z2wWJtYVndn615b+QzONdc0OduZrYjzLnQKOdRrYmnmulPVxrrJWBRVpdqK9jsibXXKEJllJISUrFhXL2NQb6Vq/d7R0aXB1IpR2Lg1w0zGFD3VItWsOMvLi63qB4m9Jspiu9YfsbNAMyzL12R3OVTizkVKijyj0gLLLgrxqEEwIA572FhnRWYpOLDRq5wAXmOcMC0QAU3zDqRKXs1z2WyllcAp2BkfCJ7pkNbpCBAlfpRwc1mza1/FnaV38FFM3T0AUxAP+f0RglovnuLV4dBcOVvShMawGwzt78kGzZBaw+5Cl/girczom4DX55O04IP+6GBbGEMpgrpc+oZo0MwNDWaLiaog1kjjwKQzW9SihnLMceZoNTmbI1i2kCs1keuai47xTIUjdX90TGlWWDVyipscK1RSmlc3ulFEET3Iu/p+SJU5vb3IuZY8BEt9nOcXCzcJRT9qdmXZHuUKIuHANWwSgD8BYDpU1dyG555h6Zq9JAyDQIp6m9ziiqit2ZkwalzPtqBVPt63/lIUo0i9F3vQtFKYHtQzS2MeGjrD4Ll+l3rzcehnfkFqcJrBoKEF/ZL3QIigOaIXLyPyfL+0jQ3MBBKxPpMlrNHOpdsxrfnA7PpgHkmc0aTjLqujeDc7agXYYXdB0uVeondoYEi1dgSBcNBmD9j0gpuIRj0gFYQu+vouqqsQRTotAUZH2IcQK4QWlJxvbA/3Ejn0novsQouHkzkd7y+x7cexdET4vrXjanM9lmxNoeWyMDFP53aSr1QeHsdhji1XScr5XJQRu41vP5o7oq73kZiqjcrfNc1Ybcx2m3WUYcAobm7tfaQZksEquE3Ne7TQFtiBLTZeJT6upHcNKCZF0Hl7cwQu4YztyUT1vpZxgfZD4ZLzGbwr9hLpkDdxcbisS0kN54fNqj/vj/2iiOJZk3g91qJKJeLstehnCxGT5yenXvU4c1kdjO0Kww6XIsYtaumlq4ty3uebYz4TTubNEGPakKwcd6JLxmg9LXg2N+Pki1u5lnSyKGxjCOvb9UHVtmic66zDlt7sjl5mp2h3vgv0PCaJRVfv3NBBqe1yZd54TJoR5m0BKM2KRX1kKzwwpYoDi1xs7lG2TjZxcWas+6PoDw1t3O5+sBIdDl6zxAWO45kxP9Or7iQ3CgPvjKtbF+msOVYzk1nCj1O2SQl3u5ndbilgXIJCMo6Tcg+15XNgwFV9LM5YlRmGfeExsiSlsm2IsKM6w1uXMGxuS5HJYgWhmeud8TMsVf2t41f6BaVqi1shF895HFQZyx7qgTd2fUjy5RX14zTDuplKFliwTLeY0y7upJ57e5emhzc/w6/TXj4jCIURry/Da9h/8b7s/Qsd9+Fnvz5n4ov58vXl/9/7ieldwde3dJ9/fhleCH8eV//8r5X65fWlMH2gwPTKp4xq9/kKYni58vHPb3WGIf30C7k0qeyuentbWOnu+GbJnH4q9rEcfyo2vCwcfiP/8evbsNfJQC/fKfv6Mr5NH99rvfupFriefo84/dwIXMbYcjGoPPwMYXpnBdQGiv/xP3NGldgiMgAA -->
