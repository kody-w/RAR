---
name: "rar-cowork-cookbook-dashboard-maintain-knowledge-base-articles"
description: "Pulls maintain knowledge base articles data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard file to the output folder, re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_knowledge_base_articles", "rar_sha256": "4336ca1849295c3dfdb6abcccae0de6e323cd8989f2d88d882228c4da800885a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
