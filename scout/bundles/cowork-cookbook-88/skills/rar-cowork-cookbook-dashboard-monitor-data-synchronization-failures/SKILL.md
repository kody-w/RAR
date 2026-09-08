---
name: "rar-cowork-cookbook-dashboard-monitor-data-synchronization-failures"
description: "Pulls data synchronization failure records from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_data_synchronization_failures", "rar_sha256": "c373727a5e0befa8d292c2ac2d923460f775f3b1f5272d73f7d45e670c518f14", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
