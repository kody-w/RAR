---
name: "rar-cowork-cookbook-dashboard-define-order-risk-management-strategy"
description: "Pulls order risk management strategy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_order_risk_management_strategy", "rar_sha256": "9b88ffaba199b76e9ed157506b61c66f65e32ad09aca9deb396c2268a4f727d4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
