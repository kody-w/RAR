---
name: "rar-cowork-cookbook-demo-data-consolidate-requisitions"
description: "Generates 25 realistic demo consolidate-requisition records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_consolidate_requisitions", "rar_sha256": "bb7d60409832065824a3bc38365340d6969a5634ca26e36654d4a0b751fdb503", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_consolidate_requisitions`. The original RAPP
agent is preserved byte-for-byte in `demo_data_consolidate_requisitions_agent.py` and in the RCI capsule.

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

Consolidate requisitions Demo Data Generator — Generates 25 realistic demo consolidate-requisition records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-requisitions
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
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging workbook filename, e.g. demo-data-consolidate-requisitions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_consolidate_requisitions_agent.py` and embedded as the fenced Python below (sha256 bb7d604098320658…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_consolidate_requisitions_agent.py` first:

```bash
python3 demo_data_consolidate_requisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_consolidate_requisitions_agent.py   # or on stdin
python3 demo_data_consolidate_requisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate requisitions Demo Data Generator — Generates 25 realistic demo consolidate-requisition records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-requisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_consolidate_requisitions',
    "version": '3.0.3',
    "display_name": 'Consolidate requisitions Demo Data Generator',
    "description": "Generates 25 realistic demo consolidate-requisition records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-consolidate-requisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-consolidate-requisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '80b89bc99925bdb2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/consolidate-requisitions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-consolidate-requisitions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging workbook filename, e.g. demo-data-consolidate-requisitions-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic consolidate requisitions data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for consolidate requisitions. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-consolidate-requisitions-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic consolidate requisitions records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo consolidate-requisition records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo consolidate requisition records in the USMF sandbox and create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging workbook filename, e.g. demo-data-consolidate-requisitions-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo consolidate requisitions data in a D365 F&SCM sandbox for training or pilot scenarios. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataConsolidateRequisitions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConsolidateRequisitions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging workbook filename, e.g. demo-data-consolidate-requisitions-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataConsolidateRequisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
