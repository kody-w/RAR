---
name: "rar-cowork-cookbook-dashboard-issue-sales-invoices"
description: "Pulls issue sales invoices data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_sales_invoices", "rar_sha256": "b18dc6fffe1fe25f0e8ceb88fe0fb6964545680e43e0b4b89776c8347c619a59", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_issue_sales_invoices`. The original RAPP
agent is preserved byte-for-byte in `dashboard_issue_sales_invoices_agent.py` and in the RCI capsule.

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

Issue sales invoices Interactive HTML Dashboard — Pulls issue sales invoices data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-sales-invoices
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
      "description": "Name of the HTML file to produce, e.g. dashboard-issue-sales-invoices-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_issue_sales_invoices_agent.py` and embedded as the fenced Python below (sha256 b18dc6fffe1fe25f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_issue_sales_invoices_agent.py` first:

```bash
python3 dashboard_issue_sales_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_issue_sales_invoices_agent.py   # or on stdin
python3 dashboard_issue_sales_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue sales invoices Interactive HTML Dashboard — Pulls issue sales invoices data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-sales-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_issue_sales_invoices',
    "version": '3.0.3',
    "display_name": 'Issue sales invoices Interactive HTML Dashboard',
    "description": 'Pulls issue sales invoices data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-issue-sales-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-issue-sales-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '12e92936b80dc6ac',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/issue-sales-invoices'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-issue-sales-invoices', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-issue-sales-invoices-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of issue sales invoices with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull issue sales invoices data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-issue-sales-invoices-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing issue sales invoices.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls issue sales invoices data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to', 'example_request': 'Build an interactive HTML dashboard of issue sales invoices for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-issue-sales-invoices-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants issue sales invoices from D365 turned into a shareable browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardIssueSalesInvoices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIssueSalesInvoices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-issue-sales-invoices-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardIssueSalesInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
