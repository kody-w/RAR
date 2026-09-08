---
name: "rar-cowork-cookbook-forecast-vs-actuals"
description: "Compares demand forecast quantities to actual sales-order quantities for the same items and period, computes absolute forecast accuracy, flags items under 70%, and returns an Excel workbook; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/forecast_vs_actuals", "rar_sha256": "3d9b94371d5b3ee154f46baff6d22255cd56f7dc4777bb9349dc5b8f567035e3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
