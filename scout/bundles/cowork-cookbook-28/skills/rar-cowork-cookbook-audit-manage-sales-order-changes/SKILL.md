---
name: "rar-cowork-cookbook-audit-manage-sales-order-changes"
description: "Audits Dynamics 365 F&SCM sales order change records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_sales_order_changes", "rar_sha256": "db9adcd2e84e7f7788364e8e3d22d8fbda65bc6c2e60f1536a4169818c1d4bec", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
