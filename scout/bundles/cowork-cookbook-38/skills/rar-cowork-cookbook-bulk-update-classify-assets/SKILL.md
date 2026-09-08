---
name: "rar-cowork-cookbook-bulk-update-classify-assets"
description: "Applies a bulk field update to classify assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook of before/after/status, pauses for approval, th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_classify_assets", "rar_sha256": "af3c8c4274b62e95e720b7e3fef8ec5d94fcece1ab044bc943314938a5d4bc55", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_classify_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_classify_assets_agent.py` and in the RCI capsule.

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

Classify assets Bulk Field Update — Applies a bulk field update to classify assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook of before/after/status, pauses for approval, th

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-classify-assets
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
    "environment": {
      "description": "Target environment; sandbox only for write actions.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF).",
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
      "description": "List of classify assets record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_classify_assets_agent.py` and embedded as the fenced Python below (sha256 af3c8c4274b62e95…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_classify_assets_agent.py` first:

```bash
python3 bulk_update_classify_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_classify_assets_agent.py   # or on stdin
python3 bulk_update_classify_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Classify assets Bulk Field Update — Applies a bulk field update to classify assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook of before/after/status, pauses for approval, th

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-classify-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_classify_assets',
    "version": '3.0.3',
    "display_name": 'Classify assets Bulk Field Update',
    "description": 'Applies a bulk field update to classify assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook of before/after/status, pauses for approval, th',
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
        "upstream_slug": 'bulk-update-classify-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-classify-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a4b0d9b438961099',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/classify-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-classify-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox only for write actions.', 'legal_entity': 'D365 legal entity to run against (default USMF).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of classify assets record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when classify assets records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to classify assets records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to classify assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook of before/after/status, pauses for approval, th', 'example_request': 'Bulk update these classify assets record IDs in USMF sandbox to the new value - show me a dry-run first.', 'inputs': [{'description': 'List of classify assets record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (default USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox only for write actions.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many classify assets records at once in a D365 sandbox and want a reviewable dry-run before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateClassifyAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateClassifyAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox only for write actions.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of classify assets record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateClassifyAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
