---
name: "rar-cowork-cookbook-dashboard-track-employee-learning"
description: "Pulls employee learning data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_track_employee_learning", "rar_sha256": "cc8e1a75b9a36a04915aaa90d937cb9bff5f54336579c266be123be35fa069f0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
