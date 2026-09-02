---
name: "rar-cowork-cookbook-3d-warehouse-heatmap"
description: "Generates a self-contained 3D HTML visualization of warehouse bins colored by fill percentage or inventory value, navigable in any browser."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/3d_warehouse_heatmap", "rar_sha256": "3e36cc9cc11ed1b71f7e15bdcb1719a39af69540d9cf5b0dc8ccb791e5096951", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "3d_warehouse_heatmap_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/3d-warehouse-heatmap:4674d408a4db9e95b3230b5ed1d1c5d01720b4bdeaecf1273e80be0748a66bc0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/3d_warehouse_heatmap`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `3d_warehouse_heatmap_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
