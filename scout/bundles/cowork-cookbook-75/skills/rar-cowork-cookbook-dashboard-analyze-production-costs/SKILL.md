---
name: "rar-cowork-cookbook-dashboard-analyze-production-costs"
description: "Pulls production cost data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and produces a standalone interactive HTML dashboard file saved to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_production_costs", "rar_sha256": "2d3e646638708b11c57de519081a340fd34c08b49be68788da081ce3bb5366dd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_analyze_production_costs`. The original RAPP
agent is preserved byte-for-byte in `dashboard_analyze_production_costs_agent.py` and in the RCI capsule.

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

Analyze production costs Interactive HTML Dashboard — Pulls production cost data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and produces a standalone interactive HTML dashboard file saved to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-production-costs
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
      "description": "Fiscal period to analyze; defaults to the most recent available.",
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
      "description": "Name of the HTML file to generate, e.g. dashboard-analyze-production-costs-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_analyze_production_costs_agent.py` and embedded as the fenced Python below (sha256 2d3e646638708b11…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_analyze_production_costs_agent.py` first:

```bash
python3 dashboard_analyze_production_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_analyze_production_costs_agent.py   # or on stdin
python3 dashboard_analyze_production_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze production costs Interactive HTML Dashboard — Pulls production cost data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and produces a standalone interactive HTML dashboard file saved to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-production-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_analyze_production_costs',
    "version": '3.0.3',
    "display_name": 'Analyze production costs Interactive HTML Dashboard',
    "description": 'Pulls production cost data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and produces a standalone interactive HTML dashboard file saved to the output folder; read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-analyze-production-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-analyze-production-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '213681ed37e746db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/analyze-production-costs'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-analyze-production-costs', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to analyze; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to generate, e.g. dashboard-analyze-production-costs-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of analyze production costs with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull analyze production costs data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-analyze-production-costs-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing analyze production costs.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls production cost data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and produces a standalone interactive HTML dashboard file saved to the output folder; read-only.', 'example_request': 'Build me an interactive HTML dashboard of production costs from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to analyze; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to generate, e.g. dashboard-analyze-production-costs-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants production cost data from D365 packaged as a self-contained browser dashboard for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardAnalyzeProductionCosts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAnalyzeProductionCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to analyze; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to generate, e.g. dashboard-analyze-production-costs-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardAnalyzeProductionCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
