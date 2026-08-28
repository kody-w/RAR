---
name: "rar-cowork-cookbook-bulk-update-raise-purchase-requisitions"
description: "Applies a bulk field update across raise purchase requisitions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_raise_purchase_requisitions", "rar_sha256": "03597de784d444b75f6483d31dc20ccf69247b438bca0d50d83e04ba8f3df7d2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_raise_purchase_requisitions`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_raise_purchase_requisitions_agent.py` and in the RCI capsule.

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

Raise purchase requisitions Bulk Field Update — Applies a bulk field update across raise purchase requisitions records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-raise-purchase-requisitions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_raise_purchase_requisitions_agent.py` and embedded as the fenced Python below (sha256 03597de784d444b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_raise_purchase_requisitions_agent.py` first:

```bash
python3 bulk_update_raise_purchase_requisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_raise_purchase_requisitions_agent.py   # or on stdin
python3 bulk_update_raise_purchase_requisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Raise purchase requisitions Bulk Field Update — Applies a bulk field update across raise purchase requisitions records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-raise-purchase-requisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_raise_purchase_requisitions',
    "version": '2.0.1',
    "display_name": 'Raise purchase requisitions Bulk Field Update',
    "description": 'Applies a bulk field update across raise purchase requisitions records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-raise-purchase-requisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-raise-purchase-requisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a5a1a8992fe1c43',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/raise-purchase-requisitions'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-raise-purchase-requisitions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateRaisePurchaseRequisitions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRaisePurchaseRequisitions'
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
    print(BulkUpdateRaisePurchaseRequisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
