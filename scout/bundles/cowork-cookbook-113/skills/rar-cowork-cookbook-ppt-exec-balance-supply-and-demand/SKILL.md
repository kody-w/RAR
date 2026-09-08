---
name: "rar-cowork-cookbook-ppt-exec-balance-supply-and-demand"
description: "Builds a read-only executive PowerPoint deck on balance supply and demand from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_balance_supply_and_demand", "rar_sha256": "0c7245734cfcc849cb588c65325f53d899656029c350f202cb072ce8fb345322", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
