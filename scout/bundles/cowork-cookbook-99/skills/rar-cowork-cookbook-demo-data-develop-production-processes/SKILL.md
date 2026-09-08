---
name: "rar-cowork-cookbook-demo-data-develop-production-processes"
description: "Generates 25 realistic demo production-process records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_production_processes", "rar_sha256": "f14024ec4f30753f3093b103e7213ab426026cb5e70e7fee0910ee2fd01fd949", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_production_processes`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_production_processes_agent.py` and in the RCI capsule.

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

Develop production processes Demo Data Generator — Generates 25 realistic demo production-process records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-production-processes
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
      "description": "Sandbox D365 legal entity to target; defaults to USMF. Must not be a production entity.",
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
      "description": "Excel staging workbook filename, e.g. demo-data-develop-production-processes-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_production_processes_agent.py` and embedded as the fenced Python below (sha256 f14024ec4f30753f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_production_processes_agent.py` first:

```bash
python3 demo_data_develop_production_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_production_processes_agent.py   # or on stdin
python3 demo_data_develop_production_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop production processes Demo Data Generator — Generates 25 realistic demo production-process records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-production-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_production_processes',
    "version": '3.0.3',
    "display_name": 'Develop production processes Demo Data Generator',
    "description": "Generates 25 realistic demo production-process records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-develop-production-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-production-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bc95351f77599255',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/develop-production-processes'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-develop-production-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be a production entity.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging workbook filename, e.g. demo-data-develop-production-processes-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop production processes data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop production processes. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-production-processes-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop production processes records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo production-process records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo production process records in the USMF sandbox and stage them in Excel before creating.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be a production entity.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging workbook filename, e.g. demo-data-develop-production-processes-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or pilot production-process data in a D365 sandbox legal entity. Never run against production; requires the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopProductionProcesses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopProductionProcesses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be a production entity.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging workbook filename, e.g. demo-data-develop-production-processes-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDevelopProductionProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
