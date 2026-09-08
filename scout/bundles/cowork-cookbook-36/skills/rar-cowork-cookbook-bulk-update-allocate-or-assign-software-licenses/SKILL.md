---
name: "rar-cowork-cookbook-bulk-update-allocate-or-assign-software-licenses"
description: "Applies a bulk field update to software license allocation/assignment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_allocate_or_assign_software_licenses", "rar_sha256": "ef60e575f8cbec27b256aeea47a389922db4d106f0b38e36c00f249975d51457", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
