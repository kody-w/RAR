---
name: "rar-cowork-cookbook-audit-forecast-cash-flow"
description: "Read-only audit of Dynamics 365 forecast cash flow records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations; returns an Excel workbook with a sh"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_forecast_cash_flow", "rar_sha256": "aa18e8e21a629a32986f4ff8d88ea8ae1a3f32bb7054baa548e79dd8d2ed2c28", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_forecast_cash_flow`. The original RAPP
agent is preserved byte-for-byte in `audit_forecast_cash_flow_agent.py` and in the RCI capsule.

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

Forecast cash flow Completeness Audit — Read-only audit of Dynamics 365 forecast cash flow records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations; returns an Excel workbook with a sh

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-cash-flow
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
      "description": "Date range for staleness checks; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-forecast-cash-flow-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_forecast_cash_flow_agent.py` and embedded as the fenced Python below (sha256 aa18e8e21a629a32…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_forecast_cash_flow_agent.py` first:

```bash
python3 audit_forecast_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_forecast_cash_flow_agent.py   # or on stdin
python3 audit_forecast_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast cash flow Completeness Audit — Read-only audit of Dynamics 365 forecast cash flow records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations; returns an Excel workbook with a sh

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_forecast_cash_flow',
    "version": '3.0.2',
    "display_name": 'Forecast cash flow Completeness Audit',
    "description": 'Read-only audit of Dynamics 365 forecast cash flow records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations; returns an Excel workbook with a sh',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-forecast-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-forecast-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2256c3d37957e241',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/forecast-cash-flow'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-forecast-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-forecast-cash-flow-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit forecast cash flow records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to forecast cash flow. Output an Excel workbook 'audit-forecast-cash-flow-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no forecast cash flow data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads forecast cash flow records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of Dynamics 365 forecast cash flow records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations; returns an Excel workbook with a sh', 'example_request': 'Audit forecast cash flow records in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-forecast-cash-flow-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness/policy compliance audit of forecast cash flow records in Dynamics 365 F&SCM, delivered as an Excel workbook, without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditForecastCashFlow(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditForecastCashFlow'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-forecast-cash-flow-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditForecastCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
