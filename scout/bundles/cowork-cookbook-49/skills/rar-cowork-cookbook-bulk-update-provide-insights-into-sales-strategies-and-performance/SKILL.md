---
name: "rar-cowork-cookbook-bulk-update-provide-insights-into-sales-strategies-and-performance"
description: "Applies a bulk field update to Dynamics 365 F&SCM sales-performance records from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_provide_insights_into_sales_strategies_and_performance", "rar_sha256": "cff80692b50500a8bded60b959fe9333f7663a9cc075a554cf9c432613039fc4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_provide_insights_into_sales_strategies_and_performance`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py` and in the RCI capsule.

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

Provide insights into sales strategies and performance Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM sales-performance records from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-provide-insights-into-sales-strategies-and-performance
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
      "description": "User confirmation after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF, sandbox).",
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
      "description": "List of record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py` and embedded as the fenced Python below (sha256 cff80692b50500a8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py` first:

```bash
python3 bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py   # or on stdin
python3 bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Provide insights into sales strategies and performance Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM sales-performance records from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-provide-insights-into-sales-strategies-and-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_provide_insights_into_sales_strategies_and_performance',
    "version": '3.0.3',
    "display_name": 'Provide insights into sales strategies and performance Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM sales-performance records from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.',
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
        "upstream_slug": 'bulk-update-provide-insights-into-sales-strategies-and-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-provide-insights-into-sales-strategies-and-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '22c7ba06d0d6807c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/provide-insights-into-sales-strategies-and-performance'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-provide-insights-into-sales-strategies-and-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'User confirmation after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF, sandbox).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when provide insights into sales strategies and performance records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to provide insights into sales strategies and performance records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM sales-performance records from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.', 'example_request': 'Bulk update these sales records in USMF sandbox to the new value — show me a dry-run preview first.', 'inputs': [{'description': 'List of record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (e.g. USMF, sandbox).', 'name': 'legal_entity'}, {'description': 'User confirmation after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-update sales-related D365 ERP records in a sandbox legal entity with a reviewable before/after preview and explicit approval step.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateProvideInsightsIntoSalesStrategiesAndPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateProvideInsightsIntoSalesStrategiesAndPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'User confirmation after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF, sandbox).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateProvideInsightsIntoSalesStrategiesAndPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
