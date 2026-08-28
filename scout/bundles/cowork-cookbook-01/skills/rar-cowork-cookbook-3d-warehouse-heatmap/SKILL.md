---
name: "rar-cowork-cookbook-3d-warehouse-heatmap"
description: "Generates a self-contained 3D HTML visualization of warehouse bins colored by fill percentage or inventory value, navigable in any browser."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/3d_warehouse_heatmap", "rar_sha256": "fcc2361829bb76b9af34cffb0be2e0cd329bcb20d31e5e5c04ea9183f9e101c9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

3D Warehouse Inventory Heatmap (HTML) — Generates a self-contained 3D HTML visualization of warehouse bins colored by fill percentage or inventory value, navigable in any browser.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `3d_warehouse_heatmap_agent.py` and embedded as the fenced Python below (sha256 fcc2361829bb76b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `3d_warehouse_heatmap_agent.py` first:

```bash
python3 3d_warehouse_heatmap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 3d_warehouse_heatmap_agent.py   # or on stdin
python3 3d_warehouse_heatmap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
3D Warehouse Inventory Heatmap (HTML) — Generates a self-contained 3D HTML visualization of warehouse bins colored by fill percentage or inventory value, navigable in any browser.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.1',
    "display_name": '3D Warehouse Inventory Heatmap (HTML)',
    "description": 'Generates a self-contained 3D HTML visualization of warehouse bins colored by fill percentage or inventory value, navigable in any browser.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0496f0a57d216656',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class Agent3dWarehouseHeatmap(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'Agent3dWarehouseHeatmap'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
