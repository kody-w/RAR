---
name: "rar-cowork-cookbook-demo-data-inspect-inventory"
description: "Generates 25 realistic demo inspect-inventory records for a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_inspect_inventory", "rar_sha256": "4ba99ac8d2834c15f28481faf8c49b1442ff3a4fbfbad86f880b394e2525368c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
