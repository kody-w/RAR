---
name: "rar-cowork-cookbook-bulk-update-develop-a-disaster-recovery-plan"
description: "Runs a bulk field update on Dynamics 365 F&SCM disaster recovery plan records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then applies changes and emits"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_a_disaster_recovery_plan", "rar_sha256": "f70192c02a30695d31eaa9854642bb82318f9520e6626c71c74e356cc862a9ed", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_a_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_a_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Develop a disaster recovery plan Bulk Field Update — Runs a bulk field update on Dynamics 365 F&SCM disaster recovery plan records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then applies changes and emits

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-a-disaster-recovery-plan
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
      "description": "Explicit approval to commit after reviewing the dry-run preview.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF, sandbox first).",
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
      "description": "List of record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_a_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 f70192c02a30695d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_a_disaster_recovery_plan_agent.py` first:

```bash
python3 bulk_update_develop_a_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_a_disaster_recovery_plan_agent.py   # or on stdin
python3 bulk_update_develop_a_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop a disaster recovery plan Bulk Field Update — Runs a bulk field update on Dynamics 365 F&SCM disaster recovery plan records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then applies changes and emits

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-a-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_a_disaster_recovery_plan',
    "version": '3.0.3',
    "display_name": 'Develop a disaster recovery plan Bulk Field Update',
    "description": 'Runs a bulk field update on Dynamics 365 F&SCM disaster recovery plan records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then applies changes and emits',
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
        "upstream_slug": 'bulk-update-develop-a-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-a-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '913d0fb73f08b65b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/develop-a-disaster-recovery-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-develop-a-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval to commit after reviewing the dry-run preview.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF, sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when develop a disaster recovery plan records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to develop a disaster recovery plan records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk field update on Dynamics 365 F&SCM disaster recovery plan records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then applies changes and emits', 'example_request': 'Bulk-update these disaster recovery plan record IDs in USMF sandbox with the new values — show me a dry run first.', 'inputs': [{'description': 'List of record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (e.g. USMF, sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit approval to commit after reviewing the dry-run preview.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-update field values on a supplied list of D365 ERP disaster recovery plan records in a sandbox legal entity, with preview and approval first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDevelopADisasterRecoveryPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopADisasterRecoveryPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval to commit after reviewing the dry-run preview.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF, sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDevelopADisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
