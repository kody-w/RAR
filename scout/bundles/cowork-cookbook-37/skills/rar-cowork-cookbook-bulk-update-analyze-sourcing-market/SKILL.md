---
name: "rar-cowork-cookbook-bulk-update-analyze-sourcing-market"
description: "Applies a bulk field update to Dynamics 365 F&SCM sourcing-market records via the ERP plugin: builds a dry-run preview workbook (before/after/status), waits for approval, then commits and emits a confirmation workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_sourcing_market", "rar_sha256": "6437b3493d4199f62820dc3be1ad8de65c5f5a0ea2af5cf6f1e8701aacc5edca", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
