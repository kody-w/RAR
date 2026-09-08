---
name: "rar-cowork-cookbook-dashboard-develop-a-business-continuity-plan"
description: "Pulls business continuity plan data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_a_business_continuity_plan", "rar_sha256": "e37c668bdd4b650b4f5c34b6a58e55e2df2c45ee9680b0412182f9200e2f6e3f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_a_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_a_business_continuity_plan_agent.py` and in the RCI capsule.

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

Develop a business continuity plan Interactive HTML Dashboard — Pulls business continuity plan data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-a-business-continuity-plan
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
      "description": "Name of the HTML file to write, e.g. dashboard-develop-a-business-continuity-plan-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 e37c668bdd4b650b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_a_business_continuity_plan_agent.py` first:

```bash
python3 dashboard_develop_a_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_a_business_continuity_plan_agent.py   # or on stdin
python3 dashboard_develop_a_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop a business continuity plan Interactive HTML Dashboard — Pulls business continuity plan data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-a-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_a_business_continuity_plan',
    "version": '3.0.3',
    "display_name": 'Develop a business continuity plan Interactive HTML Dashboard',
    "description": "Pulls business continuity plan data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-a-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-a-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '71884e347452ce89',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/develop-a-business-continuity-plan'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-develop-a-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-develop-a-business-continuity-plan-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of develop a business continuity plan with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull develop a business continuity plan data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-develop-a-business-continuity-plan-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing develop a business continuity plan.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Pulls business continuity plan data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;", 'example_request': 'Build the business continuity plan HTML dashboard from D365 for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-develop-a-business-continuity-plan-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 business continuity plan data for viewers who lack D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDevelopABusinessContinuityPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopABusinessContinuityPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-develop-a-business-continuity-plan-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDevelopABusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
