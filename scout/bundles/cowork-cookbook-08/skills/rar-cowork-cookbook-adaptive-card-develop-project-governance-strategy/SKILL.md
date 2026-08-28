---
name: "rar-cowork-cookbook-adaptive-card-develop-project-governance-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop project governance strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_project_governance_strategy", "rar_sha256": "2716e2baae17405c9b09a4c521da9695998e49d67027a4ae3b2a48038c71ba5c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_project_governance_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_project_governance_strategy_agent.py` and in the RCI capsule.

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

Develop project governance strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop project governance strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-project-governance-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_project_governance_strategy_agent.py` and embedded as the fenced Python below (sha256 2716e2baae17405c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_project_governance_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_project_governance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_project_governance_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_project_governance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project governance strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop project governance strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-project-governance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_project_governance_strategy',
    "version": '2.0.0',
    "display_name": 'Develop project governance strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop project governance strategy status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-project-governance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-project-governance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '10c517358b3f91b2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-governance-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-develop-project-governance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopProjectGovernanceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopProjectGovernanceStrategy'
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
    print(AdaptiveCardDevelopProjectGovernanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
