---
name: "rar-cowork-cookbook-report-define-environment-strategy"
description: "Builds a read-only summary report of define environment strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_environment_strategy", "rar_sha256": "9c85f68c134374ed6850054f006b044c118b4c6c1c640e496727fdda65338efe", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_environment_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_define_environment_strategy_agent.py` and in the RCI capsule.

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

Define environment strategy Summary Report — Builds a read-only summary report of define environment strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-environment-strategy
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
      "description": "Excel workbook name, e.g. report-define-environment-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_environment_strategy_agent.py` and embedded as the fenced Python below (sha256 9c85f68c134374ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_environment_strategy_agent.py` first:

```bash
python3 report_define_environment_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_environment_strategy_agent.py   # or on stdin
python3 report_define_environment_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define environment strategy Summary Report — Builds a read-only summary report of define environment strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-environment-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_environment_strategy',
    "version": '3.0.3',
    "display_name": 'Define environment strategy Summary Report',
    "description": 'Builds a read-only summary report of define environment strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-define-environment-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-environment-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7af29d2e0c7b88e6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-environment-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-define-environment-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-define-environment-strategy-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define environment strategy stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define environment strategy for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-environment-strategy-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define environment strategy records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of define environment strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a define environment strategy summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook name, e.g. report-define-environment-strategy-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary report of define environment strategy with totals, by-dimension breakdowns, and a Top 10 by value section.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineEnvironmentStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineEnvironmentStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-define-environment-strategy-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDefineEnvironmentStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
