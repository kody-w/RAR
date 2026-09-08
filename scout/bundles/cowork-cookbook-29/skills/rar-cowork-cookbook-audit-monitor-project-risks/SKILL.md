---
name: "rar-cowork-cookbook-audit-monitor-project-risks"
description: "Read-only audit of monitor project risks records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) that returns an Excel workbook flagging missing fields, stale dates, blank descriptions, inactive references, and po"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_project_risks", "rar_sha256": "ba046f806656b7d50f8f395606083e2f9d1b828c88c7a8e9c8106873cafc6f77", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
