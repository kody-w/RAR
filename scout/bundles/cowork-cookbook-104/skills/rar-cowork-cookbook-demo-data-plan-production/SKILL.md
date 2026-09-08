---
name: "rar-cowork-cookbook-demo-data-plan-production"
description: "Generates 25 realistic demo plan production records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_production", "rar_sha256": "3b5e5dcc30b846a114532a1d6b6c75de3d94fa94aa8d81d24cf3f85ffa8b8660", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
