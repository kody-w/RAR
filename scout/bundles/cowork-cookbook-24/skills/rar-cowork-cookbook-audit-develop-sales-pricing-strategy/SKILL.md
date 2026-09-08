---
name: "rar-cowork-cookbook-audit-develop-sales-pricing-strategy"
description: "Runs a read-only completeness and policy audit of develop sales pricing strategy records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary shee"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_sales_pricing_strategy", "rar_sha256": "c01fd617ee00ea89670d003127f2a3aa3f06dbb6def293b755d9f0c4c3840fe6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
