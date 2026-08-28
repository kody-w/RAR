---
name: "rar-cowork-cookbook-scheduled-brief-plan-events"
description: "Schedulable morning-brief email summarizing plan events for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_events", "rar_sha256": "880506c451846a19f3d36b2c22778db603efb30f5ef58bc9f8ee2ed7f46ac90f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_events`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_events_agent.py` and in the RCI capsule.

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
