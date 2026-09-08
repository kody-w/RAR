---
name: "rar-cowork-cookbook-dashboard-implement-project-governance-approach"
description: "Pulls project governance data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_implement_project_governance_approach", "rar_sha256": "6717e94956cb493597bcd91cf5b51647c71cf0629653533cb558cdda8636abbd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_implement_project_governance_approach`. The original RAPP
agent is preserved byte-for-byte in `dashboard_implement_project_governance_approach_agent.py` and in the RCI capsule.

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

Implement project governance approach Interactive HTML Dashboard — Pulls project governance data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-o

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-implement-project-governance-approach
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
      "description": "Name of the generated HTML file, e.g. dashboard-implement-project-governance-approach-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the HTML file, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_implement_project_governance_approach_agent.py` and embedded as the fenced Python below (sha256 6717e94956cb4935…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_implement_project_governance_approach_agent.py` first:

```bash
python3 dashboard_implement_project_governance_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_implement_project_governance_approach_agent.py   # or on stdin
python3 dashboard_implement_project_governance_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement project governance approach Interactive HTML Dashboard — Pulls project governance data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-o

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-implement-project-governance-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_implement_project_governance_approach',
    "version": '3.0.3',
    "display_name": 'Implement project governance approach Interactive HTML Dashboard',
    "description": 'Pulls project governance data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-o',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-implement-project-governance-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-implement-project-governance-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0d9164fa711ec25c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-project-governance-approach'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-implement-project-governance-approach', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-implement-project-governance-approach-2026-05-24.html.', 'output_folder': 'Destination folder for the HTML file, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of implement project governance approach with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull implement project governance approach data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-implement-project-governance-approach-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing implement project governance approach.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls project governance data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-o', 'example_request': 'Build an interactive HTML dashboard of project governance data from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-implement-project-governance-approach-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the HTML file, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 project governance data for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardImplementProjectGovernanceApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardImplementProjectGovernanceApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-implement-project-governance-approach-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the HTML file, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardImplementProjectGovernanceApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
