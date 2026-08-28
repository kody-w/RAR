---
name: "rar-cowork-cookbook-ppt-exec-measure-goal-achievement"
description: "Generates an executive-ready PowerPoint deck on measure goal achievement status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_measure_goal_achievement", "rar_sha256": "3459a7004b112d299a1e04e02cc2bb920d5b1a968fed548c21356220829458c8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_measure_goal_achievement_agent.py` and embedded as the fenced Python below (sha256 3459a7004b112d29…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_measure_goal_achievement_agent.py` first:

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
    "version": '2.0.1',
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
