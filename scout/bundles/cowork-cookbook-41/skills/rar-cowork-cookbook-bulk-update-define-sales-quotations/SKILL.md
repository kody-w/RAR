---
name: "rar-cowork-cookbook-bulk-update-define-sales-quotations"
description: "Applies a bulk field update to Dynamics 365 sales quotation records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_sales_quotations", "rar_sha256": "ed5aeba30c43c7ebdaf7a19cef9998b400337a1dabb48df0e16b6fb1509891a8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
