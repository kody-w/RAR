---
name: "rar-cowork-cookbook-dashboard-convert-projects-to-fixed-assets"
description: "Pulls convert-projects-to-fixed-assets data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_convert_projects_to_fixed_assets", "rar_sha256": "d150d36b8a46c3d00611f2d3068bb5170aa42a5cf43c00157d3a6d16a361de31", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_convert_projects_to_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_convert_projects_to_fixed_assets_agent.py` and in the RCI capsule.

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

Convert projects to fixed assets Interactive HTML Dashboard — Pulls convert-projects-to-fixed-assets data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-convert-projects-to-fixed-assets
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
      "description": "D365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-convert-projects-to-fixed-assets-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_convert_projects_to_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 d150d36b8a46c3d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_convert_projects_to_fixed_assets_agent.py` first:

```bash
python3 dashboard_convert_projects_to_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_convert_projects_to_fixed_assets_agent.py   # or on stdin
python3 dashboard_convert_projects_to_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Convert projects to fixed assets Interactive HTML Dashboard — Pulls convert-projects-to-fixed-assets data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-convert-projects-to-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_convert_projects_to_fixed_assets',
    "version": '3.0.3',
    "display_name": 'Convert projects to fixed assets Interactive HTML Dashboard',
    "description": 'Pulls convert-projects-to-fixed-assets data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the o',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-convert-projects-to-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-convert-projects-to-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5d1104806dfb49c3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/convert-projects-to-fixed-assets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-convert-projects-to-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-convert-projects-to-fixed-assets-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of convert projects to fixed assets with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull convert projects to fixed assets data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-convert-projects-to-fixed-assets-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing convert projects to fixed assets.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls convert-projects-to-fixed-assets data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the o', 'example_request': 'Build the convert projects to fixed assets HTML dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-convert-projects-to-fixed-assets-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone needs a shareable browser-viewable dashboard of convert projects to fixed assets data for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardConvertProjectsToFixedAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConvertProjectsToFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-convert-projects-to-fixed-assets-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardConvertProjectsToFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
