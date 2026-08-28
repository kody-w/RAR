---
name: "rar-cowork-cookbook-scheduled-brief-forecast-marketing-campaign-targets"
description: "Schedulable morning-brief email summarizing forecast marketing campaign targets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_marketing_campaign_targets", "rar_sha256": "9aa6cc11e8af5a4a50e28fa6b8cca4bbec7266e46522e8e5641fcea7ac1cb0ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_forecast_marketing_campaign_targets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_forecast_marketing_campaign_targets_agent.py` and in the RCI capsule.

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

Forecast marketing campaign targets Scheduled Email Brief — Schedulable morning-brief email summarizing forecast marketing campaign targets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-marketing-campaign-targets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_marketing_campaign_targets_agent.py` and embedded as the fenced Python below (sha256 9aa6cc11e8af5a4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_marketing_campaign_targets_agent.py` first:

```bash
python3 scheduled_brief_forecast_marketing_campaign_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_forecast_marketing_campaign_targets_agent.py   # or on stdin
python3 scheduled_brief_forecast_marketing_campaign_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast marketing campaign targets Scheduled Email Brief — Schedulable morning-brief email summarizing forecast marketing campaign targets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-marketing-campaign-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_forecast_marketing_campaign_targets',
    "version": '2.0.0',
    "display_name": 'Forecast marketing campaign targets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing forecast marketing campaign targets for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-forecast-marketing-campaign-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-forecast-marketing-campaign-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '99c0c0116db6c114',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/forecast-marketing-campaign-targets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-forecast-marketing-campaign-targets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefForecastMarketingCampaignTargets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefForecastMarketingCampaignTargets'
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
    print(ScheduledBriefForecastMarketingCampaignTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
