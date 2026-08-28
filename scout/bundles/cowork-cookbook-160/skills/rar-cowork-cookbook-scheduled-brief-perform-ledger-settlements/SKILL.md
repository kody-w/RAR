---
name: "rar-cowork-cookbook-scheduled-brief-perform-ledger-settlements"
description: "Schedulable morning-brief email summarizing perform ledger settlements for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_ledger_settlements", "rar_sha256": "49374b27c0f7d0fb8e9c7e93f97ab7f45361f24d9839c007831a62df4ca7ec2c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_ledger_settlements_agent.py` and embedded as the fenced Python below (sha256 49374b27c0f7d0fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_ledger_settlements_agent.py` first:

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
    "version": '2.0.0',
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
