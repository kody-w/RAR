---
name: "rar-cowork-cookbook-demo-data-inspect-inventory"
description: "Generates 25 realistic demo inspect-inventory records for a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_inspect_inventory", "rar_sha256": "4ba99ac8d2834c15f28481faf8c49b1442ff3a4fbfbad86f880b394e2525368c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_inspect_inventory`. The original RAPP
agent is preserved byte-for-byte in `demo_data_inspect_inventory_agent.py` and in the RCI capsule.

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

Inspect inventory Demo Data Generator — Generates 25 realistic demo inspect-inventory records for a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-inspect-inventory
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
      "description": "Number of demo inspect inventory records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-inspect-inventory-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_inspect_inventory_agent.py` and embedded as the fenced Python below (sha256 4ba99ac8d2834c15…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_inspect_inventory_agent.py` first:

```bash
python3 demo_data_inspect_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_inspect_inventory_agent.py   # or on stdin
python3 demo_data_inspect_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Inspect inventory Demo Data Generator — Generates 25 realistic demo inspect-inventory records for a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-inspect-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_inspect_inventory',
    "version": '3.0.3',
    "display_name": 'Inspect inventory Demo Data Generator',
    "description": "Generates 25 realistic demo inspect-inventory records for a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-inspect-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-inspect-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '75045348b949e44e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/inspect-inventory'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-inspect-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo inspect inventory records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-inspect-inventory-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic inspect inventory data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for inspect inventory. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-inspect-inventory-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic inspect inventory records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo inspect-inventory records for a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo inspect inventory records in sandbox USMF, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo inspect inventory records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-inspect-inventory-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training inspect inventory data created in a sandbox D365 legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataInspectInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataInspectInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo inspect inventory records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-inspect-inventory-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataInspectInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
