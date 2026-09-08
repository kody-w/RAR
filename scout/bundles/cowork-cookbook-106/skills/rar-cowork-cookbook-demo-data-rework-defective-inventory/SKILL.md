---
name: "rar-cowork-cookbook-demo-data-rework-defective-inventory"
description: "Generates 25 realistic rework-defective-inventory demo records for a D365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_rework_defective_inventory", "rar_sha256": "ca82f8e614853ce8025555d61aa7e44f48f7ac7436ebd2f07afebfd43b798ff7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
