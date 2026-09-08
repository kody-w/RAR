---
name: "rar-cowork-cookbook-bulk-update-request-time-off"
description: "Applies a bulk field update to Dynamics 365 request time off records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_request_time_off", "rar_sha256": "798c1f833e3e6c5202e3ee2cc13110d7d8dc49ba94fddc962c58508c62160c29", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_request_time_off`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_request_time_off_agent.py` and in the RCI capsule.

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

Request time off Bulk Field Update — Applies a bulk field update to Dynamics 365 request time off records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-request-time-off
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
      "description": "Explicit confirmation after reviewing the dry-run preview workbook, before changes are written.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; sandbox environment only.",
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
      "description": "List of request time off record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_request_time_off_agent.py` and embedded as the fenced Python below (sha256 798c1f833e3e6c52…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_request_time_off_agent.py` first:

```bash
python3 bulk_update_request_time_off_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_request_time_off_agent.py   # or on stdin
python3 bulk_update_request_time_off_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Request time off Bulk Field Update — Applies a bulk field update to Dynamics 365 request time off records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-request-time-off
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_request_time_off',
    "version": '3.0.3',
    "display_name": 'Request time off Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 request time off records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook.',
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
        "upstream_slug": 'bulk-update-request-time-off',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-request-time-off',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cb799e4c894a67b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/request-time-off'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-request-time-off', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the dry-run preview workbook, before changes are written.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of request time off record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when request time off records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to request time off records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 request time off records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook.', 'example_request': 'Bulk update these time off record IDs in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'name': 'legal_entity'}, {'description': 'List of request time off record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Explicit confirmation after reviewing the dry-run preview workbook, before changes are written.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many request time off records in D365 F&SCM (sandbox) with a reviewed dry-run before commit.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateRequestTimeOff(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRequestTimeOff'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the dry-run preview workbook, before changes are written.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of request time off record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateRequestTimeOff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
