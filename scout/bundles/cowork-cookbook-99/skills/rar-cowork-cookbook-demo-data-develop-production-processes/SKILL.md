---
name: "rar-cowork-cookbook-demo-data-develop-production-processes"
description: "Generates 25 realistic demo production-process records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_production_processes", "rar_sha256": "f14024ec4f30753f3093b103e7213ab426026cb5e70e7fee0910ee2fd01fd949", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
