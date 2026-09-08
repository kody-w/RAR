---
name: "rar-cowork-cookbook-dashboard-plan-service-contractor-work"
description: "Pulls plan service contractor work data from Dynamics 365 F&SCM for a legal entity and fiscal period and saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_service_contractor_work", "rar_sha256": "d0e76fc99adcc9300538aa7ac709624854489c8e07815bfa16348bc240ad8ceb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
