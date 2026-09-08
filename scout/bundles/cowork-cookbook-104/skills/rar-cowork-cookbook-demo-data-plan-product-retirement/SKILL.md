---
name: "rar-cowork-cookbook-demo-data-plan-product-retirement"
description: "Generates 25 realistic plan-product-retirement demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_product_retirement", "rar_sha256": "fb19b62c0afad2ccb23245f863bd643c0bfcab9f3921c27f04c3a1870e95428c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_plan_product_retirement`. The original RAPP
agent is preserved byte-for-byte in `demo_data_plan_product_retirement_agent.py` and in the RCI capsule.

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

Plan product retirement Demo Data Generator — Generates 25 realistic plan-product-retirement demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-product-retirement
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-plan-product-retirement-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_product_retirement_agent.py` and embedded as the fenced Python below (sha256 fb19b62c0afad2cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_product_retirement_agent.py` first:

```bash
python3 demo_data_plan_product_retirement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_product_retirement_agent.py   # or on stdin
python3 demo_data_plan_product_retirement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan product retirement Demo Data Generator — Generates 25 realistic plan-product-retirement demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-product-retirement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_product_retirement',
    "version": '3.0.3',
    "display_name": 'Plan product retirement Demo Data Generator',
    "description": "Generates 25 realistic plan-product-retirement demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-plan-product-retirement',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-product-retirement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6a765b3a3402c3e9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/plan-product-retirement'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-plan-product-retirement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-plan-product-retirement-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic plan product retirement data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for plan product retirement. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-plan-product-retirement-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic plan product retirement records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic plan-product-retirement demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 plan product retirement demo records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-plan-product-retirement-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need seeded plan product retirement demo data in a D365 sandbox for training or pilot scenarios. Sandbox only — never production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataPlanProductRetirement(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanProductRetirement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-plan-product-retirement-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataPlanProductRetirement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
