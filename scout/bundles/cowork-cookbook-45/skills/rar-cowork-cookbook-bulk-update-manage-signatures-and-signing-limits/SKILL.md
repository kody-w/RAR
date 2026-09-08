---
name: "rar-cowork-cookbook-bulk-update-manage-signatures-and-signing-limits"
description: "Applies a bulk field update to Dynamics 365 signature and signing limit records in legal entity USMF via the ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_signatures_and_signing_limits", "rar_sha256": "be0d58c3ed93e6933c93d90318d17ccdad2d6bd253f559e8752d03ea7ce44d77", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
