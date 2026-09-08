---
name: "rar-cowork-cookbook-report-negotiate-project-contracts"
description: "Builds a read-only summary report of negotiate project contracts activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_negotiate_project_contracts", "rar_sha256": "274ce32f06c7c8c589a87e6f5bc8b5754acd43ee31aff834e8883742cbb075bc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
