---
name: "rar-cowork-cookbook-bulk-update-respond-to-non-compliance"
description: "Applies a bulk field update to Dynamics 365 F&SCM respond-to-non-compliance records via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and a confirmation workbook"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_respond_to_non_compliance", "rar_sha256": "2f6c9350496f26eb7cc15b409763507c95cb4e06147402202de71762a1fd365d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
