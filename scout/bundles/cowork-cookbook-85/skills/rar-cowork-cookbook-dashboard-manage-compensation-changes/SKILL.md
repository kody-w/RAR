---
name: "rar-cowork-cookbook-dashboard-manage-compensation-changes"
description: "Pulls manage compensation changes data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_compensation_changes", "rar_sha256": "71cd1a6103c7bfa7c1314b6562b23ce4b8237c1a11805140a8c83731a2b85330", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_compensation_changes`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_compensation_changes_agent.py` and in the RCI capsule.

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

Manage compensation changes Interactive HTML Dashboard — Pulls manage compensation changes data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-compensation-changes
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
      "description": "Name of the HTML file to write, e.g. dashboard-manage-compensation-changes-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_compensation_changes_agent.py` and embedded as the fenced Python below (sha256 71cd1a6103c7bfa7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_compensation_changes_agent.py` first:

```bash
python3 dashboard_manage_compensation_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_compensation_changes_agent.py   # or on stdin
python3 dashboard_manage_compensation_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage compensation changes Interactive HTML Dashboard — Pulls manage compensation changes data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-compensation-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_compensation_changes',
    "version": '3.0.3',
    "display_name": 'Manage compensation changes Interactive HTML Dashboard',
    "description": 'Pulls manage compensation changes data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp',
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
        "upstream_slug": 'dashboard-manage-compensation-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-compensation-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b690e6bbfddca643',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/manage-compensation-changes'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-manage-compensation-changes', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-manage-compensation-changes-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage compensation changes with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage compensation changes data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-compensation-changes-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage compensation changes.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls manage compensation changes data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp', 'example_request': 'Build an HTML dashboard of compensation changes in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-manage-compensation-changes-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 compensation change data for viewers who have no D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageCompensationChanges(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageCompensationChanges'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-manage-compensation-changes-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardManageCompensationChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
