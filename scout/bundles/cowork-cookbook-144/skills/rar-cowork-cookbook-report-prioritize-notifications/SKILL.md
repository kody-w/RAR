---
name: "rar-cowork-cookbook-report-prioritize-notifications"
description: "Builds a read-only summary report of prioritize notifications activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_prioritize_notifications", "rar_sha256": "92ee64a0eb69e23fdc633d3efcf9e996d881373822eb0d6ef6b5be585957c0ed", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
