---
name: "rar-cowork-cookbook-dashboard-evaluate-supplier-performance"
description: "Pulls supplier performance data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_evaluate_supplier_performance", "rar_sha256": "8049c21edc4247f71afd6c8387af1f98311d0400b5088bfa174956c50a46fbe8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_evaluate_supplier_performance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_evaluate_supplier_performance_agent.py` and in the RCI capsule.

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

Evaluate supplier performance Interactive HTML Dashboard — Pulls supplier performance data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-evaluate-supplier-performance
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
      "description": "Name of the HTML file to write, e.g. dashboard-evaluate-supplier-performance-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_evaluate_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 8049c21edc4247f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_evaluate_supplier_performance_agent.py` first:

```bash
python3 dashboard_evaluate_supplier_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_evaluate_supplier_performance_agent.py   # or on stdin
python3 dashboard_evaluate_supplier_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate supplier performance Interactive HTML Dashboard — Pulls supplier performance data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-evaluate-supplier-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_evaluate_supplier_performance',
    "version": '3.0.3',
    "display_name": 'Evaluate supplier performance Interactive HTML Dashboard',
    "description": 'Pulls supplier performance data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde',
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
        "upstream_slug": 'dashboard-evaluate-supplier-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-evaluate-supplier-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8f0ff1d269c6e168',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/evaluate-supplier-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-evaluate-supplier-performance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-evaluate-supplier-performance-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of evaluate supplier performance with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull evaluate supplier performance data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-evaluate-supplier-performance-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing evaluate supplier performance.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls supplier performance data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde', 'example_request': 'Build me a supplier performance dashboard from D365 for USMF for the latest fiscal period as an HTML file.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-evaluate-supplier-performance-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants supplier performance from D365 packaged as a shareable browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardEvaluateSupplierPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardEvaluateSupplierPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-evaluate-supplier-performance-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardEvaluateSupplierPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
