---
name: "rar-cowork-cookbook-dashboard-handle-quarantine-goods"
description: "Pulls quarantine goods data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; r"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_handle_quarantine_goods", "rar_sha256": "61e911a722fff40538176baa5d455e705c4d8c8e90efceea1c788264bbd4acba", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
