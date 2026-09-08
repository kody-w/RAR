---
name: "rar-cowork-cookbook-depreciation-forecast"
description: "Calculates expected depreciation expense for the next 12 months for every active fixed asset under its current depreciation profile, returning an Excel workbook with 'By group', 'By account', and 'Detail' sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/depreciation_forecast", "rar_sha256": "2be3bba3d408e20018e12acea0bbe4fa842ea54647bc556fb764067530904a62", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/depreciation_forecast`. The original RAPP
agent is preserved byte-for-byte in `depreciation_forecast_agent.py` and in the RCI capsule.

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

Depreciation Forecast (12 months) — Calculates expected depreciation expense for the next 12 months for every active fixed asset under its current depreciation profile, returning an Excel workbook with 'By group', 'By account', and 'Detail' sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/depreciation-forecast
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `depreciation_forecast_agent.py` and embedded as the fenced Python below (sha256 2be3bba3d408e200…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `depreciation_forecast_agent.py` first:

```bash
python3 depreciation_forecast_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 depreciation_forecast_agent.py   # or on stdin
python3 depreciation_forecast_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Depreciation Forecast (12 months) — Calculates expected depreciation expense for the next 12 months for every active fixed asset under its current depreciation profile, returning an Excel workbook with 'By group', 'By account', and 'Detail' sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/depreciation-forecast
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/depreciation_forecast',
    "version": '3.0.3',
    "display_name": 'Depreciation Forecast (12 months)',
    "description": "Calculates expected depreciation expense for the next 12 months for every active fixed asset under its current depreciation profile, returning an Excel workbook with 'By group', 'By account', and 'Detail' sheets.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'depreciation-forecast',
        "upstream_url": 'https://coworkcookbook.com/recipes/depreciation-forecast',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c24a38395e3df63e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/depreciation-forecast', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Fixed assets role', 'Output matches: Workbook with three sheets.'], 'confidence': 1.0, 'deliverable': 'Workbook with three sheets.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives FP&A a defensible, asset-by-asset depreciation forecast for the budget instead of the historical-average shortcut.', 'expected_output': 'Workbook with three sheets.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Fixed assets role'], 'prompt': "For every active fixed asset, calculate the depreciation expense expected over the next 12 months under the current depreciation profile. Aggregate by asset group and by GL account. Produce an Excel workbook with a 'By group', 'By account', and 'Detail' sheet.", 'steps': ['Paste the prompt.', 'Share the workbook with FP&A.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF (forecast window 2026-05-23 to 2027-05-22). Cowork ran all four plan steps and produced 'Depreciation-forecast-2026-05-23.xlsx' with three sheets (By group, By account, Detail). Headline numbers: 35 active depreciating fixed assets across 7 asset groups, total 12-month forecast ~$911,784 (Buildings dominate at ~$734K under 200% reducing-balance). GL split: $180200 Tangible covers all groups except Patents; $180240 Intangible covers Patents. 6 Machinery assets use the Consumption method and were correctly shown as N/A in totals (depreciation depends on actual usage). No data was modified.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'A 12-month forward look at depreciation expense.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Calculates expected depreciation expense for the next 12 months for every active fixed asset under its current depreciation profile, returning an Excel workbook with 'By group', 'By account', and 'Detail' sheets.", 'example_request': 'Forecast the next 12 months of depreciation by asset group and GL account as an Excel workbook.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a 12-month forward depreciation forecast for fixed assets aggregated by asset group and GL account, e.g. for FP&A budgeting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Share the workbook with FP&A.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DepreciationForecast(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DepreciationForecast'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(DepreciationForecast().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
