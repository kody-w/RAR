---
name: "rar-cowork-cookbook-report-negotiate-project-contracts"
description: "Builds a read-only summary report of negotiate project contracts activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_negotiate_project_contracts", "rar_sha256": "274ce32f06c7c8c589a87e6f5bc8b5754acd43ee31aff834e8883742cbb075bc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_negotiate_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `report_negotiate_project_contracts_agent.py` and in the RCI capsule.

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

Negotiate project contracts Summary Report — Builds a read-only summary report of negotiate project contracts activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-negotiate-project-contracts
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
      "description": "Name of the Excel workbook to produce, e.g. report-negotiate-project-contracts-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_negotiate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 274ce32f06c7c8c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_negotiate_project_contracts_agent.py` first:

```bash
python3 report_negotiate_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_negotiate_project_contracts_agent.py   # or on stdin
python3 report_negotiate_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Negotiate project contracts Summary Report — Builds a read-only summary report of negotiate project contracts activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-negotiate-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_negotiate_project_contracts',
    "version": '3.0.3',
    "display_name": 'Negotiate project contracts Summary Report',
    "description": 'Builds a read-only summary report of negotiate project contracts activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-negotiate-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-negotiate-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '73ca9616ab3a5a9f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/negotiate-project-contracts'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-negotiate-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-negotiate-project-contracts-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where negotiate project contracts stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of negotiate project contracts for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-negotiate-project-contracts-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads negotiate project contracts records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of negotiate project contracts activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a negotiate project contracts summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-negotiate-project-contracts-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals, breakdown, and Top 10 by value report of negotiate project contracts activity from D365 ERP data, with no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportNegotiateProjectContracts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportNegotiateProjectContracts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-negotiate-project-contracts-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportNegotiateProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
