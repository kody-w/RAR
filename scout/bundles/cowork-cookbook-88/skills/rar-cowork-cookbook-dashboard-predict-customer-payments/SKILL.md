---
name: "rar-cowork-cookbook-dashboard-predict-customer-payments"
description: "Pulls predict-customer-payments data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_predict_customer_payments", "rar_sha256": "a88a7d1df31feee14745e10002ec077554aba8696b371ed67b7be834f55a412c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_predict_customer_payments`. The original RAPP
agent is preserved byte-for-byte in `dashboard_predict_customer_payments_agent.py` and in the RCI capsule.

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

Predict customer payments Interactive HTML Dashboard — Pulls predict-customer-payments data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-predict-customer-payments
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
      "description": "Period to report on; defaults to the most recent fiscal period available.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-predict-customer-payments-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file (default Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_predict_customer_payments_agent.py` and embedded as the fenced Python below (sha256 a88a7d1df31feee1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_predict_customer_payments_agent.py` first:

```bash
python3 dashboard_predict_customer_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_predict_customer_payments_agent.py   # or on stdin
python3 dashboard_predict_customer_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Predict customer payments Interactive HTML Dashboard — Pulls predict-customer-payments data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-predict-customer-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_predict_customer_payments',
    "version": '3.0.3',
    "display_name": 'Predict customer payments Interactive HTML Dashboard',
    "description": "Pulls predict-customer-payments data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder",
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
        "upstream_slug": 'dashboard-predict-customer-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-predict-customer-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e9d2ea01acad3de7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/predict-customer-payments'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-predict-customer-payments', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Period to report on; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-predict-customer-payments-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (default Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of predict customer payments with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull predict customer payments data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-predict-customer-payments-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing predict customer payments.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Pulls predict-customer-payments data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder", 'example_request': 'Build me an interactive HTML dashboard of predicted customer payments for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Period to report on; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-predict-customer-payments-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (default Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of predicted customer payments from D365 without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardPredictCustomerPayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPredictCustomerPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Period to report on; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-predict-customer-payments-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (default Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardPredictCustomerPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
