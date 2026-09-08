---
name: "rar-cowork-cookbook-dashboard-manage-store-operations"
description: "Pulls store operations data from Dynamics 365 F&SCM (read-only) for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard with SVG charts, sortable table, and RAG indicator to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_store_operations", "rar_sha256": "33e8b31ec05a553ffde6078ef51b1655ce2780bfc607301f39f4560e8e50a1fe", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
