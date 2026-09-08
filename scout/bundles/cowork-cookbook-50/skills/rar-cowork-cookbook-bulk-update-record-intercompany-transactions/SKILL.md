---
name: "rar-cowork-cookbook-bulk-update-record-intercompany-transactions"
description: "Applies a bulk field update to Dynamics 365 intercompany transaction records in legal entity USMF via the ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_intercompany_transactions", "rar_sha256": "fa1aef8b36e67eb1497d9c6fa8cc673005e1d88c85a22979aea3db26a80e7318", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
