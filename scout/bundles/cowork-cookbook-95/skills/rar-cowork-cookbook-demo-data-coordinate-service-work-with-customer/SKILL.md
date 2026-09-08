---
name: "rar-cowork-cookbook-demo-data-coordinate-service-work-with-customer"
description: "Generates 25 realistic demo records for coordinate service work with customer in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_coordinate_service_work_with_customer", "rar_sha256": "1b942781ca26641607b05e48b7918995997d7f14e1f815edecdffc0ca9d8c3f0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_coordinate_service_work_with_customer`. The original RAPP
agent is preserved byte-for-byte in `demo_data_coordinate_service_work_with_customer_agent.py` and in the RCI capsule.

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

Coordinate service work with customer Demo Data Generator — Generates 25 realistic demo records for coordinate service work with customer in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-coordinate-service-work-with-customer
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
      "description": "Sandbox D365 legal entity to write to (default USMF); never a production entity.",
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
      "description": "Excel staging file name, e.g. demo-data-coordinate-service-work-with-customer-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_coordinate_service_work_with_customer_agent.py` and embedded as the fenced Python below (sha256 1b942781ca266416…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_coordinate_service_work_with_customer_agent.py` first:

```bash
python3 demo_data_coordinate_service_work_with_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_coordinate_service_work_with_customer_agent.py   # or on stdin
python3 demo_data_coordinate_service_work_with_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Coordinate service work with customer Demo Data Generator — Generates 25 realistic demo records for coordinate service work with customer in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-coordinate-service-work-with-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_coordinate_service_work_with_customer',
    "version": '3.0.3',
    "display_name": 'Coordinate service work with customer Demo Data Generator',
    "description": "Generates 25 realistic demo records for coordinate service work with customer in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, then returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-coordinate-service-work-with-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-coordinate-service-work-with-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eef161ca6c140498',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/coordinate-service-work-with-customer'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-coordinate-service-work-with-customer', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); never a production entity.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-coordinate-service-work-with-customer-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic coordinate service work with customer data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for coordinate service work with customer. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-coordinate-service-work-with-customer-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic coordinate service work with customer records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for coordinate service work with customer in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, then returns each new record's primary key.", 'example_request': 'Generate 25 demo coordinate service work with customer records in USMF sandbox, stage them in Excel, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); never a production entity.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-coordinate-service-work-with-customer-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need sandbox-only demo/training data for coordinate service work with customer in Dynamics 365 F&SCM, staged in Excel before creation.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataCoordinateServiceWorkWithCustomer(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCoordinateServiceWorkWithCustomer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); never a production entity.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-coordinate-service-work-with-customer-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataCoordinateServiceWorkWithCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
