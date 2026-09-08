---
name: "rar-cowork-cookbook-demo-data-test-and-validate-the-business-continuity-plan"
description: "Generates 25 realistic demo records for business continuity plan testing in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_test_and_validate_the_business_continuity_plan", "rar_sha256": "8d9755d3f5d0ce9570dc5ce24b23ec1111fc5e79220b6e4395af4629a95a44f6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
