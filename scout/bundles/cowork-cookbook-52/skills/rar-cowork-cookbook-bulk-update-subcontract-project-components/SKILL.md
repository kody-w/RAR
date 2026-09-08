---
name: "rar-cowork-cookbook-bulk-update-subcontract-project-components"
description: "Applies a bulk field update to subcontract project components records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_subcontract_project_components", "rar_sha256": "75fb92e5d3175db1a1326119ac75915745ca2f897b368743ea47474a7296d403", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_subcontract_project_components`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_subcontract_project_components_agent.py` and in the RCI capsule.

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

Subcontract project components Bulk Field Update — Applies a bulk field update to subcontract project components records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-subcontract-project-components
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
      "description": "List of subcontract project components record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_subcontract_project_components_agent.py` and embedded as the fenced Python below (sha256 75fb92e5d3175db1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_subcontract_project_components_agent.py` first:

```bash
python3 bulk_update_subcontract_project_components_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_subcontract_project_components_agent.py   # or on stdin
python3 bulk_update_subcontract_project_components_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Subcontract project components Bulk Field Update — Applies a bulk field update to subcontract project components records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-subcontract-project-components
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_subcontract_project_components',
    "version": '3.0.3',
    "display_name": 'Subcontract project components Bulk Field Update',
    "description": 'Applies a bulk field update to subcontract project components records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for',
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
        "upstream_slug": 'bulk-update-subcontract-project-components',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-subcontract-project-components',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '49fabe5eef5a48cd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/subcontract-project-components'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-subcontract-project-components', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of subcontract project components record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when subcontract project components records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to subcontract project components records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to subcontract project components records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for', 'example_request': 'Bulk update these subcontract project components in USMF sandbox to the new value — show me the dry-run preview first.', 'inputs': [{'description': 'List of subcontract project components record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change one or more fields on many subcontract project components records at once and want a before/after preview and approval gate first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateSubcontractProjectComponents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateSubcontractProjectComponents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of subcontract project components record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateSubcontractProjectComponents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
