---
name: "rar-cowork-cookbook-dashboard-manage-store-operations"
description: "Pulls store operations data from Dynamics 365 F&SCM (read-only) for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard with SVG charts, sortable table, and RAG indicator to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_store_operations", "rar_sha256": "33e8b31ec05a553ffde6078ef51b1655ce2780bfc607301f39f4560e8e50a1fe", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_store_operations`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_store_operations_agent.py` and in the RCI capsule.

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

Manage store operations Interactive HTML Dashboard — Pulls store operations data from Dynamics 365 F&SCM (read-only) for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard with SVG charts, sortable table, and RAG indicator to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-store-operations
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
      "description": "D365 legal entity to pull from, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-manage-store-operations-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_store_operations_agent.py` and embedded as the fenced Python below (sha256 33e8b31ec05a553f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_store_operations_agent.py` first:

```bash
python3 dashboard_manage_store_operations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_store_operations_agent.py   # or on stdin
python3 dashboard_manage_store_operations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage store operations Interactive HTML Dashboard — Pulls store operations data from Dynamics 365 F&SCM (read-only) for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard with SVG charts, sortable table, and RAG indicator to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-store-operations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_store_operations',
    "version": '3.0.3',
    "display_name": 'Manage store operations Interactive HTML Dashboard',
    "description": 'Pulls store operations data from Dynamics 365 F&SCM (read-only) for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard with SVG charts, sortable table, and RAG indicator to the out',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-store-operations',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-store-operations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b78e3238fc9e5ed4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-store-operations'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-manage-store-operations', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-manage-store-operations-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage store operations with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage store operations data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-store-operations-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage store operations.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls store operations data from Dynamics 365 F&SCM (read-only) for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard with SVG charts, sortable table, and RAG indicator to the out', 'example_request': 'Build me an interactive store operations dashboard for USMF for the latest fiscal period as an HTML file.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-manage-store-operations-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser-viewable store operations dashboard built from D365 ERP data without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageStoreOperations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageStoreOperations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-manage-store-operations-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardManageStoreOperations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
