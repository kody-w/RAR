---
name: "rar-cowork-cookbook-audit-plan-service-demand"
description: "Runs a read-only completeness and policy audit of plan service demand records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_service_demand", "rar_sha256": "9499ca65c21f68fc99665f76e9dc787afe7d06828346e7864e2f72ad319ee892", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_service_demand`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_service_demand_agent.py` and in the RCI capsule.

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

Plan service demand Completeness Audit — Runs a read-only completeness and policy audit of plan service demand records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-service-demand
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
      "description": "Name of the Excel workbook to produce, e.g. audit-plan-service-demand-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_service_demand_agent.py` and embedded as the fenced Python below (sha256 9499ca65c21f68fc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_service_demand_agent.py` first:

```bash
python3 audit_plan_service_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_service_demand_agent.py   # or on stdin
python3 audit_plan_service_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service demand Completeness Audit — Runs a read-only completeness and policy audit of plan service demand records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-service-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_service_demand',
    "version": '3.0.3',
    "display_name": 'Plan service demand Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of plan service demand records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-service-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-service-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '066a879f47987662',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/plan-service-demand'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-plan-service-demand', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-plan-service-demand-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit plan service demand records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to plan service demand. Output an Excel workbook 'audit-plan-service-demand-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no plan service demand data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan service demand records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of plan service demand records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit plan service demand records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-service-demand-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants plan service demand records checked for missing fields, stale dates, blank descriptions, inactive entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPlanServiceDemand(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanServiceDemand'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-service-demand-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPlanServiceDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
