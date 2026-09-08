---
name: "rar-cowork-cookbook-dashboard-create-marketing-material"
description: "Pulls create-marketing-material data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_marketing_material", "rar_sha256": "fb106f2d6df5ec1ece79e881e4fd51dc3d890b2d4a15eab2f30a6e4f5f463e30", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
