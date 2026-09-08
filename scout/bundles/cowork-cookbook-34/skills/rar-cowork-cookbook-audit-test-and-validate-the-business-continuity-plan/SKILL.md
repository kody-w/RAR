---
name: "rar-cowork-cookbook-audit-test-and-validate-the-business-continuity-plan"
description: "Runs a read-only completeness and policy audit of business continuity plan records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_test_and_validate_the_business_continuity_plan", "rar_sha256": "960e093f1b1f277a3330e39a5e95ec09a7764f90884ae82afda2b724ef33a170", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
