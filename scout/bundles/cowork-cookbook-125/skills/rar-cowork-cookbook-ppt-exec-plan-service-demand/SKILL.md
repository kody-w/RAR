---
name: "rar-cowork-cookbook-ppt-exec-plan-service-demand"
description: "Builds a read-only executive PowerPoint deck on plan service demand from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_service_demand", "rar_sha256": "1d3547c47d75c4d49900d74dc3de46f4e0023d0178235c7df4ba755a3bd858cb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
