---
name: "rar-cowork-cookbook-adaptive-card-develop-communication-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop communication strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_communication_strategy", "rar_sha256": "fac9158ea89567b2fab0b30685b4651338cc55509ca699474a5e2fb4c35f1790", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_communication_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-communication-strategy:9ff23595fc3728c0f592d0328fba2b9d3abd2ad4b2fb9b45b0e4fdeb0ec15b1b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_communication_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_communication_strategy_agent.py` is
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
