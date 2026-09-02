---
name: "rar-cat-agent-skills-process-sop-architect"
description: "Turn process notes and transcripts into an editable SOP, process map, RACI, control register, improvement backlog, and polished PowerPoint briefing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/process_sop_architect", "rar_sha256": "7b3e33d031c6c6388c76d4fe360cb24beb8092dd33e2d45b60ab5a93431d84a2", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "process_sop_architect_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/process-sop-architect:90039aa2b73873b20c94c5efffac0aaeed960a0d3ec1150dcba2960857eb3b8e", "kind": "skill"}, "version": "2.1.0", "author": "Parag Dessai", "tags": ["process_improvement", "sop", "operations", "powerpoint", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/process_sop_architect`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `process_sop_architect_agent.py` is
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
