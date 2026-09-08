---
name: "rar-cowork-cookbook-bulk-update-develop-project-approval-processes"
description: "Applies a bulk field update to develop project approval processes records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_project_approval_processes", "rar_sha256": "34c5ce97f9790115e9da887c0e8ae34169e0dbe2fad02d0927ba7d23b1588907", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
