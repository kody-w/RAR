---
name: "rar-cowork-cookbook-configure-process-customer-rebates"
description: "Reads an attached configuration Excel file of customer rebate targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies the changes and r"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_customer_rebates", "rar_sha256": "f7a9ffc62ef8d990118c59cbff726983c6ae11db3910298eba772e79c8487360", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_process_customer_rebates`. The original RAPP
agent is preserved byte-for-byte in `configure_process_customer_rebates_agent.py` and in the RCI capsule.

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

Process customer rebates Configuration Bulk Setup — Reads an attached configuration Excel file of customer rebate targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies the changes and r

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-customer-rebates
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per customer rebate target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF, sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_process_customer_rebates_agent.py` and embedded as the fenced Python below (sha256 f7a9ffc62ef8d990…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_process_customer_rebates_agent.py` first:

```bash
python3 configure_process_customer_rebates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_process_customer_rebates_agent.py   # or on stdin
python3 configure_process_customer_rebates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer rebates Configuration Bulk Setup — Reads an attached configuration Excel file of customer rebate targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies the changes and r

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-customer-rebates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_process_customer_rebates',
    "version": '3.0.3',
    "display_name": 'Process customer rebates Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of customer rebate targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies the changes and r',
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
        "upstream_slug": 'configure-process-customer-rebates',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-process-customer-rebates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '500d98a0121605c8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-rebates'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-process-customer-rebates', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per customer rebate target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF, sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for process customer rebates, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per process customer rebates target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of customer rebate targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies the changes and r', 'example_request': 'Bulk-update customer rebates in USMF sandbox from this Excel file - validate first and show me before I approve.', 'inputs': [{'description': 'Attached Excel file with one row per customer rebate target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against; defaults to USMF, sandbox first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update customer rebate configuration in D365 from a spreadsheet, with dry-run validation and approval before any data is written.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureProcessCustomerRebates(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureProcessCustomerRebates'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per customer rebate target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF, sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureProcessCustomerRebates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
