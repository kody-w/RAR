---
name: "rar-cowork-cookbook-bulk-update-plan-projects"
description: "Applies a bulk field update to plan projects records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_projects", "rar_sha256": "0f165597a35a00361fcd660df95632679fc4bf8e9fc02cf01c1a9a5df39c8fb5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_projects`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_projects_agent.py` and in the RCI capsule.

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

Plan projects Bulk Field Update — Applies a bulk field update to plan projects records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before c

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-projects
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
      "description": "The new field value(s) to apply to those records.",
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
      "description": "List of plan projects record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_projects_agent.py` and embedded as the fenced Python below (sha256 0f165597a35a0036…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_projects_agent.py` first:

```bash
python3 bulk_update_plan_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_projects_agent.py   # or on stdin
python3 bulk_update_plan_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan projects Bulk Field Update — Applies a bulk field update to plan projects records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before c

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-projects
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_projects',
    "version": '3.0.3',
    "display_name": 'Plan projects Bulk Field Update',
    "description": 'Applies a bulk field update to plan projects records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before c',
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
        "upstream_slug": 'bulk-update-plan-projects',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-projects',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a3a38cafdcfb91b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-projects'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-plan-projects', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of plan projects record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when plan projects records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to plan projects records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to plan projects records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before c', 'example_request': 'Bulk update these plan projects record IDs in USMF sandbox with the new value — show me the dry-run preview first.', 'inputs': [{'description': 'List of plan projects record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) on many plan projects records at once and want a before/after preview and approval step before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePlanProjects(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanProjects'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of plan projects record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePlanProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
