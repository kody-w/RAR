---
name: "rar-cowork-cookbook-ppt-exec-measure-goal-achievement"
description: "Generates an executive-ready PowerPoint deck on measure goal achievement status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_measure_goal_achievement", "rar_sha256": "d600ef3d69199f2171ab58356d56faee7ce52cc1d1947c2fba402a1d0eeaf7fc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_measure_goal_achievement_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-measure-goal-achievement:7100f68ad963b014221c3aeeaeb6d77630b1b11ca00bdee2e531fa388431288f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_measure_goal_achievement`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_measure_goal_achievement_agent.py` is
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

Measure goal achievement Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on measure goal achievement status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-measure-goal-achievement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_measure_goal_achievement_agent.py` and embedded as the fenced Python below (sha256 d600ef3d69199f21…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_measure_goal_achievement_agent.py` first:

```bash
python3 ppt_exec_measure_goal_achievement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_measure_goal_achievement_agent.py   # or on stdin
python3 ppt_exec_measure_goal_achievement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure goal achievement Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on measure goal achievement status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-measure-goal-achievement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_measure_goal_achievement',
    "version": '2.0.0',
    "display_name": 'Measure goal achievement Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on measure goal achievement status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-measure-goal-achievement',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-measure-goal-achievement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '06e5433ef2741e8c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-goal-achievement'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-measure-goal-achievement', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecMeasureGoalAchievement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMeasureGoalAchievement'
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
    print(PptExecMeasureGoalAchievement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
