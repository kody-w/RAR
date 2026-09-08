---
name: "rar-cowork-cookbook-dashboard-develop-currency-policies"
description: "Pulls develop currency policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_currency_policies", "rar_sha256": "ac46bbe868fa56847aa3dc181ef51015412f1ac2a8cd58bb325bae57263a49ca", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_currency_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_currency_policies_agent.py` and in the RCI capsule.

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

Develop currency policies Interactive HTML Dashboard — Pulls develop currency policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-currency-policies
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
      "description": "D365 legal entity to pull from, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-develop-currency-policies-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_currency_policies_agent.py` and embedded as the fenced Python below (sha256 ac46bbe868fa5684…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_currency_policies_agent.py` first:

```bash
python3 dashboard_develop_currency_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_currency_policies_agent.py   # or on stdin
python3 dashboard_develop_currency_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop currency policies Interactive HTML Dashboard — Pulls develop currency policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-currency-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_currency_policies',
    "version": '3.0.3',
    "display_name": 'Develop currency policies Interactive HTML Dashboard',
    "description": 'Pulls develop currency policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-develop-currency-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-currency-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1bd5d1e1125f2619',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-currency-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-develop-currency-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-develop-currency-policies-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of develop currency policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull develop currency policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-develop-currency-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing develop currency policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls develop currency policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output', 'example_request': 'Build an interactive HTML dashboard of develop currency policies from D365 for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-develop-currency-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a browser-viewable currency policy dashboard from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDevelopCurrencyPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopCurrencyPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-develop-currency-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardDevelopCurrencyPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
