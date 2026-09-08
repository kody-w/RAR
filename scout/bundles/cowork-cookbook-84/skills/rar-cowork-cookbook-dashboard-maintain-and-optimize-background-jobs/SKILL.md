---
name: "rar-cowork-cookbook-dashboard-maintain-and-optimize-background-jobs"
description: "Pulls background job data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs", "rar_sha256": "a42787cfcc409f67996d231be83d8166fa822aaefe683d773bf9c7298019444b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `dashboard_maintain_and_optimize_background_jobs_agent.py` and in the RCI capsule.

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

Maintain and optimize background jobs Interactive HTML Dashboard — Pulls background job data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-and-optimize-background-jobs
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
      "description": "Name of the HTML file to write, e.g. dashboard-maintain-and-optimize-background-jobs-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_maintain_and_optimize_background_jobs_agent.py` and embedded as the fenced Python below (sha256 a42787cfcc409f67…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_maintain_and_optimize_background_jobs_agent.py` first:

```bash
python3 dashboard_maintain_and_optimize_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_maintain_and_optimize_background_jobs_agent.py   # or on stdin
python3 dashboard_maintain_and_optimize_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain and optimize background jobs Interactive HTML Dashboard — Pulls background job data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-and-optimize-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs',
    "version": '3.0.3',
    "display_name": 'Maintain and optimize background jobs Interactive HTML Dashboard',
    "description": 'Pulls background job data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl',
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
        "upstream_slug": 'dashboard-maintain-and-optimize-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-maintain-and-optimize-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '87e2a2b5d76a7772',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/maintain-and-optimize-background-jobs'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-maintain-and-optimize-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-maintain-and-optimize-background-jobs-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of maintain and optimize background jobs with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull maintain and optimize background jobs data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-maintain-and-optimize-background-jobs-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing maintain and optimize background jobs.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls background job data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl', 'example_request': 'Build an interactive HTML dashboard of background job maintenance for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-maintain-and-optimize-background-jobs-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser-viewable dashboard of D365 background job maintenance/optimization data without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMaintainAndOptimizeBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMaintainAndOptimizeBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-maintain-and-optimize-background-jobs-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardMaintainAndOptimizeBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
