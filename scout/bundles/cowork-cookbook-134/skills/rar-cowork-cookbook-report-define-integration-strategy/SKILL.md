---
name: "rar-cowork-cookbook-report-define-integration-strategy"
description: "Builds a read-only summary report of define integration strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_integration_strategy", "rar_sha256": "378fb1a23b77d2b48142b1446807e89c621d7bb696bfa464ed4b401da2693510", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
