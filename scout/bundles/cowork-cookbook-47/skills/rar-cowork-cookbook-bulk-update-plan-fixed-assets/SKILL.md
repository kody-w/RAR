---
name: "rar-cowork-cookbook-bulk-update-plan-fixed-assets"
description: "Applies a bulk field update to plan fixed assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval befo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_fixed_assets", "rar_sha256": "7da087fbd4e4b605997c276e489b8b3a4a3ece735c0ba3e2effa537780e5d279", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_fixed_assets_agent.py` and in the RCI capsule.

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

Plan fixed assets Bulk Field Update — Applies a bulk field update to plan fixed assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval befo

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-fixed-assets
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
      "description": "Explicit confirmation after reviewing the dry-run preview workbook, before changes are committed.",
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
      "description": "List of plan fixed assets record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 7da087fbd4e4b605…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_fixed_assets_agent.py` first:

```bash
python3 bulk_update_plan_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_fixed_assets_agent.py   # or on stdin
python3 bulk_update_plan_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan fixed assets Bulk Field Update — Applies a bulk field update to plan fixed assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval befo

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_fixed_assets',
    "version": '3.0.3',
    "display_name": 'Plan fixed assets Bulk Field Update',
    "description": 'Applies a bulk field update to plan fixed assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval befo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fc7dfd57e78bdde6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-fixed-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-plan-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of plan fixed assets record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when plan fixed assets records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to plan fixed assets records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to plan fixed assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval befo', 'example_request': 'Bulk update these plan fixed assets records in USMF sandbox with the new values below — show me a dry-run preview first.', 'inputs': [{'description': 'List of plan fixed assets record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit confirmation after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change one or more fields on many plan fixed assets records at once and want a before/after preview and approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePlanFixedAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of plan fixed assets record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePlanFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
