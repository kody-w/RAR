---
name: "rar-cowork-cookbook-demo-data-maintain-product-costs"
description: "Generates 25 realistic demo product-cost records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_maintain_product_costs", "rar_sha256": "1ed609ae6d319761341d79fb89a953a88c2efb986ca2c472360a858f2264630d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_maintain_product_costs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_maintain_product_costs_agent.py` and in the RCI capsule.

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

Maintain product costs Demo Data Generator — Generates 25 realistic demo product-cost records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-maintain-product-costs
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
      "description": "Number of demo product cost records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-maintain-product-costs-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_maintain_product_costs_agent.py` and embedded as the fenced Python below (sha256 1ed609ae6d319761…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_maintain_product_costs_agent.py` first:

```bash
python3 demo_data_maintain_product_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_maintain_product_costs_agent.py   # or on stdin
python3 demo_data_maintain_product_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain product costs Demo Data Generator — Generates 25 realistic demo product-cost records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-maintain-product-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_maintain_product_costs',
    "version": '3.0.3',
    "display_name": 'Maintain product costs Demo Data Generator',
    "description": "Generates 25 realistic demo product-cost records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-maintain-product-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-maintain-product-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a0019983e6c4de8d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/maintain-product-costs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-maintain-product-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo product cost records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-maintain-product-costs-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic maintain product costs data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for maintain product costs. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-maintain-product-costs-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic maintain product costs records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo product-cost records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.", 'example_request': 'Generate 25 demo product cost records in USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo product cost records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-maintain-product-costs-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training product cost data created in a D365 sandbox legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataMaintainProductCosts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMaintainProductCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo product cost records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-maintain-product-costs-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataMaintainProductCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
