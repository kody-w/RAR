---
name: "rar-cowork-cookbook-dashboard-issue-blanket-purchase-orders"
description: "Pulls issue blanket purchase order data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_blanket_purchase_orders", "rar_sha256": "2b36cb2f723b28e32f0007632f58cd69541c67cd550571a6665afed3bdb64888", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_issue_blanket_purchase_orders`. The original RAPP
agent is preserved byte-for-byte in `dashboard_issue_blanket_purchase_orders_agent.py` and in the RCI capsule.

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

Issue blanket purchase orders Interactive HTML Dashboard — Pulls issue blanket purchase order data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-blanket-purchase-orders
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
      "description": "Name of the HTML file to write, e.g. dashboard-issue-blanket-purchase-orders-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_issue_blanket_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 2b36cb2f723b28e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_issue_blanket_purchase_orders_agent.py` first:

```bash
python3 dashboard_issue_blanket_purchase_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_issue_blanket_purchase_orders_agent.py   # or on stdin
python3 dashboard_issue_blanket_purchase_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue blanket purchase orders Interactive HTML Dashboard — Pulls issue blanket purchase order data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-blanket-purchase-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_issue_blanket_purchase_orders',
    "version": '3.0.3',
    "display_name": 'Issue blanket purchase orders Interactive HTML Dashboard',
    "description": 'Pulls issue blanket purchase order data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-issue-blanket-purchase-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-issue-blanket-purchase-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '656d6a78baf74e87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/issue-blanket-purchase-orders'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-issue-blanket-purchase-orders', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-issue-blanket-purchase-orders-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of issue blanket purchase orders with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull issue blanket purchase orders data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-issue-blanket-purchase-orders-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing issue blanket purchase orders.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls issue blanket purchase order data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o', 'example_request': 'Build an interactive HTML dashboard of issue blanket purchase orders for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-issue-blanket-purchase-orders-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants blanket purchase order data from D365 packaged as a shareable browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardIssueBlanketPurchaseOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIssueBlanketPurchaseOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-issue-blanket-purchase-orders-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardIssueBlanketPurchaseOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
