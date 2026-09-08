---
name: "rar-cowork-cookbook-dashboard-manage-environmental-social-and-governance-esg-plan"
description: "Pulls ESG plan data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output folder; r"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_environmental_social_and_governance_esg_plan", "rar_sha256": "746d08f523d03eab13961da520f642db1f7e6f583908372c8385117b1d86106a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObWLblX1HfF9HpfLIvgxhdURGNQAIkgRAgMaQznMyDmAcJyM7/3gfpesgq13uvoupTy/a1GM6e91r7XPj9xem7uGxePr5ogVMseCfLkjhoFk7hL9jyXjZX8F95dcG/hVcWXZO4fVc27cv7Fz9ovSapuqQswHKlz7J2sdH4RZUBQb7TOYuwKfMFNxZOnnjtYkXgi+3/1lhpEZZAwSJKbkGxyILIyRZB0SXd+NAaJq0HzlRBk5T+48y9SbqgBSvaDhw6WVkEi6TogsbxOiBjIejSAShsY7d0Gn/xris7B9gSB44fNO8X2oVfeLHTdO37RVs2neNmweLx8/1CZXggyk88Bzj186IrF10cLMq+q/oOmJkBAX9ZNMDZYHDyKgval4+//Pr+JQHfXz7+/uJlTgtOvXBflEtO4UTBprglTVnkwCsn00ovcTKm8PnyFjSFU3jBpo0UECQgFvyMwPpqBEmYj4HXIDg5OOUH4eLt6F0bZOH7xX/+5/XuNFH788dPxeLt8+ll/qP2xcPurnTaLvAXnlM5bpKBiL4umOzujO2iCbq+KZ5BbJIien2u/CaprBZ/na+9eyp5jYLu3aeXEpjgzBn+9PLzAmTt00vTz99fZynVu59fs/IeNO9+/ian7d008LpZGLD69fPb8ZtYcOO3W5Nw8VlTNuybribwkioAwr/zb/48TX8T9xaSz8+b35XV+8WPJc/+/BXY+6xSF8j9sVgQA7Dy5TUtk+Ldm44GZOqRqHc//yOxXhx41yxpu/+R3F+egp8V+e4tJD+/f6Tv18XyzbevMv+x2rm3/hlPwO1f1H0N1D+S/cjs34jOkgJ03pdc/lDcjxYs/7r45R/69l8teL8IP71wQQbaupk79OPi90eJ/PKT/+3kT7/+AUT/t2K0sm+8h4TPuVMkYdB2nz//8lP7OP3Tr7/81FegigMn/9w32Y9k/iiuDz1/iuDbXe/+vBboPxfXorwXi689tPi9rP5X88fr4uJkif/tfPtx8X0nzp/lYnbii9JnCL7rxhbY+l0cf375A2BSAbzpvcdlgB//8R8LKfGasi3DbqF5ANIWIMFdkgez8XqctAvwd0aNJgBxbZMZFZ/3gfqfMzxbXIaL3/6P9+CBD94bD0BfoXaOK4C7z8H3ePe5fQDeZwDVn6OvkPc5aKNH/fz2utBniG2SKCkAzquMonyapRTdbFDVBG3Q3ACIuWMXfAC9/mH+AkB68du/pPfzQ8VrNf724JTkiZgqK85o2fZZ8DrHxYgBJT2j4AEWC4bA64H2rJwpKUwAAbwH8WrLDNBON8ewvSZZtvATgEeAQZ4MBuL8cRb222+/ucDkT8UT3leLJ1+2ELjhqzmLDx+Az2GWRHH3qQi8uFz89PsfPy3+7+K/WvUQPutQAAG9ZRFYuNOO8gJ0ZT+HBCQYlASAnEcWf//jLfJATAEIHgQoCZPguRhU9TXwv6RBE5gPKE4s3ACEH4Q+rwBrAs5YJN3rQgwXX+0FSudLM6vEZdst/KAKCj8ovBFIdYA7XyNZlN2iBaXbhuP7Rd8GD62/uY3zMDEH8OB0vy0kVgEcVmYzDzdvnAYWlwXg5+xrkTzPAyHNT+1i/UXE60Ke63hROY1TxY3zpiN0nnmZJ4635UC4syiC+6dipvHgUT1zsT/DA24CkfHeUvphzjkYfHJQcX77RffjHmdmWv3BuM2non1rGKeZU+HN9Tcuoj7x5yL8y1tJtXHZZ/4jfsDSWdJbFvy3rDxq8DlDLP5U3PPkMlf3+0eBfSvvxTswcf38HLnEvx2Jvk4li089CiPY4v/nGW2OHMPz6oZn9A232Mi6aj0zOo+tc+afk+7swuzbo3u/DUpfwPALJ3wqsgSUZzP+5Xnnow7e7nnibN+AtKmM+pAPihBkdJb76JG55ptm7i7nU/GFfEDuFg+kBWUCAAU03OzLF4Xz1S+WxiBO8/G3QeRRU80j1KAPFlXvZqBGwyDwXce7Aquauc/f0lzMwQc9f48TL/6TV3MOQV0C+QtgRAI6FxDU61dCeF79YvqfFj7nrXnJYxbtQZs3DwHAjmA28FEESQfQzumeuwTg58eHEOBGXnWz7y5oNODp82TQBHWftHPdvH+La1ABtP8w///0dD4bDBXoLRCsZ8Zfnz03w1EOagfYAGAH1FmeFGC6AEF5C8JDoJPPAAIA+m38fUp8nH5zKHg06kyLXxbOjsxrHiX46A6nGL/HGf1HZQLk5fMdD71/W2lftc2yZ6wFhV8CjV+uPkeS1+dU8RxbFl/kfvy7bdi7f26n9pgTzn8ugI+LuOuq9iMEPbn9C7W/AqSDnra232j+w5NuP/wJkT48AekDUP/hGx59AHT74TGkfq/0GY+Pi3/O8D+JeGucjwvkFX6F50uHt8J7+4A4sR/W1gdsvvqpUINvIA3UlzmovDmrI5grvjLql1sArUYNwDhw85Nh25mY72AWeFAKSNGn4vtOmDsRoFURBQ+4+g4hHqMF6IpnRr8yH7hUdEC3P4+wUfA67/xm89vg5WMBQPn9C8Df4F/ZSM60l8990M77UtBxAJu7JHgcPWBl6Oavf96zHx9fnOx1wQUAwrL2+1p9I6uZrL9rqaf3wGsPaHg/UwhAClDGwPtZ+dyOTgvqG5T27GU3VrNbzz3nPKU+mePzkzn+3qLtn4hlHgMeEwZAq7+ANg+dPgPBfWOAfB45gD0PbL8B8+eO/aHSB399fvLX3+vkZtL7E8UBBXUPcOH9IniNXhdnTdr+UO7XefzvhRpgoJnl+OXHmdvfv4Hg+wfzvl983Q6BEL5tUGcNQdGDvf8v81ZszuljyfzlmeOvi77+8sUNXn79kV0PpPw8V+Szrv7WOnlGQMAQT9T9StgPkn7UMbD8S3O8BeFfQoMPKIwSH2D8A4q9xl2e/Tiab1Y/GP0HpfE4P3dl8xztvlk7z+EO2DO8mcqV3nMAhp7wAj0lQz/QCtQ+WAhw+Rz3bwn9Ftbysd2dDQSedM/fzvz+AnrNmeent2572y+B2wFof2jnaQ8CSAUUguMnpoBr/96d1JvwNnbAsA6kkxjhw1SIoysfXgWOi6xoAvEdHIVDAkN9FwnJgAhxakXD1IpEPWpF4QhCuohPEQhMOEDeE7Y+z/NuMhs8Wwvi9AEgX/DtMjjlv3n69GwO49eN2xyRN4d/f3EJDNwpYK3IPD8sRCMuZB7coTGhAl4OWxzFd9tW83eoogUpoeeD7aewfhyagwZOeDlzMnZ78cSOI8Pqk5PqeryMdPpa9CQ++OF6f7blotdtedgPB0sxb2iokEfUMdOjKJthv79VNrdTHfXSVpcd2Xr61blGZUMvN2WN9BVDULbMJJ0wEFY/aLwEbbSlbvIlNO6lwz4kCbozV1iVh67t7hFCwJAJWu7PxP4oYZu4uqmlDZFWbV4u6eTuQgxl08Mw+D4Y7EMoNBtYq8fztsGtCBETqylQa8XqKpQfLwi9NSymqH1NZW/FrrLwMTe2fNYfG4HoNkmdHvRLPEhUeekqbZeGKldrYULvPVPsUuzY0mU+NauM3JwhhdKpwN2xOLMvKU7JVOJgihklYueaanTxblgSUy43QjQGNyEd8Fu6vZKhMFH6QJD+LSzcrYHdD9tDLHr9xlye7QqNuO4g05v8lFLIluYlfcXJ486ptnlfuZQ/yFttuWpWIzN4asDxXMszYhsdDmfpTpfubolsEtk+yl4WUNNmaxFYcpX8lNBcTTNORMZqUZsM2rW2dtMkWcuxN0vXK4p1uk9IIufjEmW703i2041CHQZryDbRJdvz2kRha3gZWbLmXmXuomVDX+acjkZQpfdLsYsY7mxhUIZdSf4wZis7W+28ZedcIlxLLvJV2dZiWW7a3q2szUZziInYy5QEcZMJuwex9TY4fOcgdNIKXYNoRRKN6XyscIfeZjt+0Pd3ytYrn6xdOCN9kVua5IWx8JjXYG4D1wrVpzaLou3av4sbcYfSFa9ZusAEyyAJM9eRR8VaMUdBM+1SqOpuPKzhDcGIXq4nAuVMkMs3PVMcoe35RFwih++kmm8v5cHIGHe4IgRRZ1YMC6xZSMJ+i3j1KtcqWGS3pHgm8XJMqqk11D7TCUGAzkv1AG0IWWd1n2ZCIuFOqrI9dNzIDxa1qQqL5qjWWQ29n14Du5Ft8sjs7jZaxH1Jevd73sJ1hw/9McAlY7UtnPZw3O47hSCiKfMzQsv4a+846nAZKF7uZLazBbw/KGSkrBgfp9z7SoYizxbOaAilE71JKMFdqs79BoIen9rGte7y9gCcH1Zi1MHZ0bWb9ZQsgx5R44mzhGkzpeJq5W0v1Lo+XPOS112piGGZ0TpHExEx5bo1OjKGJOYbWnN24zXYXq65Um3k7bEhttF6taUwIcvWCkNRl9jjjAgAid1aG+Focqmj01LVTgqXVugusOjooGzR5Q5R0UY/GzVcTWi6d9BiL+HNeN9vTYequSqdNERea920z9cuwWQHqiwwX43zDdkgEw2PQewkl6rjj/iSQ4vKPByG9FJ2A5QDrdRqSxe5AKPDTtxOwkmwPc9zS0+XLneDN3enrMjFPhKWcCrp0THTDakLOXbL8BprgR3PeEl4/rDjO46VMRXKaM4JBmRzbNYRXVN79Rjfb6CfrR6Bm5uz7eWjauq3wVraF++WjupNOG8LY1Sxc0RG9n6dqYUt9Uh3Xle7Pb4rr6eNk+AUvsLZZKpsehuF22C4k3Q0JdWmPjer7toS5VkVOB9aYz2zXnZA1I1GGCsMqZPKKHibGMg6GWRdXN6aYztEcXA9T3HvReQpHCw3b8s0ua53Tb2XL2RWhjjEMHi5UvjxWJ5iNrjRxraQ9dskRDe2RCOjwKDVmjaPeSH4RcVv0zqP9PAaBc71nOLBNvab/Oaro8ObVA9LoX3YIIcOFSF7iPPr0bqOOu/khua4heLz4iXjQy7a7kc2FglPHuXdnhPYg3ab+LIUVbzd96kICbCNbbcDG3Mpx9vDiaZL1mEve3FdexZf75MTFx4uIxn0jE0ZLXwNA4kSXTu2cc6sogRmjXWhEw7bsLXSHYx2EmAxuGvQvu1V4hR7xhJmr+1ltdq494g15OpyXWMZndJqxgeTgvi46fTRKtYSgAYSf7fucd1s4RaNmPvg5QiHH8fS1tjJdkZDonZhu6RDIUYhJUXzzf6S1c1aGfYH8qydnT6kg51RkypAhxObbSevGciEsrFeRe530jlbkTTeoJGHCrlDaKiHBpQOWTemqQ1Sk+1u7+2JdJpCDzNidi2WajWup1C52tZ1CHZlZ9WseLWkIqAEsorYAM1DoUmchPbFwEymg7mXRn1KbptNH9u+IO/veyqTNkvtug1smd3vOsy48uqJKpd26Fh4W2KoIw6psDuTRGyz4v2yX66pnAgYGmzdmyKYllOKRvHleOmDC29EGEmc8OVEhlWg0qmhWrF1OAOLYaeC7BRrCYPdc+VBmdh9nGtiKZXbHhHM3XIDK6LXZtqxKNCVmNwQSbARex0l+oGI9iJV7aGTdOcE93jJswuiDAx8FftDjUARykfdiVdLl00TP4C46CbFWKfYZmAUdbjkEnZ3O4rerkMy/46nRCTtWDRY45XGJUxolwxl9GupnaI9o4oaitvirlybrHe+pyIuo1cLGrFVGBFwhvuqPaBqi61PfnQV8ZBroh1bJAqcsLpjCM3AifoxP59GJqxK03L0TbNRXWm1cUQFi4UqG1HbXWVDe/FQltPvfe+WkTZMaL1dVmM4FnQhctk1EVd7+tbn6rpmFGJytKsjxn57YIkSly4lmV02J/pc21jsUnll7XYxoqiRdBL0owcjtJPX5jo+abBubeX4ohD+Rg/S/Ym8H3eystvH53NrEjeqP+/uSmc5g5rpUlmXO2ps0LW5z0KGQuRzaWycnEiCUlK3Ls5ZYy1s6OxGpKJGyCfhwoWQHWaxNJTKKOpqke5Deb+ycjs51PlpMFcr97r3aeXAn26WRB0R1AVTWJS42nl/2i9vpIG39sW1XNII7T2zyUhIvy6PqSR5R3/QpLI3VKqO9+fgCCNXMRFWm2V8Vm9nwXG1GL4mNeFp6/01Y1YoUYtt1pJqdrPi09pg5T4u4SqYnFbKSWbpsFrrxA22wUZ4nbfT4GU8XyZg6EnPd4gkegcSGbaTitvqoIqYsWUGlZ1gbo2VnZdbzerK+xssLKREl3QGabPq6B2WYLLjkhy/X1u0mfyC12nzxshOdGYOh6S+wtUtT11m6u6GXJuqYk09u2TDG9SjXr1n08BObWW6D+fcRdNuoq5UdeUPdsjtkGHcXvjupACc20tXQ6MQXGyaFUXZ67A6Z7fzaX/Ky/qCGlmQs1v1mlYC3w2OOZyrRsL4DnJWR5E5OXChLjFPsdPLdJ+Cg2L7p0O+z1hJZC4XXd/qxIk7rIN1eerPCB1JtsXL96ocCcfEAXFuvZynddXs86S2tgUZ7p1WPZ+yVjyyFa4qArsemt14q1Y1ufcuvWYQdwMTietoOKTh6iJgicFpVDHYgbbURRVGCBKjQv3ijbKYNWshqZnTCZfDM6WtTRzwRGY63gQoQu3KTKthnMPq5kyFSpFidKivL/RRMMEAGK771fK4c4q7uS2I5IpIbuIUZITYGSSelcPEbhovyYUMxo9BCuYvVF43Hrbm4fhCIxDmeTy7tImxYg6nlMy3VwMFE2panyr2oqNyZDAlvsV5asdkPUkXGXaJkhXVR+XG2Y9ByRO7tQxfulZzRqRYcSGSx65o2dfDoR/XN0EablS4clVplHSQ6dwqXF89N9sjGWete89vgNlPpaBTkibtNnVhOCWCQ1XpIjmyEm/0enuJGV3xL21ebI3zGTbdm+44rVe45WCdNwIDIf0xHK9mGsHBxdYbONFZ1yaC1cVNkdOwHQEFu2pHXoou57GQtKG1lCRdJ93Ry7HITxOW3VkCJc6alFXxgQJVuwnz7H4VB2UPqaJ0OpnjkahrlSHPcCKSLp+vm1ObmStYOYn6WlJFTlyn8hCduTSXiLW1Nau9b5IW4DT2OK4JhOOzhu7Es2WeZIk/OAczvd4nZ+uHnqmg0xASp7FWJZJwmki5765CrYfqBrv0HXI4FLJ6cgaGUBh/yJAznch6lDhdOJrwsSQpyvTjnpIExd9GTQLmHOHecIGGDWu5RlY22dbwaYWvdY6vWOS6v46XqzXsID1DITC/R2tDFVdp37Jx2FOufMikZaXeGMYBm5Q07SgthUk3mjgwweB2cGt9UbHVvNpOlHjTMiRU1zki3yCz2KT+CPpCEyGCk+/9UTuzWRzExb6Gxz1oZudmqoJcHqMdmDImrF8u3TNGMCRlaiXONKlW2W6gl+kFNfVd0sG4XbWDTtcdc9ksXTtBGjvS0iyPMWwpZdLFJ9QljaraPTONLhFq6HQczxTXek2GRknvkqtwLWA1GqySHsHW4WlXIu7xGhmkud1gJ9kwPQK7wOqGE3Yn7kIrhDhVIY5KTFEwaA6JqstY46RvJ5OId7cq1r2lxMt4Wx9HPJeGTMpL1OHLNPaxJApsjN2y6mB3G2tnse0hLm9T3+zvZ8tI8SN1p/hwS8UBo96XvDtdAI4oR9Yd5DWttjyJr6mzQW9lBasZ7DqpQuH5x5NO58di1OOEqvcpqSCseVrVtzbroiI5MpiY465U8VWO8u2mTMmOcPWtyWEO2aOofCibySP3lIB53D0QjunWbHRcDoK1d9Cz6rYkPI7zlM6DnMMQ+rmD6quW3AzNrVf2OEVYlYCk1bqmcf2I6cdpuLhRqtgCzFvGsvEElkGJZUDD4GZimY++IRNKMNIr9UBKS4MrqjN5CWMBP1gBlplCiUHjakyZ6JKUeKGx8r5QaoOtNsgWOWlrFb1LQ2zsNPcIucoySz1naVLyTUr14G42lqtkwZFkcXoVyD7dM0tcUnCtR3wZJaXbHgf7bSEuScFNijYnGp1DhDjqlxC07D2IYqBIupK7GzWZEBZDqRbfrrjb1TYdLovalx2Rrhx86h2lH6RksBB+dTwNHGFJQMdW2ZcwWwG8xe/WiUn7s5weNubpHkaBZlmVkqbblWZPpdMR9nY/ydOt9hMPE463NQILjatllED52dKg7vZU7LWdFB55hjCnDNZ2e1ouSFSfBv1sa+s6jZU2rMhbPybXwrvgoSlJu0CukOu4cYmI3vE1BTPSJfVct7ySZAdVNzBJHy2fumzvAwZtK+NIJxeBgP2dqC9vYXtHTW6Z5ZOYaqCrtTVGQXJp++ilGNJwo+75onHPgXURupHcJRMxwK5rUOg6qPlLUN9lEaCCnaqNu7IQF9/g9jBKrDKBLmiHNbTJvUbFooYUk4u6Ncqdu7GEXbw8taFqOZuMVTTJMhu10/qeXVduX/G4QAnnq8lgXbls9zrLqvMOCsVbnrvFzormN2WAtgOFBQS3H9NrfOarnRLiJBVw6zsW9AReKhmPGvUulMfL2iGv8L0SbCLZmjR8lY54YWOGoMpxmN2OmWZbh/aEWBjk4djGl0lROOHTQQbNZGdWsr8xY5qV/S6yCe1u6M6xPRQKmFU2/v0wOax8CNpL0+bLPjrYxwZphnhD7rRhnfk+41oOvMPkJSbWxI3pYcWZWu3iIWqoLAP9XuRZGzYbjrrjhZGny5Zt8o7BGLSfTLHPldq/abjAnY/yOW8V1fBupxr3aDvDeJGtN4RwwMEOOjUYDi+h/pBUO1U1TpTQTcle6ZOgyjdUA3eNd99fSEbIBZvmT5i7wm/GLbrTDWEhDXHwj/slBbN3gs75gIShzuvJ08FBxdyD0LBQGHUwz0DjdSiC/XQqRvFu31wXMS90uiHt8ESGyPIUIsqy2bDCmSdMs/G4gAtAu3rsalkdkvG+PqdhLU1BnEOecVwi9Q0Vzx6PDOWWUo8hpxjhcKVchZlKcxlBAP4OyYR5xVIFG/9NXqv8idacctUI3uSmV1HNz0vZVXpAGlv3TpkGw7vHvj+F3GV7DS06CeGokSjvhF0SiOGv8FYo1DvPs2mhTepmlKFyiGT1cqiaIEqkY8VBB6s/JuMBGWEYTnr6Xt72KFfptoqqJEAc3oZI1Wz9cE9D7km3uJzuM2+1E8XaO6/RC7oW0IalW92CTPWqdrl73KlLU7lx2S3vYNe5LB0jp3k2cwPkWKl0GQz1ldy26f1WboZzOhBNVRljlR34ZdfxSGo7q4mmTnVlGHckhVsPVUOu6mwH4XRbctNbaazvNryEUccL2nLlt5nnIryrgRpT6k5ps40lG+q4UTC05Sl3eSzBntI3DzsXhk7q6eR13LlgA62pI81ACiIu425lxPapiHl3mEY+92DdS1MwJywzt2Cu+1XREzupXZYsrNLQlC8vQAbZoSR34MCCfGrbC3LiNd5gZJFEz8elqKmnQI4wyKUbfIRg+ypAxqiSuR1EXmUTaHx16Ztc6VUR6N6tW+0D++gZY88NgXvxaFi/D4kpsz7mb5VeO3STIJmXDvWIuycp4pUzkpbYIp2eQU7o+tv6bLZhvh7Ngx/hrnlr1EmmhJu23rk5Y+2v09U1g7CeBqRr2mWAbR3Bohl/Ezk4bmIbsd0QMayDLQUKGaf1nZDdaNBJuwIac/ZYnr1aOBfTHTluG4ULPN9He5lgQiZeydurcimh5F4KzYGNafPs0wDKz1RN0BpyuRQU7V4PYdWYLopNtg+BdI37m3rjDjEdOvLqbskDNWJrGMYC3+hJnBtjrI5ro2ybLCTMuMeXVC+VzQ7iJrqyKqSQjVIwIxzZ3sz9yjNWPUsEVobdoFx0kMGQjERZDemqvU9rfIk3K7M/ZuiqNqCRakIrlGV2qo7YQVGu0Wlb8mQGT7Esrc+n2AlqVtil/jkv1iuvJ6pmaKLzgdeTYzDy4eSsu5NcM2V5JHfLMyce9nZh3naCt9sGkE7wpNKx23BFQqVJwHwMWDUvCr4w6OFArdZabwnaXa1v/rjkcuSQm9rBw67W/qIK+lSyubAue7rvnX5phivYpviKIb21U6yIC2eS+m6vbKh60pdDMJXFzbsOOWYr+wYRhnYlRNCSW1L4SjsEKsMwL/Nz3S/PGl/+Pa/pzY+b/m1Ptp4PqL68TPN4who4/seHro//Jnt/ff8CNnrA2udzvzbro7eHZH/z1O/Dv/QodRY9Pt+Z+/JY//kGQedE89vpL0nh923XjMDw7PESDljh9u383mo7v9oMkKz9/uHyV2vmLJZN4Dlt97krvzxifLzElQc+2PEEb4fR2zNSsPbtvbHPKwL/HDTVHIS3NzWA76tX+HX18sf/Axma03BkMAAA -->
