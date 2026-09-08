---
name: "rar-cowork-cookbook-bulk-update-configure-and-maintain-electronically-generated-documents"
description: "Applies a bulk field update to electronically generated document configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, producing a dry-run preview wor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_maintain_electronically_generated_documents", "rar_sha256": "5fc22da4b1b4019b43682839e0b7260e9cf1f599636d2c9274559d546d0459c0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_configure_and_maintain_electronically_generated_documents`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_configure_and_maintain_electronically_generated_documents_agent.py` and in the RCI capsule.

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

Configure and maintain electronically generated documents Bulk Field Update — Applies a bulk field update to electronically generated document configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, producing a dry-run preview wor

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-maintain-electronically-generated-documents
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
      "description": "Dynamics 365 legal entity to run against (sandbox; defaults to USMF).",
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
      "description": "List of record IDs for the electronically generated document configuration records to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_configure_and_maintain_electronically_generated_documents_agent.py` and embedded as the fenced Python below (sha256 5fc22da4b1b4019b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_configure_and_maintain_electronically_generated_documents_agent.py` first:

```bash
python3 bulk_update_configure_and_maintain_electronically_generated_documents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_configure_and_maintain_electronically_generated_documents_agent.py   # or on stdin
python3 bulk_update_configure_and_maintain_electronically_generated_documents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and maintain electronically generated documents Bulk Field Update — Applies a bulk field update to electronically generated document configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, producing a dry-run preview wor

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-maintain-electronically-generated-documents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_configure_and_maintain_electronically_generated_documents',
    "version": '3.0.3',
    "display_name": 'Configure and maintain electronically generated documents Bulk Field Update',
    "description": 'Applies a bulk field update to electronically generated document configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, producing a dry-run preview wor',
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
        "upstream_slug": 'bulk-update-configure-and-maintain-electronically-generated-documents',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-configure-and-maintain-electronically-generated-documents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cf52dbdb2fb7523d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-maintain-electronically-generated-documents'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-configure-and-maintain-electronically-generated-documents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (sandbox; defaults to USMF).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of record IDs for the electronically generated document configuration records to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when configure and maintain electronically generated documents records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to configure and maintain electronically generated documents records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to electronically generated document configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, producing a dry-run preview wor', 'example_request': 'Bulk update these electronic document config records in USMF sandbox to the new value - show me a dry run first.', 'inputs': [{'description': 'List of record IDs for the electronically generated document configuration records to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against (sandbox; defaults to USMF).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-change field values on electronic document configuration records in D365 F&SCM with a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateConfigureAndMaintainElectronicallyGeneratedDocuments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConfigureAndMaintainElectronicallyGeneratedDocuments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (sandbox; defaults to USMF).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs for the electronically generated document configuration records to update.', 'type': 'string'}},
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
    print(BulkUpdateConfigureAndMaintainElectronicallyGeneratedDocuments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
