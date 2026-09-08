---
name: "rar-cowork-cookbook-dashboard-identify-strategic-initiatives"
description: "Pulls strategic-initiatives data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_strategic_initiatives", "rar_sha256": "f21b7cee92e83e1bd993d68b98c53cae03952d7816287aeeef1a0636f6ea7ca7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
