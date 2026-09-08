---
name: "rar-cowork-cookbook-dashboard-finalize-project-contracts"
description: "Pulls finalize project contracts data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_finalize_project_contracts", "rar_sha256": "aafb1cbfd39c46f61d3874a0849e6de556ef67d3965b9a79a67d440e576af6ea", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_finalize_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `dashboard_finalize_project_contracts_agent.py` and in the RCI capsule.

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

Finalize project contracts Interactive HTML Dashboard — Pulls finalize project contracts data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-finalize-project-contracts
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
      "description": "Name of the HTML file to write, e.g. dashboard-finalize-project-contracts-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_finalize_project_contracts_agent.py` and embedded as the fenced Python below (sha256 aafb1cbfd39c46f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_finalize_project_contracts_agent.py` first:

```bash
python3 dashboard_finalize_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_finalize_project_contracts_agent.py   # or on stdin
python3 dashboard_finalize_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize project contracts Interactive HTML Dashboard — Pulls finalize project contracts data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-finalize-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_finalize_project_contracts',
    "version": '3.0.3',
    "display_name": 'Finalize project contracts Interactive HTML Dashboard',
    "description": 'Pulls finalize project contracts data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output',
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
        "upstream_slug": 'dashboard-finalize-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-finalize-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ef7c42f856a52845',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/finalize-project-contracts'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-finalize-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-finalize-project-contracts-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of finalize project contracts with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull finalize project contracts data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-finalize-project-contracts-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing finalize project contracts.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls finalize project contracts data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output', 'example_request': 'Build an interactive HTML dashboard of finalize project contracts for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-finalize-project-contracts-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser-openable dashboard of finalize project contracts data without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardFinalizeProjectContracts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardFinalizeProjectContracts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-finalize-project-contracts-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardFinalizeProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
