---
name: "rar-cowork-cookbook-report-audit-workplace-for-safety"
description: "Generates a read-only workplace safety audit summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_audit_workplace_for_safety", "rar_sha256": "1cd1d9780298ebbecc0236dcb4dfd365a3b026db6f19c99412eebaa3299d04ec", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_audit_workplace_for_safety`. The original RAPP
agent is preserved byte-for-byte in `report_audit_workplace_for_safety_agent.py` and in the RCI capsule.

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

Audit workplace for safety Summary Report — Generates a read-only workplace safety audit summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-audit-workplace-for-safety
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
    "breakdown_dimensions": {
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-audit-workplace-for-safety-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_audit_workplace_for_safety_agent.py` and embedded as the fenced Python below (sha256 1cd1d9780298ebbe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_audit_workplace_for_safety_agent.py` first:

```bash
python3 report_audit_workplace_for_safety_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_audit_workplace_for_safety_agent.py   # or on stdin
python3 report_audit_workplace_for_safety_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit workplace for safety Summary Report — Generates a read-only workplace safety audit summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-audit-workplace-for-safety
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_audit_workplace_for_safety',
    "version": '3.0.3',
    "display_name": 'Audit workplace for safety Summary Report',
    "description": 'Generates a read-only workplace safety audit summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-audit-workplace-for-safety',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-audit-workplace-for-safety',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e7e1a2cb87d83146',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/audit-workplace-for-safety'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-audit-workplace-for-safety', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-audit-workplace-for-safety-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where audit workplace for safety stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of audit workplace for safety for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-audit-workplace-for-safety-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads audit workplace for safety records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only workplace safety audit summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a safety audit summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-audit-workplace-for-safety-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a safety audit summary with totals, by-dimension breakdowns, and a Top 10 by value list exported to Excel from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportAuditWorkplaceForSafety(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAuditWorkplaceForSafety'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-audit-workplace-for-safety-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportAuditWorkplaceForSafety().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
