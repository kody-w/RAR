---
name: "rar-cowork-cookbook-dashboard-revalue-currency"
description: "Pulls revalue currency data from Dynamics 365 F&SCM for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_revalue_currency", "rar_sha256": "39cb50d756a4f89d03814604c02771cf5e179f5b819c87d86fd6dc8b58ef5be6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_revalue_currency`. The original RAPP
agent is preserved byte-for-byte in `dashboard_revalue_currency_agent.py` and in the RCI capsule.

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

Revalue currency Interactive HTML Dashboard — Pulls revalue currency data from Dynamics 365 F&SCM for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to t

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-revalue-currency
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
      "description": "Name of the HTML file to write, e.g. dashboard-revalue-currency-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_revalue_currency_agent.py` and embedded as the fenced Python below (sha256 39cb50d756a4f89d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_revalue_currency_agent.py` first:

```bash
python3 dashboard_revalue_currency_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_revalue_currency_agent.py   # or on stdin
python3 dashboard_revalue_currency_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue currency Interactive HTML Dashboard — Pulls revalue currency data from Dynamics 365 F&SCM for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to t

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-revalue-currency
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_revalue_currency',
    "version": '3.0.3',
    "display_name": 'Revalue currency Interactive HTML Dashboard',
    "description": "Pulls revalue currency data from Dynamics 365 F&SCM for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to t",
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
        "upstream_slug": 'dashboard-revalue-currency',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-revalue-currency',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9a56b54092ec1d70',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/revalue-currency'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-revalue-currency', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-revalue-currency-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of revalue currency with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull revalue currency data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-revalue-currency-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing revalue currency.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Pulls revalue currency data from Dynamics 365 F&SCM for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to t", 'example_request': 'Build a revalue currency dashboard for USMF for the latest fiscal period as a standalone HTML file.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-revalue-currency-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 revalue currency data for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardRevalueCurrency(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRevalueCurrency'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-revalue-currency-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardRevalueCurrency().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
