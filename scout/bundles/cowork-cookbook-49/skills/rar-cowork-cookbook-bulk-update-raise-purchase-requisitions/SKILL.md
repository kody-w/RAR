---
name: "rar-cowork-cookbook-bulk-update-raise-purchase-requisitions"
description: "Applies a bulk field update across raise purchase requisitions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_raise_purchase_requisitions", "rar_sha256": "76e233d15257dc9c2668865ed8508a4076602212defb2c98a98546e1c0a17e70", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_raise_purchase_requisitions_agent.py` and embedded as the fenced Python below (sha256 76e233d15257dc9c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_raise_purchase_requisitions_agent.py` first:

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
    "version": '2.0.0',
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
