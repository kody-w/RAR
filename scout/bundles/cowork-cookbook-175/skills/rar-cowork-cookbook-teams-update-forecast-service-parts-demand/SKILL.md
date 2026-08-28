---
name: "rar-cowork-cookbook-teams-update-forecast-service-parts-demand"
description: "Drafts a Teams channel post on forecast service parts demand status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_service_parts_demand", "rar_sha256": "456d6b5949144ed146289cf7113c9ac3dd27dc3095c597aeb16415b9ddb5e4a2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_service_parts_demand_agent.py` and embedded as the fenced Python below (sha256 456d6b5949144ed1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_service_parts_demand_agent.py` first:

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
    "version": '2.0.0',
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
