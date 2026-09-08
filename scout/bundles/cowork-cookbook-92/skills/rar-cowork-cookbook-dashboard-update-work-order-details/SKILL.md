---
name: "rar-cowork-cookbook-dashboard-update-work-order-details"
description: "Pulls update work order details data from Dynamics 365 F&SCM for a legal entity and recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_update_work_order_details", "rar_sha256": "2c73607757293de6217b0f9e92fe67930a0564e2c8aa6062a056a0e382893799", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_update_work_order_details`. The original RAPP
agent is preserved byte-for-byte in `dashboard_update_work_order_details_agent.py` and in the RCI capsule.

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

Update work order details Interactive HTML Dashboard — Pulls update work order details data from Dynamics 365 F&SCM for a legal entity and recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-update-work-order-details
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
      "description": "Name of the HTML file to write, e.g. dashboard-update-work-order-details-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_update_work_order_details_agent.py` and embedded as the fenced Python below (sha256 2c73607757293de6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_update_work_order_details_agent.py` first:

```bash
python3 dashboard_update_work_order_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_update_work_order_details_agent.py   # or on stdin
python3 dashboard_update_work_order_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update work order details Interactive HTML Dashboard — Pulls update work order details data from Dynamics 365 F&SCM for a legal entity and recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-update-work-order-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_update_work_order_details',
    "version": '3.0.3',
    "display_name": 'Update work order details Interactive HTML Dashboard',
    "description": 'Pulls update work order details data from Dynamics 365 F&SCM for a legal entity and recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-update-work-order-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-update-work-order-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e0fa2a30a9b4796e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/update-work-order-details'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-update-work-order-details', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-update-work-order-details-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of update work order details with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull update work order details data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-update-work-order-details-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing update work order details.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls update work order details data from Dynamics 365 F&SCM for a legal entity and recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folde', 'example_request': 'Build an interactive HTML dashboard of update work order details for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-update-work-order-details-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants work order detail data from D365 rendered as a shareable browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardUpdateWorkOrderDetails(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardUpdateWorkOrderDetails'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-update-work-order-details-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardUpdateWorkOrderDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
