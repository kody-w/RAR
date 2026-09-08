---
name: "rar-cowork-cookbook-bulk-update-monitor-financial-ratios-and-metrics"
description: "Applies a bulk field update to financial ratio/metric records in Dynamics 365 F&SCM (legal entity USMF, sandbox) \u2014 returns a dry-run preview workbook of before/after/status, then a confirmation workbook after approval."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_financial_ratios_and_metrics", "rar_sha256": "b5dcb164ee773f5db61f877e5bccffde772b63320387e234946a6a13a7517f7c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_monitor_financial_ratios_and_metrics`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_monitor_financial_ratios_and_metrics_agent.py` and in the RCI capsule.

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

Monitor financial ratios and metrics Bulk Field Update — Applies a bulk field update to financial ratio/metric records in Dynamics 365 F&SCM (legal entity USMF, sandbox) — returns a dry-run preview workbook of before/after/status, then a confirmation workbook after approval.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-financial-ratios-and-metrics
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
    "approval": {
      "description": "Explicit user approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to those records.",
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
    "record_ids": {
      "description": "List of record IDs of the financial ratio/metric records to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_financial_ratios_and_metrics_agent.py` and embedded as the fenced Python below (sha256 b5dcb164ee773f5d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_financial_ratios_and_metrics_agent.py` first:

```bash
python3 bulk_update_monitor_financial_ratios_and_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_financial_ratios_and_metrics_agent.py   # or on stdin
python3 bulk_update_monitor_financial_ratios_and_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor financial ratios and metrics Bulk Field Update — Applies a bulk field update to financial ratio/metric records in Dynamics 365 F&SCM (legal entity USMF, sandbox) — returns a dry-run preview workbook of before/after/status, then a confirmation workbook after approval.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-financial-ratios-and-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_financial_ratios_and_metrics',
    "version": '3.0.3',
    "display_name": 'Monitor financial ratios and metrics Bulk Field Update',
    "description": 'Applies a bulk field update to financial ratio/metric records in Dynamics 365 F&SCM (legal entity USMF, sandbox) — returns a dry-run preview workbook of before/after/status, then a confirmation workbook after approval.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-monitor-financial-ratios-and-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-financial-ratios-and-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e7bbf6bdb19f2ef5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-financial-ratios-and-metrics'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-monitor-financial-ratios-and-metrics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of record IDs of the financial ratio/metric records to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when monitor financial ratios and metrics records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to monitor financial ratios and metrics records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to financial ratio/metric records in Dynamics 365 F&SCM (legal entity USMF, sandbox) — returns a dry-run preview workbook of before/after/status, then a confirmation workbook after approval.', 'example_request': 'Bulk update these financial metric records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of record IDs of the financial ratio/metric records to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-update a list of D365 financial ratio/metric records in a sandbox with a dry-run preview and explicit approval before commit.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateMonitorFinancialRatiosAndMetrics(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorFinancialRatiosAndMetrics'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs of the financial ratio/metric records to update.', 'type': 'string'}},
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
    print(BulkUpdateMonitorFinancialRatiosAndMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebPaWLLnV2Hui5iqetjWglZ3dMQIgYQQWgAhJModLq1o3/ea+u5zBFxXVbe7Z/rN/DU4HCDpnNzzl5n36Nc3q22CvHr7/Hb2rGzBW0kSBl61sDJ3weZ9XsXgK49t8H/h5FlThXbb5FX99uHN9WqnCosmzDOwnSmKJPTqhbWw2yRe+KGXuIu2cK3GWzQ5uM6szAmtZFFZYAeUeoCUs6g8J6/cehFmi82YWWno1IsVgS+4/35mpcWPiXcHO7ysCZtxcTlL3IdFDSSz8+GnxZcWhREMUGjaKpv5utX4sWqzRVF5Xej1i1n4h9y5v7A9P688yPIbr4Lqxmra+sOiCbwM7ANq+WGVzmJlv296LF1YRVHlnZV8Avp6g5UWiVe/ff75bx/eQvD77fOvb05i1eDW2xpofXmoK+VZCEzEvWt8minXTOZKD51n0yVWdgd7ihHYPgPXhVcB+VJwy/X8xevqx9pL/A+L//zPuLeqe/3T5y/Z4vX58jb/OwFlgQ7AvFbdeO7CsQrLDhNgq08LJumtsf6DdWrAO7t/eu78nVJeLP46P/vxyeTT3Wt+/PKWAxEe9vjy9tMirwA/YFjw+9NMpfjxp09J3nvVjz/9Tqdu7chzmpkYkPrT19f1iyxY+PvS0F98Patb9sULhEBYeID4H/SbP0/RX+ReJvn6XPxjXnxYfJ/yrM9fgbzP4LQB3e+TBTYAO98+RXmY/fjiATztzT7zfvzpn5F1As+Jk7Bu/o/o/vwkHHiWC6z1MslPHx7u+9ti+dLtG81/zrYAAfPvaAKWv7P7Zqh/Rvvh2b8jnYQZSOV3X36X3Pc2LP+6+Pmf6vavNnxY+F/eNl4SdiDu7MT7vPj1ESI//+D+fvOHv/0GSP9vyZzztnIeFL6mVhb6Xt18/frzD/Xj9g9/+/mHtgBR7Fnp17ZKvkfze3Z98PmTBV+rfvzzXsD/ksVZ3meLbzm0+DUv/lv126eFbiWh+/v9+vPij5k4f5aLWYl3pk8T/CEbayDrH+z409tvAIcyoE3rPB4D/PiP/1hIoVPlde43i7OTt80COLgJU28WXgtCgLX1AzUASnpVHQLDvtaB+J89PEsMEPOX/+E84P+j84J/aMb1r09E/5o+Me7rN1j/+pCw/grQ+esT2+tfPi00wCevwjtYlSxOjKp+yaw7gPNZBgDTtVd1ALfssfE+gvT+OP+YS8Ev/y6rrw+qn4rxl0fhCp+4eGKFGRPrNvE+zdpfZ7x/6uqAWucNntMChknuAOn8EED7B2CVOk86gKmzpeo4TJKFGwLUARKMD9rAmp9nYr/88ott1cGX7Aniq8WzGNYQWPBNnMXHj0BNPwnvQfMl85wgX/zw628/LP7n4l/tehCfeaigtLx8BSTcnxV5AXKvTcGyuWQC0Lfch69+/e1lbEAmA2ULeDb052o8bwaxG3vuu+XPO+YjihOvirgAZSyvGlAZFmHzaSH4i2/yAqbzo7l2BHndLFyv8DLXy5wRULWAOt8smeUNKMtNWPvjh0Vbew+uv9iV9RAxBSBgNb8sJFYFlSpP5m6gelUusBl4F5j/W1w87wMi1Q/1Yv1O4tNCnqN1UViVVQSV9eLhW0+/gAr1vh0QtxaZ13/J5gLtzaZ6pM7TPGCRN7cdT5d+nH0Oyn8KcOLZgzTva6y5nmqPulp9yepXWliV9+hYgCjj4t6G7lws/vIKqTrIW9DyzPYDks6UXl5wX155xOCrOfj7fqh+xNYrmhdzL7HgHh3Us6V4b3b+P2+yZgMxPH/a8oy23Sy2snYyn46bW8/Zwc9udRYUsHom6e9dzzuyvQP8lywJQRRW41+eKx/ufq15gmZbAe+cmNODPog1IMxM95EKc2hX1cPaX7L3SvIBqPKATaAFwA2QV7Pd3xl+eCr6kDQA4DBf/95VvPwwexqE+6Jo7QQ4x/c817acGEhVzen8sjjIC2+2aR+ETvAnrWZPgfAD9BdAiBAkKKg2n76h+/Ppu+h/2vhsnuYtj8ayBdlcPQgAObxZwDkG+7ABoGY1z04f6Pn5QQSokRbNrLsNfJh+eN30Kq9swzpsvKergV29AuD4x/n7qel81xsKkELAWCBRihZY95FaM+qkoDUCMgB0AZGQhhloFYBRXkZ4ELTSGScADr+C8EnxcfulkPfIx7nGvW+cFZn3zG3DwgeigzvjH+FE+16YAHrpvOLB9+8j7Ru3mfYMqTWARcDx/emzv/j0bBGePcjine7nfxilfvz3pq1H0b/8OQA+L4KmKerPEPQs1O91+hMANOgpa/2o2R+fAPHxVUg/fkOJj0/o+Qi4f3xBz5/4PE3wefHvyfonEq9c+bxAPsGf4PnR4RVrrw8wDftxbX7E5qdfspP3O/wC9vkMGLMjR9AkfKuV70tAwbxXALzA4mftrOeS2wPAeRQL4JUv2R+Df04+UIuy+xysdf4HUHg0DSARnk78VtPAo6wBvN25Bb178xD4SJXae/uctUny4Q2gqffvDn9zEUvncK/n+REkFmjvmtB7XL1D4fz7z/P1dgDQ74BMmWvjN8h8IegTjOd8mkPxn2H0h/ei/zLCo57N5S9sgAln7ZqxmNV5zopzd/lAs6H5R3GUxw+A2YuNB5Azqf+YIq9SOLcCf8jkpweA5R2g8YfFbK168SiFyWyMGQWsGqQVEPG7sjzq1NdnnfpHgf5U2f5U0l79hnV/ZP9fANT4VpsAb4MHc7l7r3bfZQpaia/Azu3TPX9mOYMIeP4qw49VP9Y/zWSBe5IHY5BA9bvm9XcZfGvu/5H+FfRNMxE3/zxr8OEFwuAbDGQfFt9mK2DL17T7+DNF1qZvn3+e57o52B5b5h9gD/j6tunbH3Bs7+1v35HrKfPX0P2O4gewfy5Or5wSNvV89ejI/nUH8qiVs+O/Y4oHT1BMQEmexf/dLr9Llz9G0Fk6oE3z/IvJr2+AhwVoWq9ses0wYDnA3o/13JtBAH0AQ3D9xAnw7P96unnRqwMLdNOAoI27jo0QmOeR5MrHXZtAfIokPdx2HN93wV3UJlYrFF5RpIeuMBojLMJCVhaJI6RPOoDeE32+PjMSkMRp0odpGvUxBIVdELYo5roUQREOTqKwRdsWbuO0Zf++NQ4z96X4U9HZqt8GrQfAPPX/9c0mMLByh9UC8/yw0BKxCZS0z3t7WRFejh2ZSjzLJ99NveFc2ietVbZDlBeMlKkmyp9QJq/D86DduNJo9/mGUaetqmypUSMzQym9tZwoeKasDus1s01ixEo0HBLdM35xhyGltL2SnzcKEgYCxJ4FSC8S/8SnLcSeLlcEiS83tipQnSpu+E65k/qG7I4HUiMIHILyGEfbKTrzYnqldyRHwg1uECc3jKSgiAS34FKzHIPTBFn7bjQIA4KWPGRQKk04XXKOriI1HEeX05VJ36C0pxbLfCf2NdzTkRFp2ukWJw0fmqTl3lIrcIuG3i2Twi3oTJditNMPxflMIqI0rSYdM5RblgUcelleHJ3f43ejkOJyrOztBdmrWLkTV0t0pA+w32LqejRrg0OdTmsIT9XlrKJxD1LOZTM0ctzXfQGNIyoeb5QZcsdNJurepoP4ywWeVKpPxeNJx2O0oRQsDW9LN1vWx8E52Tx6nNj75sBEO6s8ADopCTt7heXHi8eXVC9ua2xKVDkizrZ29rTdWm7I6iA67sAnfeDGx5ZDWqFoYjVyl1258xsWkZfNmmcszWduhDEOgXi9xu6hW93ZaFwfgfO1Zr+Nx7GTEb63PHQH1G1C22QZhF9Hy3orZM2hxeVV0vpXWewdUjvJsMqVeZ3HyDpR131rXVnFbjFCnBymM9nuECdH+DZUd5+sK0uWDyKPkdKRRoqMKvKpLxvlblDNmSQMASoukCdEq8tuZRIiy8YNO6B7UyPkzpiEuLpabbsbBEqU7TMU3QQh6lVPPalTQ7PYjvKvxN3WL6Skb0wbZe/j/jRsIFnG/WMtVbXQZx50ge9wtYa5m1TytZ4frgljDzFCEGViBvCO1Y3WLeOrhC4nVxrZ6RRX9NGGgIaIHROakxLUjRdDE/KsDX06UGtgV85eU0a73Qg2l40WflWPkMg3lJ1ZnHRpM4pOmQslTZt+dT44k6md/e0pkNZHK73CvGGZF+4CvsWT5fPZqTiEqp0RrYqRp31vR5yxWxV+yy3vmu/zbj1CI3uFl5mWETYU3rwNS66uzsbybUY+FP1RLA5L+tri+i7VTlUdZG4egZh0bjCTbqjThR3dlbtriDWChJdmw+XXqMKvh80QT9fbrcBQY79Ej4jZtbm63m8Tq1yPXXzfH4JhJ1QWp60hhqI2U0XviSwrQ5u5rtjRlORIsm7i6GxuW/SWnRKU3E6xaqx1bLnqQVJrCFuKiafsnWiMdiJ9jkJfpBz2fsOPk8yc5auQpciwqRHohvPKlURlmnRrTmVHR5fPCCuPHa30jtmi18GTq2agUyrTIYwYxumAuadtYfVdhRrFtN3gKzYM6no8Tdre6ZfVugvjWy8mVGWO6y4v7p0iIlIHH2oEO++PR0nJeylVcxqvuMk/bQSUUZnuBjdB3W64ej2UkGZvKduixgJViYRmk7MXX2PPl5iYh/cwndnMcapTBwO/xgw6w+WWToqBWeWGryyzK7Rn0NtBxSjWuXS7jYo2XgJzqu7R0rA7saOM3VReqXhHjiK5d4cwFQR/R8pFr2/lmkXKGoPN7YRWVM9Ummj3Y8vsCwBGHF6JknkQ+vvEHvRcr7K9T+/q8SBh9U2XQxYHoXyJodKdDl4ICyddaoMA86OKbdBKdLPbPuNklVE0nlbq7jBQVeDA5Kiu/cIzO3+ixGQoDA9f5/hw5+8KFvYxR2c3Xt5NWRpse1HwtDMvC/JVs3IXlQ9rd9PvLtxw2NlXgSemmNYvNHRJgm3ki3IGJ3dqK/neEUuOVnlaC3DSXIKNXLUGjtLu+eTKSanTN/4eFijXOqW+lyc0TLZB3+4lVdczvbeF1FnvLCHlQ2EbK8WdFVsnkdndgK8cr6fPZ6mxeoaXfRM6W4nE+diSKnGD8XLzctmsjhRoEOiINg57pV6ug2u9CWxVS+KVlGQ8kXE7Xla7FlK1GrnVU2/hblrIe3KzlMVmm0MMXcQppoqqZu6F6ZjR2UDWFA6rLGoe3aZi+Q3cLRFDxJddPxoGRK6IsKWXtW0mtyzWlY0sTdTF3vKMUodXidk5qupHxloNT2Wjc/vjEO/2S1aiBoTTbkXvtXib63AWUujNFC75WsOyId+svYERMQe27uJouQwVxkF7OYpsUHhJLKrHPh+ZfKUJBWptD1y+EeUjsmlKPAQ1QV1qdhVVWuoIOdexeJNusl0cMMfyijeZKaVDBB8Y7+INK1Cx5QvnrHsJ6+ROK++SpwaDe5zOuxME8tqkK2zSWGbbqE0sKTof78szbu9Q02WGUSjFJXRIia3vrI8JepGyRLhyWXlM+g5yiSp1S0Y670s6EnKWW473+shL+RDse1c149jbnXhf0C1agXA75zwdX4NAJa16x56oUozWQWHcTAPuWV7cRv0Zi8XQKwP2WIg83Br7K1MVTC/zdQX8IZRQQncQMEZbbfo6JwURZvIOvim4uq5wqSsNSV+mx6N97Ok2Zg9H0hLM0D/b+X2MdAmpl9FJs3uB2ZnrnZgkmqfTHVzcTxuJOKyPfbKOIpFYNqIvZvQ9k4/3NLg2TTwhV2a9lJaZHp22hyY0JQ7ah7QyJcNW1nSHwwnxqoM2rC5tu78yTJ4pnkhcI2QdytP2xl2nPUiKo5e5rHY3b4WgE5QmSSNSQmcsi0VuQx6k4HTStvHlclma+sjoRGGM6v5MiezAX4q1hkdscJDhzBkqw1zG/sbgirWYH5dRQFlnN7yrqKiZ2YAy67MMx2lZEvSFR2gPv/LLZYZEjFGP/lpqWrTcojp7ugdj052XDUUfA9s4mVoob5PNuKr6pUIi8O0QTh7TJ1fKyixzf64OMC+0xPE6wLBVKHxxD3fn854ip6NwqZztMjudOrRILachLtetdd/opSIzFxRZB/HK2U3MVXdjCTr2+6J22q1D3vMbfmUrkbIFYwVcQWLMhR/Wu0O7R1j6fj4b59KU1jEEo/FZSqY+4lPHqPDLfV3dFC0AwitUcoZBTwtAz7MvOIwrxTXgBPEeiCYXD4nNwD5+VnMNwTQRqcYCmVoeYqEOaq+n8gL8Am/xdRYXqrRqdjY5qPSBkZqE4jViLEToEi8BvOd8czts7HS77BrQVbAQTFoU5q+NfQsTLBwedaGUmGviKBnftPTxzEGTtIJzqT5dQtLza6av7gKbX5gYcRW8OF/K4iyFlYWRXOhe96LutoeLcAp1HuHW+qU54tsKP40wprqOR0iU7lBxckXRfL9REv3M4GRVxiBWTrfcPDKmdvK2u118SPy+vzpo2Sz9RNeK6l7YESYnvIKkzc0R63FNbDS36xGawrwtMuHjrhi9mNPbcQUamjGsJhi0nUen7YOOkjSYhe54s4U1weHNsyPTDtXQZGSJqzGItw29Bs2rXOT0BIVjZpBa5OG5shLMRLLvl9yCAQATOLx2DtbNIGxmrecOWW/vdUbSUs6p8U4ShIpIq5EjQmIj+2AYGU/l9XaaAnQvClvPgRh5TadqYUSuWh5tEwFtM2tgNbOi+izgLdK8yZ4x+Lp5ZVkrP7g2UkEbjl93PNlceDT1V+hKnWLiVIs9rfpK7BMHCVUC6eBSt5RuT7zgXERoq8Xd0QUNhF7m/IYSbG+50stGcigsmIrcsvg7pywZf88q0NWkQLsEFXsVlQw7LDtl29/5jAReyo7LYMsI6XGj5gOYP00M3fnynsjhTk5tNs46aFCDmgkgTm7bPtayoLndLpGJ1tMdc6a9F1ewb+5BI+kEmXI86zotrwz2TkHyFoWTfoWnwm1f4iwS6Cuqm5ALlCUjpWQQ0ofndh1QJ1LM2jG4ZEddATFVnMNjrK38qLMcqQ/wQL2O997ZGlKjJTbSOeRSRIctkeGpuSVJkxnR7ExH0XUFJl9ySWpSvNcSRGnuzoqWl7p2mMaI81kHWvErTMv2eYbrlyOfUwQsXI6NXCaTLDNocoWEUTzRjJ+npiBddglsKVkeECeJSE9TLLYSBCSrisSM9+aOFLFoIAZl0C7d2BypCtlxMbFUyqHkUnJT96qJI0fPk4KsR45sbxooe+FxmY8tXKEYMUsvkjFchLPoowdjalOq2+krLagtFYx+iH2Up5VD6a3g7O4WlawnP16l17xYpu0k+v5G7IxgS29Kb1nZnd+vSNLW3KizV95AAyxpzqG86Q81F3C7tN0hzg4CjR297oRt0a1rdrMdalKwhwk3FNnq0YQWSQFKfIEuNC4Xy5LHGoet1rpRZM2FFrVxak6lrZ2gzhhLX7JKBK6uS1CMlqzVpMWlle373WYqEychcxh3U8UznApDxUlxRIi7FplqTctTpLmEmq+Og7fD/cyfRKS9UN3+HhC2jt4t0ao86oiBdojLI5zAiRt2TyiywKR9xFpqBJneXkil6IA7tHA4rExjKG1Q/kErXLT32jvfe6WU+ZJIGWx/2O4UoYb3eKZUUN8pwZYAxcmIj5ZCpFeB2AtkZBzWFebyMZGdTWxF69lygL3UbLMlhDapYFU3N0VRA3NYYndHlSa9NVeMsjyO8w+aDDJp6ZGTq+YjZB9OhpsS47iSyN1QRa16RnkiKviVVoclTR/93FS7ZGO0GoPvLqKY17CgsFzN0RoldOhwOK0KhlT3yGSsGHjptb0BJtublmRjW9NgwgVDPpTpm1sNV3quJDa+9UtM4M6phBcHXCUgZrotLyddu7X7OoTt89U7O11bkDfM45KODqilnhua0XmrYZep/a47BF54xaqiRm8Neb1wcrjko7qp1tJFvMjHpbK2bB+izzQ0ZEsE9nlF4/QlFHeUPbIrViPS0MCRyMgje2SwwGKqzvIupnc2ayvCd1tcIMz6Iqp9s7pc1zCaUudVRQYiJkb5GQuX2yhej1o6dQrKgmoa2xFSnfK9pmbrsbxmHORtohzkP1fcoXzPFjrNO5g97fh+79jx5qoo1EQD7xNx7RL7MW9sKWBLxzlArl1VVdCToadOWHBTellu076/IZs+texJjDmMuty8g9qmtltB8LVYga60bvnOjkOrgF32jl8jWjx3CE6fVdthuEG5J7uYGYRYG7ClCE9kXShDBMZrZnNBklKt+UMp42KNbqTKONXNoSc4sVVq9j7Sx6tESpVI75AscZGIF44SlLjJdMO2IbQ7JOLuutnZ/FkWE+HM9vyJsKCiUNNa6mFWPUumUZ0qq2lFbou6rIIvnc2FcVMnMwlJNJjl5hpoxmSi0X7V+9p4AuNQs2P2mTaWo5PgmpMmguon0dK5GMZqlbQlTmHHPMbamzkcHPTGU86q0LQjMZXhCZ+kg7/piX0l1gMEE1wdKmWaXW2qMKQzzGwjYxivDhHyZEjqxwbenmp83VN6XBxkUxbQsc0HJFb2KeOMVXbmLQURD8eV5Da8PsJ4vrJFKw42YUSDaovfheMqh8m+zUtKAZM16odjlDYVdphgj6XgJKAHxk8ziYAvxorVL0i+25XI1cK5ywBJDWEIknzEgtTEgJNvXncdB6pvGI4bANDQOAa7fX8QdjTqw+P9pl80HqO2dJQJedlJMbKmpfZ8rFYS45lyhdy0Ww3xa2uJHsZuX107zkXxaSBhJEDIreLtYLJxWvIIWS0YDCmV7KDJOR6RFrrX9xAix2I3mBR5Q7OyO5ResRyX25Ts0LDYN8taWiuZDLegjZbh9UTYBEYVfq9QwsXK92JTj4nlqagn0vruvOcTC0O0lomUYNMqxujLIlm6I2nsKDQi1asX9dAo35Xh6BTpbYOsy8C/tsPO2OT702i7KbJD8lO3U5PBMZlLmzjxuOQtTgC6bYVjkCUYfhTMHorDBEbUeAVGQR2PA+Pkh/mQAxPp18HaFeou28bQOr7yk7tRwxhdna8jAaNiM+nmLT+IeKSZZrSHGs4ZOEpS6YaR7zuxc0WyZU3tcjA3tV0zqmzsSUk1+50U5w505fucrqA6iP0QsppQhFbqZYKjG5ossSXcmWO82Xeg0UcssxAoz0ItvSuiTMZNQm94UkGmgNJy/HztT8B90njytaS+lchau0m3CKqvpzvZ0vsYxYmkW7IgPLyatuJac2+yi5S+Lgq9JUWpBUW3cbWyw3RA9l7WcWYcQOmdLREVtOXrSVu6aLb3vWNeiva1yS9ZIa+CYuIVo9c8ZxKHyiGSfiRo46iO0Ripq2u0xQTcT4zDcUm6y77sKYcqJLqOlVAYBfcmFGCCXq8G9iYzGFMlEDR22WnK3VzHToZjUczNOCDhTuxtyz6vDAUMRp7dXp10reKltIlKtMTJNrtnl068utiG2zWKvsyiVKTW8R4JMNM6Cddim8BqZGXqEvZG8mD1Ru2n67PdtRenqVbLPZ4qm9VeiBuNUbjxNspVJhmEsEUR1FUdsYt49czct1zrmQGz56IsZULQTa5XbM8oqxNIWVazm31nOCGDoN32xJ3ojevfrQm7TlXTIUxXDoWo3swyILg1tSs7r6YOro7sHIBZmUq0zdl1jVvH3vAIwi1uJFtqeYFSoTZ13+zWzbhsZJ7EuJ3jM8E9rdPITlHDAEiw43TZWl01MiO0o+FClCLl1R7aTHSJa5ViyUexW0/twWv1FkPyllWovkI2kHRHqhhb3k7KdMoxCZ7WQ85Vq1XTxvyqukLT0Bin5RG7O9R0OMZszpMJPAVyzJQCJsblvemxzrI10Jka7gWlLOLKZZtQ8RBpuYV3NnuNI+4EUyp7989n0Ybt1FgdeIoQ1p6PKmhkrBGIwKH6htX0OvJXG7V1hYa0TpgqZu5RSaoI+DtxOF/wmYg9eER8WV8G8njPcXfdO3pkqOy0hDL1DmMb525JGORsMXp7taP1QZXgKupWd9d3TnRAchVjyWAATDEyi3q/l7YutGZPDMO8fXibD7FfR9H/5Vfn5lOk/2eHWc9zp/c3Xx7HkZ7lfn7w+vxfF/FvH94qJwQCPg/06qS9v467/u447+O/++LDTG18vq32fuT9POFvrPv8xvdbmLktaKvGr3WePN6LATvstp7fC63nV4cd8P3H89Y/KPn27TS1yb8+36p7m1/cnN948dzwuWK+vL9OPD+8ua/T7K8rAv/qVcWs+etdCqDw6hP8afX22/8CnSr2WL0vAAA= -->
