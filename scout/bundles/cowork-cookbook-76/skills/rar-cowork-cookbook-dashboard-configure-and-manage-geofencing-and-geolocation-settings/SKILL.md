---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-geofencing-and-geolocation-settings"
description: "Pulls geofencing and geolocation settings data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_geofencing_and_geolocation_settings", "rar_sha256": "f390b8b9527e2300bb2e4bcf79598f7adb1245f9cad78bd711ce99c7ba1b162b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
