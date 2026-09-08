---
name: "rar-cowork-cookbook-bulk-update-reimburse-workers-for-expenses"
description: "Applies a bulk field update to reimburse-workers-for-expenses records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and appro"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reimburse_workers_for_expenses", "rar_sha256": "e2225488059e812b57696cd3afb167102117fa59fcc880ff2cec31821f5af6ce", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
