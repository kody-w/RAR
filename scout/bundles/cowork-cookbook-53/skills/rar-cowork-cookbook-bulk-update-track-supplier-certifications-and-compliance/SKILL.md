---
name: "rar-cowork-cookbook-bulk-update-track-supplier-certifications-and-compliance"
description: "Applies a bulk field update to supplier certification and compliance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_supplier_certifications_and_compliance", "rar_sha256": "f5666e73a62efa63d17e070095771b596aa8d687db12c8a01902dd5f9e670462", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_track_supplier_certifications_and_compliance`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_track_supplier_certifications_and_compliance_agent.py` and in the RCI capsule.

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

Track supplier certifications and compliance Bulk Field Update — Applies a bulk field update to supplier certification and compliance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-track-supplier-certifications-and-compliance
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
      "description": "Explicit user approval after reviewing the dry-run preview, required before changes are applied.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; USMF sandbox by default.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to each listed record.",
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
      "description": "List of supplier certification/compliance record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_track_supplier_certifications_and_compliance_agent.py` and embedded as the fenced Python below (sha256 f5666e73a62efa63…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_track_supplier_certifications_and_compliance_agent.py` first:

```bash
python3 bulk_update_track_supplier_certifications_and_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_track_supplier_certifications_and_compliance_agent.py   # or on stdin
python3 bulk_update_track_supplier_certifications_and_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track supplier certifications and compliance Bulk Field Update — Applies a bulk field update to supplier certification and compliance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-track-supplier-certifications-and-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_track_supplier_certifications_and_compliance',
    "version": '3.0.3',
    "display_name": 'Track supplier certifications and compliance Bulk Field Update',
    "description": 'Applies a bulk field update to supplier certification and compliance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-track-supplier-certifications-and-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-track-supplier-certifications-and-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '771134c850f21291',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/track-supplier-certifications-and-compliance'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-track-supplier-certifications-and-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the dry-run preview, required before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to each listed record.', 'record_ids': 'List of supplier certification/compliance record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when track supplier certifications and compliance records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to track supplier certifications and compliance records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to supplier certification and compliance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbo', 'example_request': 'Bulk update these supplier compliance records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of supplier certification/compliance record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each listed record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the dry-run preview, required before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants to change a field on many supplier certification/compliance records at once and needs a before/after preview to approve before the write is committed.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateTrackSupplierCertificationsAndCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateTrackSupplierCertificationsAndCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the dry-run preview, required before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each listed record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of supplier certification/compliance record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateTrackSupplierCertificationsAndCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
