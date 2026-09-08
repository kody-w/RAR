---
name: "rar-cowork-cookbook-dashboard-monitor-project-status"
description: "Pulls project status data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_project_status", "rar_sha256": "3bdad0a44ea0a3200f294e34762dbea4a5f97b261548bfc3c845aa122f40df56", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_monitor_project_status`. The original RAPP
agent is preserved byte-for-byte in `dashboard_monitor_project_status_agent.py` and in the RCI capsule.

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

Monitor project status Interactive HTML Dashboard — Pulls project status data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-project-status
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
      "description": "Name of the HTML file to write, e.g. dashboard-monitor-project-status-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_project_status_agent.py` and embedded as the fenced Python below (sha256 3bdad0a44ea0a320…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_project_status_agent.py` first:

```bash
python3 dashboard_monitor_project_status_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_project_status_agent.py   # or on stdin
python3 dashboard_monitor_project_status_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor project status Interactive HTML Dashboard — Pulls project status data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-project-status
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_project_status',
    "version": '3.0.3',
    "display_name": 'Monitor project status Interactive HTML Dashboard',
    "description": 'Pulls project status data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-monitor-project-status',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-project-status',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dd6eddfe6b4fa0c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/monitor-project-status'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-monitor-project-status', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-monitor-project-status-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of monitor project status with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull monitor project status data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-monitor-project-status-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing monitor project status.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls project status data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-only.', 'example_request': 'Build me an interactive HTML dashboard of project status from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-monitor-project-status-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants project status from D365 packaged as a self-contained browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMonitorProjectStatus(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorProjectStatus'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-monitor-project-status-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardMonitorProjectStatus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
