---
name: "rar-cowork-cookbook-report-develop-subcontracting-strategy"
description: "Builds a read-only subcontracting strategy summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_subcontracting_strategy", "rar_sha256": "d6d27bee3cc644510108ce85ac0a7c9e13097598897ec067646840cb0e6beca4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_subcontracting_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_develop_subcontracting_strategy_agent.py` and in the RCI capsule.

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

Develop subcontracting strategy Summary Report — Builds a read-only subcontracting strategy summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-subcontracting-strategy
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
      "description": "Name of the Excel workbook to produce, e.g. report-develop-subcontracting-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_subcontracting_strategy_agent.py` and embedded as the fenced Python below (sha256 d6d27bee3cc64451…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_subcontracting_strategy_agent.py` first:

```bash
python3 report_develop_subcontracting_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_subcontracting_strategy_agent.py   # or on stdin
python3 report_develop_subcontracting_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop subcontracting strategy Summary Report — Builds a read-only subcontracting strategy summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-subcontracting-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_subcontracting_strategy',
    "version": '3.0.3',
    "display_name": 'Develop subcontracting strategy Summary Report',
    "description": 'Builds a read-only subcontracting strategy summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-subcontracting-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-subcontracting-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bbcf711102bf41f4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/develop-subcontracting-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-develop-subcontracting-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-develop-subcontracting-strategy-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where develop subcontracting strategy stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of develop subcontracting strategy for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-develop-subcontracting-strategy-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop subcontracting strategy records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only subcontracting strategy summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a subcontracting strategy summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-develop-subcontracting-strategy-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown summary report of develop subcontracting strategy activity from D365 ERP data, output as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDevelopSubcontractingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopSubcontractingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-develop-subcontracting-strategy-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDevelopSubcontractingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
