---
name: "rar-cowork-cookbook-scheduled-brief-forecast-service-demand"
description: "Schedulable morning-brief email summarizing forecast service demand for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_service_demand", "rar_sha256": "e8d56d695c231e795b75d31afefa7fb278562095e62296789e39c5571fd46f8a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_forecast_service_demand_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-forecast-service-demand:b75d7920b3d47362689338ceb4082f9508f043dac20537d181803c368fe798ff", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_forecast_service_demand`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_forecast_service_demand_agent.py` is
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

Forecast service demand Scheduled Email Brief — Schedulable morning-brief email summarizing forecast service demand for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-service-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_service_demand_agent.py` and embedded as the fenced Python below (sha256 e8d56d695c231e79…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_service_demand_agent.py` first:

```bash
python3 scheduled_brief_forecast_service_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_forecast_service_demand_agent.py   # or on stdin
python3 scheduled_brief_forecast_service_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast service demand Scheduled Email Brief — Schedulable morning-brief email summarizing forecast service demand for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-service-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_forecast_service_demand',
    "version": '2.0.0',
    "display_name": 'Forecast service demand Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing forecast service demand for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-forecast-service-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-forecast-service-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee7bb3bf845ac419',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/forecast-service-demand'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-forecast-service-demand', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefForecastServiceDemand(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefForecastServiceDemand'
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
    print(ScheduledBriefForecastServiceDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
