---
name: "rar-cowork-cookbook-bulk-update-analyze-supply-purchase-plan"
description: "Applies a bulk field update to analyze supply purchase plan records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, then a confirmation workbook afte"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_supply_purchase_plan", "rar_sha256": "c93636041e418885717d71954ab341e798053386bcca6fb255c0a7be369a6c95", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
