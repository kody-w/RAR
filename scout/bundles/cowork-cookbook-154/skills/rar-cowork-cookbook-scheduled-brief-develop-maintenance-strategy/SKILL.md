---
name: "rar-cowork-cookbook-scheduled-brief-develop-maintenance-strategy"
description: "Schedulable morning-brief email summarizing develop maintenance strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_maintenance_strategy", "rar_sha256": "510ef0e5be328de3007a30ee7381b8f47cf9b85a1883be4970e287733e6b9f58", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_develop_maintenance_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-develop-maintenance-strategy:87237c0f3dc253d21cdfad236ecba128fcb6a13eeda7516262d2eb211de03323", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_develop_maintenance_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_develop_maintenance_strategy_agent.py` is
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

Develop maintenance strategy Scheduled Email Brief — Schedulable morning-brief email summarizing develop maintenance strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-maintenance-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_maintenance_strategy_agent.py` and embedded as the fenced Python below (sha256 510ef0e5be328de3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_maintenance_strategy_agent.py` first:

```bash
python3 scheduled_brief_develop_maintenance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_maintenance_strategy_agent.py   # or on stdin
python3 scheduled_brief_develop_maintenance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop maintenance strategy Scheduled Email Brief — Schedulable morning-brief email summarizing develop maintenance strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-maintenance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_maintenance_strategy',
    "version": '2.0.0',
    "display_name": 'Develop maintenance strategy Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop maintenance strategy for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-develop-maintenance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-maintenance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5cf0b495a18702dd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/develop-maintenance-strategy'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-develop-maintenance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDevelopMaintenanceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopMaintenanceStrategy'
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
    print(ScheduledBriefDevelopMaintenanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
