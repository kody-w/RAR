---
name: "rar-cowork-cookbook-dashboard-manage-lead-identification-process"
description: "Pulls lead identification process data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fold"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_lead_identification_process", "rar_sha256": "5d0d373699363c0a201752d28f8d38ff129fe2ab41043c469a378b4bbce06d27", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
