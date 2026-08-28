---
name: "rar-cowork-cookbook-bulk-update-quarantine-received-goods"
description: "Applies a bulk field update across quarantine received goods records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_quarantine_received_goods", "rar_sha256": "177c82b75a2e4c73acd09f0644b3b4d8142380c5d02ea51399a0e23a1f3a3b92", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_quarantine_received_goods`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_quarantine_received_goods_agent.py` and in the RCI capsule.

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

Quarantine received goods Bulk Field Update — Applies a bulk field update across quarantine received goods records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-quarantine-received-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_quarantine_received_goods_agent.py` and embedded as the fenced Python below (sha256 177c82b75a2e4c73…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_quarantine_received_goods_agent.py` first:

```bash
python3 bulk_update_quarantine_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_quarantine_received_goods_agent.py   # or on stdin
python3 bulk_update_quarantine_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quarantine received goods Bulk Field Update — Applies a bulk field update across quarantine received goods records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-quarantine-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_quarantine_received_goods',
    "version": '2.0.1',
    "display_name": 'Quarantine received goods Bulk Field Update',
    "description": 'Applies a bulk field update across quarantine received goods records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-quarantine-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-quarantine-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7c82986f13dd5fa2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/quarantine-received-goods'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-quarantine-received-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateQuarantineReceivedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateQuarantineReceivedGoods'
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
    print(BulkUpdateQuarantineReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
