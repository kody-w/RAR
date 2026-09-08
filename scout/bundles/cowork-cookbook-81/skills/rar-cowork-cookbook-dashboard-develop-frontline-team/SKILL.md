---
name: "rar-cowork-cookbook-dashboard-develop-frontline-team"
description: "Pulls develop frontline team data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_frontline_team", "rar_sha256": "f9f0cd18acf4c5d651ab44a5a34ea31d2374c9f98c89253231b2a9155d013559", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_frontline_team`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_frontline_team_agent.py` and in the RCI capsule.

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

Develop frontline team Interactive HTML Dashboard — Pulls develop frontline team data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-frontline-team
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Name of the HTML file to create, e.g. dashboard-develop-frontline-team-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated file, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_frontline_team_agent.py` and embedded as the fenced Python below (sha256 f9f0cd18acf4c5d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_frontline_team_agent.py` first:

```bash
python3 dashboard_develop_frontline_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_frontline_team_agent.py   # or on stdin
python3 dashboard_develop_frontline_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop frontline team Interactive HTML Dashboard — Pulls develop frontline team data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-frontline-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_frontline_team',
    "version": '3.0.3',
    "display_name": 'Develop frontline team Interactive HTML Dashboard',
    "description": 'Pulls develop frontline team data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) and writes a standalone interactive HTML dashboard file to the output folder, read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-frontline-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-frontline-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c0983789ff77e056',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-frontline-team'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-develop-frontline-team', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the HTML file to create, e.g. dashboard-develop-frontline-team-2026-05-24.html.', 'output_folder': 'Destination folder for the generated file, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of develop frontline team with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull develop frontline team data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-develop-frontline-team-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing develop frontline team.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls develop frontline team data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) and writes a standalone interactive HTML dashboard file to the output folder, read-only.', 'example_request': 'Build the develop frontline team HTML dashboard from USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to create, e.g. dashboard-develop-frontline-team-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated file, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of develop frontline team D365 data that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDevelopFrontlineTeam(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopFrontlineTeam'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to create, e.g. dashboard-develop-frontline-team-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated file, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDevelopFrontlineTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
