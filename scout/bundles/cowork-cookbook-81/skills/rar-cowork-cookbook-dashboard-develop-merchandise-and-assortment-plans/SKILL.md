---
name: "rar-cowork-cookbook-dashboard-develop-merchandise-and-assortment-plans"
description: "Pulls merchandise and assortment planning data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_merchandise_and_assortment_plans", "rar_sha256": "e116afb6f4312feb67581130cf40d7ea08847825383c988f37aa9a087fffec86", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
