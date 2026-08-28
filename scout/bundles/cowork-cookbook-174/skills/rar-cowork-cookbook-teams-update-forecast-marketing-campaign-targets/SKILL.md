---
name: "rar-cowork-cookbook-teams-update-forecast-marketing-campaign-targets"
description: "Drafts a Teams channel post on forecast marketing campaign targets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_marketing_campaign_targets", "rar_sha256": "7a055f0a1b5e3b9f2d9d3a2cfabb77a026ae8d77087b82ca179b8eae91921d78", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_forecast_marketing_campaign_targets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_forecast_marketing_campaign_targets_agent.py` and in the RCI capsule.

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

Forecast marketing campaign targets Teams Channel Update — Drafts a Teams channel post on forecast marketing campaign targets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-marketing-campaign-targets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_marketing_campaign_targets_agent.py` and embedded as the fenced Python below (sha256 7a055f0a1b5e3b9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_marketing_campaign_targets_agent.py` first:

```bash
python3 teams_update_forecast_marketing_campaign_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_forecast_marketing_campaign_targets_agent.py   # or on stdin
python3 teams_update_forecast_marketing_campaign_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast marketing campaign targets Teams Channel Update — Drafts a Teams channel post on forecast marketing campaign targets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-marketing-campaign-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_forecast_marketing_campaign_targets',
    "version": '2.0.1',
    "display_name": 'Forecast marketing campaign targets Teams Channel Update',
    "description": 'Drafts a Teams channel post on forecast marketing campaign targets status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-forecast-marketing-campaign-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-forecast-marketing-campaign-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cf8cd7be5d438e8d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/forecast-marketing-campaign-targets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-forecast-marketing-campaign-targets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateForecastMarketingCampaignTargets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateForecastMarketingCampaignTargets'
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
    print(TeamsUpdateForecastMarketingCampaignTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
