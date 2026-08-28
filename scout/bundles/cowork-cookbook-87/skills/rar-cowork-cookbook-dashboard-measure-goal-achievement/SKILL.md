---
name: "rar-cowork-cookbook-dashboard-measure-goal-achievement"
description: "Produces a self-contained interactive HTML dashboard for measure goal achievement - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_goal_achievement", "rar_sha256": "c86b0e2bc52b80f11a44fb255b27d6645d26cfe3d8c624dee79a42f0f939e4ca", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_measure_goal_achievement`. The original RAPP
agent is preserved byte-for-byte in `dashboard_measure_goal_achievement_agent.py` and in the RCI capsule.

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

Measure goal achievement Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for measure goal achievement - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-goal-achievement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_measure_goal_achievement_agent.py` and embedded as the fenced Python below (sha256 c86b0e2bc52b80f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_measure_goal_achievement_agent.py` first:

```bash
python3 dashboard_measure_goal_achievement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_measure_goal_achievement_agent.py   # or on stdin
python3 dashboard_measure_goal_achievement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure goal achievement Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for measure goal achievement - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-goal-achievement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_measure_goal_achievement',
    "version": '2.0.1',
    "display_name": 'Measure goal achievement Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for measure goal achievement - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-measure-goal-achievement',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-measure-goal-achievement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '412dc74acad4659b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-goal-achievement'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-measure-goal-achievement', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardMeasureGoalAchievement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMeasureGoalAchievement'
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
    print(DashboardMeasureGoalAchievement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
