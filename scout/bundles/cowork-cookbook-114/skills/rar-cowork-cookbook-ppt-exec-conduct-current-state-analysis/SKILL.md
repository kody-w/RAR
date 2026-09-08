---
name: "rar-cowork-cookbook-ppt-exec-conduct-current-state-analysis"
description: "Builds a read-only executive PowerPoint deck on current state analysis from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_conduct_current_state_analysis", "rar_sha256": "0a5f24791d0b7bbe54e1593e192762a620c081ff7bf104a25d61813e8a392ac4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
