---
name: "rar-cowork-cookbook-report-conduct-root-cause-analysis"
description: "Builds a read-only conduct root cause analysis summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_root_cause_analysis", "rar_sha256": "fb3efa4e28633837034c7247cbfe6a414a9c4ab6c5f333ff87027f4a184cc8c9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_conduct_root_cause_analysis`. The original RAPP
agent is preserved byte-for-byte in `report_conduct_root_cause_analysis_agent.py` and in the RCI capsule.

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

Conduct root cause analysis Summary Report — Builds a read-only conduct root cause analysis summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-root-cause-analysis
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
      "description": "Name of the Excel workbook to produce, e.g. report-conduct-root-cause-analysis-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_root_cause_analysis_agent.py` and embedded as the fenced Python below (sha256 fb3efa4e28633837…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_root_cause_analysis_agent.py` first:

```bash
python3 report_conduct_root_cause_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_conduct_root_cause_analysis_agent.py   # or on stdin
python3 report_conduct_root_cause_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct root cause analysis Summary Report — Builds a read-only conduct root cause analysis summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-root-cause-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_conduct_root_cause_analysis',
    "version": '3.0.3',
    "display_name": 'Conduct root cause analysis Summary Report',
    "description": 'Builds a read-only conduct root cause analysis summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-conduct-root-cause-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-conduct-root-cause-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2fa167651fc9b95c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/conduct-root-cause-analysis'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-conduct-root-cause-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-conduct-root-cause-analysis-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where conduct root cause analysis stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of conduct root cause analysis for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-conduct-root-cause-analysis-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct root cause analysis records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only conduct root cause analysis summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a conduct root cause analysis summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-conduct-root-cause-analysis-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a conduct root cause analysis summary with totals, by-dimension breakdowns, and a Top 10 by value list from D365 ERP data, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportConductRootCauseAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConductRootCauseAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-conduct-root-cause-analysis-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportConductRootCauseAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
