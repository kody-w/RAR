---
name: "rar-cowork-cookbook-bulk-update-define-accounts-receivable-strategy"
description: "Applies a bulk field update to accounts receivable records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_accounts_receivable_strategy", "rar_sha256": "92febba9850a5372b92937c2c7810d192117956fa7277ed28cefd30686fb6e60", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_accounts_receivable_strategy`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_accounts_receivable_strategy_agent.py` and in the RCI capsule.

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

Define accounts receivable strategy Bulk Field Update — Applies a bulk field update to accounts receivable records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy
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
      "description": "Dynamics 365 legal entity to run against (defaults to USMF sandbox).",
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
      "description": "List of accounts receivable record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_accounts_receivable_strategy_agent.py` and embedded as the fenced Python below (sha256 92febba9850a5372…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_accounts_receivable_strategy_agent.py` first:

```bash
python3 bulk_update_define_accounts_receivable_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_accounts_receivable_strategy_agent.py   # or on stdin
python3 bulk_update_define_accounts_receivable_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define accounts receivable strategy Bulk Field Update — Applies a bulk field update to accounts receivable records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_accounts_receivable_strategy',
    "version": '3.0.3',
    "display_name": 'Define accounts receivable strategy Bulk Field Update',
    "description": 'Applies a bulk field update to accounts receivable records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a',
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
        "upstream_slug": 'bulk-update-define-accounts-receivable-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e69a1c9d53f0ead',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-accounts-receivable-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-define-accounts-receivable-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (defaults to USMF sandbox).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of accounts receivable record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define accounts receivable strategy records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define accounts receivable strategy records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to accounts receivable records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a', 'example_request': 'Bulk-update these AR record IDs in USMF sandbox with the new credit limit - show me the dry-run first.', 'inputs': [{'description': 'List of accounts receivable record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against (defaults to USMF sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many accounts receivable records at once and want a reviewable before/after preview prior to writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineAccountsReceivableStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineAccountsReceivableStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (defaults to USMF sandbox).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of accounts receivable record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineAccountsReceivableStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
