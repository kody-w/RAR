---
name: "rar-cowork-cookbook-bulk-update-allocate-or-assign-software-licenses"
description: "Applies a bulk field update to software license allocation/assignment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_allocate_or_assign_software_licenses", "rar_sha256": "ef60e575f8cbec27b256aeea47a389922db4d106f0b38e36c00f249975d51457", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_allocate_or_assign_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_allocate_or_assign_software_licenses_agent.py` and in the RCI capsule.

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

Allocate or assign software licenses Bulk Field Update — Applies a bulk field update to software license allocation/assignment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-allocate-or-assign-software-licenses
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
      "description": "D365 legal entity to run against (USMF, sandbox first).",
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
      "description": "List of software license allocation/assignment record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_allocate_or_assign_software_licenses_agent.py` and embedded as the fenced Python below (sha256 ef60e575f8cbec27…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_allocate_or_assign_software_licenses_agent.py` first:

```bash
python3 bulk_update_allocate_or_assign_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_allocate_or_assign_software_licenses_agent.py   # or on stdin
python3 bulk_update_allocate_or_assign_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate or assign software licenses Bulk Field Update — Applies a bulk field update to software license allocation/assignment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-allocate-or-assign-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_allocate_or_assign_software_licenses',
    "version": '3.0.3',
    "display_name": 'Allocate or assign software licenses Bulk Field Update',
    "description": 'Applies a bulk field update to software license allocation/assignment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-allocate-or-assign-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-allocate-or-assign-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ebae9c9523407397',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/allocate-or-assign-software-licenses'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-allocate-or-assign-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (USMF, sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of software license allocation/assignment record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when allocate or assign software licenses records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to allocate or assign software licenses records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to software license allocation/assignment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook a', 'example_request': 'Bulk-update these software license records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of software license allocation/assignment record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (USMF, sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to change a field across many software license allocation/assignment records in D365 F&SCM at once and want a reviewable dry-run before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAllocateOrAssignSoftwareLicenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAllocateOrAssignSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (USMF, sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of software license allocation/assignment record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAllocateOrAssignSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
