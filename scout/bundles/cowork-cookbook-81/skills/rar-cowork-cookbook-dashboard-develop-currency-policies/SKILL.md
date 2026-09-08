---
name: "rar-cowork-cookbook-dashboard-develop-currency-policies"
description: "Pulls develop currency policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_currency_policies", "rar_sha256": "ac46bbe868fa56847aa3dc181ef51015412f1ac2a8cd58bb325bae57263a49ca", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
