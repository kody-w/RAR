---
name: "rar-cowork-cookbook-bulk-update-receive-goods"
description: "Applies a bulk field update across receive goods records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_receive_goods", "rar_sha256": "92eb4398bd317327a76c40f3570d00d6261748f9c6d650bd8d5b380fa20e3089", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
