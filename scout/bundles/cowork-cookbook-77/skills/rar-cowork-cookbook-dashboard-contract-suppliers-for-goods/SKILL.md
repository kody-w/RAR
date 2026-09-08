---
name: "rar-cowork-cookbook-dashboard-contract-suppliers-for-goods"
description: "Pulls contract suppliers for goods data from Dynamics 365 F&SCM (read-only) for a legal entity and fiscal period, and saves a standalone interactive HTML dashboard with SVG charts, sortable table, and RAG indicator to th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_contract_suppliers_for_goods", "rar_sha256": "264bb3bfc0dc75b8606a46f2fbf8a2cfc02f0872907798cf83b0d50afb55e1ae", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_contract_suppliers_for_goods`. The original RAPP
agent is preserved byte-for-byte in `dashboard_contract_suppliers_for_goods_agent.py` and in the RCI capsule.

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

Contract suppliers for goods Interactive HTML Dashboard — Pulls contract suppliers for goods data from Dynamics 365 F&SCM (read-only) for a legal entity and fiscal period, and saves a standalone interactive HTML dashboard with SVG charts, sortable table, and RAG indicator to th

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-contract-suppliers-for-goods
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
      "description": "Name of the HTML file to write, e.g. dashboard-contract-suppliers-for-goods-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the file, normally Documents/Cowork/output in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_contract_suppliers_for_goods_agent.py` and embedded as the fenced Python below (sha256 264bb3bfc0dc75b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_contract_suppliers_for_goods_agent.py` first:

```bash
python3 dashboard_contract_suppliers_for_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_contract_suppliers_for_goods_agent.py   # or on stdin
python3 dashboard_contract_suppliers_for_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Contract suppliers for goods Interactive HTML Dashboard — Pulls contract suppliers for goods data from Dynamics 365 F&SCM (read-only) for a legal entity and fiscal period, and saves a standalone interactive HTML dashboard with SVG charts, sortable table, and RAG indicator to th

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-contract-suppliers-for-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_contract_suppliers_for_goods',
    "version": '3.0.3',
    "display_name": 'Contract suppliers for goods Interactive HTML Dashboard',
    "description": 'Pulls contract suppliers for goods data from Dynamics 365 F&SCM (read-only) for a legal entity and fiscal period, and saves a standalone interactive HTML dashboard with SVG charts, sortable table, and RAG indicator to th',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-contract-suppliers-for-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-contract-suppliers-for-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1b99b7330839af02',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/contract-suppliers-for-goods'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-contract-suppliers-for-goods', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-contract-suppliers-for-goods-2026-05-24.html.', 'output_folder': 'Destination folder for the file, normally Documents/Cowork/output in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of contract suppliers for goods with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull contract suppliers for goods data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-contract-suppliers-for-goods-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing contract suppliers for goods.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls contract suppliers for goods data from Dynamics 365 F&SCM (read-only) for a legal entity and fiscal period, and saves a standalone interactive HTML dashboard with SVG charts, sortable table, and RAG indicator to th', 'example_request': 'Build me an interactive HTML dashboard of contract suppliers for goods in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-contract-suppliers-for-goods-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the file, normally Documents/Cowork/output in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of contract suppliers for goods from D365, without the viewer needing D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardContractSuppliersForGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardContractSuppliersForGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-contract-suppliers-for-goods-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the file, normally Documents/Cowork/output in OneDrive.', 'type': 'string'}},
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
    print(DashboardContractSuppliersForGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
