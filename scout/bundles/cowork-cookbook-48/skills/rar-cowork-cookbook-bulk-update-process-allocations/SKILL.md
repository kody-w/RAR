---
name: "rar-cowork-cookbook-bulk-update-process-allocations"
description: "Applies a bulk field update to Dynamics 365 F&SCM process allocations records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitti"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_process_allocations", "rar_sha256": "1121482be2fd02a3020aa918d2cad54ba06b3c2f3688a6809ce07aec1812994a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
