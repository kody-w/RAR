---
name: "rar-cowork-cookbook-report-define-learning-paths"
description: "Builds a read-only summary report of define learning paths activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_learning_paths", "rar_sha256": "7527892435badb5f2c8cac26029bf8258a03294ab8a1b57362c410da1fa400e9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_learning_paths`. The original RAPP
agent is preserved byte-for-byte in `report_define_learning_paths_agent.py` and in the RCI capsule.

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

Define learning paths Summary Report — Builds a read-only summary report of define learning paths activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-learning-paths
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner.",
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
      "description": "Excel workbook name, e.g. report-define-learning-paths-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_learning_paths_agent.py` and embedded as the fenced Python below (sha256 7527892435badb5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_learning_paths_agent.py` first:

```bash
python3 report_define_learning_paths_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_learning_paths_agent.py   # or on stdin
python3 report_define_learning_paths_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define learning paths Summary Report — Builds a read-only summary report of define learning paths activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-learning-paths
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_learning_paths',
    "version": '3.0.3',
    "display_name": 'Define learning paths Summary Report',
    "description": 'Builds a read-only summary report of define learning paths activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-define-learning-paths',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-learning-paths',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '964df06bf1c3a1f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/define-learning-paths'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-define-learning-paths', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-define-learning-paths-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define learning paths stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define learning paths for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-learning-paths-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define learning paths records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of define learning paths activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a define learning paths summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-define-learning-paths-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of define learning paths from D365 ERP data, exported to Excel without modifying any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineLearningPaths(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineLearningPaths'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-define-learning-paths-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDefineLearningPaths().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
