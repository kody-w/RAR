---
name: "rar-cowork-cookbook-bulk-update-maintain-quality-certifications"
description: "Applies a bulk field update to quality certification records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing changes"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_maintain_quality_certifications", "rar_sha256": "c24d905aac35c9fa41d576c940467a759a27e60cec8add4cd29c4d3f00364c32", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_maintain_quality_certifications`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_maintain_quality_certifications_agent.py` and in the RCI capsule.

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

Maintain quality certifications Bulk Field Update — Applies a bulk field update to quality certification records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing changes

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-maintain-quality-certifications
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
      "description": "List of quality certification record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_maintain_quality_certifications_agent.py` and embedded as the fenced Python below (sha256 c24d905aac35c9fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_maintain_quality_certifications_agent.py` first:

```bash
python3 bulk_update_maintain_quality_certifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_maintain_quality_certifications_agent.py   # or on stdin
python3 bulk_update_maintain_quality_certifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain quality certifications Bulk Field Update — Applies a bulk field update to quality certification records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing changes

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-maintain-quality-certifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_maintain_quality_certifications',
    "version": '3.0.3',
    "display_name": 'Maintain quality certifications Bulk Field Update',
    "description": 'Applies a bulk field update to quality certification records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing changes',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-maintain-quality-certifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-maintain-quality-certifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ba2c93b9608b6a22',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/maintain-quality-certifications'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-maintain-quality-certifications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of quality certification record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when maintain quality certifications records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to maintain quality certifications records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to quality certification records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing changes', 'example_request': 'Bulk update these quality certification records in USMF sandbox to the new expiry date — show me a dry run first.', 'inputs': [{'description': 'List of quality certification record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of quality certification record IDs and new values to update in bulk in a D365 sandbox, and want a reviewable preview before writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateMaintainQualityCertifications(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMaintainQualityCertifications'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of quality certification record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateMaintainQualityCertifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
