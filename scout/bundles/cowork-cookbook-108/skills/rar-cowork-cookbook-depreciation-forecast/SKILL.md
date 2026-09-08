---
name: "rar-cowork-cookbook-depreciation-forecast"
description: "Calculates expected depreciation expense for the next 12 months for every active fixed asset under its current depreciation profile, returning an Excel workbook with 'By group', 'By account', and 'Detail' sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/depreciation_forecast", "rar_sha256": "2be3bba3d408e20018e12acea0bbe4fa842ea54647bc556fb764067530904a62", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
