---
name: "rar-cowork-cookbook-bulk-update-clean-up-and-archive-background-jobs"
description: "Applies a bulk field update to background job cleanup/archive records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, with a dry-run preview workbook and approval pause before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_clean_up_and_archive_background_jobs", "rar_sha256": "33de1a9e879afdcc292096799153116eff146d9a75bb590dc474fc85b8f2d1f3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_clean_up_and_archive_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_clean_up_and_archive_background_jobs_agent.py` and in the RCI capsule.

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

Clean up and archive background jobs Bulk Field Update — Applies a bulk field update to background job cleanup/archive records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, with a dry-run preview workbook and approval pause before commit.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-clean-up-and-archive-background-jobs
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are applied.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; recipe uses USMF sandbox.",
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
      "description": "List of clean up / archive background job record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_clean_up_and_archive_background_jobs_agent.py` and embedded as the fenced Python below (sha256 33de1a9e879afdcc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_clean_up_and_archive_background_jobs_agent.py` first:

```bash
python3 bulk_update_clean_up_and_archive_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_clean_up_and_archive_background_jobs_agent.py   # or on stdin
python3 bulk_update_clean_up_and_archive_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clean up and archive background jobs Bulk Field Update — Applies a bulk field update to background job cleanup/archive records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, with a dry-run preview workbook and approval pause before commit.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-clean-up-and-archive-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_clean_up_and_archive_background_jobs',
    "version": '3.0.3',
    "display_name": 'Clean up and archive background jobs Bulk Field Update',
    "description": 'Applies a bulk field update to background job cleanup/archive records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, with a dry-run preview workbook and approval pause before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-clean-up-and-archive-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-clean-up-and-archive-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2ef700a883764ecb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/clean-up-and-archive-background-jobs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-clean-up-and-archive-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; recipe uses USMF sandbox.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of clean up / archive background job record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when clean up and archive background jobs records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to clean up and archive background jobs records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to background job cleanup/archive records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, with a dry-run preview workbook and approval pause before commit.', 'example_request': 'Bulk-update these background job records in USMF sandbox to the new value — show me the dry-run preview first.', 'inputs': [{'description': 'List of clean up / archive background job record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; recipe uses USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of background job record IDs and new field values to update in bulk in D365 F&SCM sandbox, and want a dry-run preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateCleanUpAndArchiveBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCleanUpAndArchiveBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; recipe uses USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of clean up / archive background job record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateCleanUpAndArchiveBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
