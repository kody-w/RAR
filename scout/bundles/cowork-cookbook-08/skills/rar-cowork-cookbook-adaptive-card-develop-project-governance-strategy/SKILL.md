---
name: "rar-cowork-cookbook-adaptive-card-develop-project-governance-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop project governance strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_project_governance_strategy", "rar_sha256": "14d384503dcc9b2310c63954207ef0ee4d0ba6ab6a2e8e3b01b01354fd1aad2e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_project_governance_strategy_agent.py` and embedded as the fenced Python below (sha256 14d384503dcc9b23…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_project_governance_strategy_agent.py` first:

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
    "version": '2.0.1',
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
