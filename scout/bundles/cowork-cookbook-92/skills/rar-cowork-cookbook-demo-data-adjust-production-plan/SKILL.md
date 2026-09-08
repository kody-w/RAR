---
name: "rar-cowork-cookbook-demo-data-adjust-production-plan"
description: "Generates 25 realistic demo production plan adjustment records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_adjust_production_plan", "rar_sha256": "46f6b4fc513f1d0754bf01d77e1b2c819f6a87716b073af86bda716c2e05ca5e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
