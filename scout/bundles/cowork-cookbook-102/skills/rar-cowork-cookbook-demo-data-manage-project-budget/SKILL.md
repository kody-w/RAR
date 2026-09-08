---
name: "rar-cowork-cookbook-demo-data-manage-project-budget"
description: "Generates 25 realistic demo project budget records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_project_budget", "rar_sha256": "f8808991a418c4a9da827ef7a523fe1f39b4d06ac51ba8819df871e7968c5dfa", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_project_budget`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_project_budget_agent.py` and in the RCI capsule.

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

Manage project budget Demo Data Generator — Generates 25 realistic demo project budget records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-project-budget
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
      "description": "Sandbox D365 legal entity to target; defaults to USMF. Must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-manage-project-budget-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_project_budget_agent.py` and embedded as the fenced Python below (sha256 f8808991a418c4a9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_project_budget_agent.py` first:

```bash
python3 demo_data_manage_project_budget_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_project_budget_agent.py   # or on stdin
python3 demo_data_manage_project_budget_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project budget Demo Data Generator — Generates 25 realistic demo project budget records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-project-budget
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_project_budget',
    "version": '3.0.3',
    "display_name": 'Manage project budget Demo Data Generator',
    "description": "Generates 25 realistic demo project budget records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-project-budget',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-project-budget',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fa93feb8388b1f97',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/manage-project-budget'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-manage-project-budget', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-project-budget-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage project budget data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage project budget. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-project-budget-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage project budget records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo project budget records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo project budget records in the USMF sandbox and stage them in Excel before creating.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-project-budget-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training project budget data created in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageProjectBudget(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageProjectBudget'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-project-budget-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageProjectBudget().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
