---
name: "rar-cowork-cookbook-configure-monitor-financial-ratios-and-metrics"
description: "Bulk-applies financial ratio/metric monitoring configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for approval, then applies changes with a b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_monitor_financial_ratios_and_metrics", "rar_sha256": "2926d8135a055a842f2e7325cd9d622ec9c544861a753caf054360a6cf32c42c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_monitor_financial_ratios_and_metrics`. The original RAPP
agent is preserved byte-for-byte in `configure_monitor_financial_ratios_and_metrics_agent.py` and in the RCI capsule.

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

Monitor financial ratios and metrics Configuration Bulk Setup — Bulk-applies financial ratio/metric monitoring configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for approval, then applies changes with a b

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-monitor-financial-ratios-and-metrics
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
      "description": "Explicit user approval after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per monitor financial ratios and metrics target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_monitor_financial_ratios_and_metrics_agent.py` and embedded as the fenced Python below (sha256 2926d8135a055a84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_monitor_financial_ratios_and_metrics_agent.py` first:

```bash
python3 configure_monitor_financial_ratios_and_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_monitor_financial_ratios_and_metrics_agent.py   # or on stdin
python3 configure_monitor_financial_ratios_and_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor financial ratios and metrics Configuration Bulk Setup — Bulk-applies financial ratio/metric monitoring configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for approval, then applies changes with a b

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-monitor-financial-ratios-and-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_monitor_financial_ratios_and_metrics',
    "version": '3.0.3',
    "display_name": 'Monitor financial ratios and metrics Configuration Bulk Setup',
    "description": 'Bulk-applies financial ratio/metric monitoring configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for approval, then applies changes with a b',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-monitor-financial-ratios-and-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-monitor-financial-ratios-and-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0ede97d4cf11a728',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-financial-ratios-and-metrics'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-monitor-financial-ratios-and-metrics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Attached Excel file with one row per monitor financial ratios and metrics target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for monitor financial ratios and metrics, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per monitor financial ratios and metrics target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies financial ratio/metric monitoring configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for approval, then applies changes with a b', 'example_request': 'Bulk-update our financial ratio monitoring config in USMF sandbox from this Excel file — validate first and show me before applying.', 'inputs': [{'description': 'Attached Excel file with one row per monitor financial ratios and metrics target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF); sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-update monitor financial ratios and metrics config in D365 from a spreadsheet, with row validation, approval gate, and before/after output.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureMonitorFinancialRatiosAndMetrics(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMonitorFinancialRatiosAndMetrics'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per monitor financial ratios and metrics target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureMonitorFinancialRatiosAndMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
