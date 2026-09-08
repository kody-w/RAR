---
name: "rar-cowork-cookbook-dashboard-implement-cloud-solutions"
description: "Pulls implement cloud solutions data from Dynamics 365 F&SCM for a given legal entity and fiscal period via the D365 ERP plugin, and saves a standalone interactive HTML dashboard file to the Cowork output folder; read-on"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_implement_cloud_solutions", "rar_sha256": "eb23ce8b47ea68215c55e79751dd62a54dbaee6e2ec6caa0f967e7e5deac5bcb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_implement_cloud_solutions`. The original RAPP
agent is preserved byte-for-byte in `dashboard_implement_cloud_solutions_agent.py` and in the RCI capsule.

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

Implement cloud solutions Interactive HTML Dashboard — Pulls implement cloud solutions data from Dynamics 365 F&SCM for a given legal entity and fiscal period via the D365 ERP plugin, and saves a standalone interactive HTML dashboard file to the Cowork output folder; read-on

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-implement-cloud-solutions
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
      "description": "Name of the HTML file to write, e.g. dashboard-implement-cloud-solutions-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_implement_cloud_solutions_agent.py` and embedded as the fenced Python below (sha256 eb23ce8b47ea6821…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_implement_cloud_solutions_agent.py` first:

```bash
python3 dashboard_implement_cloud_solutions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_implement_cloud_solutions_agent.py   # or on stdin
python3 dashboard_implement_cloud_solutions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement cloud solutions Interactive HTML Dashboard — Pulls implement cloud solutions data from Dynamics 365 F&SCM for a given legal entity and fiscal period via the D365 ERP plugin, and saves a standalone interactive HTML dashboard file to the Cowork output folder; read-on

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-implement-cloud-solutions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_implement_cloud_solutions',
    "version": '3.0.3',
    "display_name": 'Implement cloud solutions Interactive HTML Dashboard',
    "description": 'Pulls implement cloud solutions data from Dynamics 365 F&SCM for a given legal entity and fiscal period via the D365 ERP plugin, and saves a standalone interactive HTML dashboard file to the Cowork output folder; read-on',
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
        "upstream_slug": 'dashboard-implement-cloud-solutions',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-implement-cloud-solutions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '528e2da84d8157f6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-cloud-solutions'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-implement-cloud-solutions', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-implement-cloud-solutions-2026-05-24.html.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of implement cloud solutions with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull implement cloud solutions data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-implement-cloud-solutions-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing implement cloud solutions.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls implement cloud solutions data from Dynamics 365 F&SCM for a given legal entity and fiscal period via the D365 ERP plugin, and saves a standalone interactive HTML dashboard file to the Cowork output folder; read-on', 'example_request': 'Build an interactive HTML dashboard of implement cloud solutions data from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-implement-cloud-solutions-2026-05-24.html.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable, self-contained dashboard of implement cloud solutions D365 data for people without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardImplementCloudSolutions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardImplementCloudSolutions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-implement-cloud-solutions-2026-05-24.html.', 'type': 'string'}},
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
    print(DashboardImplementCloudSolutions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
