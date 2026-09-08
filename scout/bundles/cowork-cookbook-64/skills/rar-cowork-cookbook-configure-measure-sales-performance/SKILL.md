---
name: "rar-cowork-cookbook-configure-measure-sales-performance"
description: "Reads an attached Excel file of measure sales performance configuration rows in Dynamics 365 F&SCM, validates each row, emits a validation workbook, and after your approval applies the changes with a before/after confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_measure_sales_performance", "rar_sha256": "b1c39decd1c168fa64cb212a29e4459a1a71c2356bd28ad0b5e78d07fb3b9779", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
