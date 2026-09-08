---
name: "rar-cowork-cookbook-dashboard-process-customer-refunds"
description: "Pulls customer refund data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_process_customer_refunds", "rar_sha256": "5adf32de84e7f85d03da60908f174e56e960724c17e9ce470d4c09abbfba72db", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_process_customer_refunds`. The original RAPP
agent is preserved byte-for-byte in `dashboard_process_customer_refunds_agent.py` and in the RCI capsule.

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

Process customer refunds Interactive HTML Dashboard — Pulls customer refund data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) t

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-process-customer-refunds
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
      "description": "Name of the HTML file to produce, e.g. dashboard-process-customer-refunds-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_process_customer_refunds_agent.py` and embedded as the fenced Python below (sha256 5adf32de84e7f85d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_process_customer_refunds_agent.py` first:

```bash
python3 dashboard_process_customer_refunds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_process_customer_refunds_agent.py   # or on stdin
python3 dashboard_process_customer_refunds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer refunds Interactive HTML Dashboard — Pulls customer refund data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) t

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-process-customer-refunds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_process_customer_refunds',
    "version": '3.0.3',
    "display_name": 'Process customer refunds Interactive HTML Dashboard',
    "description": 'Pulls customer refund data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) t',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-process-customer-refunds',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-process-customer-refunds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '702ee3fe66fbd3b5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-refunds'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-process-customer-refunds', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-process-customer-refunds-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of process customer refunds with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull process customer refunds data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-process-customer-refunds-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing process customer refunds.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls customer refund data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) t', 'example_request': 'Build me an interactive HTML refunds dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-process-customer-refunds-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of customer refunds from D365 for viewers who lack D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardProcessCustomerRefunds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardProcessCustomerRefunds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-process-customer-refunds-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardProcessCustomerRefunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
