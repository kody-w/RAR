---
name: "rar-cowork-cookbook-bulk-update-forecast-service-demand"
description: "Applies a bulk field update to Dynamics 365 forecast service demand records in legal entity USMF via the D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_forecast_service_demand", "rar_sha256": "7e016559ab34d2ec4b2808e80023166db3a2401ffebc71d72eaa04e316adbbf1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_forecast_service_demand`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_forecast_service_demand_agent.py` and in the RCI capsule.

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

Forecast service demand Bulk Field Update — Applies a bulk field update to Dynamics 365 forecast service demand records in legal entity USMF via the D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-forecast-service-demand
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
    "environment": {
      "description": "Target environment \u2014 sandbox first before any production run.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Legal entity to run against; defaults to USMF.",
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
      "description": "List of forecast service demand record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_forecast_service_demand_agent.py` and embedded as the fenced Python below (sha256 7e016559ab34d2ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_forecast_service_demand_agent.py` first:

```bash
python3 bulk_update_forecast_service_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_forecast_service_demand_agent.py   # or on stdin
python3 bulk_update_forecast_service_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast service demand Bulk Field Update — Applies a bulk field update to Dynamics 365 forecast service demand records in legal entity USMF via the D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-forecast-service-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_forecast_service_demand',
    "version": '3.0.3',
    "display_name": 'Forecast service demand Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 forecast service demand records in legal entity USMF via the D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-forecast-service-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-forecast-service-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '86129f369a93808a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/forecast-service-demand'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-forecast-service-demand', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first before any production run.', 'legal_entity': 'Legal entity to run against; defaults to USMF.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of forecast service demand record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when forecast service demand records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to forecast service demand records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 forecast service demand records in legal entity USMF via the D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk update these forecast service demand records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of forecast service demand record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first before any production run.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field across many forecast service demand records at once and want a before/after preview and approval gate first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateForecastServiceDemand(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateForecastServiceDemand'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first before any production run.', 'type': 'string'}, 'legal_entity': {'description': 'Legal entity to run against; defaults to USMF.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of forecast service demand record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateForecastServiceDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
