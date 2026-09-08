---
name: "rar-cowork-cookbook-ppt-exec-plan-logistics-and-distribution"
description: "Builds a read-only executive PowerPoint deck on logistics and distribution status from Dynamics 365 F&SCM ERP data, with title, KPI, trend, issues, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_logistics_and_distribution", "rar_sha256": "a01b80991c181ae68b281fe0ae58727cfe912ccaddc3dcf0dbeb2cf933da0d75", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
