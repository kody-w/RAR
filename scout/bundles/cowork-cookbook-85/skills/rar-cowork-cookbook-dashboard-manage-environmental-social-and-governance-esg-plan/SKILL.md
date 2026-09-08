---
name: "rar-cowork-cookbook-dashboard-manage-environmental-social-and-governance-esg-plan"
description: "Pulls ESG plan data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output folder; r"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_environmental_social_and_governance_esg_plan", "rar_sha256": "746d08f523d03eab13961da520f642db1f7e6f583908372c8385117b1d86106a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_environmental_social_and_governance_esg_plan`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_environmental_social_and_governance_esg_plan_agent.py` and in the RCI capsule.

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

Manage environmental, social, and governance (ESG) plan Interactive HTML Dashboard — Pulls ESG plan data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output folder; r

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-environmental-social-and-governance-esg-plan
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
      "description": "Name of the standalone HTML file to generate, e.g. dashboard-manage-environmental-social-and-governance-esg-plan-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_environmental_social_and_governance_esg_plan_agent.py` and embedded as the fenced Python below (sha256 746d08f523d03eab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_environmental_social_and_governance_esg_plan_agent.py` first:

```bash
python3 dashboard_manage_environmental_social_and_governance_esg_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_environmental_social_and_governance_esg_plan_agent.py   # or on stdin
python3 dashboard_manage_environmental_social_and_governance_esg_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage environmental, social, and governance (ESG) plan Interactive HTML Dashboard — Pulls ESG plan data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output folder; r

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-environmental-social-and-governance-esg-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_environmental_social_and_governance_esg_plan',
    "version": '3.0.3',
    "display_name": 'Manage environmental, social, and governance (ESG) plan Interactive HTML Dashboard',
    "description": 'Pulls ESG plan data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output folder; r',
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
        "upstream_slug": 'dashboard-manage-environmental-social-and-governance-esg-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-environmental-social-and-governance-esg-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a48e8969b9f2828c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/manage-environmental-social-and-governance-esg-plan'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-manage-environmental-social-and-governance-esg-plan', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the standalone HTML file to generate, e.g. dashboard-manage-environmental-social-and-governance-esg-plan-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage environmental, social, and governance (ESG) plan with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage environmental, social, and governance (ESG) plan data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-environmental-social-and-governance-esg-plan-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage environmental, social, and governance (ESG) plan.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls ESG plan data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output folder; r', 'example_request': 'Build an ESG plan dashboard from D365 for USMF for the latest fiscal period as a standalone HTML file.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the standalone HTML file to generate, e.g. dashboard-manage-environmental-social-and-governance-esg-plan-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable ESG plan dashboard from D365 data that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageEnvironmentalSocialAndGovernanceEsgPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageEnvironmentalSocialAndGovernanceEsgPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the standalone HTML file to generate, e.g. dashboard-manage-environmental-social-and-governance-esg-plan-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardManageEnvironmentalSocialAndGovernanceEsgPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
