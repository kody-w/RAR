---
name: "rar-cowork-cookbook-bulk-update-purchase-assets"
description: "Applies a bulk field update to purchase assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_purchase_assets", "rar_sha256": "a32fa436c3c77cffdb5394bc3e42ff2f4d36631d6e3df8e33790756d479ebad7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
