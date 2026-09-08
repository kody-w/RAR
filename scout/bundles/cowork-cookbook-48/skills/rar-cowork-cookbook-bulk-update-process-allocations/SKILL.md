---
name: "rar-cowork-cookbook-bulk-update-process-allocations"
description: "Applies a bulk field update to Dynamics 365 F&SCM process allocations records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitti"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_process_allocations", "rar_sha256": "1121482be2fd02a3020aa918d2cad54ba06b3c2f3688a6809ce07aec1812994a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_process_allocations`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_process_allocations_agent.py` and in the RCI capsule.

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

Process allocations Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM process allocations records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitti

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-process-allocations
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
      "description": "Explicit user approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "field_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; sandbox environment first.",
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
      "description": "List of process allocations record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_process_allocations_agent.py` and embedded as the fenced Python below (sha256 1121482be2fd02a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_process_allocations_agent.py` first:

```bash
python3 bulk_update_process_allocations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_process_allocations_agent.py   # or on stdin
python3 bulk_update_process_allocations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process allocations Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM process allocations records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitti

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-process-allocations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_process_allocations',
    "version": '3.0.3',
    "display_name": 'Process allocations Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM process allocations records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitti',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-process-allocations',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-process-allocations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dce8b6cab07d177e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/process-allocations'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-process-allocations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'field_values': 'The field(s) and new value(s) to apply to each record.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox environment first.', 'record_ids': 'List of process allocations record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when process allocations records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to process allocations records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM process allocations records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitti', 'example_request': 'Bulk update these process allocation record IDs in USMF sandbox with a new value — show me the dry-run first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment first.', 'name': 'legal_entity'}, {'description': 'List of process allocations record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'field_values'}, {'description': 'Explicit user approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs to change the same field(s) across a known list of process allocations records in D365 (sandbox), with a reviewable preview before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateProcessAllocations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateProcessAllocations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'field_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of process allocations record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateProcessAllocations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
