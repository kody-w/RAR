---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-store-devices"
description: "Pulls store device configuration data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_store_devices", "rar_sha256": "82880b7cb124c8ace6341e2bd5bfc6acd91f3252f15c476a31e516ff21741e39", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_configure_and_manage_store_devices`. The original RAPP
agent is preserved byte-for-byte in `dashboard_configure_and_manage_store_devices_agent.py` and in the RCI capsule.

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

Configure and manage store devices Interactive HTML Dashboard — Pulls store device configuration data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-store-devices
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
      "description": "Name of the HTML file to write, e.g. dashboard-configure-and-manage-store-devices-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_and_manage_store_devices_agent.py` and embedded as the fenced Python below (sha256 82880b7cb124c8ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_and_manage_store_devices_agent.py` first:

```bash
python3 dashboard_configure_and_manage_store_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_and_manage_store_devices_agent.py   # or on stdin
python3 dashboard_configure_and_manage_store_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage store devices Interactive HTML Dashboard — Pulls store device configuration data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-store-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_and_manage_store_devices',
    "version": '3.0.3',
    "display_name": 'Configure and manage store devices Interactive HTML Dashboard',
    "description": 'Pulls store device configuration data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde',
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
        "upstream_slug": 'dashboard-configure-and-manage-store-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-and-manage-store-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '536957e0daa19b09',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-store-devices'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-and-manage-store-devices', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-configure-and-manage-store-devices-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of configure and manage store devices with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull configure and manage store devices data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-configure-and-manage-store-devices-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing configure and manage store devices.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls store device configuration data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde', 'example_request': 'Build an HTML dashboard of store device configuration in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-configure-and-manage-store-devices-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when someone needs a shareable browser-viewable dashboard of store device configuration data from D365, without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardConfigureAndManageStoreDevices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureAndManageStoreDevices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-configure-and-manage-store-devices-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardConfigureAndManageStoreDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
