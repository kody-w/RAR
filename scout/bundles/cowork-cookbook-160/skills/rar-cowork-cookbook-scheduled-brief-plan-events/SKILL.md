---
name: "rar-cowork-cookbook-scheduled-brief-plan-events"
description: "Schedulable morning-brief email summarizing plan events for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_events", "rar_sha256": "880506c451846a19f3d36b2c22778db603efb30f5ef58bc9f8ee2ed7f46ac90f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_plan_events_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-plan-events:028046668e6a89aa51d34b3235c4f7213f8223d5bc3cecf65dccb21b1a4d94de", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_plan_events`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_plan_events_agent.py` is
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

Plan events Scheduled Email Brief — Schedulable morning-brief email summarizing plan events for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-events
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_events_agent.py` and embedded as the fenced Python below (sha256 880506c451846a19…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_events_agent.py` first:

```bash
python3 scheduled_brief_plan_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_events_agent.py   # or on stdin
python3 scheduled_brief_plan_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan events Scheduled Email Brief — Schedulable morning-brief email summarizing plan events for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_events',
    "version": '2.0.0',
    "display_name": 'Plan events Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan events for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '635f01766b35401f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/plan-events'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-plan-events', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPlanEvents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanEvents'
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
    print(ScheduledBriefPlanEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
