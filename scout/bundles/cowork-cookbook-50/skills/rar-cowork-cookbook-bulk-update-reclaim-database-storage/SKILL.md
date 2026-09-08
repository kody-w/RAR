---
name: "rar-cowork-cookbook-bulk-update-reclaim-database-storage"
description: "Applies a bulk field update to reclaim-database-storage records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, with a dry-run preview workbook and approval gate before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reclaim_database_storage", "rar_sha256": "8030e2a7b4575b90313ec63f1ab760bd1d269d719b8aa6ebb1674f2f12b8840d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_reclaim_database_storage`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_reclaim_database_storage_agent.py` and in the RCI capsule.

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

Reclaim database storage Bulk Field Update — Applies a bulk field update to reclaim-database-storage records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, with a dry-run preview workbook and approval gate before commit.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reclaim-database-storage
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
      "description": "D365 legal entity to run against; USMF sandbox by default.",
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
      "description": "List of reclaim database storage record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reclaim_database_storage_agent.py` and embedded as the fenced Python below (sha256 8030e2a7b4575b90…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reclaim_database_storage_agent.py` first:

```bash
python3 bulk_update_reclaim_database_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_reclaim_database_storage_agent.py   # or on stdin
python3 bulk_update_reclaim_database_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reclaim database storage Bulk Field Update — Applies a bulk field update to reclaim-database-storage records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, with a dry-run preview workbook and approval gate before commit.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reclaim-database-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_reclaim_database_storage',
    "version": '3.0.3',
    "display_name": 'Reclaim database storage Bulk Field Update',
    "description": 'Applies a bulk field update to reclaim-database-storage records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, with a dry-run preview workbook and approval gate before commit.',
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
        "upstream_slug": 'bulk-update-reclaim-database-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-reclaim-database-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9a5b82d562c7c428',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/reclaim-database-storage'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-reclaim-database-storage', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of reclaim database storage record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when reclaim database storage records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to reclaim database storage records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to reclaim-database-storage records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, with a dry-run preview workbook and approval gate before commit.', 'example_request': 'Bulk-update these reclaim database storage records in USMF sandbox — show me a dry-run preview first.', 'inputs': [{'description': 'List of reclaim database storage record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change one or more fields across many reclaim database storage records at once in a D365 sandbox, with a reviewable before/after preview.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateReclaimDatabaseStorage(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReclaimDatabaseStorage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of reclaim database storage record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateReclaimDatabaseStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
