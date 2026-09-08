---
name: "rar-cowork-cookbook-audit-issue-purchase-orders"
description: "Audits purchase order records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_issue_purchase_orders", "rar_sha256": "f680bb401d52d4f8a9049931a11557510634a5de7dd9899369155896e3c1e098", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_issue_purchase_orders`. The original RAPP
agent is preserved byte-for-byte in `audit_issue_purchase_orders_agent.py` and in the RCI capsule.

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

Issue purchase orders Completeness Audit — Audits purchase order records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-issue-purchase-orders
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
      "description": "Date range for staleness checks; USMF demo data is mostly FY2017.",
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
      "description": "Excel workbook name, e.g. audit-issue-purchase-orders-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_issue_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 f680bb401d52d4f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_issue_purchase_orders_agent.py` first:

```bash
python3 audit_issue_purchase_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_issue_purchase_orders_agent.py   # or on stdin
python3 audit_issue_purchase_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue purchase orders Completeness Audit — Audits purchase order records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-issue-purchase-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_issue_purchase_orders',
    "version": '3.0.3',
    "display_name": 'Issue purchase orders Completeness Audit',
    "description": 'Audits purchase order records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo',
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
        "upstream_slug": 'audit-issue-purchase-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-issue-purchase-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2d6cf1dc60d1b4fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/issue-purchase-orders'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-issue-purchase-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. audit-issue-purchase-orders-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit issue purchase orders records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to issue purchase orders. Output an Excel workbook 'audit-issue-purchase-orders-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no issue purchase orders data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads issue purchase orders records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits purchase order records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo', 'example_request': 'Audit issue purchase orders in USMF for completeness and policy issues and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-issue-purchase-orders-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of issue purchase orders in Dynamics 365 ERP, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditIssuePurchaseOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditIssuePurchaseOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-issue-purchase-orders-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditIssuePurchaseOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
