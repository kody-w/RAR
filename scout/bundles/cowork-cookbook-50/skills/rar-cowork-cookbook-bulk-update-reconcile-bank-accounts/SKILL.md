---
name: "rar-cowork-cookbook-bulk-update-reconcile-bank-accounts"
description: "Applies a bulk field update to Dynamics 365 F&SCM reconcile bank accounts records in legal entity USMF via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reconcile_bank_accounts", "rar_sha256": "a9ae36df15e86a50788188a60d48b2f3ffa1faa6860494a2a61950aae0ccbee6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_reconcile_bank_accounts`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_reconcile_bank_accounts_agent.py` and in the RCI capsule.

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

Reconcile bank accounts Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM reconcile bank accounts records in legal entity USMF via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reconcile-bank-accounts
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are applied.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF, sandbox first.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to each listed record.",
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
      "description": "List of reconcile bank accounts record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reconcile_bank_accounts_agent.py` and embedded as the fenced Python below (sha256 a9ae36df15e86a50…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reconcile_bank_accounts_agent.py` first:

```bash
python3 bulk_update_reconcile_bank_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_reconcile_bank_accounts_agent.py   # or on stdin
python3 bulk_update_reconcile_bank_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile bank accounts Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM reconcile bank accounts records in legal entity USMF via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reconcile-bank-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_reconcile_bank_accounts',
    "version": '3.0.3',
    "display_name": 'Reconcile bank accounts Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM reconcile bank accounts records in legal entity USMF via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a',
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
        "upstream_slug": 'bulk-update-reconcile-bank-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-reconcile-bank-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0834676a6e2fe32b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/reconcile-bank-accounts'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-reconcile-bank-accounts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF, sandbox first.', 'new_values': 'The field(s) and new value(s) to apply to each listed record.', 'record_ids': 'List of reconcile bank accounts record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when reconcile bank accounts records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to reconcile bank accounts records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM reconcile bank accounts records in legal entity USMF via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a', 'example_request': 'Bulk update these reconcile bank accounts records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of reconcile bank accounts record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each listed record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF, sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of reconcile bank accounts records in a D365 sandbox, with a reviewable preview before write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateReconcileBankAccounts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReconcileBankAccounts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF, sandbox first.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each listed record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of reconcile bank accounts record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateReconcileBankAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
