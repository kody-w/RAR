---
name: "rar-cowork-cookbook-dashboard-measure-goal-achievement"
description: "Produces a self-contained interactive HTML dashboard for measure goal achievement - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_goal_achievement", "rar_sha256": "0f7131ed26678494ac4dfb16ef8b864769e2795f854dca6b2047a1f4f468622f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_measure_goal_achievement_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-measure-goal-achievement:85402c28cb516cfdfc5c37d1e3cfe6037cd445f4f98c8b66d16d4be3eb1e7348", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_measure_goal_achievement`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_measure_goal_achievement_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_measure_goal_achievement_agent.py` and embedded as the fenced Python below (sha256 0f7131ed26678494…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_measure_goal_achievement_agent.py` first:

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
    "version": '2.0.0',
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjVpruX2FyPpQ9ZKVAbCI7OuIiJBBiEVqRcDmyWA6LWMWOPP7vc5CUWVXt9nT7xv1wVeEqCc55l+ddnveAf3uy6irIiqfXpy2wUkS04jgMQIFYqYvwWZsVEfwni2z4H+JkaVWEdl1lRfn0/OSC0inCvAqzFG7Xi8ytHVAiFlKC2Ps8LLbCFLhImFagsJwqbACy2KkK4lplYGdW4SJeViAJsMq6AIifWTFiOUEIGpCAtEI+I1kO0hLuh9b0iF1kbQmKZyTNkBlBU3AtVFciKQAu1GL3SBUApAlBC4oXaB7orCSPQfn0+suvz08h/P70+tuTE1slvPQ0e7dBvasXoXbum3K4P7ZSHy7Me4hPCn/noIDmJvCSCzzk8eunwddn5L/+K2qtwi9/fv2SIo/Pl6fhz6ZOb3ZVmVVW0EzHyi07jMOqf0G4uLX6EilAVRfpDTgIb+q/3Hd+k5TlyN+Hez/dlbz4oPrpyxMEp7AG8L88/YxAHL88FfXw/WWQkv/080ucQSR++vmbnLK2z8CpBmHQ6pe3x++HWLjw29LQu2n9O5R6D7MNvjx959zwuds9+Al3Pr2cszD96S44L7IGpFbqgJ9+/jOxTgCcKA7L6t+S+8tdcAAsF/r0MPzn5xvIvyLow6EPmX+uNodh/SuewOXv6p6RB1B/JvuG/z+IjmEJlB+I/1Nx/2wD+nfklz/17X/b8Ix4X55mIIbFVlh2DF6R3962+pz/5ZP77eKnX3+Hov+lmG1WF85NwltipaEHyurt7ZdP5e3yp19/+VTnMNeAlbzVRfzPZP4zXG96fkDwseqnH/dC/fs0SrM2RT4yHfkty/+j+P0FOVhx6H67Xr4i39fL8EGRwYl3pXcIvquZEtr6HY4/P/0OW0QKvamd221Y5f/5n4gaOkVWZl6FbJ2srhAY4CpMwGD8LghLZPco6q9bWVKUl8T9isCrQ7nDFmHVcYWIhRXGCKyHIeKDB5mHfP0/zq2xwhZ5b6yjj4b49miGb0MzfPuuGX59QXYBVJwVoR+msFFuOF1HLH/ok1DlLTnKOvncDFpvPfdmxoaXho5T1jH4G/L1X6t5u0l8yfvBkS8pjMy9hVcgybPCKsK4R6yhU9l9BT7DDgu7SZHFsW05ETL8VecvAzpGANIHZg5kFdABp64AEmcONN0LYVd+hmEvsxhSQjUgWUZhHCNuWECYsqK/0Q9E+3UQ9vXrVxta/iW9t2ICudNOOYILPgxGPn/OC+DFoR9UX1LgBBny6bffPyH/jfxvu27CBx06ZIUbYjCdY2S5XWkIrM16wGQgIBhly73F7rff76EYrEshT8KKCr0Q3DZDad8SYfDgHp/34ECfBxNB8dD0I25IG0BckLCCaMEqL5+/pIOIDC4t2rAE7yDeN9+hf4/2Xc8Qk/KBIYyTV2TJbe0tB4dgOlnhviCSh3wgBd2Fca2GiAZZWcG0hYzrgtQZyNSqvoUwzSqkhJVTev0zUpfQ1UHyVxuKHsBJYHuyqq+IyuuQ6bIY/jUAdFMPd2dpOAT+ka73y1BI8Qnm2PRdxAuiwSwskNwqrDworBLc1nnWPSMgw73vh8ItSPstMpD6LW9vNX3LPPXPpgnpH6eQjwkA+VKPMZxE/v+aYAZnOFHczEVuN58hc223Od0zb7BrkH6f3OAkcTPiVkbfpov3RvTeor+kcQijVfR/u6/0bsl2X3Nve9ADF7aVDfLud3GTG1YwZYYcKIohza0v6TsXPEOgYMDKoa3Byo6GPpF9KBzuvlsaQLiG39/mAuSejUOVwDxH8tqOQwfxIBC3kqiCYii4R2Bg/oCh+GCFOMEPXiFQOswNKB+BRoQwkSFf3KDTYOHAWepeBR/Lw2Hayu9xdhFYWeAFMYZEh8laIjaAI9OwBqLw6SYKhhZiDE38QLgMrPxuzDAaPwy0hlhkiVWB7yPwuAmTdiAdqO+jIqFUy7UqiGULgwALrrtH9sPOR6ygsclQHbdNP4b74SvyPWn9bahKaOM3WoDT/MD334EDW3mRlLfuBJk4KmHdJ+CRQDATbtT+cmfnO/1/2PL6h/PAT3/tyHDj2/2PkXtFgqrKy9fR6M6J75T44mTJCOZImIPyGz1+flTa56HSPn9XaT9IvgP1ivw1634Q8UjrVwR/wV6w4ZYSOmDI28cHgsF/np4+k8PdL+kGfIvyIxWGjge7MCzqd+J5XwLZxy+APyy+E1E58FcLKfPW/25E8pEJjzqB7TX1B9Yss+/qd/BpiOs9bB99Gt5KBwZwh3nPB8NhKB7ML8HTa1rH8fNTaiXg3zoEDc0YZiuEYzg8wcqBA1QVgtuvj2Fq+PHjYfBWU7AZuNnrUFqQ+ODg+4x8zLDPyPup4nZSS2t4rPplmJ8HlXAp/Odj7cdJ0wZP8CBX9flg+v2oNIxtj3H6j0YMFQUtvrXYgTIeJTpo/IMQ+MX3QfFHIavbFyt+9Imysga6hCz9qO4S2unC8eoZgaDBqhvowEpruOGPaqCeAlxqSNDu4O43/L65ld19+f0GQ3U/b/729N4vhu/3aeGeOMNZ9N+f6QZQ37n4bRBtDQJuk9cN49vE+gb9CwfO/e6WPwwQb/dMfHqF7QY8Pw1IFiEcw6+3E/bT3R7oyLdZF0qAjeNzOcwQI1hIUBJk9nxwIoJN7zsFw+XQva0fvrz++YD8px3gdUKR2NgZTxybwmnHcz2HcgjGxQHheIDGCMZxSZLySI+dOBObpl2cdkkbEMDGAUOQE2jGEMvEepgxwocoQAc+oP6/GNuf7hIgaYwpGorAPAYncOCOaZqZkCxpOaTr2TgNvIk9oUmGZsGYYSkPOuM6Fm2PMZKxcGg0SU/o8dgb5D3GxrtZb+8j+ntc7q3gDbbPJByMHluWM3EYnHRZxqIdQGA24QB8jLsMATCKJbzJBJBw/8fWR2yG0N09H/IWToxwcmkGPb89Yj3kIk3ClQuylLj7hx+xB4sxGHsT2GxBg5N5HEl2uL/01ik/VFFJn/OVeJku/X7LbMBcJvg5FV2sZKW2qrV38Jm+DtBsw0ZnnNCjUI7y8ThsjbFv6lK6jBgXZRY1cFbC/rih5aOfVyJfbNaNqI6MfdzL521QsBe5DIBpKtuJgI4Ktx+PTvsxY1yARJvMCB1xFVMcjsBUpfYKQxpXmhrvjGPuhOaCZ9QxeVByN00qf5zuBCPUhLMOlDi+HMzjpvaXcndg0MpdpGO1rs6rUuCVhVInBm40U+VikPNzBs57GugEe2Wba0S48c5t7AthNs1pdFq19PrQA1NrDqaFx3WxLsZGkBgT8gLxmcaohMeaaWQVKpr7XthcmyNRLkMqlhxpvxPDXoSnZUYllmJ3WhUWfjIcr9ysiakRlf1VPM+2TLTPc4bbLl1epGP5cDmX3KUqcINaZNhC1/ad0OCudTxdtjEV+0aylvNai/VSuS5DPOpyq107lyuP+nPeIYN8mwl7rBpXpm2C2pnMlgoeJ+urzE+L0cI9tMm2EVTqWFTB9oJhhLj1DlmqgKsbW9ZUvDKsNTGLy9TBl5sLX1s+utKLLUcKiq1taDy4mvlxF6xihe4u6apvtKI1PKvZ9fOCA4sQrPqDZJHn88oaUTSXGwqhd+0x6XFnwkyxvD4tijSOCQINtLA6qserSIIz3dXe/GBUFdnwOcOXJi6I6nJ8mpzXY3k1UcW+0kplwV/7RsyxpSGNu2pkni+T0Em3OYML0J5YmZh7t5luR6YzboPTblI4u1BYyFTMF1rmtL05Yq84bvYVzWT9hI3Ksi2vTc+scNESwyV/UBV1XNAnNKet/Z7VwK7ZC6uu0cZgtCu2o2kw4h3iNGo6z2knGaFOJSMbtdosndMjNGXoubQ6a7RyLTyALmWtkY+alieHQ4Inp6iZHbZZedjt6TLEOsfeLJaiaiWmzm5oAvVmbGLF8PC7TKeqghH5arVZUT1O1tvucF33Yh/kNjXhouYkHaV+5snzmPfD0xJM5HpDbKVe3BQb4YSZ1CI57AycLruWTM5hF9XofOO7HhpN1HZc026/AQsnoiQ6oki6E9C5tj1IIOLT2QTvrUs9s5fitZsyPCVsDefsYeMRzmYLc4NJ+5Qe2bQ/W1VFc16evB0p7s5r6TzGw4O2WCeOs9Mi0vY71YrambqdunSQofblYurAcDqtNJcb57SZMgeZ5ESGmOaJRMjLC9ePio4vj+kFDUw3MgPJ0QKRFkN0sg/SpKB2ACsE2sIvMXEFDsmjeW5PFxvMbJJgqbf+uiLO7panVtIkX66qceDymZ5uZ/5eIDLg7aPpKqqpyEyVpAz00Wl7KemJp3o1ofTUUsnnLWujG9nxnaMRZxXekJ5IslWeLHRd4bWcFzZaCc+5uWKjbZtul3np1xJVLFu10kThnAQWzcRlRrF2lWCBLtU43q4rOdEplMWk3naTZe31Wmtaoed1TXNdV6R6qj3uOj8dNX2+ilZYwzfmcqeJpaURi8jz/Ek2atCqDkaAE3WDp4hWNVZ05Jcze6X7YjIj+91MSfYB02+yqzJrwBZ1TF8D08M5XHRnwWCpGa9E7HLDsjtitjxbLix9u16kFBnj5eWgZgRjz3f4wbRXQFpNuTLnl/4ajTSsXqfruedz+EktOkwil9w+ks7buWQlCtAq6+jNlzNOUZeBgS+P8y23uuSXrIJBT93aXnMHCWsLT+XHQrhtDu2hCBpioXt8JFu4UmicQhmLAk/ya1WnliFsExfDq4hQMEY/FhgrUYJvqLmULo5MR2+352U+2stHi5lH5FwwMVpITosRm3HinNAdr+b8jdCrOjMbKWVIOhNylM421GikeMaUDFxBcRkr3rAXsVO4JbbcLGcyBpyTIrV+Qh2lvKRPXKMShGrv/SuHTWOML1bHUhCzerM7rHb7Tt82PKjXkFKSyg6Zbkeu+uPEBcFqvWSz3MiueSmt/QVuXehIYKMD7FWG7jNa0qx2Ahs63Wx7iAw/YfMlN89Uqr46oeBuO2EfyHK78NHLbIM2GmVoyZgG1S5x1GOhrYlK9g62ygn9TO4SJdlsMC2puy5y8p15NjDvJErmkjEFTyeIxJ7OVZCSLJWfLivqUKSXqUrJwbTa4ka+GrlsgZrlrJpvNeXiefNOXFeSaNdcL17NHXcNs5kwrmpbWZW7asmccl/AL5OspPDVaL8Q1vpuKbGQdJLrdFqeq/HIJndgHklro40FJSHW1XTuSsG6PdWMvDjSNT+LZHJfxtvciHrJ8bm+mEnnUk3LGJSSRJi2PZ4EswsfGFnk7yVaq+neOoTlZHox666aNv1yWVD2hCVi/JAdKu6w8BNppkwSw62V2dEGJh+Tuxgrqcsyxqvz5Lq3TyqaV7nKjZc9a8Gxwh6Xl2ueW9vciqOrlHTTA+2EmJnYmOHPs+OKwS9yRqEnti8XUR7LtBmPNlmn0WogeWq8ODD8/mT2i/XpSu1aTboWrjAx5ulq7o55sK7m9SGEhs79NRb3m1l7mEXLZcrsOM+9avlugi2tk3lajTBiRPnhKNDrguq1hTLd91Uk4Fc4GG5nu2pl4rPN4XDgRruOoZm63rkjymrlpXSGpVdzOluKE2e+aZkRrCR8JCdGf2UnkRKP0fRwXWSds4Otka3ZNA+DJWap/kJm6ZrURX7eHiS+XQOtNsbtOVhqwcgR+tiYm2FMTrYVjernOu4ST9W8wG7l3fqCr2ojLtK1LqnWOi5wWQ7JSe60+qK2/X2OnxqQXzZdS4Ew4y3WvcQJj0ZXjHNhKOSOyp3tTuqStk7G8/VibtTRTiZm8NSgSKrNrncGKaQ8t9ACYxsZ1DbiaKpajuZTdBv1Y/zC7OOU3FhrnQL7UdmaXUSmgoWSpdEebeXiz9KDYMqbcVBLsTwrroetPFalZLnFUifpO0whGIzm6ottyb6Xy6sNcWIkR4zNDR2QziHZzIz1BYh7VccvmyO2PZ9rvGvWqWnu+St73sIkkLF97hpRLBYxr6RznLwwAlbWo21S8uj8siAkzuVXLRgVBdqZYe6vNDgvLE6dYJGwfjECFuBp2eAbc7Z3r6hcRRhNHHpBZuYMeoARN9jqOimXnuiLqLsnnKu6D7XLPktn070irVeaGRgMdZan5OWsHeTtuLjkqjsf2w4pMgGfjT0NXWI2HQWpS08rsqqZnD6tz7Pg4O4pTiuYbSmvk3VOSxrNpetVWHKYxfPVtN1P9ag6iMdrbhiKPD312aQN8gMTHTRgFJcRTo3ZHXng913dRwRXqq5aBmo1s087HbbVihG2ByVZuHweqQ1h9JbvhxvCK+Om49WTNk5PVK2wZ2te061igGA2xehquZbnfj6SD/uL0J3X/qntk6NW2cL5Co8F8mlHoemJb3zGqdmGI5ar1GV2li+1p2tLUdnRda4ABvzoXsTGRqXZcZOud2u1ZKYSfW0nYqNMxoq2lZlamh9PES0lnL3XL4d0Kkh+VlarNLngp33GtYEZoCLXnsRc4ibHk3rkyUI7+IYs2kKfOckxq/TG7KYXsr5wU3yBY5eJQizOPiM2hjvdcbGEd5LinI5G63h6hm1Z3ggnStck8+DcEd2W74+BaB78Qz+yxY4ayd7aIVZolBHU4rgj8M1OlrNwJuIAXxojwVG23oSXCSJbnQU2ZcrTPK1jMEXRDT7aKKOOVizaU/Bd5ei4EVZMeS4nNa8UR1R0mZasg7Ai7HIt8kR1bom9MVvvtxhkGYPZnQ8zO6/iqSlgYDfaxC2cTmO3csZ4h5Xw+HbERUpLC+CH1lmCM3II5tJeGKHj0wwPOCuvJtKlH3st6nDsgcjnHM+Ubr9Cc6f3MgZrLnTJg3zGWkJLle5C57qG2SqKczzRYyGYMGVhX3OuUKasrJ8B76lHcK2mddP1M70/wqYo7lDf4A6G2IyKFJXTmN0BmqLSI94HxlVmKd6mgS9O1piGCXpC0YK3RmMwdk6xA8b7UXbUpcyfEw26EdYTjss7jCJ3YrLAFpFqR0SYUedJ4uKu0l93POP2TQLCVhyft4xLi+fW4UCFZ0rqyD4Ts2CSU1fhJCjq2eT6Hj03sro7xj6c0ydT2tmotK+3HnaceeZmbRhgAwh+1jK2bDeRgkb1erwda5JPYuj65KK9ntdc686WcaEGqBVaexSUmrlAKes8Mo5mqKOVx7bdKWY2irffKJy2MbkJM9qe6EVVrK4ANUN7WuDjcnGeH8pWK2RIXQVktrizqQ1hX30uZBt8Vq8SJmYWhaeYrJ9kPjdyrSbFTku2K+nj3NCPq6WAz4vxmeXh4QWvjaalXclfO4mox71Zn46b1XmSKnG3UJkt54nG1eyouT6dxDic2BtvdZ2uTjGLr/aN4+YdS866dbm0N9ZYco7VdregcobtyEm40k+exdHRPFdcvXJLHtOVWeZfhY0fWdNL1ZsnXZsG6ro9XIjJKNsvcfEqbfXRZLIq02xWyqhOOJWtsgQ1vk6Ls9ZQdH88JVRSCWfMZ5ZsZCsLL92KE62I5x5Um0ij4xwwWpECY+fV887lU1lX2vVmVJ7QjiTFLvCZCeNsknLBmenRbqh67Hb2FTcWzohbGWFry+fiHNfCaEdTh/FhxWqYSwDmUKxbXKnzMp1iTaBnDOCnKjfhBGUcFH2zHqNF3UlwvCk9ctMflQy3pYm3yCQy6W06O7KazavjhGivx5CzFm5zOvOtBwzGZuKU8RQ0QSUmbo/HWr6ujz1JjSoloPIFuyqEJpU7OIYxR3LVsb23r6fLwEXhRC8QxoltQkbPWDRER9F0rlNHTKnYBGdXe6WL9WhhzOXMF/R4s3Bt8zySS3t60fLFeWnVNagnfEE3YxMV8yY6zhiy9poiP0bCPO/MWl9TrrUk9weiKxohLWmCJdC9ox0DPrikGMBW+vrso34L/Gx96DMZVVR9zVS9sM0qUnCCFFY9zlhMlGYdLnUS308xD1+j5w7n0pL0Ft36KJQ7PbQbdaFyiubLJIh5Y8ytbMzcUzvvYu9TzVdJJ55HMEO3Yx+L9G1xOVSbdgIp3oFDAcsY5HWFzpojMeePU5PYpjMvpDK9dJKYJsJuRqyUusczynNLaus4M0fsGt5fQhKRTBdc0KwUMy87KuMd0HfelQM21pOLlNOIyNIWJo9d1KUwns+V2S4mj75yvUTKEh7aJjiaAiU7MQ7WEYJEL6zzsqfxc+SNOCAR1Q5dyWuOe3p+ur3ufXrFIftPnp+G9wGPp/p/7ZGwfw3zt4csgiGo56f/d08r708O39/53R7xA8t9vWl//Stm/vr8VDghNOn+GLmMa//xiPIfnsl+/tdPiof9/f2d9fB6sqveX4pUln97lB3C02ZZFf1bmcX17UE2BLsuh/9vpXx7vFB4ujmW5Le3E+8q4XcvK4BjldVblb09XmTcXh4nwA2tCjx++o/n/nBvD4MWOuUbQVNvoMgHTx8vn4aHt8Pbp6ff/weQ9+8VpScAAA== -->
