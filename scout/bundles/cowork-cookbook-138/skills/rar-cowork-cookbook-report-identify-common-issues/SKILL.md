---
name: "rar-cowork-cookbook-report-identify-common-issues"
description: "Builds a read-only summary report of common issues from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_common_issues", "rar_sha256": "6e332706963a1501a48f5a42c2655b06c867a9eddb5250364fce75f25a2c7964", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_identify_common_issues`. The original RAPP
agent is preserved byte-for-byte in `report_identify_common_issues_agent.py` and in the RCI capsule.

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

Identify common issues Summary Report — Builds a read-only summary report of common issues from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-common-issues
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-identify-common-issues-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_common_issues_agent.py` and embedded as the fenced Python below (sha256 6e332706963a1501…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_common_issues_agent.py` first:

```bash
python3 report_identify_common_issues_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_identify_common_issues_agent.py   # or on stdin
python3 report_identify_common_issues_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify common issues Summary Report — Builds a read-only summary report of common issues from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-common-issues
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_identify_common_issues',
    "version": '3.0.3',
    "display_name": 'Identify common issues Summary Report',
    "description": "Builds a read-only summary report of common issues from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-identify-common-issues',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-identify-common-issues',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b925ae2974de2050',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/identify-common-issues'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-identify-common-issues', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-identify-common-issues-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where identify common issues stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of identify common issues for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-identify-common-issues-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify common issues records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only summary report of common issues from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.", 'example_request': "Build the identify common issues summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-identify-common-issues-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary of common issues with totals, dimension breakdowns, and a Top 10 by value list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportIdentifyCommonIssues(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIdentifyCommonIssues'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-identify-common-issues-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportIdentifyCommonIssues().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
