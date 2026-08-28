---
name: "rar-cowork-cookbook-scheduled-brief-define-accounts-receivable-strategy"
description: "Schedulable morning-brief email summarizing define accounts receivable strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_accounts_receivable_strategy", "rar_sha256": "73e98de96f137c9f09fa1fd7cab53d91c35d41b32fa505d60a462cc40bd2a329", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_accounts_receivable_strategy`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_accounts_receivable_strategy_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_accounts_receivable_strategy_agent.py` and embedded as the fenced Python below (sha256 73e98de96f137c9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_accounts_receivable_strategy_agent.py` first:

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
    "version": '2.0.1',
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
