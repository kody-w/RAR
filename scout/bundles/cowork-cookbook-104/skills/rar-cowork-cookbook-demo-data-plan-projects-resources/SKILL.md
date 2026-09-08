---
name: "rar-cowork-cookbook-demo-data-plan-projects-resources"
description: "Generates 25 realistic demo project-resource records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_projects_resources", "rar_sha256": "36ad6747fc4b6b52f0df6ca2d23ac348cc05a5d333f84d214350d9c4f7ee4562", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
