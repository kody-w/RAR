---
name: "rar-cowork-cookbook-dashboard-analyze-marketing-trends"
description: "Pulls marketing trend data from Dynamics 365 ERP for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_marketing_trends", "rar_sha256": "719dbfdf6ec292d0e4a8d5ad9b8d052f1966d22bfc815dfd6e485556864dbe74", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
