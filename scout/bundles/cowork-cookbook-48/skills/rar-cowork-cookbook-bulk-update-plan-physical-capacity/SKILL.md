---
name: "rar-cowork-cookbook-bulk-update-plan-physical-capacity"
description: "Applies a bulk field update to Dynamics 365 plan physical capacity records for a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_physical_capacity", "rar_sha256": "670f53d4b84c32148cb7742e9213df6d8debd3245b036862e9d83ff01acd1f1e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_physical_capacity`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_physical_capacity_agent.py` and in the RCI capsule.

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

Plan physical capacity Bulk Field Update — Applies a bulk field update to Dynamics 365 plan physical capacity records for a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-physical-capacity
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
      "description": "D365 legal entity to run against, e.g. USMF (sandbox first).",
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
      "description": "List of plan physical capacity record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_physical_capacity_agent.py` and embedded as the fenced Python below (sha256 670f53d4b84c3214…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_physical_capacity_agent.py` first:

```bash
python3 bulk_update_plan_physical_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_physical_capacity_agent.py   # or on stdin
python3 bulk_update_plan_physical_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan physical capacity Bulk Field Update — Applies a bulk field update to Dynamics 365 plan physical capacity records for a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-physical-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_physical_capacity',
    "version": '3.0.3',
    "display_name": 'Plan physical capacity Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 plan physical capacity records for a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.',
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
        "upstream_slug": 'bulk-update-plan-physical-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-physical-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f6f584a28abcab38',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-physical-capacity'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-plan-physical-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of plan physical capacity record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when plan physical capacity records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to plan physical capacity records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 plan physical capacity records for a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.', 'example_request': 'Bulk update these plan physical capacity records in USMF sandbox with new values - show me a dry-run first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'name': 'legal_entity'}, {'description': 'List of plan physical capacity record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many plan physical capacity records at once in D365 F&SCM (sandbox), with a reviewed preview before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePlanPhysicalCapacity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanPhysicalCapacity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of plan physical capacity record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePlanPhysicalCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
