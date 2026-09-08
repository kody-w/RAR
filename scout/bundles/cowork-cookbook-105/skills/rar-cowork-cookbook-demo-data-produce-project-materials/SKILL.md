---
name: "rar-cowork-cookbook-demo-data-produce-project-materials"
description: "Generates 25 realistic demo produce project materials records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_produce_project_materials", "rar_sha256": "53eace3c9ab62f40a3d0257ee35fb3200b5f242f85eb4105076df88b78d05bc3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
