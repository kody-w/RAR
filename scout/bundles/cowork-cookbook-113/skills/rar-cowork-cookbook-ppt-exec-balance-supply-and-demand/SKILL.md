---
name: "rar-cowork-cookbook-ppt-exec-balance-supply-and-demand"
description: "Builds a read-only executive PowerPoint deck on balance supply and demand from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_balance_supply_and_demand", "rar_sha256": "0c7245734cfcc849cb588c65325f53d899656029c350f202cb072ce8fb345322", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_balance_supply_and_demand`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_balance_supply_and_demand_agent.py` and in the RCI capsule.

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

Balance supply and demand Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on balance supply and demand from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-balance-supply-and-demand
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
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-balance-supply-and-demand-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_balance_supply_and_demand_agent.py` and embedded as the fenced Python below (sha256 0c7245734cfcc849…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_balance_supply_and_demand_agent.py` first:

```bash
python3 ppt_exec_balance_supply_and_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_balance_supply_and_demand_agent.py   # or on stdin
python3 ppt_exec_balance_supply_and_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Balance supply and demand Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on balance supply and demand from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-balance-supply-and-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_balance_supply_and_demand',
    "version": '3.0.3',
    "display_name": 'Balance supply and demand Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on balance supply and demand from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-balance-supply-and-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-balance-supply-and-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b86b8ee44aded69e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/balance-supply-and-demand'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-balance-supply-and-demand', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-balance-supply-and-demand-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for balance supply and demand reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on balance supply and demand for a 15-minute monthly review. Produce 'ppt-exec-balance-supply-and-demand-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads balance supply and demand data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on balance supply and demand from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': "Build an exec PowerPoint on balance supply and demand for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-balance-supply-and-demand-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison.', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready supply/demand review deck from D365 ERP data for a monthly 15-minute review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecBalanceSupplyAndDemand(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecBalanceSupplyAndDemand'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-balance-supply-and-demand-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison.', 'type': 'string'}},
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
    print(PptExecBalanceSupplyAndDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
