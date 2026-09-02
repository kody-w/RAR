---
name: "rar-cowork-cookbook-adaptive-card-develop-spend-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop spend strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_spend_strategy", "rar_sha256": "dba04125b44fe1321b12d8354ea7b0f6ac0ca71e9f1c764aa00e328b586994cf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_spend_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-spend-strategy:119b282166c457f5b2923bddf994bb93ae4aa1dd2f539ac2a987bf66214b96fc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_spend_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_spend_strategy_agent.py` is
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

Develop spend strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop spend strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-spend-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_spend_strategy_agent.py` and embedded as the fenced Python below (sha256 dba04125b44fe132…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_spend_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_spend_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_spend_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_spend_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop spend strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop spend strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-spend-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_spend_strategy',
    "version": '2.0.0',
    "display_name": 'Develop spend strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop spend strategy status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-spend-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-spend-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8bcbeb84e5db6dce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-spend-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-develop-spend-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopSpendStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopSpendStrategy'
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
    print(AdaptiveCardDevelopSpendStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
