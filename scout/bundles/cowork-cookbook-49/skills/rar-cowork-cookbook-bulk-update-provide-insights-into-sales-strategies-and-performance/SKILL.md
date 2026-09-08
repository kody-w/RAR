---
name: "rar-cowork-cookbook-bulk-update-provide-insights-into-sales-strategies-and-performance"
description: "Applies a bulk field update to Dynamics 365 F&SCM sales-performance records from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_provide_insights_into_sales_strategies_and_performance", "rar_sha256": "cff80692b50500a8bded60b959fe9333f7663a9cc075a554cf9c432613039fc4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
