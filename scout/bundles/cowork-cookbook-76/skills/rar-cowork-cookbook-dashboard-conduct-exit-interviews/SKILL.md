---
name: "rar-cowork-cookbook-dashboard-conduct-exit-interviews"
description: "Pulls conduct exit interviews data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard with totals header, inline SVG charts, sortable table, a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_conduct_exit_interviews", "rar_sha256": "c0869fe3213b20ae4895f21c464ae309c1e81122762b2767844e26041db3bea1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
