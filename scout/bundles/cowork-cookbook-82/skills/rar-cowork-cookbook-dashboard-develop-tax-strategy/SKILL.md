---
name: "rar-cowork-cookbook-dashboard-develop-tax-strategy"
description: "Pulls develop tax strategy data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard file to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_tax_strategy", "rar_sha256": "63d1f7a4e7ef39ae31c5e8c554c4ab4325bbabc21f4f6d85848db152c162569d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
