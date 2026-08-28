---
name: "rar-cowork-cookbook-bulk-update-receive-goods"
description: "Applies a bulk field update across receive goods records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_receive_goods", "rar_sha256": "c33f8bcf034a4dbc8a36864bf1363beb76b1fb6f2cb8960bb5a4b2c09e51623e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_receive_goods`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_receive_goods_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_receive_goods_agent.py` and embedded as the fenced Python below (sha256 c33f8bcf034a4dbc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_receive_goods_agent.py` first:

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
    "version": '2.0.1',
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
