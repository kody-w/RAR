---
name: "rar-cat-agent-skills-copilot-studio-topic-blueprint"
description: "Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_topic_blueprint", "rar_sha256": "c11337248088a38d1cbbbba408808e2a111734b20ccebd659534832ff67882f2", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "copilot_studio_topic_blueprint_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/copilot-studio-topic-blueprint:332f77b003a8fd8b4aa6815068e23dd858062a5c0eb10a3160311c5e47568e0e", "kind": "skill"}, "version": "2.0.0", "author": "Elliot Margot", "tags": ["agent", "blueprint", "topics", "design", "power_platform", "orchestration", "adaptive_card"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/copilot_studio_topic_blueprint`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `copilot_studio_topic_blueprint_agent.py` is
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

Copilot Studio Topic Blueprint — Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-topic-blueprint
  Upstream author: Elliot Margot
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_topic_blueprint_agent.py` and embedded as the fenced Python below (sha256 c11337248088a38d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_topic_blueprint_agent.py` first:

```bash
python3 copilot_studio_topic_blueprint_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_topic_blueprint_agent.py   # or on stdin
python3 copilot_studio_topic_blueprint_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot Studio Topic Blueprint — Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-topic-blueprint
  Upstream author: Elliot Margot
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_studio_topic_blueprint',
    "version": '2.0.0',
    "display_name": 'Copilot Studio Topic Blueprint',
    "description": 'Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan.',
    "author": 'Elliot Margot',
    "tags": ['agent', 'blueprint', 'topics', 'design', 'power_platform', 'orchestration', 'adaptive_card'],
    "category": 'creative',
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
        "upstream_slug": 'copilot-studio-topic-blueprint',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-studio-topic-blueprint',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '05163d5246a491ef',
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.667, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:blueprint', 'tag:design', 'word:blueprint', 'word:plan'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class CopilotStudioTopicBlueprint(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotStudioTopicBlueprint'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(CopilotStudioTopicBlueprint().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
