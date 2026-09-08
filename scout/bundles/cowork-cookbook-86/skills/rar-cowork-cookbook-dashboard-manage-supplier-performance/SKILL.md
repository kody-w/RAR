---
name: "rar-cowork-cookbook-dashboard-manage-supplier-performance"
description: "Pulls supplier performance data from Dynamics 365 F&SCM for a legal entity and the most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_supplier_performance", "rar_sha256": "4ab9eefbcaa7ae2319e15fa891e08d7a2b46efb03d294d036ca74eaab1b7a317", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
