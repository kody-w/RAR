---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-monitor-system-generated-numbers"
description: "Schedulable morning-brief email summarizing configure and monitor system generated numbers for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_monitor_system_generated_numbers", "rar_sha256": "edef6a92dfa7954c75720e0e893091e8a3ad42e8d989bb48c69fef91009c0f81", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_configure_and_monitor_system_generated_numbers`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py` and embedded as the fenced Python below (sha256 edef6a92dfa7954c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py` first:

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
    "version": '2.0.1',
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
