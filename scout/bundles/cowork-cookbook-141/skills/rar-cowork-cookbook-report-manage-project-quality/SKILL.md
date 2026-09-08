---
name: "rar-cowork-cookbook-report-manage-project-quality"
description: "Builds a read-only manage project quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_project_quality", "rar_sha256": "90e4dff32fb78fe723bc8762debc983eb60805b8891ec79300e0c79d31052983", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_project_quality`. The original RAPP
agent is preserved byte-for-byte in `report_manage_project_quality_agent.py` and in the RCI capsule.

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

Manage project quality Summary Report — Builds a read-only manage project quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-project-quality
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
      "description": "Dimensions for breakdowns where applicable: department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Excel workbook name, e.g. report-manage-project-quality-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_project_quality_agent.py` and embedded as the fenced Python below (sha256 90e4dff32fb78fe7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_project_quality_agent.py` first:

```bash
python3 report_manage_project_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_project_quality_agent.py   # or on stdin
python3 report_manage_project_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project quality Summary Report — Builds a read-only manage project quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-project-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_project_quality',
    "version": '3.0.3',
    "display_name": 'Manage project quality Summary Report',
    "description": 'Builds a read-only manage project quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-project-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-project-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6af6814bc75afba9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/manage-project-quality'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-manage-project-quality', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-manage-project-quality-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage project quality stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage project quality for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-project-quality-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage project quality records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only manage project quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a manage project quality summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-manage-project-quality-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a caller wants a no-write summary of manage project quality activity with totals, by-dimension breakdowns, and a Top 10 by value list from D365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageProjectQuality(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageProjectQuality'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-manage-project-quality-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageProjectQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
