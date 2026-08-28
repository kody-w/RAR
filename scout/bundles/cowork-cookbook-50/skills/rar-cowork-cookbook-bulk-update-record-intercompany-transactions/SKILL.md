---
name: "rar-cowork-cookbook-bulk-update-record-intercompany-transactions"
description: "Applies a bulk field update across record intercompany transactions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_intercompany_transactions", "rar_sha256": "f4d14ed145dce1cbddeb7e16901edb931f19d8004cb0877343e45b36eabb0a5c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_record_intercompany_transactions`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_record_intercompany_transactions_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_record_intercompany_transactions_agent.py` and embedded as the fenced Python below (sha256 f4d14ed145dce1cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_record_intercompany_transactions_agent.py` first:

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
    "version": '2.0.1',
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
