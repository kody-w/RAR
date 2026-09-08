---
name: "rar-cowork-cookbook-demo-data-develop-financial-period-strategy"
description: "Generates 25 realistic demo records for financial period strategy in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_financial_period_strategy", "rar_sha256": "c36def832cfa1cdd7bebc56cb2cc9a2e3884d566f4a70665097f90b778507fce", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
