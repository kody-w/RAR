---
name: "rar-cowork-cookbook-report-identify-business-continuity-risks"
description: "Builds a read-only business continuity risk summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_business_continuity_risks", "rar_sha256": "e53f9a3815b231ea187fe3d0f88be3c57ef01894fb154f32ad72571619e26202", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_identify_business_continuity_risks`. The original RAPP
agent is preserved byte-for-byte in `report_identify_business_continuity_risks_agent.py` and in the RCI capsule.

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

Identify business continuity risks Summary Report — Builds a read-only business continuity risk summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-business-continuity-risks
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
      "description": "D365 legal entity to report against (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-identify-business-continuity-risks-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_business_continuity_risks_agent.py` and embedded as the fenced Python below (sha256 e53f9a3815b231ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_business_continuity_risks_agent.py` first:

```bash
python3 report_identify_business_continuity_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_identify_business_continuity_risks_agent.py   # or on stdin
python3 report_identify_business_continuity_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify business continuity risks Summary Report — Builds a read-only business continuity risk summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-business-continuity-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_identify_business_continuity_risks',
    "version": '3.0.3',
    "display_name": 'Identify business continuity risks Summary Report',
    "description": 'Builds a read-only business continuity risk summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-identify-business-continuity-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-identify-business-continuity-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '093a6677d22d8f33',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/identify-business-continuity-risks'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-identify-business-continuity-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-identify-business-continuity-risks-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where identify business continuity risks stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of identify business continuity risks for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-identify-business-continuity-risks-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify business continuity risks records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only business continuity risk summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build me a business continuity risk summary report for USMF from D365 as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-identify-business-continuity-risks-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-data-modification summary report of business continuity risks from D365 ERP with totals, dimension breakdowns, and a Top 10 by value.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportIdentifyBusinessContinuityRisks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIdentifyBusinessContinuityRisks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-identify-business-continuity-risks-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportIdentifyBusinessContinuityRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
