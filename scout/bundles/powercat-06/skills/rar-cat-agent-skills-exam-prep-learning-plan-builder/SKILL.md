---
name: "rar-cat-agent-skills-exam-prep-learning-plan-builder"
description: "Build a personalized study plan app for an exam or certification: overview timeline, day-by-day schedule with a calendar picker, domain breakdown, one-click .ics download, and a notes tab to track confidence over time."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/exam_prep_learning_plan_builder", "rar_sha256": "35509b26742d474c7b205a420085c28a755754e18621d8599f5d4a54f0bdab35", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "exam_prep_learning_plan_builder_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/exam-prep-learning-plan-builder:54aba7b14bc74ef646777c3354a85eb1f14288f65b5c5881ac7205f13e27e163", "kind": "skill"}, "version": "3.0.1", "author": "Michael Heath", "tags": ["planning", "productivity", "learning"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/exam_prep_learning_plan_builder`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `exam_prep_learning_plan_builder_agent.py` is
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
