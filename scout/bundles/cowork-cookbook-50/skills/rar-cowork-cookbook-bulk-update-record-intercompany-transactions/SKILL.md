---
name: "rar-cowork-cookbook-bulk-update-record-intercompany-transactions"
description: "Applies a bulk field update across record intercompany transactions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_intercompany_transactions", "rar_sha256": "ac9ba8e0027241cace809272b0c2c02026ddf0b30dd4f1722684df92d17dc961", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
