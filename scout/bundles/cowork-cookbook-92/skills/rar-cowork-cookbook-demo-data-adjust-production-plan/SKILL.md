---
name: "rar-cowork-cookbook-demo-data-adjust-production-plan"
description: "Generates 25 realistic demo production plan adjustment records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_adjust_production_plan", "rar_sha256": "46f6b4fc513f1d0754bf01d77e1b2c819f6a87716b073af86bda716c2e05ca5e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_adjust_production_plan`. The original RAPP
agent is preserved byte-for-byte in `demo_data_adjust_production_plan_agent.py` and in the RCI capsule.

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

Adjust production plan Demo Data Generator — Generates 25 realistic demo production plan adjustment records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-adjust-production-plan
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
      "description": "Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.",
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
      "description": "Number of demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging workbook filename, e.g. demo-data-adjust-production-plan-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_adjust_production_plan_agent.py` and embedded as the fenced Python below (sha256 46f6b4fc513f1d07…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_adjust_production_plan_agent.py` first:

```bash
python3 demo_data_adjust_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_adjust_production_plan_agent.py   # or on stdin
python3 demo_data_adjust_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust production plan Demo Data Generator — Generates 25 realistic demo production plan adjustment records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-adjust-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_adjust_production_plan',
    "version": '3.0.3',
    "display_name": 'Adjust production plan Demo Data Generator',
    "description": "Generates 25 realistic demo production plan adjustment records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-adjust-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-adjust-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '837630de360e72b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/adjust-production-plan'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-adjust-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging workbook filename, e.g. demo-data-adjust-production-plan-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic adjust production plan data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for adjust production plan. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-adjust-production-plan-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic adjust production plan records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo production plan adjustment records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo adjust production plan records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging workbook filename, e.g. demo-data-adjust-production-plan-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for adjust production plan in a D365 sandbox tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAdjustProductionPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAdjustProductionPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging workbook filename, e.g. demo-data-adjust-production-plan-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAdjustProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
