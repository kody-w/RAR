---
name: "rar-cowork-cookbook-audit-plan-service-operations"
description: "Runs a read-only completeness and policy audit of plan service operations records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook of findings by category with a summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_service_operations", "rar_sha256": "500cc4bd5a9bd29e6929dbd2588446ca5cece65be26f2da83ef189453d40a1fc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_service_operations`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_service_operations_agent.py` and in the RCI capsule.

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

Plan service operations Completeness Audit — Runs a read-only completeness and policy audit of plan service operations records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook of findings by category with a summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-service-operations
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
      "description": "Date range for stale-date checks; adjust for demo data vintage (USMF is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-plan-service-operations-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_service_operations_agent.py` and embedded as the fenced Python below (sha256 500cc4bd5a9bd29e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_service_operations_agent.py` first:

```bash
python3 audit_plan_service_operations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_service_operations_agent.py   # or on stdin
python3 audit_plan_service_operations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service operations Completeness Audit — Runs a read-only completeness and policy audit of plan service operations records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook of findings by category with a summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-service-operations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_service_operations',
    "version": '3.0.3',
    "display_name": 'Plan service operations Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of plan service operations records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook of findings by category with a summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-service-operations',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-service-operations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7aeb5dc75f851444',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-service-operations'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-plan-service-operations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for stale-date checks; adjust for demo data vintage (USMF is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-plan-service-operations-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit plan service operations records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to plan service operations. Output an Excel workbook 'audit-plan-service-operations-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no plan service operations data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan service operations records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of plan service operations records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook of findings by category with a summary sheet.', 'example_request': 'Audit plan service operations in USMF for completeness and give me an Excel workbook of the findings.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for stale-date checks; adjust for demo data vintage (USMF is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-service-operations-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants plan service operations records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPlanServiceOperations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanServiceOperations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for stale-date checks; adjust for demo data vintage (USMF is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-service-operations-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPlanServiceOperations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
