---
name: "rar-cowork-cookbook-ppt-exec-measure-goal-achievement"
description: "Builds a read-only executive PowerPoint deck on measure goal achievement from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_measure_goal_achievement", "rar_sha256": "d2e22255b33e611632874992651e6a82839b9a026736a97811f9e923d62a7b92", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
