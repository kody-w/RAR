---
name: "rar-cowork-cookbook-dashboard-train-employees"
description: "Pulls train employees data from Dynamics 365 F&SCM for a legal entity and the most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_train_employees", "rar_sha256": "4b21b02cf604959215b27a705e4054f60346d6003944186fdbf5b61dbb31b115", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_train_employees`. The original RAPP
agent is preserved byte-for-byte in `dashboard_train_employees_agent.py` and in the RCI capsule.

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

Train employees Interactive HTML Dashboard — Pulls train employees data from Dynamics 365 F&SCM for a legal entity and the most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-train-employees
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
      "description": "Name of the HTML file to produce, e.g. dashboard-train-employees-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_train_employees_agent.py` and embedded as the fenced Python below (sha256 4b21b02cf6049592…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_train_employees_agent.py` first:

```bash
python3 dashboard_train_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_train_employees_agent.py   # or on stdin
python3 dashboard_train_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Train employees Interactive HTML Dashboard — Pulls train employees data from Dynamics 365 F&SCM for a legal entity and the most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-train-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_train_employees',
    "version": '3.0.3',
    "display_name": 'Train employees Interactive HTML Dashboard',
    "description": 'Pulls train employees data from Dynamics 365 F&SCM for a legal entity and the most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-train-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-train-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ec55f41e453abb27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/train-employees'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-train-employees', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-train-employees-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of train employees with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull train employees data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-train-employees-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing train employees.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls train employees data from Dynamics 365 F&SCM for a legal entity and the most recent fiscal period, then saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator', 'example_request': 'Build me an interactive HTML dashboard of train employees from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-train-employees-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser-viewable dashboard of train employees data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardTrainEmployees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardTrainEmployees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-train-employees-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardTrainEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
