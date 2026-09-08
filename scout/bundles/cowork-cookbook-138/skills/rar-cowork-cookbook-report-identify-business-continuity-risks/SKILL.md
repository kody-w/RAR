---
name: "rar-cowork-cookbook-report-identify-business-continuity-risks"
description: "Builds a read-only business continuity risk summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_business_continuity_risks", "rar_sha256": "e53f9a3815b231ea187fe3d0f88be3c57ef01894fb154f32ad72571619e26202", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
