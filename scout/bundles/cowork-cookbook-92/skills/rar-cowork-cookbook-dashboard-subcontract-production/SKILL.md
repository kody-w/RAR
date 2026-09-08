---
name: "rar-cowork-cookbook-dashboard-subcontract-production"
description: "Pulls subcontract production data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; r"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_subcontract_production", "rar_sha256": "482ac7af3dcaaf8ea706b7538a5859bebf1eadcf4756c762fac97603d913e7f7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
