---
name: "rar-cowork-cookbook-demo-data-perform-preventative-maintenance"
description: "Generates 25 realistic preventative-maintenance demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_perform_preventative_maintenance", "rar_sha256": "29982fbe2565faa7ecb3a3ae772501194d4a55b6510c878eeb9364f26cd0951a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
