---
name: "rar-cowork-cookbook-ppt-exec-plan-logistics-and-distribution"
description: "Builds a read-only executive PowerPoint deck on logistics and distribution status from Dynamics 365 F&SCM ERP data, with title, KPI, trend, issues, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_logistics_and_distribution", "rar_sha256": "a01b80991c181ae68b281fe0ae58727cfe912ccaddc3dcf0dbeb2cf933da0d75", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_logistics_and_distribution`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_logistics_and_distribution_agent.py` and in the RCI capsule.

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

Plan logistics and distribution Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on logistics and distribution status from Dynamics 365 F&SCM ERP data, with title, KPI, trend, issues, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-logistics-and-distribution
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-plan-logistics-and-distribution-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_logistics_and_distribution_agent.py` and embedded as the fenced Python below (sha256 a01b80991c181ae6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_logistics_and_distribution_agent.py` first:

```bash
python3 ppt_exec_plan_logistics_and_distribution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_logistics_and_distribution_agent.py   # or on stdin
python3 ppt_exec_plan_logistics_and_distribution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan logistics and distribution Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on logistics and distribution status from Dynamics 365 F&SCM ERP data, with title, KPI, trend, issues, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-logistics-and-distribution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_logistics_and_distribution',
    "version": '3.0.3',
    "display_name": 'Plan logistics and distribution Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on logistics and distribution status from Dynamics 365 F&SCM ERP data, with title, KPI, trend, issues, actions, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-plan-logistics-and-distribution',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-logistics-and-distribution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ac472360c168f4ed',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-logistics-and-distribution'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-plan-logistics-and-distribution', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-logistics-and-distribution-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for plan logistics and distribution reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on plan logistics and distribution for a 15-minute monthly review. Produce 'ppt-exec-plan-logistics-and-distribution-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan logistics and distribution data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on logistics and distribution status from Dynamics 365 F&SCM ERP data, with title, KPI, trend, issues, actions, and appendix slides plus speaker notes.', 'example_request': "Build the exec PowerPoint on plan logistics and distribution for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-logistics-and-distribution-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a monthly 15-minute executive review deck on plan logistics and distribution sourced from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPlanLogisticsAndDistribution(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanLogisticsAndDistribution'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-logistics-and-distribution-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review).', 'type': 'string'}},
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
    print(PptExecPlanLogisticsAndDistribution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
