---
name: "rar-cowork-cookbook-dashboard-convert-a-case-to-a-knowledge-article"
description: "Pulls read-only case-to-knowledge-article data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_convert_a_case_to_a_knowledge_article", "rar_sha256": "54e532a485d2c4c9584e0a75910eaf5a102617cc90422ee98467d87b33e58d3c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_convert_a_case_to_a_knowledge_article`. The original RAPP
agent is preserved byte-for-byte in `dashboard_convert_a_case_to_a_knowledge_article_agent.py` and in the RCI capsule.

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

Convert a case to a knowledge article Interactive HTML Dashboard — Pulls read-only case-to-knowledge-article data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-convert-a-case-to-a-knowledge-article
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
      "description": "Name of the HTML file to write, e.g. dashboard-convert-a-case-to-a-knowledge-article-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_convert_a_case_to_a_knowledge_article_agent.py` and embedded as the fenced Python below (sha256 54e532a485d2c4c9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_convert_a_case_to_a_knowledge_article_agent.py` first:

```bash
python3 dashboard_convert_a_case_to_a_knowledge_article_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_convert_a_case_to_a_knowledge_article_agent.py   # or on stdin
python3 dashboard_convert_a_case_to_a_knowledge_article_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Convert a case to a knowledge article Interactive HTML Dashboard — Pulls read-only case-to-knowledge-article data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-convert-a-case-to-a-knowledge-article
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_convert_a_case_to_a_knowledge_article',
    "version": '3.0.3',
    "display_name": 'Convert a case to a knowledge article Interactive HTML Dashboard',
    "description": "Pulls read-only case-to-knowledge-article data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-convert-a-case-to-a-knowledge-article',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-convert-a-case-to-a-knowledge-article',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '118faa0b9c196b54',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/convert-a-case-to-a-knowledge-article'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-convert-a-case-to-a-knowledge-article', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-convert-a-case-to-a-knowledge-article-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of convert a case to a knowledge article with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull convert a case to a knowledge article data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-convert-a-case-to-a-knowledge-article-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing convert a case to a knowledge article.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Pulls read-only case-to-knowledge-article data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out", 'example_request': 'Build the case-to-knowledge-article HTML dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-convert-a-case-to-a-knowledge-article-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a browser-viewable dashboard of case-to-knowledge-article data from D365 that recipients can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardConvertACaseToAKnowledgeArticle(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConvertACaseToAKnowledgeArticle'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-convert-a-case-to-a-knowledge-article-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardConvertACaseToAKnowledgeArticle().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
