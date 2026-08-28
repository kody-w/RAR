---
name: "rar-cowork-cookbook-teams-update-forecast-service-parts-demand"
description: "Drafts a Teams channel post on forecast service parts demand status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_service_parts_demand", "rar_sha256": "e55a0af09fcfb70624f56ae6cc886c12b739514e4c6d5dafe28aa569bedce031", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_forecast_service_parts_demand`. The original RAPP
agent is preserved byte-for-byte in `teams_update_forecast_service_parts_demand_agent.py` and in the RCI capsule.

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

Forecast service parts demand Teams Channel Update — Drafts a Teams channel post on forecast service parts demand status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-service-parts-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_service_parts_demand_agent.py` and embedded as the fenced Python below (sha256 e55a0af09fcfb706…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_service_parts_demand_agent.py` first:

```bash
python3 teams_update_forecast_service_parts_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_forecast_service_parts_demand_agent.py   # or on stdin
python3 teams_update_forecast_service_parts_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast service parts demand Teams Channel Update — Drafts a Teams channel post on forecast service parts demand status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-service-parts-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_forecast_service_parts_demand',
    "version": '2.0.1',
    "display_name": 'Forecast service parts demand Teams Channel Update',
    "description": 'Drafts a Teams channel post on forecast service parts demand status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-forecast-service-parts-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-forecast-service-parts-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d77defff89e3754',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/forecast-service-parts-demand'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-forecast-service-parts-demand', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateForecastServicePartsDemand(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateForecastServicePartsDemand'
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
    print(TeamsUpdateForecastServicePartsDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
