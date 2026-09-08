---
name: "rar-cat-agent-skills-exam-prep-learning-plan-builder"
description: "Build a personalized study plan app for an exam or certification: overview timeline, day-by-day schedule with a calendar picker, domain breakdown, one-click .ics download, and a notes tab to track confidence over time."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/exam_prep_learning_plan_builder", "rar_sha256": "03a5fb8c787b71080cb833cb37f80dd8b7a981731a2b71086670ad239f59a2cc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "4.0.3", "author": "Michael Heath", "tags": ["planning", "productivity", "learning"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `exam_prep_learning_plan_builder_agent.py` and embedded as the fenced Python below (sha256 03a5fb8c787b7108…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `exam_prep_learning_plan_builder_agent.py` first:

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
    "version": '4.0.3',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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
    print(ExamPrepLearningPlanBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
