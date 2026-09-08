---
name: "rar-cowork-cookbook-audit-develop-sales-pricing-strategy"
description: "Runs a read-only completeness and policy audit of develop sales pricing strategy records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary shee"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_sales_pricing_strategy", "rar_sha256": "c01fd617ee00ea89670d003127f2a3aa3f06dbb6def293b755d9f0c4c3840fe6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_sales_pricing_strategy`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_sales_pricing_strategy_agent.py` and in the RCI capsule.

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

Develop sales pricing strategy Completeness Audit — Runs a read-only completeness and policy audit of develop sales pricing strategy records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary shee

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-sales-pricing-strategy
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
      "description": "Name of the Excel workbook to produce, e.g. audit-develop-sales-pricing-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_sales_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 c01fd617ee00ea89…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_sales_pricing_strategy_agent.py` first:

```bash
python3 audit_develop_sales_pricing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_sales_pricing_strategy_agent.py   # or on stdin
python3 audit_develop_sales_pricing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales pricing strategy Completeness Audit — Runs a read-only completeness and policy audit of develop sales pricing strategy records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary shee

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-sales-pricing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_sales_pricing_strategy',
    "version": '3.0.2',
    "display_name": 'Develop sales pricing strategy Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of develop sales pricing strategy records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary shee',
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
        "upstream_slug": 'audit-develop-sales-pricing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-sales-pricing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37e380ba5f3b6055',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-sales-pricing-strategy'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-develop-sales-pricing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-develop-sales-pricing-strategy-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit develop sales pricing strategy records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to develop sales pricing strategy. Output an Excel workbook 'audit-develop-sales-pricing-strategy-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no develop sales pricing strategy data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads develop sales pricing strategy records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of develop sales pricing strategy records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary shee', 'example_request': 'Audit develop sales pricing strategy records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-sales-pricing-strategy-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to audit develop sales pricing strategy records in D365 for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDevelopSalesPricingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopSalesPricingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-sales-pricing-strategy-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDevelopSalesPricingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
