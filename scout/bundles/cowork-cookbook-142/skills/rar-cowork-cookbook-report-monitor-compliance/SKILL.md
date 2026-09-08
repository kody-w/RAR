---
name: "rar-cowork-cookbook-report-monitor-compliance"
description: "Builds a read-only monitor compliance summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_compliance", "rar_sha256": "39695986bd3ad92029305898e34b6045c5aea7091218a1838876dd24edecade8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_monitor_compliance`. The original RAPP
agent is preserved byte-for-byte in `report_monitor_compliance_agent.py` and in the RCI capsule.

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

Monitor compliance Summary Report — Builds a read-only monitor compliance summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-compliance
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
      "description": "D365 legal entity to report against (default USMF).",
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
      "description": "Excel workbook name, e.g. report-monitor-compliance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_compliance_agent.py` and embedded as the fenced Python below (sha256 39695986bd3ad920…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_compliance_agent.py` first:

```bash
python3 report_monitor_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_monitor_compliance_agent.py   # or on stdin
python3 report_monitor_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor compliance Summary Report — Builds a read-only monitor compliance summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_monitor_compliance',
    "version": '3.0.3',
    "display_name": 'Monitor compliance Summary Report',
    "description": 'Builds a read-only monitor compliance summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-monitor-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-monitor-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37a1a2ed511591ac',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/monitor-compliance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-monitor-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against (default USMF).', 'output_filename': 'Excel workbook name, e.g. report-monitor-compliance-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where monitor compliance stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of monitor compliance for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-monitor-compliance-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor compliance records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only monitor compliance summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a monitor compliance summary report for USMF with breakdowns and a Top 10 by value, as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against (default USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-monitor-compliance-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a monitor compliance summary from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportMonitorCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMonitorCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-monitor-compliance-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportMonitorCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
