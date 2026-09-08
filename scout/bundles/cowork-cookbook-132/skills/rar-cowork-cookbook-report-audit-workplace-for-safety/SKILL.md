---
name: "rar-cowork-cookbook-report-audit-workplace-for-safety"
description: "Generates a read-only workplace safety audit summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_audit_workplace_for_safety", "rar_sha256": "1cd1d9780298ebbecc0236dcb4dfd365a3b026db6f19c99412eebaa3299d04ec", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
