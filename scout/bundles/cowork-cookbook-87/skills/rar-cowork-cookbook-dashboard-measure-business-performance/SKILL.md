---
name: "rar-cowork-cookbook-dashboard-measure-business-performance"
description: "Pulls business performance data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only; call when you want a sha"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_business_performance", "rar_sha256": "3a4cb90dc48f26c747c2e18b6a652e0fdc30524ea7b2293ab270d19b9030080c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_measure_business_performance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_measure_business_performance_agent.py` and in the RCI capsule.

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

Measure business performance Interactive HTML Dashboard — Pulls business performance data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only; call when you want a sha

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-business-performance
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
      "description": "D365 legal entity to pull from (recipe default: USMF).",
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
      "description": "Name of the HTML file to write, e.g. dashboard-measure-business-performance-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder to save the HTML file to (Documents/Cowork/output/ in OneDrive).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_measure_business_performance_agent.py` and embedded as the fenced Python below (sha256 3a4cb90dc48f26c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_measure_business_performance_agent.py` first:

```bash
python3 dashboard_measure_business_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_measure_business_performance_agent.py   # or on stdin
python3 dashboard_measure_business_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure business performance Interactive HTML Dashboard — Pulls business performance data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only; call when you want a sha

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-business-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_measure_business_performance',
    "version": '3.0.3',
    "display_name": 'Measure business performance Interactive HTML Dashboard',
    "description": 'Pulls business performance data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only; call when you want a sha',
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
        "upstream_slug": 'dashboard-measure-business-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-measure-business-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8c74cb205c8f1cee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-business-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-measure-business-performance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull from (recipe default: USMF).', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-measure-business-performance-2026-05-24.html.', 'output_folder': 'Folder to save the HTML file to (Documents/Cowork/output/ in OneDrive).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of measure business performance with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull measure business performance data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-measure-business-performance-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing measure business performance.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls business performance data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only; call when you want a sha', 'example_request': "Build me an interactive HTML dashboard of business performance for USMF's most recent fiscal period.", 'inputs': [{'description': 'D365 legal entity to pull from (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Name of the HTML file to write, e.g. dashboard-measure-business-performance-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder to save the HTML file to (Documents/Cowork/output/ in OneDrive).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when someone needs a self-contained HTML dashboard of D365 business performance for the latest fiscal period that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMeasureBusinessPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMeasureBusinessPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-measure-business-performance-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder to save the HTML file to (Documents/Cowork/output/ in OneDrive).', 'type': 'string'}},
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
    print(DashboardMeasureBusinessPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
