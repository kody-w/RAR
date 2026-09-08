---
name: "rar-cowork-cookbook-demo-data-coordinate-service-work-with-customer"
description: "Generates 25 realistic demo records for coordinate service work with customer in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_coordinate_service_work_with_customer", "rar_sha256": "1b942781ca26641607b05e48b7918995997d7f14e1f815edecdffc0ca9d8c3f0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOj1pLmX9G8HTG2m6oSIDbVjRsxCARoQSAQi3A5yuz7vgjk9n+fg6RafK9vT7tnPo0q6hXLObnnk5mC397svovK5u3jm+rbxYK3syyO/GZhF96CKW9lk4KvMnXA/4VbFl0TO31XNu3buzfPb90mrrq4LMB23i/8xu78doHii8a3s7jtYnfh+XkJTt2y8dpFUDaACDiMC7By0frNELv+4sHlFnfRwu3brswB+7hY2IsWCOGU44JdEfiC+58qIy4yP7SzhV90cTe9W7SdHQKGXeTnjx3FYju6fvYg+JA4iJu2e7dwgTzda+G7+W8BROr6pmgXvu1Gi8K/vWT8oV1UTZzbzbRI/ekD0NIf7bzK/Pbt48+/vHuLwfHbx9/e3MxuwaU3FqjH2p3NfNVKfSplABEMoBLz0ghQyuwiBFuqCRi8AOeV3wCD5OCS5weL19mPrZ8F7xb//u/pzW7C9qePn4rF6/Ppbf6n9MWswaIr7bbzvYVrV7YTZ8AeHxZ0drOn9qtuwILAX0X44bnzG6WyWvx9vvfjk8mH0O9+/PRWVrMDgTc/vf20AJ769Nb08/GHmUr1408fsvLmNz/+9I1O2zuJ73YzMSD1h8+v8xdZsPDb0jhYfFblLfPiBawdVz4g/p1+8+cp+ovcyySfn4t/LKt3iz+nPOvzdyDvMyIdQPfPyQIbgJ1vH5IyLn588WjKwS/swvV//OlfkXUj303neP4v0f35STjybQ9Y62WSn9493PfLAnrp9pXmv2ZbgYD5K5qA5V/YfTXUv6L98Ow/kM7iAuTIF1/+Kbk/2wD9ffHzv9TtP9vwbhF8AgmUxQOIOyfzPy5+e4TIzz943y7+8MvvgPT/kYxa9o37oPA5t4s48Nvu8+eff2gfl3/45ecf+gpEsW/nn/sm+zOaf2bXB58/WPC16sc/7gX8tSItylux+JpDi9/K6n80v39Y6AAJvW/X24+L7zNx/kCLWYkvTJ8m+C4bWyDrd3b86e13AEMF0KZ3H7cBfvzbvy3E2G3Ktgy6heqWfbcADu7i3J+Fv0Rxu4gf6AcUAHZtY2DY1zoQ/7OHZ4nLYPHr/3IfmP/efWH+csbvzx5AuM/fgPvzC7g/z0s/z8D9+Qtw//phcQFsyiYOwdJsodCy/KkAKF10swhV4897AWw5U+e/B9n9fj6YwfvXv8jp84Poh2r69VGr4icqKsxuRsS2z/wPs+7GjPVPTV1QHvzRd3vALytdIFwQA1x/B2zSltkAEHW2U5vGWbbwYoA5oMxND9rAlh9nYr/++qtjt9Gn4gnhq8Wz/rVLsOCrOIv374GWQRaHUfep8N2oXPzw2+8/LP5j8Z/tehCfecigrrw8BSTcq9JpATKvz8Ey4ETgdgArD0/99vvL1oAMqLwL4Nc4iJ9Fbs6Q1Pe+GF4V6PcoTiwcHxgcGDuvyqYDdWERdx8Wu2DxVV7AdL41V46obDtQvCu/8PzCnQBVG6jz1ZJF2YHy3MVtAMpw3/oPrr86jf0QMQcQYHe/LkRGBnWqzMCfWczHIrC5LGJg/q9h8bwOiDSg+m6+kPiwOM2xuqjsxq6ixn7xCOynX0B9+rIdELfnEv6pmKuzP5vqkThP84RzXzI3Ig+Xvp99DnqQHKCE137hHb56F29xeVTV5lPRvpLCbvxHawBEmRZhH3tzqfjbK6TaqOwz72E/IOlM6eUF7+WVRwwy/6WOZ+4kFnMrsXh1UnMF7lEYwRb/X7ZWs2Vonle2PH3Zsovt6aJcnx6b28zZs8/OFEjzUO6Rnd+anS+A9gXXPxVZDMKvmf72XPnw82vNEyv7BrhFoZUHfRBkwBQz3UcOzDHdNHP22J+KLwXkHbDTAy1BGADAAAk1x/EXhvPdL5JGABXm82/NxEvnGT5AnC+q3smAxwLf9xzbTYFUzZzHL/+ChPDnnL5FMbDY91rN7gD2AvQXQIgYZCYoMh++gvrz7hfR/7Dx2TPNWx79ZA/SuHkQAHL4s4AzsM2BAcTrnl090PPjgwhQI6+6WXcHJNLTrXOQN37dx23czaD5tKtfAfx+P38/NZ2v+mMFcgcYC2RI1QPrPnJqhpscdERABhC4IMXyuHiG8csID4J2PgMEAOBXDD0pPi6/FPIfiTiXti8bZ0XmPXO3sAiA6ODK9D2OXP4sTAC9fF7x4PuPkfaV20x7xtIW4CHg+OXus6348OwMnq3H4gvdj/80Nv341yarR63X/hgAHxdR11Xtx+XyWZ+/lOcPAMmWT1nbR6l+PxfQ99+A4P0LCN4/qvrs7/dfgOAPbJ4W+Lj4a6L+gcQrVT4ukA/wB3i+dXyF2usDLMO831zfY/PdT4Xif4NdwL7MQazNfpxAb/C1Rn5ZAgpl2ACAAoufNbOdS+0NwM2jSACnfCq+j/0590ANKsI5VtvyO0x4NAsgD54+/FrLwK2iA7y9ufEM/Xnye2RK6799LPose/dWgCj8ixPfXLvyOdjbeWYEaQV6ui72H2cP7Bi7+fCPg7T0OLCzD6AkAJzK2u8D8lVx5or7Xd48FQaKuoDDu4X3QGQQq0Dhmfmcc3abPorErFg3VbMmz+Fwbicf0P/5Cf3/LJD6fa34vkrMcHgDaTMPo4sfwRBr91m30FSR++lvi6djHpjoPTvV164/leBrt/vP7A3QSswMvPLjXFXfveAJfIMJBRSgL8MG0Ps1/j3G9qIHk/XP86AzO+KxZT4Ae8DX101ff8Zw/Ldf/kSup2VBRwra6X8W7dTnDlASQPcfajEQ9kvcfjMLiv/0p5p/Kaifn/H1jyyeVXeuxjOCPiJ4Xvhu4X8IPyz+Ysq/R2GUeA/j71Hsw5i1458I9NAZwDwolrP5vvnlm3XKx0w4yw6s2T1/wvjtDcS5PUvyivTXUAGWA1R8387t0hIAA2AIzp8pDO79344bL3JtZIP+FtBDnDWGkhTi2ihBYAgBkw6M+xjlkGuEWq/x9Zr0yADBfCSgENz3fNcLAhd27bVHuatgFu+JC5/nFjGeRcTXZACv12iAISjsAW+imOdRBEW4OInC9tqxcQdf2863rWlceC+9n3rORv06+cz2ean/25tDYGClgLU7+vlhlhDiQCjpTCdzacLUaF05VY01YjIwowkOGSoqaBiyp41po5Bi9yXHpqp0sHdNTqGbrUiv0J2c80F1XN+t8upq1XlA7evqxG7i2LrhLmS5Qe9OV8obN6VX5aWnYJWncuxhGdO76tjJlMmNPK6XW13ncx7Pjzsy248WF0D9Qb/wlz5D03452OaAV0MbMXKBRS5UcFrGbcNzVPvTjUkZUtii0kaqYXVPbc1oD23jpTpJw1D0sZng+VpmT9PBONwpQ4zzxE1aQ/HzoeUZPIt6P70myR3jxdyn44u75MS2PrrxjaE4uQ4NmZBv3NGytCKyNlC7sffD6Uz1pbmj8iTBkW48NoF/lVkKsfsLhgSyPN5AXy6tBBiH1qIqdO45T6O9yBypGkFTySyiBr+UtSJtimV8OBB6sT1gZX2Ay1u7KbawuhNw26sx9nColJyhdY2O8nN5qYhAFNJlmEyWwykEVmj7Gxi+rooMXSWxgPWjOhbjuAvEWI1EpaK2uFV51aBM65M59Utjf1qRIjVYzL6A2dJuoLNxSWgKLZUzkh0PrsQJ+MTuEXpn2Ot9nsbKsTUzqTykpIye+Zgu4I0V7phmJO6HzcSSZ7I7k7fVqeEzWxLT9GIdb248lXvV569sdE3bs+2jmxsfZEUO27u6dbcVfGOXOTGlF3VJidmBGLeSNeFQU+/iECN5o6JueQyh22AQDcIWqELMw2jPqnV7qxlZZ4n2xKe4eYUYYaRRsbMcYr/NDaIT2hzPodC9QFLibUWi9ojDuBOds3ZNk2kPHYJxGe5ss9xn8ik/cPdMY8orOpUqoYeczY8Nra6crs6IvSp6ipsRu1MwpUHWp7qC7yaO2GlLrGRPRiVt79YAsd4U+3w1HiQqbCjFaHdFHKERzlqtxF6GTbzBw3WXaEuuj6f7tahuW5ndnsXlPSyUe7kJO7ZNxv3E3a7dHltuFXK5U/KLlnBbSB7XcVWvkdMow1bHgB6o6g/Ker0hY9ZbIgc7W8LbOsJFU4YJaHQBN32sSLqqCPPMwtMRcVw9BnEVJuRhktgNiw94nZ2lrbgJg911yUykdWObO1/WqhgaqxLnjxs0XRvWPuPsIoWcqy+adSqtq11qq+lh2FaH4wbhd0efUSM4pFAaOt2xZYF1BZZXdL5iDrSQ5BIiR7hAGBcr9mjofuXtYcVoN81Zr4bMKnMlhdr8XlRWR5ZWjSMi4Ufu+nhaSQmPBCqs74r0hLPNCbJwfqNbJL8srAYe2PiMnO1i20TWfRl3bIzwqlhcVXS5EldueAg29jXwLV69hh3edXjqXkFO49d+19fnza2Kk/wsUpvBry06Y0ndSzdBIuNHeb8bc4VaJ8qBUTYZjx5MfCh300lGbgyhC+cLLwiSO93Xk2XFAw1xhu2gWYJUk01aVFOgx3TY3VJnJM+tnarAxSx/2t8Nd8zcVCDztYGmWrZNGIU2D0JxH7x0SbvHAQsZ3OIlYagaysEkDyexipcjeTeFqLy7cHQ83A9bFZI3Urg7QEWzN2+wi7RnpHTNeLwWgX+mPSPf3sNU3OKq3CkNH/Z1HEqHy8T7zrmVfXRFyvvQHPJRLEVbH1jqjJB7NzhJibUWSmWvTXjgrUz+xJN2W6FemrkuTNFXuJtcC3KnY881yiB0TMBAHYoU2K1k1R6vuevmZpFb3g0U5eDGV2x9vBV8t52ITrzAoafKTGGcbHFDdDsuqtAS4mFV7BIJszmMsmV6l++vjYy4yvm8XO+FQOQ31uSud5WiVNPWWeGDJlwIYy+BRrbkuPha0dF6xFfwtD9E5zqHqZwl8rG2kNRrVXVSY+XAbVb7QVN8Qp24kosHaFSNolRHnWnpQdXRAcaqoTKhrrh25Z4AwCfrPe7UOhKvjYY9MBMbqaEc3QzhuKcxw3VKrNzeK2wHDSy2DIoIu7CSNqkkJ2MiamqqZlcBhV+844ktNT+dzo3MsslgUYerxCPW2esqhmfT4ogTx04IA1D+pcSJ1ktoWQR2M5zTCrP6Yshxi24ZeMujEZ2EeK0FHH68nbKyLwnmEFryxTQZqbQdW+6D0AZd065YCTmM6FoVqdcDdeLwLZ1Ed6XeNMKeYkfG57E4EjWxt3AmQQmOP4gdrt+UDRxbnUUzqU6OKZcw9lTgNiV4Sznh/d5M+LEPy6oJsaUzMNCKv+QO53P1nVpSbooOfhaTJ5KhHZqzuN5ThJPEN8gduffaba/fdzbFTdhe2cRutIP6+2F9lqSiOQuXdouFeHTHQm7w8qUxLc2WDyUtCUWpNk+YwaW6zDarjNDGUV/f86uwbbZK3zEFoTaBqmD1nuVsquKVfNtuoIyWl+aBD8tgnyVyI2/EDbdxzvuD0jMB3eK6vT3LuNcM8IXQN5VmbPX0zmw0kzkobhAiVDaMRqtA2VlpLuelkU87wtJ5cZR9uBF3JXd2c/yenqubcGPMOGLStXfgoB7G483mTgibyzkbY/NwwwfGP/PRNV7HZzc55N2exNOzsty4l91YxhwxIs6BzMZLoedYzIPZUdX2eOlzWqvV1V1WQhFY5+AiRgbShDmMsAKr1pFCDlS5DWTCzehbjIE6vVTbXZOhpELl5x2VLEWQO+uLVlblPh0bhy4yrb0XNbdRGHrUl9o9CuIbGrNIeqlP+VFGk51CnM4nnR5WVpCX6fXK4rFGVRgrYSv5io42X2b6NggKIoi8Yo/f6INfQzyONteiCPvTmhF2udbgSGPRwhXle2R7U9NNFQwNBMmsqLmSh+piiV5oSFUk7dLDyJaJPDK9n2tBs4mqtPZlXuYwsKt05ddSHq2qiwiXDrJrdzDNg6QnQBEblpt9T51yuq1H/bZU1laRbj3h6oDIxHYHtls7qRnWSaMcY8IBeCUzF6ByH9xljBd2l0OuToZwUw7rkyK0+2xaCnsI4s7h2BbWDa1kYdCFjSCeOynO87XkIUx9aYWJ1nZqqfBnvFwet85ZSKYcvmjZQJvuCRWWy5WqbTqDZznQ3p0lXY1GqmyCYVvkWog7YL9vmlsbWOhEpYIyovp2wM2jR1HLIuFoIiWu+U7VohpNTQVmmIq7ppk11df6ePCYrV7LPT6st5szrfdoi5FNNqzRrcQZa5sLj1aPb886Ex63CVmvq0N5wrlyI23qYyp2+4mmnfAu6sg+mOKV1Lv7bGiyk95LG9rna7MtropKrehpvOfnCOLPNDY3rhgWXE7TmruUXqmvQF8PAnrnV3aBTRl2Tip170xFt9bz0BduGecorFPxWxdmEhwS851dZcfU36mHOjw4TF6gBzWOOdPbO75/8DUzmSBJSMjpKhfwzQ+gbp2Ug1wUnYff+BY0/uZhjaIgaQxTh01zGY3juSBcZex8js+Od2+/ccV43UZk1ele69NQDTXHLMkFvr8YZxk0mZ0xymegnJ35KWfUOb3FGyqyGda4nw7t2UrDw+XisjzjH5zrASG8wTOiQtxJNzvhvLA4npp0vZIzX1gy40qMuH2MuRY95XjBqX3bTtB20nva9WxMEi7QGd4SO+7QIfaIL8va6QpGgyFvSBCCgpYQGpHGug5zaYlFfKZ60IGNliGRqTs87XQXMZeG4+3U7WlSQtpN+W7vlWJ+0w+naSOw4MqJK3BVOZc+dJGQED0dA9f0611jRtMyELyp4apky7KrfpS9gyOGDcEiqs7fesYILykU9tnJrIqJbq/3KQl2zbb2VdhFu1MgjJBbOAi6DojzqJ+JZYUcOXifXTh4qPOtFlshfpCV1rIpxWLQpiosCKRHu0LM67Wz+9NlvJT3oD6NmkY4TQYMQGPKwbQdPcnEsqbzTTCcfaoujRY/qv61WLumE+3XGtejdxGgOWPhyC6mYqjEq0ShnNw8mJjqlhdYczcbT8zqrej7NbuZqFQ6CZKnCdD56pqHkiinXBNjz4Fvqxu507mcqIoVRguksc26btxx6M3YXkI2RDLteKJwq5euOHeO7tZRiaaGHE4DAloipolbbr8XtKtd3RsnjarjDtevpN6OmpkeRhTxDJmZlN1OoDBT4GMl0/2ooBkqptJLt8JPVymuw2bVG82wHHSkiRMaGp0Wx65rzSjGDFPwgQITHG2325K3ltgN5ykFg/MbenDYu55glsIR9c2Jh7CeFH4PZrS9sb1l1oobJiURW8VBdTegbMhV9bzt9qBlWu07fetO5AyPVXChzvxkrKqluvXz1VYUGlbgedpopHKFyRKdxoWzaYXbEKyT0/Z4iaKjqcQ7jRHHk5VxrQmfG7zXSFK6RGJOKgEEQgWVl2FwhihubcZ7VLWodRTYXHdea8ui52pWTkx2tZE1fX3uNQc+ScOUtOQyr+WNRgRlspdvSp6QWhxhqKmwHlrQ7oZUtBIo000JLDpdec+2xF0lZBbZk/4UGXcKzPhktLK6nUfyfWUeNfvYW9suw7OVQHqSFiOX1UpG43WxsvJuu5YlReo8byTMVrg0pRF6ytocanu9UcDwQ6xbi8SIkOPueQWKXnsbIsG7EGhpjITLl1WIkH7tGcva38YbDCUyixVuVFArHqcbV6KyFXi1uYelZDE163QbOKJP4xrjr1lKbFuHu8OtFzdQAMYfAslzdLxgHKaixywwZc3q1LiFrgcCQZaab0MWEt5oPQrXghl2UXaUVrCxheHTCkTOCjkuQ8Ues8I6OTWxWm4TzCik+FgWwwWvLGhgws48qFgYEBdaFi6wIakqW3ugPGw9JWCK065lqrUs4P3O9Ok6YxV9ZClJ2LFprAqMm2oBAbqxBGmUsjYsUOLUFs5WiNdtcJQuNRvKBe2Q2BnkuNcSS3Ysn69ALEsBZFbS/rC2U7I09+jlbKujHTPLfgMjCExY0U64eymy3EmF6bWifb14ezSnpki4g0HwblhL2As8t1MJD3XOzTFqUHKflx44lvRyqcYN7gVG0vXb6GJxe2mnpOddk95caSh0UDrymtqrFnNzHMMvz7o2SmdLNHzD72x7laMH5Izc64iGx+6KItsEXXZKvbwZ0z1KsZ1XrzsVTJ7QoSW0ZNzoaLUpyYrZc9fEuYpLeF04Nq+r+KbkXRHG+l42OQ61+5wnintA2FIvcpjsqfltm/blFqbaxBaLYIOcGGMfeIO1cQmf5YVqOPjiBT8R6z6oMVcWkvtK1kA7EMa3eH9YuXVbiKtQKQYNk1unanp3uRlocEwQlShD6BlPMVSD+XUQ3vFVRuMrnXL0q0cgMSGN4t1V9FI6+0ZM5Mo9H3Me1dc7Iy0o98bmnEu6nryKeJvEk6qcILU+uRAiwjpTSBxnYQy0KU+rEiNufVhT/uRYuRPBbNUfYeGunmrgymq6hpe8ENHVVdgk+pa43SvWOSZGbLsQgXKbnG+4kxfV0j2rBfO4GsQVTZ8zZYTvZlaTSgjqL1kuLYWfHDoXo/LkFLxm6vz6kh5xQ3FHu9QalD6JPVmco+tquPBdMOErA4buR/0SSOLodYoLBJdlr9ZXkuDUHMcK99ElO++O3UTaTTbeGtFV/3a556QD9euh3mVOQ0mNAdkMWkZ43CyPza2XVfJqq6SXRQ5EF0SRZmaK9j0My/7UOMNl0G0kHiOkz6+evfXgoavuWYKix7paNZUz3G1ZvFgBuVnll9AKQ+tymIqY1Rlo8GK+5UG3oO3vQ71KjASSgyNDqrTugPaQxPBSS8ii3faM5BVJvWf4I1VoUFxSo5uxgpmrvL+zeBxW9VXuqROA871A0tkyT82mbDVztG1HEWz8MvAo7XZu6eygMjGu9+PSrqHkCF86kqAt2nO66ZBj++ikWKE09TcaQnSzvXmJ69a6QOzDnhPg5TJ2TVhvlE4xCUtbJWe4s9AMdVbdEXYrWXH27jFntvs9Nf/mXsMwhoy+gRbOmE4dBXnbA6Fn7alcn4RTat4IxzD6s3M5JJq3ZCaR9+ROzmXZ0BxCVXuPiLvkrOjLzHJxQry1sTp5JIxQ1RrFsmGIg4pUjON+QDK6ji7TClFd4UxmSZMGzN7ystMxpfZ3qiXOVxzVUCpO9LUNIU7Kwwe08BE2j2XyHK8bRFtNTYYFbn93wXx9CjTUzjVSF6xdfc20ZFBoEov2h42n4CO0JMx76hJ1TS/Lg0Qmuh+63ZWAvcTqACkcvrd4bxj3QQZTnDv5wugf1+7acLpRNc3JOwfcUFssdY9zCxRUXrHRhB6V3b26d3Z3gq6Dl1atdUSPdxo/5SsHNRASt917sHHgVOXxkGcqseKRVRG2mOfYpFz0GwO6CyUb8uxK2JmhFt/uCaagdGCfbi3NdrAtn9rMXg8nfwV6QvGOrXaJHCUVldg2wDTSWZ+PxFBfWCcRNPnakKFfdoflNMVDlWPpUNTH4oxwqreuV6yxvJh9g9zyabmcr9TH09Jy2Y4fmTUDkdzdacGwhVHkyUInM2NGXQDlwTLtwG6EY0Om41q4BqIbdI7k+WOthz3F+3cxrwwyMTpkdXfYgTtS411tQZnNt+RWYFeOKgor0ZAtPySupFuBrr+OhksQMYIa3A62GJ3PrNaYUwvfFJ1WthSiGWeO8E1PqG44cZTGpjOMNt6DUr7CPVHp9ujZqIsSk/CNr1GqrQWFWRxJqt55/oCe0IvDnAKUXLY60XabdSDIcn8SO7I2cJlI3DOfDYnnkxnFnXaB2DOsT6ba3huP56RkamF1ynrTlFaQPAyhRrFu6EvYcFnBHW06l/0BL6TuJBPNHRK848SL8k4019ZRziRf2hSUcHb9O3bvWJqm//727m1+ePZ6iPvffddsfsjz/+xZ0/Ox0Jc3Rh4PK33b+/jg9fG/LeEv794aN57lezxta7M+fD2M+odnbe//4sPDmdj0fLnry6Pr54Pxzg7nt6Pf4sIDS5vpc1tmj7dJwA6nb+eXKNv5PVsXfH//LParijPll2YduPJ8+fNtfstxfk/E92Ig2Os0fD2NBLsn4MvYbT+vCPyz31Sz4q9XEIC+qw/wh9Xb7/8bmEbPnt8uAAA= -->
