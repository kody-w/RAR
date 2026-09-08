---
name: "rar-cowork-cookbook-audit-monitor-system-performance-and-health"
description: "Runs a read-only completeness audit of system performance and health monitoring records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_system_performance_and_health", "rar_sha256": "2adb45c3ffa05f559c55b44fd4329e879a506286f230a97b616ea0844d800e8f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_monitor_system_performance_and_health`. The original RAPP
agent is preserved byte-for-byte in `audit_monitor_system_performance_and_health_agent.py` and in the RCI capsule.

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

Monitor system performance and health Completeness Audit — Runs a read-only completeness audit of system performance and health monitoring records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-system-performance-and-health
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
      "description": "Name of the Excel workbook to produce, e.g. audit-monitor-system-performance-and-health-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_monitor_system_performance_and_health_agent.py` and embedded as the fenced Python below (sha256 2adb45c3ffa05f55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_monitor_system_performance_and_health_agent.py` first:

```bash
python3 audit_monitor_system_performance_and_health_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_monitor_system_performance_and_health_agent.py   # or on stdin
python3 audit_monitor_system_performance_and_health_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor system performance and health Completeness Audit — Runs a read-only completeness audit of system performance and health monitoring records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-system-performance-and-health
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_monitor_system_performance_and_health',
    "version": '3.0.3',
    "display_name": 'Monitor system performance and health Completeness Audit',
    "description": 'Runs a read-only completeness audit of system performance and health monitoring records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-monitor-system-performance-and-health',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-monitor-system-performance-and-health',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9817eb027f794ffe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-system-performance-and-health'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-monitor-system-performance-and-health', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-monitor-system-performance-and-health-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit monitor system performance and health records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to monitor system performance and health. Output an Excel workbook 'audit-monitor-system-performance-and-health-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no monitor system performance and health data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-04', 'what_it_does': 'Reads monitor system performance and health records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness audit of system performance and health monitoring records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.', 'example_request': 'Audit monitor system performance and health records in USMF for completeness and give me the Excel findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-monitor-system-performance-and-health-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to check monitoring records for missing fields, stale dates, blank descriptions, inactive references, or policy violations without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditMonitorSystemPerformanceAndHealth(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMonitorSystemPerformanceAndHealth'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-monitor-system-performance-and-health-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditMonitorSystemPerformanceAndHealth().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
