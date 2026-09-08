---
name: "rar-cowork-cookbook-bulk-update-record-production-costs"
description: "Applies a bulk field update to record production costs records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_production_costs", "rar_sha256": "ee917a814c421ace902adb2d4e9b92e2f9c287f362ab9f7f0fe5a5e576cce1b5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_record_production_costs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_record_production_costs_agent.py` and in the RCI capsule.

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

Record production costs Bulk Field Update — Applies a bulk field update to record production costs records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confi

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-production-costs
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
      "description": "List of record production costs record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_record_production_costs_agent.py` and embedded as the fenced Python below (sha256 ee917a814c421ace…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_record_production_costs_agent.py` first:

```bash
python3 bulk_update_record_production_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_record_production_costs_agent.py   # or on stdin
python3 bulk_update_record_production_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record production costs Bulk Field Update — Applies a bulk field update to record production costs records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confi

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-production-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_record_production_costs',
    "version": '3.0.3',
    "display_name": 'Record production costs Bulk Field Update',
    "description": 'Applies a bulk field update to record production costs records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confi',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-record-production-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-record-production-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5c69ffb66c6539ed',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/record-production-costs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-record-production-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of record production costs record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when record production costs records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to record production costs records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to record production costs records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confi', 'example_request': 'Bulk update these record production costs IDs in USMF sandbox with the new value — show me the dry-run first.', 'inputs': [{'description': 'List of record production costs record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many record production costs records at once and want a before/after preview and approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateRecordProductionCosts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRecordProductionCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record production costs record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateRecordProductionCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
