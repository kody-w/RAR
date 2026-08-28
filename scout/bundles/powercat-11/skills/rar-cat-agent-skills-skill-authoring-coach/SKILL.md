---
name: "rar-cat-agent-skills-skill-authoring-coach"
description: "Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/skill_authoring_coach", "rar_sha256": "123cd43acf80de040e407c00cd0991d61bd4c8dafd7972602a769fc8f647b6e1", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Simon Owen", "tags": ["skills", "authoring", "documentation", "productivity", "agent"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/skill_authoring_coach`. The original RAPP
agent is preserved byte-for-byte in `skill_authoring_coach_agent.py` and in the RCI capsule.

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
