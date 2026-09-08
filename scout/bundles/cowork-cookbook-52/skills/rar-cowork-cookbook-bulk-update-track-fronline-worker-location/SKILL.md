---
name: "rar-cowork-cookbook-bulk-update-track-fronline-worker-location"
description: "Applies a bulk field update to frontline worker location records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing chan"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_fronline_worker_location", "rar_sha256": "4524bda5a283ccffc4e3401bb4a7ac1d5bb0084979c1aaedea4742ed5e98296d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
