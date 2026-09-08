---
name: "rar-cowork-cookbook-demo-data-develop-financial-period-strategy"
description: "Generates 25 realistic demo records for financial period strategy in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_financial_period_strategy", "rar_sha256": "c36def832cfa1cdd7bebc56cb2cc9a2e3884d566f4a70665097f90b778507fce", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_financial_period_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_financial_period_strategy_agent.py` and in the RCI capsule.

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

Develop financial period strategy Demo Data Generator — Generates 25 realistic demo records for financial period strategy in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-financial-period-strategy
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Sandbox D365 legal entity to target (default USMF).",
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
    "record_count": {
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-develop-financial-period-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_financial_period_strategy_agent.py` and embedded as the fenced Python below (sha256 c36def832cfa1cdd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_financial_period_strategy_agent.py` first:

```bash
python3 demo_data_develop_financial_period_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_financial_period_strategy_agent.py   # or on stdin
python3 demo_data_develop_financial_period_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop financial period strategy Demo Data Generator — Generates 25 realistic demo records for financial period strategy in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-financial-period-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_financial_period_strategy',
    "version": '3.0.3',
    "display_name": 'Develop financial period strategy Demo Data Generator',
    "description": "Generates 25 realistic demo records for financial period strategy in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-financial-period-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-financial-period-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c9661b92b45a2d22',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-financial-period-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-develop-financial-period-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-develop-financial-period-strategy-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop financial period strategy data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop financial period strategy. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-financial-period-strategy-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop financial period strategy records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for financial period strategy in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo financial period strategy records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-develop-financial-period-strategy-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need seeded demo/training data for financial period strategy in a D365 F&SCM sandbox. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopFinancialPeriodStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopFinancialPeriodStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-develop-financial-period-strategy-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDevelopFinancialPeriodStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
