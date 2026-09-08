---
name: "rar-cowork-cookbook-ppt-exec-conduct-current-state-analysis"
description: "Builds a read-only executive PowerPoint deck on current state analysis from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_conduct_current_state_analysis", "rar_sha256": "0a5f24791d0b7bbe54e1593e192762a620c081ff7bf104a25d61813e8a392ac4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_conduct_current_state_analysis`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_conduct_current_state_analysis_agent.py` and in the RCI capsule.

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

Conduct current state analysis Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on current state analysis from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-conduct-current-state-analysis
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
    "analysis_topic": {
      "description": "Subject of the current state analysis the deck covers.",
      "type": "string"
    },
    "comparison_period": {
      "description": "Prior period to trend the KPIs against.",
      "type": "string"
    },
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
      "description": "Target .pptx filename, e.g. ppt-exec-conduct-current-state-analysis-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length the deck is scoped to, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_conduct_current_state_analysis_agent.py` and embedded as the fenced Python below (sha256 0a5f24791d0b7bbe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_conduct_current_state_analysis_agent.py` first:

```bash
python3 ppt_exec_conduct_current_state_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_conduct_current_state_analysis_agent.py   # or on stdin
python3 ppt_exec_conduct_current_state_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct current state analysis Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on current state analysis from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-conduct-current-state-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_conduct_current_state_analysis',
    "version": '3.0.3',
    "display_name": 'Conduct current state analysis Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on current state analysis from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-conduct-current-state-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-conduct-current-state-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a645881ae23b219b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/conduct-current-state-analysis'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-conduct-current-state-analysis', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'analysis_topic': 'Subject of the current state analysis the deck covers.', 'comparison_period': 'Prior period to trend the KPIs against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-conduct-current-state-analysis-2026-05-24.pptx.', 'review_length': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for conduct current state analysis reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on conduct current state analysis for a 15-minute monthly review. Produce 'ppt-exec-conduct-current-state-analysis-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct current state analysis data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on current state analysis from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build me a 15-minute exec PowerPoint on current state analysis from D365 legal entity USMF, with speaker notes.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the current state analysis the deck covers.', 'name': 'analysis_topic'}, {'description': 'Target .pptx filename, e.g. ppt-exec-conduct-current-state-analysis-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the KPIs against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready current state analysis deck from D365 ERP data for a short monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecConductCurrentStateAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConductCurrentStateAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'analysis_topic': {'description': 'Subject of the current state analysis the deck covers.', 'type': 'string'}, 'comparison_period': {'description': 'Prior period to trend the KPIs against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-conduct-current-state-analysis-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecConductCurrentStateAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
