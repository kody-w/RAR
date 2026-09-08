---
name: "rar-cowork-cookbook-bulk-update-manage-formulas"
description: "Applies a bulk field update to manage formulas records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, then applie"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_formulas", "rar_sha256": "995397dac0f0a00ed82246438a123ec36186ace0ee1327c6beb3e8795897e22e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
