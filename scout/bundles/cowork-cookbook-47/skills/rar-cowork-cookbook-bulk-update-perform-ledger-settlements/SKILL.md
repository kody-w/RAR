---
name: "rar-cowork-cookbook-bulk-update-perform-ledger-settlements"
description: "Applies a bulk field update to perform ledger settlements records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_ledger_settlements", "rar_sha256": "34f146af54e024ac9c18926be2b0fefb460968286b97ec31d89a89b189bc3685", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_perform_ledger_settlements`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_perform_ledger_settlements_agent.py` and in the RCI capsule.

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

Perform ledger settlements Bulk Field Update — Applies a bulk field update to perform ledger settlements records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-ledger-settlements
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against, e.g. USMF (sandbox first).",
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
      "description": "List of perform ledger settlements record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_perform_ledger_settlements_agent.py` and embedded as the fenced Python below (sha256 34f146af54e024ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_perform_ledger_settlements_agent.py` first:

```bash
python3 bulk_update_perform_ledger_settlements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_perform_ledger_settlements_agent.py   # or on stdin
python3 bulk_update_perform_ledger_settlements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform ledger settlements Bulk Field Update — Applies a bulk field update to perform ledger settlements records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-ledger-settlements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_perform_ledger_settlements',
    "version": '3.0.3',
    "display_name": 'Perform ledger settlements Bulk Field Update',
    "description": 'Applies a bulk field update to perform ledger settlements records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.',
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
        "upstream_slug": 'bulk-update-perform-ledger-settlements',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-perform-ledger-settlements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a5179c6a875b78af',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/perform-ledger-settlements'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-perform-ledger-settlements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against, e.g. USMF (sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of perform ledger settlements record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when perform ledger settlements records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to perform ledger settlements records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to perform ledger settlements records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.', 'example_request': 'Bulk update these perform ledger settlements records in USMF sandbox — here are the IDs and new values; show me a dry run first.', 'inputs': [{'description': 'Dynamics 365 legal entity to run against, e.g. USMF (sandbox first).', 'name': 'legal_entity'}, {'description': 'List of perform ledger settlements record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field across many perform ledger settlements records at once and want a before/after preview and approval step first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePerformLedgerSettlements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePerformLedgerSettlements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against, e.g. USMF (sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of perform ledger settlements record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePerformLedgerSettlements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
