---
name: "rar-cowork-cookbook-report-define-integration-strategy"
description: "Builds a read-only summary report of define integration strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_integration_strategy", "rar_sha256": "378fb1a23b77d2b48142b1446807e89c621d7bb696bfa464ed4b401da2693510", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_integration_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_define_integration_strategy_agent.py` and in the RCI capsule.

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

Define integration strategy Summary Report — Builds a read-only summary report of define integration strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-integration-strategy
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-define-integration-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_integration_strategy_agent.py` and embedded as the fenced Python below (sha256 378fb1a23b77d2b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_integration_strategy_agent.py` first:

```bash
python3 report_define_integration_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_integration_strategy_agent.py   # or on stdin
python3 report_define_integration_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define integration strategy Summary Report — Builds a read-only summary report of define integration strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-integration-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_integration_strategy',
    "version": '3.0.3',
    "display_name": 'Define integration strategy Summary Report',
    "description": 'Builds a read-only summary report of define integration strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-define-integration-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-integration-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fb3d3a50de41a329',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-integration-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-define-integration-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-define-integration-strategy-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define integration strategy stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define integration strategy for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-integration-strategy-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define integration strategy records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of define integration strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a define integration strategy summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-define-integration-strategy-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write define integration strategy summary from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineIntegrationStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineIntegrationStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-define-integration-strategy-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDefineIntegrationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
