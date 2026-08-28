---
name: "rar-cowork-cookbook-adaptive-card-develop-spend-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop spend strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_spend_strategy", "rar_sha256": "dba04125b44fe1321b12d8354ea7b0f6ac0ca71e9f1c764aa00e328b586994cf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_spend_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_spend_strategy_agent.py` and in the RCI capsule.

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
