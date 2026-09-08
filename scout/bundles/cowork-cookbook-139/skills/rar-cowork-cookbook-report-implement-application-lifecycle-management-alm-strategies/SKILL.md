---
name: "rar-cowork-cookbook-report-implement-application-lifecycle-management-alm-strategies"
description: "Builds a read-only ALM strategy summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_implement_application_lifecycle_management_alm_strategies", "rar_sha256": "0797092d5bfe1dcc78e4da7a4e387f10e9130a73937d30a58200feb1b2c8266b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_implement_application_lifecycle_management_alm_strategies`. The original RAPP
agent is preserved byte-for-byte in `report_implement_application_lifecycle_management_alm_strategies_agent.py` and in the RCI capsule.

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

Implement application lifecycle management (ALM) strategies Summary Report — Builds a read-only ALM strategy summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-implement-application-lifecycle-management-alm-strategies
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
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-implement-application-lifecycle-management-alm-strategies-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_implement_application_lifecycle_management_alm_strategies_agent.py` and embedded as the fenced Python below (sha256 0797092d5bfe1dcc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_implement_application_lifecycle_management_alm_strategies_agent.py` first:

```bash
python3 report_implement_application_lifecycle_management_alm_strategies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_implement_application_lifecycle_management_alm_strategies_agent.py   # or on stdin
python3 report_implement_application_lifecycle_management_alm_strategies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement application lifecycle management (ALM) strategies Summary Report — Builds a read-only ALM strategy summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-implement-application-lifecycle-management-alm-strategies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_implement_application_lifecycle_management_alm_strategies',
    "version": '3.0.3',
    "display_name": 'Implement application lifecycle management (ALM) strategies Summary Report',
    "description": 'Builds a read-only ALM strategy summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-implement-application-lifecycle-management-alm-strategies',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-implement-application-lifecycle-management-alm-strategies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a3ca0162a63cea02',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-application-lifecycle-management-alm-strategies'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-implement-application-lifecycle-management-alm-strategies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-implement-application-lifecycle-management-alm-strategies-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where implement application lifecycle management (ALM) strategies stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of implement application lifecycle management (ALM) strategies for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-implement-application-lifecycle-management-alm-strategies-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads implement application lifecycle management (ALM) strategies records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only ALM strategy summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build an ALM summary report for USMF from the latest posted period as an Excel workbook with Summary, Detail, and Top10 sheets.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-implement-application-lifecycle-management-alm-strategies-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary report of ALM activity with totals, dimension breakdowns, and a Top 10 by value list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportImplementApplicationLifecycleManagementAlmStrategies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportImplementApplicationLifecycleManagementAlmStrategies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-implement-application-lifecycle-management-alm-strategies-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportImplementApplicationLifecycleManagementAlmStrategies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
