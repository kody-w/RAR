---
name: "rar-cowork-cookbook-audit-assess-customer-credit-risk"
description: "Runs a read-only completeness and policy audit of customer credit risk records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_assess_customer_credit_risk", "rar_sha256": "9ece99c8fea9f9323ddd228ce7e648a56adff755e151bcb568c7eb9b2601aec3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
