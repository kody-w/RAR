---
name: "rar-cowork-cookbook-bulk-update-define-operating-hours-and-schedule"
description: "Applies a bulk field update to operating-hours/schedule records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval ga"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_operating_hours_and_schedule", "rar_sha256": "b875cd6346081b8151986812c4fd1af4f2a83e45a0c09879ad7674e9cd489969", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_operating_hours_and_schedule`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_operating_hours_and_schedule_agent.py` and in the RCI capsule.

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

Define operating hours and schedule Bulk Field Update — Applies a bulk field update to operating-hours/schedule records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval ga

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-operating-hours-and-schedule
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, required before changes are applied.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of operating hours/schedule record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_operating_hours_and_schedule_agent.py` and embedded as the fenced Python below (sha256 b875cd6346081b81…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_operating_hours_and_schedule_agent.py` first:

```bash
python3 bulk_update_define_operating_hours_and_schedule_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_operating_hours_and_schedule_agent.py   # or on stdin
python3 bulk_update_define_operating_hours_and_schedule_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define operating hours and schedule Bulk Field Update — Applies a bulk field update to operating-hours/schedule records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval ga

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-operating-hours-and-schedule
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_operating_hours_and_schedule',
    "version": '3.0.3',
    "display_name": 'Define operating hours and schedule Bulk Field Update',
    "description": 'Applies a bulk field update to operating-hours/schedule records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval ga',
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
        "upstream_slug": 'bulk-update-define-operating-hours-and-schedule',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-operating-hours-and-schedule',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f981273a5e6820d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-operating-hours-and-schedule'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-define-operating-hours-and-schedule', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, required before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of operating hours/schedule record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define operating hours and schedule records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define operating hours and schedule records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to operating-hours/schedule records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval ga', 'example_request': 'Bulk-update these schedule record IDs in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of operating hours/schedule record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, required before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many D365 operating hours/schedule records at once and want a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineOperatingHoursAndSchedule(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineOperatingHoursAndSchedule'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, required before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of operating hours/schedule record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineOperatingHoursAndSchedule().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
