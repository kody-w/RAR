---
name: "rar-cowork-cookbook-bulk-update-implement-a-business-continuity-plan"
description: "Runs a bulk field update on business continuity plan records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies and confirms."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_implement_a_business_continuity_plan", "rar_sha256": "e2e826a5b60b45e682fe2e81a541f6c34a5b425ce7aa97ddb1eaf9f2894643b0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_implement_a_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_implement_a_business_continuity_plan_agent.py` and in the RCI capsule.

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

Implement a business continuity plan Bulk Field Update — Runs a bulk field update on business continuity plan records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies and confirms.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-implement-a-business-continuity-plan
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
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF (sandbox first).",
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
      "description": "List of record IDs for the business continuity plan records to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_implement_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 e2e826a5b60b45e6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_implement_a_business_continuity_plan_agent.py` first:

```bash
python3 bulk_update_implement_a_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_implement_a_business_continuity_plan_agent.py   # or on stdin
python3 bulk_update_implement_a_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement a business continuity plan Bulk Field Update — Runs a bulk field update on business continuity plan records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies and confirms.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-implement-a-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_implement_a_business_continuity_plan',
    "version": '3.0.3',
    "display_name": 'Implement a business continuity plan Bulk Field Update',
    "description": 'Runs a bulk field update on business continuity plan records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies and confirms.',
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
        "upstream_slug": 'bulk-update-implement-a-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-implement-a-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c04668f4a4f2700',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/implement-a-business-continuity-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-implement-a-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of record IDs for the business continuity plan records to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when implement a business continuity plan records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to implement a business continuity plan records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk field update on business continuity plan records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies and confirms.', 'example_request': 'Bulk update these business continuity plan records in USMF sandbox to the new owner — show me a dry run first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'name': 'legal_entity'}, {'description': 'List of record IDs for the business continuity plan records to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of D365 record IDs in a sandbox legal entity, with a preview and approval step first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateImplementABusinessContinuityPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateImplementABusinessContinuityPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs for the business continuity plan records to update.', 'type': 'string'}},
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
    print(BulkUpdateImplementABusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
