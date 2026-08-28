---
name: "rar-cowork-cookbook-teams-update-forecast-revenue"
description: "Drafts a Teams channel post on forecast revenue status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_revenue", "rar_sha256": "2466a13183d7bf95c8ca2521572906bd146613f990c9013f61ed23c339202551", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_forecast_revenue`. The original RAPP
agent is preserved byte-for-byte in `teams_update_forecast_revenue_agent.py` and in the RCI capsule.

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

Forecast revenue Teams Channel Update — Drafts a Teams channel post on forecast revenue status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_revenue_agent.py` and embedded as the fenced Python below (sha256 2466a13183d7bf95…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_revenue_agent.py` first:

```bash
python3 teams_update_forecast_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_forecast_revenue_agent.py   # or on stdin
python3 teams_update_forecast_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast revenue Teams Channel Update — Drafts a Teams channel post on forecast revenue status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_forecast_revenue',
    "version": '2.0.0',
    "display_name": 'Forecast revenue Teams Channel Update',
    "description": 'Drafts a Teams channel post on forecast revenue status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-forecast-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-forecast-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44cc808c795599bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/forecast-revenue'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-forecast-revenue', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateForecastRevenue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateForecastRevenue'
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
    print(TeamsUpdateForecastRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
