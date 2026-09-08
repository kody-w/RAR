---
name: "rar-cowork-cookbook-ppt-exec-prepare-statutory-financial-reports"
description: "Builds a read-only executive PowerPoint deck on statutory financial report preparation status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_prepare_statutory_financial_reports", "rar_sha256": "f22f1292e95b92d5e5cf3e7deae7ac3dab2f9f8c5ff31e69bacea47a85ab2349", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
