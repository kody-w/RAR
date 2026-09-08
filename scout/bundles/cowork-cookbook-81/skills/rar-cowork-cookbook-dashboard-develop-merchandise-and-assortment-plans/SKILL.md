---
name: "rar-cowork-cookbook-dashboard-develop-merchandise-and-assortment-plans"
description: "Pulls merchandise and assortment planning data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_merchandise_and_assortment_plans", "rar_sha256": "e116afb6f4312feb67581130cf40d7ea08847825383c988f37aa9a087fffec86", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_merchandise_and_assortment_plans`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_merchandise_and_assortment_plans_agent.py` and in the RCI capsule.

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

Develop merchandise and assortment plans Interactive HTML Dashboard — Pulls merchandise and assortment planning data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to th

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-merchandise-and-assortment-plans
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
      "description": "Name of the generated HTML file, e.g. dashboard-develop-merchandise-and-assortment-plans-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_merchandise_and_assortment_plans_agent.py` and embedded as the fenced Python below (sha256 e116afb6f4312feb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_merchandise_and_assortment_plans_agent.py` first:

```bash
python3 dashboard_develop_merchandise_and_assortment_plans_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_merchandise_and_assortment_plans_agent.py   # or on stdin
python3 dashboard_develop_merchandise_and_assortment_plans_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop merchandise and assortment plans Interactive HTML Dashboard — Pulls merchandise and assortment planning data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to th

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-merchandise-and-assortment-plans
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_merchandise_and_assortment_plans',
    "version": '3.0.3',
    "display_name": 'Develop merchandise and assortment plans Interactive HTML Dashboard',
    "description": 'Pulls merchandise and assortment planning data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to th',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-merchandise-and-assortment-plans',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-merchandise-and-assortment-plans',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6e25e189d940258a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-merchandise-and-assortment-plans'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-develop-merchandise-and-assortment-plans', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-develop-merchandise-and-assortment-plans-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of develop merchandise and assortment plans with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull develop merchandise and assortment plans data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-develop-merchandise-and-assortment-plans-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing develop merchandise and assortment plans.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls merchandise and assortment planning data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to th', 'example_request': 'Build an interactive HTML dashboard of merchandise and assortment plans for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-develop-merchandise-and-assortment-plans-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 merchandise and assortment plan data for viewers without D365 access. Read-only.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDevelopMerchandiseAndAssortmentPlans(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopMerchandiseAndAssortmentPlans'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-develop-merchandise-and-assortment-plans-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDevelopMerchandiseAndAssortmentPlans().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
