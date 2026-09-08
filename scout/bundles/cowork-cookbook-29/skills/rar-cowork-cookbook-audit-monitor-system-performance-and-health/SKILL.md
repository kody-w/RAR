---
name: "rar-cowork-cookbook-audit-monitor-system-performance-and-health"
description: "Runs a read-only completeness audit of system performance and health monitoring records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_system_performance_and_health", "rar_sha256": "2adb45c3ffa05f559c55b44fd4329e879a506286f230a97b616ea0844d800e8f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
