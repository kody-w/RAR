---
name: "rar-cowork-cookbook-report-configure-monitor-and-send-emails"
description: "Builds a read-only Excel summary report of configure/monitor/send emails activity from Dynamics 365 F&SCM for a legal entity and posted period, with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_monitor_and_send_emails", "rar_sha256": "74ee9d0631afc72e3bfad0dfb403c7d893255223b5a34580e0d726cceb59202f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_configure_monitor_and_send_emails`. The original RAPP
agent is preserved byte-for-byte in `report_configure_monitor_and_send_emails_agent.py` and in the RCI capsule.

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

Configure, monitor, and send emails Summary Report — Builds a read-only Excel summary report of configure/monitor/send emails activity from Dynamics 365 F&SCM for a legal entity and posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-monitor-and-send-emails
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
      "description": "Dimensions for breakdowns where applicable: department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-configure-monitor-and-send-emails-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_monitor_and_send_emails_agent.py` and embedded as the fenced Python below (sha256 74ee9d0631afc72e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_monitor_and_send_emails_agent.py` first:

```bash
python3 report_configure_monitor_and_send_emails_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_configure_monitor_and_send_emails_agent.py   # or on stdin
python3 report_configure_monitor_and_send_emails_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure, monitor, and send emails Summary Report — Builds a read-only Excel summary report of configure/monitor/send emails activity from Dynamics 365 F&SCM for a legal entity and posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-monitor-and-send-emails
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_configure_monitor_and_send_emails',
    "version": '3.0.3',
    "display_name": 'Configure, monitor, and send emails Summary Report',
    "description": 'Builds a read-only Excel summary report of configure/monitor/send emails activity from Dynamics 365 F&SCM for a legal entity and posted period, with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-configure-monitor-and-send-emails',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-configure-monitor-and-send-emails',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1bea211fcda46e33',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-monitor-and-send-emails'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-configure-monitor-and-send-emails', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-configure-monitor-and-send-emails-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where configure, monitor, and send emails stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of configure, monitor, and send emails for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-configure-monitor-and-send-emails-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure, monitor, and send emails records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only Excel summary report of configure/monitor/send emails activity from Dynamics 365 F&SCM for a legal entity and posted period, with Summary, Detail, and Top10 sheets.', 'example_request': "Build the configure/monitor/send emails summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-configure-monitor-and-send-emails-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of email configuration/monitoring/sending activity from D365 ERP data, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportConfigureMonitorAndSendEmails(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConfigureMonitorAndSendEmails'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-configure-monitor-and-send-emails-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportConfigureMonitorAndSendEmails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
