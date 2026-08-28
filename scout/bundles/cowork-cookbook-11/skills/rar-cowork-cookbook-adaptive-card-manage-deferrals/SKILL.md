---
name: "rar-cowork-cookbook-adaptive-card-manage-deferrals"
description: "Produces a reusable Adaptive Card JSON snapshot of manage deferrals status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_deferrals", "rar_sha256": "77975301bdd769241dd01cdfa8801e9c7e84a100ad62ca110d80dfeeeb61e642", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_deferrals`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_deferrals_agent.py` and in the RCI capsule.

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

Manage deferrals Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage deferrals status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-deferrals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_deferrals_agent.py` and embedded as the fenced Python below (sha256 77975301bdd76924…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_deferrals_agent.py` first:

```bash
python3 adaptive_card_manage_deferrals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_deferrals_agent.py   # or on stdin
python3 adaptive_card_manage_deferrals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage deferrals Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage deferrals status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-deferrals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_deferrals',
    "version": '2.0.0',
    "display_name": 'Manage deferrals Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage deferrals status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-deferrals',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-deferrals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9ab23900cc6b5fd4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/manage-deferrals'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-manage-deferrals', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardManageDeferrals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageDeferrals'
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
    print(AdaptiveCardManageDeferrals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOi2NLuX/Hu90NVv1ZtJgGpEx1xARFlUJRBoKujmmExKJMMIvbt/34X6t7Vdfqc854TcSOuNSiyVq7MJzOfzLXw9xeva5OyfvnyogOvmIhelqUJqCdeEU74si/rE3wrTz78NwnKoq1Tv2vLunn59BKCJqjTqk3LAk7X6jLsAtBMvEkNusbzMzBhQw/evoAJ79XhRNK3m0lTeFWTlO2kjCa5V3gxmIQgAnXtZc2kab22ayZRWU9A7oMwTIt4khaT0GsSv4Qymk/whpdm8B2OMYCXN69QE3D18ioDzcuXX3799JLCzy9ffn8JMq+BX728aTEqod6XXLytCOdmXhHDQdUAYSjgdQVquH4Ov4J6TZ5XHxuQRZ8m//3fp96r4+anL1+LyfP19WX8s++KSZuASVt6TQvCSeBVnp9maTu8Ttis94YGotJ2dTHi00AUi/j1MfO7pLKa/Dze+/hY5DUG7cevLyVUwRsx/vry02j015e6Gz+/jlKqjz+9ZmUP6o8/fZfTdP4RBO0oDGr9+u15/RQLB34fmkb3VX+GUh/e9MHXlz8ZN74eeo92wpkvr8cyLT4+BFd1eQGFVwTg40//TGyQgOCUpU37b8n95SE4AV4IbXoq/tOnO8i/TqZPg95l/vNlK+jW/8QSOPxtuU+TJ1D/TPYd/78TnaUFDP03xP+huH80Yfrz5Jd/atu/mvBpEn19WYAMhnU9ptqXye/fdE3gf/kQfv/yw69/QNH/oxi97OrgLuEbzMg0Ak377dsvH5r71x9+/eVDV8FYg7n2rauzfyTzH+F6X+cHBJ+jPv44F65vFqei7IvJe6RPfi+r/1X/8TqxvCwNv3/ffJn8OV/G13QyGvG26AOCP+VMA3X9E44/vfwB6aGA1nTB/TbM8v/6r4maBnXZlFE70YOyayfQwW2ag1F5I0mbCfw75nYNIK5NOhLbYxyM/9HDo8aQzX7738GdLz8HT75EvCfxfAsg83x7sN23d7b77XViQKllncZp4WWTPatpX8chRTuuWNWgAfUFcok/tOAzZKHP44eRDn/714K/3WW8VsNvdxZPH8y059cjKzVdBl5Hyw4JKJ52BJD4wRUEHRSflQHUJUohm36CFjdlBum7HVFoTmmWTcK0hiaX9XCXDZH6Mgr77bfffMjRX4sHjRKTR2VoEDjgXZ3J58/QqChL46T9WoAgKScffv/jw+T/TP7VrLvwcQ0NsvnTD1DDezGBedXlcBh0EXQqJI27H37/4wktFFPAUga9lkYpeEyGcXkC4RvO+or9jJPUxAcQX4htXpV1ey867etkHU3e9YWLjrdG9k7KpoU1qwJFCIpggFI9aM47kgWsbQ0MviYaPk26BtxX/c2vvbuKOUxwr/1tovIarBVlBv8b1bwPgpPLIoXwv0fB43sopP7QTLg3Ea+TzRiJk8qrvSqpvecakffwC6wRb9OhcG9SgP5rMdZEMEJ1T4sHPHAQRCZ4uvTz6HNY4nMYTmHztvZ9jDdWNONe2eqvRfMMea8eXRHAEgAXjbs0HAvB354hBUt8l4V3/KCmo6SnF8KnV+4xqP59A6A/GoAf+4avHY5is8n/twZj1JQVxb0gsoawmAgbY+88EBwbohHpRw8Fi/1d8j1bvjcAb/TxxqJfiyyF4VAPf3uMvOP+HPNgpq6GMO3Z/V0+dDpEcJR7j8kxxup6jGbva/FG158gJndugm6BCQwDfIyrtwXHu2+aJtDQ8fp76b77EIIHvQ7jblJ1fgZjIgIg9L3gBLWqx7x6+gAGKBiB7ZM0SH6wagKlwziA8idQiRRmCqT0O3SbEpoJYY7qMv8+PB0bourh0nACO07wOjnA1BjDo4H5CLuacQxE4cNd1CQHEGOo4jvCTeJVD2XGJvWpoDf6osxhxP7ZA8+b34P5rsuoPpQKybSFWPYjtYbg+vDsu55PX0Fl8zH97pN+dPfT1smf68rfvhZ3Hd/ZHGZ1do/Y7+BMYDblzZ1GR1JqILHk4BlAMBLu1ff1UUAfFfpdly9/6cw//mfN+70kmj967sskaduq+YIgjzL2VsVeISUgMEbSCjTvFe3zWHg+P9Lr83t6/SD1AdKXyX+m2Q8iniH9ZYK9oq/oeEtJAzDG7PMFgeA/c87n2Xj3a7EH3z38DIORTrMBltD32vI2BBaYuAbxOPhRa5qxRPWwKt7JFfrga/EeBc8cgdxdxGNhbMo/5e69yEKfPlz2XgPgraKFa4djOxaDcZ+Sjeo34OVL0WXZp5fCy8H/uD8ZWR5GKYRi3NPAjIG9TZuC+9V7nzNe/Lgdu+cSJIGw/DKm1KfJ2JN+mry3l58mbw3/fQNVdHDH88vY2o5LwqHw7X3s+17PBy9wf9UO1aj2YxczdlTPTvevSoyZBDWGpN2Muryl5rjiX4TAD3EM6r8K2d4/eNmTHyCFj3U4bd+yuoF6hrCrgcx9GbMNJhAMzA5O+OsycJ0anDtY8MLR3O/4fTerfNjyxx2G9rEV/P3ljSeePni2fXA4TMjPzVjyEBikcEF4/QgneO8/bAifsyGvwZYETqdphiYJFPPDkKYYfIaFIYoFYeTN5ygGmIAG85mHoagXUnjgYRgaztEQEjfwKQxQMxzKe4Tkt7Gqp6NGuOcF84DGZiFDe1QACNQnAoDhWEgTACUZIprPwQyC8z71BEnxaebDrBHD9950hONp7e8vPjWDI1ezZs0+XjzCWB6Fz/zN1Z/WVBQbBbP2z9Y+zyhW7tqlHUSS24qnGBBhWfBL+QBEGHFaUqnJdUYf1A2/ojgN1yOHlrbB+Wrm9IHvvU4x5xI7125TkyamQsmvlb1O0rf2wFeHdT6QUpYvZ56v11sj40KRiBN8aDoTiXylnl6xc7g+C251tcpKnt9iI8YKpNOO3TJUSQXZi6LnHvxFY9YV0Wf62cVVJzUOh6l7lAo5BP5BEMUil9mhHxAVhPpcRrd7amuQc0S7kVRkSzPGPYCL0jAIvymyfc0JpOmfkstK9pe76hbQ8mbfVYdgrayaTi064RLPM6s0USnwNuo1NS8higRXyRbkqDcNOdZN0kxdEBQk5swz+lTWVlLtLj6/W3GuXiscLwJDplabpebNBO9wkHPg6mfqip+TfHs9t0x4i0/anjC90j9F6lwwuFOZs7PiHBw1GUkN3m0kc+fNpztvexL5hsC74CSIl5BYuxuVXsy0E+wsBnGv77ia6QLy2GSBQjqbq3X2/daVBnS5tm6uWuJlskumBL1Y6F1tKxvH3Z4PZLeYOUO39ndWk89mXj8tNwrZ5+d6wM+FOFyYaljT1aEiRSzWVr22suTTxtldsU033cYHq2GMeeiSTbvStn0or+NkIElvChBUasIzyeO+baDuYTPbebU4MAVu4tqyU2CnLde6u3BmyPxQbzd4XEYKws/PTSX04lm1w1Q76mslPNeNaU6trqSvK7INeIm6kUzC9wV5mBWsvPUHUw2uOpVqa0SMIqvvcNXzdylymje7xrgMpIqtvG0q8Ut0pXUq3omp0BZKtcwNXcISo6aVzfGCUk3dO9ElLlBPg7o4YO/nu1g2kLm2P6ZhFGkLeqWqx4ZcUlh0AeZJJOjl7Ers9aFRSmCg2axrMTl00K2vdOhBvO6u+6ModTptgg1NoJ3EdaDu7cGm2m3aStdBsrcmwvVFvEk3a3eIKcw4yFXQz1RuLaLm3raGfSLQbhEctyc9PvV4KmdpX273S9XXzrfVKnW2tRjQM0vkMIT2++HMEHrHr1MLNbZLa3VM62VEl9haSChDBJfiHO6X1yLcKxG1YJXQVaTr8gIWiNgb9rROnDVmTW3asKgeizxqmIqpRspIwizx3LJsfT539c0MLRc+fdjGS3ZWeW4xVeJ2sSLOnSOAbs1Lx/WZ9bwzesL321Qn9dTlawSbHYULuqV2ZHda51vtchlSNDWv9rFamk0fUYS82uNtQ7l7RCCWfBik65nJaJmEHabWzDzNy6vbytlJWq3raSIMM39xdfidFBRnrkY1LfXKfA6CATWyq8wVSLm3rCQSBQU/UXPP1M/7BXCKil3pZXqVPbhZ8xbktWhTdFdJM8e6rOO4pS2PbIJrQN9Ef51ud17ZFL6Vu8Gg9xkuXJXOkBPjOvgBtgCSu1YS3rvMo2GoVR1d2dptTZ6oHXLQPb9HapRSd1Ef5MvcEk1szi5wOsVrer8411htdI4ZM51mMFti5tjJ3CROomrcurWjh1miLjzcsyFHakdJ2HYkL1wqPsUCviN966ZxuSerpg4OlOk7pbLeLrCMQG5ss842pKlnm4wElzpWlT04U7TY4sbWculmuY4xp0wWg8NH2bIrrj6mC13D+WrYz1iVTWTY2he2PaM8p9vQtqc6uCeXvL6RpU4ynXPAMxbNpk2h5u6udzdrzrKBW0pxWhwK7tCJRBi0M28n106HzviuNUE3PRRaFakzExGD27FGmMaucFgt1D5Ak3CtuwzBqN7p1CM8IWeRr+1Oq11ZbjUPKZIbU+82IXOll4wjs+upU6+ON4SmWvEoaacByWUr6maLK2R78TxgMjP3xKvCSmG6F5KjpwnbNV9Kq86qpUotWW/WMooKNcvLMOBE9FBz9kw2HdzyxII778kEu3J7SUPrnRjiEUvsi6Q+bXD2kpeWWpfq3lxy+O5W4g5AJRB61o5aNJQ37QNWF/iC3BRqtrjZxGq1gGF7VjKi2rHJcgPOWjKNe78Djn1Y3qoUE4zd2ibEa+kJ0yMzEzhXTB0dQxRF3iwIBzWAkLRX2u2bhdAIbXdjyjNt0uiVau0Ql4i9mKSHI85zS81e4YK09I5IEyNNBVBekFg7crdTo3F0s9l18lXy1YET1C19OcmYtqJPMHQcVRYtXqsN2rxy8XYRA3mQaMmsWjcuuVumYRspKMMy2JmHpWp3MNolEkans6zbZTozSxAdUFkztHhIjXUmR2Wib6b8Od7jIqvrlwPr1oh0mk3NhOAOZ2MQbqocKCZl6Y1dbLzOb9axIHKWFsWX/DC3vaPanvk1ml9jNzwNt3JP+N7yyJrEftOm9lkJ1wpCq1dV0ykeKdpDvrZX0rWNwDWjDhsfNzfLQ7tYa4yI4WF62sOSDI6Cs+vo5VmpJBINp7F4wjrZjJyNZpwTadCum0RcOjrDKcctd72ILltRINMPFJ9epK0nhY14ZPnFalOeUp4X7P1+3TbcDiSFMPfnC/JMMmskTxR9seGGaW0iuLyYBmHTHE9OB9Y9zzarzHfnpMdNQ922rCV3wiigJzTCTIMuoyOnOclRRaeLy47Uqk5QV3uPkIvCmOFEvqowJjgTAdaRjKecwm3FKH7oETtXzAiB3x4PZ8TVY06Qd725Fgnj2ObIYXeMXSyZN9YuP5QRvyynx5QJT1Vo7I92KdNYyJnQVeaZ9PWtx853WM2LJ8cMl4PLH4/AduO4Mur9YWqi9SWT3c2eFMnw3FbxlJ0d2H7PT0ViduwDqZSqYZsLpBv7cU7BJAm20C9NfIXhY3kx7KZYgHOuvK9PYLc452gx3/ukbCg+qG39ECXLikUs0pjeuEI00sDy6Rw3uGBXYKu6013eqYYEsCR1K4aM5zHV6SRZ6OY5P1sC0zYN0T9I4SId8DiXbjpBnLXW8QXrxBJwx3QVRXu2wY1p3qt4K0coeZAX/Gbl4uHZSpV548oo7B7n86ubLCJKTyN67aISs2v34RXHb9mBZLEp2MzojbPw/SuTTlXO69YXVtfcsl3TZzm6elIJNm67snXKlM/HRKRPt7llRJftpgrmcyRk2S2iC4v2dnKSjbzz90JI7mY8xxWbWbLcIaZ26E6y4ixbdS8cYBu3CPvEVEyb2FMqw5s32JbfphsLZVYGLzgH2U+QdVKDbCPt+GGp7BNNNQ8SdsoAFnhGtuYVyT+rUq7PVdvUq9OuyBZ6ja3P3rkNC4/TiKnBr8N0I+6KqUXGpHyWFqs9hqvDYOObS4ayyILvlyginM6+a+0rY01fcN3uW7HcUkYTZAKYF5wd0NYWJAsOnWGzxRpn5My5wq1EyJrUNV/IRx+d9wd1vp4hJLk6yUOs5Je2VvBjZS1x6iK7h7i/+IRIUu5pSTgpuc9Lj+lmKUZZKIGyVxen3CHneg0Q/T73ToTtzaRuC1qaqwpXm5/cjWn1sEksjmiLKdHai8+3RQDrZ+wL8QKP4msgpw124JzSbQo5m9cgR6dMIch1TJX90owiveqLINouWo/ZwNIgrfdKszvM/G3I9tMI9mCUQC7J+TFUK2V11HxxebqU7vLA2crhku8bY2NHp3kdFVEl46fLsRd3Fq8EnEXj7Y6y5qa0nZ5FgC26XXHJQp91wll1aRF+u2K4VltV9sanawzUVHse9tspqi1wiumO4WAhBEfaXEbPq7pR2NsmuxamxcaCbV+q89qtcEmChV/ujp5DN1P2RArFNSNMQrFgr+4zZq1iIBx4yVsnFqwDBCTFAzIgLDhV52HlcWdifZ4SFxY5UG190f2piHNRwIT7mTAlMEmJ6IsenY8MWLD7S7Dyt8NlsCR6GboO2B7VW1PTm5StDWkeJD66C+mVvWC84wlEyQUhKJ4g2XohN5hGa9rc0iRKZLAbTl9qcnmkdnRq4idmX86Sm1sKl5SklsqO4QBu77LAxE2ktBjYlwnHy3Tp7j2WrVA8mHMLQ7py5H4728Tn7Q5ZZuqxqBVSPbf2diBFnvMz/+SvdihgKu68JmI5oasbCFB6yIpGCuyA5/Mbf6FktrgWh2hhsbJuMzf7Avv9w0ILQy4y05Q5KqDXp7btR1aQREf6pqBJfO5NUUO9dQRN93tV3C0qTyn9rMQvwtUjBtS/FZ499azpBqGuV/RIsnaoo0wsOnEKmGPFzFd7dOV2UROqyRJj6ivaL2uB9YbOzx38cnGBPUVdbI6XNljlx1uxCm4aSRI8FTlSx7KXm1lbM0FH4BVWLo8bItlvSYujC9j4p1uiXs3DEI12Dc9tLQ9A57orQ6gULIQ9FViEIj9394Kx6uH+r1c8XAYhO1VPTINbzVynj7WqFWwgY2k1M8zbIr3V08aG3ay2OqrsLeSoctH4O6FlLjR+Udg41viQXeH8usZv8U7hbmWTUMuUAfPcWhJhkt+EGz2XjUSmgM9f+ow44pdVuLS6oZsb/hbkp1xq4F4kCkvxCgrQX4ubxAHNIpPV9NiEvYZhq0gqABMCtQv0lZCHvSpd4jpy+nDh9NAyfiWQF67PrB6vyby9BVY6d4+0h7IZ24jD4LY60zfUypAi1/JRekeEBVofkuOZEBh3q9Rnzi5vgF+oXs/Kty73OcQYOgO9rsvFoEZXd7BvOr84UWKNFmbkbhhHARYRH2CbPNvd+rjdtLZxO86IWpnySLtsqBttd0cujEwaGN56gYTzaJrt5jMOdLCdUSLHOyPTzbJo611M1FlH47TUmOFMw66Kg0f+fIVMLUKey8lli8SbujtcThEH1sN8jV65zZav0LPMsIgGMzR2YCO8RkMWC2eZDelSRA5ZKcZxznn5Jb0yyGUZ7FDPttorvqqPS63JuinKzBq89jWmOWt53XoJX+PA5Fe7WzONWe9Y7fZJlVOSSgSzlt8YoY+3w8EKffri6kwTYgjmKKwnVAcX1abO1CAJdhHPotXesLG1QQzGRV2xrNKeJLg9Zs1c3cLSbJM7BW3P+2KXO7DgBPxqKNwWLbc60WTeoqIz1qFufEXhLRm38xW4bGKhG/og6+T5THF8h9xI2GUzrDpgL5a1MWxpfxAGF/L+cAlQ2ZZyxS30emqW0g5xWrhdwSNqbrIBXWf9asuGhdz7W3QpmZ6unIQ1vs1pDWHtlaXkJtBDt2ZY1S7KsHPKWtqSODCcKrT31GJuTMs6UdMTy7I///zy6WU8bX6eGf+bT4DHc7z/Z8eJj5O/t+dG9+Ni4IVf7mt9+XcV+vXTSx2kUJ3HcSmMjPh5vPh3h6Wf//WzhnHu8HigOj7aurZvh+qtF4+/A3pJi7Br2nr41pRZdz+s/fTid834s4Tm2/NQ+uVuUF6NJ9w/GDAexd6P/L+15bfHo9+X8ZcD4yMbEKZeC56X8fP8+NNLOEDXpEHzjaDIb6CuRkufDzDGg9fxCcbLH/8XbPahtm8lAAA= -->
