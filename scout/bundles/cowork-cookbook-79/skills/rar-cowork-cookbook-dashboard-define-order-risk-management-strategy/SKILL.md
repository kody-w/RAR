---
name: "rar-cowork-cookbook-dashboard-define-order-risk-management-strategy"
description: "Pulls order risk management strategy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_order_risk_management_strategy", "rar_sha256": "9b88ffaba199b76e9ed157506b61c66f65e32ad09aca9deb396c2268a4f727d4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_order_risk_management_strategy`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_order_risk_management_strategy_agent.py` and in the RCI capsule.

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

Define order risk management strategy Interactive HTML Dashboard — Pulls order risk management strategy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-order-risk-management-strategy
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
      "description": "D365 legal entity to pull from; defaults to USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-define-order-risk-management-strategy-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_order_risk_management_strategy_agent.py` and embedded as the fenced Python below (sha256 9b88ffaba199b76e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_order_risk_management_strategy_agent.py` first:

```bash
python3 dashboard_define_order_risk_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_order_risk_management_strategy_agent.py   # or on stdin
python3 dashboard_define_order_risk_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define order risk management strategy Interactive HTML Dashboard — Pulls order risk management strategy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-order-risk-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_order_risk_management_strategy',
    "version": '3.0.3',
    "display_name": 'Define order risk management strategy Interactive HTML Dashboard',
    "description": 'Pulls order risk management strategy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the output folder, read-only.',
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
        "upstream_slug": 'dashboard-define-order-risk-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-order-risk-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '03e6174980d4bd25',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-order-risk-management-strategy'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-define-order-risk-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-define-order-risk-management-strategy-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define order risk management strategy with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define order risk management strategy data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-order-risk-management-strategy-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define order risk management strategy.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls order risk management strategy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the output folder, read-only.', 'example_request': 'Build me an interactive HTML dashboard of order risk management strategy from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-define-order-risk-management-strategy-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable D365 order risk dashboard with charts, a sortable table, and RAG status that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineOrderRiskManagementStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineOrderRiskManagementStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-define-order-risk-management-strategy-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardDefineOrderRiskManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
