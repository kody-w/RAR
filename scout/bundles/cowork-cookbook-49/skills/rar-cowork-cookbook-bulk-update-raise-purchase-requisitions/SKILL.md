---
name: "rar-cowork-cookbook-bulk-update-raise-purchase-requisitions"
description: "Applies a bulk field update across raise purchase requisitions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_raise_purchase_requisitions", "rar_sha256": "76e233d15257dc9c2668865ed8508a4076602212defb2c98a98546e1c0a17e70", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_raise_purchase_requisitions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-raise-purchase-requisitions:8667dadf39ef7f1545a7781c6f635adcf898fbdfa356ae8b366109f25011b96b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_raise_purchase_requisitions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_raise_purchase_requisitions_agent.py` is
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
