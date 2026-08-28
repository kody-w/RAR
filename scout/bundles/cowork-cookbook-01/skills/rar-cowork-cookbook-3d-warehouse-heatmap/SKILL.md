---
name: "rar-cowork-cookbook-3d-warehouse-heatmap"
description: "Generates a self-contained 3D HTML visualization of warehouse bins colored by fill percentage or inventory value, navigable in any browser."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/3d_warehouse_heatmap", "rar_sha256": "3e36cc9cc11ed1b71f7e15bdcb1719a39af69540d9cf5b0dc8ccb791e5096951", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `3d_warehouse_heatmap_agent.py` and embedded as the fenced Python below (sha256 3e36cc9cc11ed1b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `3d_warehouse_heatmap_agent.py` first:

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
    "version": '2.0.0',
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
