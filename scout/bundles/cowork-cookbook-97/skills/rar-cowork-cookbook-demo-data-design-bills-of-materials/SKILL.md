---
name: "rar-cowork-cookbook-demo-data-design-bills-of-materials"
description: "Generates 25 realistic design bill-of-materials demo records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_design_bills_of_materials", "rar_sha256": "ddf5de5d532b18193e3673c8b537f17502264a6f2d463a206ce42cf5e7137536", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_design_bills_of_materials`. The original RAPP
agent is preserved byte-for-byte in `demo_data_design_bills_of_materials_agent.py` and in the RCI capsule.

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

Design bills of materials Demo Data Generator — Generates 25 realistic design bill-of-materials demo records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-design-bills-of-materials
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
      "description": "Sandbox D365 legal entity to create records in (default USMF).",
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
      "description": "Excel staging file name, e.g. demo-data-design-bills-of-materials-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_design_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 ddf5de5d532b1819…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_design_bills_of_materials_agent.py` first:

```bash
python3 demo_data_design_bills_of_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_design_bills_of_materials_agent.py   # or on stdin
python3 demo_data_design_bills_of_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design bills of materials Demo Data Generator — Generates 25 realistic design bill-of-materials demo records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-design-bills-of-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_design_bills_of_materials',
    "version": '3.0.3',
    "display_name": 'Design bills of materials Demo Data Generator',
    "description": 'Generates 25 realistic design bill-of-materials demo records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new primary key.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-design-bills-of-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-design-bills-of-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '279e1f6ab8127dc6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/design-bills-of-materials'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-design-bills-of-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-design-bills-of-materials-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic design bills of materials data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for design bills of materials. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-design-bills-of-materials-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic design bills of materials records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates 25 realistic design bill-of-materials demo records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new primary key.', 'example_request': 'Generate 25 demo design bills of materials in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-design-bills-of-materials-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for design bills of materials in a D365 F&SCM sandbox tenant. Sandbox only - never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDesignBillsOfMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDesignBillsOfMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-design-bills-of-materials-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDesignBillsOfMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
