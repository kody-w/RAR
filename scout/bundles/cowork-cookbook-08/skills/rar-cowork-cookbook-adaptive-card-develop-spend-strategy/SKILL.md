---
name: "rar-cowork-cookbook-adaptive-card-develop-spend-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop spend strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_spend_strategy", "rar_sha256": "22d8e569735a17b40dd31cf42ba868dc87aad9380d2461233f2d1fd03ccff657", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_spend_strategy_agent.py` and embedded as the fenced Python below (sha256 22d8e569735a17b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_spend_strategy_agent.py` first:

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
    "version": '2.0.1',
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
