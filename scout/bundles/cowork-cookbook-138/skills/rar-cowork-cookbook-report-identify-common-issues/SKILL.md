---
name: "rar-cowork-cookbook-report-identify-common-issues"
description: "Builds a read-only summary report of common issues from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_common_issues", "rar_sha256": "6e332706963a1501a48f5a42c2655b06c867a9eddb5250364fce75f25a2c7964", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
