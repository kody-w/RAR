---
name: "rar-cowork-cookbook-demo-data-allocate-goods"
description: "Generates 25 realistic demo allocate-goods records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_allocate_goods", "rar_sha256": "a028578e0e589311d5559f3fb4136e8621d5bbd08421f92f4499163cbb77cb2c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_allocate_goods`. The original RAPP
agent is preserved byte-for-byte in `demo_data_allocate_goods_agent.py` and in the RCI capsule.

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

Allocate goods Demo Data Generator — Generates 25 realistic demo allocate-goods records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-allocate-goods
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
      "description": "Number of demo allocate goods records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging workbook filename, e.g. demo-data-allocate-goods-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_allocate_goods_agent.py` and embedded as the fenced Python below (sha256 a028578e0e589311…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_allocate_goods_agent.py` first:

```bash
python3 demo_data_allocate_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_allocate_goods_agent.py   # or on stdin
python3 demo_data_allocate_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate goods Demo Data Generator — Generates 25 realistic demo allocate-goods records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-allocate-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_allocate_goods',
    "version": '3.0.3',
    "display_name": 'Allocate goods Demo Data Generator',
    "description": "Generates 25 realistic demo allocate-goods records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each record's primary key.",
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
        "upstream_slug": 'demo-data-allocate-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-allocate-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3e5e92c714439dc8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/allocate-goods'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-allocate-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'record_count': 'Number of demo allocate goods records to generate (default 25).', 'workbook_name': 'Excel staging workbook filename, e.g. demo-data-allocate-goods-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic allocate goods data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for allocate goods. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-allocate-goods-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic allocate goods records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo allocate-goods records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each record's primary key.", 'example_request': 'Generate 25 demo allocate goods records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo allocate goods records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging workbook filename, e.g. demo-data-allocate-goods-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or training data for allocate goods in a D365 sandbox tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAllocateGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAllocateGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo allocate goods records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging workbook filename, e.g. demo-data-allocate-goods-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAllocateGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
