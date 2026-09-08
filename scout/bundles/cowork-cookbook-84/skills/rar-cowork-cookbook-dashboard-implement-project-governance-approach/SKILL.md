---
name: "rar-cowork-cookbook-dashboard-implement-project-governance-approach"
description: "Pulls project governance data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_implement_project_governance_approach", "rar_sha256": "6717e94956cb493597bcd91cf5b51647c71cf0629653533cb558cdda8636abbd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
