---
name: "rar-cowork-cookbook-scheduled-brief-plan-demand-consensus"
description: "Schedulable morning-brief email summarizing plan demand consensus for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_demand_consensus", "rar_sha256": "b25b6a1ceb97fe48cecaf43402e7d616589bf1f659a8af2d0627a0127795610f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_demand_consensus`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_demand_consensus_agent.py` and in the RCI capsule.

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

Plan demand consensus Scheduled Email Brief — Schedulable morning-brief email summarizing plan demand consensus for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-demand-consensus
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_demand_consensus_agent.py` and embedded as the fenced Python below (sha256 b25b6a1ceb97fe48…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_demand_consensus_agent.py` first:

```bash
python3 scheduled_brief_plan_demand_consensus_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_demand_consensus_agent.py   # or on stdin
python3 scheduled_brief_plan_demand_consensus_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan demand consensus Scheduled Email Brief — Schedulable morning-brief email summarizing plan demand consensus for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-demand-consensus
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_demand_consensus',
    "version": '2.0.1',
    "display_name": 'Plan demand consensus Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan demand consensus for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-demand-consensus',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-demand-consensus',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f82482cd35d63dd8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-demand-consensus'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-plan-demand-consensus', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPlanDemandConsensus(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanDemandConsensus'
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
    print(ScheduledBriefPlanDemandConsensus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
