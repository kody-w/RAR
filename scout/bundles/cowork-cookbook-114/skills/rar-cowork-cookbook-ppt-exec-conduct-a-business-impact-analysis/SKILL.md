---
name: "rar-cowork-cookbook-ppt-exec-conduct-a-business-impact-analysis"
description: "Builds a read-only executive PowerPoint deck on business impact analysis from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_conduct_a_business_impact_analysis", "rar_sha256": "e3dd7de1c5cabf7391c203ef115bec6c5468f3cde749f0675c1744d3d8b4bcf5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
