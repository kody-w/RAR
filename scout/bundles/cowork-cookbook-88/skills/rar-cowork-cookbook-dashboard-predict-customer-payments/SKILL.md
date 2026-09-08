---
name: "rar-cowork-cookbook-dashboard-predict-customer-payments"
description: "Pulls predict-customer-payments data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_predict_customer_payments", "rar_sha256": "a88a7d1df31feee14745e10002ec077554aba8696b371ed67b7be834f55a412c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
