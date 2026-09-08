---
name: "rar-cowork-cookbook-dashboard-correct-production-processes"
description: "Pulls read-only production process data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard file to the Cowork output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_production_processes", "rar_sha256": "247f6a05e51343198fac9279698c3b1815cb9d39bddafed1fc4024e3f34bfba0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_correct_production_processes`. The original RAPP
agent is preserved byte-for-byte in `dashboard_correct_production_processes_agent.py` and in the RCI capsule.

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

Correct production processes Interactive HTML Dashboard — Pulls read-only production process data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard file to the Cowork output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-production-processes
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
      "description": "Fiscal period to pull; defaults to the most recent available.",
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
      "description": "Name of the HTML file to produce, e.g. dashboard-correct-production-processes-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the file, normally Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_correct_production_processes_agent.py` and embedded as the fenced Python below (sha256 247f6a05e5134319…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_correct_production_processes_agent.py` first:

```bash
python3 dashboard_correct_production_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_correct_production_processes_agent.py   # or on stdin
python3 dashboard_correct_production_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct production processes Interactive HTML Dashboard — Pulls read-only production process data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard file to the Cowork output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-production-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_correct_production_processes',
    "version": '3.0.3',
    "display_name": 'Correct production processes Interactive HTML Dashboard',
    "description": 'Pulls read-only production process data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard file to the Cowork output folder.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-correct-production-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-correct-production-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '239bb824dd8b4695',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/correct-production-processes'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-correct-production-processes', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-correct-production-processes-2026-05-24.html.', 'output_folder': 'Destination folder for the file, normally Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of correct production processes with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull correct production processes data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-correct-production-processes-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing correct production processes.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls read-only production process data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard file to the Cowork output folder.', 'example_request': 'Build an interactive HTML dashboard of production processes from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-correct-production-processes-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the file, normally Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser-viewable dashboard of production process data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardCorrectProductionProcesses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCorrectProductionProcesses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-correct-production-processes-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the file, normally Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardCorrectProductionProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
