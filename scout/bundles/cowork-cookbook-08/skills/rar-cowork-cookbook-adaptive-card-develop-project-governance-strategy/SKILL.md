---
name: "rar-cowork-cookbook-adaptive-card-develop-project-governance-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop project governance strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_project_governance_strategy", "rar_sha256": "2716e2baae17405c9b09a4c521da9695998e49d67027a4ae3b2a48038c71ba5c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_project_governance_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-project-governance-strategy:b5af7b5b146c881ee1dfb8aa02c59946b014ea4edb646dc63feaa2d096c4c786", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_project_governance_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_project_governance_strategy_agent.py` is
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
