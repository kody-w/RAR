---
name: "rar-cowork-cookbook-bulk-update-purchase-assets"
description: "Applies a bulk field update to purchase assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_purchase_assets", "rar_sha256": "a32fa436c3c77cffdb5394bc3e42ff2f4d36631d6e3df8e33790756d479ebad7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_purchase_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_purchase_assets_agent.py` and in the RCI capsule.

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

Purchase assets Bulk Field Update — Applies a bulk field update to purchase assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-purchase-assets
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
      "description": "Target environment; sandbox first before any production run.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; USMF by default.",
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
      "description": "List of purchase assets record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_purchase_assets_agent.py` and embedded as the fenced Python below (sha256 a32fa436c3c77cff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_purchase_assets_agent.py` first:

```bash
python3 bulk_update_purchase_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_purchase_assets_agent.py   # or on stdin
python3 bulk_update_purchase_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purchase assets Bulk Field Update — Applies a bulk field update to purchase assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-purchase-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_purchase_assets',
    "version": '3.0.3',
    "display_name": 'Purchase assets Bulk Field Update',
    "description": 'Applies a bulk field update to purchase assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before',
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
        "upstream_slug": 'bulk-update-purchase-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-purchase-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c09daddaf4df5098',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/purchase-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-purchase-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before any production run.', 'legal_entity': 'D365 legal entity to run against; USMF by default.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of purchase assets record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when purchase assets records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to purchase assets records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to purchase assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before', 'example_request': 'Bulk update these purchase asset records in USMF sandbox with the new values — show me the dry-run first.', 'inputs': [{'description': 'List of purchase assets record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF by default.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before any production run.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many purchase assets records in D365 and want a before/after dry-run preview and approval gate first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePurchaseAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePurchaseAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before any production run.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of purchase assets record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePurchaseAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
