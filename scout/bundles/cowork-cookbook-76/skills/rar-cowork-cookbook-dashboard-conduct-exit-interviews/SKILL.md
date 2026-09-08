---
name: "rar-cowork-cookbook-dashboard-conduct-exit-interviews"
description: "Pulls conduct exit interviews data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard with totals header, inline SVG charts, sortable table, a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_conduct_exit_interviews", "rar_sha256": "c0869fe3213b20ae4895f21c464ae309c1e81122762b2767844e26041db3bea1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_conduct_exit_interviews`. The original RAPP
agent is preserved byte-for-byte in `dashboard_conduct_exit_interviews_agent.py` and in the RCI capsule.

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

Conduct exit interviews Interactive HTML Dashboard — Pulls conduct exit interviews data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard with totals header, inline SVG charts, sortable table, a

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-conduct-exit-interviews
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
      "description": "D365 legal entity to pull from; defaults to USMF.",
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
      "description": "Name of the generated HTML file, e.g. dashboard-conduct-exit-interviews-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_conduct_exit_interviews_agent.py` and embedded as the fenced Python below (sha256 c0869fe3213b20ae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_conduct_exit_interviews_agent.py` first:

```bash
python3 dashboard_conduct_exit_interviews_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_conduct_exit_interviews_agent.py   # or on stdin
python3 dashboard_conduct_exit_interviews_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct exit interviews Interactive HTML Dashboard — Pulls conduct exit interviews data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard with totals header, inline SVG charts, sortable table, a

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-conduct-exit-interviews
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_conduct_exit_interviews',
    "version": '3.0.3',
    "display_name": 'Conduct exit interviews Interactive HTML Dashboard',
    "description": 'Pulls conduct exit interviews data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard with totals header, inline SVG charts, sortable table, a',
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
        "upstream_slug": 'dashboard-conduct-exit-interviews',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-conduct-exit-interviews',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '445e4acac81cf1fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/conduct-exit-interviews'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-conduct-exit-interviews', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from; defaults to USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-conduct-exit-interviews-2026-05-24.html.', 'output_folder': 'Destination folder for the HTML file, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of conduct exit interviews with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull conduct exit interviews data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-conduct-exit-interviews-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing conduct exit interviews.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls conduct exit interviews data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard with totals header, inline SVG charts, sortable table, a', 'example_request': 'Build me an interactive HTML dashboard of conduct exit interviews from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-conduct-exit-interviews-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the HTML file, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of conduct exit interviews data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardConductExitInterviews(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConductExitInterviews'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-conduct-exit-interviews-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the HTML file, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardConductExitInterviews().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
