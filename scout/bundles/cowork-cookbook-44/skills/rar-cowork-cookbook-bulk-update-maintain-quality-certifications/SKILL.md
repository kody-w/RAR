---
name: "rar-cowork-cookbook-bulk-update-maintain-quality-certifications"
description: "Applies a bulk field update to quality certification records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing changes"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_maintain_quality_certifications", "rar_sha256": "c24d905aac35c9fa41d576c940467a759a27e60cec8add4cd29c4d3f00364c32", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
