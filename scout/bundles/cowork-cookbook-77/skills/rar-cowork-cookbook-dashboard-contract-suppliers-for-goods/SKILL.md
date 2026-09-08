---
name: "rar-cowork-cookbook-dashboard-contract-suppliers-for-goods"
description: "Pulls contract suppliers for goods data from Dynamics 365 F&SCM (read-only) for a legal entity and fiscal period, and saves a standalone interactive HTML dashboard with SVG charts, sortable table, and RAG indicator to th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_contract_suppliers_for_goods", "rar_sha256": "264bb3bfc0dc75b8606a46f2fbf8a2cfc02f0872907798cf83b0d50afb55e1ae", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
