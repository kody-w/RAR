---
name: "rar-cowork-cookbook-bulk-update-plan-worker-retirement"
description: "Applies a bulk field update to plan worker retirement records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the ERP plugin, producing a dry-run preview workbook for approval before committing changes and emittin"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_worker_retirement", "rar_sha256": "867ec429acb88c53464577b1fa98e120cfe1976c9c353815f24a78bd0c658b99", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_worker_retirement`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_worker_retirement_agent.py` and in the RCI capsule.

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

Plan worker retirement Bulk Field Update — Applies a bulk field update to plan worker retirement records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the ERP plugin, producing a dry-run preview workbook for approval before committing changes and emittin

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-worker-retirement
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; USMF sandbox by default.",
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
      "description": "List of plan worker retirement record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_worker_retirement_agent.py` and embedded as the fenced Python below (sha256 867ec429acb88c53…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_worker_retirement_agent.py` first:

```bash
python3 bulk_update_plan_worker_retirement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_worker_retirement_agent.py   # or on stdin
python3 bulk_update_plan_worker_retirement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan worker retirement Bulk Field Update — Applies a bulk field update to plan worker retirement records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the ERP plugin, producing a dry-run preview workbook for approval before committing changes and emittin

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-worker-retirement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_worker_retirement',
    "version": '3.0.3',
    "display_name": 'Plan worker retirement Bulk Field Update',
    "description": 'Applies a bulk field update to plan worker retirement records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the ERP plugin, producing a dry-run preview workbook for approval before committing changes and emittin',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-worker-retirement',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-worker-retirement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f0b7017b27f2461',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/plan-worker-retirement'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-plan-worker-retirement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of plan worker retirement record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when plan worker retirement records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to plan worker retirement records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to plan worker retirement records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the ERP plugin, producing a dry-run preview workbook for approval before committing changes and emittin', 'example_request': 'Bulk update these plan worker retirement records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of plan worker retirement record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of plan worker retirement record IDs and want a reviewable dry-run before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePlanWorkerRetirement(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanWorkerRetirement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of plan worker retirement record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePlanWorkerRetirement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
