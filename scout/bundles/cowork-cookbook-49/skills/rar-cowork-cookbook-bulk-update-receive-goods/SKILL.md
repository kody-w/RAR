---
name: "rar-cowork-cookbook-bulk-update-receive-goods"
description: "Applies a bulk field update across receive goods records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_receive_goods", "rar_sha256": "92eb4398bd317327a76c40f3570d00d6261748f9c6d650bd8d5b380fa20e3089", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_receive_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-receive-goods:3788b3423b44259aba14e521fa1ee966f5406523581e9343245733eeb165aeb8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_receive_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_receive_goods_agent.py` is
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

Receive goods Bulk Field Update — Applies a bulk field update across receive goods records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-receive-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_receive_goods_agent.py` and embedded as the fenced Python below (sha256 92eb4398bd317327…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_receive_goods_agent.py` first:

```bash
python3 bulk_update_receive_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_receive_goods_agent.py   # or on stdin
python3 bulk_update_receive_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive goods Bulk Field Update — Applies a bulk field update across receive goods records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-receive-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_receive_goods',
    "version": '2.0.0',
    "display_name": 'Receive goods Bulk Field Update',
    "description": 'Applies a bulk field update across receive goods records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-receive-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-receive-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ad8c43b0042d68e8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/receive-goods'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-receive-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateReceiveGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReceiveGoods'
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
    print(BulkUpdateReceiveGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
