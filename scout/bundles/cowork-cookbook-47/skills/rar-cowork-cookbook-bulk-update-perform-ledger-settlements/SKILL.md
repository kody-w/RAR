---
name: "rar-cowork-cookbook-bulk-update-perform-ledger-settlements"
description: "Applies a bulk field update across perform ledger settlements records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_ledger_settlements", "rar_sha256": "38a48f4af4e2025dc4f09d5b315b2df6679a872bf06ab88a9fec4dde1d08ef16", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_perform_ledger_settlements`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_perform_ledger_settlements_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_perform_ledger_settlements_agent.py` and embedded as the fenced Python below (sha256 38a48f4af4e2025d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_perform_ledger_settlements_agent.py` first:

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
    "version": '2.0.1',
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
