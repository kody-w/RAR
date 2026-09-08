---
name: "rar-cowork-cookbook-report-configure-and-manage-search"
description: "Builds a read-only summary report of configure and manage search activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_search", "rar_sha256": "ea99b24d37329d0c39ecdaf2ceeb0874fcb5b0d3c79b3e053f1bdedaabfdea53", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
