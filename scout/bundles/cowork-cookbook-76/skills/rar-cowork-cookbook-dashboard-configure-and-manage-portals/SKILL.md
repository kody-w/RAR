---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-portals"
description: "Pulls read-only configure-and-manage-portals data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_portals", "rar_sha256": "9fe7bc0cf03472d2cf9c64ce23373f42f4537b7fab9c452fad345331c0b45fce", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_configure_and_manage_portals`. The original RAPP
agent is preserved byte-for-byte in `dashboard_configure_and_manage_portals_agent.py` and in the RCI capsule.

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

Configure and manage portals Interactive HTML Dashboard — Pulls read-only configure-and-manage-portals data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-portals
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
      "description": "Name of the HTML file to produce, e.g. dashboard-configure-and-manage-portals-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the file, normally Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_and_manage_portals_agent.py` and embedded as the fenced Python below (sha256 9fe7bc0cf03472d2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_and_manage_portals_agent.py` first:

```bash
python3 dashboard_configure_and_manage_portals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_and_manage_portals_agent.py   # or on stdin
python3 dashboard_configure_and_manage_portals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage portals Interactive HTML Dashboard — Pulls read-only configure-and-manage-portals data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-portals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_and_manage_portals',
    "version": '3.0.3',
    "display_name": 'Configure and manage portals Interactive HTML Dashboard',
    "description": 'Pulls read-only configure-and-manage-portals data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder.',
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
        "upstream_slug": 'dashboard-configure-and-manage-portals',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-and-manage-portals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '346d52036fc0e339',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-portals'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-and-manage-portals', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-configure-and-manage-portals-2026-05-24.html.', 'output_folder': 'Destination folder for the file, normally Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of configure and manage portals with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull configure and manage portals data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-configure-and-manage-portals-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-04', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing configure and manage portals.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls read-only configure-and-manage-portals data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder.', 'example_request': 'Build the configure and manage portals HTML dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-configure-and-manage-portals-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the file, normally Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of configure-and-manage-portals D365 data for viewers who have no D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardConfigureAndManagePortals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureAndManagePortals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-configure-and-manage-portals-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the file, normally Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardConfigureAndManagePortals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
