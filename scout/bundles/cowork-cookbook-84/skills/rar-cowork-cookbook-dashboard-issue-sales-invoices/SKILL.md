---
name: "rar-cowork-cookbook-dashboard-issue-sales-invoices"
description: "Pulls issue sales invoices data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_sales_invoices", "rar_sha256": "b18dc6fffe1fe25f0e8ceb88fe0fb6964545680e43e0b4b89776c8347c619a59", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
