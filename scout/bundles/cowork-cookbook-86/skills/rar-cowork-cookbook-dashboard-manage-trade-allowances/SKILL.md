---
name: "rar-cowork-cookbook-dashboard-manage-trade-allowances"
description: "Pulls trade allowance data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-on"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_trade_allowances", "rar_sha256": "9d40f9a36ddef205cf623f612aa105773f418af3c31be28ab15742eb06b86702", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
