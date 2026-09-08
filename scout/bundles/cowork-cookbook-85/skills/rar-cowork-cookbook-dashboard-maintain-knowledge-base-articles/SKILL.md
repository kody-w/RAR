---
name: "rar-cowork-cookbook-dashboard-maintain-knowledge-base-articles"
description: "Pulls maintain knowledge base articles data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard file to the output folder, re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_knowledge_base_articles", "rar_sha256": "4336ca1849295c3dfdb6abcccae0de6e323cd8989f2d88d882228c4da800885a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_maintain_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `dashboard_maintain_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Maintain knowledge base articles Interactive HTML Dashboard — Pulls maintain knowledge base articles data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard file to the output folder, re

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-knowledge-base-articles
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
      "description": "D365 legal entity to query; recipe defaults to USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-maintain-knowledge-base-articles-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated file, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_maintain_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 4336ca1849295c3d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_maintain_knowledge_base_articles_agent.py` first:

```bash
python3 dashboard_maintain_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_maintain_knowledge_base_articles_agent.py   # or on stdin
python3 dashboard_maintain_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain knowledge base articles Interactive HTML Dashboard — Pulls maintain knowledge base articles data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard file to the output folder, re

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_maintain_knowledge_base_articles',
    "version": '3.0.3',
    "display_name": 'Maintain knowledge base articles Interactive HTML Dashboard',
    "description": 'Pulls maintain knowledge base articles data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard file to the output folder, re',
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
        "upstream_slug": 'dashboard-maintain-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-maintain-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '272277a291b17a97',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/maintain-knowledge-base-articles'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-maintain-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query; recipe defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-maintain-knowledge-base-articles-2026-05-24.html.', 'output_folder': 'Destination folder for the generated file, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of maintain knowledge base articles with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull maintain knowledge base articles data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-maintain-knowledge-base-articles-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing maintain knowledge base articles.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls maintain knowledge base articles data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard file to the output folder, re', 'example_request': 'Build me an interactive HTML dashboard of knowledge base article maintenance from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; recipe defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-maintain-knowledge-base-articles-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated file, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable knowledge base articles dashboard from D365 that recipients can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMaintainKnowledgeBaseArticles(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMaintainKnowledgeBaseArticles'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; recipe defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-maintain-knowledge-base-articles-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated file, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardMaintainKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
