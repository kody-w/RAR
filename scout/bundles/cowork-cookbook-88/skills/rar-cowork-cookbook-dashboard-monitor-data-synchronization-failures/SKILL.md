---
name: "rar-cowork-cookbook-dashboard-monitor-data-synchronization-failures"
description: "Pulls data synchronization failure records from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_data_synchronization_failures", "rar_sha256": "c373727a5e0befa8d292c2ac2d923460f775f3b1f5272d73f7d45e670c518f14", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_monitor_data_synchronization_failures`. The original RAPP
agent is preserved byte-for-byte in `dashboard_monitor_data_synchronization_failures_agent.py` and in the RCI capsule.

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

Monitor data synchronization failures Interactive HTML Dashboard — Pulls data synchronization failure records from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-data-synchronization-failures
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
      "description": "Name of the HTML file to write, e.g. dashboard-monitor-data-synchronization-failures-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 c373727a5e0befa8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_data_synchronization_failures_agent.py` first:

```bash
python3 dashboard_monitor_data_synchronization_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_data_synchronization_failures_agent.py   # or on stdin
python3 dashboard_monitor_data_synchronization_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor data synchronization failures Interactive HTML Dashboard — Pulls data synchronization failure records from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-data-synchronization-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_data_synchronization_failures',
    "version": '3.0.3',
    "display_name": 'Monitor data synchronization failures Interactive HTML Dashboard',
    "description": 'Pulls data synchronization failure records from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f',
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
        "upstream_slug": 'dashboard-monitor-data-synchronization-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-data-synchronization-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '18f8e4abedd706c3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/monitor-data-synchronization-failures'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-monitor-data-synchronization-failures', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-monitor-data-synchronization-failures-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of monitor data synchronization failures with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull monitor data synchronization failures data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-monitor-data-synchronization-failures-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing monitor data synchronization failures.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls data synchronization failure records from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f', 'example_request': 'Build me an HTML dashboard of data sync failures in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-monitor-data-synchronization-failures-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 data synchronization failures for a recent fiscal period, without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMonitorDataSynchronizationFailures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorDataSynchronizationFailures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-monitor-data-synchronization-failures-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardMonitorDataSynchronizationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
