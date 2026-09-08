---
name: "rar-cowork-cookbook-bulk-update-promote-employees"
description: "Applies a bulk field update to promote-employees records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_promote_employees", "rar_sha256": "75c863680c358893b207b7c6ad159dc93c7c59aec3e73efe876a791304fe9e1c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
