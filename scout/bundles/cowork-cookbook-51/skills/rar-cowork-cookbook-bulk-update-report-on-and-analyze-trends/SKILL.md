---
name: "rar-cowork-cookbook-bulk-update-report-on-and-analyze-trends"
description: "Applies a bulk field update to Dynamics 365 F&SCM records in a given legal entity via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_report_on_and_analyze_trends", "rar_sha256": "7044ecf86b4117a9736ec163c6ddb833a463c484bed0567040313fc4f92312d6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
