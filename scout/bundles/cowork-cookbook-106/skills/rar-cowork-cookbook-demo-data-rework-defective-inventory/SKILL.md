---
name: "rar-cowork-cookbook-demo-data-rework-defective-inventory"
description: "Generates 25 realistic rework-defective-inventory demo records for a D365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_rework_defective_inventory", "rar_sha256": "ca82f8e614853ce8025555d61aa7e44f48f7ac7436ebd2f07afebfd43b798ff7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_rework_defective_inventory`. The original RAPP
agent is preserved byte-for-byte in `demo_data_rework_defective_inventory_agent.py` and in the RCI capsule.

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

Rework defective inventory Demo Data Generator — Generates 25 realistic rework-defective-inventory demo records for a D365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-rework-defective-inventory
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
      "description": "Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-rework-defective-inventory-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_rework_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 ca82f8e614853ce8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_rework_defective_inventory_agent.py` first:

```bash
python3 demo_data_rework_defective_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_rework_defective_inventory_agent.py   # or on stdin
python3 demo_data_rework_defective_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rework defective inventory Demo Data Generator — Generates 25 realistic rework-defective-inventory demo records for a D365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-rework-defective-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_rework_defective_inventory',
    "version": '3.0.3',
    "display_name": 'Rework defective inventory Demo Data Generator',
    "description": "Generates 25 realistic rework-defective-inventory demo records for a D365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-rework-defective-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-rework-defective-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17f70b5e6a59851f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/rework-defective-inventory'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-rework-defective-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-rework-defective-inventory-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic rework defective inventory data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for rework defective inventory. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-rework-defective-inventory-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic rework defective inventory records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic rework-defective-inventory demo records for a D365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo rework defective inventory records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-rework-defective-inventory-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or training data for rework defective inventory in a D365 sandbox tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataReworkDefectiveInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReworkDefectiveInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-rework-defective-inventory-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataReworkDefectiveInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
