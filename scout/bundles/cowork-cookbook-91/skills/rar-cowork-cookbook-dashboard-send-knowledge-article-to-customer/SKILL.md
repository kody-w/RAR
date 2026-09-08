---
name: "rar-cowork-cookbook-dashboard-send-knowledge-article-to-customer"
description: "Pulls send-knowledge-article-to-customer data from Dynamics 365 F&SCM for the most recent fiscal period and writes a standalone interactive HTML dashboard (header totals, two inline SVG charts, sortable table, RAG indica"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_send_knowledge_article_to_customer", "rar_sha256": "d1cd7765cf5079f6eadac31ddac4826dc53b160b6bd6fbd1703dced46f2c390b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_send_knowledge_article_to_customer`. The original RAPP
agent is preserved byte-for-byte in `dashboard_send_knowledge_article_to_customer_agent.py` and in the RCI capsule.

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

Send knowledge article to customer Interactive HTML Dashboard — Pulls send-knowledge-article-to-customer data from Dynamics 365 F&SCM for the most recent fiscal period and writes a standalone interactive HTML dashboard (header totals, two inline SVG charts, sortable table, RAG indica

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-send-knowledge-article-to-customer
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
      "description": "Name of the generated HTML file, e.g. dashboard-send-knowledge-article-to-customer-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_send_knowledge_article_to_customer_agent.py` and embedded as the fenced Python below (sha256 d1cd7765cf5079f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_send_knowledge_article_to_customer_agent.py` first:

```bash
python3 dashboard_send_knowledge_article_to_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_send_knowledge_article_to_customer_agent.py   # or on stdin
python3 dashboard_send_knowledge_article_to_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send knowledge article to customer Interactive HTML Dashboard — Pulls send-knowledge-article-to-customer data from Dynamics 365 F&SCM for the most recent fiscal period and writes a standalone interactive HTML dashboard (header totals, two inline SVG charts, sortable table, RAG indica

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-send-knowledge-article-to-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_send_knowledge_article_to_customer',
    "version": '3.0.3',
    "display_name": 'Send knowledge article to customer Interactive HTML Dashboard',
    "description": 'Pulls send-knowledge-article-to-customer data from Dynamics 365 F&SCM for the most recent fiscal period and writes a standalone interactive HTML dashboard (header totals, two inline SVG charts, sortable table, RAG indica',
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
        "upstream_slug": 'dashboard-send-knowledge-article-to-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-send-knowledge-article-to-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '50182dad6e193d85',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/send-knowledge-article-to-customer'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-send-knowledge-article-to-customer', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-send-knowledge-article-to-customer-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of send knowledge article to customer with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull send knowledge article to customer data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-send-knowledge-article-to-customer-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing send knowledge article to customer.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls send-knowledge-article-to-customer data from Dynamics 365 F&SCM for the most recent fiscal period and writes a standalone interactive HTML dashboard (header totals, two inline SVG charts, sortable table, RAG indica', 'example_request': 'Build an interactive HTML dashboard of send knowledge article to customer data for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-send-knowledge-article-to-customer-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable dashboard of send knowledge article to customer data from D365 ERP that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardSendKnowledgeArticleToCustomer(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardSendKnowledgeArticleToCustomer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-send-knowledge-article-to-customer-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardSendKnowledgeArticleToCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
