---
name: "rar-cowork-cookbook-audit-process-freight-invoices"
description: "Audits freight invoice records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_freight_invoices", "rar_sha256": "8632383b9cedf004cfde4d98932268aaa08674804a0ccc9711c66d6015f320f6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_freight_invoices`. The original RAPP
agent is preserved byte-for-byte in `audit_process_freight_invoices_agent.py` and in the RCI capsule.

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

Process freight invoices Completeness Audit — Audits freight invoice records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-freight-invoices
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
      "description": "Date range used to judge stale records; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-process-freight-invoices-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_freight_invoices_agent.py` and embedded as the fenced Python below (sha256 8632383b9cedf004…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_freight_invoices_agent.py` first:

```bash
python3 audit_process_freight_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_freight_invoices_agent.py   # or on stdin
python3 audit_process_freight_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process freight invoices Completeness Audit — Audits freight invoice records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-freight-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_freight_invoices',
    "version": '3.0.3',
    "display_name": 'Process freight invoices Completeness Audit',
    "description": 'Audits freight invoice records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel workbook.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-process-freight-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-freight-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c5290973dc18a5b3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/process-freight-invoices'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-process-freight-invoices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-process-freight-invoices-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit process freight invoices records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to process freight invoices. Output an Excel workbook 'audit-process-freight-invoices-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no process freight invoices data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process freight invoices records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits freight invoice records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel workbook.', 'example_request': 'Audit freight invoices in USMF for completeness and give me an Excel workbook of the findings.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-process-freight-invoices-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy audit of process freight invoice records in Dynamics 365 ERP, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditProcessFreightInvoices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessFreightInvoices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-process-freight-invoices-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditProcessFreightInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
