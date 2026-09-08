---
name: "rar-cowork-cookbook-demo-data-return-goods-to-vendor"
description: "Generates 25 realistic return-goods-to-vendor demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_return_goods_to_vendor", "rar_sha256": "af359e3a003ca51a7018e370c52839cfb27eac116b289e5b83c9032e417fdf73", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_return_goods_to_vendor`. The original RAPP
agent is preserved byte-for-byte in `demo_data_return_goods_to_vendor_agent.py` and in the RCI capsule.

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

Return goods to vendor Demo Data Generator — Generates 25 realistic return-goods-to-vendor demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor
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
      "description": "Sandbox D365 legal entity to create records in (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-return-goods-to-vendor-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_return_goods_to_vendor_agent.py` and embedded as the fenced Python below (sha256 af359e3a003ca51a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_return_goods_to_vendor_agent.py` first:

```bash
python3 demo_data_return_goods_to_vendor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_return_goods_to_vendor_agent.py   # or on stdin
python3 demo_data_return_goods_to_vendor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Return goods to vendor Demo Data Generator — Generates 25 realistic return-goods-to-vendor demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_return_goods_to_vendor',
    "version": '3.0.3',
    "display_name": 'Return goods to vendor Demo Data Generator',
    "description": "Generates 25 realistic return-goods-to-vendor demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each record's primary key.",
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
        "upstream_slug": 'demo-data-return-goods-to-vendor',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4723df33d826a25d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/return-goods-to-vendor'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-return-goods-to-vendor', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-return-goods-to-vendor-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic return goods to vendor data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for return goods to vendor. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-return-goods-to-vendor-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic return goods to vendor records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic return-goods-to-vendor demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each record's primary key.", 'example_request': 'Generate 25 return goods to vendor demo records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-return-goods-to-vendor-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use to populate a D365 sandbox with organic-looking return goods to vendor demo data for training or pilot scenarios. Sandbox only, never production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataReturnGoodsToVendor(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReturnGoodsToVendor'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-return-goods-to-vendor-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataReturnGoodsToVendor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
