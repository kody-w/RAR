---
name: "rar-cowork-cookbook-dashboard-identify-opportunity"
description: "Pulls identify-opportunity data from Dynamics 365 ERP for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_opportunity", "rar_sha256": "ca0528e9e1efdadbdd99b94d8c7b24a8c4910821d9a6b3457058867196793a7c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_identify_opportunity`. The original RAPP
agent is preserved byte-for-byte in `dashboard_identify_opportunity_agent.py` and in the RCI capsule.

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

Identify opportunity Interactive HTML Dashboard — Pulls identify-opportunity data from Dynamics 365 ERP for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; re

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-opportunity
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
      "description": "Name of the HTML file to produce, e.g. dashboard-identify-opportunity-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_opportunity_agent.py` and embedded as the fenced Python below (sha256 ca0528e9e1efdadb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_opportunity_agent.py` first:

```bash
python3 dashboard_identify_opportunity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_opportunity_agent.py   # or on stdin
python3 dashboard_identify_opportunity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify opportunity Interactive HTML Dashboard — Pulls identify-opportunity data from Dynamics 365 ERP for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; re

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-opportunity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_opportunity',
    "version": '3.0.3',
    "display_name": 'Identify opportunity Interactive HTML Dashboard',
    "description": "Pulls identify-opportunity data from Dynamics 365 ERP for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; re",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-identify-opportunity',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-opportunity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c7e77a6c431cb336',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/identify-opportunity'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/dashboard-identify-opportunity', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-identify-opportunity-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of identify opportunity with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull identify opportunity data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-identify-opportunity-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing identify opportunity.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Pulls identify-opportunity data from Dynamics 365 ERP for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; re", 'example_request': 'Build an interactive HTML dashboard of identify opportunity for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-identify-opportunity-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants identify-opportunity D365 data packaged as a shareable browser dashboard for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardIdentifyOpportunity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyOpportunity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-identify-opportunity-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardIdentifyOpportunity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
