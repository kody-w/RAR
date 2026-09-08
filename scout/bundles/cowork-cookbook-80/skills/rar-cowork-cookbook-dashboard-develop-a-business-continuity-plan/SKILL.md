---
name: "rar-cowork-cookbook-dashboard-develop-a-business-continuity-plan"
description: "Pulls business continuity plan data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_a_business_continuity_plan", "rar_sha256": "e37c668bdd4b650b4f5c34b6a58e55e2df2c45ee9680b0412182f9200e2f6e3f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
