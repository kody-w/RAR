---
name: "rar-cowork-cookbook-scheduled-brief-monitor-system-usage"
description: "Schedulable morning-brief email summarizing monitor system usage for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_system_usage", "rar_sha256": "3b2b5ec3283b1343e4c9f3e69010f875f31d7aabb8496532f2b78a6f3d16a765", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_system_usage`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_system_usage_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_system_usage_agent.py` and embedded as the fenced Python below (sha256 3b2b5ec3283b1343…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_system_usage_agent.py` first:

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
    "version": '2.0.1',
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
