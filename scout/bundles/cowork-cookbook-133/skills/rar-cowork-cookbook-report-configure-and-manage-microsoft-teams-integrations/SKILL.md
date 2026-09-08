---
name: "rar-cowork-cookbook-report-configure-and-manage-microsoft-teams-integrations"
description: "Builds a read-only summary report of configure and manage Microsoft Teams integrations activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_microsoft_teams_integrations", "rar_sha256": "b074f2f01b66431ea3422045ec607be1aee3a3c5806507470dccae9897d0559f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
