---
name: "rar-cowork-cookbook-scheduled-brief-plan-events"
description: "Schedulable morning-brief email summarizing plan events for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_events", "rar_sha256": "5b5b8ad057f88caf17de0ede866b89420bd8e4d5d97a45f9642cf5431e48e8b1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_events_agent.py` and embedded as the fenced Python below (sha256 5b5b8ad057f88caf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_events_agent.py` first:

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
    "version": '2.0.1',
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
