---
name: "rar-cowork-cookbook-dashboard-plan-logistics-and-distribution"
description: "Pulls plan logistics and distribution data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_logistics_and_distribution", "rar_sha256": "43b81d8ec0ca582fd6f14f2a54bb2b73b6215d961a2c009a78cee44e76b79d33", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
