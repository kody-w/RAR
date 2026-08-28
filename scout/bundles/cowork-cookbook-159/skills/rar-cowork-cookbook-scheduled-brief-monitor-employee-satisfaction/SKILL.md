---
name: "rar-cowork-cookbook-scheduled-brief-monitor-employee-satisfaction"
description: "Schedulable morning-brief email summarizing monitor employee satisfaction for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_employee_satisfaction", "rar_sha256": "63b50696d48a0406ee97f6046ecb3bc9438bdbdda1b8267dc55ae53f5561a159", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_employee_satisfaction`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_employee_satisfaction_agent.py` and in the RCI capsule.

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
