---
name: "rar-cowork-cookbook-scheduled-brief-modify-production-plan"
description: "Schedulable morning-brief email summarizing modify production plan for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_modify_production_plan", "rar_sha256": "ef4cb23df7bd09d79143a281f22e7060731ccb7f0f4254688e89eb6a928ed686", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_modify_production_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-modify-production-plan:56fd5759c7501330b9a803010a98fc06d5540d5088ae816c26324d873c2907f9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_modify_production_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_modify_production_plan_agent.py` is
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

Modify production plan Scheduled Email Brief — Schedulable morning-brief email summarizing modify production plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_modify_production_plan_agent.py` and embedded as the fenced Python below (sha256 ef4cb23df7bd09d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_modify_production_plan_agent.py` first:

```bash
python3 scheduled_brief_modify_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_modify_production_plan_agent.py   # or on stdin
python3 scheduled_brief_modify_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Modify production plan Scheduled Email Brief — Schedulable morning-brief email summarizing modify production plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_modify_production_plan',
    "version": '2.0.0',
    "display_name": 'Modify production plan Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing modify production plan for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-modify-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '760bfa7f3960a4bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/modify-production-plan'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-modify-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefModifyProductionPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefModifyProductionPlan'
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
    print(ScheduledBriefModifyProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
