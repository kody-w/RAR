---
name: "rar-cowork-cookbook-dashboard-handle-quarantine-goods"
description: "Pulls quarantine goods data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; r"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_handle_quarantine_goods", "rar_sha256": "61e911a722fff40538176baa5d455e705c4d8c8e90efceea1c788264bbd4acba", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_handle_quarantine_goods`. The original RAPP
agent is preserved byte-for-byte in `dashboard_handle_quarantine_goods_agent.py` and in the RCI capsule.

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

Handle quarantine goods Interactive HTML Dashboard — Pulls quarantine goods data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; r

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-handle-quarantine-goods
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
      "description": "Name of the HTML file to write, e.g. dashboard-handle-quarantine-goods-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder to save the HTML file, typically Documents/Cowork/output in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_handle_quarantine_goods_agent.py` and embedded as the fenced Python below (sha256 61e911a722fff405…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_handle_quarantine_goods_agent.py` first:

```bash
python3 dashboard_handle_quarantine_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_handle_quarantine_goods_agent.py   # or on stdin
python3 dashboard_handle_quarantine_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Handle quarantine goods Interactive HTML Dashboard — Pulls quarantine goods data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; r

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-handle-quarantine-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_handle_quarantine_goods',
    "version": '3.0.3',
    "display_name": 'Handle quarantine goods Interactive HTML Dashboard',
    "description": 'Pulls quarantine goods data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; r',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-handle-quarantine-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-handle-quarantine-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd27dd57c57be83c2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/handle-quarantine-goods'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-handle-quarantine-goods', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-handle-quarantine-goods-2026-05-24.html.', 'output_folder': 'Folder to save the HTML file, typically Documents/Cowork/output in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of handle quarantine goods with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull handle quarantine goods data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-handle-quarantine-goods-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing handle quarantine goods.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls quarantine goods data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; r', 'example_request': 'Build me an interactive HTML dashboard for quarantine goods in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-handle-quarantine-goods-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder to save the HTML file, typically Documents/Cowork/output in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of quarantine goods handling from D365 for viewers who have no D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardHandleQuarantineGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardHandleQuarantineGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-handle-quarantine-goods-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder to save the HTML file, typically Documents/Cowork/output in OneDrive.', 'type': 'string'}},
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
    print(DashboardHandleQuarantineGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
