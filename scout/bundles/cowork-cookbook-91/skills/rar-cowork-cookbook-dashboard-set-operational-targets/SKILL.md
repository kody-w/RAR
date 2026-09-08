---
name: "rar-cowork-cookbook-dashboard-set-operational-targets"
description: "Generates a standalone interactive HTML dashboard for operational targets from Dynamics 365 ERP data (legal entity USMF, most recent fiscal period), with SVG charts, sortable table, and RAG indicator; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_set_operational_targets", "rar_sha256": "2625b99ca69dc262f7e494414e0df78c55c11990e031c7c86d089d2988109c37", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_set_operational_targets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_set_operational_targets_agent.py` and in the RCI capsule.

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

Set operational targets Interactive HTML Dashboard — Generates a standalone interactive HTML dashboard for operational targets from Dynamics 365 ERP data (legal entity USMF, most recent fiscal period), with SVG charts, sortable table, and RAG indicator; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-operational-targets
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
      "description": "D365 legal entity to pull data from; defaults to USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-set-operational-targets-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_set_operational_targets_agent.py` and embedded as the fenced Python below (sha256 2625b99ca69dc262…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_set_operational_targets_agent.py` first:

```bash
python3 dashboard_set_operational_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_set_operational_targets_agent.py   # or on stdin
python3 dashboard_set_operational_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set operational targets Interactive HTML Dashboard — Generates a standalone interactive HTML dashboard for operational targets from Dynamics 365 ERP data (legal entity USMF, most recent fiscal period), with SVG charts, sortable table, and RAG indicator; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-operational-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_set_operational_targets',
    "version": '3.0.3',
    "display_name": 'Set operational targets Interactive HTML Dashboard',
    "description": 'Generates a standalone interactive HTML dashboard for operational targets from Dynamics 365 ERP data (legal entity USMF, most recent fiscal period), with SVG charts, sortable table, and RAG indicator; read-only.',
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
        "upstream_slug": 'dashboard-set-operational-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-set-operational-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c187ff48f63ffb49',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/set-operational-targets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-set-operational-targets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull data from; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-set-operational-targets-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of set operational targets with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull set operational targets data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-set-operational-targets-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing set operational targets.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a standalone interactive HTML dashboard for operational targets from Dynamics 365 ERP data (legal entity USMF, most recent fiscal period), with SVG charts, sortable table, and RAG indicator; read-only.', 'example_request': 'Build an operational targets dashboard from D365 USMF for the latest fiscal period as an HTML file.', 'inputs': [{'description': 'D365 legal entity to pull data from; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-set-operational-targets-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants operational targets from D365 F&SCM turned into a shareable browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardSetOperationalTargets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardSetOperationalTargets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-set-operational-targets-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardSetOperationalTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
