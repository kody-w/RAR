---
name: "rar-cowork-cookbook-ppt-exec-conduct-a-business-impact-analysis"
description: "Builds a read-only executive PowerPoint deck on business impact analysis from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_conduct_a_business_impact_analysis", "rar_sha256": "e3dd7de1c5cabf7391c203ef115bec6c5468f3cde749f0675c1744d3d8b4bcf5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_conduct_a_business_impact_analysis`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_conduct_a_business_impact_analysis_agent.py` and in the RCI capsule.

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

Conduct a business impact analysis Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on business impact analysis from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-conduct-a-business-impact-analysis
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
      "description": "Prior period to chart the trend against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-conduct-a-business-impact-analysis-2026-05-24.pptx.",
      "type": "string"
    },
    "review_context": {
      "description": "Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_conduct_a_business_impact_analysis_agent.py` and embedded as the fenced Python below (sha256 e3dd7de1c5cabf73…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_conduct_a_business_impact_analysis_agent.py` first:

```bash
python3 ppt_exec_conduct_a_business_impact_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_conduct_a_business_impact_analysis_agent.py   # or on stdin
python3 ppt_exec_conduct_a_business_impact_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a business impact analysis Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on business impact analysis from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-conduct-a-business-impact-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_conduct_a_business_impact_analysis',
    "version": '3.0.3',
    "display_name": 'Conduct a business impact analysis Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on business impact analysis from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-conduct-a-business-impact-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-conduct-a-business-impact-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '182f3fb7305e0b44',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/conduct-a-business-impact-analysis'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-conduct-a-business-impact-analysis', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to chart the trend against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-conduct-a-business-impact-analysis-2026-05-24.pptx.', 'review_context': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for conduct a business impact analysis reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on conduct a business impact analysis for a 15-minute monthly review. Produce 'ppt-exec-conduct-a-business-impact-analysis-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct a business impact analysis data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on business impact analysis from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on our business impact analysis from D365 USMF for the 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-conduct-a-business-impact-analysis-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.', 'name': 'review_context'}, {'description': 'Prior period to chart the trend against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing business impact analysis status from D365 ERP data for a short periodic review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecConductABusinessImpactAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConductABusinessImpactAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to chart the trend against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-conduct-a-business-impact-analysis-2026-05-24.pptx.', 'type': 'string'}, 'review_context': {'description': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecConductABusinessImpactAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
