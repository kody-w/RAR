---
name: "rar-cowork-cookbook-demo-data-consolidate-requisitions"
description: "Generates 25 realistic demo consolidate-requisition records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_consolidate_requisitions", "rar_sha256": "bb7d60409832065824a3bc38365340d6969a5634ca26e36654d4a0b751fdb503", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
