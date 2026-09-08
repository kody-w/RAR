---
name: "rar-cowork-cookbook-dashboard-monitor-asset-performance"
description: "Pulls monitor asset performance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and returns a standalone interactive HTML dashboard file saved to the Cowork output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_asset_performance", "rar_sha256": "b880b5c8434b73c5a6fe1c001b8152163eeeea2ec5cc0ae285d09ab428e84a59", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_monitor_asset_performance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_monitor_asset_performance_agent.py` and in the RCI capsule.

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

Monitor asset performance Interactive HTML Dashboard — Pulls monitor asset performance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and returns a standalone interactive HTML dashboard file saved to the Cowork output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-asset-performance
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Name of the generated HTML file, e.g. dashboard-monitor-asset-performance-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the HTML file; defaults to Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_asset_performance_agent.py` and embedded as the fenced Python below (sha256 b880b5c8434b73c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_asset_performance_agent.py` first:

```bash
python3 dashboard_monitor_asset_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_asset_performance_agent.py   # or on stdin
python3 dashboard_monitor_asset_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor asset performance Interactive HTML Dashboard — Pulls monitor asset performance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and returns a standalone interactive HTML dashboard file saved to the Cowork output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-asset-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_asset_performance',
    "version": '3.0.3',
    "display_name": 'Monitor asset performance Interactive HTML Dashboard',
    "description": 'Pulls monitor asset performance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and returns a standalone interactive HTML dashboard file saved to the Cowork output folder; read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-monitor-asset-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-asset-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '22600917c7b62e25',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/monitor-asset-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-monitor-asset-performance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-monitor-asset-performance-2026-05-24.html.', 'output_folder': 'Destination folder for the HTML file; defaults to Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of monitor asset performance with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull monitor asset performance data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-monitor-asset-performance-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing monitor asset performance.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls monitor asset performance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and returns a standalone interactive HTML dashboard file saved to the Cowork output folder; read-only.', 'example_request': 'Build me an interactive HTML dashboard of monitor asset performance from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-monitor-asset-performance-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the HTML file; defaults to Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of monitor asset performance from D365, without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMonitorAssetPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorAssetPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-monitor-asset-performance-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the HTML file; defaults to Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardMonitorAssetPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
