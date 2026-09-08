---
name: "rar-cowork-cookbook-ppt-exec-measure-project-progress"
description: "Builds a read-only executive PowerPoint deck on project progress from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_measure_project_progress", "rar_sha256": "9f486d47dffe0f094ffd162a0df1dce2be5c8d3bd23b770df7df3c91bdf3f807", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
