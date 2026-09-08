---
name: "rar-cowork-cookbook-bulk-update-manage-formulas"
description: "Applies a bulk field update to manage formulas records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, then applie"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_formulas", "rar_sha256": "995397dac0f0a00ed82246438a123ec36186ace0ee1327c6beb3e8795897e22e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_formulas`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_formulas_agent.py` and in the RCI capsule.

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

Manage formulas Bulk Field Update — Applies a bulk field update to manage formulas records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, then applie

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-formulas
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
      "description": "Explicit approval after reviewing the dry-run preview before changes are applied.",
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
      "description": "List of manage formulas record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_formulas_agent.py` and embedded as the fenced Python below (sha256 995397dac0f0a00e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_formulas_agent.py` first:

```bash
python3 bulk_update_manage_formulas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_formulas_agent.py   # or on stdin
python3 bulk_update_manage_formulas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage formulas Bulk Field Update — Applies a bulk field update to manage formulas records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, then applie

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-formulas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_formulas',
    "version": '3.0.3',
    "display_name": 'Manage formulas Bulk Field Update',
    "description": 'Applies a bulk field update to manage formulas records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, then applie',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-formulas',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-formulas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '30e47cc3cb378d92',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-formulas'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/bulk-update-manage-formulas', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox only for write actions.', 'legal_entity': 'D365 legal entity to run against (default USMF).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of manage formulas record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when manage formulas records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to manage formulas records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to manage formulas records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, then applie', 'example_request': 'Bulk update these manage formulas record IDs in USMF sandbox with the new values — show me the dry-run first.', 'inputs': [{'description': 'List of manage formulas record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (default USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox only for write actions.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the dry-run preview before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to change the same field(s) across many manage formulas records in a D365 sandbox and want a reviewable dry-run before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateManageFormulas(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageFormulas'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox only for write actions.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of manage formulas record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateManageFormulas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
