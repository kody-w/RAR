---
name: "rar-cowork-cookbook-dashboard-monitor-asset-performance"
description: "Pulls monitor asset performance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and returns a standalone interactive HTML dashboard file saved to the Cowork output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_asset_performance", "rar_sha256": "b880b5c8434b73c5a6fe1c001b8152163eeeea2ec5cc0ae285d09ab428e84a59", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
