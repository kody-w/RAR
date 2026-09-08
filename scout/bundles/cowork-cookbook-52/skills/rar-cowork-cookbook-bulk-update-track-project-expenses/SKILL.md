---
name: "rar-cowork-cookbook-bulk-update-track-project-expenses"
description: "Applies a bulk field update to track project expenses records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_project_expenses", "rar_sha256": "e0874737bc9d138bc7df99c9d39ea1a3a2a95c7c358e3da85076359d4c25d778", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_track_project_expenses`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_track_project_expenses_agent.py` and in the RCI capsule.

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

Track project expenses Bulk Field Update — Applies a bulk field update to track project expenses records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-track-project-expenses
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are applied.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to those records.",
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
      "description": "List of track project expenses record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_track_project_expenses_agent.py` and embedded as the fenced Python below (sha256 e0874737bc9d138b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_track_project_expenses_agent.py` first:

```bash
python3 bulk_update_track_project_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_track_project_expenses_agent.py   # or on stdin
python3 bulk_update_track_project_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project expenses Bulk Field Update — Applies a bulk field update to track project expenses records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-track-project-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_track_project_expenses',
    "version": '3.0.3',
    "display_name": 'Track project expenses Bulk Field Update',
    "description": 'Applies a bulk field update to track project expenses records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval.',
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
        "upstream_slug": 'bulk-update-track-project-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-track-project-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '41a0f5124e958079',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-expenses'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-track-project-expenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of track project expenses record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when track project expenses records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to track project expenses records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to track project expenses records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval.', 'example_request': 'Bulk update these project expense record IDs with a new value in USMF — show me the dry-run preview first.', 'inputs': [{'description': 'List of track project expenses record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of track project expenses record IDs and new field values to update in bulk, and want a dry-run preview before committing. Sandbox only.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateTrackProjectExpenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateTrackProjectExpenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of track project expenses record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateTrackProjectExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
