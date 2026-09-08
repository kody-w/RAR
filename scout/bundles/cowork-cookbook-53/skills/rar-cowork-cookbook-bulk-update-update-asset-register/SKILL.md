---
name: "rar-cowork-cookbook-bulk-update-update-asset-register"
description: "Applies a bulk field update to asset register records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_update_asset_register", "rar_sha256": "a5c5e3333f234efcb91b8897d28523d2aa61f48219dbe4d2e7660c5d5d539241", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
