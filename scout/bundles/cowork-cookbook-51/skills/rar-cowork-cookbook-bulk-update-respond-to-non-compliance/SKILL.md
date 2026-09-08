---
name: "rar-cowork-cookbook-bulk-update-respond-to-non-compliance"
description: "Applies a bulk field update to Dynamics 365 F&SCM respond-to-non-compliance records via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and a confirmation workbook"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_respond_to_non_compliance", "rar_sha256": "2f6c9350496f26eb7cc15b409763507c95cb4e06147402202de71762a1fd365d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_respond_to_non_compliance`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_respond_to_non_compliance_agent.py` and in the RCI capsule.

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

Respond to non-compliance Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM respond-to-non-compliance records via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and a confirmation workbook

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-respond-to-non-compliance
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
      "description": "D365 legal entity to run against (e.g. USMF); sandbox only.",
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
      "description": "List of respond-to-non-compliance record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_respond_to_non_compliance_agent.py` and embedded as the fenced Python below (sha256 2f6c9350496f26eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_respond_to_non_compliance_agent.py` first:

```bash
python3 bulk_update_respond_to_non_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_respond_to_non_compliance_agent.py   # or on stdin
python3 bulk_update_respond_to_non_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Respond to non-compliance Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM respond-to-non-compliance records via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and a confirmation workbook

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-respond-to-non-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_respond_to_non_compliance',
    "version": '3.0.3',
    "display_name": 'Respond to non-compliance Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM respond-to-non-compliance records via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and a confirmation workbook',
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
        "upstream_slug": 'bulk-update-respond-to-non-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-respond-to-non-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee249f3daf3d7017',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/respond-to-non-compliance'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-respond-to-non-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); sandbox only.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of respond-to-non-compliance record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when respond to non-compliance records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to respond to non-compliance records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM respond-to-non-compliance records via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and a confirmation workbook', 'example_request': 'Bulk update these non-compliance record IDs in USMF sandbox to the new status - show me the dry-run first.', 'inputs': [{'description': 'List of respond-to-non-compliance record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (e.g. USMF); sandbox only.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many respond-to-non-compliance records at once in a D365 sandbox legal entity, with a reviewable dry-run first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateRespondToNonCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRespondToNonCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); sandbox only.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of respond-to-non-compliance record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateRespondToNonCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
