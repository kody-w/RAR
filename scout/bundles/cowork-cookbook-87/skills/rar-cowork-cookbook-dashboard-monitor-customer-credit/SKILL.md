---
name: "rar-cowork-cookbook-dashboard-monitor-customer-credit"
description: "Pulls customer credit data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_customer_credit", "rar_sha256": "e02eda9c3f11bda14baa809029b0c94f48994c49133d4901a0153d1d7f0c1211", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
