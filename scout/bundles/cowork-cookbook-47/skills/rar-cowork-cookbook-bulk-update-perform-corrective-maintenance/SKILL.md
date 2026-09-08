---
name: "rar-cowork-cookbook-bulk-update-perform-corrective-maintenance"
description: "Applies a bulk field update to corrective maintenance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing changes"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_corrective_maintenance", "rar_sha256": "7393da6f391d99eba5005e282e54e27c01d6079911e41212a29d06434b21ef0f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
