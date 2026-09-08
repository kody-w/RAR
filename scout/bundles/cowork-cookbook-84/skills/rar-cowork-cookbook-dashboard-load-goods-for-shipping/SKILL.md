---
name: "rar-cowork-cookbook-dashboard-load-goods-for-shipping"
description: "Pulls load goods for shipping data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_load_goods_for_shipping", "rar_sha256": "fa361285f9ad8d84f78ed7b9f4560d5d7d590d967e5aac26ce0a1a6a4a3b8183", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
