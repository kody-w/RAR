---
name: "rar-cowork-cookbook-bulk-update-classify-assets"
description: "Applies a bulk field update to classify assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook of before/after/status, pauses for approval, th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_classify_assets", "rar_sha256": "af3c8c4274b62e95e720b7e3fef8ec5d94fcece1ab044bc943314938a5d4bc55", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
