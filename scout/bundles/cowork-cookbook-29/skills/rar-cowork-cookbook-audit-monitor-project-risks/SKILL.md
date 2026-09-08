---
name: "rar-cowork-cookbook-audit-monitor-project-risks"
description: "Read-only audit of monitor project risks records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) that returns an Excel workbook flagging missing fields, stale dates, blank descriptions, inactive references, and po"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_project_risks", "rar_sha256": "ba046f806656b7d50f8f395606083e2f9d1b828c88c7a8e9c8106873cafc6f77", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_monitor_project_risks`. The original RAPP
agent is preserved byte-for-byte in `audit_monitor_project_risks_agent.py` and in the RCI capsule.

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

Monitor project risks Completeness Audit — Read-only audit of monitor project risks records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) that returns an Excel workbook flagging missing fields, stale dates, blank descriptions, inactive references, and po

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-project-risks
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
      "description": "Excel workbook name, e.g. audit-monitor-project-risks-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_monitor_project_risks_agent.py` and embedded as the fenced Python below (sha256 ba046f806656b7d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_monitor_project_risks_agent.py` first:

```bash
python3 audit_monitor_project_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_monitor_project_risks_agent.py   # or on stdin
python3 audit_monitor_project_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor project risks Completeness Audit — Read-only audit of monitor project risks records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) that returns an Excel workbook flagging missing fields, stale dates, blank descriptions, inactive references, and po

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-project-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_monitor_project_risks',
    "version": '3.0.3',
    "display_name": 'Monitor project risks Completeness Audit',
    "description": 'Read-only audit of monitor project risks records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) that returns an Excel workbook flagging missing fields, stale dates, blank descriptions, inactive references, and po',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-monitor-project-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-monitor-project-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93e0e7c3b565e7bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/monitor-project-risks'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-monitor-project-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. audit-monitor-project-risks-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit monitor project risks records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to monitor project risks. Output an Excel workbook 'audit-monitor-project-risks-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no monitor project risks data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor project risks records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of monitor project risks records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) that returns an Excel workbook flagging missing fields, stale dates, blank descriptions, inactive references, and po', 'example_request': 'Audit monitor project risks in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-monitor-project-risks-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a completeness and policy-compliance check on monitor project risks records in a D365 legal entity, with findings exported to Excel and no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditMonitorProjectRisks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMonitorProjectRisks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-monitor-project-risks-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditMonitorProjectRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
