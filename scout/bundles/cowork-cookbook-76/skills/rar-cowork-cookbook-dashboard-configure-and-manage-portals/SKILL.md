---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-portals"
description: "Pulls read-only configure-and-manage-portals data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_portals", "rar_sha256": "9fe7bc0cf03472d2cf9c64ce23373f42f4537b7fab9c452fad345331c0b45fce", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
