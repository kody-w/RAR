---
name: "rar-cowork-cookbook-dashboard-manage-supplier-performance"
description: "Pulls supplier performance data from Dynamics 365 F&SCM for a legal entity and the most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_supplier_performance", "rar_sha256": "4ab9eefbcaa7ae2319e15fa891e08d7a2b46efb03d294d036ca74eaab1b7a317", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_supplier_performance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_supplier_performance_agent.py` and in the RCI capsule.

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

Manage supplier performance Interactive HTML Dashboard — Pulls supplier performance data from Dynamics 365 F&SCM for a legal entity and the most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indi

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-supplier-performance
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
      "description": "Reporting period; defaults to the most recent fiscal period available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data for, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-manage-supplier-performance-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 4ab9eefbcaa7ae23…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_supplier_performance_agent.py` first:

```bash
python3 dashboard_manage_supplier_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_supplier_performance_agent.py   # or on stdin
python3 dashboard_manage_supplier_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier performance Interactive HTML Dashboard — Pulls supplier performance data from Dynamics 365 F&SCM for a legal entity and the most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indi

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-supplier-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_supplier_performance',
    "version": '3.0.3',
    "display_name": 'Manage supplier performance Interactive HTML Dashboard',
    "description": 'Pulls supplier performance data from Dynamics 365 F&SCM for a legal entity and the most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indi',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-supplier-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-supplier-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e80657f3b94e6c6c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/manage-supplier-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-manage-supplier-performance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to pull data for, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-manage-supplier-performance-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage supplier performance with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage supplier performance data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-supplier-performance-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage supplier performance.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls supplier performance data from Dynamics 365 F&SCM for a legal entity and the most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indi', 'example_request': 'Build me a supplier performance dashboard for USMF for the latest fiscal period as a standalone HTML file.', 'inputs': [{'description': 'D365 legal entity to pull data for, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-manage-supplier-performance-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable supplier performance dashboard from D365 that viewers can open without D365 access. Read-only; no data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageSupplierPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageSupplierPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data for, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-manage-supplier-performance-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardManageSupplierPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
