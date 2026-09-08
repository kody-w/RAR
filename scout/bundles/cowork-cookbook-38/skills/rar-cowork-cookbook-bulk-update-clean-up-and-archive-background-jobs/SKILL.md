---
name: "rar-cowork-cookbook-bulk-update-clean-up-and-archive-background-jobs"
description: "Applies a bulk field update to background job cleanup/archive records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, with a dry-run preview workbook and approval pause before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_clean_up_and_archive_background_jobs", "rar_sha256": "33de1a9e879afdcc292096799153116eff146d9a75bb590dc474fc85b8f2d1f3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
