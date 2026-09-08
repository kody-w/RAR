---
name: "rar-cowork-cookbook-demo-data-onboard-new-employees"
description: "Generates 25 realistic demo employee-onboarding records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_onboard_new_employees", "rar_sha256": "a5130283d9c54b265ac2c2f1a94ed5ec5482cb51966c86f06fe326bcc8fa7560", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
