---
name: "rar-cowork-cookbook-dashboard-configure-monitoring-and-alert-systems"
description: "Pulls monitoring and alert configuration data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard file (charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_monitoring_and_alert_systems", "rar_sha256": "3b51b13b12d7ffacc1a80265858717ee9a86429ec591159f98cd6b2941bde690", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
