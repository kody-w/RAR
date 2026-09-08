---
name: "rar-cowork-cookbook-bulk-update-transfer-budgets"
description: "Applies a bulk field update to Dynamics 365 transfer budgets records in a given legal entity via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval and a confirmation workbook after commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_transfer_budgets", "rar_sha256": "4b0c0c5f6eeeeb82353737b154f9a00cb0e1e72787354fab59c1c06b494b063a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
