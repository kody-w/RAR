---
name: "rar-cowork-cookbook-dashboard-manage-compensation-changes"
description: "Pulls manage compensation changes data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_compensation_changes", "rar_sha256": "71cd1a6103c7bfa7c1314b6562b23ce4b8237c1a11805140a8c83731a2b85330", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
