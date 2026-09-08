---
name: "rar-cowork-cookbook-bulk-update-perform-corrective-maintenance"
description: "Applies a bulk field update to corrective maintenance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing changes"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_corrective_maintenance", "rar_sha256": "7393da6f391d99eba5005e282e54e27c01d6079911e41212a29d06434b21ef0f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_perform_corrective_maintenance`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_perform_corrective_maintenance_agent.py` and in the RCI capsule.

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

Perform corrective maintenance Bulk Field Update — Applies a bulk field update to corrective maintenance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing changes

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-corrective-maintenance
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
      "description": "List of corrective maintenance record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_perform_corrective_maintenance_agent.py` and embedded as the fenced Python below (sha256 7393da6f391d99eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_perform_corrective_maintenance_agent.py` first:

```bash
python3 bulk_update_perform_corrective_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_perform_corrective_maintenance_agent.py   # or on stdin
python3 bulk_update_perform_corrective_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform corrective maintenance Bulk Field Update — Applies a bulk field update to corrective maintenance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing changes

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-corrective-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_perform_corrective_maintenance',
    "version": '3.0.3',
    "display_name": 'Perform corrective maintenance Bulk Field Update',
    "description": 'Applies a bulk field update to corrective maintenance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing changes',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-perform-corrective-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-perform-corrective-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '157c75b7552688b2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-corrective-maintenance'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-perform-corrective-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of corrective maintenance record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when perform corrective maintenance records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to perform corrective maintenance records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to corrective maintenance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing changes', 'example_request': 'Bulk update these corrective maintenance record IDs in USMF sandbox with a new value — show me the dry-run first.', 'inputs': [{'description': 'List of corrective maintenance record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of corrective maintenance record IDs and new field values to update in bulk in a D365 sandbox, and want a reviewed dry-run before writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePerformCorrectiveMaintenance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePerformCorrectiveMaintenance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of corrective maintenance record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePerformCorrectiveMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
