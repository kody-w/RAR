---
name: "rar-cowork-cookbook-bulk-update-forecast-sales"
description: "Applies a bulk field update to Dynamics 365 forecast sales records in legal entity USMF via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, then commits and ret"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_forecast_sales", "rar_sha256": "e481ef7f0b08e155cd51794abe2cef05e0ae9473e7358dbc88d0270a9e6707af", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
