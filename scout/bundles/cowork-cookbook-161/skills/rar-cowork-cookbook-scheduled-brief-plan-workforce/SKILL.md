---
name: "rar-cowork-cookbook-scheduled-brief-plan-workforce"
description: "Schedulable morning-brief email summarizing plan workforce for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_workforce", "rar_sha256": "8dedbbf5fd94b33941f33e4a19df9bc8f8c64a9fc4389c95ffdff19312ad25a7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_plan_workforce_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-plan-workforce:a96eb4e44a0bcfe687fcd93dbbd07efb4630aa990365be5fd36d5076e8c65d62", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_plan_workforce`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_plan_workforce_agent.py` is
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

Plan workforce Scheduled Email Brief — Schedulable morning-brief email summarizing plan workforce for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-workforce
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_workforce_agent.py` and embedded as the fenced Python below (sha256 8dedbbf5fd94b339…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_workforce_agent.py` first:

```bash
python3 scheduled_brief_plan_workforce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_workforce_agent.py   # or on stdin
python3 scheduled_brief_plan_workforce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce Scheduled Email Brief — Schedulable morning-brief email summarizing plan workforce for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-workforce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_workforce',
    "version": '2.0.0',
    "display_name": 'Plan workforce Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan workforce for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-workforce',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-workforce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '58eb8ea1e0c7f701',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/plan-workforce'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-plan-workforce', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPlanWorkforce(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanWorkforce'
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
    print(ScheduledBriefPlanWorkforce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
