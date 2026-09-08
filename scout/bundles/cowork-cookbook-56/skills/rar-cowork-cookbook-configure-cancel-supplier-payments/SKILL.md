---
name: "rar-cowork-cookbook-configure-cancel-supplier-payments"
description: "Reads an attached configuration Excel file of cancel-supplier-payment rows in Dynamics 365 F&SCM (legal entity USMF), validates each row, returns a validation workbook, and after your approval applies the changes with a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_cancel_supplier_payments", "rar_sha256": "35998cf927bb2400e41536eb7293481818771d13a9fa3b49216b3544a6c578f8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_cancel_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `configure_cancel_supplier_payments_agent.py` and in the RCI capsule.

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

Cancel supplier payments Configuration Bulk Setup — Reads an attached configuration Excel file of cancel-supplier-payment rows in Dynamics 365 F&SCM (legal entity USMF), validates each row, returns a validation workbook, and after your approval applies the changes with a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-cancel-supplier-payments
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
      "description": "Explicit go-ahead after reviewing the validation workbook, required before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per cancel-supplier-payment target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_cancel_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 35998cf927bb2400…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_cancel_supplier_payments_agent.py` first:

```bash
python3 configure_cancel_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_cancel_supplier_payments_agent.py   # or on stdin
python3 configure_cancel_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cancel supplier payments Configuration Bulk Setup — Reads an attached configuration Excel file of cancel-supplier-payment rows in Dynamics 365 F&SCM (legal entity USMF), validates each row, returns a validation workbook, and after your approval applies the changes with a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-cancel-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_cancel_supplier_payments',
    "version": '3.0.3',
    "display_name": 'Cancel supplier payments Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of cancel-supplier-payment rows in Dynamics 365 F&SCM (legal entity USMF), validates each row, returns a validation workbook, and after your approval applies the changes with a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-cancel-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-cancel-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7ad2c38308f683e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/cancel-supplier-payments'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-cancel-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, required before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per cancel-supplier-payment target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for cancel supplier payments, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per cancel supplier payments target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of cancel-supplier-payment rows in Dynamics 365 F&SCM (legal entity USMF), validates each row, returns a validation workbook, and after your approval applies the changes with a', 'example_request': "Here's my cancel supplier payments sheet — validate it against USMF sandbox and show me what would fail before applying.", 'inputs': [{'description': 'Attached Excel file with one row per cancel-supplier-payment target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, required before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-cancel supplier payments in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any data is written.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureCancelSupplierPayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureCancelSupplierPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, required before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per cancel-supplier-payment target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureCancelSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916edOb5pbnV9G8XTVJWrYBCSThrls17AIJhEAgIL7lsIPYd0Hmfvd5kPQ6zk3S3Xdq/hpctlie5+znd84x/Ppmd21U1G+f31TfzhecnaZx5NcLO/cWVDEUdQJ+isQBfxdukbd17HRtUTdvH948v3HruGzjIgfbFd/2GrBtYbet7Ua+Ny8P4rCr7XnFgrm7froI4tRfFMHCtXNw+bHpyjKN/fpjaY+Zn7eLuhiaRZwv6DG3s9htFusNtmD/p0qJix9TP7TTBVgVt+NCU0X2pw+L3k5jz279ZuEDpvP2D4vab7s6B7K8P53Zz5rMSnx4aGYHLdBxLDqgaFnWBVg4nwBRmkUb+Qs3svMQnA9xGy1soKt/t7My9Zu3zz///cNbDM7fPv/65qZ2A269US9NfeqhlvrSSn4qNdsqBfTAwnIExs7BdenXQVFn4JbnB4vX1Y+NnwYfFv/+78lg12Hz0+cv+eJ1fHmb/yhd/hCvLeymnS1sl7YTp8AenxZEOthj853yDfBVHn567vyNUlEu/jY/+/HJ5FPotz9+eSuACA9DfXn7aVHUgF/dzeefZirljz99SovBr3/86Tc6TefcfLediQGpP319Xb/IgoW/LY2DxVdVZqgXr9p349IHxL/Tbz6eor/IvUzy9bn4x6L8sPhzyrM+fwPyPqPRAXT/nCywAdj59ulWxPmPLx7A8X4+u+zHn/6KLIhkN0njpv1v0f35STgCuQCs9TIJCNPZBX9fLF+6faP512xLEDD/iiZg+Tu7b4b6K9oPz/4T6TTOQbi/+/JPyf3ZhuXfFj//pW7/2YYPi+DLG+2ncQ/izkn9z4tfHyHy8w/ebzd/+Ps/AOn/kowK0th9UPia2Xkc+E379evPPzSP2z/8/ecfuhJEsW9nX7s6/TOaf2bXB5/fWfC16sff7wX8tTzJiyFffMuhxa9F+T/qf3xa6DP+/Ha/+bz4PhPnY7mYlXhn+jTBd9nYAFm/s+NPb/8A4JMDbTr38Rjgx7/920KM3bpoiqBdqG7RARDtAEZm/iz8JYoBnj5BrfaBXZsYGPa1DsT/7OFZYgDJv/wv94H3H90X3kPvAO5/fcL113e4/vqC6+aXT4sLoFzUcRjnAEMVQpa/5HY4QzngWtZ+49c9QCpnbP2PIKE/ziczwP/yXxP/+qDzqRx/eWB2/MQ+heJn3Gu61P80a3iN/PylDyC08O++2wEWaeHaz3LTzBWhKdIe4OZsjSaJ03ThxQBZQCEbH7SBxT7PxH755RfHbqIv+ROo14tnhWsgsOCbOIuPH4FiQRqHUfsl992oWPzw6z9+WPzvxX+260F85iGDmvHyB5BQUE/SAuRX91B5MTsXgMfDH7/+42VeQCYH5Qp4Lw7eKxSIz8T33m2t7omPK2yzcHxgY2DfrCzqFqD/Im4/Lfhg8U1ewHR+NNeHqGjaheeXfu75uTsCqjZQ55sl86JdNCAIm2D8sOga/8H1F6e2HyJmINHt9peFSMmgGhUp+GcW81k87bzIY2D+b5HwvA+I1D80C/KdxKeFNEfkorRru4xq+8UjsJ9+AVXofTsgbi9yf/iSz5XXn031SI+necAiYBn35dKPjxbDLTKABV7zzvuxxp5r5uVRO+svefMKfbueXeGCUgCYhh1oGEA4/scrpJqo6FLvYT8g6Uzp5QXv5ZVHDD7L/uI9ghfvEbygftcCkV2aLFQAI+XiS7eCEXTx/3HTNNuF4DiF4YgLQy8Y6aKYT3/NbeQs9rPznOUCQfvMzd8amnfQesfuL3kag+Crx/94rnzY5LXmiYcASjwAQMqDPggxIOtM95EBc0TX9SwokOu9SHyYlZ0REWgK4AKk0xzF7wznp++SRgAT5uvfGoZHxNTebBcQ5Yuyc1IQgYHve47tJkCqes7il5dBOjz8N0QxMPf3Ws2OAVEH6C+AEDGIGFBIPn0D7ufTd9F/t/HZF81bHj1jB5K4fhAAcvizgLPHZk8A8dpn1w70/PwgAtTIynbW3QF+Bpo+b/q1X3VxE7czZD7t6pcAsD/Ov09N57v+vQSZA4wF8qPsgHUfGTWDTQa6HiADABUQKFmcgy4AGOVlhAdBO5vhAcDvK9yeFB+3Xwr5jzScy9f7xlmRec/cESwCIDq4M36PIpc/CxNAL5tXPPj+c6R94zbTnpG0AWgIOL4/fbYOn57V/9leLN7pfv7DWPTjvzY5Peq59vsA+LyI2rZsPkPQswa/l+BPAMegp6zNb+X4418AQfM7yk+lPy/+Nel+R+KVHZ8XyCf4Ezw/Or6i63UAY1AfSfMjOj/9kiv+bzgL2BcZCK/ZdSOo/9+K4vsSUBnDGqATWPwsks1cWwdQzh9VAfjhS/59uM/p9oKYD8BD38HAozsAof9027fiBR7lLeDtzf1k6H+ax7BZ/MZ/+5x3afrhDcCl/98a3+YSlc1R3cxjH8gf0KC1sf+4esfC+fz3IzFzB3RckBBh8dGeZ4IXhIJGLPaHOWMeBeXP8PaRijOgvSr6O7bOxeqJud6sTzuWswLPUW9uDn9XPr76c/n4Otvoj8IR7xXnuxrzQO4ZrEBJmIfSv6w4LehY/PZh+FkFUJoBAR8USqBM5zd/JVrr39s/SnJ6nNjppwXtA+BOm+8z9FWA5wbkOyB5hgMIAxd44sPiWcxA8gItZifNIGQ3IKuB7f5UFj/v47rIZ13+KM/lqdx3a95ZN0Bhp7gDNjXonV6uAd73nu34n7J6FOCvzwL8R170XKp/V6NfjZQdPvDtPwCYBnaXgugGD+b6/adMvg0Mf+RwBX3avNcrPs+EP7zQH/yCIe/D4tu8Bqz4mqBnDn7eZW+ff55nxTn8H1vmE7AH/Hzb9O1/gRz/7e9/kAsI9h7HM63fhPxtafGYMWcVAOn2+V8iv76BVLOBT+1Xsr2GFLAcIPDHZm7MIIBIgDm4fmIHePZ/Mb68KDSRDZpnQGKN4fjODfDV1nFWKAz7KIKtN76zXeFrdIeAP9st4iFrGw/stYPiK2TjrDEUtTcutt0FO0DviUFf5/4znqWaRQLG+AhgzP/tMbjlvdR5ij/b6tu09ECV8BWbzgYFK/dowxPPg4KWiOOjkHOvDcjA8HgMBSOpuj2HL1ehcccZo8Pxm3E+8a1XwtzAXuPDnskupRZz53XRHkmniJZhvqWCcouNFqr12rYtSzj0OpQjUrdzxCyQUWAzURZ3Tk4owoE7ReM4HlP3zrLdfS3GGXwCNFuv0nydKiSS6cc+OhhiHE/iJYB6wXDVDa3yTchorEKe2KsSCw19gXCVuRiH0owNszsjWLyRbGtFW1yOIFWhHCdX2LGnSC92y2Dd3w891N1u2LW4x90ZjDA6V634tj9usaVkbXga5pqios7XJGzUVsz50JP9s+Cv2daGbrVUI1bp3zQyxhgeCbVVm0BHg1CstHJNlYSIOHJYvSgHbjw7wRG73nWTCXf7CdlA8gXZQcE62GjluAyMYAlp465A2FKL6MtZTxsYG9Fr5WJY3EnQ1SDVxoAvZKZatg142Nuzfb/6Ft3nWEUeSWJLEvKBOd5prwvkCUt3BckPaqbooiL1VESf3CU/cqeRUg6r9BjbsGal9Sq7ulHqm4Z90d3+ct05iYQL9hJGrfQcVUQt8vANDjNiGnp9yxzuen2wySujLwmBpY5Xp+Sz+hjUtXkwM6iJIl/ZFvGaCPmDVUqB4NAkqmybaXuf5PqamtfrVRWaCJUVNmWazC1RkVXtUcmT25K4R1qdmmll7ElJpKFj3Bbw2BQs0sD0SuuCcdT1muJi65pPB7uGrMtyFzllEYzm6FBEIh3GkSl4XIftDcOn3JY58p2wV8gj1+gnYehOZ28HMWEEw/tGvTcbnMQ9pVPMQ9SfSTqJXQWazssrs6ftLSUKIDz4wjsMHn3KWNo4JGStDBI62pinq42y0cNUR8pG20zZOqtNdwwjf2S65UEadDIYjIAnICa3aPdSnBvBMFARak0jjK/CmhISiZq2Eq6EcL9C6oDiVoq1L+/G4O+ay3kqO3ZzxTpO0qdoYEe/udw86zSsApIKyLK/nOsrozhxu5X3zc5Dd7BXXwITok5CsuyO240B3TCfdJ344h5Gsh6kY0m3FsO13RHRt4XIelbhe11M4o10S84UL9+TSxxYRo8SCHbTrCNUcLmDsdpVUa3zRZQt+9ImGGw5Ea8I1zCWdDgjS1Ax3Aj46Sxq9HoKOgdUtVUQWwnl7OjL4CkeSi336fkAl80k72/1SvDPUJPuwy0kloXVlZq26WlpWQ/5pdyV6CYSrgyr6ipIM0VeyxK/UYcTXmMOWp5oRdN5LswdJdjQAxo4jcN2q27MV47vGMPZuXmZccZ0RlDv7XbZwFYaupdGGfRrzVAVgu9IOT5O8HRmsuDQGBd2JWFByalIl5FqeLtbh3NI9R5uDopsjGJ9USAV564+bfkAIuibtMqW5QQjWHp2ISTkWOKIE7cqFjWKM6w8jJWeiAXkuHX7hFgh7VVJ90LEnJOIUEsw4+urS7FDrqF+jXfA/XQwrk9VFq6YJd5Wsngjg8TYrphBY1QfM0uxiVoIPUjyypSjG+aYdH1G/ZtCuciWJlnbvGSchyo6T47FSmL9NI5PhyDlOqQxxGUcHjl3cPJJu2oMw+c1dFSnrFwjWVqJIV911/Wwk+5psERo28stId9LMnFqOOzk9se7p987murXvHHrcbk1AiPmN+wqJHRKxF2EzBmh4O+7PT6t+9i07GrCWp5wQ9w6bqIMhU22OIVOngthvK2J4urmfGzkQ9/wobm5rs4cOshFSApxwRGnQrSy7RDevBju8+3kZNYoW03MKbeYNB1buFUXJ8PopXnPTiWSlEkl0KWNiBoIRE1dnSG2G9aRtUrPNF+s2y7BowlONHUrUme2jHG80/jUVLZUs8/ylCDB3GDvexOWTa7C3BqpeQ7h4AZuEBnA1GDsjNJOtuXUj7IDY6c1snGZ9paISXe/bOgDhjAplxiDqK3V9Zlj93HD9KE3SevtKhyceH1xmoKHc4ullT16LGKIFlJ45wfbfAlZnlwetfq0y+pGSEETMZlhSOYJtcZkJ8JYV7GZqqpwvWKt8wAb5J1yiQHRA6cMNx3r840LivHK0hhlHINThFsDEeiDDl9vh1r1iWqVR5KZMSwp7mRR86O7StP7UKQQdXfjCf+24oZmiphTWIYuIoYTKapQmMi2LHr5VrMtgDZHYMXdVUBt/hL709Ysl4o1GbHuG9lVJ5uNfnUy0wvJIipiJg2qS5zRHiyeV2G2PsPYVISRctzHgSFUpnYJo32EicOdovNdohE3WxkpIRDEHbd3+rTPW4UczwdaOkjnQVnKVa5p1KmHpIvCaMFqbHFC3HfiEBVXh4ywLG/4VVLKaHPcG+NZzlcbZ4mqDRpwUSKd6P0Qqixb7Uv4FhuHDs+6LrJIg02UK45fDcWkEo7O1v5BHw3tTi95l6xI/KizSBIrolapG7GGq9DWVItn7ocR1YSNHK37M3xg3J4qPIxLnBOVHDFO6Jy7jcWaT8lxwUxUbWv7LTwo5iTqPHKFDmLJl9djl9Q21vGkzIokrd3Xjt1jm2xnirVIaEeOKEUfUzGdNPCxsVhB6eo4Gptjbsu65LGoAJ2ERqct5thODl2dLqzq7424sLMNKkwG6OpMi1HbtidNgoopDKvHlL3cL6p6qNjV1SoMNNRwP8FkMjqewgu98pRKb4zRYSsohDy2zCtJNOGSYwJQVsyrl+jDcQ271s0TUosvd2paZGYRmGqI3usmUINJSZRYOmM4FQyY1/Ghjd7wWBMV1ECWNTfCFw1R1lVnLzs4C6He2kzhHp5kOnDyIs+HxB6pk+KeDLzfbg4HAH704bBTNZnvJyDn8QZPa7ZZRhbvobgIn529YYSghgu0I0xKlcH2quE9ga96XiAilRycTX7gtKSZ1FuvxcXtzNj4hSmorFNdMZPvzcAi5x1diG5nN/QVa1NtzxKUvSaho8SV9b44bE4EBEJHqKFwHxq6vIt7/mprl2l/se+nu9EfVFsY/XzIaE4KN6crwqDb3X089wdnTcUsbmSOsARD/y5EQCMSXg1Wpy4XSGD887ofMrY20qNVdxxEQT20tJTquifZJr8R68o77mRnjQsl07s4ZYvBfdIPXBUuVboUDpR3XGsJ0a0NDJ2o9Gp5gqYfzql13XYb4s4nqSrczmRpOPo9rDeq4DCMvwVlxCO1eusHML8Rsoqo7qodkGlZ4mV9kbCzm9a7zLf3He45RLv2SYfJDoWNYKdgSgBYShl2TShCZIWtIIa2nOd1a/W67DVXT2kVmuma0/LWOhuBIgc6FlPGKE6EQrEZUbZOLvDDtWsc56YxO9DbSscUbzYcBx0d5kKdRd2BZIQP+AyW+GAUxHSgN2R5OicHizNtqpekhDii2kHv9PJcTYrb7UQPXeUXNqPXurFh9PP5bk1FwS8LjLwd02OkmIYo8c3Vh5elz5M3kgzpcM20IH4Jhxf2Gs7zG246HVa7LXn1A9e/0Vd4VSybPavV59N1L7VsvTcrVEUmeZA4N7l6uowRsKL754yCi9o6dcj+tuUpGsH2GcyojOUyuL5b5yQ+TJgVaqTR+6Ru9rahE1d3xA11PdHTOTqfhvYo8k7nNepIB/4OhmAt8uXY1LbFtN861Sk2t/pOaB0/3GyPXOydO2NT51q31rNebEYzpcGEWXGjU/ZdLaoMgbo6fcpNMCjuWXpabcu1VxhOby95to8nyLqXSNtFEruBR0Y2ulXKqTLDh3IxVFXGmyusPGttv9oH9hjRRyo+mBo4MlM9mjI8RTdkUHThyOtUiNYcdQlNIYR5K3BuuCsKTsXsajohdyuJz092461oMyGKYYCpwNSJC251PAtaM3ePMZtRS7wswneqaHeH6cYV57LdErcYpD1lBK2/d2LJbKTJP2/Hy3YNRph2Bfl9bZbNTt+XZAqmy5rceD5MX2WX8imfJPtRGiPVkAiAzViGMpupwM7Y+nqPxysMu2nU1ZWwhAdUn8YosrcJAuy13a2uqxjfOAKNhOaYhFcMQ6aCE0tc852yScsknwi0pAhIOFOUcxwJu1NQ3NdPFTEK8LLOT2hNEynsnjm1MgMsaMrCEEBVgn35euwPm3Ad28VR0WUCTKhNHPNL9UpC7m5ZQgnZYrBbFugRQDyE1DJ68hKmvXi+LKXXnI1wzWQvZ7aGj6wd9YO7PaSnuAhUHrs4knpZ79Y1u3XgvTk5x0sXQVBZG81BFJku3ujygRIs3dtChLo8Vz60uo+s6Gw0mPcATkUZHekep588Zs2Z9C0iTJdgK4ZXogIV+S1XVGGgV/DGKKqTkF82cSFy7co9b8ZThpre8bbJCTVrdLPeL6sbdJfGo+Nx4rqvr0veUIWzd0D0ZZD0A+GrugsAGG4YNveZMCcmjCcwiybxbDiG1h2OzfRASrd7UXZ631qVWYa0KhC33tnuziZ9T0/mqm+UJG/lXA01JakYQbiRsm6HgkLIqDhcs9U5kPpNZMqHosKCozwMRo9BPJ2o6l7FliFn1dFuf1g1SlnfSoPYDCjA5JG/U0lQLIGfb5dMTU/OCW9O1mBVSKTT3t3hAm4HBlY8FU5pOu7vOpYysh7plWdIy9Nlg6NX7SCn8Gpa0yc8ci4hioT+xjbAYCeya8Xo1aCFsZ5D/TpdroxxsxWRLkeslXAzAs/X72t4DavrSyHUEnYRUee00+VrfXGxPcOU/W44unfartotxKl0miV+ttqpfqD5JLTr9+V6u3QIKAyFVdCNAegQV9tLQMk0p+HxWttQwbIYpHHS2mu0SfvsBJfVmSIPLKzgWonXRVP58aGsSTO389JoK0HdTktk7enZbhswjQVJu8Gm7bPks9wk9fY9rERjgPPaICaVPHEb0LHg/RrC2wACvYkZ97cbNbGBvFovJZ9wo45y6ADaRDVXRd35UuwLtUPLWokwLx5Uvdhd9L4MZSGESis59C4qEHJzP5PIgbvnsTgMQeirZi9O0/0mq9Zk2u3GLlsrw04sda/OgbiC97mpthyjR1RxtYK0Fzn3fh/jy36K0rW/xHYJe/GzAV8Kk9s66aploWWLgGPrRMJ+42vtnrfz9cW0mopELpKApqos+JTZpeu12i7dU9nl9VHxPNfjBmuHM6Ut0aO33xziPJ02TdCgsEUUd7GImIRA+IS+Y8sNuto2N/nGrfiY56K61jxTvIAhQXeazLp2tWUbEcwjKDYcjkeENKc2s/YNZJVGYJKZTMsTM7EYqkKM4zr5KjreyFsaCUmqJCo17JWNHcBXdhfxZ57c15xII8jpLq5TCnO6pnZpbl+FzPakacGVpeOarFVhPZmrm7AeEE28xVfZOZ0vp/ympFsLUeIsFeSgnZbB7c4ikGjd5ClUG+VusM7Ohq/N5HXBOesj5KZXt3VmHsUTveu66kJDF9MbC/vgRHh9T/HtlDDoZqnb8Ekh680JU4+iLtknzZXSSQRuvI4bS9GjQKXzoy/zCtY60t6H8ca/xl24tUQnraeoQeBUIXP8wEwDuzkPdXtXkMgjL+gu9xHR2Dc5fkHWciW5OlnV070mc8m3pKqSV1Uh3LzTWmo6xD4VDpHBpRgOyNQAtWLMidINvqXZiYRJbesRLZ7ot/uWIHZNYNGb9KBEV2VnRMNtI7pxV0pMk8ltjo4HfCL27YBwm2AfrvL2ivtHG8hatitvh4+p3XJ3GpJ3LlcZLgp15ZhmRgTtQPGTVRuMw1FzWEpL17hAaXTMWnxZj3l9g9q6x3mTCyX6vL7aG9/z03uE0hmc6Shjj0U0YGJxHuz2eMa1Vene/CVSJTJTSQfknmqEogYX2XEJoVgHvKEsTwYB39ZHo7ih+HhsxDuhlSm2R8hD6l9POGfQLq9k2lKy5e4MeqBgu9oNRA0q9bTHhOYS10pvkyPl7rclKGygZ3PHyEQ3AXKkNO568jiAB7hA7sVuFyfGxYcOPL/cy00bo0UvWI2fdImO9Np2bIcLvwZ9ipxHcLbDoNWht3xIZPwu3J/Xx9aL9w3Fe8YxkWBpeWBPTghx+8K8ibvaJ+zjIG5PUMHmbry125HCpz5mc4uT22MDL+HAGpOj0N/Otxq9u7e71TtlBlobPxiRpHakzqryyy7X46QNt0ZnWsltCR3Nia3oLDanfe+2N3JyN5PUTqnYLw/omPkNbifNxbWkACmC4sAPtnjLbOhmjeu1E2d3XPDznjWTFMpDqkLkgwkaLgfaGJy81w1dYqWjDh+mXbI9w9ubnxAX358OSO1uvPtygxtneazHRIk6j4mnodYL3+1wv0ApCcKG0d2tbH7kpztZCTizT0JmZ3IX9XT2twGE19tbgvEb2Vc8qofJ9NxdB7ck8bY7thpGOfdt5xhrg4UsnbDlelOnXecL3oiVU1/4hRSuPRaOb32qEl5isaCWc/aB66K7Ddw1pCtbdrpsF4uwfDmWyA0p/eWuPg+DCglw3phkUVxIq/GE1VEZlnB3wbZh2nj3DbEnifs4wiLDN+zmDl/O8qGDrgM5bCQnxNS9BXLEza6nUnNNYKXBRHy27mnK9bxVx+KULChriU1kvYBCWDsieWThV83DpeC0wmsOvyO6nu+220wOQJvjjuiEBZBF4Y0uZZDo0yvM3PqkCcVYIhIwjPretdtiVBWhVVRdi86R5FYPsr5XPENGr0FrHDxr0gHgoyfccpCxXbOtE5d5xvp8gHVc6673DnVcbSSW5DJLPvG9Ty0VWAwoexvLVwSuRffMBy5dqCRDe2Pl3bOMqHj+kFdhbN/9BMkVdNcdohpN4froXxjXG51dm/Ar4ENukxfoiSWXWqiuzOnU++oJ07Q9LhdOs1oxFdSuIbNHrMN+vzzZvmt7zprpJ5+lsBA/KlyFr4/oaXvuLJrhMExAr1XMpfszC3DZ8veeu6bRbgmRN1QaSRiNW6lHN0y/qpRDIO2qmwEhp23dI42EYikVX7vY2nnBHT1Byb2BXTrRCIL429/ePrzNb2xfL7D/hW/p5ndQ/89edz3fWr1/E/N4X+jb3ucHr8//ilB///BWuzEQ6flar0m78PV67J9e6n38rz+CmPePz0/U3t84P9/2t3Y4f7/9Fude17T1+LUp0sdXMWAHKM7zB5/N/E2wC36/f+n5jeVv7+/aYlbibf4Yc/7Uxfdiu/Vfl+HrJeeHN+/1PdbX9Qb76tflrObrk4rZ+p/gT+u3f/wf7p4hC4IvAAA= -->
