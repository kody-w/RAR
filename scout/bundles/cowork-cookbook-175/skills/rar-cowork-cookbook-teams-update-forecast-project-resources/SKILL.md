---
name: "rar-cowork-cookbook-teams-update-forecast-project-resources"
description: "Drafts a Teams channel post on forecast project resources status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_project_resources", "rar_sha256": "fbca85db68f707b8495fd68431268869d02277419901f13d330f900df61abad8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_forecast_project_resources`. The original RAPP
agent is preserved byte-for-byte in `teams_update_forecast_project_resources_agent.py` and in the RCI capsule.

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

Forecast project resources Teams Channel Update — Drafts a Teams channel post on forecast project resources status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-project-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_project_resources_agent.py` and embedded as the fenced Python below (sha256 fbca85db68f707b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_project_resources_agent.py` first:

```bash
python3 teams_update_forecast_project_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_forecast_project_resources_agent.py   # or on stdin
python3 teams_update_forecast_project_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast project resources Teams Channel Update — Drafts a Teams channel post on forecast project resources status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-project-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_forecast_project_resources',
    "version": '2.0.0',
    "display_name": 'Forecast project resources Teams Channel Update',
    "description": 'Drafts a Teams channel post on forecast project resources status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-forecast-project-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-forecast-project-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '362660ba24797920',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/forecast-project-resources'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-forecast-project-resources', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateForecastProjectResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateForecastProjectResources'
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
    print(TeamsUpdateForecastProjectResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
