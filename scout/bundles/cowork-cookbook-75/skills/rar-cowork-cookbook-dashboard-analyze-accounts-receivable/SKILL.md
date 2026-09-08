---
name: "rar-cowork-cookbook-dashboard-analyze-accounts-receivable"
description: "Pulls accounts receivable data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_accounts_receivable", "rar_sha256": "f9e4e7583c90465d997dd05529e4356ee7c3771831ba3d399e9721b52a7c1079", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_analyze_accounts_receivable`. The original RAPP
agent is preserved byte-for-byte in `dashboard_analyze_accounts_receivable_agent.py` and in the RCI capsule.

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

Analyze accounts receivable Interactive HTML Dashboard — Pulls accounts receivable data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to th

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-accounts-receivable
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
      "description": "Fiscal period to analyze; defaults to the most recent available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data for (e.g. USMF).",
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
      "description": "Name of the HTML file to write, e.g. dashboard-analyze-accounts-receivable-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_analyze_accounts_receivable_agent.py` and embedded as the fenced Python below (sha256 f9e4e7583c90465d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_analyze_accounts_receivable_agent.py` first:

```bash
python3 dashboard_analyze_accounts_receivable_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_analyze_accounts_receivable_agent.py   # or on stdin
python3 dashboard_analyze_accounts_receivable_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze accounts receivable Interactive HTML Dashboard — Pulls accounts receivable data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to th

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-accounts-receivable
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_analyze_accounts_receivable',
    "version": '3.0.3',
    "display_name": 'Analyze accounts receivable Interactive HTML Dashboard',
    "description": 'Pulls accounts receivable data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to th',
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
        "upstream_slug": 'dashboard-analyze-accounts-receivable',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-analyze-accounts-receivable',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '296916e9ddafda60',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-accounts-receivable'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-analyze-accounts-receivable', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to analyze; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull data for (e.g. USMF).', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-analyze-accounts-receivable-2026-05-24.html.', 'output_folder': 'Folder where the generated HTML file is saved.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of analyze accounts receivable with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull analyze accounts receivable data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-analyze-accounts-receivable-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing analyze accounts receivable.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls accounts receivable data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to th', 'example_request': 'Build an interactive AR dashboard from D365 for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull data for (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Fiscal period to analyze; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-analyze-accounts-receivable-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the generated HTML file is saved.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable AR dashboard from D365 data that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardAnalyzeAccountsReceivable(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAnalyzeAccountsReceivable'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to analyze; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data for (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-analyze-accounts-receivable-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the generated HTML file is saved.', 'type': 'string'}},
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
    print(DashboardAnalyzeAccountsReceivable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
