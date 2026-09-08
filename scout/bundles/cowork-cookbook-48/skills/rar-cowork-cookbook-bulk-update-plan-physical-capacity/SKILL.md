---
name: "rar-cowork-cookbook-bulk-update-plan-physical-capacity"
description: "Applies a bulk field update to Dynamics 365 plan physical capacity records for a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_physical_capacity", "rar_sha256": "670f53d4b84c32148cb7742e9213df6d8debd3245b036862e9d83ff01acd1f1e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
