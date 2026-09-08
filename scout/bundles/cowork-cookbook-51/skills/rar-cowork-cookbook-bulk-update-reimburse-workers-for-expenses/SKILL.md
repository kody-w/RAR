---
name: "rar-cowork-cookbook-bulk-update-reimburse-workers-for-expenses"
description: "Applies a bulk field update to reimburse-workers-for-expenses records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and appro"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reimburse_workers_for_expenses", "rar_sha256": "e2225488059e812b57696cd3afb167102117fa59fcc880ff2cec31821f5af6ce", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_reimburse_workers_for_expenses`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_reimburse_workers_for_expenses_agent.py` and in the RCI capsule.

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

Reimburse workers for expenses Bulk Field Update — Applies a bulk field update to reimburse-workers-for-expenses records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and appro

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reimburse-workers-for-expenses
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
      "description": "D365 legal entity to run against; USMF sandbox by default.",
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
      "description": "List of reimburse-workers-for-expenses record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reimburse_workers_for_expenses_agent.py` and embedded as the fenced Python below (sha256 e2225488059e812b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reimburse_workers_for_expenses_agent.py` first:

```bash
python3 bulk_update_reimburse_workers_for_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_reimburse_workers_for_expenses_agent.py   # or on stdin
python3 bulk_update_reimburse_workers_for_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reimburse workers for expenses Bulk Field Update — Applies a bulk field update to reimburse-workers-for-expenses records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and appro

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reimburse-workers-for-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_reimburse_workers_for_expenses',
    "version": '3.0.3',
    "display_name": 'Reimburse workers for expenses Bulk Field Update',
    "description": 'Applies a bulk field update to reimburse-workers-for-expenses records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and appro',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-reimburse-workers-for-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-reimburse-workers-for-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e7944599e6acc8c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/reimburse-workers-for-expenses'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-reimburse-workers-for-expenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of reimburse-workers-for-expenses record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when reimburse workers for expenses records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to reimburse workers for expenses records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to reimburse-workers-for-expenses records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and appro', 'example_request': 'Bulk update these expense reimbursement records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of reimburse-workers-for-expenses record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many reimburse-workers-for-expenses records at once in a D365 sandbox and want a before/after preview to approve first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateReimburseWorkersForExpenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReimburseWorkersForExpenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of reimburse-workers-for-expenses record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateReimburseWorkersForExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
