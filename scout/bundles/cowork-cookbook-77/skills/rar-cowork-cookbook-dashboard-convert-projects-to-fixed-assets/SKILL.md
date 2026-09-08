---
name: "rar-cowork-cookbook-dashboard-convert-projects-to-fixed-assets"
description: "Pulls convert-projects-to-fixed-assets data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_convert_projects_to_fixed_assets", "rar_sha256": "d150d36b8a46c3d00611f2d3068bb5170aa42a5cf43c00157d3a6d16a361de31", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
