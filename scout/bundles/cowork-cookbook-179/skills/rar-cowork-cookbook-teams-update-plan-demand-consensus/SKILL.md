---
name: "rar-cowork-cookbook-teams-update-plan-demand-consensus"
description: "Drafts a Teams channel post on plan demand consensus status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_demand_consensus", "rar_sha256": "6b04fff997ca4cd30e48cfbf9753e25bad6b972b2c8b0e8a006b70497b657882", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_plan_demand_consensus`. The original RAPP
agent is preserved byte-for-byte in `teams_update_plan_demand_consensus_agent.py` and in the RCI capsule.

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

Plan demand consensus Teams Channel Update — Drafts a Teams channel post on plan demand consensus status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-demand-consensus
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_plan_demand_consensus_agent.py` and embedded as the fenced Python below (sha256 6b04fff997ca4cd3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_plan_demand_consensus_agent.py` first:

```bash
python3 teams_update_plan_demand_consensus_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_plan_demand_consensus_agent.py   # or on stdin
python3 teams_update_plan_demand_consensus_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan demand consensus Teams Channel Update — Drafts a Teams channel post on plan demand consensus status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-demand-consensus
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_plan_demand_consensus',
    "version": '2.0.0',
    "display_name": 'Plan demand consensus Teams Channel Update',
    "description": 'Drafts a Teams channel post on plan demand consensus status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-plan-demand-consensus',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-plan-demand-consensus',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16e8075e38c33d49',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-demand-consensus'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-plan-demand-consensus', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdatePlanDemandConsensus(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePlanDemandConsensus'
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
    print(TeamsUpdatePlanDemandConsensus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
