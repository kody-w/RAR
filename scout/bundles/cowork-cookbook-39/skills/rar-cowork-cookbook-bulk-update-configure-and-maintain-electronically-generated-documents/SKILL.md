---
name: "rar-cowork-cookbook-bulk-update-configure-and-maintain-electronically-generated-documents"
description: "Applies a bulk field update to electronically generated document configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, producing a dry-run preview wor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_maintain_electronically_generated_documents", "rar_sha256": "5fc22da4b1b4019b43682839e0b7260e9cf1f599636d2c9274559d546d0459c0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
