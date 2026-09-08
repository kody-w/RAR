---
name: "rar-cowork-cookbook-dashboard-measure-goal-achievement"
description: "Pulls measure goal achievement data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_goal_achievement", "rar_sha256": "3a058812a11c17982a6e5ecbbcd8c90953f5233318d6f10ab0ab6759dd5cbcf8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_measure_goal_achievement`. The original RAPP
agent is preserved byte-for-byte in `dashboard_measure_goal_achievement_agent.py` and in the RCI capsule.

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

Measure goal achievement Interactive HTML Dashboard — Pulls measure goal achievement data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-goal-achievement
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
      "description": "Name of the HTML file to write, e.g. dashboard-measure-goal-achievement-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_measure_goal_achievement_agent.py` and embedded as the fenced Python below (sha256 3a058812a11c1798…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_measure_goal_achievement_agent.py` first:

```bash
python3 dashboard_measure_goal_achievement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_measure_goal_achievement_agent.py   # or on stdin
python3 dashboard_measure_goal_achievement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure goal achievement Interactive HTML Dashboard — Pulls measure goal achievement data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-goal-achievement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_measure_goal_achievement',
    "version": '3.0.3',
    "display_name": 'Measure goal achievement Interactive HTML Dashboard',
    "description": 'Pulls measure goal achievement data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the out',
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
        "upstream_slug": 'dashboard-measure-goal-achievement',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-measure-goal-achievement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fc3eeb7cdccfd7a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-goal-achievement'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-measure-goal-achievement', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-measure-goal-achievement-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of measure goal achievement with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull measure goal achievement data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-measure-goal-achievement-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing measure goal achievement.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls measure goal achievement data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the out', 'example_request': 'Build me an interactive HTML dashboard of measure goal achievement for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-measure-goal-achievement-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 measure goal achievement for a legal entity, without the viewer needing D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMeasureGoalAchievement(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMeasureGoalAchievement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-measure-goal-achievement-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardMeasureGoalAchievement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
