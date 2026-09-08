---
name: "rar-cowork-cookbook-bulk-update-verify-employment"
description: "Applies a bulk field update to verify-employment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval, then a confirmation workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_verify_employment", "rar_sha256": "045e54becc641752d225ea87e6a5f9a04076e7c8de6ed23a330513c343092f21", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
