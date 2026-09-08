---
name: "rar-cowork-cookbook-bulk-update-manage-opportunity-process"
description: "Applies a bulk field update to Dynamics 365 manage opportunity process records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_opportunity_process", "rar_sha256": "5f41daa4cc1a03eade6504344636922ce2e36cf932b41f82ab6ad11e8b97546a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_opportunity_process`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_opportunity_process_agent.py` and in the RCI capsule.

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

Manage opportunity process Bulk Field Update — Applies a bulk field update to Dynamics 365 manage opportunity process records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-opportunity-process
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
      "description": "Dynamics 365 legal entity to run against; USMF sandbox by default.",
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
      "description": "List of manage opportunity process record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_opportunity_process_agent.py` and embedded as the fenced Python below (sha256 5f41daa4cc1a03ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_opportunity_process_agent.py` first:

```bash
python3 bulk_update_manage_opportunity_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_opportunity_process_agent.py   # or on stdin
python3 bulk_update_manage_opportunity_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage opportunity process Bulk Field Update — Applies a bulk field update to Dynamics 365 manage opportunity process records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-opportunity-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_opportunity_process',
    "version": '3.0.3',
    "display_name": 'Manage opportunity process Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 manage opportunity process records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-opportunity-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-opportunity-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '14b5eaf285e0b5a0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-manage-opportunity-process', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of manage opportunity process record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when manage opportunity process records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to manage opportunity process records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 manage opportunity process records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk update these opportunity process records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of manage opportunity process record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many manage opportunity process records at once and want a before/after preview and approval step first (sandbox only).'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateManageOpportunityProcess(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageOpportunityProcess'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of manage opportunity process record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateManageOpportunityProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
