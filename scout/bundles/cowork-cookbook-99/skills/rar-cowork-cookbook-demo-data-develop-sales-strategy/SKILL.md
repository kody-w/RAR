---
name: "rar-cowork-cookbook-demo-data-develop-sales-strategy"
description: "Generates 25 realistic demo sales-strategy records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_sales_strategy", "rar_sha256": "f587de57f2569e72ae75ffa613a2fee9588d2c895d51cef73208e8dc0cade14a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
