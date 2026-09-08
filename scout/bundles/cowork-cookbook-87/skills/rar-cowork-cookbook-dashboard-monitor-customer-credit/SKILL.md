---
name: "rar-cowork-cookbook-dashboard-monitor-customer-credit"
description: "Pulls customer credit data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_customer_credit", "rar_sha256": "e02eda9c3f11bda14baa809029b0c94f48994c49133d4901a0153d1d7f0c1211", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_monitor_customer_credit`. The original RAPP
agent is preserved byte-for-byte in `dashboard_monitor_customer_credit_agent.py` and in the RCI capsule.

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

Monitor customer credit Interactive HTML Dashboard — Pulls customer credit data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) re

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-customer-credit
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
      "description": "Name of the HTML file to write, e.g. dashboard-monitor-customer-credit-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_customer_credit_agent.py` and embedded as the fenced Python below (sha256 e02eda9c3f11bda1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_customer_credit_agent.py` first:

```bash
python3 dashboard_monitor_customer_credit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_customer_credit_agent.py   # or on stdin
python3 dashboard_monitor_customer_credit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor customer credit Interactive HTML Dashboard — Pulls customer credit data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) re

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-customer-credit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_customer_credit',
    "version": '3.0.3',
    "display_name": 'Monitor customer credit Interactive HTML Dashboard',
    "description": 'Pulls customer credit data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) re',
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
        "upstream_slug": 'dashboard-monitor-customer-credit',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-customer-credit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd0961bbe31b78d3f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/monitor-customer-credit'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-monitor-customer-credit', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-monitor-customer-credit-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of monitor customer credit with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull monitor customer credit data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-monitor-customer-credit-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing monitor customer credit.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls customer credit data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) re', 'example_request': 'Build me a customer credit dashboard HTML from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-monitor-customer-credit-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants customer credit monitoring shared as a browser-openable dashboard file that viewers can read without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMonitorCustomerCredit(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorCustomerCredit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-monitor-customer-credit-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardMonitorCustomerCredit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
