---
name: "rar-cowork-cookbook-scheduled-brief-forecast-service-demand"
description: "Schedulable morning-brief email summarizing forecast service demand for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_service_demand", "rar_sha256": "062e73d8fc02d1fa0e3742481fb76397d7c1b5e91851bee5cd7c030c753afe13", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_service_demand_agent.py` and embedded as the fenced Python below (sha256 062e73d8fc02d1fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_service_demand_agent.py` first:

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
    "version": '2.0.1',
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
