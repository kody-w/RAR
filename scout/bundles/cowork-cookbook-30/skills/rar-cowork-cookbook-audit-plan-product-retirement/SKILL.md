---
name: "rar-cowork-cookbook-audit-plan-product-retirement"
description: "Audits plan product retirement records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_product_retirement", "rar_sha256": "10385876b5412393ee93b973c4f55aea02c6c1f97ccbc128d07c05f18c5ac33b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
