---
name: "rar-cowork-cookbook-report-develop-campaign-themes-and-messages"
description: "Builds a read-only summary report of develop campaign themes and messages activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_campaign_themes_and_messages", "rar_sha256": "0b984421b805237f302f2d42d71d2998ef16f76eb19ae17cb4490cee66c82877", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_campaign_themes_and_messages`. The original RAPP
agent is preserved byte-for-byte in `report_develop_campaign_themes_and_messages_agent.py` and in the RCI capsule.

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

Develop campaign themes and messages Summary Report — Builds a read-only summary report of develop campaign themes and messages activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-campaign-themes-and-messages
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner.",
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
      "description": "Excel workbook filename, e.g. report-develop-campaign-themes-and-messages-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_campaign_themes_and_messages_agent.py` and embedded as the fenced Python below (sha256 0b984421b805237f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_campaign_themes_and_messages_agent.py` first:

```bash
python3 report_develop_campaign_themes_and_messages_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_campaign_themes_and_messages_agent.py   # or on stdin
python3 report_develop_campaign_themes_and_messages_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop campaign themes and messages Summary Report — Builds a read-only summary report of develop campaign themes and messages activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-campaign-themes-and-messages
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_campaign_themes_and_messages',
    "version": '3.0.3',
    "display_name": 'Develop campaign themes and messages Summary Report',
    "description": 'Builds a read-only summary report of develop campaign themes and messages activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-campaign-themes-and-messages',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-campaign-themes-and-messages',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '11c7817c9b272270',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-campaign-themes-and-messages'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-develop-campaign-themes-and-messages', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-develop-campaign-themes-and-messages-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where develop campaign themes and messages stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of develop campaign themes and messages for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-develop-campaign-themes-and-messages-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop campaign themes and messages records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of develop campaign themes and messages activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a develop campaign themes and messages summary report for USMF for the latest posted period as an Excel file.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook filename, e.g. report-develop-campaign-themes-and-messages-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-data-modification Excel summary of develop campaign themes and messages activity with totals, breakdowns, and a Top 10 by value section.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDevelopCampaignThemesAndMessages(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopCampaignThemesAndMessages'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-develop-campaign-themes-and-messages-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDevelopCampaignThemesAndMessages().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
