---
name: "rar-cowork-cookbook-dashboard-correct-production-processes"
description: "Pulls read-only production process data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard file to the Cowork output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_production_processes", "rar_sha256": "247f6a05e51343198fac9279698c3b1815cb9d39bddafed1fc4024e3f34bfba0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
