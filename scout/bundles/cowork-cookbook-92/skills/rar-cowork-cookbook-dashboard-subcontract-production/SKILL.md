---
name: "rar-cowork-cookbook-dashboard-subcontract-production"
description: "Pulls subcontract production data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; r"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_subcontract_production", "rar_sha256": "482ac7af3dcaaf8ea706b7538a5859bebf1eadcf4756c762fac97603d913e7f7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_subcontract_production`. The original RAPP
agent is preserved byte-for-byte in `dashboard_subcontract_production_agent.py` and in the RCI capsule.

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

Subcontract production Interactive HTML Dashboard — Pulls subcontract production data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; r

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-subcontract-production
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
      "description": "Name of the HTML file to write, e.g. dashboard-subcontract-production-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_subcontract_production_agent.py` and embedded as the fenced Python below (sha256 482ac7af3dcaaf8e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_subcontract_production_agent.py` first:

```bash
python3 dashboard_subcontract_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_subcontract_production_agent.py   # or on stdin
python3 dashboard_subcontract_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Subcontract production Interactive HTML Dashboard — Pulls subcontract production data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; r

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-subcontract-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_subcontract_production',
    "version": '3.0.3',
    "display_name": 'Subcontract production Interactive HTML Dashboard',
    "description": 'Pulls subcontract production data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; r',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-subcontract-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-subcontract-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '533358c333b7aaad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/subcontract-production'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-subcontract-production', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-subcontract-production-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of subcontract production with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull subcontract production data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-subcontract-production-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing subcontract production.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls subcontract production data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; r', 'example_request': 'Build a subcontract production dashboard for USMF for the latest fiscal period as an HTML file.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-subcontract-production-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants subcontract production figures from D365 packaged as a browser-viewable dashboard file for people without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardSubcontractProduction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardSubcontractProduction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-subcontract-production-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardSubcontractProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
