---
name: "rar-cat-agent-skills-exam-prep-learning-plan-builder"
description: "Build a personalized study plan app for an exam or certification: overview timeline, day-by-day schedule with a calendar picker, domain breakdown, one-click .ics download, and a notes tab to track confidence over time."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/exam_prep_learning_plan_builder", "rar_sha256": "bd985899fe983b4f68a0f915ee19628c54d774f79167fafef7a7e2866cbe7fdb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "4.0.3", "author": "Michael Heath", "tags": ["planning", "productivity", "learning"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `exam_prep_learning_plan_builder_agent.py` and embedded as the fenced Python below (sha256 bd985899fe983b4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `exam_prep_learning_plan_builder_agent.py` first:

```bash
python3 exam_prep_learning_plan_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 exam_prep_learning_plan_builder_agent.py   # or on stdin
python3 exam_prep_learning_plan_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/exam_prep_learning_plan_builder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/exam_prep_learning_plan_builder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/exam_prep_learning_plan_builder/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
