---
name: "rar-cowork-cookbook-audit-process-freight-invoices"
description: "Audits freight invoice records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_freight_invoices", "rar_sha256": "8632383b9cedf004cfde4d98932268aaa08674804a0ccc9711c66d6015f320f6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
