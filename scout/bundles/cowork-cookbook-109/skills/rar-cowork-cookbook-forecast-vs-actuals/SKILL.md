---
name: "rar-cowork-cookbook-forecast-vs-actuals"
description: "Compares demand forecast quantities to actual sales-order quantities for the same items and period, computes absolute forecast accuracy, flags items under 70%, and returns an Excel workbook; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/forecast_vs_actuals", "rar_sha256": "3d9b94371d5b3ee154f46baff6d22255cd56f7dc4777bb9349dc5b8f567035e3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/forecast_vs_actuals`. The original RAPP
agent is preserved byte-for-byte in `forecast_vs_actuals_agent.py` and in the RCI capsule.

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

Demand Forecast vs Actuals Variance — Compares demand forecast quantities to actual sales-order quantities for the same items and period, computes absolute forecast accuracy, flags items under 70%, and returns an Excel workbook; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/forecast-vs-actuals
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
    "accuracy_threshold": {
      "description": "Accuracy cutoff for flagging poor performers; defaults to 70%.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
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
    "output_file_name": {
      "description": "Excel workbook name, defaulting to 'Forecast-accuracy-<YYYY-MM-DD>.xlsx'.",
      "type": "string"
    },
    "period": {
      "description": "The period to compare, e.g. the previous 3 months (Jan-Mar 2017 for the USMF demo tenant).",
      "type": "string"
    },
    "tenant_legal_entity": {
      "description": "D365 F&SCM legal entity or demo tenant to pull forecast and sales-order data from, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `forecast_vs_actuals_agent.py` and embedded as the fenced Python below (sha256 3d9b94371d5b3ee1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `forecast_vs_actuals_agent.py` first:

```bash
python3 forecast_vs_actuals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 forecast_vs_actuals_agent.py   # or on stdin
python3 forecast_vs_actuals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Demand Forecast vs Actuals Variance — Compares demand forecast quantities to actual sales-order quantities for the same items and period, computes absolute forecast accuracy, flags items under 70%, and returns an Excel workbook; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/forecast-vs-actuals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/forecast_vs_actuals',
    "version": '3.0.3',
    "display_name": 'Demand Forecast vs Actuals Variance',
    "description": 'Compares demand forecast quantities to actual sales-order quantities for the same items and period, computes absolute forecast accuracy, flags items under 70%, and returns an Excel workbook; read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'forecast-vs-actuals',
        "upstream_url": 'https://coworkcookbook.com/recipes/forecast-vs-actuals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c3f35eb9202429c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/forecast-vs-actuals', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Demand planner role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: Workbook with poor/all/by-planner accuracy sheets.'], 'confidence': 1.0, 'deliverable': 'Workbook with poor/all/by-planner accuracy sheets.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'accuracy_threshold': 'Accuracy cutoff for flagging poor performers; defaults to 70%.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'output_file_name': "Excel workbook name, defaulting to 'Forecast-accuracy-<YYYY-MM-DD>.xlsx'.", 'period': 'The period to compare, e.g. the previous 3 months (Jan-Mar 2017 for the USMF demo tenant).', 'tenant_legal_entity': 'D365 F&SCM legal entity or demo tenant to pull forecast and sales-order data from, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Surfaces which items and which planners are consistently over- or under-forecasting so demand planning can be improved where it matters most — and inventory dollars stop pooling on the wrong SKUs.', 'expected_output': 'Workbook with poor/all/by-planner accuracy sheets.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Demand planner role', 'Cowork D365 ERP plugin enabled'], 'prompt': "For each item with a demand forecast in the previous 3 months (for the USMF demo tenant, use FY2017 — Jan-Mar 2017), compare forecasted quantity vs the sum of actual sales-order quantities for the same period. Compute the absolute forecast accuracy as 1 - |forecast - actual| / max(forecast, actual). Flag items with accuracy < 70%. Output an Excel workbook 'Forecast-accuracy-<YYYY-MM-DD>.xlsx' with: a 'Poor' sheet (accuracy < 70%, sorted ascending), an 'All' sheet, and a 'By planner' summary. Do not modify any forecast lines.", 'steps': ['Paste the prompt.', 'Review with the demand planning team and adjust forecast models on the worst items.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF Q1 2017 forecast model 'CurrentF'. Cowork found 46 items with a Q1 2017 demand forecast and matched actuals on RequestedShippingDate. Findings: 35 items (StandardSpeakerDF1 through DF35) had zero matching Q1 2017 sales orders (0% accuracy); the 11 items with sales activity all scored below 50% accuracy. Best performer: S0001 (31.2%); worst: P0001 (12,839 forecast vs 368 actual = 2.9%). Cowork also flagged four items (T0004, A0001, D0006, D0111) that had Q1 sales but no forecast - correctly excluded from accuracy math. Per the prompt, no forecast lines were modified.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Quantifies forecast accuracy at the item level and routes poor-performing items to the right planner.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Compares demand forecast quantities to actual sales-order quantities for the same items and period, computes absolute forecast accuracy, flags items under 70%, and returns an Excel workbook; read-only.', 'example_request': 'Compare my demand forecast vs actual sales orders for Jan-Mar 2017 in USMF and flag items under 70% accuracy.', 'inputs': [{'description': 'The period to compare, e.g. the previous 3 months (Jan-Mar 2017 for the USMF demo tenant).', 'name': 'period'}, {'description': 'D365 F&SCM legal entity or demo tenant to pull forecast and sales-order data from, e.g. USMF.', 'name': 'tenant/legal entity'}, {'description': 'Accuracy cutoff for flagging poor performers; defaults to 70%.', 'name': 'accuracy_threshold'}, {'description': "Excel workbook name, defaulting to 'Forecast-accuracy-<YYYY-MM-DD>.xlsx'.", 'name': 'output_file_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a demand planner wants forecast-vs-actuals accuracy for a recent period and a list of poorly forecasted items to review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Review with the demand planning team and adjust forecast models on the worst items.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ForecastVsActuals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ForecastVsActuals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'accuracy_threshold': {'description': 'Accuracy cutoff for flagging poor performers; defaults to 70%.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': "Excel workbook name, defaulting to 'Forecast-accuracy-<YYYY-MM-DD>.xlsx'.", 'type': 'string'}, 'period': {'description': 'The period to compare, e.g. the previous 3 months (Jan-Mar 2017 for the USMF demo tenant).', 'type': 'string'}, 'tenant_legal_entity': {'description': 'D365 F&SCM legal entity or demo tenant to pull forecast and sales-order data from, e.g. USMF.', 'type': 'string'}},
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
    print(ForecastVsActuals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
