---
name: "rar-cowork-cookbook-teams-update-forecast-revenue"
description: "Drafts a Teams channel post on forecast revenue status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_revenue", "rar_sha256": "2466a13183d7bf95c8ca2521572906bd146613f990c9013f61ed23c339202551", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_forecast_revenue_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-forecast-revenue:4c411d9aece3d47d42fa6243f2e938761529366aa64e984a7a03038393533450", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_forecast_revenue`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_forecast_revenue_agent.py` is
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
