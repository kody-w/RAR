---
name: "rar-cowork-cookbook-dashboard-plan-logistics-and-distribution"
description: "Pulls plan logistics and distribution data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_logistics_and_distribution", "rar_sha256": "43b81d8ec0ca582fd6f14f2a54bb2b73b6215d961a2c009a78cee44e76b79d33", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_plan_logistics_and_distribution`. The original RAPP
agent is preserved byte-for-byte in `dashboard_plan_logistics_and_distribution_agent.py` and in the RCI capsule.

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

Plan logistics and distribution Interactive HTML Dashboard — Pulls plan logistics and distribution data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-logistics-and-distribution
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-plan-logistics-and-distribution-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_logistics_and_distribution_agent.py` and embedded as the fenced Python below (sha256 43b81d8ec0ca582f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_logistics_and_distribution_agent.py` first:

```bash
python3 dashboard_plan_logistics_and_distribution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_plan_logistics_and_distribution_agent.py   # or on stdin
python3 dashboard_plan_logistics_and_distribution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan logistics and distribution Interactive HTML Dashboard — Pulls plan logistics and distribution data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-logistics-and-distribution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_plan_logistics_and_distribution',
    "version": '3.0.3',
    "display_name": 'Plan logistics and distribution Interactive HTML Dashboard',
    "description": 'Pulls plan logistics and distribution data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only.',
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
        "upstream_slug": 'dashboard-plan-logistics-and-distribution',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-plan-logistics-and-distribution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '33d2b97f44cddd04',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-logistics-and-distribution'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-plan-logistics-and-distribution', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-plan-logistics-and-distribution-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of plan logistics and distribution with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull plan logistics and distribution data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-plan-logistics-and-distribution-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing plan logistics and distribution.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls plan logistics and distribution data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only.', 'example_request': 'Build me an interactive HTML logistics and distribution dashboard from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-plan-logistics-and-distribution-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable logistics/distribution dashboard from D365 that can be shared with people who have no D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardPlanLogisticsAndDistribution(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPlanLogisticsAndDistribution'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-plan-logistics-and-distribution-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardPlanLogisticsAndDistribution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
