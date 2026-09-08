---
name: "rar-cowork-cookbook-audit-send-notification-to-customer"
description: "Audits send notification to customer records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning a read-only Excel workbook"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_send_notification_to_customer", "rar_sha256": "acada2f456fd37c9464c1d5557f3a5237e402c577c04181e883d039cf218a6b9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
