---
name: "rar-cowork-cookbook-dashboard-correct-supplier-payments"
description: "Pulls correct supplier payments data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the Cowork output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_supplier_payments", "rar_sha256": "c936619ba7f82bb8a9a38965f8ddf372f2c5e9e8c2a16971f52025952681a3f3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
