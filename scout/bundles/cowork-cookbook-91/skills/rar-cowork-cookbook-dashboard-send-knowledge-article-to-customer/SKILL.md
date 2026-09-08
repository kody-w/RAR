---
name: "rar-cowork-cookbook-dashboard-send-knowledge-article-to-customer"
description: "Pulls send-knowledge-article-to-customer data from Dynamics 365 F&SCM for the most recent fiscal period and writes a standalone interactive HTML dashboard (header totals, two inline SVG charts, sortable table, RAG indica"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_send_knowledge_article_to_customer", "rar_sha256": "d1cd7765cf5079f6eadac31ddac4826dc53b160b6bd6fbd1703dced46f2c390b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/91657LjRpbmq3DvRKykQVWBhGd1TMTSACAIwoMECJWiBO8NYQij0btvguQtSd3q6dXs/lpWXcJlHn++c5KJX97sro3K+u3zm+bbxYK1syyO/HphF95iV/ZlnYJDmTrgb+GWRVvHTteWdfP24c3zG7eOqzYuCzBd7rKsWTR+4X1Mi7LPfC/0P9p1G7uZ/7EtP7pd05Y5oOzZrb0I6jJf7MfCzmO3WaAEvmD+p7YTFkFZL9rIX+Rl0y5q3/WLdhHEjWtni8qv49J7CNbXces3C3vRtODSzsrCX8RF69e228Z3f3HQhRPg00ROadfe4vvItz3AuS1bO2s+LNq+BMOzGMzSLuzCjYCY4HZT1q3tZP7i8f1hoW5YMMyLXRso6w92XmV+8/b5x58+vMXg/O3zL29uZjfg1tv+nZcG9Off1d88tdfL3Ut3QCezixBMqEZg9QJcA62Azjm45fnB4nX1feNnwYfFv/972tt12Pzw+UuxeH2+vM3/1K54mKkt7ab1vYVrV7YTZ3E7flpsst4eG2C8tquLp5HquAg/PWf+RqmsFv8xP/v+yeRT6Lfff3krgQj27NIvbz8sgDO+vNXdfP5pplJ9/8OnrOz9+vsffqPTdE7iu+1MDEj96evr+kUWDPxtaBwsvmoyvXvxAv6NKx8Q/51+8+cp+ovcyyRfn4O/L6sPiz+nPOvzH0DeZ1g6gO6fkwU2ADPfPiVlXHz/4lGXd7+wC9f//od/RtaNfDfN4qb9P6L745PwM/C+f5nkhw8P9/20gF66faP5z9lWIGD+iiZg+Du7b4b6Z7Qfnv070nNWNN98+afk/mwC9B+LH/+pbv/VhA+L4Mvb3s9A2tZz2n1e/PIIkR+/8367+d1PvwLS/5KMVna1+6DwNbeLOPCb9uvXH79rHre/++nH77oKRLFv51+7Ovszmn9m1wefP1jwNer7P84F/M/FjHzF4lsOLX4pq/9R//ppcbGz2PvtfvN58ftMnD/QYlbinenTBL/LxgbI+js7/vD2KwChAmjTuY/HAD/+7d8WQuzWZVMG7UJzyw4AaFe0ce7PwutR3CzA/xk1ah/YtYlnqHuOA/E/e3iWuAwWP/8v9wH8H90X8MPfoPTrjO9fv+H71xe+f23Lr+/4/vOnhQ54lHUcxgWAbXUjy18KO5yRHPCvar/x6zvALGds/Y8gtT/OJwBoFz//FTZfHxQ/VePPj4oQP/FQ3XEzFjZd5n+atTYiv3jp6ILq5g++2wFmWTkXlCAGeP4BWKMpM1A02tlCTRpn2cKLAdqAKjc+aAMrfp6J/fzzzw6Q8EvxBG908Sx/DQwGfBNn8fEjUDHI4jBqvxS+G5WL73759bvFfy7+q1kP4jMPGdSTl4+AhEdNEhcg57ocDAPuAw4HgPLw0S+/vgwNyBSgtgGPxkHsPyeDmE19793q2mHzEcGJheMDawNL5xUodKAiLOL204ILFt/kBUznR3PNiOb66/kV8INfuCOgagN1vlmyKNtFAwKzCcYPi67xH1x/dmr7IWIOkt9uf14IOxlUqDIDX7OYj0FgclmAkpp9i4nnfUCk/q5ZbN9JfFqIc5QuKru2q6i2XzwC++kXUJnepwPi9qLw+y/FXJX92VSPlHmaBwwClnFfLv04+xz0MTnAB6955/0YY891VH/U0/pL0bzSwa5nV7igPACmYRd7c5H42yukmqjsMu9hP//Ztry84L288ojBuSVYfIvlxSuWZ5t8a4m4v+9dvvUTiy8dslxhi/+fu6vZSBuWVWl2o9P7BS3q6vXpvLnhnGV89qigu3lpABL1t47nHdXewf0L4A0isR7/9hz5cPlrzBMwuxp4SN2oD/og3oDwM91HOszhXddzIgG53qvIB2CMB2SCiADYAXJrdt87w/npu6QRMMt8/VtH8Qif+mFZEPKLqnMyEI6B73uO7aZAqnpO6Zebi9nWIL37KHajP2i1ANRBCAL6CyBEDJIUVJpP35D9+fRd9D9MfDZO85RHU9kVs7NmAkAOfxbw4fO4BcBmt8/+Huj5+UEEqJFX7ay7A3IKaPq86df+rYubOUw+vOzqVwDHP87Hp6bzXX+oQBoBY4FkqTpg3Ud6zciTg4gBMgCEAWGVxwVoE4BRXkZ4ELTzGSsAFr/62CfFx+2XQv4jJ+f69j5xVmSe8wizRw7Yxfh7SNH/LEwAvXwe8eD795H2jdtMe4bVBkAj4Pj+9NlbfHq2B8/+Y/FO9/M/LKC+/2trrEfBP/8xAD4voratms8w/CzS7zX6EwA1+Clr81u9/vivEeMPPJ7qf178NTn/QOKVJ58Xq0/LT8v50ekVZ68PMMvu4/b6EZuffilU/zf4BezLHATa7MQRNAjfauX7EFAww9oP58HP2tnMJbcHVf5RLIBHvhS/D/w58QAAFaH/QKDfAcKjaQBJ8HTgt5oGHhUt4O3NrWfof5pXbLP4jf/2uQAY/OENgKr/l1Z8cwXL5zhv5hUjyCgAtW3sP64esDG08+kfV9PS48TOPi32PoCorPl9LL7qzlx3f5cyT3WBmi7g8GEuBAAJQJgCdWfmc7rZDYhfELqzWu1YzXo8F4dzO/ksBF+fheAfJVL997bhOeJvIHkDu8uADdvyX1WVO1Bhzso/ZZwBh2ZfwSyQdv/Idz+Xr8eQxXPIzO7Wgdz/sPA/hZ8WZ01g/pTut+b5H4kaoD+Z6Xjl57lUf3gBHTiCBc+Hxbe1CzDjazU5c/CLDizUf5zXTbNfH1PmEzAHHL5N+vbTiOO//fRncj3Q8Oschs9g+nvpxBnlQBX4Y2/yKLvzpJfefyXJPyJLhPi4xD8i2KeozbM/t9dLrjIDFeIfpWIe9+dkq5+92DeB5ura2KCnf0m2L91nxwo/UQN+Uob/hCtg+6gloCLPlv3NZb8ZrnysPmcBgaHb548lv7yBjLLnXueVU6/lCxgOoPdjM7dnMAAgwBBcP6ECPPu/Wti8aDWRDZrp+fealeuRJIG7Ab4k1wEByrjtoisPfGMUQngujjorYukQjkcEjrcil6jn+h5GBIiLrpcOoPcEn69zPxrP8s3CAbN8BPjl//YY3PJeij0Vma32bR01G+Cl3y9vDoGBkQes4TbPzw5erxwCPTlq5UATEZTDRWlHNdU8aRjsyvIdyjAcbl1fl14mWRlvX8J+t1eP6m5jK4qkdVp1mc6yQFOETh48SSQwWvVyf9qdu6PGb8lWKiboTGYIhieJgGXLtDxF4urgtv3pagT4hVY0nK5pVSEuq86KPe94SgR45IWaD0gMbhAUa3UzJ8yxWe0pUlvDjOExB7aLFMOzl1ZmS63o6lpDlBZMXiujqvXEOwYYsqtVbC1fEirg4GkJ+/HR5NUToV5v7fKUcNa4U8zbMjwE8aDl5/ON2WPXu0vEJltHOxxNbgNUq9ytHFf4tdEDW9vD9FgXPHyJZPVAtMJ+lATpTkUrN0a4rSiL19sILzPSqiF5ONyLGt01+w0PC4cQsVuTXBGUf3egwc4wKnDW3bD2KBV3t+HtFKYSPO5dXpaWDYzTRmjBxDjGuQVHrDFWWmEEGtqTsX0scMQnjqwT8w3PeWHIMOnWt/anAyaNzj2kOmE82zi/IgvuOGS0sYIa2dDt3WUll3RY51rO4QZnbAwz3yDrzL2rCH6S92d1h65FwXQLWu+PRyG7WhpqbHDqPCYhP6TJ0YUaOvM3HFOuCdriBwMrSn1r3Y0gVEpr6uKTu91kkmx6Pidtu3XlQZY3mmLNAhed01S3TqMd77iI8Zhls9sdRc9aZizFBhVeLJ0T17g0vuz3MDJpha7Ba1ngjOksWaMFnbSj2Op8T1l65ZE3Z5mTHreHzMNlc8UjXuPl3TJcyQG/QvNzLZyNS8hJ6i6KtLYp42CDYeJyEkzqlATtsBeIqFwq8u3mIfzACaSiXNNkPEJ8MDiM2FAHYqQparptFcG5Lo8gynbt6boMj0GDZMaKrlgWvuC35srIFwNa8fVxo9ytXSGLh/OF9+JBXNXO8QQzvKnBfaF2gaZTSk1tvZY7xDGyXe2sRtpd8NQPIQd1rqg8aI58npBgUnifFSPcue0QgZLKIrv40n4p7d1lNolOgbUS5jB8f0po0yRTGd14GEUgKx5uZC7JLfm+HqCiow6nUbf77EBRadecwOkN57ypG9BN6lkMaxOrFB9k2SSWY2frG0iJEls3g35/GqH0Nh4VT+ZHB9oIbmYLTbhEjwSiDNZ9vbESTeUvO2xlalciU5Ct1ZZX6KDtl70s8hHsUtRFd/dsqCchhgjbqDhVk6CvhaqZ5H1SIUdfgejMDElYANjKlLfbxRZUrB745oJdEsav60ETzuJp4m5nYo/szlvoMlEiV5EsTFE1c49j+0JrWeq0HiW6rkmVLUsIKH3vz80IFziM21fYYWgWaJVPha2eJyfEimsdNiKTaEgoUtt7JE79qC1vfp/V1HVb4/mGitK0352uu/t+d7SCIIP3nD/VS652QjJc57a5j4xz3cvxCiyel6CFceMOCXY4tass75AmrgyLobGziPNmSMz+2hTpeLdRghtTVUc2vMe6/KGYkiDdnqSsJuSNz1tJBONswZyHaTgHDg3sGEZSbkKbnbshm0nZe3Cr7u4kGZ2Wzj2/HZ0zC6KxT0LWXUXsjiFUTWIv467dwkzU2WMs8co1166qfXfbgDzVIZwnOuUIRBJuXTiwMMNdSbDg7yg+sbe2nKDuYeURluARfno1jHO/J7H9Er+pmlwRUjyZIjRoLjleloGMyjstX2vTJUxYce8Om+Kwrrl608uyDx3VWuOhRKNJjjnroLfLbsKWQDkuOeBFX/hWQjE3PSVpaqAYJqKTvdX3gkvLga2gmdxxaodNYpQzu7Zw0XqASLxslpplLlMvtnJludpbTF5oE9fcaFGUq4pmLkJtoDW3srYizKVjCKW5dKxP2+MuVWwENYJesHXhaOVbd4cOEobG8dElO+pWoZxX0ucKlJI1Iu5J9taY2tpGt6HdnRRd0rMaEZg7ayd5orIFQvqdziCwbA6bjaUfL8jOV/C7VNIl6sJEqLUekixZSWbYKMfNBD32y/OdRa+K2iYjv/FlOLnt+/Vehgc7uF+ChOJg+WQhlubijJFME0fhxrAJ9zWXnTYb9DQw/nHHtC1TMYpKg1gMyGY77HXrsva77e3UYnHYHcS2CQe1uNP+VXR3ESTZTMhgF3EDHZUQ5RQujiy/uu057nw245BMLQ4tGzYUql20vG6Hc3ZP0luwdaKYuOhsfi5adJ+pfnOtuanG+rJH08IVCxTSsCxAOrqlavw8wcGSb3w8wUSD3ujJ4U4I6TEWYlD9TW+/z7bx7kC3hjIU1QiJAV0O5roXeAuo0ulKdA0weuQxXO2ZOPDJ1uRI2vSVmIvrAhITcWuHQqLmdLGh1t0u9W0G9yT7TrW8HVASs4t46iAW+uXuXgIyl+XtpWoOoWXpQJNkuw17GmbG+Kifyv3+pKdZeN7s8OyuxHGGexN9DgbXgQd32HP30Dh7qQ5t0hPOMp3e26N+xGqDgzXuKFZX/0Bvopa/qIk04fIO3mlcZuX6XhwO6SbeyGkuni5ZW5vscJ68hmmb6y4bxC07moPnx1BWrIRbt1N7Kzcd+SLc2OsWlrUVo0DaLlHQJnN6jDMbfXnZrcYkNU9mujoxvO/tm+ue3i6nQhRrI+Tj5bXjiGMbRyAvee8wQclROWDCcXdiAG+jMceaqlwekpt4XG1wQTOS+FDv7hxfnHmCxokDq+rnQYjOGK6UenM2Ma4U7BUiV4d+NdiKyu/h2womeTfeHDIVmXiWpiypu3UjrZ+3qsfXLNVdnNgxm/W1P2JWUWVtB/FWI9Dx9pSPq4S0DT7cIXkIp/T1COCusMa1dIr6CWVSKrSOp6FkTrcTbNvj3tjXOarYAnLbqsJJYXVV2kpHJdL8Xic8hl1qWZulDE7fNnyvRks2z47IWUxSVGEmJTDdpQApQuVwliLguM+f1aHayEZDU2gW+L5wiIRNHh2EPXc1DpyNMDl9ZsPRIxztZGhL4jiULWpRXLitLUlvOgWq0ON+tVHDQVjXk1Xk0/ZC9odqS9PH067Lu8rME1i5IqV8WJ1uucMU+0CVEbiHCh6UdksKEUZYC2JyIhUWgjVIrbZZ2fWj57rRRW1SeFQ8nHWdrQ8WF8xygnyhPxGX45XZayCBLizZhJx2PJ7j63JjM8vWRTUii5UBwvN1u9+zQ0E608HzoaAb+TMuamLSbjTQDV62AqdcjP1YKTcNQIG71yIpSshQGXtBj/WqIYx6pFbj1cTFwrhbUOUb9513PPSRNJlyEW15iA4n8Wh2KlXnPLrl0tzUBPdmIpvrsmymfFAgxj+HtKRbQnTQzfqeQLCwOnHL0WjSgOeOcTQa1NHzt85Ag7bpRm5tK86oXbH14brvXele9ZSvDzCEtmiKkPGqKSsVhAhxglP9YhJWY7c3TSljpIa08oKSKY9gDJ+dLqPT5uEpQOi8Hlh3um3qJT9RnS/dg3M8nEcRKJvsS91SeGO8ck13qRJWOzOH62U0Oi3VSd83mD7drrMzs7n3mF5RN2O7Lzb3My8UzqZiPeUWlkwmWB4a5joK0TDSJac93VfokDnIcFbsAdpTunyFQ9w+IcFRJVGkA0jB3GrPvuIEhLPrCdmbHHthMWY4KHJgVdAKZqFLZ4SrTXncIbdehFunNWn5TmmXKL6mVquZoxtjRolMXe6xSkWc0isUX9oEyS2aXK/3V36f37f2+XK+K+LKQvH0eK+vh5ujN2oZO2kq+QoPa0t0L9PThmf4XabvQP2IbWysNtrKWfuiMBik7TYJSucqxfY9P6DDkr41cb46XQ76lfDicASFZLvRz73BxUvc0bb0lWO1oq9oLDKkCduUzGrYuuNKEu+xR2TCmEaNXYy01Gm6t0ol3GFu9yuWtbgKFl5NvytldSW24XbKkxNfZ7mlXoNkG6AsivWGLt3TcHNIshggPUjITEDyqPYQw6an9XY9OjzHb8OmVBudm6SbKxnlNJJhOB1PmHdJXHbtJg5CJXlGDeQ4rXaD1hPBGYWEjiB7NgstFpGKlVsi57glmAS7eebyYhtlAkdrHD2wd96irYsqXA2UV5T66EYH/rZMj/Khh+pVr7LKSuIvPVphNgRx59VmP/mn6uxj/BU1DFr0CohoAocKLxxr9M7t6lamNGSofi0dy74IkwepMIyPsb5TbUMpzOUW0QKSom/MOBaGvKqDVB5znI/qGr+o61OAwXSFeMd0lXh0im32uekSqHy2CF/fjhqylgl6yjp8DeH6vPkHCxoA9JwY7m51tc5byoVGRXZ4OktxN2K2cTadrdWOHpELOwiiEOd7RVl6APFchPBd11lhBaxaNru9wNF5d4+hi6xthLVxGi4VnzlSGFyYO2GSzFjGRCJezVJbmXRQqCbkEHllLS2VXBvHiyeVZIZeo1JPJH6bIrGk32omTNYeE5i6Zl9YPOAcG4Gz0tvfbPNKRvIldfchsVIM3J4XiPzJsq/rI4TqGe2A1DJrNTjV5WSMflZcc9Fbr3Dz4GimEnhSAd3QTLiHKWEw/t3O/VEu5eFq1Ske5I1Ro92VShuzQcxg2Ks2sofItb+872R3fUM9HttRnDmh9A239gfoDNPXcWvwSe7R5XRzod2ZVUVVNNiQUVua4kCTkA+w17NqBJ18zKTk8b5EXcY1/Dt8jtm+g0Gj18NWDyHKntzUg2l7rX6Y2tB2N414uJIuY/WWg+Sb5aEN2fUahqAooEqJ588wF1OwGWA3d4smDoacnBXuGEFtnvfDLqVNt/TWSssmEXLym3tkHjkoFwUevukaf9gQtUF293AHlY6mcj4eQ5swHTB1kyQiollwZYujzdxQYZJzP25WayEQkeWhuMZpmTsO6CurHs0lMdSw0RL78TAVVKG14/VSXEFdW3fjea+xvGnCU+J5wNHStUgoiDP0Zq87VSMY5w18ZHMKIM1V3oI+cyIrpLdJwsCIGM1Mc683xEVUCSMK3FqFsq0+ZmtDRq5OXaGaY230Y7gFf1gQSJ3UkcKERVXIcWJrEwNtZBeq4WFHAE22MWLturSqoVLK5n5mEgmxUn9a55m3jtirK8CCLhRJc6L0dmhMnu4EVjLo7KxcSi2m2C1heMtq2xi5om2LhBFOZLUaFCTrjlZnsZglHAyaoZ1Vqp+ZqVS2js/XQ2kPNEkiVqwO9v5O9mKup/zoCsuyO9l5EYyYLx8SbHm4eBTG7rCIY+okozS3W+/OhFioeHxRginlJPygYoZ5ESO4aqTL1VGcDiizorCp54hlJ5Gd76QVwZI7klZEjL246y2o37JmaKOtZpnni/XJrYUN3poSDS3XlWBAnULaQp1Vk9og9ErcFSJzsbDd2uFEFMOIvgtvVAABSZ1o1LvaWRX9VSSo5SWCbqGeFwKyOhdjdqGH+qCzAHzXh7MKMS2vc4Ko4BB7xTqjtPy73w/UwG9uJyLq1vo0lHi08TWZTKmbll4vacBgrqCq69RcSWGRqatmyNVLd91QPRnUO3ZvQyKxWq9Rz9eNu4+S1WQWeXRB9aafpqBY1xnKs6Qe0VMN+x0iy9HGNGppKycSaeapfD0ekXV7v7hm7+qDtA4Qqe7Ce2x6k+3pcu2dEqIl8rQ1m9KAL4wv8M6GlRnTNu94Z4r7rrWr9cAnWuvalrdUD80ePaCWzDpBIsGBsfcvKp77jh6ioxVa6vbWTJxfHs8nYkA5BMN3tJXJiZGQxXKKC2h9FzY8wqhaBGkOfb0t6/HUhOgWwdTwFsn0QSgNSaqp8mqHo0reXMW32AxisktjxIRFU1i6x5qxR8j8SF3ykdAQ3WQxAxUvUb6tzBb0LscxGOv79bYOTggaIdhGPLgYDh05jlfZba6iG5Qoh/Vt3wT3aOTGMVstS/iUIOSU5OqaRZggy9TusNXau12cS3gZXMf0dLwnSlJjwyYZrLtT5UiVHUTcJi4tO7Z1oVPFJU7bkDS7q5UmEHq6Tsxtn8fX6XB322Q7uYQutlMmy5CH1bnfqK2d0SirmGsvHXc3idU3RH7HULfFUcwKfQ3NiMEQ+eCIbW6tDlox38e3HKQhTXBmlseGIGzDUmp51Nu93snnO5dSYEFZG/iy3ngrogu9TO/AumtdEy461lkZuB3pnq6SBFfCxB/b6zZVszg5q8QJPW2OWC+wnWsMsA+7d5xWh3p5QaslHNDsZYfbx2FNIgjWrfT82qEdngWiYK6r87ak7jfIAB5v0VOeS5hPRIjoLR0dkW56cPJKG6xObPa2Zbw9j9RTkJ0aCEL4E8JNylrIusZvTxOSWAW5M/FD2iY7kdldJ7EopbvXkXk2BcGVbqeboAQux0qaAfURHRZnKba3eFwQ6EbaK7XLngLnKHZTOqnLPMk20PzLUNWvPcxJkrrLlvdyu+alqmyjW3WgjDz0c405EV1JjjbkpmQ9LlerlZdT+SGiA2JZ05RHQYpHZvaJh8vltiXW3nqHY/Q+uG/wCKFukYOM5jmRvOTcSksmcW/wlRK6+32bEFIfhBgMKBOTURu7uvfJ3XTLnE60USETKYMy5ckR+aGV86veeDDkxZTYIL7t+2vRdsq7B6F3T86KAe1PEYfpEB1PR5rerPgVxd7cI4D92OdvPLf3jBWqEq4ExXWZobWjKUD2waGqgkNCkjOQtCxlcguB4mQok3T3NQlXTNI71A41IrRNdih8vq8qiTl0vONTtucU9H1yxS2u4PwW6Si0XgpkeLPWSxYbrOX5FvP5QWFESVddUnRXa6yD4aHGxN0WxXaRFOCuGHh0XlL6VIsnrF5WhzWJ3oWDdWr50AjYmvKSCQsgq3Nio1L6zeZt3jx938x7+2+9xTbv9vw/21h67g+9v4Dy2LEEND4/eH3+74n304e32o2BcM9NtSbrwteW1N9tqX38K9uSM6Xx+cLY+0b4c5O9tcP5Teu3uPDA0Hr82pTZ47UUMMPpmvmVzGZ+a9cFx99vxX5jPu/H2s1Dmcf7fe+TH+8x5b4X263/ugxfO45g9uuNqa8ogX/162rW+vU6A1AW/bT8hL79+r8BkcJAdDIvAAA= -->
