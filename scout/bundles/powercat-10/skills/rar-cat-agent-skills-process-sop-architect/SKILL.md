---
name: "rar-cat-agent-skills-process-sop-architect"
description: "Turn process notes and transcripts into an editable SOP, process map, RACI, control register, improvement backlog, and polished PowerPoint briefing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/process_sop_architect", "rar_sha256": "174c35849b502c0837ad6690e7045929d441db09a00f385fe55e768f99c81a83", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.1.2", "author": "Parag Dessai", "tags": ["process_improvement", "sop", "operations", "powerpoint", "productivity"]}
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
