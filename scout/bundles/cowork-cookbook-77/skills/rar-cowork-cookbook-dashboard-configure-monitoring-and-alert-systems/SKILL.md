---
name: "rar-cowork-cookbook-dashboard-configure-monitoring-and-alert-systems"
description: "Pulls monitoring and alert configuration data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard file (charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_monitoring_and_alert_systems", "rar_sha256": "3b51b13b12d7ffacc1a80265858717ee9a86429ec591159f98cd6b2941bde690", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_configure_monitoring_and_alert_systems`. The original RAPP
agent is preserved byte-for-byte in `dashboard_configure_monitoring_and_alert_systems_agent.py` and in the RCI capsule.

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

Configure monitoring and alert systems Interactive HTML Dashboard — Pulls monitoring and alert configuration data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard file (charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-monitoring-and-alert-systems
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
      "description": "Name of the HTML file to generate, e.g. dashboard-configure-monitoring-and-alert-systems-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_monitoring_and_alert_systems_agent.py` and embedded as the fenced Python below (sha256 3b51b13b12d7ffac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_monitoring_and_alert_systems_agent.py` first:

```bash
python3 dashboard_configure_monitoring_and_alert_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_monitoring_and_alert_systems_agent.py   # or on stdin
python3 dashboard_configure_monitoring_and_alert_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure monitoring and alert systems Interactive HTML Dashboard — Pulls monitoring and alert configuration data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard file (charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-monitoring-and-alert-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_monitoring_and_alert_systems',
    "version": '3.0.3',
    "display_name": 'Configure monitoring and alert systems Interactive HTML Dashboard',
    "description": 'Pulls monitoring and alert configuration data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard file (charts, sortable table, RAG indicator) to the out',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-configure-monitoring-and-alert-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-monitoring-and-alert-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c0a2c3aa356ed1e6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/configure-monitoring-and-alert-systems'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-monitoring-and-alert-systems', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to generate, e.g. dashboard-configure-monitoring-and-alert-systems-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of configure monitoring and alert systems with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull configure monitoring and alert systems data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-configure-monitoring-and-alert-systems-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing configure monitoring and alert systems.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls monitoring and alert configuration data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard file (charts, sortable table, RAG indicator) to the out', 'example_request': 'Build an HTML dashboard of monitoring and alert setup in D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to generate, e.g. dashboard-configure-monitoring-and-alert-systems-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 monitoring/alert configuration data without giving the viewer D365 access. Read-only.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardConfigureMonitoringAndAlertSystems(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureMonitoringAndAlertSystems'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to generate, e.g. dashboard-configure-monitoring-and-alert-systems-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardConfigureMonitoringAndAlertSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
