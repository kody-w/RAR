---
name: "rar-cowork-cookbook-bulk-update-plan-projects"
description: "Applies a bulk field update to plan projects records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_projects", "rar_sha256": "0f165597a35a00361fcd660df95632679fc4bf8e9fc02cf01c1a9a5df39c8fb5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
