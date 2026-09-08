---
name: "rar-cowork-cookbook-bulk-update-report-quality-test-results"
description: "Applies a bulk field update to report quality test results records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_report_quality_test_results", "rar_sha256": "b72ccd2522a2391b303136d9f7aa4a01bad7787020d7b6844a990cc9dd1c0149", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
