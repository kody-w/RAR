---
name: "rar-cowork-cookbook-dashboard-plan-service-contractor-work"
description: "Pulls plan service contractor work data from Dynamics 365 F&SCM for a legal entity and fiscal period and saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_service_contractor_work", "rar_sha256": "d0e76fc99adcc9300538aa7ac709624854489c8e07815bfa16348bc240ad8ceb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_plan_service_contractor_work`. The original RAPP
agent is preserved byte-for-byte in `dashboard_plan_service_contractor_work_agent.py` and in the RCI capsule.

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

Plan service contractor work Interactive HTML Dashboard — Pulls plan service contractor work data from Dynamics 365 F&SCM for a legal entity and fiscal period and saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-service-contractor-work
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
      "description": "Name of the HTML file to write, e.g. dashboard-plan-service-contractor-work-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_service_contractor_work_agent.py` and embedded as the fenced Python below (sha256 d0e76fc99adcc930…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_service_contractor_work_agent.py` first:

```bash
python3 dashboard_plan_service_contractor_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_plan_service_contractor_work_agent.py   # or on stdin
python3 dashboard_plan_service_contractor_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service contractor work Interactive HTML Dashboard — Pulls plan service contractor work data from Dynamics 365 F&SCM for a legal entity and fiscal period and saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-service-contractor-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_plan_service_contractor_work',
    "version": '3.0.3',
    "display_name": 'Plan service contractor work Interactive HTML Dashboard',
    "description": 'Pulls plan service contractor work data from Dynamics 365 F&SCM for a legal entity and fiscal period and saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the out',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-plan-service-contractor-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-plan-service-contractor-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bc83daf8368a6103',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/plan-service-contractor-work'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-plan-service-contractor-work', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-plan-service-contractor-work-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of plan service contractor work with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull plan service contractor work data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-plan-service-contractor-work-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing plan service contractor work.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls plan service contractor work data from Dynamics 365 F&SCM for a legal entity and fiscal period and saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the out', 'example_request': 'Build me an HTML dashboard of plan service contractor work in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-plan-service-contractor-work-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a shareable browser-viewable dashboard of plan service contractor work from D365 for someone without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardPlanServiceContractorWork(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPlanServiceContractorWork'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-plan-service-contractor-work-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardPlanServiceContractorWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
