---
name: "rar-cowork-cookbook-adaptive-card-develop-communication-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop communication strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_communication_strategy", "rar_sha256": "752a51d8da6b04699a9f19c0e4b6a22e161442bb4f857a9522d1438868373efb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_communication_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_communication_strategy_agent.py` and in the RCI capsule.

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

Develop communication strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop communication strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-communication-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_communication_strategy_agent.py` and embedded as the fenced Python below (sha256 752a51d8da6b0469…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_communication_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_communication_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_communication_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_communication_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop communication strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop communication strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-communication-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_communication_strategy',
    "version": '2.0.1',
    "display_name": 'Develop communication strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop communication strategy status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-communication-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-communication-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '635d39bb447ed1c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/develop-communication-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-develop-communication-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopCommunicationStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopCommunicationStrategy'
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
    print(AdaptiveCardDevelopCommunicationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
