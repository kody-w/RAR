---
name: "rar-cowork-cookbook-bulk-update-release-goods-for-picking"
description: "Applies a bulk field update across release goods for picking records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_release_goods_for_picking", "rar_sha256": "251ca18279e719ea8c4c941c7d2da6619bc874228a0898fbba5cd37cf3d027f5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_release_goods_for_picking`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_release_goods_for_picking_agent.py` and in the RCI capsule.

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
