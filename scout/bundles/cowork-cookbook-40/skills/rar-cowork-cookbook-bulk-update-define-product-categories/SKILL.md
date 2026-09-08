---
name: "rar-cowork-cookbook-bulk-update-define-product-categories"
description: "Applies a bulk field update to product category records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_product_categories", "rar_sha256": "e9b88c1f6f9160d0b5b1142f1d3557b46b4b223192a0997bdcfb27c3ac18186f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_product_categories`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_product_categories_agent.py` and in the RCI capsule.

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

Define product categories Bulk Field Update — Applies a bulk field update to product category records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, th

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-product-categories
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
      "description": "List of product category record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_product_categories_agent.py` and embedded as the fenced Python below (sha256 e9b88c1f6f9160d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_product_categories_agent.py` first:

```bash
python3 bulk_update_define_product_categories_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_product_categories_agent.py   # or on stdin
python3 bulk_update_define_product_categories_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product categories Bulk Field Update — Applies a bulk field update to product category records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, th

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-product-categories
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_product_categories',
    "version": '3.0.3',
    "display_name": 'Define product categories Bulk Field Update',
    "description": 'Applies a bulk field update to product category records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, th',
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
        "upstream_slug": 'bulk-update-define-product-categories',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-product-categories',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e094df810d44fca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-categories'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/bulk-update-define-product-categories', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of product category record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define product categories records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define product categories records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to product category records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, th', 'example_request': 'Bulk update these product category records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of product category record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to change a field on many product category records at once in D365 and needs a reviewable dry-run before the write is committed.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineProductCategories(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineProductCategories'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of product category record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineProductCategories().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
