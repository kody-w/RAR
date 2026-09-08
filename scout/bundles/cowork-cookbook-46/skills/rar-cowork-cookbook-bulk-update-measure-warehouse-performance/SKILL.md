---
name: "rar-cowork-cookbook-bulk-update-measure-warehouse-performance"
description: "Applies a bulk field update to measure warehouse performance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_measure_warehouse_performance", "rar_sha256": "cfea00f5816bb9de2183b286155ac833c2a930c32ed2f21a4372021861603c91", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
