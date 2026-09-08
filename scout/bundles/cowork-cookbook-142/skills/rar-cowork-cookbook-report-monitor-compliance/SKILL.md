---
name: "rar-cowork-cookbook-report-monitor-compliance"
description: "Builds a read-only monitor compliance summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_compliance", "rar_sha256": "39695986bd3ad92029305898e34b6045c5aea7091218a1838876dd24edecade8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
