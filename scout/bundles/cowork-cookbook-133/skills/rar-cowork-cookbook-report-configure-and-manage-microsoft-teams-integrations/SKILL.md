---
name: "rar-cowork-cookbook-report-configure-and-manage-microsoft-teams-integrations"
description: "Builds a read-only summary report of configure and manage Microsoft Teams integrations activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_microsoft_teams_integrations", "rar_sha256": "b074f2f01b66431ea3422045ec607be1aee3a3c5806507470dccae9897d0559f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_configure_and_manage_microsoft_teams_integrations`. The original RAPP
agent is preserved byte-for-byte in `report_configure_and_manage_microsoft_teams_integrations_agent.py` and in the RCI capsule.

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

Configure and manage Microsoft Teams integrations Summary Report — Builds a read-only summary report of configure and manage Microsoft Teams integrations activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary,

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
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-microsoft-teams-integrations
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
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-configure-and-manage-microsoft-teams-integrations-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_and_manage_microsoft_teams_integrations_agent.py` and embedded as the fenced Python below (sha256 b074f2f01b66431e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_and_manage_microsoft_teams_integrations_agent.py` first:

```bash
python3 report_configure_and_manage_microsoft_teams_integrations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_configure_and_manage_microsoft_teams_integrations_agent.py   # or on stdin
python3 report_configure_and_manage_microsoft_teams_integrations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage Microsoft Teams integrations Summary Report — Builds a read-only summary report of configure and manage Microsoft Teams integrations activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary,

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
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-microsoft-teams-integrations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_configure_and_manage_microsoft_teams_integrations',
    "version": '3.0.3',
    "display_name": 'Configure and manage Microsoft Teams integrations Summary Report',
    "description": 'Builds a read-only summary report of configure and manage Microsoft Teams integrations activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary,',
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
        "upstream_slug": 'report-configure-and-manage-microsoft-teams-integrations',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-configure-and-manage-microsoft-teams-integrations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f99503372a5dc913',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-microsoft-teams-integrations'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-configure-and-manage-microsoft-teams-integrations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-configure-and-manage-microsoft-teams-integrations-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where configure and manage Microsoft Teams integrations stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of configure and manage Microsoft Teams integrations for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-configure-and-manage-microsoft-teams-integrations-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage Microsoft Teams integrations records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of configure and manage Microsoft Teams integrations activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary,', 'example_request': 'Build a USMF summary report of Teams integrations activity for the latest posted period, with Summary, Detail, and Top10 sheets.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-configure-and-manage-microsoft-teams-integrations-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals, by-dimension breakdown, and Top 10 by value report of Teams integration activity from D365 ERP, with no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportConfigureAndManageMicrosoftTeamsIntegrations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConfigureAndManageMicrosoftTeamsIntegrations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-configure-and-manage-microsoft-teams-integrations-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportConfigureAndManageMicrosoftTeamsIntegrations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
