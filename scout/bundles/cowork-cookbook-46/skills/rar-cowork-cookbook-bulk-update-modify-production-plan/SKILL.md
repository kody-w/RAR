---
name: "rar-cowork-cookbook-bulk-update-modify-production-plan"
description: "Applies a bulk field update to Dynamics 365 F&SCM production plan records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_modify_production_plan", "rar_sha256": "c54a6c354e8015b7badf4a57adccd982605b388e3fe40bf2866b3a373797cd0e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_modify_production_plan`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_modify_production_plan_agent.py` and in the RCI capsule.

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

Modify production plan Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM production plan records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-modify-production-plan
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
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "field_and_new_value": {
      "description": "The field(s) to change and the new value(s) to apply.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity / company to run against, e.g. USMF (sandbox first).",
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
      "description": "List of production plan record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_modify_production_plan_agent.py` and embedded as the fenced Python below (sha256 c54a6c354e8015b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_modify_production_plan_agent.py` first:

```bash
python3 bulk_update_modify_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_modify_production_plan_agent.py   # or on stdin
python3 bulk_update_modify_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Modify production plan Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM production plan records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-modify-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_modify_production_plan',
    "version": '3.0.3',
    "display_name": 'Modify production plan Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM production plan records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.',
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
        "upstream_slug": 'bulk-update-modify-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-modify-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c337897eacd1f3f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/modify-production-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-modify-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'field_and_new_value': 'The field(s) to change and the new value(s) to apply.', 'legal_entity': 'D365 legal entity / company to run against, e.g. USMF (sandbox first).', 'record_ids': 'List of production plan record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when modify production plan records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to modify production plan records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM production plan records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.', 'example_request': 'Bulk update these production plan records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'D365 legal entity / company to run against, e.g. USMF (sandbox first).', 'name': 'legal_entity'}, {'description': 'List of production plan record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) to change and the new value(s) to apply.', 'name': 'field_and_new_value'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many production plan records at once in D365 F&SCM and want a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateModifyProductionPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateModifyProductionPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'field_and_new_value': {'description': 'The field(s) to change and the new value(s) to apply.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity / company to run against, e.g. USMF (sandbox first).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of production plan record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateModifyProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
