---
name: "rar-cowork-cookbook-bulk-update-plan-worker-retirement"
description: "Applies a bulk field update to plan worker retirement records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the ERP plugin, producing a dry-run preview workbook for approval before committing changes and emittin"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_worker_retirement", "rar_sha256": "867ec429acb88c53464577b1fa98e120cfe1976c9c353815f24a78bd0c658b99", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
