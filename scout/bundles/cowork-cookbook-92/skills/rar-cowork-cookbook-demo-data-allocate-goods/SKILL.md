---
name: "rar-cowork-cookbook-demo-data-allocate-goods"
description: "Generates 25 realistic demo allocate-goods records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_allocate_goods", "rar_sha256": "a028578e0e589311d5559f3fb4136e8621d5bbd08421f92f4499163cbb77cb2c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
