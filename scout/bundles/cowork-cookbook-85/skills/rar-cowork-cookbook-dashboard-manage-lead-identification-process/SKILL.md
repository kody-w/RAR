---
name: "rar-cowork-cookbook-dashboard-manage-lead-identification-process"
description: "Pulls lead identification process data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fold"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_lead_identification_process", "rar_sha256": "5d0d373699363c0a201752d28f8d38ff129fe2ab41043c469a378b4bbce06d27", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_lead_identification_process`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_lead_identification_process_agent.py` and in the RCI capsule.

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

Manage lead identification process Interactive HTML Dashboard — Pulls lead identification process data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fold

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-lead-identification-process
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
      "description": "D365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-manage-lead-identification-process-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_lead_identification_process_agent.py` and embedded as the fenced Python below (sha256 5d0d373699363c0a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_lead_identification_process_agent.py` first:

```bash
python3 dashboard_manage_lead_identification_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_lead_identification_process_agent.py   # or on stdin
python3 dashboard_manage_lead_identification_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage lead identification process Interactive HTML Dashboard — Pulls lead identification process data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fold

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-lead-identification-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_lead_identification_process',
    "version": '3.0.3',
    "display_name": 'Manage lead identification process Interactive HTML Dashboard',
    "description": "Pulls lead identification process data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fold",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-lead-identification-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-lead-identification-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7fa23de9dfe10f19',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/manage-lead-identification-process'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/dashboard-manage-lead-identification-process', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-manage-lead-identification-process-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage lead identification process with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage lead identification process data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-lead-identification-process-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage lead identification process.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Pulls lead identification process data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fold", 'example_request': 'Build an interactive HTML dashboard of the lead identification process from D365 for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-manage-lead-identification-process-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 lead identification process data for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageLeadIdentificationProcess(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageLeadIdentificationProcess'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-manage-lead-identification-process-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardManageLeadIdentificationProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
