---
name: "rar-cowork-cookbook-bulk-update-retry-background-jobs"
description: "Applies a bulk field update to Dynamics 365 retry background jobs records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retry_background_jobs", "rar_sha256": "56cdc1dc7c772c9390e04d18abbb4f118d600bf6e559ba0e1c0e19c255d06c27", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_retry_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_retry_background_jobs_agent.py` and in the RCI capsule.

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

Retry background jobs Bulk Field Update — Applies a bulk field update to Dynamics 365 retry background jobs records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retry-background-jobs
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
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of retry background jobs record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_retry_background_jobs_agent.py` and embedded as the fenced Python below (sha256 56cdc1dc7c772c93…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_retry_background_jobs_agent.py` first:

```bash
python3 bulk_update_retry_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_retry_background_jobs_agent.py   # or on stdin
python3 bulk_update_retry_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retry background jobs Bulk Field Update — Applies a bulk field update to Dynamics 365 retry background jobs records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retry-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_retry_background_jobs',
    "version": '3.0.3',
    "display_name": 'Retry background jobs Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 retry background jobs records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.',
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
        "upstream_slug": 'bulk-update-retry-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-retry-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '01612d6654b07643',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/retry-background-jobs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-retry-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of retry background jobs record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when retry background jobs records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to retry background jobs records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 retry background jobs records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk-update these retry background jobs record IDs in USMF sandbox to the new value, and show me the dry-run first.', 'inputs': [{'description': 'List of retry background jobs record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many retry background jobs records at once and want a before/after preview to approve before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateRetryBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRetryBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of retry background jobs record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateRetryBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
