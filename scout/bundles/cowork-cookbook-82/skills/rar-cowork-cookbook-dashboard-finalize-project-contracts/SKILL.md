---
name: "rar-cowork-cookbook-dashboard-finalize-project-contracts"
description: "Pulls finalize project contracts data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_finalize_project_contracts", "rar_sha256": "aafb1cbfd39c46f61d3874a0849e6de556ef67d3965b9a79a67d440e576af6ea", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
