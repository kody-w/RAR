---
name: "rar-cowork-cookbook-teams-update-forecast-marketing-campaign-targets"
description: "Drafts a Teams channel post on forecast marketing campaign targets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_marketing_campaign_targets", "rar_sha256": "f97c267193bee2f39202ca7e73a65e0df832a7ed99050b25156d7da1685dd749", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_marketing_campaign_targets_agent.py` and embedded as the fenced Python below (sha256 f97c267193bee2f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_marketing_campaign_targets_agent.py` first:

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
    "version": '2.0.0',
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
