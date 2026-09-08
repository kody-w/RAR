---
name: "rar-cowork-cookbook-bulk-update-print-shipping-documentation"
description: "Applies a bulk field update to print shipping documentation records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_print_shipping_documentation", "rar_sha256": "5579558dace49e1c60fa3c38a5ddcb391c6a65cf8f8101f243371205b89fb7fd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_print_shipping_documentation`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_print_shipping_documentation_agent.py` and in the RCI capsule.

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

Print shipping documentation Bulk Field Update — Applies a bulk field update to print shipping documentation records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confi

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-print-shipping-documentation
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
      "description": "Target environment; sandbox only for this recipe.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity, default USMF.",
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
      "description": "List of print shipping documentation record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_print_shipping_documentation_agent.py` and embedded as the fenced Python below (sha256 5579558dace49e1c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_print_shipping_documentation_agent.py` first:

```bash
python3 bulk_update_print_shipping_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_print_shipping_documentation_agent.py   # or on stdin
python3 bulk_update_print_shipping_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Print shipping documentation Bulk Field Update — Applies a bulk field update to print shipping documentation records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confi

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-print-shipping-documentation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_print_shipping_documentation',
    "version": '3.0.3',
    "display_name": 'Print shipping documentation Bulk Field Update',
    "description": 'Applies a bulk field update to print shipping documentation records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confi',
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
        "upstream_slug": 'bulk-update-print-shipping-documentation',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-print-shipping-documentation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6076267427244d2f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/print-shipping-documentation'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-print-shipping-documentation', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox only for this recipe.', 'legal_entity': 'Dynamics 365 legal entity, default USMF.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of print shipping documentation record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when print shipping documentation records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to print shipping documentation records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to print shipping documentation records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confi', 'example_request': 'Bulk update these print shipping doc records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of print shipping documentation record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity, default USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox only for this recipe.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) on many print shipping documentation records at once and want a before/after preview and approval gate first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePrintShippingDocumentation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePrintShippingDocumentation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox only for this recipe.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity, default USMF.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of print shipping documentation record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePrintShippingDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
