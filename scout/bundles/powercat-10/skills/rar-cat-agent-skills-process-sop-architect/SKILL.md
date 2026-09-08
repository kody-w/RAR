---
name: "rar-cat-agent-skills-process-sop-architect"
description: "Turn process notes and transcripts into an editable SOP, process map, RACI, control register, improvement backlog, and polished PowerPoint briefing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/process_sop_architect", "rar_sha256": "174c35849b502c0837ad6690e7045929d441db09a00f385fe55e768f99c81a83", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.1.2", "author": "Parag Dessai", "tags": ["process_improvement", "sop", "operations", "powerpoint", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/process_sop_architect`. The original RAPP
agent is preserved byte-for-byte in `process_sop_architect_agent.py` and in the RCI capsule.

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

Process & SOP Architect — Turn process notes and transcripts into an editable SOP, process map, RACI, control register, improvement backlog, and polished PowerPoint briefing.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#process-sop-architect
  Upstream author: Parag Dessai
  Upstream version: 1.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `process_sop_architect_agent.py` and embedded as the fenced Python below (sha256 174c35849b502c08…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `process_sop_architect_agent.py` first:

```bash
python3 process_sop_architect_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 process_sop_architect_agent.py   # or on stdin
python3 process_sop_architect_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process & SOP Architect — Turn process notes and transcripts into an editable SOP, process map, RACI, control register, improvement backlog, and polished PowerPoint briefing.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#process-sop-architect
  Upstream author: Parag Dessai
  Upstream version: 1.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/process_sop_architect',
    "version": '3.1.2',
    "display_name": 'Process & SOP Architect',
    "description": 'Turn process notes and transcripts into an editable SOP, process map, RACI, control register, improvement backlog, and polished PowerPoint briefing.',
    "author": 'Parag Dessai',
    "tags": ['process_improvement', 'sop', 'operations', 'powerpoint', 'productivity'],
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
        "upstream_slug": 'process-sop-architect',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#process-sop-architect',
        "upstream_version": '1.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '3851098193863859',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ProcessSopArchitect(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ProcessSopArchitect'
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
    print(ProcessSopArchitect().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
