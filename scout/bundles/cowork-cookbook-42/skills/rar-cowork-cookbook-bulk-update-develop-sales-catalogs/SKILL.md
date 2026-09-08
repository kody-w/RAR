---
name: "rar-cowork-cookbook-bulk-update-develop-sales-catalogs"
description: "Applies a bulk field update to develop sales catalogs records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_sales_catalogs", "rar_sha256": "2d1e0e2d2e11b64770bfd910ecab155923b40f62e3dd0e403df317dc67aa3e3f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
