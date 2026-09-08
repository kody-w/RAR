---
name: "rar-cowork-cookbook-bulk-update-plan-events"
description: "Applies a bulk field update to plan events records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_events", "rar_sha256": "aeb3509802e19d067bd3be0e036ad94b97e2b8e0b4a55a9524a36e4158f62cca", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_events`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_events_agent.py` and in the RCI capsule.

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

Plan events Bulk Field Update — Applies a bulk field update to plan events records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-events
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are applied.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; USMF sandbox.",
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
      "description": "List of plan events record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_events_agent.py` and embedded as the fenced Python below (sha256 aeb3509802e19d06…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_events_agent.py` first:

```bash
python3 bulk_update_plan_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_events_agent.py   # or on stdin
python3 bulk_update_plan_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan events Bulk Field Update — Applies a bulk field update to plan events records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_events',
    "version": '3.0.3',
    "display_name": 'Plan events Bulk Field Update',
    "description": 'Applies a bulk field update to plan events records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation workbook.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eb9405949daaf041',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/plan-events'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-plan-events', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of plan events record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when plan events records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to plan events records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to plan events records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation workbook.', 'example_request': 'Bulk update these plan events record IDs in USMF sandbox to the new value - show me a dry-run preview first.', 'inputs': [{'description': 'List of plan events record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to update a field on many plan events records at once and want a before/after dry-run preview to approve before the write is committed.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePlanEvents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanEvents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of plan events record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePlanEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
