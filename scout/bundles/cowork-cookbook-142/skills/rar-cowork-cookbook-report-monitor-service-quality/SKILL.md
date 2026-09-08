---
name: "rar-cowork-cookbook-report-monitor-service-quality"
description: "Builds a read-only monitor service quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_service_quality", "rar_sha256": "8be8883e0db48a40c56d852d710e45ac4ceda3b1085b76cf4ebb4bf9732bd43b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
