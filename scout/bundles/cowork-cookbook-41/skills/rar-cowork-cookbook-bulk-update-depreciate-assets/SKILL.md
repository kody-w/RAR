---
name: "rar-cowork-cookbook-bulk-update-depreciate-assets"
description: "Applies a bulk field update to depreciate assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confirmation wor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_depreciate_assets", "rar_sha256": "612dc09d6ff3f9b9b9d569d78c07396694c666898d885d8cdd250b440094bf51", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_depreciate_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_depreciate_assets_agent.py` and in the RCI capsule.

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

Depreciate assets Bulk Field Update — Applies a bulk field update to depreciate assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confirmation wor

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-depreciate-assets
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are committed.",
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
      "description": "List of depreciate assets record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_depreciate_assets_agent.py` and embedded as the fenced Python below (sha256 612dc09d6ff3f9b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_depreciate_assets_agent.py` first:

```bash
python3 bulk_update_depreciate_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_depreciate_assets_agent.py   # or on stdin
python3 bulk_update_depreciate_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Depreciate assets Bulk Field Update — Applies a bulk field update to depreciate assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confirmation wor

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-depreciate-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_depreciate_assets',
    "version": '3.0.3',
    "display_name": 'Depreciate assets Bulk Field Update',
    "description": 'Applies a bulk field update to depreciate assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confirmation wor',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-depreciate-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-depreciate-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1fe8db6788cc6ece',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/depreciate-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-depreciate-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of depreciate assets record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when depreciate assets records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to depreciate assets records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to depreciate assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confirmation wor', 'example_request': 'Bulk update these depreciate assets record IDs in USMF sandbox with the new values - show me a dry-run first.', 'inputs': [{'description': 'List of depreciate assets record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of depreciate assets record IDs and new values to update in bulk in a D365 sandbox, and want a before/after preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDepreciateAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDepreciateAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of depreciate assets record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDepreciateAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
