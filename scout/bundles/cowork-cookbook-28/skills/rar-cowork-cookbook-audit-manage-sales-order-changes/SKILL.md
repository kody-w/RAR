---
name: "rar-cowork-cookbook-audit-manage-sales-order-changes"
description: "Audits Dynamics 365 F&SCM sales order change records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_sales_order_changes", "rar_sha256": "db9adcd2e84e7f7788364e8e3d22d8fbda65bc6c2e60f1536a4169818c1d4bec", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_sales_order_changes`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_sales_order_changes_agent.py` and in the RCI capsule.

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

Manage sales order changes Completeness Audit — Audits Dynamics 365 F&SCM sales order change records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-sales-order-changes
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
      "description": "Date range for staleness checks; adjust for demo data that is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-manage-sales-order-changes-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_sales_order_changes_agent.py` and embedded as the fenced Python below (sha256 db9adcd2e84e7f77…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_sales_order_changes_agent.py` first:

```bash
python3 audit_manage_sales_order_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_sales_order_changes_agent.py   # or on stdin
python3 audit_manage_sales_order_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales order changes Completeness Audit — Audits Dynamics 365 F&SCM sales order change records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-sales-order-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_sales_order_changes',
    "version": '3.0.3',
    "display_name": 'Manage sales order changes Completeness Audit',
    "description": 'Audits Dynamics 365 F&SCM sales order change records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-sales-order-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-sales-order-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b52af7f1800722ea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-sales-order-changes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-manage-sales-order-changes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; adjust for demo data that is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-manage-sales-order-changes-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit manage sales order changes records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to manage sales order changes. Output an Excel workbook 'audit-manage-sales-order-changes-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no manage sales order changes data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads manage sales order changes records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits Dynamics 365 F&SCM sales order change records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit manage sales order changes in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; adjust for demo data that is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-manage-sales-order-changes-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy audit of manage sales order changes data in Dynamics 365 F&SCM via the Cowork ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditManageSalesOrderChanges(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageSalesOrderChanges'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; adjust for demo data that is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-manage-sales-order-changes-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditManageSalesOrderChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
