---
name: "rar-cowork-cookbook-bulk-update-cross-dock-produced-goods"
description: "Applies a bulk field update to cross dock produced goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook, then a c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_cross_dock_produced_goods", "rar_sha256": "de73bf1bee5e4353ae7a00269a790a9c86c57cdcd0902746947e1d8aca415b55", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_cross_dock_produced_goods`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_cross_dock_produced_goods_agent.py` and in the RCI capsule.

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

Cross dock produced goods Bulk Field Update — Applies a bulk field update to cross dock produced goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook, then a c

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-cross-dock-produced-goods
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
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook, before any write.",
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
      "description": "List of cross dock produced goods record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_cross_dock_produced_goods_agent.py` and embedded as the fenced Python below (sha256 de73bf1bee5e4353…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_cross_dock_produced_goods_agent.py` first:

```bash
python3 bulk_update_cross_dock_produced_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_cross_dock_produced_goods_agent.py   # or on stdin
python3 bulk_update_cross_dock_produced_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross dock produced goods Bulk Field Update — Applies a bulk field update to cross dock produced goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook, then a c

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-cross-dock-produced-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_cross_dock_produced_goods',
    "version": '3.0.3',
    "display_name": 'Cross dock produced goods Bulk Field Update',
    "description": 'Applies a bulk field update to cross dock produced goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook, then a c',
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
        "upstream_slug": 'bulk-update-cross-dock-produced-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-cross-dock-produced-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e2323ec11e328c4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/cross-dock-produced-goods'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-cross-dock-produced-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook, before any write.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of cross dock produced goods record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when cross dock produced goods records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to cross dock produced goods records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to cross dock produced goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook, then a c', 'example_request': 'Bulk update these cross dock produced goods records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of cross dock produced goods record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook, before any write.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many cross dock produced goods records at once in a D365 sandbox and want a before/after preview to approve first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateCrossDockProducedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCrossDockProducedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook, before any write.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of cross dock produced goods record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateCrossDockProducedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
