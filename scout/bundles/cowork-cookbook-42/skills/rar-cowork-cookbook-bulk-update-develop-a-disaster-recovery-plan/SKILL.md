---
name: "rar-cowork-cookbook-bulk-update-develop-a-disaster-recovery-plan"
description: "Runs a bulk field update on Dynamics 365 F&SCM disaster recovery plan records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then applies changes and emits"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_a_disaster_recovery_plan", "rar_sha256": "f70192c02a30695d31eaa9854642bb82318f9520e6626c71c74e356cc862a9ed", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
