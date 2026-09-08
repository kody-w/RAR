---
name: "rar-cowork-cookbook-ppt-exec-measure-project-progress"
description: "Builds a read-only executive PowerPoint deck on project progress from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_measure_project_progress", "rar_sha256": "9f486d47dffe0f094ffd162a0df1dce2be5c8d3bd23b770df7df3c91bdf3f807", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_measure_project_progress`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_measure_project_progress_agent.py` and in the RCI capsule.

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

Measure project progress Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on project progress from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-measure-project-progress
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
    "comparison_period": {
      "description": "Prior period to trend the KPIs against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-measure-project-progress-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Intended briefing length/scope, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_measure_project_progress_agent.py` and embedded as the fenced Python below (sha256 9f486d47dffe0f09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_measure_project_progress_agent.py` first:

```bash
python3 ppt_exec_measure_project_progress_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_measure_project_progress_agent.py   # or on stdin
python3 ppt_exec_measure_project_progress_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure project progress Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on project progress from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-measure-project-progress
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_measure_project_progress',
    "version": '3.0.3',
    "display_name": 'Measure project progress Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on project progress from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-measure-project-progress',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-measure-project-progress',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '78c4ed425a9d5d43',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/measure-project-progress'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-measure-project-progress', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend the KPIs against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-measure-project-progress-2026-05-24.pptx.', 'review_length': 'Intended briefing length/scope, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for measure project progress reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on measure project progress for a 15-minute monthly review. Produce 'ppt-exec-measure-project-progress-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads measure project progress data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on project progress from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on project progress for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-measure-project-progress-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Intended briefing length/scope, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the KPIs against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX summarizing project progress from D365 F&SCM for a short monthly review, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMeasureProjectProgress(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMeasureProjectProgress'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend the KPIs against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-measure-project-progress-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Intended briefing length/scope, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecMeasureProjectProgress().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
