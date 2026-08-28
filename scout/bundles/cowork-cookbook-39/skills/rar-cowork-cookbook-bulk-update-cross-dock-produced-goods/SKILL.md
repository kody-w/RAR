---
name: "rar-cowork-cookbook-bulk-update-cross-dock-produced-goods"
description: "Applies a bulk field update across cross dock produced goods records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_cross_dock_produced_goods", "rar_sha256": "6abf02111c6865f942d8d25f358dc07c2eb41f223e967871fabf5050ab760394", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_cross_dock_produced_goods`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_cross_dock_produced_goods_agent.py` and in the RCI capsule.

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

Cross dock produced goods Bulk Field Update — Applies a bulk field update across cross dock produced goods records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-cross-dock-produced-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_cross_dock_produced_goods_agent.py` and embedded as the fenced Python below (sha256 6abf02111c6865f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_cross_dock_produced_goods_agent.py` first:

```bash
python3 bulk_update_cross_dock_produced_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_cross_dock_produced_goods_agent.py   # or on stdin
python3 bulk_update_cross_dock_produced_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross dock produced goods Bulk Field Update — Applies a bulk field update across cross dock produced goods records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-cross-dock-produced-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_cross_dock_produced_goods',
    "version": '2.0.1',
    "display_name": 'Cross dock produced goods Bulk Field Update',
    "description": 'Applies a bulk field update across cross dock produced goods records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-cross-dock-produced-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-cross-dock-produced-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bb4d5bd1ab4bc289',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/cross-dock-produced-goods'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-cross-dock-produced-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateCrossDockProducedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCrossDockProducedGoods'
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
    print(BulkUpdateCrossDockProducedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
