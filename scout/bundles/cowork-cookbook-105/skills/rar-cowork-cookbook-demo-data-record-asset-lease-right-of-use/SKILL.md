---
name: "rar-cowork-cookbook-demo-data-record-asset-lease-right-of-use"
description: "Generates 25 realistic demo asset lease right-of-use records in a D365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_asset_lease_right_of_use", "rar_sha256": "2c8349f2735307623a0d6e667b884e129780e646cf65c69764e57f5d2f68cfdf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_record_asset_lease_right_of_use`. The original RAPP
agent is preserved byte-for-byte in `demo_data_record_asset_lease_right_of_use_agent.py` and in the RCI capsule.

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

Record asset lease right-of-use Demo Data Generator — Generates 25 realistic demo asset lease right-of-use records in a D365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-asset-lease-right-of-use
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
      "description": "Sandbox D365 legal entity to write to (default USMF).",
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
      "description": "Excel staging file name, e.g. demo-data-record-asset-lease-right-of-use-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_record_asset_lease_right_of_use_agent.py` and embedded as the fenced Python below (sha256 2c8349f273530762…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_record_asset_lease_right_of_use_agent.py` first:

```bash
python3 demo_data_record_asset_lease_right_of_use_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_record_asset_lease_right_of_use_agent.py   # or on stdin
python3 demo_data_record_asset_lease_right_of_use_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record asset lease right-of-use Demo Data Generator — Generates 25 realistic demo asset lease right-of-use records in a D365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-asset-lease-right-of-use
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_record_asset_lease_right_of_use',
    "version": '3.0.3',
    "display_name": 'Record asset lease right-of-use Demo Data Generator',
    "description": "Generates 25 realistic demo asset lease right-of-use records in a D365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-record-asset-lease-right-of-use',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-record-asset-lease-right-of-use',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3d5c2d8a7c5f4121',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/record-asset-lease-right-of-use'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-record-asset-lease-right-of-use', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-record-asset-lease-right-of-use-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic record asset lease right-of-use data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for record asset lease right-of-use. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-record-asset-lease-right-of-use-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic record asset lease right-of-use records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo asset lease right-of-use records in a D365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo asset lease right-of-use records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-record-asset-lease-right-of-use-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for asset lease right-of-use in a D365 sandbox tenant. Sandbox only — never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataRecordAssetLeaseRightOfUse(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRecordAssetLeaseRightOfUse'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-record-asset-lease-right-of-use-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataRecordAssetLeaseRightOfUse().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
