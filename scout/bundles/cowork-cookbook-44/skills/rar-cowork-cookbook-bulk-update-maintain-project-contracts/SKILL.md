---
name: "rar-cowork-cookbook-bulk-update-maintain-project-contracts"
description: "Applies a bulk field update to Dynamics 365 project contract records via the Cowork D365 ERP plugin: produces a dry-run preview workbook of before/after/status, waits for approval, then commits and emits a confirmation w"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_maintain_project_contracts", "rar_sha256": "5de81e06115ed8bf723c7d1ba3b69edc34a16dc201a3402edbc535e0d64d87c4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
