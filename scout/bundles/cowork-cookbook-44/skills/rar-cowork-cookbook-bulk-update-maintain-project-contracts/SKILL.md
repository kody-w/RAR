---
name: "rar-cowork-cookbook-bulk-update-maintain-project-contracts"
description: "Applies a bulk field update to Dynamics 365 project contract records via the Cowork D365 ERP plugin: produces a dry-run preview workbook of before/after/status, waits for approval, then commits and emits a confirmation w"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_maintain_project_contracts", "rar_sha256": "5de81e06115ed8bf723c7d1ba3b69edc34a16dc201a3402edbc535e0d64d87c4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_maintain_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_maintain_project_contracts_agent.py` and in the RCI capsule.

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

Maintain project contracts Bulk Field Update — Applies a bulk field update to Dynamics 365 project contract records via the Cowork D365 ERP plugin: produces a dry-run preview workbook of before/after/status, waits for approval, then commits and emits a confirmation w

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-maintain-project-contracts
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
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; sandbox is required before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF.",
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
      "description": "List of project contract record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_maintain_project_contracts_agent.py` and embedded as the fenced Python below (sha256 5de81e06115ed8bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_maintain_project_contracts_agent.py` first:

```bash
python3 bulk_update_maintain_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_maintain_project_contracts_agent.py   # or on stdin
python3 bulk_update_maintain_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain project contracts Bulk Field Update — Applies a bulk field update to Dynamics 365 project contract records via the Cowork D365 ERP plugin: produces a dry-run preview workbook of before/after/status, waits for approval, then commits and emits a confirmation w

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-maintain-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_maintain_project_contracts',
    "version": '3.0.3',
    "display_name": 'Maintain project contracts Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 project contract records via the Cowork D365 ERP plugin: produces a dry-run preview workbook of before/after/status, waits for approval, then commits and emits a confirmation w',
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
        "upstream_slug": 'bulk-update-maintain-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-maintain-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e92d37feb49865df',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/maintain-project-contracts'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-maintain-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox is required before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of project contract record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when maintain project contracts records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to maintain project contracts records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 project contract records via the Cowork D365 ERP plugin: produces a dry-run preview workbook of before/after/status, waits for approval, then commits and emits a confirmation w', 'example_request': 'Bulk-update these project contract IDs in USMF sandbox to the new manager value — show me the dry run first.', 'inputs': [{'description': 'List of project contract record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox is required before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many project contract records at once in D365 F&SCM (sandbox first) and want a reviewable dry-run before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateMaintainProjectContracts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMaintainProjectContracts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox is required before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of project contract record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateMaintainProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
