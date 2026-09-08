---
name: "rar-cowork-cookbook-bulk-update-depreciate-assets"
description: "Applies a bulk field update to depreciate assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confirmation wor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_depreciate_assets", "rar_sha256": "612dc09d6ff3f9b9b9d569d78c07396694c666898d885d8cdd250b440094bf51", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_depreciate_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_depreciate_assets_agent.py` and in the RCI capsule.

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

Depreciate assets Bulk Field Update — Applies a bulk field update to depreciate assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confirmation wor

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-depreciate-assets
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are committed.",
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
      "description": "List of depreciate assets record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_depreciate_assets_agent.py` and embedded as the fenced Python below (sha256 612dc09d6ff3f9b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_depreciate_assets_agent.py` first:

```bash
python3 bulk_update_depreciate_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_depreciate_assets_agent.py   # or on stdin
python3 bulk_update_depreciate_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Depreciate assets Bulk Field Update — Applies a bulk field update to depreciate assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confirmation wor

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-depreciate-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_depreciate_assets',
    "version": '3.0.3',
    "display_name": 'Depreciate assets Bulk Field Update',
    "description": 'Applies a bulk field update to depreciate assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confirmation wor',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-depreciate-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-depreciate-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1fe8db6788cc6ece',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/depreciate-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-depreciate-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of depreciate assets record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when depreciate assets records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to depreciate assets records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to depreciate assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, pauses for approval, then a confirmation wor', 'example_request': 'Bulk update these depreciate assets record IDs in USMF sandbox with the new values - show me a dry-run first.', 'inputs': [{'description': 'List of depreciate assets record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of depreciate assets record IDs and new values to update in bulk in a D365 sandbox, and want a before/after preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDepreciateAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDepreciateAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of depreciate assets record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDepreciateAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
