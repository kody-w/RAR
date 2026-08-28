---
name: "rar-cowork-cookbook-teams-update-forecast-revenue"
description: "Drafts a Teams channel post on forecast revenue status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_revenue", "rar_sha256": "949bd52f9533963bf2949c39b2ccc1882e2d83f692e2ce9c00378dea55978c67", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_revenue_agent.py` and embedded as the fenced Python below (sha256 949bd52f9533963b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_revenue_agent.py` first:

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
    "version": '2.0.1',
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
