---
name: "rar-cowork-cookbook-demo-data-plan-projects-resources"
description: "Generates 25 realistic demo project-resource records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_projects_resources", "rar_sha256": "36ad6747fc4b6b52f0df6ca2d23ac348cc05a5d333f84d214350d9c4f7ee4562", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_plan_projects_resources`. The original RAPP
agent is preserved byte-for-byte in `demo_data_plan_projects_resources_agent.py` and in the RCI capsule.

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

Plan projects resources Demo Data Generator — Generates 25 realistic demo project-resource records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-projects-resources
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
      "description": "Sandbox D365 legal entity to write into; defaults to USMF.",
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
      "description": "How many demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-plan-projects-resources-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_projects_resources_agent.py` and embedded as the fenced Python below (sha256 36ad6747fc4b6b52…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_projects_resources_agent.py` first:

```bash
python3 demo_data_plan_projects_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_projects_resources_agent.py   # or on stdin
python3 demo_data_plan_projects_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan projects resources Demo Data Generator — Generates 25 realistic demo project-resource records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-projects-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_projects_resources',
    "version": '3.0.3',
    "display_name": 'Plan projects resources Demo Data Generator',
    "description": "Generates 25 realistic demo project-resource records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-plan-projects-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-projects-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1cbb0a79037d707d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/plan-projects-resources'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-plan-projects-resources', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'record_count': 'How many demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-plan-projects-resources-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic plan projects resources data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for plan projects resources. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-plan-projects-resources-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic plan projects resources records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo project-resource records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo plan projects resources records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-plan-projects-resources-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for plan projects resources in a D365 sandbox. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataPlanProjectsResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanProjectsResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-plan-projects-resources-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataPlanProjectsResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
