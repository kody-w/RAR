---
name: "rar-cowork-cookbook-scheduled-brief-plan-worker-retirement"
description: "Schedulable morning-brief email summarizing plan worker retirement for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_worker_retirement", "rar_sha256": "c6f332627bd6fff42d4a0720730213bb5da6e71187ff04a2e977023ee69b995e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_plan_worker_retirement_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-plan-worker-retirement:29d7462d90b2a0827417a3289dd4038043667c439cc32a4586ec6975dd61ff19", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_plan_worker_retirement`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_plan_worker_retirement_agent.py` is
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

Plan worker retirement Scheduled Email Brief — Schedulable morning-brief email summarizing plan worker retirement for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-worker-retirement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_worker_retirement_agent.py` and embedded as the fenced Python below (sha256 c6f332627bd6fff4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_worker_retirement_agent.py` first:

```bash
python3 scheduled_brief_plan_worker_retirement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_worker_retirement_agent.py   # or on stdin
python3 scheduled_brief_plan_worker_retirement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan worker retirement Scheduled Email Brief — Schedulable morning-brief email summarizing plan worker retirement for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-worker-retirement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_worker_retirement',
    "version": '2.0.0',
    "display_name": 'Plan worker retirement Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan worker retirement for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-plan-worker-retirement',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-worker-retirement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a89cca683f4e5bf3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/plan-worker-retirement'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-plan-worker-retirement', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPlanWorkerRetirement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanWorkerRetirement'
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
    print(ScheduledBriefPlanWorkerRetirement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
