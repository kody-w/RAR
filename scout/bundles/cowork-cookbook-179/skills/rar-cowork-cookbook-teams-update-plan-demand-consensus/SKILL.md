---
name: "rar-cowork-cookbook-teams-update-plan-demand-consensus"
description: "Drafts a Teams channel post on plan demand consensus status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_demand_consensus", "rar_sha256": "a99498890f72583b3046d7af8cdea50e2ebf6b3a4f80a5b4f385e3fc39a6f911", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_plan_demand_consensus_agent.py` and embedded as the fenced Python below (sha256 a99498890f72583b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_plan_demand_consensus_agent.py` first:

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
    "version": '2.0.1',
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
