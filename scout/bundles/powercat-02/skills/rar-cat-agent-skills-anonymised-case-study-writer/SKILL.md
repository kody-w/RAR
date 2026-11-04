---
name: "rar-cat-agent-skills-anonymised-case-study-writer"
description: "Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/anonymised_case_study_writer", "rar_sha256": "49d3b3efccee510686f44a4fed6b95a9b507f706bb3c594d126aa9cda655b398", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "case_study", "marketing", "documents", "content", "privacy"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/anonymised_case_study_writer`. The original RAPP
agent is preserved byte-for-byte in `anonymised_case_study_writer_agent.py` and in the RCI capsule.

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

Anonymised Case Study Writer — Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#anonymised-case-study-writer
  Upstream author: Simon Owen
  Upstream version: 0.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `anonymised_case_study_writer_agent.py` and embedded as the fenced Python below (sha256 49d3b3efccee5106…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `anonymised_case_study_writer_agent.py` first:

```bash
python3 anonymised_case_study_writer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 anonymised_case_study_writer_agent.py   # or on stdin
python3 anonymised_case_study_writer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/anonymised_case_study_writer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/anonymised_case_study_writer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/anonymised_case_study_writer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Anonymised Case Study Writer — Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#anonymised-case-study-writer
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/anonymised_case_study_writer',
    "version": '2.1.2',
    "display_name": 'Anonymised Case Study Writer',
    "description": 'Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details.',
    "author": 'Simon Owen',
    "tags": ['writing', 'case_study', 'marketing', 'documents', 'content', 'privacy'],
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
        "upstream_slug": 'anonymised-case-study-writer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#anonymised-case-study-writer',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '30ca39e3e8405c3e',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.857, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:documents', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AnonymisedCaseStudyWriter(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AnonymisedCaseStudyWriter'
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
    print(AnonymisedCaseStudyWriter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716abOiWLruX/Hu/lBZTeZmkik7OuKAgiAKIpNaWZHFDDLPYt3673ehO3dWnVPVp0/EjWNG5EZZ653f53mX+OuL03dx2bx8ftGTvCwW6hgULx9f/KD1mqTqkrIAt4y+KRZBETlRkAdFtyjKLmgXSdGVC6coiylP2sD/uKh6N0va2HGzYOE5bbBou95PwMoxATr6bhHcqrJNimjhZQmQ88krizDxwVXiZAs/6Jwka1+B9uDm5FUWtC+ff/r540sCrl8+//riZU4LPnph31WugBId6JjsJumCBuzMnCICS6oJKJz9qIImLJscfOQH4eLt3Yc2yMKPi7//PR2dJmp//PylWLy9vrzM/459sejiYNGVTtsFPnCmctwkS7rpdcFmozO1iyboQFDahQOcbIBLr8+d3yWV1eKf870PTyWvUdB9+PJSAhOcOapfXn5clA3Q1/Tz9esspfrw42tWjkHz4cfvctrevQZeNwsDVr9+fXv/JhYs/L40CRdf9QO/etPVBF5SBUD47/ybX0/T38S9heTrc/GHsvq4+HPJsz//BPY+K8MFcv9cLIgB2Pnyei2T4sObjqYcgsIpvODDj38l1osDLwXV0/1bcn96Co4DxwfRegvJjx8f6ft5Ab359i7zr9VWoGD+J56A5d/UvQfqr2Q/MvufRGdJAfrhWy7/VNyfbYD+ufjpL337Vxs+LsIvL+sgSwZQd6AvPy9+fZTITz/43z/84effgOj/Voxe9o33kPA1d4okDNru69effmgfH//w808/9BWo4sDJv/ZN9mcy/yyuDz1/iODbqg9/3Av0m0ValGOxeO+hxa9l9X+a314XlpMl/vfP28+L33fi/IIWsxPflD5D8LtubIGtv4vjjy+/AdgpgDe997gN8ONvf1vsE68p2zLsFro3wxlIcJfkwWy8EScAENsHajQBiGubzCj4XAfqf87wbHEZLn75D8/pPgEoBQDYpkmWtfB3EP064+bXGTenr+MD1H55XRhAaNkkUVIAmDyyh8OX4rF9Vlg1QRs0AwApd+qCT6CXP80XAJwXv/wrsV8fEl6r6RcA4f68fDb9uJJmsGv7LHid3bLjoHhzwnMABdwCrwfCs9IDloQJgOiPwN22zAYAlnMIHg4t/ATASVc200M2CNPnWdgvv/ziOm38pXiiM754UkwLgwXv5iw+fQIu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 -->
