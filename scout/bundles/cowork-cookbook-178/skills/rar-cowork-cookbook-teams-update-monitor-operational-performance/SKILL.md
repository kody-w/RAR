---
name: "rar-cowork-cookbook-teams-update-monitor-operational-performance"
description: "Drafts a Teams channel post on monitor operational performance status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_operational_performance", "rar_sha256": "b8565ba781295596e478456fa3c9c558ba9755fb7e672033bd37620fd2e6ae9d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_operational_performance_agent.py` and embedded as the fenced Python below (sha256 b8565ba781295596…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_operational_performance_agent.py` first:

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
    "version": '2.0.0',
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
