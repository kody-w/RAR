---
name: "rar-cowork-cookbook-scheduled-brief-record-intercompany-transactions"
description: "Schedulable morning-brief email summarizing record intercompany transactions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_intercompany_transactions", "rar_sha256": "9400ab126f0892b0ef0d47dd9a7ed032d55c89348ddb0a0471d04da4119c9701", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_record_intercompany_transactions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_record_intercompany_transactions_agent.py` and in the RCI capsule.

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

Record intercompany transactions Scheduled Email Brief — Schedulable morning-brief email summarizing record intercompany transactions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-intercompany-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_record_intercompany_transactions_agent.py` and embedded as the fenced Python below (sha256 9400ab126f0892b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_record_intercompany_transactions_agent.py` first:

```bash
python3 scheduled_brief_record_intercompany_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_record_intercompany_transactions_agent.py   # or on stdin
python3 scheduled_brief_record_intercompany_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record intercompany transactions Scheduled Email Brief — Schedulable morning-brief email summarizing record intercompany transactions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-intercompany-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_record_intercompany_transactions',
    "version": '2.0.0',
    "display_name": 'Record intercompany transactions Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing record intercompany transactions for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-record-intercompany-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-record-intercompany-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd0ba5023f56f6059',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-intercompany-transactions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-record-intercompany-transactions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefRecordIntercompanyTransactions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRecordIntercompanyTransactions'
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
    print(ScheduledBriefRecordIntercompanyTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
