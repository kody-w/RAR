---
name: "rar-cowork-cookbook-teams-update-forecast-service-parts-demand"
description: "Drafts a Teams channel post on forecast service parts demand status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_service_parts_demand", "rar_sha256": "456d6b5949144ed146289cf7113c9ac3dd27dc3095c597aeb16415b9ddb5e4a2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_forecast_service_parts_demand_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-forecast-service-parts-demand:c59506622640ac629b6792c4b2a05564ed6e512e89f70f35cf424caa7b5f019d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_forecast_service_parts_demand`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_forecast_service_parts_demand_agent.py` is
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
