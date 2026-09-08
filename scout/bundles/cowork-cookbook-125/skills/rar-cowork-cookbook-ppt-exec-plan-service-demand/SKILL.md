---
name: "rar-cowork-cookbook-ppt-exec-plan-service-demand"
description: "Builds a read-only executive PowerPoint deck on plan service demand from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_service_demand", "rar_sha256": "1d3547c47d75c4d49900d74dc3de46f4e0023d0178235c7df4ba755a3bd858cb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_service_demand`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_service_demand_agent.py` and in the RCI capsule.

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

Plan service demand Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on plan service demand from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-service-demand
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
      "description": "Prior period to compare against in the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull plan service demand data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-plan-service-demand-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_service_demand_agent.py` and embedded as the fenced Python below (sha256 1d3547c47d75c4d4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_service_demand_agent.py` first:

```bash
python3 ppt_exec_plan_service_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_service_demand_agent.py   # or on stdin
python3 ppt_exec_plan_service_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service demand Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on plan service demand from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-service-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_service_demand',
    "version": '3.0.3',
    "display_name": 'Plan service demand Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on plan service demand from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-plan-service-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-service-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '56d555f7875de8d8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/plan-service-demand'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-plan-service-demand', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull plan service demand data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-service-demand-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for plan service demand reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on plan service demand for a 15-minute monthly review. Produce 'ppt-exec-plan-service-demand-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan service demand data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on plan service demand from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build the executive plan service demand deck for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull plan service demand data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-service-demand-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready plan service demand deck from D365 F&SCM for a short monthly review, without changing any ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPlanServiceDemand(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanServiceDemand'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull plan service demand data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-service-demand-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecPlanServiceDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
