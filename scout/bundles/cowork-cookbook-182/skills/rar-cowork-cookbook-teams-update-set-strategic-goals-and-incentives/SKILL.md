---
name: "rar-cowork-cookbook-teams-update-set-strategic-goals-and-incentives"
description: "Drafts a Teams channel post on set strategic goals and incentives status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_set_strategic_goals_and_incentives", "rar_sha256": "b2c6fec5fd0291b19083c3dc2c23e562fc45841338518b7b7a564d9251e95905", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_set_strategic_goals_and_incentives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-set-strategic-goals-and-incentives:937a4f0ee610f014a739f4fe125cc0453f11da11a15daa31560525eb69d96166", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_set_strategic_goals_and_incentives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_set_strategic_goals_and_incentives_agent.py` is
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

Set strategic goals and incentives Teams Channel Update — Drafts a Teams channel post on set strategic goals and incentives status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-set-strategic-goals-and-incentives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_set_strategic_goals_and_incentives_agent.py` and embedded as the fenced Python below (sha256 b2c6fec5fd0291b1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_set_strategic_goals_and_incentives_agent.py` first:

```bash
python3 teams_update_set_strategic_goals_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_set_strategic_goals_and_incentives_agent.py   # or on stdin
python3 teams_update_set_strategic_goals_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set strategic goals and incentives Teams Channel Update — Drafts a Teams channel post on set strategic goals and incentives status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-set-strategic-goals-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_set_strategic_goals_and_incentives',
    "version": '2.0.0',
    "display_name": 'Set strategic goals and incentives Teams Channel Update',
    "description": 'Drafts a Teams channel post on set strategic goals and incentives status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-set-strategic-goals-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-set-strategic-goals-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8feb5f6a9a5f5e20',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/set-strategic-goals-and-incentives'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-set-strategic-goals-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateSetStrategicGoalsAndIncentives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateSetStrategicGoalsAndIncentives'
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
    print(TeamsUpdateSetStrategicGoalsAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
