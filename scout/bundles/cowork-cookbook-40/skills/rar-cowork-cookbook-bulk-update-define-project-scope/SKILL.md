---
name: "rar-cowork-cookbook-bulk-update-define-project-scope"
description: "Applies a bulk field update to define project scope records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appr"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_project_scope", "rar_sha256": "746e08e9fae7a8e51750850c4434a6f913e2ad500d4063bc17dfb07c58d06fca", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_project_scope`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_project_scope_agent.py` and in the RCI capsule.

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

Define project scope Bulk Field Update — Applies a bulk field update to define project scope records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appr

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-project-scope
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
      "description": "D365 legal entity to run against (default USMF, sandbox only).",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to those records.",
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
      "description": "List of define project scope record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_project_scope_agent.py` and embedded as the fenced Python below (sha256 746e08e9fae7a8e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_project_scope_agent.py` first:

```bash
python3 bulk_update_define_project_scope_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_project_scope_agent.py   # or on stdin
python3 bulk_update_define_project_scope_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project scope Bulk Field Update — Applies a bulk field update to define project scope records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appr

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-project-scope
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_project_scope',
    "version": '3.0.3',
    "display_name": 'Define project scope Bulk Field Update',
    "description": 'Applies a bulk field update to define project scope records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appr',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-project-scope',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-project-scope',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f26c76b2079df32',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/define-project-scope'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-define-project-scope', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (default USMF, sandbox only).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of define project scope record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define project scope records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define project scope records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to define project scope records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appr', 'example_request': 'Bulk update these project scope record IDs in USMF sandbox with the new owner value — show me a dry-run first.', 'inputs': [{'description': 'List of define project scope record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (default USMF, sandbox only).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many define project scope records at once in a D365 sandbox and want a before/after preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineProjectScope(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineProjectScope'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF, sandbox only).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of define project scope record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineProjectScope().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
