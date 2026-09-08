---
name: "rar-cowork-cookbook-bulk-update-report-quality-test-results"
description: "Applies a bulk field update to report quality test results records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_report_quality_test_results", "rar_sha256": "b72ccd2522a2391b303136d9f7aa4a01bad7787020d7b6844a990cc9dd1c0149", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_report_quality_test_results`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_report_quality_test_results_agent.py` and in the RCI capsule.

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

Report quality test results Bulk Field Update — Applies a bulk field update to report quality test results records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-report-quality-test-results
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
      "description": "Explicit approval after reviewing the dry-run preview workbook.",
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
      "description": "List of report quality test results record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_report_quality_test_results_agent.py` and embedded as the fenced Python below (sha256 b72ccd2522a2391b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_report_quality_test_results_agent.py` first:

```bash
python3 bulk_update_report_quality_test_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_report_quality_test_results_agent.py   # or on stdin
python3 bulk_update_report_quality_test_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report quality test results Bulk Field Update — Applies a bulk field update to report quality test results records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-report-quality-test-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_report_quality_test_results',
    "version": '3.0.3',
    "display_name": 'Report quality test results Bulk Field Update',
    "description": 'Applies a bulk field update to report quality test results records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-report-quality-test-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-report-quality-test-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bd87ec6347711a41',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/report-quality-test-results'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-report-quality-test-results', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of report quality test results record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when report quality test results records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to report quality test results records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to report quality test results records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval', 'example_request': 'Bulk update these report quality test results records in USMF sandbox with the new values - show me a dry-run first.', 'inputs': [{'description': 'List of report quality test results record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many report quality test results records at once and want a before/after preview to approve before the write is applied.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateReportQualityTestResults(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReportQualityTestResults'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of report quality test results record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateReportQualityTestResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
