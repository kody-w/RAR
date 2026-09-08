---
name: "rar-cat-agent-skills-exam-prep-learning-plan-builder"
description: "Build a personalized study plan app for an exam or certification: overview timeline, day-by-day schedule with a calendar picker, domain breakdown, one-click .ics download, and a notes tab to track confidence over time."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/exam_prep_learning_plan_builder", "rar_sha256": "03a5fb8c787b71080cb833cb37f80dd8b7a981731a2b71086670ad239f59a2cc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "4.0.3", "author": "Michael Heath", "tags": ["planning", "productivity", "learning"]}
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
