---
name: "rar-cowork-cookbook-configure-process-customer-rebates"
description: "Reads an attached configuration Excel file of customer rebate targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies the changes and r"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_customer_rebates", "rar_sha256": "f7a9ffc62ef8d990118c59cbff726983c6ae11db3910298eba772e79c8487360", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
