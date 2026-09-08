---
name: "rar-cowork-cookbook-dashboard-plan-marketing-campaigns"
description: "Pulls plan marketing campaigns data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_marketing_campaigns", "rar_sha256": "5c723f3b9a8c4472ad84ab2ea3e40e0337b32df1012bced9f6638f150a407dd9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
