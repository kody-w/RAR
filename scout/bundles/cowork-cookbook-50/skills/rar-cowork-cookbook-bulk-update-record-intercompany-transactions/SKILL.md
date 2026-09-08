---
name: "rar-cowork-cookbook-bulk-update-record-intercompany-transactions"
description: "Applies a bulk field update to Dynamics 365 intercompany transaction records in legal entity USMF via the ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_intercompany_transactions", "rar_sha256": "fa1aef8b36e67eb1497d9c6fa8cc673005e1d88c85a22979aea3db26a80e7318", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_record_intercompany_transactions`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_record_intercompany_transactions_agent.py` and in the RCI capsule.

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

Record intercompany transactions Bulk Field Update — Applies a bulk field update to Dynamics 365 intercompany transaction records in legal entity USMF via the ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-intercompany-transactions
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
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (recipe default: USMF, sandbox).",
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
      "description": "List of intercompany transaction record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_record_intercompany_transactions_agent.py` and embedded as the fenced Python below (sha256 fa1aef8b36e67eb1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_record_intercompany_transactions_agent.py` first:

```bash
python3 bulk_update_record_intercompany_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_record_intercompany_transactions_agent.py   # or on stdin
python3 bulk_update_record_intercompany_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record intercompany transactions Bulk Field Update — Applies a bulk field update to Dynamics 365 intercompany transaction records in legal entity USMF via the ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-intercompany-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_record_intercompany_transactions',
    "version": '3.0.3',
    "display_name": 'Record intercompany transactions Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 intercompany transaction records in legal entity USMF via the ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.',
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
        "upstream_slug": 'bulk-update-record-intercompany-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-record-intercompany-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eef5bd29924559ed',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-intercompany-transactions'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-record-intercompany-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (recipe default: USMF, sandbox).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of intercompany transaction record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when record intercompany transactions records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to record intercompany transactions records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 intercompany transaction records in legal entity USMF via the ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.', 'example_request': 'Bulk update these intercompany transaction IDs in USMF sandbox with the new values — show me the dry-run first.', 'inputs': [{'description': 'List of intercompany transaction record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (recipe default: USMF, sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of intercompany transaction record IDs in a D365 sandbox, with a reviewed preview first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateRecordIntercompanyTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRecordIntercompanyTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (recipe default: USMF, sandbox).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of intercompany transaction record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateRecordIntercompanyTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
