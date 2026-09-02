---
name: "rar-cowork-cookbook-scheduled-brief-implement-a-business-continuity-plan"
description: "Schedulable morning-brief email summarizing implement a business continuity plan for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_implement_a_business_continuity_plan", "rar_sha256": "5c7a05dc6ad9995bcc9692270964d367901b443a28ec9bb8379ff0ba17671f5a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_implement_a_business_continuity_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-implement-a-business-continuity-plan:9d2f809562f89e39015693607f8ede3176ff61f7f5b76a4dc889a0b6a68d2fbf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_implement_a_business_continuity_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_implement_a_business_continuity_plan_agent.py` is
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

Implement a business continuity plan Scheduled Email Brief — Schedulable morning-brief email summarizing implement a business continuity plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-implement-a-business-continuity-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_implement_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 5c7a05dc6ad9995b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_implement_a_business_continuity_plan_agent.py` first:

```bash
python3 scheduled_brief_implement_a_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_implement_a_business_continuity_plan_agent.py   # or on stdin
python3 scheduled_brief_implement_a_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement a business continuity plan Scheduled Email Brief — Schedulable morning-brief email summarizing implement a business continuity plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-implement-a-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_implement_a_business_continuity_plan',
    "version": '2.0.0',
    "display_name": 'Implement a business continuity plan Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing implement a business continuity plan for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-implement-a-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-implement-a-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd90c5b1ac2025c6f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/implement-a-business-continuity-plan'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-implement-a-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefImplementABusinessContinuityPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefImplementABusinessContinuityPlan'
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
    print(ScheduledBriefImplementABusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
