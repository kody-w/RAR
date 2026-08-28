---
name: "rar-cat-agent-skills-exam-prep-learning-plan-builder"
description: "Build a personalized study plan app for an exam or certification: overview timeline, day-by-day schedule with a calendar picker, domain breakdown, one-click .ics download, and a notes tab to track confidence over time."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/exam_prep_learning_plan_builder", "rar_sha256": "35509b26742d474c7b205a420085c28a755754e18621d8599f5d4a54f0bdab35", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "3.0.1", "author": "Michael Heath", "tags": ["planning", "productivity", "learning"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/exam_prep_learning_plan_builder`. The original RAPP
agent is preserved byte-for-byte in `exam_prep_learning_plan_builder_agent.py` and in the RCI capsule.

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

Exam Prep Learning Plan Builder — Build a personalized study plan app for an exam or certification: overview timeline, day-by-day schedule with a calendar picker, domain breakdown, one-click .ics download, and a notes tab to track confidence over time.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#exam-prep-learning-plan-builder
  Upstream author: Michael Heath
  Upstream version: 2.0.1
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `exam_prep_learning_plan_builder_agent.py` and embedded as the fenced Python below (sha256 35509b26742d474c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `exam_prep_learning_plan_builder_agent.py` first:

```bash
python3 exam_prep_learning_plan_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 exam_prep_learning_plan_builder_agent.py   # or on stdin
python3 exam_prep_learning_plan_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Exam Prep Learning Plan Builder — Build a personalized study plan app for an exam or certification: overview timeline, day-by-day schedule with a calendar picker, domain breakdown, one-click .ics download, and a notes tab to track confidence over time.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#exam-prep-learning-plan-builder
  Upstream author: Michael Heath
  Upstream version: 2.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/exam_prep_learning_plan_builder',
    "version": '3.0.1',
    "display_name": 'Exam Prep Learning Plan Builder',
    "description": 'Build a personalized study plan app for an exam or certification: overview timeline, day-by-day schedule with a calendar picker, domain breakdown, one-click .ics download, and a notes tab to track confidence over time.',
    "author": 'Michael Heath',
    "tags": ['planning', 'productivity', 'learning'],
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
        "upstream_slug": 'exam-prep-learning-plan-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#exam-prep-learning-plan-builder',
        "upstream_version": '2.0.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'afe330883bb69ced',
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.75, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:planning', 'word:plan'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class ExamPrepLearningPlanBuilder(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ExamPrepLearningPlanBuilder'
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
    print(ExamPrepLearningPlanBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
