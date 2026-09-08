---
name: "rar-cowork-cookbook-dashboard-identify-opportunity"
description: "Pulls identify-opportunity data from Dynamics 365 ERP for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_opportunity", "rar_sha256": "ca0528e9e1efdadbdd99b94d8c7b24a8c4910821d9a6b3457058867196793a7c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
