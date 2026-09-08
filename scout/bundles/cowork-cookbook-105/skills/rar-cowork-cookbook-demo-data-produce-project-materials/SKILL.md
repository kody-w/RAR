---
name: "rar-cowork-cookbook-demo-data-produce-project-materials"
description: "Generates 25 realistic demo produce project materials records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_produce_project_materials", "rar_sha256": "53eace3c9ab62f40a3d0257ee35fb3200b5f242f85eb4105076df88b78d05bc3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_produce_project_materials`. The original RAPP
agent is preserved byte-for-byte in `demo_data_produce_project_materials_agent.py` and in the RCI capsule.

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

Produce project materials Demo Data Generator — Generates 25 realistic demo produce project materials records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-produce-project-materials
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
      "description": "Excel staging file name, e.g. demo-data-produce-project-materials-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_produce_project_materials_agent.py` and embedded as the fenced Python below (sha256 53eace3c9ab62f40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_produce_project_materials_agent.py` first:

```bash
python3 demo_data_produce_project_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_produce_project_materials_agent.py   # or on stdin
python3 demo_data_produce_project_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Produce project materials Demo Data Generator — Generates 25 realistic demo produce project materials records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-produce-project-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_produce_project_materials',
    "version": '3.0.3',
    "display_name": 'Produce project materials Demo Data Generator',
    "description": "Generates 25 realistic demo produce project materials records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-produce-project-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-produce-project-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44d60f766a8f6cbf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/produce-project-materials'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-produce-project-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-produce-project-materials-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic produce project materials data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for produce project materials. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-produce-project-materials-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic produce project materials records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo produce project materials records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo produce project materials records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-produce-project-materials-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/pilot produce project materials data created in a D365 F&SCM sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataProduceProjectMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataProduceProjectMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-produce-project-materials-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataProduceProjectMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
