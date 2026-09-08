---
name: "rar-cowork-cookbook-bulk-update-transfer-budgets"
description: "Applies a bulk field update to Dynamics 365 transfer budgets records in a given legal entity via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval and a confirmation workbook after commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_transfer_budgets", "rar_sha256": "4b0c0c5f6eeeeb82353737b154f9a00cb0e1e72787354fab59c1c06b494b063a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_transfer_budgets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_transfer_budgets_agent.py` and in the RCI capsule.

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

Transfer budgets Bulk Field Update — Applies a bulk field update to Dynamics 365 transfer budgets records in a given legal entity via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval and a confirmation workbook after commit.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-transfer-budgets
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
      "description": "Explicit user approval after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; sandbox environment only.",
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
      "description": "List of transfer budgets record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_transfer_budgets_agent.py` and embedded as the fenced Python below (sha256 4b0c0c5f6eeeeb82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_transfer_budgets_agent.py` first:

```bash
python3 bulk_update_transfer_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_transfer_budgets_agent.py   # or on stdin
python3 bulk_update_transfer_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer budgets Bulk Field Update — Applies a bulk field update to Dynamics 365 transfer budgets records in a given legal entity via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval and a confirmation workbook after commit.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-transfer-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_transfer_budgets',
    "version": '3.0.3',
    "display_name": 'Transfer budgets Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 transfer budgets records in a given legal entity via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval and a confirmation workbook after commit.',
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
        "upstream_slug": 'bulk-update-transfer-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-transfer-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd9ae5364ce694141',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/transfer-budgets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-transfer-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of transfer budgets record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when transfer budgets records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to transfer budgets records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 transfer budgets records in a given legal entity via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval and a confirmation workbook after commit.', 'example_request': 'Bulk update these transfer budget records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'name': 'legal_entity'}, {'description': 'List of transfer budgets record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Explicit user approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs to change the same field(s) across a list of transfer budgets records in D365 F&SCM, with a reviewed dry-run before writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateTransferBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateTransferBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of transfer budgets record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateTransferBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
