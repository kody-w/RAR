---
name: "rar-cowork-cookbook-teams-update-set-strategic-goals-and-incentives"
description: "Drafts a Teams channel post on set strategic goals and incentives status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_set_strategic_goals_and_incentives", "rar_sha256": "b2c6fec5fd0291b19083c3dc2c23e562fc45841338518b7b7a564d9251e95905", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_set_strategic_goals_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `teams_update_set_strategic_goals_and_incentives_agent.py` and in the RCI capsule.

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
