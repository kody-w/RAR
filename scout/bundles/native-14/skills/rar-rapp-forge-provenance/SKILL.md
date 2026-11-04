---
name: "rar-rapp-forge-provenance"
description: "Stamp a forged artifact bundle with the fingerprint of the RAPP agent it came from, then prove later that it never drifted. Reports per file: current, STALE (source moved), HAND-EDITED (derived file was edited and the edit will be lost), MISSING, or UNSTAMPED (provenance unknown, which never renders as healthy). Fingerprints the agent's declarative surface, read with ast and never imported, so a comment change does not cry wolf but a description change does."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/forge_provenance_agent", "rar_sha256": "9698949e8248472aa11df8dd58192826b3cbdab56ee3fd8c2ff5fa6819d9f14c", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "Kody Wildfeuer", "tags": ["copilot-studio", "power-platform", "forge", "provenance", "drift", "deterministic", "verification", "m365"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/617a7ebSLLlX9E690PbzbF5CSTct+4MQoBASOIlISjX6uIN4v0SQnXrv98E6RzbVdU9s2aNapUtIDMyMmJHxI5E/u3F7tqoqF++vGwLb5gZceoFfufXL68vnt+4dVy2cZGDx1prZ+XMngVFHfrezK7bOLDdduZ0uZf6sz5uo1kb+bMgzkO/Lus4b2dFMN1SaVme2aEP7sTtzLUzMKoustfxYT4r6+Lqz1K79Wtww57G5P4VXHl1HLS+93mm+mVRt82sBDeDOPW/zNyuroG815mm0xI7+9AUXe36swyI8j6+zjb0fv2JXQs6u5598Pw6BrenmbPebma+F7fjFnJvUm+8BPqn6cwBehRNCwTsBE0T9vzrrKhnxz1YZCePoiZdczsHS3V5khd9/jrro9iNnhoDncBqzQwsEvl22kbDx88z7ptFmmnByRR/a2ae76Z2bbdAu1nT1cCc/isQYXsPa9pNO+n4EB1now1873XWFMANbpFlo0HdyAbSZ17hN7O8ANf1MOuLNAB+AbNn3/nw+6GfgXv9G3Bo6jcvX37+5fUFiE9fvvz2AjRqwK0XbnSz/L5delQZTEqBCPC0HABocnANPAIAkYFbnh/MnlcfGj8NXmd//3vSf/zyNZ89PwAtoxo/zZq2/pD0n0O//fD15XH368vr7OuLG/lu8vXl48fPadH79YeP3yY/YfbT7H3i4w4Y/W3QEwXfDXrc+WFQHEyGegoE/h2viuZzabfR57jx4vrD25V/K4EDugao8hj+8fv9jJ/ab7s6nwVfX/IC+BAA4THwy+y3x5ffv778xSb+9QI/6PlmsZ+AbZox/r6+/GH952Ye2/zDs+/0e04HUPK9BwafpnpE5ajL93qOn2xyFJj01Oz1r5R+SPn48S+N8iF4Lgti7bfUzz9kP/9tjMHmb798/H2Kxg/NxykTzH4Djx6y/vkIjl9+//o1/6NKbx8gd/ZDnvlu+ne3//bLz19QEkjqMAQj/0/yMjuPAx+EHPj8tqP3Asdq+u8/IKdIQHgWfQMsMyH1/8Iyo4OepvbTxp/ti/zf+LgtQMz/ycdeUWTAhD/Nfq7H7DsDuSB/6AGm1z8jv4zXAOvfJb1HOL0nLrCLX/4SNw/R/w43YFQETApySpd6bwly5gxgxKexFIBnn/9o1zf/g+B+G+Y/BawFjaHV9QjBZpTl2ukzLzVf/o2HIKDJ9PjzpYjzD5PDfqt/Rn/5fTb78Ntog98/gnvv1nns6+O/F/Y1Z4pyACl2eNtiDbJu4vvleAUAVEyRoh2OKsM+IyWI66b9/AMqnrt9pP4Pbxj5+PI7SKo5SHXd5OAxp/7Hf8x2sVsXTRG0M80tQIauu7yNMx9ok+tRDDz6iM56TPlN7IBk8RgHCs/FfyAFFNVf/3dtlyU8Gfaf32rSI3Z+/TzTozGxxcA5wLxj9f2aP8svqKE1sHw91kNnaCfnfBq/jFb79a8Ffi6HX6dCBIZM5ZwRQBEvmy71P4+KG2MVf6jp2vnMv/lu1745dwr4sao1RQrKXDtusknGYgsSLdhRUQ+TbGCIL6OwX3/91bGb6Gv+KDH47FG/GhgMeFdn9ukT2EaQxmHUfs19Nypmf/vt97/N/nv272ZNwsc1ZFDinmYGGoraYQ/oTNiN9RR4APhsLMGjmX/7/WlMICYHNRg4JQ5i/zE5jfPE994sq23oTxhBgggBRvSf1XrCUft5JgSzd33Bog8yY8+iMZQ8vxyRk7vDxH6+5u+WnBI7YAdNMLzOQFKZVv3Vqe1JxeyfIG7aX2c7Rp61RZGCP0Y1p0FgcpHHwPzvfn/cHzMT4B2rNxGfZ/uJW5SAhZRRbT/XGHnd6BcQTW/T25Fz5H7/NR+Jgj+ayh7R+DAPGAQs4z5d+mkiWiNBAY5t3taextgj79LHLOfXX/PmiWi7Hl3hAtSBRcMu9kbs/eMJqSaaEsdov4kg+m9e8J5emTD4L5E7G7M/On+Usm/09S1zf8dA/0Q7p6DcsDOelmf6RtBmnCBJ2mPHoFCAvczsdKRrw0NqMwP5JE6B17S28+JiBs92OEmAv7gCLDcC/UmaG6DwWPa+EWMQImMUTDRuZKN+mn4Zv4zifyjYEzP8FRjw1xmwZvTgzPkPeHsFli1GHJdP+0b2yA1nTewBxYMA3G2+kd8sbppxUDzyUeCWLM7jpo3dzzPjScbfuaVXPK35Ne/HZwBk/hvHnywA7FnbYN34QawAtNNieG7wIebpjXhUoOmfDq06YM5Rh0cAZHbbTiQamMFPHp3BF8AmwaRp2TGDxO1js/kjozyJFZACEss06I8cB9jEHpr/9fe/z/h3IL67YxYWI0DG9iB6YBdk5bwbVwDAT4simT3apLid2Pob6X9k61H02NLYcdoBJNuj5qPtAUjdKUhmZfzY29R9uEU9RsmkoWcPk7vB7R4Ib/18Qh09dg+gmoDwH0YleHbPqvTYzIyGA6CYLPZ5Ro+ujR43R53rIp3mc6BkzdaqwOljf6Sz2uuMpZnNbE/v2DWYFoa1H474BXD34tEAaZz4oCxmICOlw1t3BSrqGJpd/uAoNihHD2z5U6ROYQ5o9ojYZgZ6oadPpzw+VsanmDdCabeANT0GPzzzOpWgqWqPXx6THg3d2+dPVPVBFoDvgke/OIICWO8R1g8J3zd/Y0+Q+SNOn03fZPXvGsJ/fGsBvTGzP6GT+7f2IfQh89kPfqfVO18EpG+KqPjRrcUTQMdwGaPzOf1bCzl+QCx+10iCFW2A2mdkvOWnsSrOinQEwZjdp0YUbN37lAFgjDloIgt/RXD2Bx14EizgAIeNXspB/zMlk8wHDvox4p5lBvC6h+/G/nLchZ3/lWiAhGnUiIRvMrKuaX/of79rfx8EYWPOBB34Rduw2mxMqbJ6EFlGFw7710nf8R7Iruzn2QYAeoq7aAzGIv3R/WNCfxDJILXDr/kDiG+tHADgrB3KAuz5NqaG9y4ZQB5cgV47e4QhIAfA1VOb3E61EHSuBShrY7THYV6MbgN59FuUA2o41UbgE+C8SdLnmVZ8D8/v+5GplIGQyNNhGrJmGYkGASycWBA/j07/zeETlgoPkKlPKdhOCkIRINtOx5j2QFABBunb2bfzFvB/B/AyPInDuMp4QDKmD2Ckr7lXuGDKaMLp7OBJ38ecOSa4f7ydAvxwNAB8PnGAbCwAU9mftXb4QMJk4knIKPtdn7h51McDrekgMMZq4eeT1O8OW8bC86ymr8/DoduUNAsQbI1r149DmLce4fWJorYARcAHNx619mngMct9n4THGAFJ751h/2NkVGOETME8EZZvnGNSZ4yXt4o9tjGPDQJmAfKuN1qpGEO2j4GrL91EzVJQM0bPPp527XPPB+kTze8PYOfMDJBH+ajKBw2AV2gfPONRqB7HNu8E6InSd9o7HeSMyb+ok2aq61/z90r6gPvDaO81tZ6ywHu/MjWUE55BEZ8I5SSqBOCaVBkN9jUHIfAkbK9TVpqCovTbGOjwPQafjOa92I9HBWMhA7wMGOnpn7j97ghhzKoxKKyjl4G5QQ6ZuuIxOXx+KwFvJ0KPCvLT+zHG69thyE//CQzyX69PJ//0n29h/l8f/4WA5xnR/7uAZ5P9BwEfpwSXAurz4A9/6lyfgB3PwGLXB9z15UvepenrSw7CBjR3f2Sg4+HYW0g148kaeAR0aWN/unqoM3778Zj1wVP/+2FK8PekLZAF8po/PR5De+wtH8r/WcA7hLxvcPgGur+S9LDcnyWNRxqz9ock991JLjDxn4UBaSM5Aat5L19+ftvku7K/vE8onLGdHVcvAb97HCH+9gKMZXt2az/N9ex4wfDarj81YzsAo58RIA9cPxg+ePbveuHn0CayQW8GxlIktaTmlL/E5sv5ArNtFPWCpecRS5TClhjp4K7j2Q5B+j4eeEsXCwIisEnw1KMCdO6+vFnrn2NlicflRyODvX8CadH/9hjc8p56PxQZTfPeek8AeKj/24tDzsHIzbwR6MeHgaGTjZ8lZxANiED3yJxu1HVo7BeGqmloezisxNZFfOO0FVyUsGMzYWLNEIQiYhFbrFKXv/rm6YDuF7m/gg/6YuMd9kuaD0hV3OZe5B/NJFwvvOBMQksC133GhmAfzeHVDs/9tj662iXT7ltteUTQTHBFVAodLPYZxh0kr2TKk9CUfYUfLlhk4bwWry9pRfm1WZXaJrJM5QhD9r3Xrw5nVsdjtyvTek3DqM5aiKqqW5Gpdio3IKoYd7ZEZtsSvt+0aGfcVXTnYiknVUpmEGtcaGlYZDauWUguxbpzdC6ZiRUhkXR3N/pJXmQCsjyfUUi856xVVd41dmGYWWPhCSElAYvdHJZXR9KWqA6iwH9ism0OSSaUgM6h2smgUz9O71mRwAVi+PHhcFukcO/TyGp3M9pLGaxEhsxijFUqYre8S+LFSHlTXAtw4y0ZWT3BnLtX9GFTWxoNVYetSbVXZs9sz8Cmmy4/z1WnzrQtfzLjAvfvd+12EecKc1blRTxky8U+VlNqGXr3JaY1yyJxLSknhXbXb9xkhffQkOqRMa8pOcxYYmnmB3UxoL1va+n5pERp7kieHQwVxPEsvlaaIUXrSKYiRbpoiEGrxIIzIxmmd366TJErztn0legDz4A5zW3Ihl+Hm14pqSxe7muGmUu0saCywD8OGuok94A211S9P22rVL0fAHBSVQhEbptYlRzCuia02Va0Blt0zmSQwRxEXYzdBj0WlyPaJYxr4mlLUMqySQKNO272mwNjBXcmlHMc3ge9fIB6E18sIGPZq/pFprnz8sRofHxXt6yc9cehnK+5XtSvHkfE0naOs1FBrtVOxhXOXy5QSMIUcnnFr8dOuharw+By54HjsoMyXDiLLyMr3xaNLrAMbLDajQUd2Zy8XoN5Ay9uSjagLrNUK7lH+YiH9u5dxRVUUIPEZJWaF8qEVPdnJCatDj66W0R1V0dIgOcu2UmyEFI32fX2Kntc3m9qUt4OTF9YxpLnveHEqv2NzwWX15ANz1omvOm2JbErhYpYbAxqtXblcssBk974rAkDgJ0Eay+MajSqWR8x7qJRlq6cBdRadUuQlYeVf0silhE6JR7Kk5IsJEHcKduM6S12A2fHleSa7jbbqCBcOaLy3KZUBzHaFnsMkojl8hZVAXu+IWergMpeby9KFBvHsIcJPt4S2KJwtycYhgfCZyidMc+rRXnc31hN1QftWPMXSyBODFQI2VwaYisWXYGD091x2JP8QnXJXSkpuq7Iguv38MUSucsuLXBb7/0beVD2xJmzsn0cW80l9T1F3i6vTOo1JnrzldyMjnBkqQOgyGK3IgC764NrZwV+5lINtYcSNCWHRtnoQs7t74lqu1WvXXAUpbpok+8XKN6SIhyjGyrtIux+IYVhudgsLgmvazaRiwzc19klk23/tt6V13UasmW8kcXV2lAJRFge47WXXvuYj0N0EIVMTAGBZrlOC4wqSo3KIKIEScWdlHC2rpoX7USk3OVSmmYd1hgXLBhzsT7G5LyQqS4TsNt+e1qtI17s1uyc3EEbib4QiNRAcge51LGU6bmUJC2hqvrGyk5u40ZFO18qTkLatmBW970ftjlvOaJwgTHoivvEuc11d73w6bvHwAk6p2KR6UHEcZhGFzKDCHfIExIqcO4ZoYTbLkQM5HwTSLXnRUWIlB0jbZnzeo7qTKdUzqVY5C59ZvhjyXcxh8mld26X2/WC4Xfq1hJL1+t3lgusjGHJel9ejvtyoR0v9P0UdYnbObulnPgILnSmdFaEi8MOdaQmO/KUryCdgCEGVrv58QZFEBkcedo/o3fKgr2GuvqoYUgpUp9DEfV2q3Au9YHZbjWhbhKxsrwqcVehpkclv/PvypFc6jet1nl+ce6TFYA9v2dLZMk04nKRiS3KHYgUqyx2MFfMilVT01IZppojWWUy1zhGj72EGl1pcqoh9NzK3l7Pgs+Crm64w1sTXwnGCiQZTqxydUkurJvrRXx9vVAYf+40mmtS3mopFdG26q1PsSReJ/OdFyklKxlhgq02THDC6WS5XzLrWogXosruToodr1qRpTfonhHQPrxom1Mii9mRYuNQiyQMQ47bAcCH39WCKzHYsKM95ajoq85er1xeau7LMhUUNN87fJZvghPpLWOGCTeDqHJOsxWQeb6/DNgaxhRZ96q9eUG2y/klJWDJFEPncjBP1Z05QRmsltSx6IlEaCJFVdZma+1om7p1isuuBixjWHYlnmin6GS1zABcGQs7dYa53JcqXWqceJd42oFip58nYaLRAIY4hxyve6iOIZC9ka6/7UF6lIojSlCdssqjusaZhrb1MA+DKIK1a4Ve1AsbdcvyLB05oh1WcJalB1RAKlmt4f21qtjsfKBNiLx5kSY25p5Z1tuV5jFJqa+Kc5iW254PVmQn81505luF47Uhlnhm6JDmYCeDNxSiWhgGwqNHorua57XXK05ocT02SI6ya+jV8oKZLD3frDxiZV/EBteN+Zw6he05aU3JGqBQBW1gdfN0CjrOg7uB3zu7DGC96BsOrncUlrm0hqz89WonbHsISfitl+BRXNxZM5VoiBcifemu7/6qrkE7f+RymrKKCx5D9KLGzl05D5Pu2phHDQpEa03bXXrT9hehXwsDdGDCVDYOKR55GugYsLly22StYR5wlLxrWB/C9SXpFR2E327XDK2CB+Khk+Pdas4vOVYzWiRjMnPphp4V3oC3LRETy7soWRLTMoPvYSou6ZFcBMeBh0/L3L6vYvI453HgyLCKAlLjVwsXECOXju7WPuPuWx7XHGovXoUWSUMp0hoVZ0Gw7aIEVJKg6eY4pgtajxWkIJqQIig323Ci6+6I4GD/OV/QmLnjkVxYa6yNn8TcPzUcxpFxFGSegp5XgOtt3GCt34OuyFY6vk02KHeMG+rGFniqdHbK95vr3l/4vrbXs+hWSwmiyCcySw6ZPDd7TlU9z7SCGLhy0UdnkUitkAq4ilAEKgrR80L0oDu6Wfiyh22csBH7lWjEoCwfzlmAbA7x/HoqhDBdINu9oAmHBBYg9rSk69VCoOhrO1/Mt2uk0naAcaKwDOlsf1BumOww6xg5GxfzeKO9OIPZgjvMsw2xHNwjCZ1wS+nu6+3xtKk3mAIfDxK/PEJ2vU/g3aWsFTGnc6nEoVC7YZ3c6efE7beIv3Nw/XbuLE6J7ZqVNXKzaZuLBt1heXtI0qMV0al6ZSi3SZuyPYYSqtkV10s86lVWiw69PzisueZXV4W39AHTditaYQ8OzkoM0t+H7a6PpSTHiUWEXrVQYPwVVQ+buVJXYX4MpORktfQpmONgq0g85ElYXityS1bL1ZmV7QV0a3qIKtLFMaSLAtks/dYI9uaKl+SVgRQookZqoVg4FS+E3WZoirmMkklxF4aqo9oMzzAZM7LK0Q3sSpnyMT9yK5UWXdymiXgeCYinqCcJla/pQfas0mjZU7e/EAsJr9sOjjRsaa7JQXfwy/ocshzX+gVMXRZEpdUr36X6gAorIeiJ5Y21+5u1r0vhXO6uzrKNm37X2XtUFpZ634dlUoVYgJjWggkceKDvrEMN0HAOVxfnuuOvzr30nUNR1cFOlqtdsb4kqzmmnqJ1jSckcvelNYtQTFscxOOqbWHkvBdXaBdB8JZbBO2cKiGYwq9X6Z6cYHdPUCicIu6xOy/23oqg9kSNtwTaoYvD0q7zOoO6Om8RkrkvsjN8xGGFDGBBqBb+9QYvEZAV8tP1nHuNTMmHAYLyjMy3AXK4dnoAV00jD4f0zlMqf7go5oU+DCFS2YMULoeVTjCoIUYkdul6qtUskuoqVN04wnp7yEpBEBxx0yWJsCn5pNvdGAbGe58TdO8c34gb3fSbTD5fYnQp1r7LyduEdEwIWgUMKXDxutWDSHEhZ0HC1rrzhwXmYDAV1TGiwK2ZODwqDks72FpnEWWyDtatQ7PeYr0G9draKJgIwjvDTz2nSnFAquB8TohGE0Qg+MiDW9sXox5iWrUvOgbfVwZ9FsPkrLlc3dzM4cxfw0q6i/G6CkvJvGE9qnLt7oJpLMIP5ZozT5KlbJ0A6T27TpOjc3QuJ3J+MkhbxuyjVCdnaO6aAyaxrGHwGbaSrOMmXXfCUjveYDfSDhXb0pQG3/ai6XUZuivqs1wd4U1TxIlcwa4KuZfbqk+dPMBplUdp4wA5t8OtFAa2Vmz6wGAOzwddui1op0Kc8uQn24uoXrLNihXU2sTUOX3P0Pltg7hCy7GItUcqpAGr7ZuOJ8/HjWYbKyVapygGlRcyJs78ITuHzAX4/xhekpim78Mis3NeNmoC9e/zS6W7Bnk2FZDDJGzD8H3dWxqHJ4t9KuJQ0vUL1TeKw6LHTnXfsobahcvjaXB1NL45LLa2V10v31pJN5ukvyL7zZ3AIFiKJfEO0RtT0BQ00CFzqChVpjf9Pm7cAhfXewRXLQbTt8itzF3Hr5ghOJwj+t6fCZHbrMtr4LrDzqOajDFoSknWFjWPDWuu96aG5D2jBEKiiPLK5IxV4u0PjLra5SGE427eexitg1BQjfIewA66vlxc018tThk1zxoGX6srdodFK/FMn4a5Zsu79bymFd+vV9amakx+I91WtQJXaU2IZZZ5Ag+l/rGwAobm994t38xXbIDEnb201LaXXcrmC623YHrTpBd5ixYZW2kRilnHSEb3tl20baVj90pZXXIQQd5ioy+avbKU9BCPhZ7W26sDt4HVMRzUtiQg8Vi5ii+yvN13l53d7bhDpssn/ybk0pzA79xNmosLL4w3qhOYmZfFizVsbQJoqViUax52i2oNs5pr4Zq73/Fhe9rQImMi80WLtKf4ML8X4m7QboEg9um1Wja3nGPumUrkJ4JzE6TgbVCBYL7hy37L4MntnBMlHbTG6gblwkLBQZN02ldVn0j8LYrOlrM4ck1HombvCkSN7i5uFsey3jH+BuRauCnvqS2TmluqxMmxWKLqbW0n+TtKmYdE6698xqgd9uwdaixq2ft+boYGXPowFhZmoSI92dyb7NCuL7tgPZxuhGzK2jzkLg1bEImmkqRNBPayh9dxQlPrqJSGxXCIofOdueKBmzXoxrlLxS6LdnptZcekY2urjhRPX4Td3dwd3HJAvEsqquUBQXe3u8/xWEvY+jXXYL4+otWmMu7YQaIuNDpnDWx14aq+U5g4pvkEk30CbXRsV0iBD4PscpGwKob1+eCZkW6SlBjvmjy/0GQHHbzUg7wNfA6umyG4gsQOw5cAqBFQx1MO41GxWecpvyzYfsiKObDqvVzp5WIdLpQsYnAZ7i9UIgNalRrbcuuJRt8r3lF3Sm7DX3nDdLPq6vBMHylXiU2utgFlXUnvsTwvs4q4sl6oUWmZ73eQhxH1fX83IN7M6VWR+f55GRSy6QTZYpfrqwwDPAXQXzy7wkvuoLALcb3ptVbamWh75ysP8+eexJvQgp+TeKjHB50n2dvi7uNocyIa46SSgmVzBy+TxM3JQLG6XkjhDSUxzd8FBWdsT0KA4SKxT1EbIdsFgpJBJV138sVbAGpythrMNbQ5alsi2YTztlbYdiuUt8b2q2FRDORZk3wqALFBu+z1tHeSok71IVLFJkO3dw5aMNY90PAMOp06jO+aMjX4/a2KIaiXPb/GOpGrsKqa39yhqg5Km8ccTp5ErBNwsq963kpaWXPmZVEQjB+styuVyKjFtl/emuh67w7zNSi9kYntMaAHhW93shcYJ9upOBPWoHyLCsRwNhTe1OksuzdMsKFpqrye65u7u6fOkcT33jKcr2/MagvTUtKcxeIsJCqxzhenBUldA9B1UobXUpUp8n1E3XlGl9p2AcM1juRzFMT0oXEPkG9RaXjVyAup8gmV3CXH0yo57gzMR2wqsJztTfKwgK/MNnK60EiVEnHY9Hhb0JcqNJocieRMsfM9f/PwiKgs1ZHQukTkJhJzB6ZQQl+29eZQ39C2u+gLUDqpKnLqa1vnzjXIWrcOOgIj+Navo0rjz0Ue3uTVYFt3GmBlw4flrTVkj9oW61yl0FJWXMe4A3BXcFzPbXhuIwQ7HlR2S4uCh6N+oE4nT48pgDu4owVHCqAtd6ID9aYB9B1cc4mE2KITZCsANMMQ9DnMVBfvmjrnVChImnIti1usCKRfVjkU3BMBvTshwdkZ0fLqngOoGBxz3uYXKJAsTNkZ3bAxNxbSaf39KO15vSjUo5T7NOk1fIRum+LmJZ0jknd/n1AmBF8c3L4PuHV1j8zRS2R7bXCyeLrOmasisQjXoZyHO0M1543GOpZdyA3h5c6L91Ww2ZCNd9bWfYunaFSRe5WPpECX7H2aLRFP3m5vvaMSHClhbFS1RUhC7sIWMKg2GzRykuCy4AS+Oa02hLp19pCHqDvicPFxeK/ZTBlYu3TTmafhHmzusFfPN/uLPGfPrUYudri2UOTYH+abzYo7s6sSAkXr5h0gQkXCqihSgtmgDnftpCZZs/ucB/oMBRotLZrNpTV8HLvrXs4FEXLu+yRa1CaUy9J+fj/2C0K9Zl56jtlS00UhS/A84Lc3dHnx72FTEAscMvwgw6W5ea+g0sDIDpv7zRIAULjLe8ElEa6SCAVwdYgieA4zazhjbwFSyyfJsa/8kqVp/8jWSL+gVPt4QIPAKQgSrfHNMiCieDfHqC5LMXq7004gVaJk0Vs8QJtTzg+r1t5RoBzXTcnBXUmdMA70e1LKNfK5WiPmxtQXBB0bykpLySHpIJ9pfYMv8/MA21VfL+4pnZL+ydc0qC0PDM3tm6qqtCUWX9PUl6ugk2HarrHdQTzsepp+eX0Z3yP/ixd+7z85G98C/X974fR4b/T+UvHLzy/j++sv01pf/rUKv7y+1G4MFHi8L2vSLny+jhrflj1ebH764WVlMzx+VFjkrX9r315utnY4/gOBF/fxy7ZPzfTLtvHd5vgD/U/vL+9eH+Z4+UHZ15fp5f/0T0m++2UZuH78hO/x6yhwmeEkMao8/eh1euEH1AaK//4/7VFc4Z8yAAA= -->
