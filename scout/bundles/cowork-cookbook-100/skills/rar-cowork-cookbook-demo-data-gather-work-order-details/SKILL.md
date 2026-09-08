---
name: "rar-cowork-cookbook-demo-data-gather-work-order-details"
description: "Generates 25 realistic demo work order detail records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_gather_work_order_details", "rar_sha256": "6f2632e93892b55e3eba3fee263493c5fe6b33eec1ef26665d2de4a436f1d158", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
