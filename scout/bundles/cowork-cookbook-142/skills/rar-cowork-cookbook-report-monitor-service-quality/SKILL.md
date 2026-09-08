---
name: "rar-cowork-cookbook-report-monitor-service-quality"
description: "Builds a read-only monitor service quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_service_quality", "rar_sha256": "8be8883e0db48a40c56d852d710e45ac4ceda3b1085b76cf4ebb4bf9732bd43b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_monitor_service_quality`. The original RAPP
agent is preserved byte-for-byte in `report_monitor_service_quality_agent.py` and in the RCI capsule.

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

Monitor service quality Summary Report — Builds a read-only monitor service quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-service-quality
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
    "breakdown_dimensions": {
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
    "output_filename": {
      "description": "Excel workbook name, e.g. report-monitor-service-quality-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_service_quality_agent.py` and embedded as the fenced Python below (sha256 8be8883e0db48a40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_service_quality_agent.py` first:

```bash
python3 report_monitor_service_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_monitor_service_quality_agent.py   # or on stdin
python3 report_monitor_service_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service quality Summary Report — Builds a read-only monitor service quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-service-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_monitor_service_quality',
    "version": '3.0.3',
    "display_name": 'Monitor service quality Summary Report',
    "description": 'Builds a read-only monitor service quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-monitor-service-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-monitor-service-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc7936a3e2df954a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/monitor-service-quality'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-monitor-service-quality', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-monitor-service-quality-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where monitor service quality stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of monitor service quality for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-monitor-service-quality-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor service quality records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only monitor service quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a monitor service quality summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-monitor-service-quality-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary of monitor service quality activity with totals, by-dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportMonitorServiceQuality(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMonitorServiceQuality'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-monitor-service-quality-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportMonitorServiceQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
