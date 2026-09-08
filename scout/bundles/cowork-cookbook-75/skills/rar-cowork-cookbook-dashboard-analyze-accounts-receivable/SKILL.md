---
name: "rar-cowork-cookbook-dashboard-analyze-accounts-receivable"
description: "Pulls accounts receivable data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_accounts_receivable", "rar_sha256": "f9e4e7583c90465d997dd05529e4356ee7c3771831ba3d399e9721b52a7c1079", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
