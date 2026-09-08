---
name: "rar-cowork-cookbook-audit-monitor-financial-performance"
description: "Audits monitor-financial-performance records in a Dynamics 365 F&SCM legal entity for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_financial_performance", "rar_sha256": "897f72288dfb87fafbbf00a155c871decfa86ff076a560102767ceecbbd31000", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
