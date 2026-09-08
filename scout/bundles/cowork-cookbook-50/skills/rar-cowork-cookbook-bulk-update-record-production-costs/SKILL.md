---
name: "rar-cowork-cookbook-bulk-update-record-production-costs"
description: "Applies a bulk field update to record production costs records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_production_costs", "rar_sha256": "ee917a814c421ace902adb2d4e9b92e2f9c287f362ab9f7f0fe5a5e576cce1b5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
