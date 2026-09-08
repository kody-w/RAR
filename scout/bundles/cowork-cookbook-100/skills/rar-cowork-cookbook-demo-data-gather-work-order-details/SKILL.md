---
name: "rar-cowork-cookbook-demo-data-gather-work-order-details"
description: "Generates 25 realistic demo work order detail records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_gather_work_order_details", "rar_sha256": "6f2632e93892b55e3eba3fee263493c5fe6b33eec1ef26665d2de4a436f1d158", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_gather_work_order_details`. The original RAPP
agent is preserved byte-for-byte in `demo_data_gather_work_order_details_agent.py` and in the RCI capsule.

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

Gather work order details Demo Data Generator — Generates 25 realistic demo work order detail records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-gather-work-order-details
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
      "description": "Excel workbook filename used to stage records before creation, e.g. demo-data-gather-work-order-details-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_gather_work_order_details_agent.py` and embedded as the fenced Python below (sha256 6f2632e93892b55e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_gather_work_order_details_agent.py` first:

```bash
python3 demo_data_gather_work_order_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_gather_work_order_details_agent.py   # or on stdin
python3 demo_data_gather_work_order_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Gather work order details Demo Data Generator — Generates 25 realistic demo work order detail records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-gather-work-order-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_gather_work_order_details',
    "version": '3.0.3',
    "display_name": 'Gather work order details Demo Data Generator',
    "description": "Generates 25 realistic demo work order detail records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-gather-work-order-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-gather-work-order-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '944ebf1034839553',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/gather-work-order-details'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-gather-work-order-details', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel workbook filename used to stage records before creation, e.g. demo-data-gather-work-order-details-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic gather work order details data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for gather work order details. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-gather-work-order-details-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic gather work order details records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo work order detail records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.", 'example_request': 'Generate 25 demo work order detail records in the USMF sandbox, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel workbook filename used to stage records before creation, e.g. demo-data-gather-work-order-details-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo work order detail data created in a D365 sandbox legal entity for training or pilot scenarios. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataGatherWorkOrderDetails(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataGatherWorkOrderDetails'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel workbook filename used to stage records before creation, e.g. demo-data-gather-work-order-details-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataGatherWorkOrderDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
