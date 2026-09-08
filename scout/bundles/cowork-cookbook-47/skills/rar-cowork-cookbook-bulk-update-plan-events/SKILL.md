---
name: "rar-cowork-cookbook-bulk-update-plan-events"
description: "Applies a bulk field update to plan events records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_events", "rar_sha256": "aeb3509802e19d067bd3be0e036ad94b97e2b8e0b4a55a9524a36e4158f62cca", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
