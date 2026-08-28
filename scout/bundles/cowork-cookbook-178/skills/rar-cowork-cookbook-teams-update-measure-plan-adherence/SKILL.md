---
name: "rar-cowork-cookbook-teams-update-measure-plan-adherence"
description: "Drafts a Teams channel post on measure plan adherence status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_plan_adherence", "rar_sha256": "a9d7dc05a79adc024bf6b148cacbea4237c06082005a7b16ec4fedf01f3db382", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_measure_plan_adherence`. The original RAPP
agent is preserved byte-for-byte in `teams_update_measure_plan_adherence_agent.py` and in the RCI capsule.

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

Measure plan adherence Teams Channel Update — Drafts a Teams channel post on measure plan adherence status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-plan-adherence
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_measure_plan_adherence_agent.py` and embedded as the fenced Python below (sha256 a9d7dc05a79adc02…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_measure_plan_adherence_agent.py` first:

```bash
python3 teams_update_measure_plan_adherence_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_measure_plan_adherence_agent.py   # or on stdin
python3 teams_update_measure_plan_adherence_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure plan adherence Teams Channel Update — Drafts a Teams channel post on measure plan adherence status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-plan-adherence
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_measure_plan_adherence',
    "version": '2.0.0',
    "display_name": 'Measure plan adherence Teams Channel Update',
    "description": 'Drafts a Teams channel post on measure plan adherence status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-measure-plan-adherence',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-measure-plan-adherence',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7da31101ee93b763',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-plan-adherence'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-measure-plan-adherence', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateMeasurePlanAdherence(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMeasurePlanAdherence'
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
    print(TeamsUpdateMeasurePlanAdherence().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
