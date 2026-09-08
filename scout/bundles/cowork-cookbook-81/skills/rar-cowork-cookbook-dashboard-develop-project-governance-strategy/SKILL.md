---
name: "rar-cowork-cookbook-dashboard-develop-project-governance-strategy"
description: "Pulls project governance strategy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard, read-only, to the Cowork output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_project_governance_strategy", "rar_sha256": "639ae0d51915923dedda6ddc7f119576241fcfd3b535403b0506a700a406eceb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
