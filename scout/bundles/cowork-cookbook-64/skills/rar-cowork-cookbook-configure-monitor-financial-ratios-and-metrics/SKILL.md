---
name: "rar-cowork-cookbook-configure-monitor-financial-ratios-and-metrics"
description: "Bulk-applies financial ratio/metric monitoring configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for approval, then applies changes with a b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_monitor_financial_ratios_and_metrics", "rar_sha256": "2926d8135a055a842f2e7325cd9d622ec9c544861a753caf054360a6cf32c42c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
