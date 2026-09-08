---
name: "rar-cowork-cookbook-dashboard-plan-marketing-campaigns"
description: "Pulls plan marketing campaigns data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_marketing_campaigns", "rar_sha256": "5c723f3b9a8c4472ad84ab2ea3e40e0337b32df1012bced9f6638f150a407dd9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_plan_marketing_campaigns`. The original RAPP
agent is preserved byte-for-byte in `dashboard_plan_marketing_campaigns_agent.py` and in the RCI capsule.

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

Plan marketing campaigns Interactive HTML Dashboard — Pulls plan marketing campaigns data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-marketing-campaigns
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
      "description": "Name of the HTML file to write, e.g. dashboard-plan-marketing-campaigns-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_marketing_campaigns_agent.py` and embedded as the fenced Python below (sha256 5c723f3b9a8c4472…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_marketing_campaigns_agent.py` first:

```bash
python3 dashboard_plan_marketing_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_plan_marketing_campaigns_agent.py   # or on stdin
python3 dashboard_plan_marketing_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan marketing campaigns Interactive HTML Dashboard — Pulls plan marketing campaigns data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-marketing-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_plan_marketing_campaigns',
    "version": '3.0.3',
    "display_name": 'Plan marketing campaigns Interactive HTML Dashboard',
    "description": 'Pulls plan marketing campaigns data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-plan-marketing-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-plan-marketing-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f6d22b16ee7d713c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-marketing-campaigns'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-plan-marketing-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-plan-marketing-campaigns-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of plan marketing campaigns with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull plan marketing campaigns data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-plan-marketing-campaigns-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing plan marketing campaigns.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls plan marketing campaigns data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output', 'example_request': 'Build an interactive HTML dashboard of plan marketing campaigns from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-plan-marketing-campaigns-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of plan marketing campaigns from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardPlanMarketingCampaigns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPlanMarketingCampaigns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-plan-marketing-campaigns-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardPlanMarketingCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
