---
name: "rar-cowork-cookbook-dashboard-implement-cloud-solutions"
description: "Pulls implement cloud solutions data from Dynamics 365 F&SCM for a given legal entity and fiscal period via the D365 ERP plugin, and saves a standalone interactive HTML dashboard file to the Cowork output folder; read-on"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_implement_cloud_solutions", "rar_sha256": "eb23ce8b47ea68215c55e79751dd62a54dbaee6e2ec6caa0f967e7e5deac5bcb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
