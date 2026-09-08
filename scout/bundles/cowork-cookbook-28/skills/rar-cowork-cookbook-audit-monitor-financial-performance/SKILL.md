---
name: "rar-cowork-cookbook-audit-monitor-financial-performance"
description: "Audits monitor-financial-performance records in a Dynamics 365 F&SCM legal entity for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_financial_performance", "rar_sha256": "897f72288dfb87fafbbf00a155c871decfa86ff076a560102767ceecbbd31000", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_monitor_financial_performance`. The original RAPP
agent is preserved byte-for-byte in `audit_monitor_financial_performance_agent.py` and in the RCI capsule.

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

Monitor financial performance Completeness Audit — Audits monitor-financial-performance records in a Dynamics 365 F&SCM legal entity for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-financial-performance
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
      "description": "Date range used to judge stale dates; note USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-monitor-financial-performance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_monitor_financial_performance_agent.py` and embedded as the fenced Python below (sha256 897f72288dfb87fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_monitor_financial_performance_agent.py` first:

```bash
python3 audit_monitor_financial_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_monitor_financial_performance_agent.py   # or on stdin
python3 audit_monitor_financial_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor financial performance Completeness Audit — Audits monitor-financial-performance records in a Dynamics 365 F&SCM legal entity for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-financial-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_monitor_financial_performance',
    "version": '3.0.3',
    "display_name": 'Monitor financial performance Completeness Audit',
    "description": 'Audits monitor-financial-performance records in a Dynamics 365 F&SCM legal entity for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workbo',
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
        "upstream_slug": 'audit-monitor-financial-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-monitor-financial-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a6c5d87189cc7973',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/monitor-financial-performance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-monitor-financial-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; note USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-monitor-financial-performance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit monitor financial performance records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to monitor financial performance. Output an Excel workbook 'audit-monitor-financial-performance-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no monitor financial performance data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor financial performance records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits monitor-financial-performance records in a Dynamics 365 F&SCM legal entity for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workbo', 'example_request': 'Audit monitor financial performance records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; note USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-monitor-financial-performance-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of monitor financial performance data in Dynamics 365 ERP, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditMonitorFinancialPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMonitorFinancialPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; note USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-monitor-financial-performance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditMonitorFinancialPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
