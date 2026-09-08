---
name: "rar-cowork-cookbook-3d-warehouse-heatmap"
description: "Reads on-hand inventory by location for one warehouse in Dynamics 365 F&SCM and returns a standalone interactive 3D HTML file of bins colored by fill percentage, labeled by item count."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/3d_warehouse_heatmap", "rar_sha256": "f4581a3e408052af70ae79d5b958368d75f3b3105b458c27d434db85cf862ec4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/3d_warehouse_heatmap`. The original RAPP
agent is preserved byte-for-byte in `3d_warehouse_heatmap_agent.py` and in the RCI capsule.

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

3D Warehouse Inventory Heatmap (HTML) — Reads on-hand inventory by location for one warehouse in Dynamics 365 F&SCM and returns a standalone interactive 3D HTML file of bins colored by fill percentage, labeled by item count.

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
  Upstream entry : https://coworkcookbook.com/recipes/3d-warehouse-heatmap
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
    "output_folder": {
      "description": "Folder where the generated Warehouse-3D-<warehouse>-<YYYY-MM-DD>.html file is saved.",
      "type": "string"
    },
    "warehouse": {
      "description": "Which warehouse to visualize; defaults to the primary USMF warehouse (e.g. 24) if unspecified.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `3d_warehouse_heatmap_agent.py` and embedded as the fenced Python below (sha256 f4581a3e408052af…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `3d_warehouse_heatmap_agent.py` first:

```bash
python3 3d_warehouse_heatmap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 3d_warehouse_heatmap_agent.py   # or on stdin
python3 3d_warehouse_heatmap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
3D Warehouse Inventory Heatmap (HTML) — Reads on-hand inventory by location for one warehouse in Dynamics 365 F&SCM and returns a standalone interactive 3D HTML file of bins colored by fill percentage, labeled by item count.

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
  Upstream entry : https://coworkcookbook.com/recipes/3d-warehouse-heatmap
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/3d_warehouse_heatmap',
    "version": '3.0.3',
    "display_name": '3D Warehouse Inventory Heatmap (HTML)',
    "description": 'Reads on-hand inventory by location for one warehouse in Dynamics 365 F&SCM and returns a standalone interactive 3D HTML file of bins colored by fill percentage, labeled by item count.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": '3d-warehouse-heatmap',
        "upstream_url": 'https://coworkcookbook.com/recipes/3d-warehouse-heatmap',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b41eb263135f6c3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/3d-warehouse-heatmap', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Warehouse manager role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: One standalone interactive 3D HTML file.'], 'confidence': 1.0, 'deliverable': 'One standalone interactive 3D HTML file.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'output_folder': 'Folder where the generated Warehouse-3D-<warehouse>-<YYYY-MM-DD>.html file is saved.', 'warehouse': 'Which warehouse to visualize; defaults to the primary USMF warehouse (e.g. 24) if unspecified.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Turns the warehouse on-hand snapshot into a spatial picture so ops can see at a glance where slow-movers are blocking prime pick locations and where capacity is genuinely full vs just disorganized.', 'expected_output': 'One standalone interactive 3D HTML file.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Warehouse manager role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Read on-hand inventory by warehouse location for a single warehouse (ask the user which one, default to the primary USMF warehouse e.g. 24 if unspecified). For each location, capture aisle, rack, shelf, bin, item count, on-hand quantity, and on-hand value. Produce a standalone HTML file 'Warehouse-3D-<warehouse>-<YYYY-MM-DD>.html' that renders a 3D grid (use three.js via CDN) where each bin is a colored cube — color by fill percentage (green = empty, red = at capacity) and label by item count on hover. Include orbit controls, a legend, and a header with the warehouse name and snapshot time. Save the HTML to the output folder.", 'steps': ['Paste the prompt and confirm the warehouse when asked.', 'Open the HTML in your browser and orbit/pan to inspect bins.', 'Share via Teams to the warehouse leads.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF Warehouse 24. Cowork produced 'Warehouse-3D-24-2026-05-23.html' rendering all 45 locations as colored cubes via three.js with orbit controls, zone labels (BULK / FLOOR / PICKZONE 1/2/3 / WEBSHOP1 / SERVICE), fill-% color scale, and per-bin hover tooltips. Total on-hand: 2,370 units / $859,050. Two honest data caveats surfaced by the agent: (a) USMF doesn't populate aisle/rack/shelf/bin metadata for WH 24 — Cowork derived a meaningful grid layout from zone + location ID instead; (b) D365 only exposes on-hand at the warehouse level via OData — Cowork distributed totals across likely zones by item-series convention. Both caveats are documented in the agent's output.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Renders an interactive 3D warehouse view in a single HTML file — opens in any browser, no D365 access needed by the viewer.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads on-hand inventory by location for one warehouse in Dynamics 365 F&SCM and returns a standalone interactive 3D HTML file of bins colored by fill percentage, labeled by item count.', 'example_request': 'Build a 3D inventory heatmap of warehouse 24 as an HTML file I can open in my browser.', 'inputs': [{'description': 'Which warehouse to visualize; defaults to the primary USMF warehouse (e.g. 24) if unspecified.', 'name': 'warehouse'}, {'description': 'Folder where the generated Warehouse-3D-<warehouse>-<YYYY-MM-DD>.html file is saved.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': "Call when a user wants a browser-viewable 3D visualization of a single warehouse's bin-level on-hand inventory and fill levels."}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt and confirm the warehouse when asked.', 'Open the HTML in your browser and orbit/pan to inspect bins.', 'Share via Teams to the warehouse leads.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class Agent3dWarehouseHeatmap(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'Agent3dWarehouseHeatmap'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_folder': {'description': 'Folder where the generated Warehouse-3D-<warehouse>-<YYYY-MM-DD>.html file is saved.', 'type': 'string'}, 'warehouse': {'description': 'Which warehouse to visualize; defaults to the primary USMF warehouse (e.g. 24) if unspecified.', 'type': 'string'}},
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
    print(Agent3dWarehouseHeatmap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
