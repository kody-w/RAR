---
name: "rar-cowork-cookbook-ppt-exec-measure-goal-achievement"
description: "Generates an executive-ready PowerPoint deck on measure goal achievement status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_measure_goal_achievement", "rar_sha256": "d600ef3d69199f2171ab58356d56faee7ce52cc1d1947c2fba402a1d0eeaf7fc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_measure_goal_achievement`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_measure_goal_achievement_agent.py` and in the RCI capsule.

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
