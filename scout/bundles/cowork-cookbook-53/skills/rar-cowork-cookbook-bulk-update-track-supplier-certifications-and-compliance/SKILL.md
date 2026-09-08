---
name: "rar-cowork-cookbook-bulk-update-track-supplier-certifications-and-compliance"
description: "Applies a bulk field update to supplier certification and compliance records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_supplier_certifications_and_compliance", "rar_sha256": "f5666e73a62efa63d17e070095771b596aa8d687db12c8a01902dd5f9e670462", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
