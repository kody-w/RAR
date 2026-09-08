---
name: "rar-cowork-cookbook-dashboard-correct-supplier-payments"
description: "Pulls correct supplier payments data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the Cowork output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_supplier_payments", "rar_sha256": "c936619ba7f82bb8a9a38965f8ddf372f2c5e9e8c2a16971f52025952681a3f3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_correct_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `dashboard_correct_supplier_payments_agent.py` and in the RCI capsule.

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

Correct supplier payments Interactive HTML Dashboard — Pulls correct supplier payments data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the Cowork output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-supplier-payments
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
      "description": "D365 legal entity to query; the recipe uses USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-correct-supplier-payments-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the file; Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_correct_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 c936619ba7f82bb8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_correct_supplier_payments_agent.py` first:

```bash
python3 dashboard_correct_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_correct_supplier_payments_agent.py   # or on stdin
python3 dashboard_correct_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct supplier payments Interactive HTML Dashboard — Pulls correct supplier payments data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the Cowork output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_correct_supplier_payments',
    "version": '3.0.3',
    "display_name": 'Correct supplier payments Interactive HTML Dashboard',
    "description": 'Pulls correct supplier payments data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the Cowork output folder, read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-correct-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-correct-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5dec1a40f4e59802',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/correct-supplier-payments'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-correct-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; the recipe uses USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-correct-supplier-payments-2026-05-24.html.', 'output_folder': 'Destination folder for the file; Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of correct supplier payments with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull correct supplier payments data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-correct-supplier-payments-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing correct supplier payments.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls correct supplier payments data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the Cowork output folder, read-only.', 'example_request': 'Build me an interactive HTML dashboard of correct supplier payments for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-correct-supplier-payments-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the file; Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants supplier payment correctness shown as a browser-openable HTML dashboard with charts, totals, sortable table and RAG indicator, no D365 access needed.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardCorrectSupplierPayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCorrectSupplierPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-correct-supplier-payments-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the file; Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardCorrectSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
