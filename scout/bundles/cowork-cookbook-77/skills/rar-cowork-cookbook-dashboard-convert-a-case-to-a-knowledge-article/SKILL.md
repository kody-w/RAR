---
name: "rar-cowork-cookbook-dashboard-convert-a-case-to-a-knowledge-article"
description: "Pulls read-only case-to-knowledge-article data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_convert_a_case_to_a_knowledge_article", "rar_sha256": "54e532a485d2c4c9584e0a75910eaf5a102617cc90422ee98467d87b33e58d3c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
