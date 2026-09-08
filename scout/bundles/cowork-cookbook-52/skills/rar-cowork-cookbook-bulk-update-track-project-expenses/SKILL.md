---
name: "rar-cowork-cookbook-bulk-update-track-project-expenses"
description: "Applies a bulk field update to track project expenses records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_project_expenses", "rar_sha256": "e0874737bc9d138bc7df99c9d39ea1a3a2a95c7c358e3da85076359d4c25d778", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
