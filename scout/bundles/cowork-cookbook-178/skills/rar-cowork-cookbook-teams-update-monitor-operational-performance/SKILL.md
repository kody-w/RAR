---
name: "rar-cowork-cookbook-teams-update-monitor-operational-performance"
description: "Drafts a Teams channel post on monitor operational performance status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_operational_performance", "rar_sha256": "b8565ba781295596e478456fa3c9c558ba9755fb7e672033bd37620fd2e6ae9d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_monitor_operational_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-monitor-operational-performance:75ca9f12edb97052cfb21e286f38b163ae76313dcd076d48476fd8ae1a529f21", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_monitor_operational_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_monitor_operational_performance_agent.py` is
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
