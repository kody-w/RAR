---
name: "rar-cowork-cookbook-dashboard-analyze-production-costs"
description: "Pulls production cost data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and produces a standalone interactive HTML dashboard file saved to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_production_costs", "rar_sha256": "2d3e646638708b11c57de519081a340fd34c08b49be68788da081ce3bb5366dd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
