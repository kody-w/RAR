---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-geofencing-and-geolocation-settings"
description: "Pulls geofencing and geolocation settings data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_geofencing_and_geolocation_settings", "rar_sha256": "f390b8b9527e2300bb2e4bcf79598f7adb1245f9cad78bd711ce99c7ba1b162b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_configure_and_manage_geofencing_and_geolocation_settings`. The original RAPP
agent is preserved byte-for-byte in `dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py` and in the RCI capsule.

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

Configure and manage geofencing and geolocation settings Interactive HTML Dashboard — Pulls geofencing and geolocation settings data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-geofencing-and-geolocation-settings
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
      "description": "Name of the standalone HTML file to write, e.g. dashboard-configure-and-manage-geofencing-and-geolocation-settings-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py` and embedded as the fenced Python below (sha256 f390b8b9527e2300…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py` first:

```bash
python3 dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py   # or on stdin
python3 dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage geofencing and geolocation settings Interactive HTML Dashboard — Pulls geofencing and geolocation settings data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-geofencing-and-geolocation-settings
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_and_manage_geofencing_and_geolocation_settings',
    "version": '3.0.3',
    "display_name": 'Configure and manage geofencing and geolocation settings Interactive HTML Dashboard',
    "description": 'Pulls geofencing and geolocation settings data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-configure-and-manage-geofencing-and-geolocation-settings',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-and-manage-geofencing-and-geolocation-settings',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e9ec7d4dcb9b2414',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-geofencing-and-geolocation-settings'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-and-manage-geofencing-and-geolocation-settings', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the standalone HTML file to write, e.g. dashboard-configure-and-manage-geofencing-and-geolocation-settings-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of configure and manage geofencing and geolocation settings with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull configure and manage geofencing and geolocation settings data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-configure-and-manage-geofencing-and-geolocation-settings-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-04', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing configure and manage geofencing and geolocation settings.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls geofencing and geolocation settings data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp', 'example_request': 'Build me an HTML dashboard of geofencing and geolocation settings in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the standalone HTML file to write, e.g. dashboard-configure-and-manage-geofencing-and-geolocation-settings-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 geofencing/geolocation settings for viewers who have no D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardConfigureAndManageGeofencingAndGeolocationSettings(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureAndManageGeofencingAndGeolocationSettings'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the standalone HTML file to write, e.g. dashboard-configure-and-manage-geofencing-and-geolocation-settings-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardConfigureAndManageGeofencingAndGeolocationSettings().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
