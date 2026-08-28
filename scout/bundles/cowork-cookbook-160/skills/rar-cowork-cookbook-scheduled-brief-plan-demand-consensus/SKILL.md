---
name: "rar-cowork-cookbook-scheduled-brief-plan-demand-consensus"
description: "Schedulable morning-brief email summarizing plan demand consensus for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_demand_consensus", "rar_sha256": "b5e0e3827202f298a96cb8186d4303ea728f472520d38dcf1cd9a395ea1d9e6d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_demand_consensus_agent.py` and embedded as the fenced Python below (sha256 b5e0e3827202f298…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_demand_consensus_agent.py` first:

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
    "version": '2.0.0',
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
