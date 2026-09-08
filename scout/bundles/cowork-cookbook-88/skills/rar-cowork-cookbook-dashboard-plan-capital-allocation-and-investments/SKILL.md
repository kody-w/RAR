---
name: "rar-cowork-cookbook-dashboard-plan-capital-allocation-and-investments"
description: "Pulls plan capital allocation and investment data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard file to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_capital_allocation_and_investments", "rar_sha256": "3e0e59707610e581af7f7f436d34359658356e47bb4450f35497d82e6c8c6f07", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_plan_capital_allocation_and_investments`. The original RAPP
agent is preserved byte-for-byte in `dashboard_plan_capital_allocation_and_investments_agent.py` and in the RCI capsule.

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

Plan capital allocation and investments Interactive HTML Dashboard — Pulls plan capital allocation and investment data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard file to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-capital-allocation-and-investments
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
    "fiscal_period": {
      "description": "Fiscal period to report on; defaults to the most recent available.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-plan-capital-allocation-and-investments-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_capital_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 3e0e59707610e581…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_capital_allocation_and_investments_agent.py` first:

```bash
python3 dashboard_plan_capital_allocation_and_investments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_plan_capital_allocation_and_investments_agent.py   # or on stdin
python3 dashboard_plan_capital_allocation_and_investments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan capital allocation and investments Interactive HTML Dashboard — Pulls plan capital allocation and investment data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard file to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-capital-allocation-and-investments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_plan_capital_allocation_and_investments',
    "version": '3.0.3',
    "display_name": 'Plan capital allocation and investments Interactive HTML Dashboard',
    "description": 'Pulls plan capital allocation and investment data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard file to the output folder; read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-plan-capital-allocation-and-investments',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-plan-capital-allocation-and-investments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '89ca03d9d6935cba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-capital-allocation-and-investments'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-plan-capital-allocation-and-investments', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-plan-capital-allocation-and-investments-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of plan capital allocation and investments with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull plan capital allocation and investments data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-plan-capital-allocation-and-investments-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing plan capital allocation and investments.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls plan capital allocation and investment data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard file to the output folder; read-only.', 'example_request': 'Build a capital allocation and investments HTML dashboard from D365 for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-plan-capital-allocation-and-investments-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of capital allocation and investment data from D365 without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardPlanCapitalAllocationAndInvestments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPlanCapitalAllocationAndInvestments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-plan-capital-allocation-and-investments-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardPlanCapitalAllocationAndInvestments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
