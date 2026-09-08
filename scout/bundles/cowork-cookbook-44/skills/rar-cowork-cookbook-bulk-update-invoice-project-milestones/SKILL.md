---
name: "rar-cowork-cookbook-bulk-update-invoice-project-milestones"
description: "Applies a bulk field update to invoice project milestones records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_invoice_project_milestones", "rar_sha256": "8f5a2dd5c5c2870c66960895bca628de0115aa2c133cf6a36bbf55b1b007afb9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_invoice_project_milestones`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_invoice_project_milestones_agent.py` and in the RCI capsule.

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

Invoice project milestones Bulk Field Update — Applies a bulk field update to invoice project milestones records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-invoice-project-milestones
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
      "description": "Dynamics 365 legal entity to run against; sandbox USMF by default.",
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
      "description": "List of invoice project milestone record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_invoice_project_milestones_agent.py` and embedded as the fenced Python below (sha256 8f5a2dd5c5c2870c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_invoice_project_milestones_agent.py` first:

```bash
python3 bulk_update_invoice_project_milestones_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_invoice_project_milestones_agent.py   # or on stdin
python3 bulk_update_invoice_project_milestones_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Invoice project milestones Bulk Field Update — Applies a bulk field update to invoice project milestones records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-invoice-project-milestones
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_invoice_project_milestones',
    "version": '3.0.3',
    "display_name": 'Invoice project milestones Bulk Field Update',
    "description": 'Applies a bulk field update to invoice project milestones records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the ERP plugin, producing a dry-run preview workbook for approval before committing changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-invoice-project-milestones',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-invoice-project-milestones',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0bdff0aa3b0678a0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/invoice-project-milestones'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-invoice-project-milestones', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; sandbox USMF by default.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of invoice project milestone record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when invoice project milestones records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to invoice project milestones records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to invoice project milestones records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the ERP plugin, producing a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk update these invoice project milestone IDs in USMF sandbox to the new date - show me a dry-run first.', 'inputs': [{'description': 'List of invoice project milestone record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; sandbox USMF by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of invoice project milestone record IDs and new values to update in bulk, and want a before/after preview before writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateInvoiceProjectMilestones(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateInvoiceProjectMilestones'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; sandbox USMF by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of invoice project milestone record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateInvoiceProjectMilestones().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
