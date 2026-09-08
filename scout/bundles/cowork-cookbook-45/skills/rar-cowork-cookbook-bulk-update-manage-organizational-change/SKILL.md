---
name: "rar-cowork-cookbook-bulk-update-manage-organizational-change"
description: "Applies a bulk field update to organizational change records in Dynamics 365 F&SCM (legal entity USMF, sandbox) \u2014 returns a dry-run preview workbook of before/after/status, pauses for approval, then a confirmation workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_organizational_change", "rar_sha256": "cf73673d3cda67cf96d6d1019dc8dc4965294ca27619d35b4b2499f8f5fa8ed5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_organizational_change`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_organizational_change_agent.py` and in the RCI capsule.

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

Manage organizational change Bulk Field Update — Applies a bulk field update to organizational change records in Dynamics 365 F&SCM (legal entity USMF, sandbox) — returns a dry-run preview workbook of before/after/status, pauses for approval, then a confirmation workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-organizational-change
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are committed.",
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
      "description": "List of organizational change record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_organizational_change_agent.py` and embedded as the fenced Python below (sha256 cf73673d3cda67cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_organizational_change_agent.py` first:

```bash
python3 bulk_update_manage_organizational_change_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_organizational_change_agent.py   # or on stdin
python3 bulk_update_manage_organizational_change_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage organizational change Bulk Field Update — Applies a bulk field update to organizational change records in Dynamics 365 F&SCM (legal entity USMF, sandbox) — returns a dry-run preview workbook of before/after/status, pauses for approval, then a confirmation workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-organizational-change
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_organizational_change',
    "version": '3.0.3',
    "display_name": 'Manage organizational change Bulk Field Update',
    "description": 'Applies a bulk field update to organizational change records in Dynamics 365 F&SCM (legal entity USMF, sandbox) — returns a dry-run preview workbook of before/after/status, pauses for approval, then a confirmation workbo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-organizational-change',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-organizational-change',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6cae783de7bd1658',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/manage-organizational-change'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-manage-organizational-change', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of organizational change record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when manage organizational change records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to manage organizational change records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to organizational change records in Dynamics 365 F&SCM (legal entity USMF, sandbox) — returns a dry-run preview workbook of before/after/status, pauses for approval, then a confirmation workbo', 'example_request': 'Bulk update these org change record IDs in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of organizational change record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many organizational change records at once and want a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateManageOrganizationalChange(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageOrganizationalChange'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of organizational change record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateManageOrganizationalChange().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
