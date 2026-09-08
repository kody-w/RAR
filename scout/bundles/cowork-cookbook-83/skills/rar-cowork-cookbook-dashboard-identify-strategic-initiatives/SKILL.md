---
name: "rar-cowork-cookbook-dashboard-identify-strategic-initiatives"
description: "Pulls strategic-initiatives data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_strategic_initiatives", "rar_sha256": "f21b7cee92e83e1bd993d68b98c53cae03952d7816287aeeef1a0636f6ea7ca7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_identify_strategic_initiatives`. The original RAPP
agent is preserved byte-for-byte in `dashboard_identify_strategic_initiatives_agent.py` and in the RCI capsule.

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

Identify strategic initiatives Interactive HTML Dashboard — Pulls strategic-initiatives data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; re

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-strategic-initiatives
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
      "description": "Name of the HTML file to write, e.g. dashboard-identify-strategic-initiatives-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_strategic_initiatives_agent.py` and embedded as the fenced Python below (sha256 f21b7cee92e83e1b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_strategic_initiatives_agent.py` first:

```bash
python3 dashboard_identify_strategic_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_strategic_initiatives_agent.py   # or on stdin
python3 dashboard_identify_strategic_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify strategic initiatives Interactive HTML Dashboard — Pulls strategic-initiatives data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; re

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-strategic-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_strategic_initiatives',
    "version": '3.0.3',
    "display_name": 'Identify strategic initiatives Interactive HTML Dashboard',
    "description": "Pulls strategic-initiatives data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; re",
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
        "upstream_slug": 'dashboard-identify-strategic-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-strategic-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '72417a307cb20565',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/identify-strategic-initiatives'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-identify-strategic-initiatives', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-identify-strategic-initiatives-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of identify strategic initiatives with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull identify strategic initiatives data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-identify-strategic-initiatives-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing identify strategic initiatives.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Pulls strategic-initiatives data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; re", 'example_request': 'Build an interactive HTML dashboard of strategic initiatives from D365 for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-identify-strategic-initiatives-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-openable dashboard of D365 strategic initiatives that viewers can read without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardIdentifyStrategicInitiatives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyStrategicInitiatives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-identify-strategic-initiatives-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardIdentifyStrategicInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
