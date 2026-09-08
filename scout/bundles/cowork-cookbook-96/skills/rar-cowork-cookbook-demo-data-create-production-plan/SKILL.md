---
name: "rar-cowork-cookbook-demo-data-create-production-plan"
description: "Generates 25 realistic demo production plan records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_create_production_plan", "rar_sha256": "9251625089e4e8eb6fc6946dc6dc416f7a40fd48a445a954210016af5ccf3ccc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_create_production_plan`. The original RAPP
agent is preserved byte-for-byte in `demo_data_create_production_plan_agent.py` and in the RCI capsule.

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

Create production plan Demo Data Generator — Generates 25 realistic demo production plan records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-create-production-plan
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
      "description": "Number of demo production plan records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging filename, e.g. demo-data-create-production-plan-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_create_production_plan_agent.py` and embedded as the fenced Python below (sha256 9251625089e4e8eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_create_production_plan_agent.py` first:

```bash
python3 demo_data_create_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_create_production_plan_agent.py   # or on stdin
python3 demo_data_create_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create production plan Demo Data Generator — Generates 25 realistic demo production plan records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-create-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_create_production_plan',
    "version": '3.0.3',
    "display_name": 'Create production plan Demo Data Generator',
    "description": "Generates 25 realistic demo production plan records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-create-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-create-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f09df6b944aa6443',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/create-production-plan'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-create-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo production plan records to generate (default 25).', 'workbook_name': 'Excel staging filename, e.g. demo-data-create-production-plan-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic create production plan data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for create production plan. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-create-production-plan-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic create production plan records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo production plan records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo production plan records in USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo production plan records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging filename, e.g. demo-data-create-production-plan-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training production plan data created in a sandbox D365 legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataCreateProductionPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCreateProductionPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo production plan records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging filename, e.g. demo-data-create-production-plan-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataCreateProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
