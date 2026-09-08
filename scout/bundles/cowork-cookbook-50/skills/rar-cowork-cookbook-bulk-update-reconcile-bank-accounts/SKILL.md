---
name: "rar-cowork-cookbook-bulk-update-reconcile-bank-accounts"
description: "Applies a bulk field update to Dynamics 365 F&SCM reconcile bank accounts records in legal entity USMF via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reconcile_bank_accounts", "rar_sha256": "a9ae36df15e86a50788188a60d48b2f3ffa1faa6860494a2a61950aae0ccbee6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
