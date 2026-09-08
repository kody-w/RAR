---
name: "rar-cowork-cookbook-dashboard-create-marketing-material"
description: "Pulls create-marketing-material data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_marketing_material", "rar_sha256": "fb106f2d6df5ec1ece79e881e4fd51dc3d890b2d4a15eab2f30a6e4f5f463e30", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_marketing_material`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_marketing_material_agent.py` and in the RCI capsule.

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

Create marketing material Interactive HTML Dashboard — Pulls create-marketing-material data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-marketing-material
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
      "description": "Reporting period; defaults to the most recent fiscal period available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull from (e.g. USMF).",
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
      "description": "Name of the HTML file to write, e.g. dashboard-create-marketing-material-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the file, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_marketing_material_agent.py` and embedded as the fenced Python below (sha256 fb106f2d6df5ec1e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_marketing_material_agent.py` first:

```bash
python3 dashboard_create_marketing_material_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_marketing_material_agent.py   # or on stdin
python3 dashboard_create_marketing_material_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create marketing material Interactive HTML Dashboard — Pulls create-marketing-material data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-marketing-material
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_marketing_material',
    "version": '3.0.3',
    "display_name": 'Create marketing material Interactive HTML Dashboard',
    "description": 'Pulls create-marketing-material data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-create-marketing-material',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-marketing-material',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c87fb231c73619d6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-create-marketing-material', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to pull from (e.g. USMF).', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-create-marketing-material-2026-05-24.html.', 'output_folder': 'Destination folder for the file, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of create marketing material with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull create marketing material data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-create-marketing-material-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing create marketing material.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls create-marketing-material data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output', 'example_request': 'Build the create marketing material HTML dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-create-marketing-material-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the file, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a shareable browser-viewable dashboard of create marketing material data from D365 for someone without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardCreateMarketingMaterial(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateMarketingMaterial'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-create-marketing-material-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the file, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardCreateMarketingMaterial().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
