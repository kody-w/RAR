---
name: "rar-cowork-cookbook-bulk-update-release-goods-for-picking"
description: "Applies a bulk field update across release goods for picking records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_release_goods_for_picking", "rar_sha256": "65f35684ef52459e321379d3cd15023d9735c7d5d0609981ba3d0d3607075a0c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_release_goods_for_picking_agent.py` and embedded as the fenced Python below (sha256 65f35684ef52459e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_release_goods_for_picking_agent.py` first:

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
    "version": '2.0.1',
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
