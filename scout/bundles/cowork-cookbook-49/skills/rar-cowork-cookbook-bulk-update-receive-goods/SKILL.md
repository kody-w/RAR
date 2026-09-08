---
name: "rar-cowork-cookbook-bulk-update-receive-goods"
description: "Applies a bulk field update to Dynamics 365 F&SCM receive goods records in legal entity USMF via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_receive_goods", "rar_sha256": "edd847dea41fb65943c57ddb5949829443864071a82b0942d1d3acfe00090abc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_receive_goods`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_receive_goods_agent.py` and in the RCI capsule.

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

Receive goods Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM receive goods records in legal entity USMF via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-receive-goods
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
      "description": "D365 legal entity to run against; USMF sandbox by default.",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to those records.",
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
      "description": "List of receive goods record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_receive_goods_agent.py` and embedded as the fenced Python below (sha256 edd847dea41fb659…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_receive_goods_agent.py` first:

```bash
python3 bulk_update_receive_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_receive_goods_agent.py   # or on stdin
python3 bulk_update_receive_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive goods Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM receive goods records in legal entity USMF via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-receive-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_receive_goods',
    "version": '3.0.3',
    "display_name": 'Receive goods Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM receive goods records in legal entity USMF via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-receive-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-receive-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '954411628e83abce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/receive-goods'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-receive-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of receive goods record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when receive goods records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to receive goods records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM receive goods records in legal entity USMF via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk update these receive goods record IDs in USMF sandbox with the new value - show me a dry-run preview first.', 'inputs': [{'description': 'List of receive goods record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of receive goods record IDs and new field values to update in bulk in a D365 sandbox, and want a reviewable preview first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateReceiveGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReceiveGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of receive goods record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateReceiveGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
