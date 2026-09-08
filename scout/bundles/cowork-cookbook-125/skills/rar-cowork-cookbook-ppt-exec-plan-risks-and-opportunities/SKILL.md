---
name: "rar-cowork-cookbook-ppt-exec-plan-risks-and-opportunities"
description: "Builds a read-only executive PowerPoint deck on plan risks and opportunities from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_risks_and_opportunities", "rar_sha256": "e18360b34f9729e2609cc970f30fad9817bfee68dcc8a1fa65856ceb9d2d1c68", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_risks_and_opportunities`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_risks_and_opportunities_agent.py` and in the RCI capsule.

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

Plan risks and opportunities Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on plan risks and opportunities from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-risks-and-opportunities
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
      "description": "Dynamics 365 legal entity to pull plan data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-plan-risks-and-opportunities-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend chart comparison (e.g. monthly review dated 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_risks_and_opportunities_agent.py` and embedded as the fenced Python below (sha256 e18360b34f9729e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_risks_and_opportunities_agent.py` first:

```bash
python3 ppt_exec_plan_risks_and_opportunities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_risks_and_opportunities_agent.py   # or on stdin
python3 ppt_exec_plan_risks_and_opportunities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan risks and opportunities Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on plan risks and opportunities from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-risks-and-opportunities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_risks_and_opportunities',
    "version": '3.0.3',
    "display_name": 'Plan risks and opportunities Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on plan risks and opportunities from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-plan-risks-and-opportunities',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-risks-and-opportunities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '24f93da677eb0c61',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-risks-and-opportunities'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-plan-risks-and-opportunities', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull plan data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-risks-and-opportunities-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend chart comparison (e.g. monthly review dated 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for plan risks and opportunities reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on plan risks and opportunities for a 15-minute monthly review. Produce 'ppt-exec-plan-risks-and-opportunities-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan risks and opportunities data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on plan risks and opportunities from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': 'Build the exec deck on plan risks and opportunities for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull plan data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-risks-and-opportunities-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend chart comparison (e.g. monthly review dated 2026-05-24).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX on plan risks and opportunities for a 15-minute monthly review, sourced from D365 ERP without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPlanRisksAndOpportunities(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanRisksAndOpportunities'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull plan data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-risks-and-opportunities-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend chart comparison (e.g. monthly review dated 2026-05-24).', 'type': 'string'}},
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
    print(PptExecPlanRisksAndOpportunities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
