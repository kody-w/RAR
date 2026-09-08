---
name: "rar-cowork-cookbook-audit-create-production-plan"
description: "Audits create production plan records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_create_production_plan", "rar_sha256": "63e4fb3884f7a9edd58bbe30409e01baf592fccceb19cffcab616eb8a6f3e127", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_create_production_plan`. The original RAPP
agent is preserved byte-for-byte in `audit_create_production_plan_agent.py` and in the RCI capsule.

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

Create production plan Completeness Audit — Audits create production plan records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-create-production-plan
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
      "description": "Date range used to judge stale dates; adjust for demo data (USMF data is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-create-production-plan-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_create_production_plan_agent.py` and embedded as the fenced Python below (sha256 63e4fb3884f7a9ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_create_production_plan_agent.py` first:

```bash
python3 audit_create_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_create_production_plan_agent.py   # or on stdin
python3 audit_create_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create production plan Completeness Audit — Audits create production plan records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-create-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_create_production_plan',
    "version": '3.0.2',
    "display_name": 'Create production plan Completeness Audit',
    "description": 'Audits create production plan records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-create-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-create-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4966be86be830303',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/create-production-plan'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-create-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data (USMF data is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-create-production-plan-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit create production plan records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to create production plan. Output an Excel workbook 'audit-create-production-plan-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no create production plan data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads create production plan records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits create production plan records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit', 'example_request': 'Audit create production plan records in USMF for completeness and give me the Excel audit workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data (USMF data is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-create-production-plan-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness/policy audit of create production plan records in D365 F&SCM, delivered as an Excel workbook with per-category and summary sheets.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditCreateProductionPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCreateProductionPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data (USMF data is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-create-production-plan-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditCreateProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
