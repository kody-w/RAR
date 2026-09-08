---
name: "rar-cowork-cookbook-bulk-update-monitor-financial-ratios-and-metrics"
description: "Applies a bulk field update to financial ratio/metric records in Dynamics 365 F&SCM (legal entity USMF, sandbox) \u2014 returns a dry-run preview workbook of before/after/status, then a confirmation workbook after approval."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_financial_ratios_and_metrics", "rar_sha256": "b5dcb164ee773f5db61f877e5bccffde772b63320387e234946a6a13a7517f7c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_monitor_financial_ratios_and_metrics`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_monitor_financial_ratios_and_metrics_agent.py` and in the RCI capsule.

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

Monitor financial ratios and metrics Bulk Field Update — Applies a bulk field update to financial ratio/metric records in Dynamics 365 F&SCM (legal entity USMF, sandbox) — returns a dry-run preview workbook of before/after/status, then a confirmation workbook after approval.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-financial-ratios-and-metrics
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
      "description": "Explicit user approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to those records.",
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
      "description": "List of record IDs of the financial ratio/metric records to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_financial_ratios_and_metrics_agent.py` and embedded as the fenced Python below (sha256 b5dcb164ee773f5d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_financial_ratios_and_metrics_agent.py` first:

```bash
python3 bulk_update_monitor_financial_ratios_and_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_financial_ratios_and_metrics_agent.py   # or on stdin
python3 bulk_update_monitor_financial_ratios_and_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor financial ratios and metrics Bulk Field Update — Applies a bulk field update to financial ratio/metric records in Dynamics 365 F&SCM (legal entity USMF, sandbox) — returns a dry-run preview workbook of before/after/status, then a confirmation workbook after approval.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-financial-ratios-and-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_financial_ratios_and_metrics',
    "version": '3.0.3',
    "display_name": 'Monitor financial ratios and metrics Bulk Field Update',
    "description": 'Applies a bulk field update to financial ratio/metric records in Dynamics 365 F&SCM (legal entity USMF, sandbox) — returns a dry-run preview workbook of before/after/status, then a confirmation workbook after approval.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-monitor-financial-ratios-and-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-financial-ratios-and-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e7bbf6bdb19f2ef5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-financial-ratios-and-metrics'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-monitor-financial-ratios-and-metrics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of record IDs of the financial ratio/metric records to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when monitor financial ratios and metrics records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to monitor financial ratios and metrics records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to financial ratio/metric records in Dynamics 365 F&SCM (legal entity USMF, sandbox) — returns a dry-run preview workbook of before/after/status, then a confirmation workbook after approval.', 'example_request': 'Bulk update these financial metric records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of record IDs of the financial ratio/metric records to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-update a list of D365 financial ratio/metric records in a sandbox with a dry-run preview and explicit approval before commit.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateMonitorFinancialRatiosAndMetrics(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorFinancialRatiosAndMetrics'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs of the financial ratio/metric records to update.', 'type': 'string'}},
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
    print(BulkUpdateMonitorFinancialRatiosAndMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
