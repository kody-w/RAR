---
name: "rar-cowork-cookbook-audit-test-and-validate-the-business-continuity-plan"
description: "Runs a read-only completeness and policy audit of business continuity plan records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_test_and_validate_the_business_continuity_plan", "rar_sha256": "960e093f1b1f277a3330e39a5e95ec09a7764f90884ae82afda2b724ef33a170", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_test_and_validate_the_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `audit_test_and_validate_the_business_continuity_plan_agent.py` and in the RCI capsule.

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

Test and validate the business continuity plan Completeness Audit — Runs a read-only completeness and policy audit of business continuity plan records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-test-and-validate-the-business-continuity-plan
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
      "description": "Name of the Excel workbook to produce, e.g. audit-test-and-validate-the-business-continuity-plan-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_test_and_validate_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 960e093f1b1f277a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_test_and_validate_the_business_continuity_plan_agent.py` first:

```bash
python3 audit_test_and_validate_the_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_test_and_validate_the_business_continuity_plan_agent.py   # or on stdin
python3 audit_test_and_validate_the_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test and validate the business continuity plan Completeness Audit — Runs a read-only completeness and policy audit of business continuity plan records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-test-and-validate-the-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_test_and_validate_the_business_continuity_plan',
    "version": '3.0.3',
    "display_name": 'Test and validate the business continuity plan Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of business continuity plan records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-test-and-validate-the-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-test-and-validate-the-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eab4a5178c965bcb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/test-and-validate-the-business-continuity-plan'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-test-and-validate-the-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-test-and-validate-the-business-continuity-plan-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit test and validate the business continuity plan records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to test and validate the business continuity plan. Output an Excel workbook 'audit-test-and-validate-the-business-continuity-plan-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no test and validate the business continuity plan data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-04', 'what_it_does': 'Reads test and validate the business continuity plan records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of business continuity plan records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.', 'example_request': 'Audit the business continuity plan records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-test-and-validate-the-business-continuity-plan-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants business continuity plan records in D365 audited for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditTestAndValidateTheBusinessContinuityPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTestAndValidateTheBusinessContinuityPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-test-and-validate-the-business-continuity-plan-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditTestAndValidateTheBusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
