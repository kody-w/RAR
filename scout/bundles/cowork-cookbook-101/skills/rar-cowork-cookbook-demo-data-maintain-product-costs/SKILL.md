---
name: "rar-cowork-cookbook-demo-data-maintain-product-costs"
description: "Generates 25 realistic demo product-cost records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_maintain_product_costs", "rar_sha256": "1ed609ae6d319761341d79fb89a953a88c2efb986ca2c472360a858f2264630d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObWJbtX9G7HdGZ2bKvGIQAV1TEYxZIAsQgAekMJzOIUQwClJ3/vQ/SvbazKqurKuJ9enLYkuCcffa41t5Gv724fZdUzcunFz10y4Xg5nmahM3CLYMFUw1Vk4G3KvPA34VflV2Ten1XNe3Lh5cgbP0mrbu0KsF2ISzDxu3CdoFgiyZ087TtUn8RhEW1qJsq6P3uo1+1HbjnV03QLtJy4S5acI5XjQsW3WAL/j915rDIw9jNF2HZpd20+DEII7fPu4WpH/ifPizazo3BEV0SFg8B5YIb/TBfzIo+dIzSpu0+LHygQfe28MP8bwnO7fqmbBeh6yeLMhzeFPmhBeqlhdtMiyycXoFd4egWdR62L59+/uXDSwo+v3z67cXP3RZcemGBQazbuQc3LTvwV33axgDTZqfkbhmDVfUEvFqC73XYRFVTgEvAksXbtx/bMI8+LP7rv7LBbeL2p0+fy8Xb6/PL/Efry1npRVe5bRcGC9+tXS/NgUdeF1Q+uFP71RzgQxCUMn597vwmqaoXf53v/fg85DUOux8/v1T1HCUQss8vPy2qBpzX9PPn11lK/eNPr3k1hM2PP32T0/beJfS7WRjQ+vXL2/c3sWDht6VptPiiqxzzdhZwcFqHQPh39s2vp+pv4t5c8uW5+Meq/rD4c8mzPX8F+j7TzgNy/1ws8AHY+fJ6qdLyx7czmuoWlm7phz/+9I/E+knoZ3PS/ktyf34KTkI3AN56cwnIzzkEvyyWb7Z9lfmPj61Bwvw7loDl78d9ddQ/kv2I7N+IztMSlMV7LP9U3J9tWP518fM/tO1/2/BhEX0GNZOnN5B3Xh5+Wvz2SJGffwi+Xfzhl9+B6H8qRq/6xn9I+FK4ZRqFbffly88/tI/LP/zy8w99DbI4dIsvfZP/mcw/8+vjnD948G3Vj3/cC843y6yshnLxtYYWv1X1/2l+f12cANwF3663nxbfV+L8Wi5mI94Pfbrgu2psga7f+fGnl98B8pTAGgAt822AH//xH4tD6jdVW0XdQverHkBpD1CyCGfljSQFkPoAPGAA8GubAse+rQP5P0d41riKFr/+X/8B7ACOn8C+mkH6SwBADfj1iWpf3iD7ywzZ7a+vCwPIrZo0TksAzhqlqp9LgMRlN59ZN2EbNjeAU97UhR9BOX+cP8wA/es/E/3lIeW1nn59UE76xD2NEWfMa/s8fJ2tO88A/rTFB5gfjqHfgwPyygfaRCkA6w/A6rbKbwAzZ0+0WZrniyAFqALYanrIBt76NAv79ddfPbdNPpdPkEYXTxprV2DBV3UWHz8Cs6I8jZPucxn6SbX44bfff1j89+J/2/UQPp+hArJ4iwXQUNIVeQFqqy/Aspn5AKi7wSMWv/3+5lwgBhDoAkQujdInc801kIXBu6f1LfURwTYLLwQeBt4t6qrpAPIv0u51IUaLr/qCQ+dbMzckM+MGYR2WQVj6E5DqAnO+erKsOkDBXdpG04dF34aPU3/1GvehYgGK3O1+XRwYFTBRlYN/ZjUfi8DmqkyB+7/mwfM6ENIASqXfRbwu5DkbF7XbuHXSuG9nRO4zLoCB3rcD4e7My5/LmXLD2VWP0ni6J57bi7mfeIT04xxz0I8UAAeerUT3vsad+dJ48GbzuWzf0t5twgffA1WmRdynwUwGf3lLqTap+jx4+A9oOkt6i0LwFpVHDr4T/ns3s3jk72LuBxZzQ7B464BmUu0RCF4v/j9piWbjKUHQOIEyOHbByYZmP4MyN4Rz8J495KwcyMxnAX7rWN5R6R2cP5d5CjKsmf7yXPkI5duaJ+D1DfC8RmkP+cDjICiz3Eeaz2nbNHOBuJ/Ldxb4ANz2gDwQaYAJoGbmVH0/cL77rmkCCn/+/q0jeLN5RgiQyou693IQoygMA8/1M6BVM5fqW0RBzodz2Q5JCjz2vVVzdIC/gPwFUCIFiQGY4vUrMj/vvqv+h43Pxmfe8mgKe1CpzUMA0COcFZyxa0g7AFhu9+y/gZ2fHkKAGUXdzbZ7oFaeYZ3zuAmvfdqm3YyLT7+GNcDkj/P709L5ajjWoDyAs0AR1D3w7qNsZkQpQFsDdACpCqqoSMtn4r454SHQLWYMABj7lkNPiY/LbwaFj1qb+el942zIvGem/EUEVAdXpu+hwvizNAHyZup4eu1vM+3rabPsGS5bAHngxPe7z97g9Unvz/5h8S73098NOD/+ezPQg7DNPybAp0XSdXX7abV6kuw7x74CsFo9dW0ffPtxJsWP76T48Xs8aP8g92nyp8W/p9sfRLzVxqcF/Aq9QvOt/Vtuvb2AK5iPtP1xPd/9XGrhNygFx1cFSK45cBMg+K+8974EkF/cAIACi5882M70OQB8eQA/iMLn8vtkn4sN8EoZz8nZVt+BwKMBAIn/DNpXfgK3yg6cHcztYhzOI9qjNNrw5VPZ5/mHlxKk3T8fzWYKKuaEbud5DjgcNF9dGj6+PfBh7OaPfxxrlccHN38FQA9k5u33SfdGHDNxflcbTxuBbT444cMieKAuyEdg43z4XFduCxIV5OhsSzfVs/LPKW7u+x5o/+WJ9n+vkP49PfyBGADkdaDJCLu/oYi/LIoekMzsSy98J56ZWP/s8K8d6d+ffAbNwHxIUH2aefHDG/qAdzBFAH55HwiAyW8j2mOaLnsw/f48DyNzDB5b5g9gD3j7uunr/yd44csvf6LX06mgZwQt79+rJveFB3INIPP35Lr4A7kCzd9T9puDEOynP3XDO3l+eabW3573ZNiZeWe0fCTvvPDDInyNXxf/rLw/IhCy+QhhH5H165i3459o8LAYYDhgwtl536LyzTfVY2qblQW+7J7/yfDbC0hwdz76LcXf2n6wHEDex3Zud1YABMCB4PuzXMG9f3sgeNvfJi5oSIEAOAw2EOmGmwCFSXwDo2s4wMnII0iXxFCXIHwkjDyS2Pgu4q9xBN1ALoEREYJs1hsUCoC8Z9F/mXu6dNYJI/EIIkkkWsMIFIB4IesgIDZABIYjkEt6LuZhpOt925qlZfBm6NOw2YtfZ5PZIW/2/vbibdZg5XbditTzxayWsLc6457WeCsLIsZ86Hw9LyS9UwqEP/X7urGNhI7Xg4b0DbgCU5Wf6mOdpectanMDQS1HFk/UtiRL43DHJCb1mKAjl+ve69kzd8nvWHvHlhKiCkavHNBLo0GFtIL0c41wp5yRxBQXjyO689JCWZGHU1P4F39Pyv5KRW7RXY0cRghV+oyRilLtdjKVsJpvYvGR9oY9dBlamrng1Y0xfClfcm0QRavOvKmNSmwUVKydRh3taefKk7R2E0vNT5bY3O7kcilUMG9GdbPn+R6TbElS9pk50RffQYucaKGbpjc7ZrVrjxfq6GbbS1+umMDurvehTlSdvZiXrDt73N6nw0617qWXmgpCDKG63ZBBKW1GPzIqnJ/CYtuOBEkAb7RRkdHcimmIWi4SudkhE4FyOs+o94MF2aNqd2vtxOfaMRO66rA+92684gbZ4s6jzB0Git7VflLs2jEoDXoz5ZfCuJi1ehO31MqY1JbKV616NlzmVNv4Zp2VmVbbhQgtKb0lesiq8FC4rNGoERJ8ZMncvBOSRG9uGO0oB/buJjmr6m09bMzIEsXSpBIngwpXl4R+VM0ivhrtyqHPIhMd+YKK48s5g4ecIyseqcm1U+Y3o93uTN2p4jV5sk9cVvnYWuFBztA1zgUnradLzME6Ydo1W1oIDtSK7Nuag24rQ9L7VmMLv4+um1SsFGXMr9FBam9BssXvfF8kK8mQKlE/QtfmsIsv8HHZsLtagRG1Soijet8L5+VFk/Jmr+FS79wqi1tdKlRjlWsZpq3OKhAnSCIBxpySiNa6kG9ox7g7qeNjJ+oqdO2V63ObPuetO3Adgrt1mJqXrWlJTsohO9i/e+IVnY7cHjnW97uGCNW91TS931DWppzSUMCSnULQ5UqjK7FMOyhxWLtdssebdmWx6HS7HHCunjaTbbg+bQx3SGVIsYNV3mW5/IQtuaPoSadM3Y5bjxhSt+kurVESoWOYAj6YI4EZKLLtVbnEj93GIo4Duc0we2l4K3ryGc8Saow5X5pgqB3RuvcjKmbptFPa/c4ppoMUNahCcZR3EQftGMqZglasdZb0TMWprkCHK6JepCKbRp2BrXqJHHO9CwaT0SUG5uNTIKWuxTKKcYZ2HNvRUMu3nsQPt9GSh4NLywp3ZKlI8ItSvqttXNwPxFkpPX5TElRBBB5pgObFTgx2ytPjIXEE4dh3F8psBtLkOjqVxs4/YnJUhFp8Oof3G1+4dAKFbFFJZpxbZmktjaVAcc0w2ZIqY1IxZdR9vb/vsaGa9NbmJlxztsJle+vP+8v+mlHDjmr0s81GJDckooVcA7df8jK3OTtGTSW96GelWjHXuIiHCy7zhAWp66K8rmPYvVR8Ql2p3nGWmH8YT/GKbeQA+N6FcJk8LE8Gwvem6erdgN9Q2JbKOqYvhyu2p+2pd/fB/dx5E6NR6pAdhT7FiBFxCNSoeViIo8NdO6JEiXa+No2HKDASL6G35rnccEtQKYp2ZBpy2h8C9nxYOUYoQUUXm90loc/LA+QdDtQuG3J/v48511jueB/Oed9MNA8YArt5fUe0UrscdgRpajnF0g62mpgW87pNTdhtdRKla+iGuErg67MfIGHmnENzYPGBzkJsp903O/F6t+R+WObhFEW3pcPGEHULjz0nHNDu6Awpz1UI3dE4miiyS1uwexTHMtf211KVXYoZA5HfOVMjFtdBgkseknh8udszokDbngr7FV75yyxhd6aonyp7NFGOZOVrj3p3bL2rI2OnUWzqiPt4SDEcB40+zCzNCxMYjaTX9xGfllUlYtuN6PRJytmKpEq7ehS5pmwCB2dzSZzyc8yv9/stbpjVeI00tIsOFGweO6G/uJ2lk2PfnLLy5FNKeQYxKrQJ8goGvwRslufmakUqXoWpBpGIVJHDxS46StqtGq6QfiENpNC9m1+RchwXAWpe1GC5q2ikw+yg2wsce6hXKzVt1BVAXHi199by7Xgrtqbcn8reMKHDcFexU3u0qWmSHGLbTQTRywx3lYQrbJoihXeonC1XB+doIkjEoBTMbSKxjfjijJlmkui2Sxx4qJVP4lifxJXJ6SyU1LwzxhxwdLZMNCxgUqqis/su2NDU0K0drVKygD5DeStN0hbTRE2cLL47sNGlKyNH0vbmZPsCtPadG4rp6wuGi+mpR+viRPbw/qgcVtGFvsYmx59GwTdHPLwIrMsEgdJNJc31436bXaw9d7qLQ9xMa/9ceFdNvDqmeaVOySDEPBj6ifNyiRJ8rJhMrCjpsV2bfHZS2QY9bc5jJ5PjtVqZV1Mvbim6ma6RrpHutuZ3RJWPGddSRL5dLa2dUFW0lF7o5qDt6Zw2KCnxrwRzyY32OKzgsV9prGQK1yDSEL0Rec0XB3JcsifduPHCuN2caLqTWUKSudNm2nF2H+bY2Xb03dXMnboXCVDAFJsbY72+nTYQ5B42OFV7DFW3+nDc5KOJD714MlpNHySFz42wJc0uNuIbFtuQxmD2TmHdCboZVRlqlyNkOWemveDsFdlpfm15w5miqosSXjdVl7uOt7R1scsLN1+KuWrVgCtsPYg5Mxr6Ju1P9bnBdkByGdrrTcJktWYcDedygsRDZqbD+aopRnGELRYga5hOMMNgpXGl8/0KSUVtUo6TrNxWTlCIsWtfyNQ8JGt2A8GRrU8uEZv8hIaW66WexZHOQLWAoUAv2x73lc0RNHBEE2Be0UW008QRthO5nPZKHFoq+2SAUSlbxZgor7EDdDQsw4rlEVKsnhJRt94J/RkRdGZ3dWiOvx44JtpmNTXpY3fWidSglEG7mBvD4EiGdTCPoH1za2XLS6nL8QFS2gujGYVlohcUja/QARVa61RBiX2MOI65EocqDylbPSKVdLBbn85WEJLpUI5So1/uESu9gI7Kk1zz4K4gnPc63VrvdBt2boZnT5swCytpSmnHP5l0sCdsQ2DInhov7rq2JzS+xSW+IqKLvEsRR4k3Boed6gtL6sIqkiJxTU+Imh2Jvreraq17mLiL0uOVD6f+PGHaShVcgIEZrB3NmoG6Xe/ZFKe7sHhNePhiy7p/zdgCW+HnEaJO/FTg3v1y7BRVdfTMcVDJXYLmKT8kFRQRV74lrvlI7ZIzVeGc2GtXjt1To8LL9A0o1DOjuG8H9IRBV2vL+gru7yHYkZgyOTEyURv1UtqH4kk0uhiqdWItl0amqa0oCxXX4YrrnQIqWyXS1qX3fMUfEntiiuIc3iRopDR58HuePvFmYLCncTl6J6qtWUkNkURFk2AlZUSg3moIeKvGiApFd/p6GYZYtw1Jh3er8JTV3cnX2xa/hrdof0kT9ZbdL64G5uXBPnu1uB856ZZuHdnqi71kmPiJZ+D75bIVi+O2a3XtbkMH/SAm+k2n7yeQTPcd6BKpuG/vesPxZIVAaESFVJHmCNOFpdc1S3zQ7snOSLuBKcpJB8Kn2FjdSUjSDlBqm/hxsvECTDuttFtyNHuLfRpbE+ORuPk848Bid3Lv2C1vvJpLi3paKSy8XIYgaAV+g1V3iUKHycq2Og6HpYSvbwp7Zg+nXZQXsGac2M6SEVKULFGQk0EzoWhd4x3FmdaREQRj5I+NCmVMbfC+v6ovNWB2vFQw+2pJm1VYOki1T07cpKIXjQ27vXpJpaSoqYsLU8W9Zk7HdJPudHbQzqaHnZpMZMzVleyJNo/KZAxuTUHuLUW+nA/F1XZSRGZoPew8uIZyyqxiN166rurSfecixQld364WG0lBksJXApZg2ZCX9So/RvW1h/FtFsRw7dfBWTnt2urCist6M1WYg5vtfm1a6Nj1/DbXtvheHPTisLzfe+2kycTYRLwpwnLPqCNnH3CNWnNMhpjVEcM3G5nfM+YGWsKTRpN0MmxNBR6VKwPmk+pikQeZlHVJd8LeJsNWC0+8qDYcaFSP5yRb93hwtJjonJ2bMlemaM0g58JuyxA3PPkkEMzGvsWarsGWcPMxaosLIx9bp6YzwZy1NLPaE3Q7a0RWX5/3kqmJdaBZO+bIrAt2hDdkyIFJ+lr3bdhGtxvMKMVB4Y2cr45gLs6vsn8OaUTZ9Iy4ZHVcKKNY84Srot+9657p1iYFR2ehTXTQXaP7ZeccrAzZQX56tAdys7nd0+ag9zB0PS9zC++8A+hWMdhBnd2tKnXNd5ekeQdd200W1TAjaZ3uTUopBFaxcx203a1W6ZN4aKErXnkSBKIzkqNrprkqWAdRi/Eeydr4fg236XhvOidjIvlcoEHeCeVtucUo5Wjxxr7EWHx/llbX4NxtqpWSuZDgFjUA77DyNklQWdU+4GshQSxgPwLIjtOQYBpc41551f6iCGFr3AcXhiE68qq2aJStUa6k9VLl0MblYdcdzqPRW9aExZAip1h3PhMHXwtcblyiVnmU+SV+uVc3eEJr1FEyMAjtjTAIg7EyL+USshp45ywNEmKVOj+c3ZsSbgmu9ohpT56T/AT3eL+VPRheFtlm61bIoKL+FeoIF9u266tww279aVUJtnqy1Poi0DVKT1Qla7TPWrBquLcr2oVaKrHLYK8cqeW+9JoNvCZF9dwh+pJcaVv22pZbzyaQ4qZwLMLXqOWFo9OtkSYnk+WWzbqA5kIr8/jMZlHtvgTblmmyHDOLF8jrtFxlN+IspzV1WqIRs7ytDZ1PXI5bEhd0x9rq1oDOvbNiCy0gTR6kE8xoNLQpDX/gdyJl6kl7XScbgYX4SeMvscIoKillsrYBBW02cqkg9XkHJooeiQkcUArr6eyGP3b6Su5906fvSWrs4cTe7pc7qOQv54oNpj2Yte2DJHZaoU4oBMMo5gAaoNWyQymxLJ3msNET0mEyQq+3+pbo971DQl0ku4HpBIp7b5qkQlS1rDpPu/VatdLTGhOWzRY3ZRYuRAOAtkSBMqaIMOr7Q99IxnqCRu7oIl1gXxopcT392JDtCHKo2RMoklxLXgANRzjIV0XoyvACAy/DF0E8Hlazqff8Tlj51G4Zvm8ZEFaGO+20/X2wtzW+LKDDdZyYo0jaWBIGSi8JUK3IASyWzvoemEeZ7tNEji3FPvLdOu3ATBpLFkHr2SWFSguNcS6TTy2G630MXcNgddXWq+i254j7HY7NvXDIJGXqEOOujLLP7xuSZprz+rzdHu4NwbK3Im7u3r03U2cfjNxSvaF0SG+P/ggmDdgtpNpr9wfNR2PHudv7whb68oDhjgYnAULW+4Mq0lhnHJDIJotbsexj3Dl4eXO32I6XDkfHKk1hw7VZyEZXZtc3gxiWmYQAFgurPrztabi4nwtVBuhn+/fGSFoYM1iUVq5S3ZKTWF9ywct6zfbjjSyY676InfCGTCMxyBTPY0cjwBzSBf4BvT2Jqa5zPLjT7gKFVKiRmQU7bZZLJDS40rkXOXLY6x4DreylvIHIFjXOBirfqg7C7uO9O2kQzh1IFFu5WDAlyn3QDvCqtSK22DcQFqWXdXD1N+vtXXAt2MNXJi+h29XlRJLFqT5unE3T7W9Df9PX22sIJhzeXnK3denXSnbOb1AmRarn9vQqcGEDS2GlcIPT2ociPr/D2xHZX/eol5GRwaiHWyCol5VYDHeOZgoji0zuesJsHHL8w5AItYE7ZhQmYM5ZWfAmpoHRtalO92POI220Xk6Mb93THVNsQes8JRWBRTnLmoWuBLAkYJB3aosgHN2tpG5LLl4JgJus9mCNuocne4fUPR4ZQLO6tnbLlDVtdr9yr8u0GfAb7nIeJVvBKBVraaR1fRCmfuBWMFV2Q3Ah/Z0mbOw25bdrYnXyuRa9aV1iYY6JJ0ez8xAYcSPX6zCdydGp0uTK5/SqQjvc6WqtLImu3iF3p3BrZCXxVb0HcIhfBUdcdRNyGN0YmQzBRjcAvxT8BpqlPqwxdIoyAnixOeepd5H2WM1atCbk2aDUDXnGu06J1AOrn5e3M2vU+1GmylMVZtXu0m9QE1Mcdmh23rmuzLKW0SS5N6FcC9sGmcgrqiBWj5Y9RhdndXOevGt/WA3NaR36PRGuCVWIoN4pDPxEOVxt53Z603xsTcs7unOl4Ybi1h00/ULGrmzItjSEoJzzHq5LwDteB5re8rz1bx0qhbzkb3J/e5nQK4ZnpV2a/fW4abc71ZbLs7o9WCcJ8TdDK5yylG60xO0Cz3cinMZ9dBtrxbi0ZaUFTdgdoR13y1jYNusujMwz9l2+VEoXxNsiuUeRzXX36+F4JERBAV4ZEi4uTSX1qaWNYx61ZSu4ZzE1Lz2v2zTHDZ2MbcBEqmGszy1kYiOMumsLmsddy91XIaZF9KZCG5XZb/oKn9ylX228M6TJ8DmPQGVsow20p6MII+oVrNmHzRL2BXS/MaH9LT4GI8EI7HXy5d5zAl/Kjz5swo3vyMUK49kAXSHrKWnLVlWRplAsH77GRsiWVnH3m2Bs3M3dqRMrLZdO0ljKiB5Tsr9oVnItLqOxR/ObELDbDumIE6lDW2tzudAspskAfOP99XRBz27FVHF8DTeMuk9JqVbYEfNhOV/DULVXLM4nXYdQqh3CwWLDaxChMnGkM/tuI497PKfDjgtvt/vW05q0iMhwdeYI0JkkNzzJ0b49kzJFbMH0X23d+xje/KlnukyNjQQrA/0q9nYQaybmUDi6IZtt4qxW93JwTbYfeMFfZaK9zJsBXdk9n9f1ig+14X67CeJAUOMW3rXLU7teC6vhVmpFD5EcR1HUX//68uFlfiz29mT2X/4V2Pw05//ZQ6Xn85/3H3o8HkKGbvDpcdanf12lXz68NH46K/R4cNbmffz2mOlvHpt9/GcP/ubd0/OHVe/Pm58PsDs3nn9u/JKWQd92zfSlrfLHzzzADq9v558otrN6Pnj//inqVyOej0/TuPzSVV+asEub8GX+BeH8840wSN3u/Wv89hwRrJ9AcFK//YJusC9hU892vv1QAJiHvkKv6Mvv/wMO5GZuIC4AAA== -->
