---
name: "rar-cowork-cookbook-3d-warehouse-heatmap"
description: "Reads on-hand inventory by location for one warehouse in Dynamics 365 F&SCM and returns a standalone interactive 3D HTML file of bins colored by fill percentage, labeled by item count."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/3d_warehouse_heatmap", "rar_sha256": "f4581a3e408052af70ae79d5b958368d75f3b3105b458c27d434db85cf862ec4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V66bKjSJbmq2hum01mNhFXiFVEd7WNAIFAAgFikzLKItn3RayCnHz3cXRvRGZWRdV0mc2fUSwSjvvZz3eOm/uvL07fxVXz8unlEjjlinfyPImDZuWU/oqpxqrJwFeVueDfyqvKrkncvqua9uXDix+0XpPUXVKVYLkWOH67qsqP8bI0KYegBPOmlTut8spzllmrsGrAjGA1Ok0QV30bgHkrdiqdIvHaFUrgK+5/XhjpybwJur4p25Wzajvw7OTLwqTsgsbxumQIVii7OujSaRUmebCqwpWbgNlelVdN4C9cwXi+qoPGA4I4UfBhlTtukL+9S7qgAHP7snsFigQPp6jzoH359PNfP7wk4PfLp19fvNxpwdDLLgIEUN/6KvMhcLrCqcG63CkjMKGegAVL8AyYAQ0LMOQH4er96cc2yMMPq3//9wxoHbU/ffpcrt4/n1+WP1pfrro4WHWV03ZAPM+pHTfJk256Xe3y0ZnaP9miScro9W3l75SqevWX5d2Pb0xeo6D78fNLBUR4Gv7zy08rYPrPL02//H5dqNQ//vSaV2PQ/PjT73Ta3k0Dr1uIAalfv7w/v5MFE3+fmoSrLxdlz7zzagIvqQNA/A/6LZ830d/JvZvky9vkH6v6w+r7lBd9/gLkfQsxF9D9PllgA7Dy5TWtkvLHdx5NBULPKb3gx5/+EVkvDrwsT9ruv0X35zfCMQhwYK13k/z04em+v66gd92+0fzHbGsQMP+KJmD6V3bfDPWPaD89+zek86QM2m++/C657y2A/rL6+R/q9s8WfFiFn1/YIAfZ2ThuHnxa/foMkZ9/8H8f/OGvvwHS/1cyl6oHmbtQ+FI4ZRIGbffly88/tM/hH/768w99DaI4cIovfZN/j+b37Prk8ycLvs/68c9rAX+jzMpqLFffcmj1a1X/j+a315Xp5In/+3j7afXHTFw+0GpR4ivTNxP8IRtbIOsf7PjTy28AdEqgTe89XwP8+Ld/W0mJ11RtFXarCwCqbgUc3CVFsAivx0m7An8X1GgCYNc2AYZ9nwfif/HwIjEAxV/+l/cE8Y/eO4ivUf/LN/hdYnrBsl9eVzqgVTVJlJROvtJ2ivK5dBbgW/jUTdAGzfCEzi74CFL44/JjAe9fvkfuy3Plaz39snqrBU9JNUZYsK3t8+B10cKKg/JdZg9UnuAReD0guhSL/Anq7QegXVvlAOu7ReM2WxDdTwB6PCvLs0r05aeF2C+//OI6bfy5fANjdPVWmto1mPBNnNXHj0CVME+iuPtcBl5crX749bcfVv979c9WPYkvPBRQD95tDiQUL2d5BXKoL8A04A7gQAAQT5v/+tu7QQGZEtRS4KEkTIK3xSAGs8D/at3LYfcRwYmVGwCrAosWddV0AOFBhXpdCeHqm7yA6fJqqQFx1XYrP6iD0g9KbwJUHaDON0uWVbdqQaC14fRhtdTYhesvbuM8RSxAMjvdLyuJUUDFqXLw3yLmcxJYXJUJMP8337+NAyLND+2K/kridSUvUbeqncap48Z55xE6b34BlebrckDcWZXB+LlcqmqwmOqZAm/mAZOAZbx3l358FnKvKkC+++1X3s85zlIX9Wd9bD6X7Xt4g7ADVvEA3AOmUZ/4C+j/x3tItSAic/9pPyDpQundC/67V54xCHqIb3V9JXzrWd5L/OrHpcH4afW5R+ANtvr/tcNZFN3xvLbnd/qeXe1lXbu+OWBp6BZHvfWAoON4yv9Mtt+7kK9I8xVwP5d5AqKpmf7jbeZTuvc5byDWL/JpO+1JH8QMcMBC9xnSS4g2zZIMzufyK7J/ADZ4whiwIDAlyI8lLL8yXN5+lTQGSb48/17lnyHQ+ItFQdiu6t7NQUiFQeC7jpcBqZolLd9dWC4mBpYc48SL/6TVClAHvgT0gf+AqOBrLF+/oe3b26+i/2nhWzOzLHk2ej3IyuZJAMgRLAIuvh6TDoCT0731z0DPT08iQI2i7hbdXRA/QNO3waAJ7n3SAh+2H97tGtQAcz8u32+aLqPBowapAIwFAr7ugXWfKbKgRwFaFSADQAkQTUVSgtINjPJuhCdBp1jyHcTPexS+UXwOvysUPPNqqTlfFy6KLGuWMr4KgehgZPojLOjfCxNAr1hmPPn+baR947bQXqCxBfAGOH59+1bvX99K9ltPsPpK99PfbVB+/Nf2MM8ibPw5AD6t4q6r20/r9Vvh/Fo3XwEwrd9kbUEN/fgtwT++F70/0XpT89PqX5PnTyTe8+HTavMKv8LLq9N7PL1/gPrMR/r6EVvefi614HeoBOyrAgTU4qwnPn2ta1+ngOIWNUG0TH6rc+1SHkdQkZ/ADiz/ufxjgC8JBupGGS0B2VZ/SPwnFIJgf3PUt/oDXpUd4O0vbV8ULLusZzq0wcunss/zDy8AEoN/urtaqkuxxG+77MZApgCk65Lg+fSEg0e3/PzzLvT8/OHkrys2ANCTt3+MsfeasKDyH1LhTT2glgc4fFj5wCjtUsOAegvzJY2cFsQlCMlFjW6qF7nfNmJL6/atr/t7aSxQahck86tPS9X58J7v4Bv04h9W39pqwPV9o/PcjpY92EP+vLT0ixmeS5YfYA34+rbo2w7cDV7++j25nqDwJaxyAEh/Lxv3HF983gR/U2m/OeMjyn78z2+R/l8f//MKPh8l6SPL/tdr3BX5N/BvHdAeftc835Z/zzwLCv9eKoGlhqTtQX89gzoO9tBOn4PQ6qp3WEyKJe2Ni8T9YdGPwWv0ukKwn5bdUF+2ABKfZf47wgBpnsAKytNi398d97v5quf2aJEbmLt7283/+gLC0AFx4bwH4nt/DaYDHPrYLv3GGmQpYAie3/IJvPtvdd7va9rYAV0gWBRi+HbjoAEGb2EccUISdgKS8nGXwrcosfVJPERddAPjLpjoIaSPoZjvbnEv3BJI4GGA3lsmflkaqWSRYxECqP8RJHPw+2sw5L8r8CbwYp1vjf6i6Lsev764BAZmHrBW2L19mDVlugR6crXahWYirB4mLsw1E5388mbr9flxczONtaA7o5bNfeIfKk+LVSbQ/A4WuCI1OmP7YOdYkXIIR1XUjdT8fCmHNN9MiXohdHwL5RDl9b2B6cV6bRzmUWryM5PYnGePNTbPYtNaCty2qJ1UvELi6y1aVeuBRwes0wnVPIoKh5GeRTNSHydIq4kuYcdw1uZZwe9N0csvOmvRj+BBYQUl2tc15NSBYoS30R9o7iDcODxrtWNgsAUUPDiZPcverSbCGPcvEWs69mVmL0KdHbVrrA2dmPPqVHH2Q6GP9XwYR+yOZpe9HqgZYHxLT6x3tbyARIKEgqDzASYEzyax7fnhH1yKCNb9+URZvdBtqnrGNBs/tyWzFu/4THkxN3AX98Hx1G4OvWjsjdos4W6Aq5LRAr/cSDOiWrrMSkd2bC/G6ClNkks5eb2MsxgPRZOmZ1VPT2qVUdR8Cw4MkU9ZeF0TtsTtM+XazDuSHeucOKN5C21qyoUVD74kMnEK1UyDsszKWI0MOKytup19mQo2DvwwYnyV4eKNdM2sffNw4jVBtNqWnrpd7OzlAaOP66Y4CiSLdnoDzQobFNfAGHNdo7W2145ncXdLR/+0j5NU17Zc4DZlHZaWG1UTOxX6Ttm61NGTG2QHW8wJuh8kXPISk2M8Ps7xqbxse5rUXQpLlNslNEBnv+fEC85ndOXiiiJahy2oqIPAYvsrv6ctlDlLWlqiofI4jbJ8JumrMN8o717ekvbCcvBJYjR8P3AKRsKcfBr3ExpPJxMvDCa7IkWkO3nLOfymAllw6+7dJF4EPw55bt+3+ztVoMckj6aaofZ8uDXM5G6gvGoz9o22sZwbhy2HSTPh2Qm93tlNwmFVFwVq4bJRtp1kVZdLvHJKrN6Ud/9+rktMkffodjOuEWOEK+Q+HbDHSX8Qg3zRjUuQdXprl555Lq/7x/oYE2RKPQ6BojiIsMZjAg5Tbg1JJcHk5Ebvb+J4FNZwSlg6G0wHX1KvtTK2+kHatIZSoMXdnDRDfmR+awFPyPq4a8h9BYLP7hB3Eh5roUtOswGX8qCV3VXOHWVmjuc9PlXh7j43HLw7pkezY9zdrHdzEFpt4M9bc/YoPtLT4WRLu0cJMkS6UNKjnRU6rREtjKhtfkjd9YZsrsVk7lRbuoy2lKon4lYL2sFD3XjNImQoRSZfZra37WDVi0M2vzlp5oz5tsG7oXN257y0pyDxG9zayzFVZutUkJhHKVAmXO4t+RomIZEYOxqrA2cn09CauOW8vK6M3XFrJzePo46GgeoPBa94aeJT2IOFhgeJZKw7KrdzJPYYwVOxx1xYFlUEvAQKcpMx5w60xcZ8gtpwV4USOhvKCWnNCWN5M0Jn5XrLT/LNfog8PplQts1bdkaiMIVRpQhOB2facqB7n/1pluk1d/Fz4XDibHgyisiLFSZdMw+VM7fNhZUeXTxiGDLLiBak0l7ud1wkr09OXeQulcbh/mr3wKQn1dbqpqiiJI12oh3JcAwXXXmdt9yWAuaiEcMS2JIkZSa912gwjNuaC6k8UpBu69865H7Tt6EgVF2F0TBm4VSG67JtuFwyQPAO3WIiRVAzh+Nodn/EzCjPoUYfgqOZX088jq1Rr+gm5EHzyeVqZVWD+awxmaHKZvcrocl9QXPa6CVisGaYMaGLSia7HB88mmWzvRjfo5zfS35Xn3cgjuSt3dk1IhQRvg/aeNslJDaBUl+Vdq32d/6qJ4N9ZM9WY5nyKLICKjKScdgl2oO7XXWBTlh1ImaCnb0bLSrGceTuIupsdSaBcH8DE0kw7CBnU1UyBenutmkA1lnH7bE6XQHaXXHnHFNtlVwe18uUeWWDYee0Q/xDzAQ3nVbaDGUrebPP+aZEj9dCnzWHY5v2NMiTiyiHvhnvkZ/3czTdimy/78p0shJyM1DxelA2GwiDKLdnj3pJH7kAbBtKBhaynX3LCogtNn5QMyp9I2MvLjEN90OK0N2jltO6c6NmTzAeAbZGhjhbB2kTIISnFdPpYLFWefB1oR5YORN890ZjbOEF+5luyKM6S+2oHsmgH68WvS4ZP2XW/Yzku6PEdge1hB/6sSxaOLuffFaxxE1moJLLiqCl79QHuVaa/DA1XN0dNRiiwiOcb07cVt48oq4Ss83OZKSQg+B1EOe8ruPzLoG6dBs1PuwN8ZGkjCMZAoxHuGDC2+wMBwZDM4wX4ebjbPsSiJdE74RY0s0HFEF8KquAnnqb6bnn8ADmnLt0yJvoMeWQkZReoeI8ZZrn3gjadJvlkGgWx3xLSmekO4D84GjVULJRHTb5SE3JjhY1MbPHCtIMep639hGh7L06dVjyYNpSVY3YF0zqAbHmRUd5KT0Gwtq1YnrbnfeCcpH24jmor7Z6S4TE2HRiL0iEuTufZJ4rp9xoqJv4OO724VZl4lhMubstmAFPRFJVm5tWJZojNN+wGg8VenjULqzt8BCBE4/JBh2kY8yqsBU4HrOpA/naGzM1I0EKq2UoerZV1v4JsXwhHrPpdjvl5KV6hHDNeGtIE2JsD184kdsW0GXIlIjTNgUfVGrtGKaxJ645GWnTMbjNppAKsBoQ4d2KlFhwH4w13a39Jh9IbS/6vHDkS5tqB9JQpZaGHkcL3srJzVCulnaXqmt9REN70mkqjO9jdAwIiL+hzbWxo0in1aPa4vZ9sEycdzIeeeyndM+B6n6b/APbE+cDqL6F4dJZKM78veivDnMUKTKa1fvBuBRiZYpVIZR7IPj5ylDnIuFEXYIrdyNUpz2NdEZJSQaCUlGG+uS8M82LDQ8qgpdXr947h6gW0dE5wNTdsBvHMknQjkSEHEus6SGpoas6703Bnb2JvLnFxX19qCefUUdvD7LidFTqc4xSRgHRB92zSIslsvCwv63PtDzhu4vTVY6XFEddq4NExztqe8gYrm3WTBALklxt4nkcTpFh71QBuxwZh7xzG55tbz7Jj6fruWpH1kQfAS7UbHkbTOhhC/p4z5CLdkRgUjvr83SIt15qaLvWFHejtTNQZriPaHpX68NF9rftOGSgXxb2KjNjSUpp7I2uAyL3qlz3AoUa1zx8i06YG67b07pCwwHY+lCSZTPIsklfj1PT7UExPOWeXGcq1bq56TP3ZMvSpqmVFCdE1+tW3EXHw721NmwcN1Wn4AgVmJYri2w/xSapQzv8gvESm2ZxPCZ2VfMbUzuWTWptrnFjim1PNbQxDE4ckR0+i960sxm8AEqawVTksdaExgVO9coXhO6snrHJcCenxiomwg70qO2hVugx0an5+/GUOQYMczeNJk5Egl54XOhxbY8TxxY7WBg8SEJtzzqFaUdm2EkyF4HAxk+ijXMV7dN3UWxxz1Cr2sHnm1JabR86lIRYHbM9IxJnoVVnIr64nrCsl0L0hpuDZ4FezUe6bF+vU+cqbHaOqKE2xfY7k294szvshN0VaSUfT5Pt1bDwK6adCRp3E6JVJ+kiyu0xJ6rjzqIhZh01SHv2sVbdETUyOam3aUMGQ7T2wdzikjyJfa4P9Ght/L6/N261WV890s23hxR7OKx1iW70pTnt5n0kb+DUqYSNevQ2mnSIEejwSG94hDC+K0tNAYtQ6zPYY7clgkxL2qNwZ1COV2vlyrcb4pQmIdw6/QS7vcja5EXWHEuU9D4QMOouMb5lXU4q3aNMdxQym4KEhOAE3iqYQBXT82gF5yaXvJsmnfG7X0jJrgR7nn17KaRd3etGJJWmIAf5OdYucU4PddAnHLrnAzOe9YB4jGdHqkn8tHVNj6mPWz26C6d93+d8cdyG1+Jo77hU0NrrnKGYnUK8H4a16KITezviR+C9tXHyA/Z01y2jmh1co2/iepBmj/WjWAiwuzSp4mlnypQmpjv1/EgOG1sUIfNm1pkrsuaOoKjtZeNtxK40Did2CIKUaZ3HkMCotnfg6rDLCH8jcqo8UgJi0VXWUgwSnaALT7KPI8thkK80ynQYwsEmULfT1yyGK0Oqr8kHGUxqoK+vBYSmIxakOXJdD3qM626Jw1Aq3bcQL7C2uyW3zi4PIG3AhekqyWlbeoiqRmQSCqNp60V2kSz+DHlJg2rrcgvtElrN0CpZ98i6HEiUkA+69oiR3Nrdowzrz2xp3jMGPp2OOQ4NWTZu72cW5uUI2QSCvL8vpyCzJjIIM0e3nSh4yX5naYwuGvgJPvjxYyvmbXRK9Zsw1KHBeHssFmos1sDuG2DS9XDB9UG7+QcIbBkUzFDYRxJ72z2mcMbuPM+Zt64viX3Pr/Bw8rvgFo52d7J6WEnuLXbKzaOxXp9ufKYeZFvZgGAhK4XmXSZtIOuM7Xpra7A0rcjx9PDafdCEifDwd1betVvOsb27oR6N0sI3p/OdqQp86wpHj+5aRrFTXEiA//OG75HDPTUKQkIE3YZ71R8MVuwfFHen8CAeGPE81bQ+6oK4yzLHFYfgQYUW6mT3jSogW/1oSfdEipKICYzpEk2CC23iMR55jrvSI3uWVYwIqW1qiRWxJqXA0NQBapTsGM2S69Yi7xlbLO5UMfTa/iZsnA1HSS52uVdxhuzFjnYeHvy4IVPG+k1UdxfuvhnWEj3lyKR2vE3GGu2cAOAnudNsC7vtTjoBmfKtNxHIYlzPAL3fYbqnOskkCGyBOjQ4/m4rToeAkvze5vqyj2/6WCSQq9vH9HzJIPdAXZDSGegc2QOUghsEup1QKrkEAj0dbMHgHFzVxNJJmZ51AMbzl3WCKcmGtmXzdCA5nC1IpujYDUZ0FYRAWgNz0Ly5G0jTESwmdQiLRJR4nM9lWp0bpTg6J2xOrveAg032psw7fnuX8IdVwFgOU+GZbMnOws/DTdHRLXcZyKDpbEUHm8qrSvUX/J7ifWlI1ry9KgUElSezlFs8sh5yQ1LN3J8uJTJCdy+MzeEeQky9oUXicbqRKrVLrsJVmjeICVGqy3A0BxGgzyVVt8YfHF+Rhw28Dc80EeVXT6Qlwn/kpoj2FVPzkqWTgqnVhEUI9JBgiDJbelbZCQEjj/X2Fh3c0eih/Zrd7nP2dugeaHGLiHg349Wps92uH5xZHo7y2EqHcfbju9/IyEyQLl1C3bCGlCHcCrJ6cMzMU5rGXHP6OFvsSNyaUOX8BmAOOibyCVI39PVMX7fXZI8aGNjgKlDDMMpk1gTbd3rq2VC2I448EiVue1UiVhT0osHGhw8XHsGzTqGG8NYjQTbWSEu4AbVpJf567ickmE8eh6d6FxYzBLtaRJbWdBll8q6jaq22mxYE54WRbLLsZN8/l9dLTDS3UzixNYVavH66dvBwCUQj7tG2nwvfh9OQ8v1N61uu3jVxhShKWXW61vVatdZ3PS6GZkoRPEGYMIFIu+m6M6br+YDODdv1MwyJ9yvDOK7Vt6qZXXwdBy0z4tQOoeSIe1MpPWl22Xkwqf586Eov3ZB5ukl5QZXW8OlcztFo4kN52QcCf0aE3LOL+OI9iDPhhPCO6wxevdBsw0sndNzEBppL1Q3sHSHFY429GV2RXchzbJruyIv4IA35OvnbHH4ARUEDUPGzgF6HUlOO7TjVOLrtDynqIKjsm+g2EvdhwkHJnFN6r9s0aNaz6NayHgrlkVv1B8vvjEKBCJXKd0hGHmclnnHMVES08R7y9aDMtl9e+1uv8HKpIE4CFdpcPCx520zXTrR2dYpLR6q4FHbPbBFkdm07l3L5uiHWZStpWDT21qhIonbf8qSz35huNKLnLdhq5FNNAqg4hg9jc0pNs3QK9gwaKdc8+xf8qoNtgaXjRgVvjBwzsEpSSXO2MSfdYk6cT1tylkdmf7ShDdNfN+VVYiZ67R8oeSxjdR9n52DtYVPjVGkv78L0xMUcGdPDdQcTWO8Xh9Sizg6HBCXu6sTaaUmcyt32LuaHdYNTHejYR9K/qvdb4Job0F82RlFfDIXitoZphoZLptwZrTvyxGzIZB0NJzzBMBnSq2vabzQKRgZX4OtwkMa8zXJsrNvddavfLvjZREjUf9Sm3wuGc2u6izJkEh6cYYLUSKvBj+gJnYf5CDIYH87sIG12rshMvJkfsvN9T9nuvrvKkanUuhJUkHxUMHzbnlKB3iiueRpiEF+KVIzpVbhBwbnOhOswybpzLGd/MqRbcKvOBAePm0dxu4wOissHchev49Z2zOsccuLQ77vSPLcHl0nGOfWawpbrRBqoe1OI/cVad5UG7ygfle5uVO65k8xSpR/R1F0obxF5ACh+VyRb844KQeICltaDlbqJMk7Vmo5qHm1PWbaG11eQy+LQqUnDNoGFtZsOdZ1LfpDxK2HKPHnezDWVVviFH7UGlaRJC/W8vVUb2r9JN7ZpLYAPvS9mCE7kYAsKmbNiBN3FevRSeb5DMsbtr5sieEgh0uPurDxm+5oNt00iOdq6GNnj5nC0OXGy9+njSNT0xR+TR3PbOEh8CTI04Eu55qK5mQrRkl3S6pVGbwiVMM6BNqeNJdXr2DpFEN4hlDZKzrqWHu0R6Q8Te3lYyZHi9DLabyq+08ntOuzCcwxVCbxZY5mDHhBqB4TSJn/t+CVSb8pSQr22K7XwPt7VKZTFMkf6kOgmvGYJM7jSSQplRBBrGo8rHbsb7HT30IR5HvhN4G5rn7ggeDFcU5mFZ8e3fcceJAj2pL0O+a4vIPL5juty01iNox6QfLIVj+/8QlF3o8D3gYHsgLqlCSd3GjLQBN6dD1q65SfXlTc96K/EmWHz9lFAUWcnzpya5cn2m1hRQVz5lHZjEUcBHRdD3TA7NDeHULfn+sC5KH/s7y1K4FuNpGRQv9BzeFLwgaXYE7kZXW/g7Usf0Gf0MApXsREj9NZxm/XepCdTt7pHRujrLOPQUOrzIMLWDnQlKKuxmNPokNJ0z/1edlA4lbfW1j6MG9bq9RTP9+SOWiP7hp0PXIiWuYbExlAlAwhH+7w+Z1hkrMnTLmOqg5sbcyfDtKGOoKGhT7nmZVZJj9ue6GtsA0ens733/PttK1YCsqdE59jVZMCxQWboVoVKZW9ucFhzKLK9tXuIv69zFL3GmxvBEFBvhR4R31C4G33zTETdSeEJ6nEiCUKFNGZfUBuxujySIubUHFYoxL75W5LFoC1E6/NmojEyoaTwDNN+J1Vz6RESvO4HZXSIdE1wDexwHnYqERgBff/IY3A6O0W2HI395S8vH16WA9H3o+1/ejVuOYn7f3bo93Z29/VGzPPsOHD8T09en/65GH/98NJ4CRDi7QCzzfvo/Vjwb44vP37v0sOyYnq7Vfb1RP7tdL9zouU69UtS+n3bNdOXtsqf917ACrdvl3uY7XJV1wPffzzk9p02diun8V+WO5HvN6y+dNWX9xukz+HlTkvgJ04XvD9G7+e4YP37VasvIAO+BE296Pd+k2LxyCv8ir789n8A7Aavn/UuAAA= -->
