---
name: "rar-cowork-cookbook-scheduled-brief-record-intercompany-transactions"
description: "Schedulable morning-brief email summarizing record intercompany transactions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_intercompany_transactions", "rar_sha256": "34922a3c57ac890bc02718a2aa8a9b1dd5c14454223c036ebca99be11b96c4da", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_record_intercompany_transactions_agent.py` and embedded as the fenced Python below (sha256 34922a3c57ac890b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_record_intercompany_transactions_agent.py` first:

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
    "version": '2.0.1',
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
