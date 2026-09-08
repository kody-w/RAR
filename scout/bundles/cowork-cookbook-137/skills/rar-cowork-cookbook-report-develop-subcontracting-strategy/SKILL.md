---
name: "rar-cowork-cookbook-report-develop-subcontracting-strategy"
description: "Builds a read-only subcontracting strategy summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_subcontracting_strategy", "rar_sha256": "d6d27bee3cc644510108ce85ac0a7c9e13097598897ec067646840cb0e6beca4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
