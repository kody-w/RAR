---
name: "rar-cowork-cookbook-bulk-update-reclaim-database-storage"
description: "Applies a bulk field update to reclaim-database-storage records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, with a dry-run preview workbook and approval gate before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reclaim_database_storage", "rar_sha256": "8030e2a7b4575b90313ec63f1ab760bd1d269d719b8aa6ebb1674f2f12b8840d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
