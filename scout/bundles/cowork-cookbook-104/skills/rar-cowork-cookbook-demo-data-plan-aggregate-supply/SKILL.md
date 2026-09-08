---
name: "rar-cowork-cookbook-demo-data-plan-aggregate-supply"
description: "Generates 25 realistic plan aggregate supply demo records in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_aggregate_supply", "rar_sha256": "62464cc24796fcb03b8e826d7ddf1c05e6097316e7cc3dee7e50265b19206997", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_plan_aggregate_supply`. The original RAPP
agent is preserved byte-for-byte in `demo_data_plan_aggregate_supply_agent.py` and in the RCI capsule.

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

Plan aggregate supply Demo Data Generator — Generates 25 realistic plan aggregate supply demo records in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-aggregate-supply
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
      "description": "Sandbox D365 legal entity to create records in (default USMF); must not be production.",
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-plan-aggregate-supply-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_aggregate_supply_agent.py` and embedded as the fenced Python below (sha256 62464cc24796fcb0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_aggregate_supply_agent.py` first:

```bash
python3 demo_data_plan_aggregate_supply_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_aggregate_supply_agent.py   # or on stdin
python3 demo_data_plan_aggregate_supply_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan aggregate supply Demo Data Generator — Generates 25 realistic plan aggregate supply demo records in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-aggregate-supply
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_aggregate_supply',
    "version": '3.0.3',
    "display_name": 'Plan aggregate supply Demo Data Generator',
    "description": "Generates 25 realistic plan aggregate supply demo records in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key.",
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
        "upstream_slug": 'demo-data-plan-aggregate-supply',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-aggregate-supply',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c1b8224959e9213a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-aggregate-supply'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-plan-aggregate-supply', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-plan-aggregate-supply-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic plan aggregate supply data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for plan aggregate supply. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-plan-aggregate-supply-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic plan aggregate supply records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic plan aggregate supply demo records in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key.", 'example_request': 'Generate 25 demo plan aggregate supply records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-plan-aggregate-supply-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo or training data for plan aggregate supply in a D365 sandbox tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataPlanAggregateSupply(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanAggregateSupply'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-plan-aggregate-supply-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataPlanAggregateSupply().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
