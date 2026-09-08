---
name: "rar-cowork-cookbook-bulk-update-update-asset-register"
description: "Applies a bulk field update to asset register records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_update_asset_register", "rar_sha256": "a5c5e3333f234efcb91b8897d28523d2aa61f48219dbe4d2e7660c5d5d539241", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_update_asset_register`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_update_asset_register_agent.py` and in the RCI capsule.

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

Update asset register Bulk Field Update — Applies a bulk field update to asset register records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-update-asset-register
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of asset register record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_update_asset_register_agent.py` and embedded as the fenced Python below (sha256 a5c5e3333f234efc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_update_asset_register_agent.py` first:

```bash
python3 bulk_update_update_asset_register_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_update_asset_register_agent.py   # or on stdin
python3 bulk_update_update_asset_register_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update asset register Bulk Field Update — Applies a bulk field update to asset register records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-update-asset-register
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_update_asset_register',
    "version": '3.0.3',
    "display_name": 'Update asset register Bulk Field Update',
    "description": 'Applies a bulk field update to asset register records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before',
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
        "upstream_slug": 'bulk-update-update-asset-register',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-update-asset-register',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e398b54af5a58cb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/update-asset-register'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-update-asset-register', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of asset register record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when update asset register records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to update asset register records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to asset register records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before', 'example_request': 'Bulk update these asset register record IDs in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of asset register record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many asset register records in D365 and want a reviewable before/after preview before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateUpdateAssetRegister(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateUpdateAssetRegister'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of asset register record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateUpdateAssetRegister().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
