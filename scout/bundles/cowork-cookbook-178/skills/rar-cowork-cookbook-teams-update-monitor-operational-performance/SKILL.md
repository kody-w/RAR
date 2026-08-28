---
name: "rar-cowork-cookbook-teams-update-monitor-operational-performance"
description: "Drafts a Teams channel post on monitor operational performance status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_operational_performance", "rar_sha256": "591bb13fa5600c48538c7af7792146eed63132bebcbf23321dba32e3159a79d2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_monitor_operational_performance`. The original RAPP
agent is preserved byte-for-byte in `teams_update_monitor_operational_performance_agent.py` and in the RCI capsule.

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

Monitor operational performance Teams Channel Update — Drafts a Teams channel post on monitor operational performance status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-operational-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_operational_performance_agent.py` and embedded as the fenced Python below (sha256 591bb13fa5600c48…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_operational_performance_agent.py` first:

```bash
python3 teams_update_monitor_operational_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_monitor_operational_performance_agent.py   # or on stdin
python3 teams_update_monitor_operational_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor operational performance Teams Channel Update — Drafts a Teams channel post on monitor operational performance status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-operational-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_monitor_operational_performance',
    "version": '2.0.1',
    "display_name": 'Monitor operational performance Teams Channel Update',
    "description": 'Drafts a Teams channel post on monitor operational performance status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-monitor-operational-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-monitor-operational-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cbea477f8266496b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/monitor-operational-performance'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-monitor-operational-performance', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateMonitorOperationalPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMonitorOperationalPerformance'
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
    print(TeamsUpdateMonitorOperationalPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
