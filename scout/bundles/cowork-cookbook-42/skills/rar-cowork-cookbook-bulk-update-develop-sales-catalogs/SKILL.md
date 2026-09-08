---
name: "rar-cowork-cookbook-bulk-update-develop-sales-catalogs"
description: "Applies a bulk field update to develop sales catalogs records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_sales_catalogs", "rar_sha256": "2d1e0e2d2e11b64770bfd910ecab155923b40f62e3dd0e403df317dc67aa3e3f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_sales_catalogs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_sales_catalogs_agent.py` and in the RCI capsule.

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

Develop sales catalogs Bulk Field Update — Applies a bulk field update to develop sales catalogs records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a c

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-sales-catalogs
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
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of develop sales catalogs record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_sales_catalogs_agent.py` and embedded as the fenced Python below (sha256 2d1e0e2d2e11b647…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_sales_catalogs_agent.py` first:

```bash
python3 bulk_update_develop_sales_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_sales_catalogs_agent.py   # or on stdin
python3 bulk_update_develop_sales_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales catalogs Bulk Field Update — Applies a bulk field update to develop sales catalogs records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a c

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-sales-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_sales_catalogs',
    "version": '3.0.3',
    "display_name": 'Develop sales catalogs Bulk Field Update',
    "description": 'Applies a bulk field update to develop sales catalogs records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a c',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-sales-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-sales-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7eb3a9f7bbf150fd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-sales-catalogs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-develop-sales-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of develop sales catalogs record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when develop sales catalogs records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to develop sales catalogs records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to develop sales catalogs records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a c', 'example_request': 'Bulk update these sales catalog record IDs to the new value in USMF sandbox — show me the dry-run first.', 'inputs': [{'description': 'List of develop sales catalogs record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of develop sales catalogs record IDs and want a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDevelopSalesCatalogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopSalesCatalogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of develop sales catalogs record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDevelopSalesCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
