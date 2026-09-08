---
name: "rar-cowork-cookbook-dashboard-develop-project-governance-strategy"
description: "Pulls project governance strategy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard, read-only, to the Cowork output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_project_governance_strategy", "rar_sha256": "639ae0d51915923dedda6ddc7f119576241fcfd3b535403b0506a700a406eceb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_project_governance_strategy`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_project_governance_strategy_agent.py` and in the RCI capsule.

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

Develop project governance strategy Interactive HTML Dashboard — Pulls project governance strategy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard, read-only, to the Cowork output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-project-governance-strategy
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
      "description": "D365 legal entity to pull from; defaults to USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-develop-project-governance-strategy-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated file; defaults to Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_project_governance_strategy_agent.py` and embedded as the fenced Python below (sha256 639ae0d51915923d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_project_governance_strategy_agent.py` first:

```bash
python3 dashboard_develop_project_governance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_project_governance_strategy_agent.py   # or on stdin
python3 dashboard_develop_project_governance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project governance strategy Interactive HTML Dashboard — Pulls project governance strategy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard, read-only, to the Cowork output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-project-governance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_project_governance_strategy',
    "version": '3.0.3',
    "display_name": 'Develop project governance strategy Interactive HTML Dashboard',
    "description": 'Pulls project governance strategy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard, read-only, to the Cowork output folder.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-project-governance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-project-governance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44140b34f0a620b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-governance-strategy'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-develop-project-governance-strategy', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-develop-project-governance-strategy-2026-05-24.html.', 'output_folder': 'Destination folder for the generated file; defaults to Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of develop project governance strategy with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull develop project governance strategy data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-develop-project-governance-strategy-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing develop project governance strategy.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls project governance strategy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard, read-only, to the Cowork output folder.', 'example_request': 'Build me an interactive HTML dashboard of project governance strategy from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-develop-project-governance-strategy-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated file; defaults to Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 project governance strategy data that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDevelopProjectGovernanceStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopProjectGovernanceStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-develop-project-governance-strategy-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated file; defaults to Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardDevelopProjectGovernanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
