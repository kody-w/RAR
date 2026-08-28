---
name: "rar-cowork-cookbook-adaptive-card-develop-communication-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop communication strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_communication_strategy", "rar_sha256": "fac9158ea89567b2fab0b30685b4651338cc55509ca699474a5e2fb4c35f1790", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_communication_strategy_agent.py` and embedded as the fenced Python below (sha256 fac9158ea89567b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_communication_strategy_agent.py` first:

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
    "version": '2.0.0',
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
