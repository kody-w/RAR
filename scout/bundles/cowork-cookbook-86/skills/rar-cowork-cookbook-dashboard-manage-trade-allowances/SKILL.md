---
name: "rar-cowork-cookbook-dashboard-manage-trade-allowances"
description: "Pulls trade allowance data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-on"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_trade_allowances", "rar_sha256": "9d40f9a36ddef205cf623f612aa105773f418af3c31be28ab15742eb06b86702", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_trade_allowances`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_trade_allowances_agent.py` and in the RCI capsule.

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

Manage trade allowances Interactive HTML Dashboard — Pulls trade allowance data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-on

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-trade-allowances
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
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the HTML file to write, e.g. dashboard-manage-trade-allowances-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the generated HTML file is saved.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 9d40f9a36ddef205…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_trade_allowances_agent.py` first:

```bash
python3 dashboard_manage_trade_allowances_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_trade_allowances_agent.py   # or on stdin
python3 dashboard_manage_trade_allowances_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage trade allowances Interactive HTML Dashboard — Pulls trade allowance data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-on

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-trade-allowances
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_trade_allowances',
    "version": '3.0.3',
    "display_name": 'Manage trade allowances Interactive HTML Dashboard',
    "description": 'Pulls trade allowance data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-on',
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
        "upstream_slug": 'dashboard-manage-trade-allowances',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-trade-allowances',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '57aacac48fdf0454',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/manage-trade-allowances'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-manage-trade-allowances', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-manage-trade-allowances-2026-05-24.html.', 'output_folder': 'Folder where the generated HTML file is saved.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage trade allowances with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage trade allowances data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-trade-allowances-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage trade allowances.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls trade allowance data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-on', 'example_request': 'Build me a trade allowances dashboard for USMF for the latest fiscal period as a standalone HTML file.', 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-manage-trade-allowances-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the generated HTML file is saved.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of manage trade allowances data from D365 without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageTradeAllowances(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageTradeAllowances'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-manage-trade-allowances-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the generated HTML file is saved.', 'type': 'string'}},
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
    print(DashboardManageTradeAllowances().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
