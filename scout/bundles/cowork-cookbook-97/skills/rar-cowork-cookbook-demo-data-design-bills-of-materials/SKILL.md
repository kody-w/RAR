---
name: "rar-cowork-cookbook-demo-data-design-bills-of-materials"
description: "Generates 25 realistic design bill-of-materials demo records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_design_bills_of_materials", "rar_sha256": "ddf5de5d532b18193e3673c8b537f17502264a6f2d463a206ce42cf5e7137536", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
