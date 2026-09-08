---
name: "rar-cowork-cookbook-bulk-update-analyze-supply-purchase-plan"
description: "Applies a bulk field update to analyze supply purchase plan records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, then a confirmation workbook afte"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_supply_purchase_plan", "rar_sha256": "c93636041e418885717d71954ab341e798053386bcca6fb255c0a7be369a6c95", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_supply_purchase_plan`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_supply_purchase_plan_agent.py` and in the RCI capsule.

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

Analyze supply purchase plan Bulk Field Update — Applies a bulk field update to analyze supply purchase plan records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, then a confirmation workbook afte

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-supply-purchase-plan
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
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of analyze supply purchase plan record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_supply_purchase_plan_agent.py` and embedded as the fenced Python below (sha256 c93636041e418885…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_supply_purchase_plan_agent.py` first:

```bash
python3 bulk_update_analyze_supply_purchase_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_supply_purchase_plan_agent.py   # or on stdin
python3 bulk_update_analyze_supply_purchase_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze supply purchase plan Bulk Field Update — Applies a bulk field update to analyze supply purchase plan records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, then a confirmation workbook afte

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-supply-purchase-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_supply_purchase_plan',
    "version": '3.0.3',
    "display_name": 'Analyze supply purchase plan Bulk Field Update',
    "description": 'Applies a bulk field update to analyze supply purchase plan records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, then a confirmation workbook afte',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-supply-purchase-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-supply-purchase-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ece501df797ffb38',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/analyze-supply-purchase-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-analyze-supply-purchase-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of analyze supply purchase plan record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when analyze supply purchase plan records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to analyze supply purchase plan records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to analyze supply purchase plan records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, then a confirmation workbook afte', 'example_request': 'Bulk update these purchase plan record IDs in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of analyze supply purchase plan record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to change a field on many analyze supply purchase plan records at once in a D365 sandbox and want a before/after preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAnalyzeSupplyPurchasePlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeSupplyPurchasePlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of analyze supply purchase plan record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAnalyzeSupplyPurchasePlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
