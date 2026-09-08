---
name: "rar-cowork-cookbook-dashboard-analyze-marketing-trends"
description: "Pulls marketing trend data from Dynamics 365 ERP for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_marketing_trends", "rar_sha256": "719dbfdf6ec292d0e4a8d5ad9b8d052f1966d22bfc815dfd6e485556864dbe74", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_analyze_marketing_trends`. The original RAPP
agent is preserved byte-for-byte in `dashboard_analyze_marketing_trends_agent.py` and in the RCI capsule.

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

Analyze marketing trends Interactive HTML Dashboard — Pulls marketing trend data from Dynamics 365 ERP for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-marketing-trends
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
      "description": "Name of the HTML file to produce, e.g. dashboard-analyze-marketing-trends-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_analyze_marketing_trends_agent.py` and embedded as the fenced Python below (sha256 719dbfdf6ec292d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_analyze_marketing_trends_agent.py` first:

```bash
python3 dashboard_analyze_marketing_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_analyze_marketing_trends_agent.py   # or on stdin
python3 dashboard_analyze_marketing_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze marketing trends Interactive HTML Dashboard — Pulls marketing trend data from Dynamics 365 ERP for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-marketing-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_analyze_marketing_trends',
    "version": '3.0.3',
    "display_name": 'Analyze marketing trends Interactive HTML Dashboard',
    "description": "Pulls marketing trend data from Dynamics 365 ERP for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-analyze-marketing-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-analyze-marketing-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '67a3207c785655fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/analyze-marketing-trends'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-analyze-marketing-trends', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-analyze-marketing-trends-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of analyze marketing trends with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull analyze marketing trends data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-analyze-marketing-trends-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing analyze marketing trends.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Pulls marketing trend data from Dynamics 365 ERP for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output", 'example_request': 'Build me a marketing trends HTML dashboard from D365 for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-analyze-marketing-trends-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when someone needs a shareable browser-viewable marketing trends dashboard from D365 data without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardAnalyzeMarketingTrends(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAnalyzeMarketingTrends'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-analyze-marketing-trends-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardAnalyzeMarketingTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
