---
name: "rar-cowork-cookbook-teams-update-forecast-marketing-campaign-targets"
description: "Drafts a Teams channel post on forecast marketing campaign targets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_marketing_campaign_targets", "rar_sha256": "f97c267193bee2f39202ca7e73a65e0df832a7ed99050b25156d7da1685dd749", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_forecast_marketing_campaign_targets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-forecast-marketing-campaign-targets:4b0ec5b3f893e5c6aab75166e1bc7e0a0590749e072f827b5b9c23c7c22e6232", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_forecast_marketing_campaign_targets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_forecast_marketing_campaign_targets_agent.py` is
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
