---
name: "rar-cowork-cookbook-audit-send-notification-to-customer"
description: "Audits send notification to customer records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning a read-only Excel workbook"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_send_notification_to_customer", "rar_sha256": "acada2f456fd37c9464c1d5557f3a5237e402c577c04181e883d039cf218a6b9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_send_notification_to_customer`. The original RAPP
agent is preserved byte-for-byte in `audit_send_notification_to_customer_agent.py` and in the RCI capsule.

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

Send notification to customer Completeness Audit — Audits send notification to customer records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning a read-only Excel workbook

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-send-notification-to-customer
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
      "description": "D365 legal entity to audit; defaults to USMF.",
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
      "description": "Excel workbook name, e.g. audit-send-notification-to-customer-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_send_notification_to_customer_agent.py` and embedded as the fenced Python below (sha256 acada2f456fd37c9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_send_notification_to_customer_agent.py` first:

```bash
python3 audit_send_notification_to_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_send_notification_to_customer_agent.py   # or on stdin
python3 audit_send_notification_to_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send notification to customer Completeness Audit — Audits send notification to customer records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning a read-only Excel workbook

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-send-notification-to-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_send_notification_to_customer',
    "version": '3.0.3',
    "display_name": 'Send notification to customer Completeness Audit',
    "description": 'Audits send notification to customer records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning a read-only Excel workbook',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-send-notification-to-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-send-notification-to-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c3e8f2306a939a89',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/send-notification-to-customer'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-send-notification-to-customer', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; defaults to USMF.', 'output_filename': 'Excel workbook name, e.g. audit-send-notification-to-customer-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit send notification to customer records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to send notification to customer. Output an Excel workbook 'audit-send-notification-to-customer-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no send notification to customer data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads send notification to customer records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits send notification to customer records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning a read-only Excel workbook', 'example_request': 'Audit send notification to customer records in USMF for completeness and give me the Excel audit workbook.', 'inputs': [{'description': 'D365 legal entity to audit; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-send-notification-to-customer-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy audit of send notification to customer records in D365 ERP, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditSendNotificationToCustomer(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditSendNotificationToCustomer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-send-notification-to-customer-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditSendNotificationToCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
