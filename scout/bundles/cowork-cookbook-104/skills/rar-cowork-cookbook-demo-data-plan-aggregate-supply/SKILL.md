---
name: "rar-cowork-cookbook-demo-data-plan-aggregate-supply"
description: "Generates 25 realistic plan aggregate supply demo records in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_aggregate_supply", "rar_sha256": "62464cc24796fcb03b8e826d7ddf1c05e6097316e7cc3dee7e50265b19206997", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
