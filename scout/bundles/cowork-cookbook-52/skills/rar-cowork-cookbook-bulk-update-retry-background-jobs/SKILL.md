---
name: "rar-cowork-cookbook-bulk-update-retry-background-jobs"
description: "Applies a bulk field update to Dynamics 365 retry background jobs records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retry_background_jobs", "rar_sha256": "56cdc1dc7c772c9390e04d18abbb4f118d600bf6e559ba0e1c0e19c255d06c27", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
