---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-portals"
description: "Produces a self-contained interactive HTML dashboard for configure and manage portals - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_portals", "rar_sha256": "2d8b49d94ab1fab6cdf97d550ad743e8ed56d1e72f3632f677ddd3db39f97ca5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_configure_and_manage_portals`. The original RAPP
agent is preserved byte-for-byte in `dashboard_configure_and_manage_portals_agent.py` and in the RCI capsule.

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

Configure and manage portals Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure and manage portals - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-portals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_and_manage_portals_agent.py` and embedded as the fenced Python below (sha256 2d8b49d94ab1fab6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_and_manage_portals_agent.py` first:

```bash
python3 dashboard_configure_and_manage_portals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_and_manage_portals_agent.py   # or on stdin
python3 dashboard_configure_and_manage_portals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage portals Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure and manage portals - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-portals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_and_manage_portals',
    "version": '2.0.1',
    "display_name": 'Configure and manage portals Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for configure and manage portals - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-configure-and-manage-portals',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-and-manage-portals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9bc5455755650843',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-portals'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-and-manage-portals', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardConfigureAndManagePortals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureAndManagePortals'
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
    print(DashboardConfigureAndManagePortals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjWJLtX+HFfMisUWYAQoCUbWU2CBCbWMQmQWVZFjtIbGKRBPXqv7+LpIis6uru1zU2H0ZpGSGJiy/H3Y/7vcSvL17fpVXz8uXFiLwS4rw8z9KogbwyhOjqWjUn8Ks6+eA/FFRl12R+31VN+/LpJYzaoMnqLqtKcLvWVGEfRC3kQW2Ux5+nxV5WRiGUlV3UeEGXXSKIN+UtFHpt6ldeE0Jx1UxS4yzpm+ius/BKL4mgumo6L2+hz1BVR2ULZICrA+Q31bWNmk9QWUEMRuCQFwCVLVRGUQg0+QPUpRF0yaJr1LwCE6ObV9R51L58+ennTy8ZeP/y5deXIPda8NUL82YH/WYCVYby3QDtoR+IyL0yAWvrAcBUgs911ACrC/BVGMXQ89PHyeVP0H/+5+nqNUn7w5evJfR8fX2Z/ul9eTetq7y2A5YGXu35WZ51wytE5VdvaKEm6vqmvOMHUC6T18ed3yVVNfTjdO3jQ8lrEnUfv74AfBpvisHXlx8gAOfXl6af3r9OUuqPP7zmFQDj4w/f5bS9f4yCbhIGrH799vz8FAsWfl+axXetPwKpj2j70deX3zk3vR52T36CO19ej1VWfnwIrpvqEpVeGUQff/hnYoM0Ck551nb/ltyfHoLTyAuBT0/Df/h0B/lnaPZ06F3mP1dbg7D+FU/A8jd1n6AnUP9M9h3/vxOdg0po3xH/h+L+0Q2zH6Gf/qlv/+qGT1D89YWJclBzjefn0Rfo12+GxtI/fQi/f/nh59+A6P+vGKPqm+Au4RuoziyO2u7bt58+tPevP/z804e+BrkWecW3vsn/kcx/hOtdzx8QfK76+Md7gX6rPJXVtYTeMx36tar/T/PbK2R7eRZ+/779Av2+XqbXDJqceFP6gOB3NdMCW3+H4w8vvwGWKIE3fXC/DKr8P/4DkrOgqdoq7iAjqPoOAgHusiKajDfTDJBTe6/tJgK4thkA9rkO5P8U4cniKoZ++a/gzqeAGR98Cr/z4Ld3DvwGOPDbgwO/PTnwl1fIBNKrJkuy0sshndK0r9OCsps0100EGPFyZ78u+gzY6PP0ZmLMX/49Bd/usl7r4Zc7A2cPptJpYWKpts+j18nTfRqVT78C0CiiWxT0QE1eBcCmOAMk+wkg0FY5YPluQqU9ZXkOhVkDIKia4S4bIPdlEvbLL7/4wLav5YNWMejRSVoYLHg3B/r8GTgX51mSdl/LKEgr6MOvv32A/i/0r+66C590aIDkn3EBFoqGqkCgzvoCLJv6CaBhL7zH5dffnhADMSVofSCKWZxFj5tBnp6i8A1vg6c+z3EC8iOAM8C4mCAEXA1l3SskxNC7vUDpdGli87RqOyiMQBsLozKYOpQH3HlHsqw6qAXJ2MbDJ6hvo7vWX/zGu5tYgIL3ul8gmdZA76hy8GMy874I3FyVGYD/PRse3wMhzYcWWr+JeIWUKTOh2mu8Om28p47Ye8QF9Iy324FwD/TS69dyapXRBNW9TB7wgEUAmeAZ0s9TzEHzLkAyhe2b7vsab+pw5r3TNV/L9lkCXjOFIgAtAShN+iycGsPfninVplWfh3f8gKX3Jv6IQviMyj0H6X81Kgh/P2a8t3foaz9H0AX0v29EmZyiOE5nOcpkGYhVTN15gD3ZNgXlMZ6BOeFuyL2wvs8Ob8zzRsBfyzwDmdMMf3usvIfoueZBasCHEDCIDr353tzl3tN3SsemmRLf+1q+Mf0nANad1kAEQa2DWphS8E3hdPXN0hRANn3+3vXv4QYQAtBAikJ17+cgfWIAhO8FJ2BVM5XgMzggl6OpHK9pFqR/8AoC0kHKAPkQMCIDRQW6wR06pQJuguqLm6r4vjybZqn6EesQAsNs9ArtQRVNmdSC0gUD0bQGoPDhLgoqIoAxMPEd4Tb16ocx0/z7NNCbYlEVILl/H4Hnxe95f7dlMh9I9UKvA1heJzYOo9sjsu92PmMFjC2mSr3f9MdwP32Fft+S/va1vNv43gAAAeRTN/8dOBDI5qK9J+vEXy3goCJ6JhDIhHvjfn303kdzf7fly5+G/o9/bV9w76bWHyP3BUq7rm6/wPCjA741wFfAHjDIkayO2u/N8PN7tX0Gyj4/qu3zs9r+IP0B1hfor1n4BxHP1P4Coa/IKzJd2mZBNOXu8wUAoT+vnc+L6erXUo++R/qZDhMD58NU2G/t6G0J6ElJEyXT4kd7aqeudgWN9M7HIBZfy/dseNYKoPsymXppW/2uhu99GcT2Ebr3tgEulR3QHU4TXRJNO558Mr+NXr6UfZ5/eim9Ivp3dzpTfwBJCxCZNkmggMCU1GXR/dP7xDR9+OPG715agBPC6stUYZ+gabr9BL0Pqp+gt63DfUdW9mDv9NM0JE8qwVLw633t+67Sj17Ahq0b6sn6x35oms2eM/OfjZgKC1h8Z9qpiz0rddL4JyHgTZJEzZ+FqPc3Xv6ki7bzpg6edW9F3gI7QzAPfYJA/EDxgXoC2dmDG/6sBuhponMPWmU4ufsdv+9uVQ9ffrvD0D02lb++vNHGMwbPARIsB/X5uZ2aJQxyFSgEnx9ZBa79N0fLpxRAd2CoAWLm4dJfrMLVwvPR2POJIIxXZIjjiBeSCyxaRiFOhGhEzmOMwOYxQZJhGGKhj63AusDDgbxHhn6b5oJssixC4ghbofMgxIg5ji9WKDn3VqG3ID0vRJZLEiHjEHSE77eeAFc+3X24N2H5PuVOsDy9/vXFJxZgJb9oBerxouGV7RHY1r+lh9lIxE51XFaiYVYq73tIbpVtdiXL6hQeZ9f5CWUXAyU6p7Rf79fJNuMctGhzBqfKUdQw9VBSx214qUPJv0lrboOZKEn2Abm+DrTDG8XybAeoZycaC7tpHy5FO0uHqi6LI6ZJKD/U4vaQlNiIt3uMpMoDgR5vcrGH4VhoInR/7liCdetbfTLmYIyrmm2p6vLxtCwYh8+J+jTY84NZn866hK8poiU3dXg+IxbugDZqkuSSyPgj7ZHWdh1kNwu7HXO7uXpEPheqgRdQtRznpMqv5rPeX9JmB88iP0txenU1xZt4kaSlX3tnVNyrS4XrXM8T/TFpg7Hi4kW2B/P+Gd1eRyMzg6DcYoZKBsZpXPhhssNRi6XX+YYIDiPVRVwjDXRXjnRlbq1aHPR0vdtW+17MGaszMtRmyq3NSxsEt8/NWbHHWeARZwnOUDHM8LHM9nRurE1rvdgry+2gynhxFQ+73XK2kzSBoxXr3Actb50K7CDnJYZzXHJQCUFJZKZtpYu/I+yLbey26Ozmeqc5uXeFfdXQ+2Oaeygnnfg5jKdW492SclOXHpISgjZ67Jx1qW5WVJZ3i5ZLcQBbvOZ6q0rYa5UG0Q8EaQxsTkXlOdrTkeDh/FGSRtLb9R0udbhrjP5SjVRq2KGWv8QMhZiZrAR2sd56Du/TUySo8C64cLO85JxbNkd3GUPMCWQZ3GQ8j0Bx2pzKz9a4bYdiInrObEBnYXKVi7AcqpSoO90+arCD7C/rAHZkGzlWI0oFfsYx+Shx+1O9YsQGJpXuPHaubUdH3AdiksWJ3AzuWV4o/MCCSOiKjwxeXzdg+O+VM9FLZ2M1nr1gMTv6y34dxVwAu5uIni1T3L64xlYwQwSWVKWdXTKe2MntMcNZD4VLyhWsC6FVqHWqM6TRYNETGtTL9wpfDGIqpktLxapbfmCrOcdYswUnZPtYWYrxjr31BStVOTDZ2ifEYTxsbNkZikvA7yVsY/SOfKL2B8rSTVyoFlnYiq1O63zlUtiF7p1W4nPdpBBSRpLAVG/EeAzo80y9NId9gR2HzvC2nLjmF5l3E4UiMlpDO+ZsYZEnNTzAx/Ic6ptbGemXmYvh/ZkrtzQR5vEKntuXkUhRc7a9IbfRKgl4YfQaguspXi28hqSlrq2bE3+CHVVaoLWyI3alcDz0iasVhJQdibwJfaeQAr+wWsW3DDvLKEc1ko6j0E6nKzImZldCwoVwpF2T37GZoeibXt0shnEN19Y5HHQfR0ZmFvaehRCylBUyrFFy7xqZvGdrrPOGDVMZM9MWey6VaWJf0ixl8XwVxSyiqosez6tCqdp1B5uK7duhubt4pjSmupRuKNSaCTyrG3tXT5p8KR+860quOaHnt6xypjdXtbWHraCEq+u1NCThlPU7/CiNiqp4LtjHY2vTsD1uq+hq4SgkV5Z7VkwPyczth02tzMeI0ER6rqxhFsM6+HDLGS2+km0j97LSEXq07fkLCE0ZWo16CW/zOEmyHRzD3KmGZ1Re7vVjUIaYhbjiYdOuZrG+chhs8Jv8kuu6zc2dQl6QK/+sh/LOF+mlskwwPpH2YUlqrMaIkYOwuOVdxvIWy1jlbOxLY/jL48qOfM+/wjJ1SXWaWhc5Rq89uEKQRcPRQiA3xY1KROZUXJQ9Wc1xKd5o8+3+eDtTWlVnHJrbWU1FitUaCuJuDpovOVSui30pRS5CbzYXMbDF9IaZ24Q+mdW87hTBNfrDsHdLLdTUxWncyLiIrnpsbGH10CxnoqjQBySVBrJcxLYn6stDcLbxdkUnYZAtjGgWY+l4O7vk1j3OeSITKBjf49dlrDHXhb2MtMt4XvhzWLscDdWpyA1j4Ch+W9q34rATCZrPiuQaoGYvZYlPFwcDL629b/kjHJre0tVPJMboES2de2M1Q1cKOeNLKsIcdG25yiCIarHbrqUdMscQosyE0BxO4Xxx0wZzec69BimEelPMhjJ3G8LdwhUp7YnlhejaJW5eAvUyHna1ylhiVLplThNyGxSkkC/j20VZi4ctoIzFtQrN/RnwEo0SnRedrv5t5svserfDD4RROO5wqEazWG86vfCdVuOQjdvaGnMebLXhCDgf8Pam3ACD5eSN3lon3ePOJsseb/1yPvRzFrM2NJuHl/YK63sB+IqfRcmb62mpWSJb+ya3WkmewVFJ1lDnxiVYdWW11pp1NtTcVlyiOHvXdd65MD3f9HtVTpKUQ5fy4lYp/JIth1T0Rg51b/JsL5/a4sDmG8OVLc6gT9ShcxzRW5urfMwvLGGuPJU/ievKFmw5Ua6xjdlnW2/xlN8dt6h6Emd0Fl2QAxcRB6+Xm54SnM2YSOuTsGMygrT144x20wueMMM6J1X8pNwoDY762t7NDKPzLubRX8jXsko9MD3a1UiVUWy3p6zCMQfhKr7CxCu6D910liwQ5yAycBtECKGY0VEwyJuo2+p1w3JVgYjLmR1kKD7fi3Vr79rKrZjl4OviXhKdNtMpmoLXfLpPE6E+wIao+ccwg1fVgKTkjjnXKExmCLpRuZxEOl5QT7P8JKLJsvFC/mDU9nlPbKuz7CabUxXNQEVgRz2pitYzBN2lSITtyTrVVCTqcxFH52pIpoQSHqQOVbpROd6C42AzTUheDiajIUhMmTuSs8hoTltVwNIZNffiTo28gW2Zvazl54q9oZR1RXlk1h1wzgR9B13QOFwuca1b0nnAwIDBNDYQdmlvS2waFLvKwVo8ZzdCSBLouO/CpWSK5yXd+t7Z32nJflkpznFTdLOtwzseHcl+WgFUOybeC8K2R/cqU85dApSBszFvMl3sGMbYUH56YpvR8G+MqTRO3bDU0hhbyt+CfboU74O9QwZmlhc9k1UcIc9ABK76Xjq3VZlooowGi10t12Yk5Ed24VEXIxuyYCBOoqgqW09yeYUB0fRNqRcymlY1a9hduGZzsK11aLnWeW+yA+JYcqa6XHDWOwX1jbTugxp3jweaw4i8PiCHETc7M7auzO7sMqvRheXLeGsoF+Vcj++U4HbGk2UtXnyt3IXxMBp0ZYxz3TdwrDh0OD+yqCp1zbyM8l0U+ZwZHGPXOgjjocq2mRWXzPpmOgRDbTfLFN3BFu0pp/PWsRXK4BBUacfzdXemhZG8dNxls/Uao9mQ6waNeJOtgoMETD5RBFZ712q9pvOq5Ev6IKKnbLOmhqMROBbHXl0jdYr9+tRntpyxi8pzoho3HPviMd1RxK4mLehLZb4vZvjtWJ1JtKwojXV3jmvPPUE8qFWISOfdKgz92Vl2RAmfXfcwWw1Gn1w4Md0qjHDwC02+EZsrr5+REy/oQbmobZOzOXSxPjNSHRSrk8z3srsPrpvxpiWbM0PgNmnNcjqck21hC1Kid+k4+vLZlWCllByckM5+xMbM2q23O1mel4qGVLJKJnu1sI/mhh11ubOOVCeViHgrmepqNvtBxw8S2AbGreVSV47ykTVoivuxAsQRlGqaHAYuFG/1RbLFosSqRWnLvM3RxJEguGJDINdEXTU4lnDVKd9EGTvnRsyZR35yzToazeRreuXY5GhgSGYh52Uwqygwe86DgSmOvOG5xEzWjpfcsWF9jq5D2xpoStTAaNMbtjb4DFduVJFcsbxNL9GE3K8VsjMT/4KEMX7cLKN01cVFYZPlypMWqTY7XRjEbbCYj93D6iabo1uAsZ8p/T3Yb8lmuhOM1dwPTLOxmbpGzplcOZoIJ4TDbzbmXOc10+2DG+mN3nkBgnyx6HAlAMZeRpZw3cCri3Xx2Jmjd4fN8bSKfNNqhstq7QiFavr1pVqFPS7DcW/Ni/NVn5WYXQXMZoVEyJb1W8kuMsWtIu4oj23po9mm8ZklwZR95JfzC0mMvLCIpRi+oBv4SrmFtTiH8xhsr2Izv5LnsW9j397ciB25tJDdKqldBsF0K2LmVRGI7oZw8Gx/3bo+nqqLlN75C1isSyWyOE7FBDaZ3eBdcjoui+XuQAWn43xbzTRARIDCZyEpnnypCS5BUy04BmtFbwCkVyler48lH7mymPkcSVW39jrOjqW4dEbmhhvrfDvHVxucmQm3Y9Rfx6XgqvCGDK8xr7Vd2+84wliaK8WRqo1gruiKX0mzS0AXgo60oC2hiO+Z7Mp3vM1qDLew7MEc3DlLW5jtNqZvaNW62Anl3CH9eL2011hYrnjTNchZ7pAVPdJr1j2IR8Hfj22zhT3bu4Q4O6ZEtVgswiKM+fKyxcmkEKgAbom4vDriasyIA7WXsZOcOFmI39RU2iKHXr3A21BIkmDOadUQ9jtMp/ugNPMbzS4tNlIV/JgN2wJAiwp+NGyPLb27ba9Fi9eLcjySWaxQV7vimmuKqRuh1FY+RnZzmF94KWytUUF0OLJ0SMeWoz1PUwVNUOKOd7C0SxYOzd/Ctc1ocJhoW9vfpRKmkdsFY6Sqo+PwnPTnAtltu4LGDF0dkVN5U0fV2fKVWhxGpLA0SrRETOo1YTWQJ3k/6xckoTZlXeodluy6vJS05rpzMFiOvaW1dndXZaZtKZffXDl3NidjU8UKJth784B16IXDM92Zm5nFTgJzc6MF57MXYvAe9RRx56J1jnSbfFxx/m2n9GSq7AJ2E4cEhWEexi4pWrrB61KM1WPaHkERJUziS5dzHyNuq669w4Vh4uu66eazTtgm0TImsJvkKMuI8PFtr6kRTMkUBxdcTN6WYQCmBeJWjvvWkbu4jquRHTdcHSujWcuzVUAyY3Pa58isdDS4bS+hoDNRB6991WnjQ8Es9fSmj6cNVtGlUXVzoffARMrvzrAz6ol2INnskqhIs6qitbejHVwy+m1Jzuc2vta3WuHeZnxan0GT9i/dRt3OgjPF79bGcRaKZ06I19ju2skW4zFrz1ivC+/UO72jpmAkH1ahxxjo6tKvNlsUxxZxdt1TSyZjw7nWO51pkLSZLpbaqejO1yqueAtsB6m+2B2zBbI2nCse6LaWC5dkXnEB7SajLl6dWOryuN5ZzUU3EN71T8xiGBhxhsotgi0xiwUzwiUzk2YeoYfR2RPDwqwjUorwW4h4irYj+1Lwj5Uvyj4sSX6L8G3X2xpXshVzPoyDCQajYLwGeI22Kk+5lXKNtna+AkWj15uTJJY+Xq35Xj8xkiYUAbJc7bfVYuag+sBrZ8/vEbwN13MNTpRkRl8Xc+NEUdSPP758epkOqp/HzX/xufN09vc/dgT5OC18ewR1P2qOvPDLXdeXv2rYz59emiADZj2OXNu8T55Hk3934Pr533t8MckYHo91p6dmt+7tnL7zkumPlF7ABrlvu2b41lZ5fz/4/fTi9+30xxLtt+cB98vdwaK+n5a/qQXvvbDIymx66Pqtq749Tpyjl+kPGqbHQVGYff+YPA+jgYABxCwL2m8YgX+Lmnpy+flQZIrGK/KKvvz2/wBkeGJrJiYAAA== -->
