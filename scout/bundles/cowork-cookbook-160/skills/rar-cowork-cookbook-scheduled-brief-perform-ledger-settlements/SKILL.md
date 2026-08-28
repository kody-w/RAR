---
name: "rar-cowork-cookbook-scheduled-brief-perform-ledger-settlements"
description: "Schedulable morning-brief email summarizing perform ledger settlements for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_ledger_settlements", "rar_sha256": "d3995a29d7afc4ccebb61ff2fa32b78c80074fbb065b06900256dfc06a38380f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_perform_ledger_settlements`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_perform_ledger_settlements_agent.py` and in the RCI capsule.

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

Perform ledger settlements Scheduled Email Brief — Schedulable morning-brief email summarizing perform ledger settlements for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-ledger-settlements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_ledger_settlements_agent.py` and embedded as the fenced Python below (sha256 d3995a29d7afc4cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_ledger_settlements_agent.py` first:

```bash
python3 scheduled_brief_perform_ledger_settlements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_perform_ledger_settlements_agent.py   # or on stdin
python3 scheduled_brief_perform_ledger_settlements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform ledger settlements Scheduled Email Brief — Schedulable morning-brief email summarizing perform ledger settlements for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-ledger-settlements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_perform_ledger_settlements',
    "version": '2.0.1',
    "display_name": 'Perform ledger settlements Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing perform ledger settlements for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-perform-ledger-settlements',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-perform-ledger-settlements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4e741da2e7ec84b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/perform-ledger-settlements'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-perform-ledger-settlements', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefPerformLedgerSettlements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPerformLedgerSettlements'
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
    print(ScheduledBriefPerformLedgerSettlements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
