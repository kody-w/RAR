---
name: "rar-cowork-cookbook-ppt-exec-prepare-statutory-financial-reports"
description: "Builds a read-only executive PowerPoint deck on statutory financial report preparation status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_prepare_statutory_financial_reports", "rar_sha256": "f22f1292e95b92d5e5cf3e7deae7ac3dab2f9f8c5ff31e69bacea47a85ab2349", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_prepare_statutory_financial_reports`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_prepare_statutory_financial_reports_agent.py` and in the RCI capsule.

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

Prepare statutory financial reports Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on statutory financial report preparation status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-prepare-statutory-financial-reports
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-prepare-statutory-financial-reports-2026-05-24.pptx.",
      "type": "string"
    },
    "reporting_period": {
      "description": "The month or period under review and the prior period used for trend comparison.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_prepare_statutory_financial_reports_agent.py` and embedded as the fenced Python below (sha256 f22f1292e95b92d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_prepare_statutory_financial_reports_agent.py` first:

```bash
python3 ppt_exec_prepare_statutory_financial_reports_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_prepare_statutory_financial_reports_agent.py   # or on stdin
python3 ppt_exec_prepare_statutory_financial_reports_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare statutory financial reports Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on statutory financial report preparation status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-prepare-statutory-financial-reports
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_prepare_statutory_financial_reports',
    "version": '3.0.3',
    "display_name": 'Prepare statutory financial reports Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on statutory financial report preparation status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-prepare-statutory-financial-reports',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-prepare-statutory-financial-reports',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eebb3edc25a64396',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/prepare-statutory-financial-reports'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-prepare-statutory-financial-reports', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-prepare-statutory-financial-reports-2026-05-24.pptx.', 'reporting_period': 'The month or period under review and the prior period used for trend comparison.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for prepare statutory financial reports reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on prepare statutory financial reports for a 15-minute monthly review. Produce 'ppt-exec-prepare-statutory-financial-reports-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads prepare statutory financial reports data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on statutory financial report preparation status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on statutory financial report prep for USMF for the May monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The month or period under review and the prior period used for trend comparison.', 'name': 'reporting_period'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-prepare-statutory-financial-reports-2026-05-24.pptx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on statutory financial reporting status pulled from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPrepareStatutoryFinancialReports(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPrepareStatutoryFinancialReports'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-prepare-statutory-financial-reports-2026-05-24.pptx.', 'type': 'string'}, 'reporting_period': {'description': 'The month or period under review and the prior period used for trend comparison.', 'type': 'string'}},
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
    print(PptExecPrepareStatutoryFinancialReports().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
