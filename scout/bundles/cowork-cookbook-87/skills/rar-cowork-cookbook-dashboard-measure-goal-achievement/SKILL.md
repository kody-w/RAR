---
name: "rar-cowork-cookbook-dashboard-measure-goal-achievement"
description: "Produces a self-contained interactive HTML dashboard for measure goal achievement - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_goal_achievement", "rar_sha256": "0f7131ed26678494ac4dfb16ef8b864769e2795f854dca6b2047a1f4f468622f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166ZOjVpbvv8LL+VB2U5UCsYnq6IhBSCDEIrSCcDnKLJdFrGJHHv/v7yIps8rt9vT4xfswqqhMAfee/fzOOZf89cVu6jAvXz6/7IGdIaKdJFEISsTOPITPu7yM4a88duB/xM2zuoycps7L6uXjiwcqt4yKOsozuF0vc69xQYXYSAUS/9O42I4y4CFRVoPSduuoBcjqoCqIZ1ehk9ulh/h5iaTArpoSIEFuJ4jthhFoQQqyGvmE5AXIKrgfSjMgTpl3FSg/IlmOLAiagmshuwrJAPAgF2dA6hAgbQQ6UL5C8UBvp0UCqpfPP/388SWC318+//riJnYFb70s3mRQH+xFyJ37xhzuT+wsgAuLAdong9cFKKG4KbzlAR95Xv0w6voR+dvf4s4ug+rHz18y5Pn58jL+2zXZXa46t6saiunahe1ESVQPrwiXdPZQISWomzK7Gw6aNwteHzu/UcoL5B/jsx8eTF4DUP/w5QUap7RH4395+RGBdvzyUjbj99eRSvHDj69JDi3xw4/f6FSNcwFuPRKDUr9+fV4/ycKF35ZG/p3rPyDVh5sd8OXlO+XGz0PuUU+48+X1kkfZDw/CRZm3ILMzF/zw45+RdUPgxklU1f8juj89CIfA9qBOT8F//Hg38s8I+lToneafsy2gW/+KJnD5G7uPyNNQf0b7bv9/Ip3AFKjeLf4vyf2rDeg/kJ/+VLf/bsNHxP/ysgAJTLbSdhLwGfn1615f8j998L7d/PDzb5D0vyWzz5vSvVP4mtpZ5IOq/vr1pw/V/faHn3/60BQw1oCdfm3K5F/R/Fd2vfP5nQWfq374/V7I/5jFWd5lyHukI7/mxf8pf3tFTnYSed/uV5+R7/Nl/KDIqMQb04cJvsuZCsr6nR1/fPkNQkQGtWnc+2OY5f/xH4gauWVe5X6N7N28qRHo4DpKwSj8IYwgMlX33C4haJRVBA37XAfjf/TwKHHuI7/8p3sHUgiJDyCdvAPg1yf4fR3B7+t34PfLK3KAlPMyCqIM4uKO0/UvmR2MuAi5FiWAUNjeYa8GnyASfRq/jFD5y78n/vVO57UYfrnDfPRAqB0vjehUNQl4HTU0QpA99XFhZQA9cBvIIsldKI8fQWT9CDWv8gTCej1ao4qjJEG8qISq5+Vwpw0t9nkk9ssvvzhQri/ZA04J5FE6qglc8C4O8ukTVMxPoiCsv2TADXPkw6+/fUD+C/nvdt2Jjzx0iOxPf0AJ1/uNhsD8akaNxyIC4df27v749beneSGZDNY66L3Ij8BjM4zPGHhvtt6vuE9TikYcAG0M7ZsWeVlDjEai+hWRfORdXsh0fDSieJhXNeIBWLs8kLljWbKhOu+WzPIaqWAQVv7wEWkqcOf6i1PadxFTmOh2/Qui8jqsGXkCf4xi3hfBzXkWQfO/R8LjPiRSfqiQ+RuJV0QbIxIp7NIuwtJ+8vDth19grXjbDonbsIB2X7KxPt6D454eD/PARdAy7tOln0afwx4ghVjgVW+872vssbId7hWu/JJVz9C3y9EVLiwFkGnQRN5YEP7+DKkqzJvEu9sPSnqv3A8veE+v3GNQ/bPeQPrnnuK9niNfmimGk8j/rn5kVIYTxd1S5A7LBbLUDrvzw8ijXCP1Rx8G+4K7EPeE+tYrvCHNG+B+yZIIRkw5/P2x8u6a55oHiEENPIgaO+RN7/JO9x62YxiW5Rjw9pfsDdk/QkPdYQx6DuY4zIEx9N4Yjk/fJA2hucbrb1X+7mZoPhgYMDSRonESGDY+NIRjuzGUqhxT7+kYGMNgTMMujNzwd1ohkDoMFUgfgUJEMJkg+t9Np+VQTZh1fpmn35ZHY+9UPPzsIbBrBa+IAbNnjKAKpixsgMY10Aof7qSga6GNoYjvFq5Cu3gIMza6TwHt0Rd5CoP6ew88H36L97sso/iQqu3ZNbRlNyKwB/qHZ9/lfPoKCpuOGXrf9Ht3P3VFvi9Bf/+S3WV8B32Y+MlYvb8zDgIjOa3uSDviVgWxJwXPAIKRcC/Ur49a+yjm77J8/kN3/8NfGwDu1fP4e899RsK6LqrPk8mj4r0VvFeIGhMYI1EBqm/F79Mz0z6Nmfbpu0z7HeWHoT4jf02635F4hvVnBH/FXrHxkRK5YIzb5wcag/80P38ix6dfsh345uVnKIyomwxjUr+VoLclsA4FJQjGxY+SVI2VrIPF847B0A9fsvdIeOYJhPgsGOtnlX+Xv/daDP36cNt7qYCPshry9sbuLQDjaJOM4lfg5XPWJMnHl8xOwf9opBkLAoxWaI5xFIKZA9uhOgL3q/fWaLz4/Wh3zykIBl7+eUytj8jYxn5E3jvSj8jbjHCfu7IGDkk/jd3wyBIuhb/e177PjQ54gWNZPRSj6I/BZ2zCns3xH4UYMwpKfIfYsWw9U3Tk+Aci8EsQgPKPRDb3L3byxImqtseSHdVv2V1BOT3YAH1EoNFg1o3lwM4auOGPbCCfElwbWBu9Ud1v9vumVv7Q5be7GerH9PjryxtePH3w7BThcpiYn6qxOk5goEKG8PoRUvDZ/0MP+aQAMQ52MJAE5jM4gQNvStPMjGRJ2yU938Fp4M+cGU0yNAumDEv5M4r0XJt2phjJ2LhP+iQ9o6dTH9J7hObXsQmIRqmmtu3OXAYnPZaxaRcQmEO4AJ/iHkMAjGIJfzYDJDTQ+9YYAuRT1Ydqox3f29nRJE+Nf31xaBKuXJGVxD0+/IQ92YzBOLvQYUsanC1zIjnR8TrY5+JUxxV9KTbidb4Ohj2zA0uZ4JdUfLXTjdqp9tHFF/o2RPMdG19wQo8jOS6m06gzpoGlS9k6ZjyUWTXA3QhHc0fLZlDUIl/utq2oToxjMsiXfViyV7kKgWUp+5mATkpvmE7OxyljXIFEW8wEnXA1U55MYKlSd4M+S2pNTQ6GWbiRteIZdUqelMLL0jqYZgfBiDThogMlSa4ny9w1wVruTwxae6tsqjb1ZVMJvLJSmtTAjXauXA1yecnB5UgDnWBvbHuLCS85eK1zJay2PU/Om47engZgae3JsvGkKbfl1AhTY0ZeoX3mCSrhiWYZeY2K1nEQdrfWJKp1RCWSKx0PYjSIcBZjVGIt9udNaeNnw/Wr3ZaYG3E13MTLYs/Ex6JguP3a40U6kU/XS8Vd6xI3qFWOrXTt2Ast7tnm+bpPqCQw0q1cNFqiV8ptHeFxX9jd1r3eeDRY8i4ZFvtcOGL1tLYcCzTubLFW8CTd3mR+Xk5W3qlL962gUmZZh/srhhHi3j/lmQJuXmLbc/HGsPbMKq9zF1/vrnxjB+hGL/ccKSiOtqPx8GYV5iHcJArdX7PN0GplZ/h2exiWJQdWEdgMJ8kmL5eNPaForjAUQu87Mx1wd8bMsaI5r8osSQgCDbWoNlXzJpLgQveNvzwZdU22fMHwlYULorqenmeX7VTezFRxqLVKWfG3oRULbG1I076eWJfrLHKzfcHgApQnUWbW0Wvn+4nlTrvwfJiV7iESVjKV8KWWu91gTdgbjltDTTP5MGPjquqqWzswG1y0xWjNn1RFnZb0GS1o+3hkNXBoj8Kmb7UpmBzK/WQeTniXOE/a3ne7WU6oc8nIJ522yJb0BM0YeiltLhqt3EofoGtZa2VT04r0dErx9By3i9M+r06HI11FWO86u9VaVO3U0tkdTaD+gk3tBI5l62yuKhhRbDa7DTXgZLPvT7ftIA5h4VAzLm7PkikNC19eJnwQnddgJjc7Yi8N4q7cCWfMolbp6WDgdNV3ZHqJ+rhBl7vA89F4pnbThvaGHVi5MSXRMUXSvYAutf1JAjGfLWb4YF+bhbMWb/2c4Slhb7gXH5tOcDZfWTtMOmb0xKGDxaYu28v67B9I8XDZSpcpHp201TZ13YMWk07Qq3bcLdT93KPDHHWuV0sHhttrlbXeuefdnDnJJCcyxLxIJUJeX7lhUvZ8ZWZXNLS82AolVwtFWozQ2THM0pI6AKwUaBu/JsQNuCSPFoUzX+0wq03Dtd4F25q4eHue2kizYr2pp6HH53q2XwRHgciBf4znm7ihYitT0irUJ+f9taJnvuo3hDJQa6VYdqyD7mQ3cE0jyWu8JX2RZOsiXem6wmsFL+y0Cs5+heKgXZft10UVNBJVrju11kThkoY2zSRVTrFOnWKhLjU43m1rOdUplMWkwfHSdeMPWmfZke/3bXvb1qR6bnzutjybmr7cxBus5VtrfdDEytaIVez7wSyftGjdhBPAibrBU0SnGhs6DqqFs9EDMV2Qw2GhpMeQGXb5TVm0YI+6VqCB+ekSrfqLYLDUgldidr1j2QOxWF9sD6a+06wyikzw6npSc4Jxlgf8ZDkbIG3mXFXw62CLxhrWbLPt0g84/KyWPSaRa+4YS5f9UrJTBWi1bfrL9YJT1HVo4Gtzuec21+Ka19Dpmdc4W+4kYV3pq/xUiPbtqTuVYUusdJ+PZRtXSo1TKGNV4mlxq5vMNoR96mF4HRMKxuhmibESJQSGWkjZymR6er+/rIvJUTZtZhmTS8HCaCE9ryZszolLQnf9hgt2wqDqzGKiVBHpzshJtthRk4niG3My9ATFY+xkx17FXuHW2Hq3XsgYcM+K1AUpZUpFRZ+5ViUI1TkGNw6bJxhfbsxKEPNmdzhtDsde37c8aLawpKS1EzH9gdwM5swD4Wa7ZvPCyG9FJW2DFW5f6Vhg4xPEKkMPGC1tNweBjdx+sT/FRpCyxZpb5irV3NxI8Pa9cAxluVsF6HWxQ1uNMrR0SoP6kLqqWWpbopb9k6NywrCQ+1RJdztMS5u+j93iYF0MzD+LkrVmLMHXCSJ15ksVZCRLFefrhjqV2XWuUnI4r/e4UWwmHluiVrWol3tNufr+she3tSQ6DTeIN+vA3aJ8IUzrxlE21aFeM+ciEPDrLK8ofDM5roStflhLLCw66W0+ry71dOKQB7CMpa3RJYKSEtt6vvSkcNudG0ZemXTDL2KZPFbJvjDiQXIDbigX0qVSsyoBlSQRluNMZ+HiyodGHgdHidYaerBPUTWbX62mr+ftsF6XlDNjiQQ/5aeaO62CVFoos9TwGmVhOsDiE/KQYBV1XSd4fZndjs5ZRYu6ULnpemBt2FY40+p6Kwp7X9hJfJPSfn6i3QizUgczgmVubhj8KucUemaHahUXiUxbyWSX9xqthpKvJqsTwx/P1rDanm/UodOkW+kJM2OZbZbelAfbetmcIijoMthiybBbdKdFvF5nzIHzvZtWHGbY2j5b580EIyZUEE1CvSmpQVsp8+NQxwJ+gz3sfnGoNxa+2J1OJ25y6BmaaZqDN6HsTl5LF5h6DaezlThzl7uOmcBMwidyagw3dhYryRTNTrdV3rsHCI1sw2ZFFK4xWw1WMks3pC7yy+4k8d0WaI0x7S7hWgsnrjAkxtKKEnK2r2lUvzRJn/qq5odOJx+2V3zTGEmZbXVJtbdJictyRM4Kt9NXjRMcC/zcguK66zsKRDlvs941SXk0vmGcB10h91Th7g9Sn3ZNOl1uV0ujiQ8ysSiKSJFUh90eDFLIeG6lhcY+Nqh9zNFUvZ4s5+g+Hqb4lTkmGbmztzoFjpOqs/qYzAQbJSujMx3lGiyyk2DJu2nYSIm8KG+nvTxVpXS9xzI3HXpMIRiM5pqrY8uBX8ibHXFmJFdMrB0dku4p3S2M7RWIR1XHrzsT218uDd6328yyjvyNvexhEMjYsfCMOBHLhFeyJU5eGQGrmsk+rXh0eV0REufxmw5MyhLtragINhrsF1bnXrBJmL8YARPwvG7xnbU4ejdUrmOMJk6DIDNLBj1BjxtsfZtVa18MRNQ7Eu5NPUba9Zhni/lRkbYbzQoNhrrIc/J60U7yflpeC9VbTh2XFJmQz6e+hq4xh47DzKPnNVk3TEGft5dFePKOFKeVzL6St+m2oCWN5rLtJqo4zOb5et4d53pcn0TzVhiGIs/PQz7rwuLExCcNGOV1glNT9kCe+GPfDDHBVaqnVqFaL5zzQYewWjPC/qSkK48vYrUljAFO7tGO8Kuk7Xn1rE2zM9Uo7MVeNnSnGCBczDG6Xm/lZVBM5NPxKvSXbXDuhtTUake43OBYIJ8PFJqd+TZg3IZtOWK9yTzmYAdSd751FJWbnnsD0OGmdxVbB5UW5i7bHrZqxcwl+tbNxFaZTRVtLzONtDTPMS2lnHPUr6dsLkhBXtWbLL3i52POdaEVoiLXncVC4mbmWTV5stROgSGLjjDkbmrmtd5a/fxKNldujq9w7DpTiNUlYMTW8OYHLpHwXlLcs2l0rq/n2J7ljWim9G26DC890e/5wQxF6xSchokj9tRE9rcusUHjnKBW5oHAdwdZzqOFiAN8bUwEV9n7M14miHxzEdiMqc7LDA7PcxTd4ZOdMulpxaZ9BT/Uro4bUc1Ul2rW8EppoqLHdGQTRjXhVFuRJ+pLRxyNxfa4x2CVMZjD5bRwijqZWwIGDpNd0sHuNPFqd4r3WAXHNxMXKS0rQRDZFwn2yBFYSkdhgk7PCzzk7KKeSddh6neoy7EnolhyPFN5wwYt3MHPGay90hUPigVrCx1VeSud61tmryiueaanQjhjqtK5FVypzFlZvwDeV01wq+dN2w8LfTAhKIoHNDC4kyG2kzJD5SxhD4CmqMzEh9C4ySzFOzQIxNkW0zBBTyla8LdoAqbuOXHB9DjJTV3KgyXRojthO+O4osco8iCmK2wVq05MRDl1maUe7inD7cAz3tCmIOrE6WXPeLR46VwO1HiuZK4cMAkLZgV1E86Col4sbhjQSyurBzMJYJ8+m9PuTqUDvfMxc+Fbu61hgB0g+EXHOLLTxgoaN9vpfqpJAYmh27OHDnrRcJ23WCelGqJ2ZB9RUGnWCqXsy8QwrUhHa5/t+nPC7BT/uFM4bWdxM2ayP9OrutzcAGpFzrzEp9XqsjxVnVbKsHSVsLIlvUPtCOcWcBHb4otmkzIJsyp9xWKDNA+4iWe3GXZes31Fm0tDNzdrAV+W0wvLw+EFb4y2oz0p2LqpqCeD1ZzN3eYyy5SkX6nMnvNF42b11FKfzxIcduytv7nNN+eExTfH1vWKniUX/bZaOzt7KrlmvT+sqIJhe3IWbfSzb3N0vCwUT6+9isd0ZZEHN2EXxPb8Wg/WWdfmobrtTldiNsmPa1y8SXt9MpttqixfVDKqE27tqCxBTW/z8qK1FD2Y55RKa+GCBcyajR1l5Wd7caaVydKHbFNpYi4Bo5UZMA5+s+w9PpN1pdvuJtUZ7UlS7MOAmTHuLq1WnJWZTks1U693brixcifcxog6R76Ul6QRJgeaOk1PG1bDPAIwp3Lb4UpTVNkca0M9ZwA/V7kZJyjTsBza7RQtm16C7U3lk7vBVHLckWb+KpfIdHDo3GQ1h1enKdHdzIizV157vvCdDwzGYZKM8RU0RSUm6UyzkW9bcyCpSa2EVLFiN6XQZnIP2zDGJDc9O/jHZr4OPRR29AJhnNk2YvScRSN0Es+XOmViSs2mOLs5Kn2ixytjKeeBoCe7ledYl4lcOfOrVqwua7tpQDPjS7qdWqhYtLG5YMjGb8vCjIVl0VuNvqU8e00eT0RftkJW0QRLoEdXM0M+vGYYwDb69hKgQQeCfHsachlVVH3L1IOwz2tScMMMZj3O2Eyc5T0u9RI/zDEf36KXHueyivRX/dYUqoMeOa26UjlFC2QSJLwx5TYOZh2pg391jpkWqKSbLGMYoftpgMX6vrye6l03gyXehU0ByxjkbYMuWpNY8ubcIvbZwo+oXK/cNKGJqF8QG6UZ8JzyvYrau+7CFfuWD9awiEiWB65oXom5n5vK9AD0g3/jgIMN5CrjNCK2tZXFY1d1LUyXS2VxSEgzUG7XWFnDoW2GoxlQ8jPjYj0hSPTKvqwHGr/E/oQDElEf0I285biXjy/jifTzXPkvvFAez/n+vx03Pk4G394x3Y+Uge19vvP6/FeE+vnjS+lGUKTHsWqVNMHzCPKfDlU//ft3E+P+4fGednwd1tdvh/C1HYx/avQSwWmyqsvha5Unzf1g9+OL01TjXz1UX58H2C93xdLifhr+xnI0el4C167qr3X+9Xlwfn9ZmQIvsmvwvAye58xw7wBdFLnVV4KmvoKyGDV9vuwYD2fHtx0vv/1fmoPjReMlAAA= -->
