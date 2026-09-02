---
name: "rar-cowork-cookbook-scheduled-brief-plan-demand-consensus"
description: "Schedulable morning-brief email summarizing plan demand consensus for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_demand_consensus", "rar_sha256": "b5e0e3827202f298a96cb8186d4303ea728f472520d38dcf1cd9a395ea1d9e6d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_plan_demand_consensus_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-plan-demand-consensus:77d9d2a87c774f5f838bdcdb31df70e116ecd81bdf3fed8e5e9847afab8117aa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_plan_demand_consensus`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_plan_demand_consensus_agent.py` is
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
