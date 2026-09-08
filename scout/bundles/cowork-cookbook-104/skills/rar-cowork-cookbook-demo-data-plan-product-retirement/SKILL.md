---
name: "rar-cowork-cookbook-demo-data-plan-product-retirement"
description: "Generates 25 realistic plan-product-retirement demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_product_retirement", "rar_sha256": "fb19b62c0afad2ccb23245f863bd643c0bfcab9f3921c27f04c3a1870e95428c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
