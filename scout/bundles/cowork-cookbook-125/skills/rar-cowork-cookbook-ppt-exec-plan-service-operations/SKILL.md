---
name: "rar-cowork-cookbook-ppt-exec-plan-service-operations"
description: "Builds a read-only executive PowerPoint deck on plan service operations from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_service_operations", "rar_sha256": "c2d789719ef63e8271b7505ae43f6a2e188c03dfdeb029c06875e3f40e76aa4b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_service_operations`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_service_operations_agent.py` and in the RCI capsule.

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

Plan service operations Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on plan service operations from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-service-operations
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
      "description": "Prior period to compare trends against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-plan-service-operations-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_service_operations_agent.py` and embedded as the fenced Python below (sha256 c2d789719ef63e82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_service_operations_agent.py` first:

```bash
python3 ppt_exec_plan_service_operations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_service_operations_agent.py   # or on stdin
python3 ppt_exec_plan_service_operations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service operations Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on plan service operations from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-service-operations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_service_operations',
    "version": '3.0.3',
    "display_name": 'Plan service operations Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on plan service operations from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-plan-service-operations',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-service-operations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '97145fc1efdce144',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-service-operations'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-plan-service-operations', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare trends against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-service-operations-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for plan service operations reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on plan service operations for a 15-minute monthly review. Produce 'ppt-exec-plan-service-operations-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan service operations data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on plan service operations from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on plan service operations for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-service-operations-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare trends against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX summarizing plan service operations status from D365 ERP for a monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPlanServiceOperations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanServiceOperations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare trends against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-service-operations-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecPlanServiceOperations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
