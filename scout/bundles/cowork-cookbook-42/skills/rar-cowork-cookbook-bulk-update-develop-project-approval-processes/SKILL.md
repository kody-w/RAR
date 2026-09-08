---
name: "rar-cowork-cookbook-bulk-update-develop-project-approval-processes"
description: "Applies a bulk field update to develop project approval processes records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_project_approval_processes", "rar_sha256": "34c5ce97f9790115e9da887c0e8ae34169e0dbe2fad02d0927ba7d23b1588907", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_project_approval_processes`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_project_approval_processes_agent.py` and in the RCI capsule.

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

Develop project approval processes Bulk Field Update — Applies a bulk field update to develop project approval processes records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, the

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-project-approval-processes
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
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; USMF sandbox by default.",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to each listed record.",
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
      "description": "List of develop project approval processes record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_project_approval_processes_agent.py` and embedded as the fenced Python below (sha256 34c5ce97f9790115…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_project_approval_processes_agent.py` first:

```bash
python3 bulk_update_develop_project_approval_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_project_approval_processes_agent.py   # or on stdin
python3 bulk_update_develop_project_approval_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project approval processes Bulk Field Update — Applies a bulk field update to develop project approval processes records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, the

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-project-approval-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_project_approval_processes',
    "version": '3.0.3',
    "display_name": 'Develop project approval processes Bulk Field Update',
    "description": 'Applies a bulk field update to develop project approval processes records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, the',
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
        "upstream_slug": 'bulk-update-develop-project-approval-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-project-approval-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cfd7778e50e181f2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-approval-processes'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-develop-project-approval-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The new field value(s) to apply to each listed record.', 'record_ids': 'List of develop project approval processes record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when develop project approval processes records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to develop project approval processes records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to develop project approval processes records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, the', 'example_request': 'Bulk update these project approval process records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of develop project approval processes record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to each listed record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of develop project approval processes record IDs and new field values to update in bulk in a D365 sandbox, with preview and approval first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDevelopProjectApprovalProcesses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopProjectApprovalProcesses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to each listed record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of develop project approval processes record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDevelopProjectApprovalProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
