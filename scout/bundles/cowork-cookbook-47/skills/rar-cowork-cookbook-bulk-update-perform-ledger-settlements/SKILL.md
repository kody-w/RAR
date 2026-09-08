---
name: "rar-cowork-cookbook-bulk-update-perform-ledger-settlements"
description: "Applies a bulk field update to perform ledger settlements records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_ledger_settlements", "rar_sha256": "34f146af54e024ac9c18926be2b0fefb460968286b97ec31d89a89b189bc3685", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
