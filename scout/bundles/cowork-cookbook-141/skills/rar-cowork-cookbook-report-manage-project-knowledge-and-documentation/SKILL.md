---
name: "rar-cowork-cookbook-report-manage-project-knowledge-and-documentation"
description: "Builds a read-only summary report of manage project knowledge and documentation activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 she"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_project_knowledge_and_documentation", "rar_sha256": "cb82e89d5b0621ed8b8b58d09fbf1067b71c3d3d392d3a7f311f6d376901dd5b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_project_knowledge_and_documentation`. The original RAPP
agent is preserved byte-for-byte in `report_manage_project_knowledge_and_documentation_agent.py` and in the RCI capsule.

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

Manage project knowledge and documentation Summary Report — Builds a read-only summary report of manage project knowledge and documentation activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 she

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-project-knowledge-and-documentation
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
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-project-knowledge-and-documentation-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_project_knowledge_and_documentation_agent.py` and embedded as the fenced Python below (sha256 cb82e89d5b0621ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_project_knowledge_and_documentation_agent.py` first:

```bash
python3 report_manage_project_knowledge_and_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_project_knowledge_and_documentation_agent.py   # or on stdin
python3 report_manage_project_knowledge_and_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project knowledge and documentation Summary Report — Builds a read-only summary report of manage project knowledge and documentation activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 she

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-project-knowledge-and-documentation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_project_knowledge_and_documentation',
    "version": '3.0.3',
    "display_name": 'Manage project knowledge and documentation Summary Report',
    "description": 'Builds a read-only summary report of manage project knowledge and documentation activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 she',
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
        "upstream_slug": 'report-manage-project-knowledge-and-documentation',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-project-knowledge-and-documentation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '930dec6197d1e392',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/manage-project-knowledge-and-documentation'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-manage-project-knowledge-and-documentation', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-project-knowledge-and-documentation-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage project knowledge and documentation stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage project knowledge and documentation for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-project-knowledge-and-documentation-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage project knowledge and documentation records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of manage project knowledge and documentation activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 she', 'example_request': 'Build a summary report of manage project knowledge and documentation for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-project-knowledge-and-documentation-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of manage project knowledge and documentation activity from D365 ERP data, exported to Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageProjectKnowledgeAndDocumentation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageProjectKnowledgeAndDocumentation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-project-knowledge-and-documentation-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageProjectKnowledgeAndDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
