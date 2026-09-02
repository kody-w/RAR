---
name: "rar-cowork-cookbook-scheduled-brief-define-accounts-receivable-strategy"
description: "Schedulable morning-brief email summarizing define accounts receivable strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_accounts_receivable_strategy", "rar_sha256": "7d096c0c00412b456a04d7bb9fef8c8e64b2470d71543e838e38b46e8d0ee915", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_define_accounts_receivable_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-define-accounts-receivable-strategy:4c939e526a314d3e8057102e51adf330eae6a81abb4c3d5b2d5d63435cdfe25d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_define_accounts_receivable_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_define_accounts_receivable_strategy_agent.py` is
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

Define accounts receivable strategy Scheduled Email Brief — Schedulable morning-brief email summarizing define accounts receivable strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-receivable-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_accounts_receivable_strategy_agent.py` and embedded as the fenced Python below (sha256 7d096c0c00412b45…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_accounts_receivable_strategy_agent.py` first:

```bash
python3 scheduled_brief_define_accounts_receivable_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_accounts_receivable_strategy_agent.py   # or on stdin
python3 scheduled_brief_define_accounts_receivable_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define accounts receivable strategy Scheduled Email Brief — Schedulable morning-brief email summarizing define accounts receivable strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-receivable-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_accounts_receivable_strategy',
    "version": '2.0.0',
    "display_name": 'Define accounts receivable strategy Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define accounts receivable strategy for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-accounts-receivable-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-receivable-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5e2c3ca7a92fc9bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-accounts-receivable-strategy'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-define-accounts-receivable-strategy', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDefineAccountsReceivableStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineAccountsReceivableStrategy'
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
    print(ScheduledBriefDefineAccountsReceivableStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
