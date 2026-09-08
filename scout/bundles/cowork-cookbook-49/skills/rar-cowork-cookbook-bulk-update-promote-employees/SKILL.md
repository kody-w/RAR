---
name: "rar-cowork-cookbook-bulk-update-promote-employees"
description: "Applies a bulk field update to promote-employees records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_promote_employees", "rar_sha256": "75c863680c358893b207b7c6ad159dc93c7c59aec3e73efe876a791304fe9e1c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_promote_employees`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_promote_employees_agent.py` and in the RCI capsule.

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

Promote employees Bulk Field Update — Applies a bulk field update to promote-employees records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-promote-employees
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
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to each record.",
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
      "description": "List of promote employees record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_promote_employees_agent.py` and embedded as the fenced Python below (sha256 75c863680c358893…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_promote_employees_agent.py` first:

```bash
python3 bulk_update_promote_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_promote_employees_agent.py   # or on stdin
python3 bulk_update_promote_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Promote employees Bulk Field Update — Applies a bulk field update to promote-employees records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-promote-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_promote_employees',
    "version": '3.0.3',
    "display_name": 'Promote employees Bulk Field Update',
    "description": 'Applies a bulk field update to promote-employees records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation',
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
        "upstream_slug": 'bulk-update-promote-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-promote-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd2f7ce1d81fef422',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/promote-employees'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-promote-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The new field value(s) to apply to each record.', 'record_ids': 'List of promote employees record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when promote employees records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to promote employees records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to promote-employees records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation', 'example_request': 'Bulk update these promote employees record IDs in USMF sandbox to the new value - show me the dry-run first.', 'inputs': [{'description': 'List of promote employees record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of promote employees record IDs and new values to update in bulk in a D365 sandbox, and want a reviewed dry-run before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePromoteEmployees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePromoteEmployees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of promote employees record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePromoteEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
