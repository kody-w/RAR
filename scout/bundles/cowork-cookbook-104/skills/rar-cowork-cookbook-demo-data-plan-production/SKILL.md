---
name: "rar-cowork-cookbook-demo-data-plan-production"
description: "Generates 25 realistic demo plan production records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_production", "rar_sha256": "3b5e5dcc30b846a114532a1d6b6c75de3d94fa94aa8d81d24cf3f85ffa8b8660", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_plan_production`. The original RAPP
agent is preserved byte-for-byte in `demo_data_plan_production_agent.py` and in the RCI capsule.

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

Plan production Demo Data Generator — Generates 25 realistic demo plan production records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-production
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
      "description": "Number of demo plan production records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. 'demo-data-plan-production-2026-05-24.xlsx'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_production_agent.py` and embedded as the fenced Python below (sha256 3b5e5dcc30b846a1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_production_agent.py` first:

```bash
python3 demo_data_plan_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_production_agent.py   # or on stdin
python3 demo_data_plan_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan production Demo Data Generator — Generates 25 realistic demo plan production records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_production',
    "version": '3.0.3',
    "display_name": 'Plan production Demo Data Generator',
    "description": "Generates 25 realistic demo plan production records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-plan-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7bbe72fdae16e03e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-production'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-plan-production', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo plan production records to generate (default 25).', 'workbook_name': "Excel staging file name, e.g. 'demo-data-plan-production-2026-05-24.xlsx'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic plan production data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for plan production. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-plan-production-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic plan production records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo plan production records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo plan production records in USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo plan production records to generate (default 25).', 'name': 'record_count'}, {'description': "Excel staging file name, e.g. 'demo-data-plan-production-2026-05-24.xlsx'.", 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training or pilot plan production data created in a sandbox D365 legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataPlanProduction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanProduction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo plan production records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': "Excel staging file name, e.g. 'demo-data-plan-production-2026-05-24.xlsx'.", 'type': 'string'}},
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
    print(DemoDataPlanProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
