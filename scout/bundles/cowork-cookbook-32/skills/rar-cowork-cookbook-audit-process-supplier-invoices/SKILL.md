---
name: "rar-cowork-cookbook-audit-process-supplier-invoices"
description: "Read-only audit of supplier invoice records in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workb"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_supplier_invoices", "rar_sha256": "3e28bc69eb3c70f948e96b583e97f85a911a5347c58020ec668a581c0b2b12c3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_supplier_invoices`. The original RAPP
agent is preserved byte-for-byte in `audit_process_supplier_invoices_agent.py` and in the RCI capsule.

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

Process supplier invoices Completeness Audit — Read-only audit of supplier invoice records in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workb

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-supplier-invoices
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
    "date_window": {
      "description": "Date range used to judge stale dates; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Excel workbook to produce, e.g. audit-process-supplier-invoices-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_supplier_invoices_agent.py` and embedded as the fenced Python below (sha256 3e28bc69eb3c70f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_supplier_invoices_agent.py` first:

```bash
python3 audit_process_supplier_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_supplier_invoices_agent.py   # or on stdin
python3 audit_process_supplier_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process supplier invoices Completeness Audit — Read-only audit of supplier invoice records in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workb

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-supplier-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_supplier_invoices',
    "version": '3.0.3',
    "display_name": 'Process supplier invoices Completeness Audit',
    "description": 'Read-only audit of supplier invoice records in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workb',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-process-supplier-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-supplier-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b8ef41ffd280c95f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-invoices'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-process-supplier-invoices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-process-supplier-invoices-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit process supplier invoices records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to process supplier invoices. Output an Excel workbook 'audit-process-supplier-invoices-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no process supplier invoices data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads process supplier invoices records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of supplier invoice records in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workb', 'example_request': 'Audit supplier invoices in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-process-supplier-invoices-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance audit of D365 supplier invoice records, with findings exported to Excel and no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditProcessSupplierInvoices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessSupplierInvoices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-process-supplier-invoices-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditProcessSupplierInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWJbmX9G8HTGZ2bJfsQu5oyMGsQkhAWIRQukKJyD2fQdl13+fiyQvWZXV1RUxn0YOWwLuPft5zjm+/P5md21Y1G+f3jTPzhe8naZR6NULO78t6GIo6gR8FYkD/i7cIm/ryOnaom7ePrzdvMato7KNihxsVz379rHI02lhd7eoXRT+ounKMo0AsSjvi8j1FrXnFvWtAdcLZsrtLHKbBUrgC+5/a/Rx8XPqBXa68PI2aqeFoR25XxZtaLcLP7WDZpFFTRPlwcKPvPTWfFg0rZ16i5vdeuDCSe08WfwgEbgX5bbbRr338UWx9nyv9nLXax7alUUaudOij4rUfu2ovbar85kJMAU7ul66mC3gAGW90c7K1GvePv36lw9vEfj99un3Nze1G3DrjZpVVuoC0G60l9bCU+nZUkC4AKwqJ2DqHFyXXu0XdQZu3Tx/8br6ufFS/8Pi3/89Gew6aH759DlfvD6f3+Y/apcDe3iLtrCb1rstXLu0nSgFqr0vqHSwp+alANAPWKcGerw/d36nVJSL/5yf/fxk8h547c+f3wogwsMGn99+WRQ14Fd38+/3mUr58y/vaTF49c+/fKfTdE7sue1MDEj9/uV1/SILFn5fGvmLL5rC0i9eIAai0gPEf9Bv/jxFf5F7meTLc/HPRflh8eeUZ33+E8j79LwD6P45WWADsPPtPS6i/OcXj7rovdwG8fDzL/+IrBt6bpJGTfs/ovvrk3AIMgFY62WSXz483PeXxfKl2zea/5htCQLmX9EELP/K7puh/hHth2f/hnQa5SApvvryT8n92Yblfy5+/Ye6/XcbPiz8z2+Ml4LkrG0n9T4tfn+EyK8/3b7f/OkvfwWk/ykZrehq90HhS2bnke817Zcvv/7UPG7/9Jdff+pKEMWenX3p6vTPaP6ZXR98/mDB16qf/7gX8DfyJC+GfPEthxa/F+X/qv/6vjjbaXT7fr/5tPgxE+fPcjEr8ZXp0wQ/ZGMDZP3Bjr+8/RUgTw606dzHY4Af//Zvi2Pk1kVT+O1Cc4uuXQAHt1HmzcLrYQTAtnmgRu0BuzYRMOxrHYj/2cOzxACrf/s/7gPtP7ovtF89YHzOkhnUvnzF8i8vLG9+e1/ogGxRRwEA2nShUoryObcDALYzy7L2Gq/uAUw5U+t9BNn8cf4xQ/9v/4TylweR93L67YHT0RP1VFqYEa/pUu991s0MvfyliQvQ2hs9twP008IFwvhR6j3wvCnSHiDmbIcmidJ0cYsApoACNj1oA1t9mon99ttvjt2En/MnRKOLZx1pVmDBN3EWHz8Crfw0CsL2c+65YbH46fe//rT4r8V/t+tBfOahgFLx8gSQcK/J0gJkVpeBZXNFBJBu3x6e+P2vL9sCMjmonsBvESh6z80gMhPv9tXQ2o76iODEwvGAgYFxs7Ko27l+Re37QvAX3+QFTOdHc2UIi6YFlbL08hsohtOjxH7Ov1kyL9pFA8Kv8acPi67xHlx/c2r7IWIGUtxuf1scaQXUoSIF/8xiPhaBzUUeAfN/C4PnfUCk/qlZbL+SeF9IcywuSru2y7C2Xzx8++kXUH++bgfE7UXuDZ/zueB6s6keifE0D1gELOO+XPpx9jloUTKAAs8Wo/26xp6rpf6omvXnvHkFvV0/GxIgyrQIuug2l4L/eIVUExZdenvYD0g6U3p54fbyyiMGXxX/7xqdBvRMs8At4A4eP7qDxecOgWBs8f9znzTbhOJ5leUpnWUWrKSr1tNXc+s4+/TZbc5cQMA+8/J7G/MVqr4i9uc8jUDg1dN/PFc+PPxa80TBrgYOUSn1QR+EF7DhTPcR/XM01/WcN/bn/Gtp+AAC6oGDIAAAVIBUmiP4K8P56VdJQ4AH8/X3NuHlltkoIMIXZecAwyx8z7s5tpsAqeo5g19uBqngzb4dwsgN/6DV7DgQcYD+AggRgZwE5eP9G1w/n34V/Q8bn93QvOXRKXYggesHASDH7K+Hu4aoBThmt89OHej56UEEqJGV7ay7A7wINH3eBI6uuqiJHsHxtKtXAqT+OH8/NZ3vemMJsgYYC+RG2QHrPrJpDoAM9DpABhBSILmyKAe1HxjlZYQHQTuboQFA76s5fVJ83H4p5D1ScC5aXzfOisx75j5g4QPRwZ3pRwTR/yxMAL1sXvHg+7eR9o3bTHtG0QYgIeD49emzYXh/1vxnU7H4SvfT341CP/9r09Kjiht/DIBPi7Bty+bTavWsvF8L7zvAsNVT1uZZhD++SuXHr0Dx8SvO/IHsU+NPi39NtD+QeKXGpwX8Dr1D86PDK7ReH2AJ+uPW+ojNTz/nqvcdYAH7IgOxNfttAlX/WzX8ugSUxKAG0AUWP6tjMxfVAdTxRzkATvic/xjrc66BapMHc2w2xQ8Y8GgLQNw/ffataoFHeQt43+YWMvDe58lrFr/x3j7lXZp+eANY6v3zcW0uTNkcz8084wHjg4asjbzH1QMexnb++cf5V378sNP3BeMBKEqbH2PuVU7mcvpDajx1BLq5gMOHJ0TP5Q/oODOf08puQJyCEJ11aadyFv452c294LzhyxDlt2L4e3kY8HBRz9ab2T5gLu5ugfdjPfiPR/UAuZsV8w17BtcMtAfAhpwFxFz/KdtH+fnyLBZ/wncuVH+oUHMVnw3+YeG9B+8Pln9K91vf+/dEzbm8ATq34tNcfz+84Ax8g3r2YfFt7Piw+DoIzhy8vAMz9q/zyDN79bFl/gH2gK9vm779V4bjvf3lz+R6YN6XOfKe8fO30kkzlgGsn336QzWcMw3IDPjeOtd7af9PEvojAiHERwj/iGDvY9qMf2IoINEDtEHpm5X7brXvsheP2W2WHejaPv+r4fc3ENL27OVXUL+af7AcYNzHZm57ViDtAUNw/UxQ8OxfHQte25vQBn0p2I96COm4xMZzUHcN+RuM9DaEg5Oot1n7JG5vYNjGUWzt4iSEQJ5LEKSNk7ALOYgDIy4K6D2z/Mvc2kWzSLM8wBIfAVB43x+DW7eXLk/ZZ0N9m0JmnV8q/f7mEBhYucMagXp+6NUGdlYm5kzX3SqHVqo08PKVFeVewuFDtVPCtZF6CBugsZE4mMidWkbKNAuH8212i7GExURKYTXvyG6mnqi7XX8ljb22weFpCoNJPW7QM+xf8GpZmTiaMS2a2JUonNTrOXVtdWK1y8W21B0W67drzVZnQ+xz+BaehXK1ktEeS+97d19kpIELfml3ci5xdSFAzNCSHOKtVZ6Ii+3WX62IvaeYPkfc+pEOTXtMDulVVTv1uLrUIy6pTqqW14hzW1hwrqph6HuzGiLO8jl1q6Xx3hCudj5c1fyAsxVbBfEk0l0sHfm7uOe2/BmpK5u3Kvwino39OmGTook1OSgRLG73VhZmuFg1ZGGcEyHFlwx3apz2QNpxYinKqutW8gW9w6vNan/slfsS9VOlzyPU0PYCS0bhKKwP+rXW+aqBtuRGFU7idTINA7pLpHjnsakopjMqrCNRSg+9cjPu8MCZ7OUaBPyZ4ixDZDEfXcs4bxonYctKUbkhnYLF9EmxqY6pjSlKtVqMrkxkdga3iZhIOsT0mhHblJDRtFlKB8aBFLfXbfwilJy1p02NwjcAtUK2Ll0xZcQ1xU4RW0tYoqt6ueEtfXvteT8Jw6WFF/SdOqV+CCeriBn03s4veO6Z+HEgS7XMIjpKXd3QjNA8VVkwXDQ26st9VKAUnJmeozUam9zLYLds4XSfwTh9u0WRH8TtKh051T2ZhWfOU/AkERe/Z89ExeCZCGa88nCqmqGk/asvFpGWOshZWB3po1ae+2LSaQzbondST7iwurjm/VhuY0MnYZPbxjat04m3PYz6UknZsPQC0yARK7nI55MYgo4xlEqTOpcO32wPbYdUlyIVRpibzlYoRe2lQSaxJZPtdpPsXZK9hZW7DtpMF5f7s3fwOT+mMSNWhjW5vbXCLoqQLU5fG5nWV1LE7IuVFBtLFu+mu1BfJyOn2OF4vw8rbW2lWcvEocUw0o3RrkgRDO1tx5Z2icqj7I9leBgu8Vbf3VNlJfiYiwBe2dXHGZrwdU7fSD252w91awuWkyQGyWiEameqDFpJ7ywTTKjlUhDS69TDh1DhhUlBdqvwem8wCsZjQz0sB+bcuFUaCPgRNk1RlUtcRiY2homK9jV1bxYFXeOCpmGecF4lttifTsHgHUL/Mo6GQLJrl0EK9bLd9lbEuPolIu7OsW5yntmhibZSke3ZY3ryXLWp3ZvRzWGHLg2tizY1h+Ka9SUbJX5gu/3dVoJlLBR96mS70ocqseLzRrhr6pIxcsZpU+dmAxQl7w7TrUYGG5aoYO1NlmM3oC2P9cxiIjeS+WnocSE37HbDTjt1VSStd+eMfe8UyXDJbnc1mKKQF32aFsUB3Xh4y6uMsEy4/QE+ebrt8ghGx9wyX1prBCOnsvMRPCl1iIvOhsZLgb7l2d2mRnfi/n7WRsNNkHXWenyipUlAq1ReMTla3xKUvh1MQ9tu4lhhFETyuC4/wEtSWqcta1yHthc2EoX00/ro3neGzgT3Urw0rS9RJwQTzHJocm7pryEBRGd6xC47ioNiUZRcOOVcIyyd5tRN7QbD3ca60/3qfKr7AXM8BevqjZqsyHWxF/eXAbd7pu7jWupgR7zm1/1lJym0R4Aga/r9ldvxcJmnu1Pu9KgsHZSYCjfcHhXC/e6Wu6cCO9MaafEbfI3SSCdcdChAr1KkXThGHsuteYJUy93AfW1QdH0dPdAUrmhtiLbBmcfzOqJBwOojbbEGZvFmIxiU3aT8xvNRGV4zckGzaWBrkCnY3KBrulQMISHuGX3oUFgGIw9x38tUUbBHmm/CDo/JoA6mIoDaqFmOmpkL2kibhBAM1RolNCOHKryC0d1mpLSajwKi4mMiPps1bjdYcBgdE6hBpuUwqHKa84RCc4m7EnOYcPt+vcG0M5ud4Uz0NdH1t/i5SHdijGSaEzeGlwwn67z0EGW3DAcxXDfEGAAwESzJXiV82/dp1Z4Kf7XkVPLo5iIiXa7l/rJFNG/pcAkNCUGA3PcYuZPEMblEzb5suZI7qealW/INj7ZxJWbIfTCxoYx38bhe+X1dTL4+smM11kYpmqfeDowjEpA3XpHuPDHl0eaqR62BMbkc3zmquBmBo5ImZ5epIlK5lDO0eV2HVHEQdqPOG6dye4lEHYqlXTshOzSvOXuqrbPEufI1weJjh4qX5ELilV0im2QyebQ+47JaIBTNUaFQ1ZWAlRXqMsGx2G8gWXYzQbC0Ad/CU9TaTrsU1/0W1uDW0/Zj0ifshQ4ti8paf11eIJT1vVMkRH2+lGJJtgOr36cDm8KU5jbipj4qBeitNFUYT0pgUnnTTyhB13uNAhlWYuXFOBMGNGzNskVJfChTukrHoKrlsuHS8BoYbBPRMdXA0JCoyt1ly4DJHHm0VESfBE53qaOKrbZFca4Hs7EnzeKVYnCvOi4GTRRw/QEqi8No5Fy3dCOqsc5CVoDZYW+s1p4jidYwHkl2aCwtnDY0j/bTkk+TbgvQ/8JdNjaG6MfzKdhhIWHYkErjFn+cbjTUj6nUC2Fl10nFJ/j1ctcOIUi7rUXR0REnauLuSastfBKqfZt2YJZheSVvZT2w9htBzUjNPVbndpnjWofpfTDd4Z19pM02UhDWBGB7qg2NJrdjoOicxvlcqpxyq2iOqm7BaLFM/bvOliNfMF542RDmLaJ2iHC309i9ZSGK5FZ0QDiVqwp+2UM5hfZ6GlLaCiK5sUdGXwndZCe48XXZ34rmvAJxw6JnyNqLNNShNUb2vg65PIh+tkJiuSEKJ+GhLjstBwiyS5kvQ5HXNAG9DgVbmcbW96tCDM17y5ugXaGkYVtdtmUYdWPZkD1BdTZN21N4txjSqdmpC0t3EqTTliQQvUZuG+5U0Xv8vO15tiNiCeMVqhzpceKZu2qPwnjJ97zEEV4/GoTNMzV+OIWxv9meBtqoZTrJJNM5YojahSQ1soy63VtnA+H2JORzvFQx43KEdYdGA6XJ1sqqv2/EACnFMEPGdRHsdtOlJZaQHN3zw4mMM3qIzhfW5pAkWAa8bRKr856p83y5vI5qe1waB2MUNJda3l1BSDS65NQkLnc7dcAvgdHlibCTcclK2RL17XuwcfdkbXGIa0tOeeM1OqczY0umzE2SBHg7bq+UgGVdTxkJxSLbzK0qqUkioqPxI1ABYzhG3++8RDnkDq8a2+W22u1BQTme6/LsjPd1WoUejYo27asw37PQgYhsctnlY0GsltGQ3jNzmPj0mGFIbdwrRtIuVpQeVkhmB+bebbGTXQUCK+s94VkUuYx2enE+wOZQUEIZwmbA7KE4urQ2hcP9StiMALLyC19sYkvrJ8Rrx8Ta3s9VNW02NX/2j6CSRuOp1w2RShjaRcdL19VNSmDKgEYucub2wcHpU2NpFDxK+Y2jVpYCukrNYAsIPcGSB1F0UhhxuOWt2EHzLbcyzvsMy7FgPIii0oImbL/TQC+hRjQCXZDwurqviNhFTuNR3Cyv/GayU8Nklj7vI/J46HE0l9TER4Uq4rT4Zrre5SDtzo5KnEYp5rhkO7aXtvVZ+bgvrYBjMStpESmKK4eEKgjlWgZg392z86OlxUcZJNmJi6X6WPE719bzNjaotbkC5ZDnNfVwrFUdI1as5u/4GoZOKdWcWZGqTjHtwdehOpC0lfknKeXaG6xNcKLg14zwEuaoU+loBJV8jntvRxnNZX03C1tLyoDwjYyxlHMVaao8Ujrp4nYk3tnutqmz4+GmHDlCQrOwPJO1FAvn/dFw96vTAQpu/VY8l/3JuAZHXql5vZNvCmERGd1OUu/6x/JiXUWo9k2VOR3X63gvB05deiNWOyqi5j29F7kl6GSo5XJvM2d3t6bzbgVzKOn0rR+YRcmiJyblYJck4PGmrk43aHUdhYORsVK9cTVB2/N8egovlSRiXIwdWr6h7cuOxJCr69JLSdnspgPqh9ucs8OeQOLTWjJKax9Qp5NThoPRHc/ObufhkYcrmjKJsHoSMpwuEchCOitZC+e+Ko5yJ93ULF8zvOMfd/et3Bzu+YUCcF5cq8w8n4/5cK/h8aSG6zKpR/i+FNteS2Uk0fTL1jWa0jerGOXXU7NDkJ1ik1f6cjnLJJKVB9Tzr0XYDr4EB2FkmF0bdrR/D83jiU4o28Y8ca37hxXDxNf9GU7g2o848swy4aaVd9cdU0xC1e09g7hl0vqyEU5nwofqPN0MVDqBloTBJuwsEgUMt2dOWu56ME55kFSLG+YQ71TBIRGapxyV91oqgi5FCaL02jLHDoFV58S3jC3k6i5whJUVG+29V4ozkDAyc4zapnfWzRKosjoZbrKedsdDnB4Luwp3hdqI6+Mh0+Q1Tcg2fLRjtW/bwAyAtRGecLLwSKQ2JdsncwnLh3Oq7HFE2aMpwUF4OyzHA7NcBTYT4LCIYE5/Gtcll+h5rPothGWoqejT0jl4lzbD7tMk3Tgcxtc7WONu7BTY+B2FPaS4QlTaTmkN71tI3QrS+dLV8aH2+TWrmQcYviO9za8Lb9jfnQNEk9bl0ptOalb9tHU2W7pfDvtNqmxoUa3ZIVd5m9cmBZe2ekkIXeoOrHPVC7FDS6lcOqUXxuRZ7n1Yud/Pbd3hxFq6mcputEysg9daLN8P3aaBXUsJ63XsR+HKKa700WKgQVmOm9UKTNOjceF4rppWq7QnZWmnhbtYRxyESPyMcEUh2/pF3WrKUfIPR1M6ObvgmC8ryln2w769xEHr1FuU4raEoGtqWWHxko2T7aRv0N5D6NvmWkmjBVcQ6PLynXquGTH3mbRQeCQNKJI6hh4Y713shsdRypoKwVhutF4vtxSPw+3aO4OihXJpx66WMgw++C3c54Of3HpBzlEnOWbmltCkPZZqykYJ5Qt5X5fZSEBOsCVIOHUujN4guqQSRFDL52KlRTV89c24Xe4OMY/LMU1dE1C9SYVaO5vJzNV1Hwk5bcBSrbiiWDkbvskOSr07ty1z7+nUVJqpGDaUI996XcDzNSTWK+YYYtelmHmKrwCc9yO3M/au1dyaq2BURqRnFCnrvIexZxunCt47GkPf9Qp3OHH7093Xrkv4uDvxNwhollGHWLdOCHk175Y3sTWCl5p6t/X4NmwKepv6oADku2O5X2/aSw0RChejKx/eYnWpLdXI1wkVceARCSWPWYPZAtWFwR9MZiUjlc6s6kS5biWb9zKHLH2XLDjRJQZ1I8uHYp0ejqMJB/h2wA7Vdef1Mm7jOoxfMbk+DkzGuXqBJ2tpJXfdibCPddretx1R7Kno3kWE5G5d2eXXrtFazslY7hgN2VcECa2g1NKJPmsNG8HJdaBnvWQikILa5f4e5EcDMTfE4ZqPFlq6YTgxiYNfthCiM9AyM5Xs1lAqZXCXE+/JeseDrmO1DFeauM3P6tGJB5XbEVZd3VSxiokrC2m9O4DJyD+Z9UgSEF5ezqaOSr0TQuv7uBbPJrRmj6s1AAB3uVZBNylkGklIpIwr0AaW7n6+PBOF0tzIqaW7yvcJuTxhfnqx0KNgwgcvFpcXg1MOzuYQImWdQgkcC3t/kq2gaihjpQ/teL0VWOVVSMXfuaqTLZeGbpDWpnchHsdDDiaaFPJHbod4TZbv0exw4ietKcBEBuVw2J+RsTYZi9OJBG/hHVYUq/48BCo/gJIpT7qXi5JA1h7JY/5dg+BTMYYb0MXD8Co6UAYt7eSWil3ieEC1qnc3O4gWMCxRsGNE4nAIBk7d9/Zr3taxDlqaskWIZa/rY6cvz7c7d5E33UHe3YKDIY1pjiVBVNIWfd25B7+KD4gqxd0yFeL7AT1p8WYpOwqDXHcFAsUk0blQIattza8lpWURst1O9f0stAO6XBuGs9y4CFTcx/7Aa2WDXLPu1k9XXjwhjOThYUYra7KNj3whucmYAcCy+G3vE/q+HYng4q8i9a7YYLLd8ujSuyyXW5tLNDCjrJjL4OAStm986oBsrJhPFIikJOdE7qlLH55EJSorCN6ft07WMtrQhzzoQqcdK4M5TrBgC+lbUOHM1QW6wypeTPJJTNdKI6Nengv9BaGYsV8lsXg/2CdGaBV2RzO3Sb0PtAYxOBoHSwW/oOmqwAVm2QljR0sEPWUALEX+7ly8Eq53+srt2l4Gs5HFTt5uPB827rI/lKh2QbMNxXB9ZTNEHGV9FIOu+YrE1HgV1oXLp55Dqh4q6B56afRsOzltF7htjaY1bvI0irNJG1MSR1t3qa5N9OrukHTyFReU18YLttPp6DZtt6UPW6+4sdgW09GJpOSdGpOH8QDXptOuaupaglkfhDu01jG+IaErgqDEgBYhRIPGQiy8UQPCa0qtMAexq9eRvSSbFbopLuiZuK1vMiGuxtLcWus1eUUB8rLOCiloBx5wgrsPljSS2vGIJobTIRqBaWKxrsraxHRHWU0iv1bIBqN7X8HMm1TLktkARF+SO88/bKYO5VuHgLOM80Qf7/jW5eJtEYPu3b3xvCWzbu9NpArtPZhfB/UaXu9pOkfcgfeENDhxxc5JMXzICKoShlS6bZV09BI53w5kR7QjBmM0x2zvu/7KKFeJyoSdGRAyE2p+QkU77e5OS/y0jooTsVwdb93RVfrlxd9EihZDrLRyjwgOR2hb7hKs2sAUYcoKvM7Ow4UsSdBKOijUhYdMtPkzfTmREt4SOG4q6w2MhQqFCrt7d4Ba8nLiEGjSQutQ3PUlTdZq77jiWGMS6xvVfa3d48Bf0YToixJwVUBRbx/evh+hvf1P3wGbD3j+n50lPY+Evr7P8Tga9OzbpwevT/9jif7y4a12IyDP87SsSbvgdfD0N2dlH//JYd+8eXq+VPX1VPl5TN3awfyi8VuU37qmracvTZE+3uUAO5yumV9ObL5K+uPJ5oPf9yOxtvhS2rMFo3x+OcO7RXbrvS6D16Hhh7fb6w2jLyiBf/Hqctbv9R7AbPN36B0Y7v8CdBFagyguAAA= -->
