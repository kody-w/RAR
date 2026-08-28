---
name: "rar-cowork-cookbook-adaptive-card-develop-support-transition-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop support transition strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_support_transition_strategy", "rar_sha256": "f966005e8bf01fcfe0faf77c5e005b612e4453b6ba47b89ff766179401a39ee8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_support_transition_strategy_agent.py` and embedded as the fenced Python below (sha256 f966005e8bf01fcf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_support_transition_strategy_agent.py` first:

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
    "version": '2.0.0',
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
