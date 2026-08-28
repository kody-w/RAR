---
name: "rar-cowork-cookbook-bulk-update-cross-dock-produced-goods"
description: "Applies a bulk field update across cross dock produced goods records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_cross_dock_produced_goods", "rar_sha256": "29a0b8235f4648660fd8c42afd21adb187bb66daffef05402e50057748da2847", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_cross_dock_produced_goods_agent.py` and embedded as the fenced Python below (sha256 29a0b8235f464866…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_cross_dock_produced_goods_agent.py` first:

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
    "version": '2.0.0',
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
