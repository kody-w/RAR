---
name: "rar-cowork-cookbook-dashboard-monitor-project-status"
description: "Pulls project status data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_project_status", "rar_sha256": "3bdad0a44ea0a3200f294e34762dbea4a5f97b261548bfc3c845aa122f40df56", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
