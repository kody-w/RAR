---
name: "rar-cowork-cookbook-teams-update-measure-plan-adherence"
description: "Drafts a Teams channel post on measure plan adherence status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_plan_adherence", "rar_sha256": "a9d7dc05a79adc024bf6b148cacbea4237c06082005a7b16ec4fedf01f3db382", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_measure_plan_adherence_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-measure-plan-adherence:59b48e3d41cf76aff472a3966740f081136f1d02dd535b96dc833628618e556d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_measure_plan_adherence`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_measure_plan_adherence_agent.py` is
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
