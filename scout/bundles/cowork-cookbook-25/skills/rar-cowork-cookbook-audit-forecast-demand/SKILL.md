---
name: "rar-cowork-cookbook-audit-forecast-demand"
description: "Runs a read-only completeness and policy audit of Dynamics 365 forecast demand records for a legal entity, returning an Excel workbook with a sheet per finding category and a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_forecast_demand", "rar_sha256": "99117e89c675879a673830188d20e90f0cc0e762a68dc82024056e890318eded", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_forecast_demand`. The original RAPP
agent is preserved byte-for-byte in `audit_forecast_demand_agent.py` and in the RCI capsule.

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

Forecast demand Completeness Audit — Runs a read-only completeness and policy audit of Dynamics 365 forecast demand records for a legal entity, returning an Excel workbook with a sheet per finding category and a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-demand
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
      "description": "Name of the Excel workbook to produce, e.g. audit-forecast-demand-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_forecast_demand_agent.py` and embedded as the fenced Python below (sha256 99117e89c675879a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_forecast_demand_agent.py` first:

```bash
python3 audit_forecast_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_forecast_demand_agent.py   # or on stdin
python3 audit_forecast_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast demand Completeness Audit — Runs a read-only completeness and policy audit of Dynamics 365 forecast demand records for a legal entity, returning an Excel workbook with a sheet per finding category and a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_forecast_demand',
    "version": '3.0.2',
    "display_name": 'Forecast demand Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of Dynamics 365 forecast demand records for a legal entity, returning an Excel workbook with a sheet per finding category and a Summary sheet of counts.',
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
        "upstream_slug": 'audit-forecast-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-forecast-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b19aea20c5f26eb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/forecast-demand'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-forecast-demand', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-forecast-demand-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit forecast demand records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to forecast demand. Output an Excel workbook 'audit-forecast-demand-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no forecast demand data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast demand records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of Dynamics 365 forecast demand records for a legal entity, returning an Excel workbook with a sheet per finding category and a Summary sheet of counts.', 'example_request': 'Audit forecast demand in USMF for completeness and give me an Excel workbook of the findings.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-forecast-demand-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants forecast demand records in D365 F&SCM checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditForecastDemand(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditForecastDemand'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-forecast-demand-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditForecastDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
