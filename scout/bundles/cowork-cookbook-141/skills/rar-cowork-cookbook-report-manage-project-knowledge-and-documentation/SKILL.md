---
name: "rar-cowork-cookbook-report-manage-project-knowledge-and-documentation"
description: "Builds a read-only summary report of manage project knowledge and documentation activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 she"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_project_knowledge_and_documentation", "rar_sha256": "cb82e89d5b0621ed8b8b58d09fbf1067b71c3d3d392d3a7f311f6d376901dd5b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
