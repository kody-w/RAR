---
name: "rar-cowork-cookbook-audit-monitor-regulatory-compliance"
description: "Read-only audit of monitor regulatory compliance records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, output as an Excel work"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_regulatory_compliance", "rar_sha256": "294a33e69b051708da2bec233ea89bee223f995c10bcdcfc65f567002ba79455", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
