---
name: "rar-cowork-cookbook-adaptive-card-record-ledger-entries"
description: "Produces a reusable Adaptive Card JSON snapshot of record ledger entries status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_record_ledger_entries", "rar_sha256": "c45c4be077f9d09d589b4609478c10c0cc3b5c1c4b5bedfe3beb6e986227686f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_record_ledger_entries`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_record_ledger_entries_agent.py` and in the RCI capsule.

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

Record ledger entries Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of record ledger entries status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-record-ledger-entries
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_record_ledger_entries_agent.py` and embedded as the fenced Python below (sha256 c45c4be077f9d09d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_record_ledger_entries_agent.py` first:

```bash
python3 adaptive_card_record_ledger_entries_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_record_ledger_entries_agent.py   # or on stdin
python3 adaptive_card_record_ledger_entries_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record ledger entries Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of record ledger entries status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-record-ledger-entries
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_record_ledger_entries',
    "version": '2.0.1',
    "display_name": 'Record ledger entries Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of record ledger entries status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-record-ledger-entries',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-record-ledger-entries',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '786ec6c04ed8c6a2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-ledger-entries'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-record-ledger-entries', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardRecordLedgerEntries(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecordLedgerEntries'
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
    print(AdaptiveCardRecordLedgerEntries().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
