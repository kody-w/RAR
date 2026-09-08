---
name: "rar-cowork-cookbook-dashboard-evaluate-supplier-performance"
description: "Pulls supplier performance data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_evaluate_supplier_performance", "rar_sha256": "8049c21edc4247f71afd6c8387af1f98311d0400b5088bfa174956c50a46fbe8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
