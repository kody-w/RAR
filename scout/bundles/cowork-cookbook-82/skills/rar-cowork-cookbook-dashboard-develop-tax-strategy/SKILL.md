---
name: "rar-cowork-cookbook-dashboard-develop-tax-strategy"
description: "Pulls develop tax strategy data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard file to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_tax_strategy", "rar_sha256": "63d1f7a4e7ef39ae31c5e8c554c4ab4325bbabc21f4f6d85848db152c162569d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_tax_strategy`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_tax_strategy_agent.py` and in the RCI capsule.

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

Develop tax strategy Interactive HTML Dashboard — Pulls develop tax strategy data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard file to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-tax-strategy
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-develop-tax-strategy-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_tax_strategy_agent.py` and embedded as the fenced Python below (sha256 63d1f7a4e7ef39ae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_tax_strategy_agent.py` first:

```bash
python3 dashboard_develop_tax_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_tax_strategy_agent.py   # or on stdin
python3 dashboard_develop_tax_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop tax strategy Interactive HTML Dashboard — Pulls develop tax strategy data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard file to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-tax-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_tax_strategy',
    "version": '3.0.3',
    "display_name": 'Develop tax strategy Interactive HTML Dashboard',
    "description": 'Pulls develop tax strategy data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard file to the output folder; read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-tax-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-tax-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f7424f4e8842a250',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-tax-strategy'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-develop-tax-strategy', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-develop-tax-strategy-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of develop tax strategy with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull develop tax strategy data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-develop-tax-strategy-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing develop tax strategy.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls develop tax strategy data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard file to the output folder; read-only.', 'example_request': 'Build me an interactive HTML tax strategy dashboard from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-develop-tax-strategy-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of develop tax strategy data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDevelopTaxStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopTaxStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-develop-tax-strategy-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDevelopTaxStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
