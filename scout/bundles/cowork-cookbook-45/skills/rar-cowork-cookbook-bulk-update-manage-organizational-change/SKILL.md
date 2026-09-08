---
name: "rar-cowork-cookbook-bulk-update-manage-organizational-change"
description: "Applies a bulk field update to organizational change records in Dynamics 365 F&SCM (legal entity USMF, sandbox) \u2014 returns a dry-run preview workbook of before/after/status, pauses for approval, then a confirmation workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_organizational_change", "rar_sha256": "cf73673d3cda67cf96d6d1019dc8dc4965294ca27619d35b4b2499f8f5fa8ed5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
