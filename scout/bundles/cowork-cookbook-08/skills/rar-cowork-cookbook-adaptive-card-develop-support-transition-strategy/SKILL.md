---
name: "rar-cowork-cookbook-adaptive-card-develop-support-transition-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop support transition strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_support_transition_strategy", "rar_sha256": "69b51b5845c815063d44a3dfeebbe10f8e9842d7af5f5bc358d9a13149a9589f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_support_transition_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_support_transition_strategy_agent.py` and in the RCI capsule.

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

Develop support transition strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop support transition strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-support-transition-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_support_transition_strategy_agent.py` and embedded as the fenced Python below (sha256 69b51b5845c81506…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_support_transition_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_support_transition_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_support_transition_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_support_transition_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop support transition strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop support transition strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-support-transition-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_support_transition_strategy',
    "version": '2.0.1',
    "display_name": 'Develop support transition strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop support transition strategy status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-support-transition-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-support-transition-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '328ad66101ba6cdc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/develop-support-transition-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-develop-support-transition-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDevelopSupportTransitionStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopSupportTransitionStrategy'
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
    print(AdaptiveCardDevelopSupportTransitionStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
