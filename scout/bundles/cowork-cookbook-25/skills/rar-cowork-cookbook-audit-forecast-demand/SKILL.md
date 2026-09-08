---
name: "rar-cowork-cookbook-audit-forecast-demand"
description: "Runs a read-only completeness and policy audit of Dynamics 365 forecast demand records for a legal entity, returning an Excel workbook with a sheet per finding category and a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_forecast_demand", "rar_sha256": "99117e89c675879a673830188d20e90f0cc0e762a68dc82024056e890318eded", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
