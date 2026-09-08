---
name: "rar-cowork-cookbook-report-implement-application-lifecycle-management-alm-strategies"
description: "Builds a read-only ALM strategy summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_implement_application_lifecycle_management_alm_strategies", "rar_sha256": "0797092d5bfe1dcc78e4da7a4e387f10e9130a73937d30a58200feb1b2c8266b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
