---
name: "rar-cowork-cookbook-scheduled-brief-monitor-employee-satisfaction"
description: "Schedulable morning-brief email summarizing monitor employee satisfaction for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_employee_satisfaction", "rar_sha256": "63b50696d48a0406ee97f6046ecb3bc9438bdbdda1b8267dc55ae53f5561a159", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_monitor_employee_satisfaction_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-monitor-employee-satisfaction:7bc83c33666e73960763eb96bb41e45dadd6a5985b18e452e6e9e2a7777f511c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_monitor_employee_satisfaction`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_monitor_employee_satisfaction_agent.py` is
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

Monitor employee satisfaction Scheduled Email Brief — Schedulable morning-brief email summarizing monitor employee satisfaction for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-employee-satisfaction
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_employee_satisfaction_agent.py` and embedded as the fenced Python below (sha256 63b50696d48a0406…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_employee_satisfaction_agent.py` first:

```bash
python3 scheduled_brief_monitor_employee_satisfaction_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_employee_satisfaction_agent.py   # or on stdin
python3 scheduled_brief_monitor_employee_satisfaction_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor employee satisfaction Scheduled Email Brief — Schedulable morning-brief email summarizing monitor employee satisfaction for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-employee-satisfaction
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_employee_satisfaction',
    "version": '2.0.0',
    "display_name": 'Monitor employee satisfaction Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing monitor employee satisfaction for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-monitor-employee-satisfaction',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-employee-satisfaction',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7f06e76a84c3c9a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/monitor-employee-satisfaction'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-monitor-employee-satisfaction', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefMonitorEmployeeSatisfaction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorEmployeeSatisfaction'
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
    print(ScheduledBriefMonitorEmployeeSatisfaction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
