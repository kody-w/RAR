---
name: "rar-cowork-cookbook-bulk-update-define-sales-quotations"
description: "Applies a bulk field update to Dynamics 365 sales quotation records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_sales_quotations", "rar_sha256": "ed5aeba30c43c7ebdaf7a19cef9998b400337a1dabb48df0e16b6fb1509891a8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_sales_quotations`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_sales_quotations_agent.py` and in the RCI capsule.

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

Define sales quotations Bulk Field Update — Applies a bulk field update to Dynamics 365 sales quotation records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-sales-quotations
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
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook.",
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
      "description": "List of sales quotation record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_sales_quotations_agent.py` and embedded as the fenced Python below (sha256 ed5aeba30c43c7eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_sales_quotations_agent.py` first:

```bash
python3 bulk_update_define_sales_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_sales_quotations_agent.py   # or on stdin
python3 bulk_update_define_sales_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales quotations Bulk Field Update — Applies a bulk field update to Dynamics 365 sales quotation records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-sales-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_sales_quotations',
    "version": '3.0.3',
    "display_name": 'Define sales quotations Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 sales quotation records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-sales-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-sales-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '20bc3b2cee51badb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-sales-quotations'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-define-sales-quotations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of sales quotation record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define sales quotations records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define sales quotations records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 sales quotation records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft', 'example_request': 'Bulk update these sales quotation IDs in USMF sandbox with a new value — show me the dry-run first.', 'inputs': [{'description': 'List of sales quotation record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many sales quotation records in a D365 sandbox and want a reviewable before/after preview first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineSalesQuotations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineSalesQuotations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of sales quotation record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineSalesQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
