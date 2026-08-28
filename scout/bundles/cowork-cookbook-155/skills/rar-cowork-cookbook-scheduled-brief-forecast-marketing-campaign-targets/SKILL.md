---
name: "rar-cowork-cookbook-scheduled-brief-forecast-marketing-campaign-targets"
description: "Schedulable morning-brief email summarizing forecast marketing campaign targets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_marketing_campaign_targets", "rar_sha256": "252a5fe00b5fb6a2199ef85bbc7503a8370869395badd26d05c9a68b42ecc85f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_marketing_campaign_targets_agent.py` and embedded as the fenced Python below (sha256 252a5fe00b5fb6a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_marketing_campaign_targets_agent.py` first:

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
    "version": '2.0.1',
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
