---
name: "rar-cowork-cookbook-configure-measure-sales-performance"
description: "Reads an attached Excel file of measure sales performance configuration rows in Dynamics 365 F&SCM, validates each row, emits a validation workbook, and after your approval applies the changes with a before/after confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_measure_sales_performance", "rar_sha256": "b1c39decd1c168fa64cb212a29e4459a1a71c2356bd28ad0b5e78d07fb3b9779", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_measure_sales_performance`. The original RAPP
agent is preserved byte-for-byte in `configure_measure_sales_performance_agent.py` and in the RCI capsule.

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

Measure sales performance Configuration Bulk Setup — Reads an attached Excel file of measure sales performance configuration rows in Dynamics 365 F&SCM, validates each row, emits a validation workbook, and after your approval applies the changes with a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-measure-sales-performance
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_workbook": {
      "description": "Excel file with one row per measure sales performance target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_measure_sales_performance_agent.py` and embedded as the fenced Python below (sha256 b1c39decd1c168fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_measure_sales_performance_agent.py` first:

```bash
python3 configure_measure_sales_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_measure_sales_performance_agent.py   # or on stdin
python3 configure_measure_sales_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure sales performance Configuration Bulk Setup — Reads an attached Excel file of measure sales performance configuration rows in Dynamics 365 F&SCM, validates each row, emits a validation workbook, and after your approval applies the changes with a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-measure-sales-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_measure_sales_performance',
    "version": '3.0.3',
    "display_name": 'Measure sales performance Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of measure sales performance configuration rows in Dynamics 365 F&SCM, validates each row, emits a validation workbook, and after your approval applies the changes with a before/after confirm',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-measure-sales-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-measure-sales-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6217eec813463910',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/measure-sales-performance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-measure-sales-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_workbook': 'Excel file with one row per measure sales performance target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for measure sales performance, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per measure sales performance target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of measure sales performance configuration rows in Dynamics 365 F&SCM, validates each row, emits a validation workbook, and after your approval applies the changes with a before/after confirm', 'example_request': 'Bulk-update measure sales performance config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Excel file with one row per measure sales performance target and the new field values.', 'name': 'configuration_workbook'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update measure sales performance configuration in D365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureMeasureSalesPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMeasureSalesPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_workbook': {'description': 'Excel file with one row per measure sales performance target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureMeasureSalesPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
