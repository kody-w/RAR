---
name: "rar-cowork-cookbook-audit-plan-product-retirement"
description: "Audits plan product retirement records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_product_retirement", "rar_sha256": "10385876b5412393ee93b973c4f55aea02c6c1f97ccbc128d07c05f18c5ac33b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_product_retirement`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_product_retirement_agent.py` and in the RCI capsule.

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

Plan product retirement Completeness Audit — Audits plan product retirement records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-product-retirement
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
      "description": "Date range for stale-date checks; USMF demo data is mostly FY2017.",
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
      "description": "Excel workbook name, e.g. audit-plan-product-retirement-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_product_retirement_agent.py` and embedded as the fenced Python below (sha256 10385876b5412393…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_product_retirement_agent.py` first:

```bash
python3 audit_plan_product_retirement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_product_retirement_agent.py   # or on stdin
python3 audit_plan_product_retirement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan product retirement Completeness Audit — Audits plan product retirement records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-product-retirement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_product_retirement',
    "version": '3.0.3',
    "display_name": 'Plan product retirement Completeness Audit',
    "description": 'Audits plan product retirement records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workboo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-product-retirement',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-product-retirement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '95374e62f7ca6245',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/plan-product-retirement'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-plan-product-retirement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; defaults to USMF.', 'output_filename': 'Excel workbook name, e.g. audit-plan-product-retirement-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit plan product retirement records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to plan product retirement. Output an Excel workbook 'audit-plan-product-retirement-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no plan product retirement data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan product retirement records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits plan product retirement records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workboo', 'example_request': 'Audit plan product retirement records in USMF for completeness and give me the Excel audit workbook.', 'inputs': [{'description': 'D365 legal entity to audit; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-plan-product-retirement-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy compliance audit of plan product retirement records in D365 ERP, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPlanProductRetirement(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanProductRetirement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-plan-product-retirement-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPlanProductRetirement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
