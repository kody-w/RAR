---
name: "rar-cowork-cookbook-bulk-update-forecast-sales"
description: "Applies a bulk field update to Dynamics 365 forecast sales records in legal entity USMF via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, then commits and ret"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_forecast_sales", "rar_sha256": "e481ef7f0b08e155cd51794abe2cef05e0ae9473e7358dbc88d0270a9e6707af", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_forecast_sales`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_forecast_sales_agent.py` and in the RCI capsule.

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

Forecast sales Bulk Field Update — Applies a bulk field update to Dynamics 365 forecast sales records in legal entity USMF via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, then commits and ret

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-forecast-sales
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
      "description": "Explicit user approval after reviewing the dry-run preview, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of forecast sales record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_forecast_sales_agent.py` and embedded as the fenced Python below (sha256 e481ef7f0b08e155…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_forecast_sales_agent.py` first:

```bash
python3 bulk_update_forecast_sales_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_forecast_sales_agent.py   # or on stdin
python3 bulk_update_forecast_sales_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast sales Bulk Field Update — Applies a bulk field update to Dynamics 365 forecast sales records in legal entity USMF via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, then commits and ret

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-forecast-sales
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_forecast_sales',
    "version": '3.0.3',
    "display_name": 'Forecast sales Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 forecast sales records in legal entity USMF via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, then commits and ret',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-forecast-sales',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-forecast-sales',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '85129dd07be5a96a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/forecast-sales'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-forecast-sales', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of forecast sales record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when forecast sales records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to forecast sales records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 forecast sales records in legal entity USMF via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, then commits and ret', 'example_request': 'Bulk update these forecast sales records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of forecast sales record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants to change a field across many forecast sales records at once and needs a reviewable dry-run preview before the write is committed. Sandbox only.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateForecastSales(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateForecastSales'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of forecast sales record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateForecastSales().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
