---
name: "rar-cowork-cookbook-ppt-exec-measure-goal-achievement"
description: "Builds a read-only executive PowerPoint deck on measure goal achievement from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_measure_goal_achievement", "rar_sha256": "d2e22255b33e611632874992651e6a82839b9a026736a97811f9e923d62a7b92", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_measure_goal_achievement`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_measure_goal_achievement_agent.py` and in the RCI capsule.

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

Measure goal achievement Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on measure goal achievement from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-measure-goal-achievement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "comparison_period": {
      "description": "Prior period to compare against in the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull data from, e.g. USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "output_filename": {
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-measure-goal-achievement-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_measure_goal_achievement_agent.py` and embedded as the fenced Python below (sha256 d2e22255b33e6116…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_measure_goal_achievement_agent.py` first:

```bash
python3 ppt_exec_measure_goal_achievement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_measure_goal_achievement_agent.py   # or on stdin
python3 ppt_exec_measure_goal_achievement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure goal achievement Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on measure goal achievement from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-measure-goal-achievement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_measure_goal_achievement',
    "version": '3.0.3',
    "display_name": 'Measure goal achievement Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on measure goal achievement from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-measure-goal-achievement',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-measure-goal-achievement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '64582ce9ab7990da',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-goal-achievement'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-measure-goal-achievement', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-measure-goal-achievement-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for measure goal achievement reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on measure goal achievement for a 15-minute monthly review. Produce 'ppt-exec-measure-goal-achievement-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads measure goal achievement data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on measure goal achievement from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on measure goal achievement for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-measure-goal-achievement-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready measure goal achievement deck from D365 ERP data for a short monthly review; requires the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMeasureGoalAchievement(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMeasureGoalAchievement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-measure-goal-achievement-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecMeasureGoalAchievement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
