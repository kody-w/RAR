---
name: "rar-cowork-cookbook-bulk-update-release-goods-for-picking"
description: "Applies a bulk field update across release goods for picking records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_release_goods_for_picking", "rar_sha256": "251ca18279e719ea8c4c941c7d2da6619bc874228a0898fbba5cd37cf3d027f5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_release_goods_for_picking_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-release-goods-for-picking:70dd340ef6f361a109659c73901ee90dd53163c21217f0936ff2450f6a4966b0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_release_goods_for_picking`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_release_goods_for_picking_agent.py` is
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

Release goods for picking Bulk Field Update — Applies a bulk field update across release goods for picking records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-release-goods-for-picking
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_release_goods_for_picking_agent.py` and embedded as the fenced Python below (sha256 251ca18279e719ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_release_goods_for_picking_agent.py` first:

```bash
python3 bulk_update_release_goods_for_picking_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_release_goods_for_picking_agent.py   # or on stdin
python3 bulk_update_release_goods_for_picking_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Release goods for picking Bulk Field Update — Applies a bulk field update across release goods for picking records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-release-goods-for-picking
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_release_goods_for_picking',
    "version": '2.0.0',
    "display_name": 'Release goods for picking Bulk Field Update',
    "description": 'Applies a bulk field update across release goods for picking records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-release-goods-for-picking',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-release-goods-for-picking',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '002dabc6de9c97b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/release-goods-for-picking'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-release-goods-for-picking', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateReleaseGoodsForPicking(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReleaseGoodsForPicking'
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
    print(BulkUpdateReleaseGoodsForPicking().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
