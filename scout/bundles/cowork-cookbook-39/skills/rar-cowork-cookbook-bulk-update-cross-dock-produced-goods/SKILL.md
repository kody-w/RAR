---
name: "rar-cowork-cookbook-bulk-update-cross-dock-produced-goods"
description: "Applies a bulk field update across cross dock produced goods records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_cross_dock_produced_goods", "rar_sha256": "29a0b8235f4648660fd8c42afd21adb187bb66daffef05402e50057748da2847", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_cross_dock_produced_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-cross-dock-produced-goods:8a685f5f90e52f2c0e5a71af3472a45f7c43f86d92cd27481a429aef3f67a824", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_cross_dock_produced_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_cross_dock_produced_goods_agent.py` is
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
