---
name: "rar-cowork-cookbook-bulk-update-request-time-off"
description: "Applies a bulk field update to Dynamics 365 request time off records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_request_time_off", "rar_sha256": "798c1f833e3e6c5202e3ee2cc13110d7d8dc49ba94fddc962c58508c62160c29", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
