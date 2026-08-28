---
name: "rar-cat-agent-skills-process-sop-architect"
description: "Turn process notes and transcripts into an editable SOP, process map, RACI, control register, improvement backlog, and polished PowerPoint briefing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/process_sop_architect", "rar_sha256": "7b3e33d031c6c6388c76d4fe360cb24beb8092dd33e2d45b60ab5a93431d84a2", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.1.0", "author": "Parag Dessai", "tags": ["process_improvement", "sop", "operations", "powerpoint", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `process_sop_architect_agent.py` and embedded as the fenced Python below (sha256 7b3e33d031c6c638…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `process_sop_architect_agent.py` first:

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
    "version": '2.1.0',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
