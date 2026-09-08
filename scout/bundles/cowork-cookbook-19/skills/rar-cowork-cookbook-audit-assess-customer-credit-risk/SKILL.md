---
name: "rar-cowork-cookbook-audit-assess-customer-credit-risk"
description: "Runs a read-only completeness and policy audit of customer credit risk records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_assess_customer_credit_risk", "rar_sha256": "9ece99c8fea9f9323ddd228ce7e648a56adff755e151bcb568c7eb9b2601aec3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_assess_customer_credit_risk`. The original RAPP
agent is preserved byte-for-byte in `audit_assess_customer_credit_risk_agent.py` and in the RCI capsule.

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

Assess customer credit risk Completeness Audit — Runs a read-only completeness and policy audit of customer credit risk records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-assess-customer-credit-risk
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
      "description": "Date range used for stale-date checks; adjust for demo tenants where data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-assess-customer-credit-risk-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_assess_customer_credit_risk_agent.py` and embedded as the fenced Python below (sha256 9ece99c8fea9f932…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_assess_customer_credit_risk_agent.py` first:

```bash
python3 audit_assess_customer_credit_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_assess_customer_credit_risk_agent.py   # or on stdin
python3 audit_assess_customer_credit_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess customer credit risk Completeness Audit — Runs a read-only completeness and policy audit of customer credit risk records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-assess-customer-credit-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_assess_customer_credit_risk',
    "version": '3.0.2',
    "display_name": 'Assess customer credit risk Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of customer credit risk records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
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
        "upstream_slug": 'audit-assess-customer-credit-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-assess-customer-credit-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0467970700361af7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/assess-customer-credit-risk'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-assess-customer-credit-risk', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used for stale-date checks; adjust for demo tenants where data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-assess-customer-credit-risk-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit assess customer credit risk records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to assess customer credit risk. Output an Excel workbook 'audit-assess-customer-credit-risk-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no assess customer credit risk data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads assess customer credit risk records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of customer credit risk records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit customer credit risk records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-assess-customer-credit-risk-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Date range used for stale-date checks; adjust for demo tenants where data is mostly FY2017.', 'name': 'date_window'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants customer credit risk records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAssessCustomerCreditRisk(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAssessCustomerCreditRisk'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used for stale-date checks; adjust for demo tenants where data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-assess-customer-credit-risk-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAssessCustomerCreditRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
