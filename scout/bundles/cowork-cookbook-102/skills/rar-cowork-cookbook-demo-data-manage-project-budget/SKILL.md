---
name: "rar-cowork-cookbook-demo-data-manage-project-budget"
description: "Generates 25 realistic demo project budget records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_project_budget", "rar_sha256": "f8808991a418c4a9da827ef7a523fe1f39b4d06ac51ba8819df871e7968c5dfa", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
