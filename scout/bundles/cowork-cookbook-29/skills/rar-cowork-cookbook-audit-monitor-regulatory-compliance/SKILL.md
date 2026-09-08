---
name: "rar-cowork-cookbook-audit-monitor-regulatory-compliance"
description: "Read-only audit of monitor regulatory compliance records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, output as an Excel work"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_regulatory_compliance", "rar_sha256": "294a33e69b051708da2bec233ea89bee223f995c10bcdcfc65f567002ba79455", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_monitor_regulatory_compliance`. The original RAPP
agent is preserved byte-for-byte in `audit_monitor_regulatory_compliance_agent.py` and in the RCI capsule.

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

Monitor regulatory compliance Completeness Audit — Read-only audit of monitor regulatory compliance records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, output as an Excel work

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-regulatory-compliance
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
      "description": "Date range used to judge stale records; adjust for demo data that is mostly FY2017.",
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
      "description": "Excel workbook name, e.g. audit-monitor-regulatory-compliance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_monitor_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 294a33e69b051708…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_monitor_regulatory_compliance_agent.py` first:

```bash
python3 audit_monitor_regulatory_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_monitor_regulatory_compliance_agent.py   # or on stdin
python3 audit_monitor_regulatory_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor regulatory compliance Completeness Audit — Read-only audit of monitor regulatory compliance records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, output as an Excel work

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-regulatory-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_monitor_regulatory_compliance',
    "version": '3.0.3',
    "display_name": 'Monitor regulatory compliance Completeness Audit',
    "description": 'Read-only audit of monitor regulatory compliance records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, output as an Excel work',
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
        "upstream_slug": 'audit-monitor-regulatory-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-monitor-regulatory-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3cd5218712f2a4d0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-regulatory-compliance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-monitor-regulatory-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale records; adjust for demo data that is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. audit-monitor-regulatory-compliance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit monitor regulatory compliance records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to monitor regulatory compliance. Output an Excel workbook 'audit-monitor-regulatory-compliance-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no monitor regulatory compliance data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads monitor regulatory compliance records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of monitor regulatory compliance records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, output as an Excel work', 'example_request': 'Audit monitor regulatory compliance records in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale records; adjust for demo data that is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-monitor-regulatory-compliance-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance audit of monitor regulatory compliance data in D365 F&SCM, delivered as a multi-sheet Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditMonitorRegulatoryCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMonitorRegulatoryCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale records; adjust for demo data that is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-monitor-regulatory-compliance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditMonitorRegulatoryCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
