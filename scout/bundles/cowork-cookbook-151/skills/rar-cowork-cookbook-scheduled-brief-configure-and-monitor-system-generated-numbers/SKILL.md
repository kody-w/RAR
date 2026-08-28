---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-monitor-system-generated-numbers"
description: "Schedulable morning-brief email summarizing configure and monitor system generated numbers for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_monitor_system_generated_numbers", "rar_sha256": "f212d9152d9303a10d3329fe100057b0006dd90444480f7fb73850407020cb9e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
