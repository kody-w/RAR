---
name: "rar-cowork-cookbook-scheduled-brief-record-intercompany-transactions"
description: "Schedulable morning-brief email summarizing record intercompany transactions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_intercompany_transactions", "rar_sha256": "9400ab126f0892b0ef0d47dd9a7ed032d55c89348ddb0a0471d04da4119c9701", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_record_intercompany_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-record-intercompany-transactions:6f35f2eb8a7e0e6156fe26bbb298d5004f8494f4e1a611247da163fa7abacda0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_record_intercompany_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_record_intercompany_transactions_agent.py` is
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
