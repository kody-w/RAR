---
name: "rar-cowork-cookbook-bulk-update-analyze-sourcing-market"
description: "Applies a bulk field update to Dynamics 365 F&SCM sourcing-market records via the ERP plugin: builds a dry-run preview workbook (before/after/status), waits for approval, then commits and emits a confirmation workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_sourcing_market", "rar_sha256": "6437b3493d4199f62820dc3be1ad8de65c5f5a0ea2af5cf6f1e8701aacc5edca", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_sourcing_market`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_sourcing_market_agent.py` and in the RCI capsule.

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

Analyze sourcing market Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM sourcing-market records via the ERP plugin: builds a dry-run preview workbook (before/after/status), waits for approval, then commits and emits a confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-sourcing-market
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
    "environment": {
      "description": "Target environment; use sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF.",
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
      "description": "List of the sourcing-market record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_sourcing_market_agent.py` and embedded as the fenced Python below (sha256 6437b3493d4199f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_sourcing_market_agent.py` first:

```bash
python3 bulk_update_analyze_sourcing_market_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_sourcing_market_agent.py   # or on stdin
python3 bulk_update_analyze_sourcing_market_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing market Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM sourcing-market records via the ERP plugin: builds a dry-run preview workbook (before/after/status), waits for approval, then commits and emits a confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-sourcing-market
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_sourcing_market',
    "version": '3.0.3',
    "display_name": 'Analyze sourcing market Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM sourcing-market records via the ERP plugin: builds a dry-run preview workbook (before/after/status), waits for approval, then commits and emits a confirmation workbook.',
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
        "upstream_slug": 'bulk-update-analyze-sourcing-market',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-sourcing-market',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a850b533cdfed226',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/analyze-sourcing-market'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-analyze-sourcing-market', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; use sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of the sourcing-market record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when analyze sourcing market records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to analyze sourcing market records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM sourcing-market records via the ERP plugin: builds a dry-run preview workbook (before/after/status), waits for approval, then commits and emits a confirmation workbook.', 'example_request': 'Bulk-update these sourcing market record IDs in USMF sandbox to the new value — show me a dry run first.', 'inputs': [{'description': 'List of the sourcing-market record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; use sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many D365 sourcing-market records at once and want a dry-run preview and approval step before the write. Sandbox only.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAnalyzeSourcingMarket(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeSourcingMarket'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; use sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of the sourcing-market record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAnalyzeSourcingMarket().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
