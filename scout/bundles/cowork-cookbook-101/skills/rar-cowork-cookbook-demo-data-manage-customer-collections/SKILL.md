---
name: "rar-cowork-cookbook-demo-data-manage-customer-collections"
description: "Generates 25 realistic customer-collections demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_customer_collections", "rar_sha256": "a8a402fb7266c01f87ea2a1ebba59b51bff3212cc939dedff7c662ef3aa859a9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_customer_collections`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_customer_collections_agent.py` and in the RCI capsule.

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

Manage customer collections Demo Data Generator — Generates 25 realistic customer-collections demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-customer-collections
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
      "description": "Sandbox D365 legal entity to target; defaults to USMF. Must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-manage-customer-collections-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_customer_collections_agent.py` and embedded as the fenced Python below (sha256 a8a402fb7266c01f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_customer_collections_agent.py` first:

```bash
python3 demo_data_manage_customer_collections_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_customer_collections_agent.py   # or on stdin
python3 demo_data_manage_customer_collections_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer collections Demo Data Generator — Generates 25 realistic customer-collections demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-customer-collections
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_customer_collections',
    "version": '3.0.3',
    "display_name": 'Manage customer collections Demo Data Generator',
    "description": "Generates 25 realistic customer-collections demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-customer-collections',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-customer-collections',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '549d2bdbf0c65229',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-collections'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-manage-customer-collections', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-customer-collections-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage customer collections data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage customer collections. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-customer-collections-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage customer collections records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic customer-collections demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.", 'example_request': 'Generate 25 demo customer collections records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-customer-collections-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training customer collections data created in a D365 sandbox legal entity (never production).'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageCustomerCollections(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageCustomerCollections'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-customer-collections-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageCustomerCollections().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
