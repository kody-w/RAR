---
name: "rar-cowork-cookbook-dashboard-track-employee-learning"
description: "Pulls employee learning data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_track_employee_learning", "rar_sha256": "cc8e1a75b9a36a04915aaa90d937cb9bff5f54336579c266be123be35fa069f0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_track_employee_learning`. The original RAPP
agent is preserved byte-for-byte in `dashboard_track_employee_learning_agent.py` and in the RCI capsule.

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

Track employee learning Interactive HTML Dashboard — Pulls employee learning data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-track-employee-learning
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
      "description": "Name of the HTML file to write, e.g. dashboard-track-employee-learning-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_track_employee_learning_agent.py` and embedded as the fenced Python below (sha256 cc8e1a75b9a36a04…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_track_employee_learning_agent.py` first:

```bash
python3 dashboard_track_employee_learning_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_track_employee_learning_agent.py   # or on stdin
python3 dashboard_track_employee_learning_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track employee learning Interactive HTML Dashboard — Pulls employee learning data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-track-employee-learning
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_track_employee_learning',
    "version": '3.0.3',
    "display_name": 'Track employee learning Interactive HTML Dashboard',
    "description": 'Pulls employee learning data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;',
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
        "upstream_slug": 'dashboard-track-employee-learning',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-track-employee-learning',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '468669b3098dc1c1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/track-employee-learning'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-track-employee-learning', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-track-employee-learning-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of track employee learning with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull track employee learning data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-track-employee-learning-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing track employee learning.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls employee learning data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;', 'example_request': 'Build an interactive HTML dashboard of employee learning from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-track-employee-learning-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser-viewable dashboard of employee learning data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardTrackEmployeeLearning(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardTrackEmployeeLearning'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-track-employee-learning-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardTrackEmployeeLearning().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
