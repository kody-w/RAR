---
name: "rar-cowork-cookbook-bulk-update-define-operating-hours-and-schedule"
description: "Applies a bulk field update to operating-hours/schedule records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval ga"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_operating_hours_and_schedule", "rar_sha256": "b875cd6346081b8151986812c4fd1af4f2a83e45a0c09879ad7674e9cd489969", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
