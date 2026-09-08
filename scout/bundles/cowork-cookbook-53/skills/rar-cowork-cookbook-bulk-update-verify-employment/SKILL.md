---
name: "rar-cowork-cookbook-bulk-update-verify-employment"
description: "Applies a bulk field update to verify-employment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval, then a confirmation workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_verify_employment", "rar_sha256": "045e54becc641752d225ea87e6a5f9a04076e7c8de6ed23a330513c343092f21", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_verify_employment`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_verify_employment_agent.py` and in the RCI capsule.

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

Verify employment Bulk Field Update — Applies a bulk field update to verify-employment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval, then a confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-verify-employment
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
      "description": "Explicit go-ahead after reviewing the dry-run preview, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against (USMF sandbox by default).",
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
      "description": "List of verify-employment record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_verify_employment_agent.py` and embedded as the fenced Python below (sha256 045e54becc641752…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_verify_employment_agent.py` first:

```bash
python3 bulk_update_verify_employment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_verify_employment_agent.py   # or on stdin
python3 bulk_update_verify_employment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Verify employment Bulk Field Update — Applies a bulk field update to verify-employment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval, then a confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-verify-employment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_verify_employment',
    "version": '3.0.3',
    "display_name": 'Verify employment Bulk Field Update',
    "description": 'Applies a bulk field update to verify-employment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval, then a confirmation workbook.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-verify-employment',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-verify-employment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '625b4b5a96573004',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/verify-employment'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-verify-employment', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (USMF sandbox by default).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of verify-employment record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when verify employment records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to verify employment records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to verify-employment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval, then a confirmation workbook.', 'example_request': 'Bulk update these verify employment record IDs in USMF sandbox with the new value — show me the dry-run first.', 'inputs': [{'description': 'List of verify-employment record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against (USMF sandbox by default).', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many verify-employment records at once and want a before/after dry-run preview to approve before the write is committed.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateVerifyEmployment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateVerifyEmployment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (USMF sandbox by default).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of verify-employment record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateVerifyEmployment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
