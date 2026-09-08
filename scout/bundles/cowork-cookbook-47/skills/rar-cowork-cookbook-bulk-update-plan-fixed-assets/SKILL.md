---
name: "rar-cowork-cookbook-bulk-update-plan-fixed-assets"
description: "Applies a bulk field update to plan fixed assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval befo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_fixed_assets", "rar_sha256": "7da087fbd4e4b605997c276e489b8b3a4a3ece735c0ba3e2effa537780e5d279", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
