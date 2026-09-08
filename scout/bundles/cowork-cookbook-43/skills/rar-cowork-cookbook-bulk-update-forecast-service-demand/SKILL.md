---
name: "rar-cowork-cookbook-bulk-update-forecast-service-demand"
description: "Applies a bulk field update to Dynamics 365 forecast service demand records in legal entity USMF via the D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_forecast_service_demand", "rar_sha256": "7e016559ab34d2ec4b2808e80023166db3a2401ffebc71d72eaa04e316adbbf1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
