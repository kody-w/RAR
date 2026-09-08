---
name: "rar-cowork-cookbook-bulk-update-manage-signatures-and-signing-limits"
description: "Applies a bulk field update to Dynamics 365 signature and signing limit records in legal entity USMF via the ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_signatures_and_signing_limits", "rar_sha256": "be0d58c3ed93e6933c93d90318d17ccdad2d6bd253f559e8752d03ea7ce44d77", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_signatures_and_signing_limits`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_signatures_and_signing_limits_agent.py` and in the RCI capsule.

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

Manage signatures and signing limits Bulk Field Update — Applies a bulk field update to Dynamics 365 signature and signing limit records in legal entity USMF via the ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-signatures-and-signing-limits
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
      "description": "Explicit approval after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Target legal entity, default USMF; sandbox environment only.",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to those records.",
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
      "description": "List of manage-signatures/signing-limits record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_signatures_and_signing_limits_agent.py` and embedded as the fenced Python below (sha256 be0d58c3ed93e693…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_signatures_and_signing_limits_agent.py` first:

```bash
python3 bulk_update_manage_signatures_and_signing_limits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_signatures_and_signing_limits_agent.py   # or on stdin
python3 bulk_update_manage_signatures_and_signing_limits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage signatures and signing limits Bulk Field Update — Applies a bulk field update to Dynamics 365 signature and signing limit records in legal entity USMF via the ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-signatures-and-signing-limits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_signatures_and_signing_limits',
    "version": '3.0.3',
    "display_name": 'Manage signatures and signing limits Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 signature and signing limit records in legal entity USMF via the ERP plugin, producing a dry-run preview workbook for approval before committing changes.',
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
        "upstream_slug": 'bulk-update-manage-signatures-and-signing-limits',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-signatures-and-signing-limits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ae9c900569b0a295',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-signatures-and-signing-limits'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-manage-signatures-and-signing-limits', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Target legal entity, default USMF; sandbox environment only.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of manage-signatures/signing-limits record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when manage signatures and signing limits records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to manage signatures and signing limits records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 signature and signing limit records in legal entity USMF via the ERP plugin, producing a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk update these signing limit record IDs in USMF sandbox to a new limit — show me the dry-run first.', 'inputs': [{'description': 'List of manage-signatures/signing-limits record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Target legal entity, default USMF; sandbox environment only.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of signing-limit record IDs and new values to update in a D365 sandbox, and want a previewed, approval-gated bulk write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateManageSignaturesAndSigningLimits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageSignaturesAndSigningLimits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Target legal entity, default USMF; sandbox environment only.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of manage-signatures/signing-limits record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateManageSignaturesAndSigningLimits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
