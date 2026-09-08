---
name: "rar-cowork-cookbook-demo-data-develop-sales-strategy"
description: "Generates 25 realistic demo sales-strategy records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_sales_strategy", "rar_sha256": "f587de57f2569e72ae75ffa613a2fee9588d2c895d51cef73208e8dc0cade14a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_sales_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_sales_strategy_agent.py` and in the RCI capsule.

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

Develop sales strategy Demo Data Generator — Generates 25 realistic demo sales-strategy records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-sales-strategy
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
      "description": "Sandbox D365 legal entity to write to (defaults to USMF); must not be production.",
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
      "description": "How many demo records to generate (defaults to 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-develop-sales-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_sales_strategy_agent.py` and embedded as the fenced Python below (sha256 f587de57f2569e72…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_sales_strategy_agent.py` first:

```bash
python3 demo_data_develop_sales_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_sales_strategy_agent.py   # or on stdin
python3 demo_data_develop_sales_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales strategy Demo Data Generator — Generates 25 realistic demo sales-strategy records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-sales-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_sales_strategy',
    "version": '3.0.3',
    "display_name": 'Develop sales strategy Demo Data Generator',
    "description": "Generates 25 realistic demo sales-strategy records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-sales-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-sales-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c4f596d67364726c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-sales-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-develop-sales-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (defaults to USMF); must not be production.', 'record_count': 'How many demo records to generate (defaults to 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-develop-sales-strategy-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop sales strategy data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop sales strategy. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-sales-strategy-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop sales strategy records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo sales-strategy records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo sales strategy records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (defaults to USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (defaults to 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-develop-sales-strategy-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or pilot sales-strategy data created in a D365 F&SCM sandbox tenant for training scenarios. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopSalesStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopSalesStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (defaults to USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (defaults to 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-develop-sales-strategy-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDevelopSalesStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
