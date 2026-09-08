---
name: "rar-cowork-cookbook-demo-data-trace-manufactured-goods"
description: "Generates 25 realistic demo records for trace manufactured goods in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_trace_manufactured_goods", "rar_sha256": "510b02355c3ae42d3ade9c548f6b48304ec696238933a178656d2509ee2efe97", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_trace_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `demo_data_trace_manufactured_goods_agent.py` and in the RCI capsule.

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

Trace manufactured goods Demo Data Generator — Generates 25 realistic demo records for trace manufactured goods in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-trace-manufactured-goods
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
      "description": "Sandbox D365 legal entity to write into (default USMF); must not be production.",
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-trace-manufactured-goods-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_trace_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 510b02355c3ae42d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_trace_manufactured_goods_agent.py` first:

```bash
python3 demo_data_trace_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_trace_manufactured_goods_agent.py   # or on stdin
python3 demo_data_trace_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Trace manufactured goods Demo Data Generator — Generates 25 realistic demo records for trace manufactured goods in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-trace-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_trace_manufactured_goods',
    "version": '3.0.3',
    "display_name": 'Trace manufactured goods Demo Data Generator',
    "description": "Generates 25 realistic demo records for trace manufactured goods in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-trace-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-trace-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ec4e0e716d770072',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/trace-manufactured-goods'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-trace-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-trace-manufactured-goods-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic trace manufactured goods data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for trace manufactured goods. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-trace-manufactured-goods-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic trace manufactured goods records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for trace manufactured goods in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo trace manufactured goods records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-trace-manufactured-goods-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for trace manufactured goods in a D365 sandbox tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataTraceManufacturedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTraceManufacturedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-trace-manufactured-goods-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataTraceManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
