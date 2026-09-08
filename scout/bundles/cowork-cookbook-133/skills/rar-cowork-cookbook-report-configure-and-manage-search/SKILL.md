---
name: "rar-cowork-cookbook-report-configure-and-manage-search"
description: "Builds a read-only summary report of configure and manage search activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_search", "rar_sha256": "ea99b24d37329d0c39ecdaf2ceeb0874fcb5b0d3c79b3e053f1bdedaabfdea53", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_configure_and_manage_search`. The original RAPP
agent is preserved byte-for-byte in `report_configure_and_manage_search_agent.py` and in the RCI capsule.

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

Configure and manage search Summary Report — Builds a read-only summary report of configure and manage search activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-search
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
      "description": "Name of the Excel workbook to produce, e.g. report-configure-and-manage-search-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_and_manage_search_agent.py` and embedded as the fenced Python below (sha256 ea99b24d37329d0c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_and_manage_search_agent.py` first:

```bash
python3 report_configure_and_manage_search_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_configure_and_manage_search_agent.py   # or on stdin
python3 report_configure_and_manage_search_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage search Summary Report — Builds a read-only summary report of configure and manage search activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-search
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_configure_and_manage_search',
    "version": '3.0.3',
    "display_name": 'Configure and manage search Summary Report',
    "description": 'Builds a read-only summary report of configure and manage search activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-configure-and-manage-search',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-configure-and-manage-search',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f95f216efcda25ac',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-search'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-configure-and-manage-search', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-configure-and-manage-search-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where configure and manage search stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of configure and manage search for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-configure-and-manage-search-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage search records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of configure and manage search activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a configure and manage search summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-configure-and-manage-search-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a configure and manage search summary report from D365 ERP data with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportConfigureAndManageSearch(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConfigureAndManageSearch'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-configure-and-manage-search-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportConfigureAndManageSearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
