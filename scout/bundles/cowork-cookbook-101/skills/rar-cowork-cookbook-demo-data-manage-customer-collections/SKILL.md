---
name: "rar-cowork-cookbook-demo-data-manage-customer-collections"
description: "Generates 25 realistic customer-collections demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_customer_collections", "rar_sha256": "a8a402fb7266c01f87ea2a1ebba59b51bff3212cc939dedff7c662ef3aa859a9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
