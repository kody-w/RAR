---
name: "rar-cowork-cookbook-ppt-exec-report-production-quality-non-conformance"
description: "Builds a read-only executive PowerPoint deck on production quality non-conformance from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_report_production_quality_non_conformance", "rar_sha256": "07fcf209afd1e6e07e82b619716f658f25a33dabfb7e4f761e94922bc856a320", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_report_production_quality_non_conformance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_report_production_quality_non_conformance_agent.py` and in the RCI capsule.

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

Report production quality non-conformance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on production quality non-conformance from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-report-production-quality-non-conformance
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
      "description": "D365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-report-production-quality-non-conformance-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for trend comparison, e.g. month ending 2026-05-24.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_report_production_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 07fcf209afd1e6e0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_report_production_quality_non_conformance_agent.py` first:

```bash
python3 ppt_exec_report_production_quality_non_conformance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_report_production_quality_non_conformance_agent.py   # or on stdin
python3 ppt_exec_report_production_quality_non_conformance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production quality non-conformance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on production quality non-conformance from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-report-production-quality-non-conformance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_report_production_quality_non_conformance',
    "version": '3.0.3',
    "display_name": 'Report production quality non-conformance Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on production quality non-conformance from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-report-production-quality-non-conformance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-report-production-quality-non-conformance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd42c638df24ca7c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/report-production-quality-non-conformance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-report-production-quality-non-conformance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-report-production-quality-non-conformance-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period for trend comparison, e.g. month ending 2026-05-24.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for report production quality non-conformance reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on report production quality non-conformance for a 15-minute monthly review. Produce 'ppt-exec-report-production-quality-non-conformance-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads report production quality non-conformance data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on production quality non-conformance from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': "Build the exec deck on production quality non-conformance for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period and prior period for trend comparison, e.g. month ending 2026-05-24.', 'name': 'review_period'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-report-production-quality-non-conformance-2026-05-24.pptx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on production quality non-conformance status from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecReportProductionQualityNonConformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecReportProductionQualityNonConformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-report-production-quality-non-conformance-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for trend comparison, e.g. month ending 2026-05-24.', 'type': 'string'}},
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
    print(PptExecReportProductionQualityNonConformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
