---
name: "rar-cowork-cookbook-bulk-update-track-fronline-worker-location"
description: "Applies a bulk field update to frontline worker location records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing chan"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_fronline_worker_location", "rar_sha256": "4524bda5a283ccffc4e3401bb4a7ac1d5bb0084979c1aaedea4742ed5e98296d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_track_fronline_worker_location`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_track_fronline_worker_location_agent.py` and in the RCI capsule.

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

Track fronline worker location Bulk Field Update — Applies a bulk field update to frontline worker location records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing chan

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-track-fronline-worker-location
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
    "environment": {
      "description": "Target environment; sandbox only for this recipe.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF.",
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
      "description": "List of frontline worker location record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_track_fronline_worker_location_agent.py` and embedded as the fenced Python below (sha256 4524bda5a283ccff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_track_fronline_worker_location_agent.py` first:

```bash
python3 bulk_update_track_fronline_worker_location_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_track_fronline_worker_location_agent.py   # or on stdin
python3 bulk_update_track_fronline_worker_location_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track fronline worker location Bulk Field Update — Applies a bulk field update to frontline worker location records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing chan

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-track-fronline-worker-location
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_track_fronline_worker_location',
    "version": '3.0.3',
    "display_name": 'Track fronline worker location Bulk Field Update',
    "description": 'Applies a bulk field update to frontline worker location records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing chan',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-track-fronline-worker-location',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-track-fronline-worker-location',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07e86986c712c663',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/track-fronline-worker-location'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-track-fronline-worker-location', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox only for this recipe.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of frontline worker location record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when track fronline worker location records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to track fronline worker location records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to frontline worker location records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing chan', 'example_request': 'Bulk update these frontline worker location record IDs in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of frontline worker location record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox only for this recipe.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of frontline worker location record IDs in D365, with a reviewed dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateTrackFronlineWorkerLocation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateTrackFronlineWorkerLocation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox only for this recipe.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of frontline worker location record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateTrackFronlineWorkerLocation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
