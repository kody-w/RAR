---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-monitor-system-generated-numbers"
description: "Schedulable morning-brief email summarizing configure and monitor system generated numbers for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_monitor_system_generated_numbers", "rar_sha256": "f212d9152d9303a10d3329fe100057b0006dd90444480f7fb73850407020cb9e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-configure-and-monitor-system-generated-numbers:18f173bd06d195ef760d02aa9608f10ac64b046a4cbc9db4a04f17d648a135e2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_configure_and_monitor_system_generated_numbers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py` is
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

Configure and monitor system generated numbers Scheduled Email Brief — Schedulable morning-brief email summarizing configure and monitor system generated numbers for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-monitor-system-generated-numbers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py` and embedded as the fenced Python below (sha256 f212d9152d9303a1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py` first:

```bash
python3 scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py   # or on stdin
python3 scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and monitor system generated numbers Scheduled Email Brief — Schedulable morning-brief email summarizing configure and monitor system generated numbers for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-monitor-system-generated-numbers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_configure_and_monitor_system_generated_numbers',
    "version": '2.0.0',
    "display_name": 'Configure and monitor system generated numbers Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing configure and monitor system generated numbers for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-configure-and-monitor-system-generated-numbers',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-configure-and-monitor-system-generated-numbers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '75d6a6654dcf2c9a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-monitor-system-generated-numbers'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-configure-and-monitor-system-generated-numbers', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefConfigureAndMonitorSystemGeneratedNumbers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConfigureAndMonitorSystemGeneratedNumbers'
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
    print(ScheduledBriefConfigureAndMonitorSystemGeneratedNumbers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
