---
name: "rar-cat-agent-skills-skill-authoring-coach"
description: "Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/skill_authoring_coach", "rar_sha256": "123cd43acf80de040e407c00cd0991d61bd4c8dafd7972602a769fc8f647b6e1", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "skill_authoring_coach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/skill-authoring-coach:76845189c4a3bcc367e6c045b609d2e32f431cfb0447da9d0c5157695796a43b", "kind": "skill"}, "version": "1.1.0", "author": "Simon Owen", "tags": ["skills", "authoring", "documentation", "productivity", "agent"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/skill_authoring_coach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `skill_authoring_coach_agent.py` is
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

Skill Authoring Coach — Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#skill-authoring-coach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `skill_authoring_coach_agent.py` and embedded as the fenced Python below (sha256 123cd43acf80de04…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `skill_authoring_coach_agent.py` first:

```bash
python3 skill_authoring_coach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 skill_authoring_coach_agent.py   # or on stdin
python3 skill_authoring_coach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Skill Authoring Coach — Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#skill-authoring-coach
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/skill_authoring_coach',
    "version": '1.1.0',
    "display_name": 'Skill Authoring Coach',
    "description": 'Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging.',
    "author": 'Simon Owen',
    "tags": ['skills', 'authoring', 'documentation', 'productivity', 'agent'],
    "category": 'general',
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
        "upstream_slug": 'skill-authoring-coach',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#skill-authoring-coach',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'dd0ed10e586119e5',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 1.0, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['word:design'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class SkillAuthoringCoach(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SkillAuthoringCoach'
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
    print(SkillAuthoringCoach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
