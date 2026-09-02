---
name: "rar-cowork-cookbook-bulk-update-record-intercompany-transactions"
description: "Applies a bulk field update across record intercompany transactions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_intercompany_transactions", "rar_sha256": "ac9ba8e0027241cace809272b0c2c02026ddf0b30dd4f1722684df92d17dc961", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_record_intercompany_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-record-intercompany-transactions:3f524ca82ac1170ab8f0a6a179b9ce276eb6d39ac6fe81eb615b13356fffbae4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_record_intercompany_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_record_intercompany_transactions_agent.py` is
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

Record intercompany transactions Bulk Field Update — Applies a bulk field update across record intercompany transactions records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-intercompany-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_record_intercompany_transactions_agent.py` and embedded as the fenced Python below (sha256 ac9ba8e0027241ca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_record_intercompany_transactions_agent.py` first:

```bash
python3 bulk_update_record_intercompany_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_record_intercompany_transactions_agent.py   # or on stdin
python3 bulk_update_record_intercompany_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record intercompany transactions Bulk Field Update — Applies a bulk field update across record intercompany transactions records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-intercompany-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_record_intercompany_transactions',
    "version": '2.0.0',
    "display_name": 'Record intercompany transactions Bulk Field Update',
    "description": 'Applies a bulk field update across record intercompany transactions records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-record-intercompany-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-record-intercompany-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cb5bddf8b0ebe3ff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-intercompany-transactions'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-record-intercompany-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateRecordIntercompanyTransactions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRecordIntercompanyTransactions'
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
    print(BulkUpdateRecordIntercompanyTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
