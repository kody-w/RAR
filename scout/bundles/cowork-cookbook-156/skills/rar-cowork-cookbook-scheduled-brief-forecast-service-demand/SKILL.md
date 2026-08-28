---
name: "rar-cowork-cookbook-scheduled-brief-forecast-service-demand"
description: "Schedulable morning-brief email summarizing forecast service demand for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_service_demand", "rar_sha256": "e8d56d695c231e795b75d31afefa7fb278562095e62296789e39c5571fd46f8a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_forecast_service_demand`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_forecast_service_demand_agent.py` and in the RCI capsule.

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
