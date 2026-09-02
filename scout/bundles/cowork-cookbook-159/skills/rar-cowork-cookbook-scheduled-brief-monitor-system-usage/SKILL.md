---
name: "rar-cowork-cookbook-scheduled-brief-monitor-system-usage"
description: "Schedulable morning-brief email summarizing monitor system usage for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_system_usage", "rar_sha256": "acc16ce1ffa70a64541ca19c66023f823b23bf6272ad4495f34800a19991ad5c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_monitor_system_usage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-monitor-system-usage:81dd92d02e77facca0da52bde7d5caac0d1ca871fd738635b00189358b6e1b38", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_monitor_system_usage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_monitor_system_usage_agent.py` is
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

Monitor system usage Scheduled Email Brief — Schedulable morning-brief email summarizing monitor system usage for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-system-usage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_system_usage_agent.py` and embedded as the fenced Python below (sha256 acc16ce1ffa70a64…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_system_usage_agent.py` first:

```bash
python3 scheduled_brief_monitor_system_usage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_system_usage_agent.py   # or on stdin
python3 scheduled_brief_monitor_system_usage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor system usage Scheduled Email Brief — Schedulable morning-brief email summarizing monitor system usage for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-system-usage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_system_usage',
    "version": '2.0.0',
    "display_name": 'Monitor system usage Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing monitor system usage for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-monitor-system-usage',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-system-usage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b0478e985dc45228',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-system-usage'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-monitor-system-usage', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefMonitorSystemUsage(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorSystemUsage'
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
    print(ScheduledBriefMonitorSystemUsage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
