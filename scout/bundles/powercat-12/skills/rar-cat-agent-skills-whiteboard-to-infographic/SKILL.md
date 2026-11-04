---
name: "rar-cat-agent-skills-whiteboard-to-infographic"
description: "Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/whiteboard_to_infographic", "rar_sha256": "0d39d06f2819bbe36cb4e09d6d08401cba0232f23a379f9af09035cb7ba4af4b", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Andy Zehr", "tags": ["infographic", "whiteboard", "powerpoint", "presentations", "diagrams", "design", "consulting"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/whiteboard_to_infographic`. The original RAPP
agent is preserved byte-for-byte in `whiteboard_to_infographic_agent.py` and in the RCI capsule.

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

Whiteboard to Infographic — Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#whiteboard-to-infographic
  Upstream author: Andy Zehr
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What to produce, and about what.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `whiteboard_to_infographic_agent.py` and embedded as the fenced Python below (sha256 0d39d06f2819bbe3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `whiteboard_to_infographic_agent.py` first:

```bash
python3 whiteboard_to_infographic_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 whiteboard_to_infographic_agent.py   # or on stdin
python3 whiteboard_to_infographic_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/whiteboard_to_infographic_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/whiteboard_to_infographic_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/whiteboard_to_infographic/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Whiteboard to Infographic — Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#whiteboard-to-infographic
  Upstream author: Andy Zehr
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/whiteboard_to_infographic',
    "version": '3.0.2',
    "display_name": 'Whiteboard to Infographic',
    "description": "Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container.",
    "author": 'Andy Zehr',
    "tags": ['infographic', 'whiteboard', 'powerpoint', 'presentations', 'diagrams', 'design', 'consulting'],
    "category": 'productivity',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'whiteboard-to-infographic',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#whiteboard-to-infographic',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '8ba98fb5f2eb84f8',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.571, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint', 'tag:presentations'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class WhiteboardToInfographic(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WhiteboardToInfographic'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(WhiteboardToInfographic().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abObSJfmX9Hc90O5Gvuyic1vdMQAEiAJBAixiHKFi1WA2MQiQDX13yeRrq9d3VVvd0fMl5EdNlJmnnzO9pyTSv3+4vVdUjUvn1/YMpwWbpQ0Lx9fwqgNmrTu0qoEI8e+KRfeok6qrlpUMXhMvDL8FDbeUC6GJO0iv/KacFE1i7qpgqhtF+0l6oJkkZZgBVhZ5WmbROHHRZCnUdl9aiIPbJaWcXVuvDpJg0Wbp2G0+PBa193488fFOSqjxuuicFF6XXqL8nn2okuihQeGup/ahTYB3OUiqMrOS8HkVwA7Gr2izqP25fMvv358ScHzy+ffX4Lca8FHL/Y70mO1+b41WJd75RlMqB8iwfs6auKqKcBHYRQv3t59aKM8/rj4t3+7DF5zbn/+/KVcvL2+vMx/Dv0TYVd57Yw88GrPT/O0m14XbD54U7toog7YsgUmabsmLc+vz5XfJVX14t/nsQ/PTV7PUffhy0tVz8YAzvjy8vNs5S8vTT8/v85S6g8/v+bVEDUffv4up+39LAq6WRhA/fr17f2bWDDx+9Q0Xnw1tDX/tlcTBWkdAeE/6De/ntDfxL2Z5Otz8oeq/rj4a8mzPv8O8D4Dygdy/1ossAFY+fKaVWn54W2PprpFpVcG0Yef/05skETBBcRW99+S+8tTcAKCD1jrzSQg2GYX/LqA3nR7l/n329YgYP4nmoDp37Z7N9TfyX549j+IzkGAt+++/Etxf7UA+vfFL3+r279a8HERf3lZRTlIvMbz8+jz4vdHiPzyU/j9w59+/QOI/i/FGFXfBA8JXwuvTOOo7b5+/eWn9vHxT7/+8lNfgyiOvOJr3+R/JfOv7PrY508WfJv14c9rwf5meSkrwFPvObT4var/V/PH68LyAOd8/7z9vPgxE+cXtJiV+Lbp0wQ/ZGMLsP5gx59f/gCkUwJt+uAxDPjjH/9YKGnQVG0VdwsjqPpuARzcpUU0gz8mabsAf2fWaCJg1zYFhn2bB+J/9vCMGHDub/878LpPD/L71F7SPG/h78z7tau+/kCmv70ujkBi1aTntPTyxYHVtC/lY+28W91EbdTcAEP5Uxd9Aon8aX6YCfa3v5X59bH8tZ5+WwDu/0bGB34z01zb59HrrJCdROUb/MArF9EYBT2QnFcBgBGngJo/AkXbKr8BmpyVf6iyCFNAJF3VTA/ZwECfZ2G//fab77XJl/LJy/jiWZNaGEx4h7P49AnoE+fpOem+lFGQVIuffv/jp8X/WfyrVQ/h8x4aKA1v5gcIt4a6X4B06gswDXgG+BJwxcP8v//xZlUgBlSbBXBWGqfRczEIx0sUfjOxIbGfMIJc+BEwLTBrUVdNB8h+kXavi028eMcLNp2H5nKQVG23CKM6KsOoDCYg1QPqvFuyrLpFC2KujaePi76NHrv+5jfeA2IB8trrflsovAaKT5WDf2aYj0lgcVWmwPzvAfD8HAhpQBXlvol4XeznAFzU3uzvxnvbI/aefgFF59vyR0Uvo+FLORfYaDbVIxue5nkUblDPny79NPsc1OgCpH7Yftv7e3E/Pkpl86Vs3yLda2ZXBID5wabnPg1n/v/nW0i1SdXn4cN+AOks6c0L4ZtX3mLwvSEBUH8o9IsvPYagy8X/H+3MrAorioe1yB7Xq8V6fzycniae58yueHZuoL1YgDh7ptP3luMbrXxj1y9lnoJ4aaZ/Pmc+HPM258lYfQPgHdjDdwwPuY+gnYOwaeZw976U32j8IzDFg7MAbpDhIANmg3/bcB79hjQBaTy//17SH04GNgaGB4G5qHs/B1aLoyj0veACUM0m/eYwEMHR7CjgG+CEH7VaAOkgUID8BQCRglQCVP8w3b4CaoKci5uq+D49nVswgCLsA4A2iZrodWGD3JnjpwUJC/qoeQ6wwk8PUYsiAjYGEN8t3CZe/QRTNZdvAL03X/xo/7eh755/IJnBA5le6HXAksNMumE0Pv36jvLNUwBqMWfnM07+5Ow3TRc/Vpt/fikfCN95HiR9PhfqH0yzAMlWtA+WnTmrBbxTRG/hA+LgUZNfn2X1WbffsXxe8OxxwT4J7lF/Fh+Kb5XtUQTNP/vk8yLpurr9DMPv017PaZf0/mtawf+pmP3je+J96qpPP+TSn2Q/zfB58X5Y+dPoWzR+XqCvyCsyD8lpEM3h9vb6vOjLd8748MPzm7ce3pgTu3yQIYiVOTDnXH80G4fouzsBkqoAyTxbeQKV9L3OfJsCis25ic7z5GfdaedyNYAK+ZANDP6lfHf5WzoAHi/Pc5Fsqx/S9FFwgQOf/nmvB2Co7MDe4dyRnaP5AJTP6rbRy+eyz/OPL6VXRP/y4DOzPQhHYLb5oAQSA7Q2XRo93nl9mM62m5//fB5UHw9ePudONVfOmdq7bzZ84A4bAGpOtnM6E/zHBcB67pKHKsOccHN74APV2hYU23DG3k31DPZ5MJpbqfc+6z8jeOQsIJuw+jyn7sfF3BMDOv7W3n5cfDtwPI6FZQ/Ocr/MrfWsM5gK/nuf+37c9aOXX/8Cxlun/fcg3vjk40M5z58r1aziX+gEpDXRtQelMZzxfFfw+77Vc7M/Hji75yn095dvlPHmpbe+EEwHufmpnYsjDEIebAjeP4MNjP0POsa3lYDcQOMCliIhzoQIGWM0yvh+hJOBv4wQJiRDhF4iaOB7CIZjMYZ7OMXEjBcjDIITgU/53tKLlz6Q9wzWr3PtT2c0foDEKMmgNCB5xscwnEToCIlxhqRij4xwLAppBEF+WHoB2fim4lOl2X7vzesjRJ+a/v7ik0swU1q2G/b54mHI8ihH9sfEYTIyPg0Zs+mSY9WrCFJHLZb26qW85FkWOTZCVkF4vrQHSz+f1aGXJcEM40qPgw1kBBDTw+fLLii37s5zo0y3uege3ZwWvmconiPwOoYpRoanTUeGpUvvCtq1J8ZQKeOEnmriYkA8HvJSUQdZ6xw8as14PntlNGfIp9w2fKPcQhEVTcUk5R7BmgzEKfTag51THpp2fdiJyOQQlypn1seTXhjCcX241ohcqGh9c/bHbJvubMg1bECuXb7i7Nw+qYHLrJel0iHjoHXFjh6bth4VfSqW1y7bQ8GdIlQaaoreSWPiko9+5KdwXDqXZYpgQuLfi+AuNUOdbXGY7IubVuddrtzbQ2oISrq5ySt9RJHmaNyGW1PqxbHzC1jsI39ana+XBNsy8cG1Kxw16l1KFLbr5LzYXloTbwoNsYoNvEysbttu1M7dSkSMcZpHjUeZ3yHDodWCQ0nojhNf2k0TXiVP20AKfR4EIS+ni1swGk5TAbXPy9bXS1gr1je7LlDiZl5zMwn9HQJE7VHazMNmu11OppbS11Dly7WGxYdr5+ZueVR6FMMy6r5MliZxC5nEpwqyNeTI4HtsSlJ6i0LyVKyofbsbSiROM3iQqkYwIVuSjrqVEtF9Dx3b8YSK+EY/gKHR3teTrGyuKa0uCQzdNUrXHWpe9fQ8hWRpl+l5U9fBKFn9+Srg4ogHFa3Ym3b0LU+NLdVBGGhLEbulJ/TcWr3Q+tpNj2ql4TDLHpgMGgskKg497MAQJ65PXE/79CjubiK138LUvcEhOSRM8V4lkwlxeRv40soaqUuREOXpZtPJga0NIh15UM+7fLlkNpqybNv9oResDXbPgca5Oei6i6LH7akwqilrGx2/kAXrE7YttKltLHu2crLMkKRtOh0xkrs4velcdxwiDFHuOBTKMKFT92gYp0Ic36QbRSzT+xlxz2nNWts+M6l6tcQuwlpe94SR7cmkYTZRbno8ZGO6e0q3sdNHB9jz9LNoyWK3lw6rvXzatcL5Ukrp3t0evHrgWNFgt0jmsLzLtlq6ikwoVUZeU5KivBJRAqprIPLrEB4IPbZ46l5wm14uuFhc4SyNXa3B5pra3VnZjj7dlxJJ7NJgOlcBt4VZaI8z/DqzVWK3R85KR0ctmdAFtPN5GBZ2begLHYep5SQJ4VYwFe0Y7iqEZ+rhILpJP5p5Ph5tdYAPa5ntKba7lLq4d1tXvSC7WLeuk8fAfovVUNRV6EVAkpJ3+V232i23t3GPLuH7yVPDkB1tnNtW/a5sVCZuj9yuvMhcFmosc1KGZTz4lKY0BW+jHcXvbgha825rupAbGAXGV7Ecs9SG7+x2e9EJeBpNW++dmoTWZNBC7n00NhPueYNskveOUzUY00I+xeD9laXWlC35l7svHItxRNrCa4qkPPuX5d0V3Bhd+7iD1xsMUr0bjURVhTtkNFZtNsGQl07ZunC8cBjl7F5Y97V2XV3uBzsysYPOCRvouJTPjV0xPGfv5HBnHeX2eCWQoTUJWZD3JC82Tm15zn6fWoq5F2jnmpXi4aTaKU2JShQaKmyJpx2Nh8bFGtfHUoEqZytZina2bHIMWXmNbONBsAW/Fe6AapMgTeIUKBYmkx9tJBJAlcKTZBXKml6GEXPvLWupwteNnWmTSWGoF/vaKWJKJlYue9ssQrrzGEEyfeNUuci6lLVxXEpcp3OR3il0sVU7xnbymla3KbpSI1G2qEqGd2xrjPKOpeDBTs8HM9/eFcYQdturdcNtt0SUa6ghyt4sdLvIDi60Pya6c3DJA1ktTWWvspyN7oHoS89VnrUXyOrEVvUAQ3DoxVaf2xJW02fownjyuGoT85zpPNJpd3ql7mrucvJa3NAzGEmPSTOsBiOG95sbMhoH2WdEZONtPEIuD5uG8kTMWMplyW82Ec+0PFpuUoHIEUA7p8o+rpEDHrPOQWmx4C7YlnsuOOckm1yKIkawIljICs0shffHYkdADALOQ516D6Ei3DXIkR0Pt3ZFIud42atcZa/ivbbLLvK6qRvfRYqjtTUvZFpXkotjDuEyNM5tQltkT9SZ2vEbeo+RtYAPyiq/mVSmjYZ79ZtSIk4XL9EsWHZKknBu6ACbZKfFlAShbE9fSdWY0kqfPHkN2pDkVvERmW+4OrCd69HHtgp5CWJnxJCmllxLIxvq2gujVRSVyLLb2r2sMtWUxwDBg42lQH0ihFdDqpvMNDc+VOS9jU6iYY1je8tQqXEtsRCDFYML7tauzq6U8XWxKe/9mmuUm9WOlHJHsTrjmcEnUMJAljzqi1he76woNmyULjECu2tWhO9AYuV7HZLTzITcMV8qJwnveEnuzynPFqtCcy9UtkMRSUAMUta7boxiJNWU1FxF4+6KL1mIrU2My53RtcrmboipHW6P5bEbtSIL6WN3cOV8tzYJG20t2RMNgsOQpSsdw+vIbCDxsNL5zuUgyofaLbZlB9rmh40ty56RBN3K6EXyoCs4DOC2yt2vkTPu3IqLVdOyFOjbkZUDU94L7s32FR1Os/UpIwSHg3e07xjrU9KAOnG9bnllLSr6Xp5g9W5Ny5u+0mnnDkm2fROPm0u8J6/0SOywaJmuN4Uf8pUY9Zdj4kylYDBVt0mT9KrYkphv6yIgOIm1O44TQc5GK4e6VKie7Ei1TdH0uHIzPun7lbR1lTrA0DNWplDrIRVqmlUnmsNy0A9dvFOnLb8hGozVL/xNGAXA23ax1iDrfDneiwK7AkJfbrKCEG11GZPbw+oyddWKvySA4+pKJHYR76Ha2ptOStPznLTfO3ZoXsUMPk77+FJInJESor9uxYtNaTvzOvY6z5leXwb+cGZo0MX4knneEDy+624yZh3S8r5FvctpHRwC2toJqSMIScgoyUCuxdOqCAbAzLJpKzSvb0M7rc2CxYh61U0crh29jFkOBbFx98cD4vP60a4JQs5aA3XXSJCkOcMZQ27BxvHKRWdUAR1jDw60DTGgRnOjFXdDuojIbktI9bc+1gvHWGs9yZBoq+Gs64q9juge0c/tNhPWJ31V39bIUEtFDMP8UTpHqRPvaj6Al0qDjyRfHQeu7wycLia2uKr1gUoFqlppSYLdgzLcEOmAxiimuVaTT/G1IM6rkGrUuDwy5n5zJqftqYwuRliPDiUYBsefFauapsRzKRTMt/gJ0tih1s8c0Wz40XWxsdZFzsgtxVK8qDXX+SGETDrcbxm51G+WoRtS0UrhMdeNGyVkV66TWsukKBl0Lm2co4lvM96UG5O5vp5sm0Dt1Iu1zUVP7jliHUg57Lu91XcczPLy1PkelurMATRyYkk5wcHHSks8YCrtHLmSLwROCFy8E0H7f8NHvY/EYsTXmnrOGmKX3ORKWRJZC3FYY/UcYQQiOEArJDwZlu/CJ/ZWIEvHk6VCiLEJI+1tfNVqw/E2qHXoJHe8DEd0p3P6cce4lapeVXC06Gxsr0K74wVk6rl3GsSv7vJwJ1URuRp9f7rsbkllquoa9Mkhzg1dUId7JN3frynKn5fWzeqjuz36Z9MvQg0iEcFHMQSX4eom0Kp7i4lekaW7n6VaayJceZm0Potv1/igb1F1UGiths/pct0kVwcwnU5nvmnHuTRUI8k0VZoWq1Ol3RPcqE5HsybmdsmzgkGj96CyCVmMtE7vWEyvXkddFOxch68tcchX9JmOSFbAx7JwVjjGJWdSpdS73GIu3yoSAqXOebck1Umip+Mg7ZPYOgkCIpdUBuX6bav1eFpEgIvD6k6PJThTWKWXQ5sxlbTrSHIcHy7bsXYVySuy5ZpIKIkll7QeuRbolIN9c+JP9BCz02FNVpfTMd1OWziP9js/v1LhXSuilLKnUMxW/lLjhpFU/UMKwT5JEwmeixtmq8SRmAuFdKMvchD1S2rglwIeBtxKRU4UvU+gvh/wyqjgLF0lkopAJAmOM3jkaCZSprlpHSJwLBM2UUcdegIwdHpa0agwoCS93mAak6ISSYZE7RAnmEq6g7y7VARozdj9wWXpKE5CNWnc+/LeFZsiqyMIY9tTumx3yFIZuzia6BtT4dexM3ta2/H30g8mjYBwvoKH+ybh4kTe420EWjhtVExSUDe2im1KxC9IgVpvsssAV6O25thhw55J5eSUtWMc+vS0JfuoMBtYOKkpfyro3bgarOJasRg4vpUDc95KzEAa492/Z8QgpUlNwrzCb84OE+1uaKiWd4IQzEiH1sL1Zvb+eifk+e0YcyMpJ6wtFhyXRzUsHbhNK6rpJFaBTIajepUzYtWA076zNErFRTga2MkbTerWtDqPr/3ofpPKw+G+oTWhSnrzbpeZlMKGEuya+/1IbyIu1dBpdbugfQTvRceuV+lKgxQuO6cGHB11XxSzZqDDQ6lI6/BW3G8XKqHKexB5VDfsuECtK9yvG89F1PwOTVe8LnJtgmvb5bJrySKjJOAI26BEZKwUb2B3OLMRRBQ3u1UncgILHUpG2t6TPlkPxaCr27aArii0TJN7gdnQ2qZPK90/M00bi4wX4/4Vv9wbp8OiHqKhot6tVHlVLu/t8YBepW7DXKleUMrW6fDB6nj8cI5FR70mh+AakFTT7mIfknBYMZRDs4sQLa5JnghFYSNo7Oo0XFPWhGrD7vp9jKPLQKywS6QkVwJdtTkLrCTd26i4gzMtYvMk8OpRXPcOg4REvr0Rzqmm7+bqusnNe3sGPW7Kt6up6zU94YgjgV4hIhMDBwY+GLjzyfDpPmM6e725YfcJR3Q0iZILsjnFS71e7e/ETU9Ww3iv99tIs29JY6+RTi0L9jAOdYxSwr2XupCs9wxRtuINr9OBOHlVvJOviH9U3Ri2HNqKnEiqTgLNYzeVCzRhvb1mtkjZULo63Db62JPO5h7vyiVxhE4l3Q33YkVuuwbeNMfI4WzmJjmWALnqWKfa9lbqZZgaZtLIWkpZCN5VgHn9SUNKUkF9XHVw7ZYLFAvdjsOUC+C4PhY3Uwov21xZpYiySpYRX+DFNQrX2ioPJJzzL6fOj4/i1ZgG9JBgvrSzYSmi/C1FkbwKjgTc6QY1rVvtRHskBz3ul6oc5U11O3a3va5ebWu/dAtagfRKq5HhatlFeh8h12V88nyiC59STcuw7f6+1WpdNdWTzCytUx7Ao0UpNLVa6oejBOnMtdVuS+KUbcpmDTaeKiloZfe8clf4YNSZVC9h6DZoB5xEyggmNz4i5Jv+kCBbiLn18tXqt4IYbv1CpMrs5tjLsKyr5og5A7SrXT9d5XDqEKSi00Mj3uDTBcKN5FCKUnKs+cS76s6GYK4BTGYRmWJXWd0MA7ND+zbK/NFy7YRpIcOAV9mKos+GvdRFsVYIDkXjqdhnVM7SGw9TTwyb8WcvJ45L/mJLq9PknVvazb06RBxHhVl3pd8CUY59KexXeWZzfnZpqQt+dGh9B29x8YId5X51lkgllAxN3Fb3tKJXqB7akLQMmRjnUWjtUAerwnALoxAzprd0Dqq5bEuETrdCAOcak/uTx8tnlmovSxB8B1walJPWbJeYcMtROEe5AU0YP+3SBK56kdLoS3sMm3KSFQiFcqxlwKkp4gbEW9KanGAhnNDSVEN7NrbLiiE2N/9YQtShBU1rWTMEA1JwN23HIsflMhYiRZriYxdsYza304llxfIElWG7Rof1QVtZe3MLWMPZlfUKN1HJGZtLIBfHRF3lG8hBJCqRD6vDSZMEyMy28tYvdWin0p7M9Hqo1Vm3QUcqLkFl1ZWW2WZRLJ5olUegnbZfmn4uId06oiDQi966HVEoul+Kt2TnbUkrZNGB3Au3jrlH2pWCaVE72+YqvwukC1oRLuzA+dQxIBqBL00J7dMQ4o0r4gnucuPICFIODnTGRsAe+zPLvnx8me9Z3m5L/uufQMxfUf8/+6b8+aX2t3vRxzVF5IWfH3t9/m9g+fXjSxOkAMnzAqDN+/Pbl+b/8ev/T397xTavm54/JJhvbMfu2wVSBwJ/hvTnud/lzNcp80/P6iot54uUx7fzb78HaOeLldQDy4r2eceSnh8XL2Coz+cfRMzY367sAGT8FXnFXv74v816vkySKAAA -->
