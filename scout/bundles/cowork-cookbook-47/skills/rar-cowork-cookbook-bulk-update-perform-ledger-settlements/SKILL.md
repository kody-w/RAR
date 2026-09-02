---
name: "rar-cowork-cookbook-bulk-update-perform-ledger-settlements"
description: "Applies a bulk field update across perform ledger settlements records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_ledger_settlements", "rar_sha256": "e3ff1c3faf789a46bb8e65964fb2f8634d1d860c49c8a33cc20f826611a8a1da", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_perform_ledger_settlements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-perform-ledger-settlements:30b375b71dc8e559fb62dd96b054a40490b8fa0ea57a4815342ec19d5b2ff04f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_perform_ledger_settlements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_perform_ledger_settlements_agent.py` is
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

Perform ledger settlements Bulk Field Update — Applies a bulk field update across perform ledger settlements records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-ledger-settlements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_perform_ledger_settlements_agent.py` and embedded as the fenced Python below (sha256 e3ff1c3faf789a46…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_perform_ledger_settlements_agent.py` first:

```bash
python3 bulk_update_perform_ledger_settlements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_perform_ledger_settlements_agent.py   # or on stdin
python3 bulk_update_perform_ledger_settlements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform ledger settlements Bulk Field Update — Applies a bulk field update across perform ledger settlements records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-ledger-settlements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_perform_ledger_settlements',
    "version": '2.0.0',
    "display_name": 'Perform ledger settlements Bulk Field Update',
    "description": 'Applies a bulk field update across perform ledger settlements records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-perform-ledger-settlements',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-perform-ledger-settlements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '08d800f10b0d47bb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/perform-ledger-settlements'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-perform-ledger-settlements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePerformLedgerSettlements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePerformLedgerSettlements'
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
    print(BulkUpdatePerformLedgerSettlements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
