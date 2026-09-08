---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-store-devices"
description: "Pulls store device configuration data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_store_devices", "rar_sha256": "82880b7cb124c8ace6341e2bd5bfc6acd91f3252f15c476a31e516ff21741e39", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
