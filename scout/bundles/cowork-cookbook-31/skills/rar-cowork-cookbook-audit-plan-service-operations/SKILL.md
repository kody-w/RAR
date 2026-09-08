---
name: "rar-cowork-cookbook-audit-plan-service-operations"
description: "Runs a read-only completeness and policy audit of plan service operations records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook of findings by category with a summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_service_operations", "rar_sha256": "500cc4bd5a9bd29e6929dbd2588446ca5cece65be26f2da83ef189453d40a1fc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
