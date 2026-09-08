---
name: "rar-cowork-cookbook-dashboard-load-goods-for-shipping"
description: "Pulls load goods for shipping data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_load_goods_for_shipping", "rar_sha256": "fa361285f9ad8d84f78ed7b9f4560d5d7d590d967e5aac26ce0a1a6a4a3b8183", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_load_goods_for_shipping`. The original RAPP
agent is preserved byte-for-byte in `dashboard_load_goods_for_shipping_agent.py` and in the RCI capsule.

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

Load goods for shipping Interactive HTML Dashboard — Pulls load goods for shipping data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-load-goods-for-shipping
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
      "description": "Name of the HTML file to produce, e.g. dashboard-load-goods-for-shipping-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_load_goods_for_shipping_agent.py` and embedded as the fenced Python below (sha256 fa361285f9ad8d84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_load_goods_for_shipping_agent.py` first:

```bash
python3 dashboard_load_goods_for_shipping_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_load_goods_for_shipping_agent.py   # or on stdin
python3 dashboard_load_goods_for_shipping_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Load goods for shipping Interactive HTML Dashboard — Pulls load goods for shipping data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-load-goods-for-shipping
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_load_goods_for_shipping',
    "version": '3.0.3',
    "display_name": 'Load goods for shipping Interactive HTML Dashboard',
    "description": 'Pulls load goods for shipping data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o',
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
        "upstream_slug": 'dashboard-load-goods-for-shipping',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-load-goods-for-shipping',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5f35fe281a6a9556',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/load-goods-for-shipping'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-load-goods-for-shipping', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-load-goods-for-shipping-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of load goods for shipping with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull load goods for shipping data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-load-goods-for-shipping-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing load goods for shipping.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls load goods for shipping data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o', 'example_request': 'Build an interactive HTML dashboard of load goods for shipping in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-load-goods-for-shipping-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable dashboard of load goods for shipping data from D365 that can be shared with people who have no D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardLoadGoodsForShipping(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardLoadGoodsForShipping'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-load-goods-for-shipping-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardLoadGoodsForShipping().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
