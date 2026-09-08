---
name: "rar-cowork-cookbook-bulk-update-report-on-and-analyze-trends"
description: "Applies a bulk field update to Dynamics 365 F&SCM records in a given legal entity via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_report_on_and_analyze_trends", "rar_sha256": "7044ecf86b4117a9736ec163c6ddb833a463c484bed0567040313fc4f92312d6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_report_on_and_analyze_trends`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_report_on_and_analyze_trends_agent.py` and in the RCI capsule.

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

Report on and analyze trends Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM records in a given legal entity via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-report-on-and-analyze-trends
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; sandbox environment only.",
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
      "description": "List of record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_report_on_and_analyze_trends_agent.py` and embedded as the fenced Python below (sha256 7044ecf86b4117a9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_report_on_and_analyze_trends_agent.py` first:

```bash
python3 bulk_update_report_on_and_analyze_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_report_on_and_analyze_trends_agent.py   # or on stdin
python3 bulk_update_report_on_and_analyze_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on and analyze trends Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM records in a given legal entity via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-report-on-and-analyze-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_report_on_and_analyze_trends',
    "version": '3.0.3',
    "display_name": 'Report on and analyze trends Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM records in a given legal entity via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-report-on-and-analyze-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-report-on-and-analyze-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e4ad05eecfe690a7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/report-on-and-analyze-trends'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-report-on-and-analyze-trends', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when report on and analyze trends records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to report on and analyze trends records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM records in a given legal entity via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.', 'example_request': 'Bulk update these D365 record IDs in USMF sandbox to the new value — show me a dry-run preview first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'name': 'legal_entity'}, {'description': 'List of record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs to change the same field(s) across a known list of D365 ERP record IDs and wants a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateReportOnAndAnalyzeTrends(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReportOnAndAnalyzeTrends'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateReportOnAndAnalyzeTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
