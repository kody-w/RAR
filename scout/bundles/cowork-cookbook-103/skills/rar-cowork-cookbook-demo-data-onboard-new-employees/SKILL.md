---
name: "rar-cowork-cookbook-demo-data-onboard-new-employees"
description: "Generates 25 realistic demo employee-onboarding records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_onboard_new_employees", "rar_sha256": "a5130283d9c54b265ac2c2f1a94ed5ec5482cb51966c86f06fe326bcc8fa7560", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_onboard_new_employees`. The original RAPP
agent is preserved byte-for-byte in `demo_data_onboard_new_employees_agent.py` and in the RCI capsule.

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

Onboard new employees Demo Data Generator — Generates 25 realistic demo employee-onboarding records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-onboard-new-employees
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
      "description": "Sandbox D365 legal entity to target (default USMF).",
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
      "description": "Number of demo onboarding records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-onboard-new-employees-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_onboard_new_employees_agent.py` and embedded as the fenced Python below (sha256 a5130283d9c54b26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_onboard_new_employees_agent.py` first:

```bash
python3 demo_data_onboard_new_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_onboard_new_employees_agent.py   # or on stdin
python3 demo_data_onboard_new_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new employees Demo Data Generator — Generates 25 realistic demo employee-onboarding records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-onboard-new-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_onboard_new_employees',
    "version": '3.0.3',
    "display_name": 'Onboard new employees Demo Data Generator',
    "description": "Generates 25 realistic demo employee-onboarding records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-onboard-new-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-onboard-new-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2580fe651cbbb0a3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-employees'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-onboard-new-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF).', 'record_count': 'Number of demo onboarding records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-onboard-new-employees-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic onboard new employees data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for onboard new employees. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-onboard-new-employees-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic onboard new employees records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo employee-onboarding records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo new-employee onboarding records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo onboarding records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-onboard-new-employees-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training onboarding data created in a sandbox D365 legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataOnboardNewEmployees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataOnboardNewEmployees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo onboarding records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-onboard-new-employees-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataOnboardNewEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
