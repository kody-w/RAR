---
name: "rar-cowork-cookbook-dashboard-revalue-currency"
description: "Pulls revalue currency data from Dynamics 365 F&SCM for a legal entity's most recent fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_revalue_currency", "rar_sha256": "39cb50d756a4f89d03814604c02771cf5e179f5b819c87d86fd6dc8b58ef5be6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
