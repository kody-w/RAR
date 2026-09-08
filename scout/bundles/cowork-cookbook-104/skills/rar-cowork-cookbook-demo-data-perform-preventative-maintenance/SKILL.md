---
name: "rar-cowork-cookbook-demo-data-perform-preventative-maintenance"
description: "Generates 25 realistic preventative-maintenance demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_perform_preventative_maintenance", "rar_sha256": "29982fbe2565faa7ecb3a3ae772501194d4a55b6510c878eeb9364f26cd0951a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_perform_preventative_maintenance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_perform_preventative_maintenance_agent.py` and in the RCI capsule.

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

Perform preventative maintenance Demo Data Generator — Generates 25 realistic preventative-maintenance demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-perform-preventative-maintenance
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
      "description": "Sandbox D365 legal entity to target; defaults to USMF. Must never be a production entity.",
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
      "description": "Excel staging file name, e.g. demo-data-perform-preventative-maintenance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_perform_preventative_maintenance_agent.py` and embedded as the fenced Python below (sha256 29982fbe2565faa7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_perform_preventative_maintenance_agent.py` first:

```bash
python3 demo_data_perform_preventative_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_perform_preventative_maintenance_agent.py   # or on stdin
python3 demo_data_perform_preventative_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform preventative maintenance Demo Data Generator — Generates 25 realistic preventative-maintenance demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-perform-preventative-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_perform_preventative_maintenance',
    "version": '3.0.3',
    "display_name": 'Perform preventative maintenance Demo Data Generator',
    "description": "Generates 25 realistic preventative-maintenance demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-perform-preventative-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-perform-preventative-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f90407cd2388e693',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-preventative-maintenance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-perform-preventative-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must never be a production entity.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-perform-preventative-maintenance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic perform preventative maintenance data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for perform preventative maintenance. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-perform-preventative-maintenance-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic perform preventative maintenance records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic preventative-maintenance demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.", 'example_request': 'Generate 25 demo preventative maintenance records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must never be a production entity.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-perform-preventative-maintenance-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training preventative-maintenance data created in a D365 sandbox legal entity (never production).'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataPerformPreventativeMaintenance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPerformPreventativeMaintenance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must never be a production entity.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-perform-preventative-maintenance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataPerformPreventativeMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
