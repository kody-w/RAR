---
name: "rar-cowork-cookbook-dashboard-balance-supply-and-demand"
description: "Produces a self-contained interactive HTML dashboard for balance supply and demand - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_balance_supply_and_demand", "rar_sha256": "c24a9d8fa9c9e7173f3b1543d9fb0e8706dde86e509092de9d27001c9ff2fe3e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_balance_supply_and_demand`. The original RAPP
agent is preserved byte-for-byte in `dashboard_balance_supply_and_demand_agent.py` and in the RCI capsule.

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

Balance supply and demand Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for balance supply and demand - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-balance-supply-and-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_balance_supply_and_demand_agent.py` and embedded as the fenced Python below (sha256 c24a9d8fa9c9e717…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_balance_supply_and_demand_agent.py` first:

```bash
python3 dashboard_balance_supply_and_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_balance_supply_and_demand_agent.py   # or on stdin
python3 dashboard_balance_supply_and_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Balance supply and demand Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for balance supply and demand - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-balance-supply-and-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_balance_supply_and_demand',
    "version": '2.0.0',
    "display_name": 'Balance supply and demand Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for balance supply and demand - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-balance-supply-and-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-balance-supply-and-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17357488517070fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/balance-supply-and-demand'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-balance-supply-and-demand', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardBalanceSupplyAndDemand(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardBalanceSupplyAndDemand'
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
    print(DashboardBalanceSupplyAndDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZei2LrmX+HG/ZBZl8xQRiXPqrUaFQVEUQREKmtlMWwGGWWDCNX133ujRmTVqVP3nurVH9pckSHw7nd43nFv4tcXp6mjonr58nIATo6tnDSNI1BhTu5j86ItqgT9KhIX/WBekddV7DZ1UcGXTy8+gF4Vl3Vc5Gj5rir8xgMQczAI0uDzQOzEOfCxOK9B5Xh1fAWYqG8UzHdg5BZO5WNBUWGukzq5BzDYlGXa3QX7IBt+fcaKEuQQMUB3O8ytihaC6hOWF9iCYhnM8ZA8iOUA+EiM22F1BLBrDFpQvSL9wM3JyhTAly8//fzpJUbfX778+uKlDkS3XhZvSswe8g938XzuL+7C0Xp0O0SEZYcAytF1CSqkb4Zu+SDAnlcfB2M/Yf/1X0nrVCH84cvXHHt+vr4M/7Qmv+tVFw6skZqeUzpunMZ194rxaet0EKtA3VT5HTmEbx6+PlZ+51SU2I/Ds48PIa8hqD9+fUHgVM6A/teXHzAE5NeXqhm+vw5cyo8/vKYFQuLjD9/5wMY9A68emCGtX789r59sEeF30ji4S/0RcX342QVfX35n3PB56D3YiVa+vJ6LOP/4YFxWxRXkA6wff/grtl4EvCSNYf1v8f3pwTgCjo9seir+w6c7yD9j+NOgd55/LbZEbv07liDyN3GfsCdQf8X7jv8/sU5RDsB3xP8lu3+1AP8R++kvbfvvFnzCgq8vC5CibKscNwVfsF+/HXbC/KcP/vebH37+DbH+H9kciqby7hy+oZyIAwDrb99++gDvtz/8/NOHpkSxBpzsW1Ol/4rnv8L1LucPCD6pPv5xLZJv5EletDn2HunYr0X5H9Vvr5jppLH//T78gv0+X4YPjg1GvAl9QPC7nIFI19/h+MPLb6hE5Miaxrs/Rln+n/+JbWKvKmAR1NjBK5oaQw6u4wwMyutRjCoTvOd2BRCuMEbAPulQ/A8eHjQuAuyX/+XdKymqiY9KOnqvgN+e1e/bo/p9Q5Xn26P6/fKK6Yh1UcVhnDsppvG73dfcCUFeD2LLCqBaeL3XvRp8RqXo8/BlqJW//Bvcv90ZvZbdL/eCGz9qlDaXhvoEmxS8DjYeI5A/LfJQcwA34DVIRlp4SKEgRrX1E7IdFimq7PWAB0ziNMX8uELGF9WjmCPMvgzMfvnlFxcp9jV/FFQKe3QPOEIE7+pgnz8jy4I0DqP6aw68qMA+/PrbB+x/Y//dqjvzQcYO1fanR5CG8kHdYijDmgyRDW0EFWDHv3vk19+e+CI2OWp3yH9xEIPHYhShCfDfwD6I/GeSYTEXIJARwFlZVDWq0lhcv2JSgL3ri4QOj4Y6HhWwRl0MdS8f5N7QmBxkzjuSeVFjEIUhDLpPWAPBXeovbuXcVcxQqjv1L9hmvkNdo0jRf4OadyK0uMhjBP97KDzuIybVB4jN3li8YtshJrHSqZwyqpynjMB5+AV1i7fliLmDWmj7NR86JBiguifIAx5EhJDxni79PPgcjQHZEELwTfadxhl6m37vcdXXHD6D36kGV3ioGSChYRP7QzT+4xlSMCqa1L/jhzS99+6HF/ynV+4xOPvL8UD657nivaVjXxtyTNDY/2czyWAOv1ppworXhQUmbHXt9IB5UGxwx2MYQ7PBXYt7Sn2fF96qzVvR/ZqnMYqZqvvHg/LunCfNo5A1FdJB4zXszfDqzvceuEMgVtUQ8s7X/K26f0JI3UsZ8h3KcpQFQ/C9CRyevmkaIbyG6++d/u5ohB9CCQUnVjZuigInQEC4jpcgraoh+Z6eQVEMhkRso9iL/mAVhrijYEH8MaREjNIJdYA7dNsCmYnyLqiK7Dt5PMxP5cPRPoZGV/CKHVH+DDEEUdKiIWigQSh8uLPCMoAwRiq+Iwwjp3woM0y7TwWdwRdFhsL69x54Pvwe8XddBvURV8d3aoRlOxRhH9wenn3X8+krpGw25Oh90R/d/bQV+30b+sfX/K7je91HqZ8OHfx34GAolDN4D9KhckFUfTLwDCAUCfdm/frot4+G/q7Llz+N+B//3i7g3kGNP3ruCxbVdQm/jEaPrvfW9F5R3RihGIlLAL83wM/PVPv8SLXPSOLnR6r9gfUDqS/Y31PvDyyecf0FI17Hr+PhkRJ7YAjc5wehMf88O32mh6dfcw18d/MzFobCi8oByuq3LvRGglpRWIFwIH50JTg0sxb1z3sZRo74mr+HwjNRUJXPw6GFwuJ3CXxvx8ixD7+9dwv0KK+RbH8Y4UIw7G/SQX0IXr7kTZp+esmdDPxb+5qhJ6BwRXAM+yGUOmgmqmNwv3qfj4aLP27w7kmFqoFffBly6xM2zLKfsPex9BP2tlG4b77yBu2UfhpG4kEkIkW/3mnfd48ueEF7s7orB9Ufu59hEntOyH9WYkgppPG9xg6d65mjg8Q/MUFfwhBUf2ai3r846bNQwNoZunZcv6U3RHr6aAb6hCHnobRDmYSga9CCP4tBcipwaVB79Adzv+P33aziYctvdxjqxxby15e3gvH0wXNcROQoMz/DoUGOUKAigej6EVLo2f/NIPlkgaocmmIQD4+kHc6fBg7ncWBCTKiAcgmGpnwucMdgOhmzvg+mLGDG3JgjfcD55GQ8JjwuCMgAUADxe8Tmt2EQiAe1SMfxpt6EoH1u4rAeoMYu5QGCJPwJBcYMRwXTKaCB/31pgkrk09aHbQOQ7zPtgMnT5F9fXJZGlCINJf7xmY8402HJiatFLl6x4GRbI8mNDZY9mvparpeW58t8r5WnFaDWy26mdpo4rvdGhK/2fnVYhToj5JPZDtZTZjPppKQkk7g9kqF5VXI56e3pJFW5qb0O4/nY9bqEyuJoTSpSDaXM8WLzeGW5w/pqzjP9kE7LqU+6KYcrJbduTvFOMXc9zpKj2D/mBzVdHg+rpVmXYSZf8KRPjQsnziIyZrxsqQg+TtNLx943J4PfbUmpWeiWWRp6ol1vnNSMgthMwisJO9lcQ4OcCr65jg9NXaWGfU5csWfwINfpUZDvWFPucJDvSKM7g5N8NtD2KbWXZK2vs2oB6n3l7s34cEuqxZaNKk4yU+p0SbVu55Vja1N2Uy7aWmq02ZqbtjDYS1Ps5/bUz4tzSnRHmVieCmu5P1jlwVXOIg8RAGQGZ2uTvYzJZh9vpklqohGSOjGrVU9YcGZxlq1nh8aEl6WUoul0ERk2bUFg63A/3xZR6oWZL22WjLwAjJCdoir12OOR9LXxrGsOos2HVTGv8MZjzjD1RGZ6MU/pyvV1z5YPhEFzrB2XRmHGEWfBSE4XIBDW55215QNRnGxCaDqtq5eXxbG2YD53st36YNrbJJioxxSUbm44xzl0F1NuX+7NcpELt1Q2AguKF3DJAzVhCZw6p3svpHR14sOGGwQ0fkPOSPRAaGCSHu2MyxHqUbaZxO1ZmPhlp61O7HWixbbvrm8tnLp40Rnu3BHUYApNM5ETeiOOLCHbwNOIzhZeZ/ZT7eY623gn79k82WwV0dvAUieFXuQgThaZmZomuc01w5MUYTJt9E3PzmeraE4edyQ8OPjl4DTo5wTV8sBecHsFkiwIaSYoDgHf726bXbsPQl7iRpW2XG3wHG9vm3xMMnhmkXLrr08sQ1WUM1HYKFUs+WI06/xq6FKeeGl2kQ1SJQWPVBYnyd7fzgal8Bd+zOe3hXxobMU+BK0+53asfk503GuaRb7TDwaMrtL6yPp8aUnytj3xV0IwtlriaGAtN7Nck/Zrt1rNJ6e5Mzcid5luDaYtskWsXXeMWUb+rtt6U3I8Naj8PD1PJErB4/XMYHbtjTuvp7KRbxhSV5g8u7i2KOu+DqdG0Db2Mc1li9tduTzeEgXrrA/LXUc3q/5oUnIJgzJerLtCOKzcTr7AMlF3Mil5xM0W68VpXshCw/FtQIzNZc4pqr1abwq2FKRofxGmgniV2xoSTqllPBl0U60iGLYpVoG/ks7iwj7Y+goA1jj0SxxNwDuRvRBlajHugUa4bdfrM81Cq/aY/LzXD9cjSVyOXeJdrqyo98TFa4F08fb0KmKmArVcb0Xo7lnvhKBdZ4Eh5eT2sDdGI2kpJwXhXVx2yUjLztwcZVd3lZzGrxrTT+MVqmo8Yc9Fqw7LmDwatF9GaqIHsmxoSq5ntueQfTrjSSU4xvOcYL2jPQe23yjh2Zlsgn5LHmu5Jk/ZbVQSs/Syxq1VM1KdfpYLfcnavp1rN7Hh6wovoMElkCpltqf5IABNMMJJkRavgAqK0LsuxOrcllK7J/tC2ZoxZzO3hJUswNBTg9MSVQ6BirKJPy6Oq26xO15XRh/LK10YibXerl1PkHK5sSQQ5LHuhcIlzmNLjXMZTsnNdO85M+cgeLOoOxsHxp/yZ/pkwllkq9qZlw5JIjj+VtpeyEzxllS90qMU52+TQ1ydzZUT8aRBdtKszyZz2tslvFJcRpux0TuJvRqp8yu+BSPG3SehD7kp5Fd9OQXXwt40V41aZnS8YVlOpJQxo1oMGSTJuVVWG6KvKuZEyLIWW0Hmd9DvdBgfIMsthX436pc81BpAT/wojNU88YNgZxUdi49GTRUVLdiJcXsQuwg3fD5WLtzUpJYSvxYkjRHXY9Wx+3UbF9uDEhmTy4LnKXJsmeflnJq7oXSElLBmZvZ53aMBqHUScOK8vXkwtup4WazyvcqXkrtY+LTCXhaHDGaby2JPjvUO9vYxDlB91Xg/mcw7V+Dt7cWJzTiUNyrj0WfVG0mCboo+HmT5kthsNIOYHYXpitj7O4Kp5wkbVmeHIM1echJzoeIlJyxufCIZs4ljqZtzlfV6POunN7YXzOV5tTpnwmiEN6gHM+6qjjzqNM09EqRetw8JaWzOLlWEckShGhxlakNrhZFVNZdP7E0b2eAWS6SoaLdTZJgNsLxySZz0VubatF3w5kI5kvjtEh4KhQ3NbG1PLoKo7YTc2U1csjbdMISxUoyXB7wZe4amHmQerqrMiTi8ClNh01iV3FyOZXzgJb4GUiuBWTM1lPE+Y/ubDaxMAsW2M9VwE+0O00u6rW/L5cI7TQSwl4p57ODIuTVztda2clhqaybmOxzlSn+j2Ql3lo8w3uZLGGqaRAaTzU2dHVh+NOs6N4L7dE3gmyMFb5F1KR2ntE1JOR1ZtTKYFd0DothKyn7lcOl+Z3pXzxtFS9oqL71Qj/Qik9kNodTC0jbpecDaa/3g9+0t5Nw9HJ+6VlaB5MIVvDmaoRh7w9Hn5/WiCImwEAuX2R3DdjRR3cOOKQ7jsGtBcCFULp6PGLUZa93W2s2MWZMsU8rjUCAR/txNlfVmlff9mKYC0R21HL/fro+lt6avp3GnsLomzuDWi3UrnHruZDHOxo3uXlxLw/tlp6YGqK/NdpPMdV2OZ7u+Mi0QSXy8KfZrYaGXzKTKaiOhV/hYTWQodNIyoWPIBDnD7KX+cJS9yOPH5XY6Zpku6nc0MMpxpBwvS21240w+36zp7oYic86xLNOvKrMrzkpFdhfDITgtP82kdrWRKdmZjp1Zvo22KqPsxSO87uU50dGXfdT1G26Tu2v+hOt8k/DduDbWtGtlOl74Xq2k26vFlsq2m0/jYD4uR/S+X4zH+dIhMxsvZMfmDjelyCxzw+w3oR8sJ0wY8Z2eKee9ttHlfTazTVUztHqciicW+skt9thTqAeNUp2iXhJwdzNV2q47EvoCzUgCVfZdsuan61vhbhQBxUeTyTIqtX2GuHZLO5gc9aDst7PAbKakSO37YnV1KOt0mOWbWzHe1jR78yJzluZK7RSgpgnOMGrxtlqRvq9UGydbC/5onRdZMvJ203JD4eJsxzfrTi6VaH1be1aorReKhvPh3u6BpBk7QjiRRqT15KG9JQGk7HZLzWf69ehOS4mi5PNqMl6IbA3ygqVP0Xw/GkMymLOooKS8Ihs1EKa8ecpXe97J5fkxpGHYMEapLmuHLKJDoe3WK0K5aEZpumDpWOII30YieTuGxfmq+q2wOFOo0Rdn193wWYOv7DXTL66R0Il1VQLiltwkbjIp3ZsRJgtfJlU3tlpKSil1q+fFvvXVSt/PI2GNtunmxvbc42llzMu0v+V7COhbyvTzYGcwvCnszku9PpEXvezBmCxmm9VmqvprOzWK/prjpUkVF6ZmtYkn+irk55N6rNcqxwPuKuhqX64ho+kgOYd2q6CYSc4bJ25mcTymQYrbB2Y/FqC3bduNM4MHaWezCzGuV7bpzE+SVudyyjlqQzTbInEqyBT80gjOzrXT92f1XDKc0y43631onRKXdtUd37K+FvH20rYn5ELblhMx2vXLxWG33swn6zJFap1dVO6zoPAZPNXlnBYt3SJkXZLCxNlcuIte1yxzSCb02NKjkJGsaUbZVKF46+mCo881fqYm57FJmPjRqewzsFyHgl3gtqjtwIBdUlAf0yI78Zpo7Cpqt1343m0VF0m5Jdk2O4uX4/lAOcto2QKd0tJ2e12n3tmjt7cxPBPUhFgx2zwL9trykNiJre3mq3k8wqnTYqwtTK2fri9TK596zcIjqFTgo3qsMmJgNFow9juT8I8zcRzh9ZyCZFMT5xPFjdKr5B+P16jQt5M1iU/CdXsbAb6l+LJfUle3tQp6mvdTjuPw234qmYVjEtcRU47OpexaVJMFdsoFRXpsr80pm1qhch3ztD8T6aYpTZ5pj5RyWlbVNUTl4pSsFot+zeTmjL+1ZCHoYqawvLEHSd4s6AWfBLeTGBFXhdus61wl6dVq5qYTtAncj4F7Ec0DTIxFjqwsKypdbTYytLz5POvnO3a1z/uFu4tifuv2JO2OSmq6i66wCbOTJo2C6bIQdx05mcyvuZtUEJ4d4WDt9jJ+3XJE7rnqLO5aqyW3Mx/NQLJQLyZOrfV1Ndo6o+OIo2la6wqpqXguXJ3CGIwWYxKftc4CUlfSy1oU8BU+vi0rYVZHZm6jLewEt5gqFf3r5rS0arbwby3ljdBeqQx2UCB43prEJsTnTRBtrHk7l45MK+Wnw9VVxlLjnFXGGbnXUphvwz7CrZIkFp6w3nXe1RK8vpZm01Of9ee28GbTJcdn4vWknuVdG3doP+A2KmwbD7TVUcqj7XmjKuAq9yOwmDEMLp5AiBszUtpqOz8IRxvGEARA6zaPZjFTpdQZD0UVdmLhKSx3Uy+XI7PQGiW3Wl2c+wQ/XUJITBdkIHoR00jI+bYK4jyzQ7cH+rQgKe+i4l2uz2aA7Hs0Wl5OE9qtnC3MtsS1uuVUvC+i3lscT/RqRG+sE73ZuvtQ41SXPynL6VJGjRa43S2rPMCSrVAs2+4oWofac5uQ6IjrhevssmoYcnKKW2JxzYsqYldSNd5eZ7ujCPjlrNVqDhRiYFGnROPtw44+cCumBXWy2S3GFjzYvm8o+JmIjsHBLTz3xm/nDQXz6LS7KtsaZ3WuSkdWsPTJSZVnqdK6N9qeXJWIuIg1P1mJE6qtfZvk8DXtQ91Je8vfBKJCuJ7u22c3X5EjbTJNudFuLgVdUCxcMCe45XgnrcRUzCS5aJfbs2l5KFhwG+rg4kerc3m8NpsLzk+6661kl6Ukh0ap0E1wrUo9WQol53qg6Sb9uUcN0FqBatearegR2pQA0lgy8L4LZ6zo5y2/MGxx7ikba7bNJ/my0FjHAXWz71gXcJVq1fkVoaLe0E77GNUil+/g1N/LE1XsaJO4uQJH527P9fz81kbBbIwmpBbvvfPlup6Bs1qu/Ll91RW53V3XfrY7XG2lsefEpKek3Y1IBH1ydXt+QuME8Hg5YK6a4hGslu3JW8fqFzCZKt5IpBV47UAVdELYCTRTekxhQBcCZbUUp+XeOeNrXfV9OKpdiWdGlhKqBk+pdkRxhXSQxmNL2uuQ2xoRLkH1EmyKaTI5u8TJu6r4kTnPoFBVPiulSuXttKBdVEialncJz/M//vjy6WU4nn4eMv+dN8zDod//s7PHxzHh2yun+wEzcPwvd1lf/pZWP396qbwY6fQ4ZYVpEz4PJP/pjPXzv/GuYmDQPV7dDu/HbvXboXzthMPfH73Eud/Auuq+wSJt7ge9n17cBg5/CgG/PQ+0X+6mZeX9dPxN5oB7UQHPgfW3uvj2PEi/v77MgB87NXhehs9zZ7S2Q16KPfiNYplvoCoHU58vP4az2uHtx8tv/wfxmpop+SUAAA== -->
