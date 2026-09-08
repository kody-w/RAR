---
name: "rar-cowork-cookbook-dashboard-plan-capital-allocation-and-investments"
description: "Pulls plan capital allocation and investment data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard file to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_capital_allocation_and_investments", "rar_sha256": "3e0e59707610e581af7f7f436d34359658356e47bb4450f35497d82e6c8c6f07", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
