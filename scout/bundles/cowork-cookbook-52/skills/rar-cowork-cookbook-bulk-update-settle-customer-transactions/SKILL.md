---
name: "rar-cowork-cookbook-bulk-update-settle-customer-transactions"
description: "Applies a bulk field update to settle customer transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_settle_customer_transactions", "rar_sha256": "5626452acec355bd30507e2c41bf5302ff6932f476ac82357c73ac49f1c67d19", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_settle_customer_transactions`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_settle_customer_transactions_agent.py` and in the RCI capsule.

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

Settle customer transactions Bulk Field Update — Applies a bulk field update to settle customer transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-settle-customer-transactions
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
      "description": "Explicit approval after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; sandbox only.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
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
      "description": "List of settle customer transactions record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_settle_customer_transactions_agent.py` and embedded as the fenced Python below (sha256 5626452acec355bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_settle_customer_transactions_agent.py` first:

```bash
python3 bulk_update_settle_customer_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_settle_customer_transactions_agent.py   # or on stdin
python3 bulk_update_settle_customer_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Settle customer transactions Bulk Field Update — Applies a bulk field update to settle customer transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-settle-customer-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_settle_customer_transactions',
    "version": '3.0.3',
    "display_name": 'Settle customer transactions Bulk Field Update',
    "description": 'Applies a bulk field update to settle customer transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-settle-customer-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-settle-customer-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c77b061721e06fef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/settle-customer-transactions'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-settle-customer-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox only.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of settle customer transactions record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when settle customer transactions records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to settle customer transactions records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to settle customer transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk update these settle customer transaction IDs in USMF sandbox with the new value — show me the dry run first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF; sandbox only.', 'name': 'legal_entity'}, {'description': 'List of settle customer transactions record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to update many settle customer transactions records at once from a list of record IDs, with a reviewable preview before any data is written.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateSettleCustomerTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateSettleCustomerTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox only.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of settle customer transactions record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateSettleCustomerTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
