---
name: "rar-cowork-cookbook-bulk-update-invoice-project-milestones"
description: "Applies a bulk field update to invoice project milestones records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_invoice_project_milestones", "rar_sha256": "8f5a2dd5c5c2870c66960895bca628de0115aa2c133cf6a36bbf55b1b007afb9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
