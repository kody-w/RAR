---
name: "rar-cowork-cookbook-demo-data-test-and-validate-the-business-continuity-plan"
description: "Generates 25 realistic demo records for business continuity plan testing in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_test_and_validate_the_business_continuity_plan", "rar_sha256": "8d9755d3f5d0ce9570dc5ce24b23ec1111fc5e79220b6e4395af4629a95a44f6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_test_and_validate_the_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `demo_data_test_and_validate_the_business_continuity_plan_agent.py` and in the RCI capsule.

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

Test and validate the business continuity plan Demo Data Generator — Generates 25 realistic demo records for business continuity plan testing in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-test-and-validate-the-business-continuity-plan
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-test-and-validate-the-business-continuity-plan-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_test_and_validate_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 8d9755d3f5d0ce95…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_test_and_validate_the_business_continuity_plan_agent.py` first:

```bash
python3 demo_data_test_and_validate_the_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_test_and_validate_the_business_continuity_plan_agent.py   # or on stdin
python3 demo_data_test_and_validate_the_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test and validate the business continuity plan Demo Data Generator — Generates 25 realistic demo records for business continuity plan testing in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-test-and-validate-the-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_test_and_validate_the_business_continuity_plan',
    "version": '3.0.3',
    "display_name": 'Test and validate the business continuity plan Demo Data Generator',
    "description": "Generates 25 realistic demo records for business continuity plan testing in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-test-and-validate-the-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-test-and-validate-the-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37d6cc87dd23adbe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/test-and-validate-the-business-continuity-plan'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-test-and-validate-the-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-test-and-validate-the-business-continuity-plan-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic test and validate the business continuity plan data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for test and validate the business continuity plan. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-test-and-validate-the-business-continuity-plan-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic test and validate the business continuity plan records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for business continuity plan testing in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo business continuity plan records in the USMF sandbox, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-test-and-validate-the-business-continuity-plan-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need organic-looking demo data for business continuity plan testing or pilot training in a D365 sandbox tenant. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataTestAndValidateTheBusinessContinuityPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTestAndValidateTheBusinessContinuityPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-test-and-validate-the-business-continuity-plan-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataTestAndValidateTheBusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
