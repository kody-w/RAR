---
name: "rar-cowork-cookbook-demo-data-create-production-plan"
description: "Generates 25 realistic demo production plan records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_create_production_plan", "rar_sha256": "9251625089e4e8eb6fc6946dc6dc416f7a40fd48a445a954210016af5ccf3ccc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
