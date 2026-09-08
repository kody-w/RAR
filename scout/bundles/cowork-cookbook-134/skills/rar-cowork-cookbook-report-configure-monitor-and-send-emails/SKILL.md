---
name: "rar-cowork-cookbook-report-configure-monitor-and-send-emails"
description: "Builds a read-only Excel summary report of configure/monitor/send emails activity from Dynamics 365 F&SCM for a legal entity and posted period, with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_monitor_and_send_emails", "rar_sha256": "74ee9d0631afc72e3bfad0dfb403c7d893255223b5a34580e0d726cceb59202f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
