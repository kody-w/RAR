---
name: "rar-cowork-cookbook-audit-plan-service-demand"
description: "Runs a read-only completeness and policy audit of plan service demand records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_service_demand", "rar_sha256": "9499ca65c21f68fc99665f76e9dc787afe7d06828346e7864e2f72ad319ee892", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
