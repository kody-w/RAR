---
name: "rar-cowork-cookbook-bulk-update-quarantine-received-goods"
description: "Applies a bulk field update across quarantine received goods records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_quarantine_received_goods", "rar_sha256": "51b3637ab8a34fc5029849b1647ee2f27e4865ad560044b212611550af395d34", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_quarantine_received_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-quarantine-received-goods:5b98fa65d972bc6ad1e230633e2ca606f9824989d6f5808419fb06332d61564b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_quarantine_received_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_quarantine_received_goods_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_quarantine_received_goods_agent.py` and embedded as the fenced Python below (sha256 51b3637ab8a34fc5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_quarantine_received_goods_agent.py` first:

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
    "version": '2.0.0',
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
