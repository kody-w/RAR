---
name: "rar-cowork-cookbook-ppt-exec-report-production-quality-non-conformance"
description: "Builds a read-only executive PowerPoint deck on production quality non-conformance from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_report_production_quality_non_conformance", "rar_sha256": "07fcf209afd1e6e07e82b619716f658f25a33dabfb7e4f761e94922bc856a320", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
