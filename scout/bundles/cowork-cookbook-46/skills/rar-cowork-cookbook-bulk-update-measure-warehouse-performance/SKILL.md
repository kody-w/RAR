---
name: "rar-cowork-cookbook-bulk-update-measure-warehouse-performance"
description: "Applies a bulk field update to measure warehouse performance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_measure_warehouse_performance", "rar_sha256": "cfea00f5816bb9de2183b286155ac833c2a930c32ed2f21a4372021861603c91", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_measure_warehouse_performance`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_measure_warehouse_performance_agent.py` and in the RCI capsule.

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

Measure warehouse performance Bulk Field Update — Applies a bulk field update to measure warehouse performance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-warehouse-performance
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
    "approval": {
      "description": "Explicit confirmation after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to those records.",
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
    "record_ids": {
      "description": "List of measure warehouse performance record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_measure_warehouse_performance_agent.py` and embedded as the fenced Python below (sha256 cfea00f5816bb9de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_measure_warehouse_performance_agent.py` first:

```bash
python3 bulk_update_measure_warehouse_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_measure_warehouse_performance_agent.py   # or on stdin
python3 bulk_update_measure_warehouse_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure warehouse performance Bulk Field Update — Applies a bulk field update to measure warehouse performance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-warehouse-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_measure_warehouse_performance',
    "version": '3.0.3',
    "display_name": 'Measure warehouse performance Bulk Field Update',
    "description": 'Applies a bulk field update to measure warehouse performance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-measure-warehouse-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-measure-warehouse-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c649fb45670cef12',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/measure-warehouse-performance'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-measure-warehouse-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of measure warehouse performance record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when measure warehouse performance records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to measure warehouse performance records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to measure warehouse performance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing', 'example_request': 'Bulk update these warehouse performance record IDs in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of measure warehouse performance record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit confirmation after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field across many warehouse performance records at once and want a before/after preview to approve before the write is applied.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateMeasureWarehousePerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMeasureWarehousePerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of measure warehouse performance record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateMeasureWarehousePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
