---
name: "rar-cowork-cookbook-report-prioritize-notifications"
description: "Builds a read-only summary report of prioritize notifications activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_prioritize_notifications", "rar_sha256": "92ee64a0eb69e23fdc633d3efcf9e996d881373822eb0d6ef6b5be585957c0ed", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_prioritize_notifications`. The original RAPP
agent is preserved byte-for-byte in `report_prioritize_notifications_agent.py` and in the RCI capsule.

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

Prioritize notifications Summary Report — Builds a read-only summary report of prioritize notifications activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-prioritize-notifications
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-prioritize-notifications-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_prioritize_notifications_agent.py` and embedded as the fenced Python below (sha256 92ee64a0eb69e23f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_prioritize_notifications_agent.py` first:

```bash
python3 report_prioritize_notifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_prioritize_notifications_agent.py   # or on stdin
python3 report_prioritize_notifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prioritize notifications Summary Report — Builds a read-only summary report of prioritize notifications activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-prioritize-notifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_prioritize_notifications',
    "version": '3.0.3',
    "display_name": 'Prioritize notifications Summary Report',
    "description": 'Builds a read-only summary report of prioritize notifications activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-prioritize-notifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-prioritize-notifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '82ae98863cdd7ae5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/prioritize-notifications'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-prioritize-notifications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-prioritize-notifications-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where prioritize notifications stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of prioritize notifications for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-prioritize-notifications-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads prioritize notifications records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of prioritize notifications activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a prioritize notifications summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-prioritize-notifications-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of prioritize notifications activity in D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportPrioritizeNotifications(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPrioritizeNotifications'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-prioritize-notifications-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportPrioritizeNotifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
