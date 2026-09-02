---
name: "rar-cowork-cookbook-scheduled-brief-plan-operational-allocation-and-investments"
description: "Schedulable morning-brief email summarizing plan operational allocation and investments for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments", "rar_sha256": "3664b4af97250d1d761cc576d38a070adea574041c5ef6db0eba2bdc38555717", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_plan_operational_allocation_and_investments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-plan-operational-allocation-and-investments:808651f091d62041bc25eebee1991c551585d6e60344c08632b9e1e4ebe73ee8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_plan_operational_allocation_and_investments_agent.py` is
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

Plan operational allocation and investments Scheduled Email Brief — Schedulable morning-brief email summarizing plan operational allocation and investments for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-operational-allocation-and-investments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_operational_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 3664b4af97250d1d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_operational_allocation_and_investments_agent.py` first:

```bash
python3 scheduled_brief_plan_operational_allocation_and_investments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_operational_allocation_and_investments_agent.py   # or on stdin
python3 scheduled_brief_plan_operational_allocation_and_investments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan operational allocation and investments Scheduled Email Brief — Schedulable morning-brief email summarizing plan operational allocation and investments for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-operational-allocation-and-investments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments',
    "version": '2.0.0',
    "display_name": 'Plan operational allocation and investments Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan operational allocation and investments for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-operational-allocation-and-investments',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-operational-allocation-and-investments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4485c489f7c26daa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-operational-allocation-and-investments'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-plan-operational-allocation-and-investments', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefPlanOperationalAllocationAndInvestments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanOperationalAllocationAndInvestments'
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
    print(ScheduledBriefPlanOperationalAllocationAndInvestments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZej1rLlX6HzfbD9yEpAzHnXXauFBAgJhECgyeWVxXAYJCYxCeTn/94HSZlZfr5+3V7XH1pe5ZLgnBh2ROyIA/Xrk9PUUV4+vT6tgZMhspMkcQRKxMl8ZJJf8vIE/8pPLvyDeHlWl7Hb1HlZPT0/+aDyyrio4zwbtnsR8JvEcROApHmZxVn4xS1jECAgdeIEqZo0dcr4Cq8jRQJV5QUonWGzkyBQa+7dftwUx1kLqjoFWV0hQV4idQSQElRFnlXxID+/ZKD8BwINiMMM+EidI2WTIT7U0yNw/QWAU9K/QBtB56RFAqqn159/eX6K4fen11+fvMSpqk+bgS8Mhq6gVfqnUeMPm8aZr3xaBKXChSHcXvQQugz+hpugmSm85EN/H79+rEASPCP/+Z+ni1OG1U+vXzPk8fn6NPxnQpMHz+rcqWrohecUjhsncd2/IOPk4vQVdLpuyqxCHKSCyGfhy33np6S8QP453PvxruQlBPWPX58+oP369NOAx9cnCA/8/jJIKX786SXJL6D88adPOVXjHoFXD8Kg1S9vj98PsXDh59I4uGn9J5R6zwAXfH36zrnhc7d78BPufHo55nH2411wUeYtyJzMAz/+9GdiYVS8UxJX9f+T3J/vgiPg+NCnh+E/Pd9A/gVBHw59yPxztUNW/hVP4PJ3dc/IA6g/k33D/7+JTuIMVB+I/0tx/2oD+k/k5z/17X/a8IwEX5+mIIlbmB2wjF6RX9/WK3Hy8w/+58UffvkNiv6/ilnnTendJLylThYHsDje3n7+obpd/uGXn39oCphrwEnfmjL5VzL/Fa43Pb9D8LHqx9/vhfrt7JRBFvgkEeTXvPhf5W8vyMZJYv/zevWKfF8vwwdFBifeld4h+K5mKmjrdzj+9PQbJI4MetN4t9uwyv/jPxAt9sq8yoMaWXt5Uw/8U8cpGIy3orhCrEdRf1svFFV9Sf1vCLw6lDukCKdJakQuB1qE9TBEfPAgD5Bv/9u7ce4X78G5WPVOUW83Mr2lydt31Pn2SZ1vkDrfvqPOby+IFUGL8jIO44FlzfFqhTghvDfYcssayMpf2sEcMLDuzT5zogxUVEGl/0C+/Rv6326qXop+cP1rBmPpxDe2BmmRl7AXQLJ2Bm5z+xp8gUwN+afMk8R1vBMy/K8pXgY8txHIHih7sG+ADnhNDZBBbYIEMWT356E75EkLuXTAvjrFSYL4cQmBzcv+1lJgfF4HYd++fXOdKvqa3cmbRO49rMLggg+DkS9fihIESRxG9dcMeFGO/PDrbz8g/4X8T7tuwgcdK9hdHj0LWjhf60sEVnNz72dDKkGqukX719/uMRqsgx0NgTUYBzG4bYbSPlNn8OAeuPeoQZ8HE0H50PR73JBLBHFB4hqiBXmhev6aDSJyuLS8xBV4B/G++Q79exrc9QwxqR4YwjgFZZ7e1t6ydgiml5f+C6IEyAdS0F0Y13qIaJRXNUz0AmQ+yLwe7nTqzxBmeY1UMGWqoH9Gmgq6Okj+5kLRAzgpJDSn/oZokxXsjXny3t6HRXB3nsVD4B95fL8MhZQ/wBwT3kW8IEsA0UQKp3SKqHQqcFsXOPeMgD3xfT8U7iAZuCDDcACGGN2S+ZZ5q78wp3zMEoh4m3duIwXytRnhBIX8fzgcDf6NZdkU5bElThFxaZn7ezIOY96AzX0yhOPIQ83AGR8jyjubvfP81yyJYQDL/h/3lcEt/+5r7tzZlNAYc2ze5A9MUN7kxjXMoiEtynLIfOdr9t5QnmFgYAyrwXGIwOnuy7vC4e67pRGs6OH353CB3BN0AAymPlI0bhJ7SACAf6uSOiqHGnxEB6YUGOoRFo0X/c4rBEqH6QLlI9CIGCIO0b1Bt4S1NETrVhgfy+NhZINW+I0HrYXFBl6Q7ZD7MAIV4gI4dw1rIAo/3EQhKYAYQxM/EK4ip7gbM4zeDwOdIRZ56tTg+wg8bsI8HnIF6vsoUijV8Z0aYnmBQYA12N0j+2HnI1bQ2HQomNum34f74Svyfef7x1Co0MbPFgJT85bTn+BAdi/T6paosJ2fKkgFKfjI0/t88HJv8fcZ4sOW1z+cN378a0eSW9O2fx+5VySq66J6xbB7Y33vqy9enmIwR+ICVJ899l6TX4YK/PJdBX75rMAv0Igv31Xg71TeEXxF/prZvxPxyPdXhHjBX/Dhlhp7YEjoxweiNPki7L9Qw92vmQk+w//IkYEdYaW7/UeTel8CO1VYgnBYfG9a1dDrLrC93rjy1nQ+UuRRQJCKs3DosFX+XWHfeAgG/B7PD06Ht7KhW/jDNBmC4QCWDOZX4Ok1a5Lk+SlzUvBvHLwGOofJDUEajnGw0OCuOga3Xx8BG378/mx6K0HIHX7+OlTi841jn5GPufkZeT/J3M6MWQOPcj8PM/ugEi6Ff32s/Tj4uuAJHinrvhgcuh/PhlHxMcL/0YihAKHFHhiGg/yjogeNfxACv4QhKP8oRC/uGD1opaqdoeHCPv8gg/dUfkZgSGGRwrqDdNrADX9UA/WU4NzAFu8P7n7i9+lWfvfltxsM9f2M++vTO70M3+/zxj2dBtl/w7g4oP3e5t8Gnc5N8jDU3cC/jc9v0PF4aOff3QqH2eTtnrhPr5C2wPPTAHEZwzPB9fYQ4OluKPTwc/CGEiABfamG8QSDdQclwaGhGLw7QfL8TsFwOfZv64cvr38+rf91JnnlcI6hiQDnCZ8Z4RTheiMaABcAgucJj6YJmqN9BjA4SVEeXEuOXB4QgIJLWBIADto3qE+dh30YMcQNevYRnL/zcPF0Fw3b1YhmoGySYSiXcgKeHdG4T/gsQ3gezTI+yTk4i8OzuUOzFHTLo0HA+C4OXGfk+h7J0TTNEuwg7zHD3u19ez8vvEfyzjVvkLjTePBm5Dge57EE5fOsw3iAxF3SA8QI6iYBTvNkwHEQHf/pY+sjmkOw75AMJQDHVzg8toOeXx/ZMaQ1Q8GVM6pSxvfPBOM3jrvFXDNS0TJBu45kDNIu8PRUsyuw4c66xjSGsJSPMb24FDtqQs4T1yC67ZYqBHKjLccBvsH2O1JdXSd0YE4S/cRfBKIXBHc2J/3sALIsSYvJWDFjrk+N2jpL8+2oMXrxqqqWtsAm8zQzGn/XJ4cy2fjbVuy2izN+Tfbna+2vD0Ayz7U5wbBgXnK4K6fmvLTRPbPD6WNwrqnCIXcOkZ0zTPIkne+oamHnSV7Y68JNl935lKKNR9iotEh7UCTThDsrVUVLcaaNxk3TJm6pLRsp91fqqQ+yw4le7g48qlQoaK8Zp3TrRlmfOmC4juG7dl841AiLhNpcK6oMGi1rRFIvvcaV7HNj0oke00mzy3IppnB+JajVQtDP5VmcN15G9x1sQ0dln9mb+OxthLl3iaJNX88detcIjNjPpGSd1zvzTLakRToKc6ypEViMkh0/q800bjb99RI5/Tq1tGSvXPuWwi/Z/izZctWexGMhGFUBehvXvZ4UeTvPzgzJTsSwWfama4zF5ZrTz9oyuYZYK5hUuy7VVmrktPBmtDPnhWth55u44XdVvGC3nVxepaslJx12VVRxW8kjxgmJUiLnlzSJ+1O9tQ4qf90U23PKE6Bc2vrelqepkqzlRjkxaUXrobOpeIv3DnRV71b6xV8oddTT9KHmsdzdl/5V4rpmRtH7JXs6LdgVqXXBGEIkFt6ZoJ2j5s/oovPO1cZsbKI2kzwdE8qG7Y8MHmukdEYX56xLrjI68fRdXIiYqXn5VsSSY+QZIdX6Rn9NVntDa1GadZrDVtps9lt/Zl6S1lr1qDadlQq+FtXC4KvTSG6a3rXP9BKwpxG7m9eTaJS2m2uZobG27FZtQZpBmGN1GoRcKwTgQtet7yi53+LBVo9wtIlnjKFzs/movDYnVJ2a9L5fxUdXmJ/37WJ23KhKmXiwMuZxvxplxkid2opXkmKub11byA+rRDYSjtn2IhlXCYtqy2By9fqVl6EgFSOn5cJiVnRlnGRCO54bnrmRrWYjno7VbhlPKPOkZjutiOf53JS07YY4ZtPjXlcBTS5qbuZyMBSHeiUdaAYomLk2M2YBMkbVrW6GH2cFKmftgayUE3ZkD80sBU5YFykT0iijCW20rbJJy+UBOjst+ZypFrtk17djmR1tyHlRBXU8VSeFaJ/dfn6u5ik5E6+y7lxqrr7uJ0rsUhnNRh25MXGbm1555UiKYSIWkiXv9vjK12hjXy+WYEGhO7K4ijpWRA1l9d4IbfXdDl+fVe1wLbuzVhROSi6nw5TmEBtsdyrG+Lk04/Fl7BHZVp9zo4ldjprl9uKeg37BHqO23VS5ITcgF1mTQ4Vy0qTHrXT2m+lFxZbzVac0I0nZxSRL66aTyHGyw8yUigjuHBO6pZWH8li1YkT3OSzH2jW6w9pjmiaJ8JBSrEKaHpZqLDpYtu8posgWhkRsm0KSgqKixbXMxRS7W8f4XpllJVc4lluQbjY62SOQl8YFNhq6FNPcMHb1lkg38gTFxgzGpN2RMa8gT9igUsQlV/I8ecaEYNHxjAW6IwEM9AgkSRY8kYmvTrLXePZ0FnegwDC7Hk+EsUEHy74S8nWp2WvAUYQj5tu9fsQ3R5IydMWMlKlYmPz5WjD8hE7xpT8SUM3a0HVxisxq1pzUy9ZaFJ7CSqjQ7vGDYkm9dhaEnp4r0F03VHewvGPa3OqStcWFdl1Iu23NOXvZulpS1E7XqK1RG1UWvZnsF3TaK3tp6hEB5fvXK9PNJ0xx5B1DYtcUz5iwsWJHZqF1Guw1o1WbEQxoXY4207mg4tdNozfpBbXWR+WMeu7pUOLHvY1yuLNdpe0usjon9Pn6yk6dk60YHFhNNxKXTkuMYVCx7jGuttcRTOVkZVBHqw2kZbceT83JDJhoPU0rr6+UdLqJqY3OhP1YX9YSte+MJkypiVQuu9ny4qjdgehserlWlwBVFsWiTw9rIrao2d7G59Wm2+aGuE40OzQWcbRcHKJtVGhqs6TqnF1c/W6jxeMqJUxrP6mtzVo0GWuyI5kZsfY1BhT1ZJEe856stq7ngvMoWnvWBlIjobOn5Xaxa8gcTcR9GGpVKV9a/+CY6paVJ2ZXEqnebGRFM7hDpTT7rF6xtuQexYSTaLI/7Zaj1Xw353xB4yVNniz6xO9ix1JJQE5HVEoZlJFaGz5jaaWL6HU36csVM+nis+twTbFWz3nGW2xchi5+lmebGjaDKjGMRAAazCl7nvaesl0C0C7oTbOW7dSYlGmtOAQ2HlfreiKe67SsjjF73UYWc+BC2xGIucGL8ro1DtokCHFUnTMLawn7R6v2pwkl+w5myPtj3zOFXpvSbOpozDirxCi0LXLEMnwbMQdLYYykTEFCrcVLGbObETubVPPAWSuHfbaNQ3VM0idlb6g8Cyt4uk/UTcmea+wQd+1Bw4nF9Ty2KhItz5uJsfatyjmuBbzLqkO8w1f4WmOMM6fahBuLFs7ka+/Irw+mud4CeV9USy1dTYMpVU6u5lwVTzQVNRfmIlXdWtTHc4wYhd70fF1I2diItfVJCLCpG5N8vraj0p7sjACr27Qvu2y2kxVeVrPwHBJrsWcbAOrxWadXThOHvXyKjYhlsY47lSveD+diWdqnmZflLvBITeyIw3SFZgS7EuUti6JLPYHDLinu8t6zzluStWlrii30+phP8V0LpvZYzK3IDtWpQCtSJkj7Yk6teGWzsPZCa2hCJ6kE6mWbxXRZ7JNwEQqV7EIYs8VhqQisma3F2sk34mxHOOmE4onLZJJtYoLF5aMlncbNBj+sI++cyV0Qdt44lA0sbui5LWOMvvHUc7oKt3nHK5k6m0ZJrCqVRV19L59YxXjKXNT5WsONsUumGW+49MJS3UOxPGnswl0LmBof+cjSNLX3NiWzSY45vjDWI28nLKLzoY8OCisbq2ghXufavpEmIqplEx5XW0Y9n6fqGTRJf1BtSyyqqz/KHC/qpMN4Q4/qixkl6IQTsbxKtFHhotli3O/73G3UU1dtdpl0OsfSiU6vsXwlCJc6tOIyC1s0PU6PpGFVs/bMZPt4mWhCTdrLvu6qYiNI2aJ2qqzOacw+JRIx0nHfXxT5qIsjEetrZp6Q3bbxVulB4iZsqRz9xj7ixJaKCcGWppEqMiax5uyxf1gvJc0MHDju0f305DZiEzIVxzDXPK4PVwLFZWZsZtvSQmcF0wC6oSgmXxatON+2a5ow7VRopU0diuiYPJ3kfuzwhT4Kl15EHoxSz2hHyLNjHk0Xc2mWOnZBuO4sntZ47MptEy8jI0NtJqcXzlLarfe6cqV9bXuFs8thUjpTbbtdE3rFKLQqHa6oleC5cV21uDvTreJ6XB+2spVYzJ7S9wtaia3QK3ZXSRfl0Fxd5kaZhWykHRhzSuJMYOiwHuiwOqxmVqDqpHSyFqf8Amdi7pScNnHhcYttTqLwaECeJ6u6CuOqFFRuavnpZY5Oi/NhbuA7ySOomTULl0WEzrceXmiwgfI4p1ajpI9qY58HUZjj0z1ug2s1wSWgEWd83BlXV7dUBveXrY8JCrGbk/CUMh7z2nXBX3Wq6RlyyU3ssBjHh6rPGqOencWmmqgjvT92xWzhbkdTOUo1OQH2Phn5u5XfXkWv95zdjNxxnmMlRwfQemYdjwbwpd0u4ZVwIpRRWRarUVnmiyMbWRBVeW7Jp4XPg0tNlsSUjDGLClkDHHl6i4/Q0SKjrkbarTK5x2anK4umq0WMjnYcOtPL3Qzs5VVL7sbBnkkmXH2u13bLZqe8sWxjGeHaZbQZCRdlIiyOfg6nnHEAeqZuD3kcLeSdaBpOurc5UwNzmxYnmG3B6uQFtlww2I5N9o6sWOHk4kz9ZB/6PqAgXTTrJj73CppMz9wZhCOWHC3jFbpRAO3a29kRnv0wfTThQqe/cPqFIUOflcmZ088UDksDrCUk7CKtvOaCY0WAdQIGmKxpAUWj8Iigx6S7JtO4LYKxeTQtgZKCmKAyfJYJlo2F2+MKnWyImRh2FHbYaU6uqLpOjicG2sEQxlMu5Y3deH86omrI6bW7KyO/oke7cReWVeu1Jr6cpXQ0Esu5NKYJHls4PG0e24krkUK9PkQzbmrv2KjM8M6Y7mnWX/L0FF2ZMWgusLvuYZISlbhKUZZdt6foarbV1QTJdtJ36BFSZhbMgACnDfc68gWv1q/UVjXQUWl7mYNdty3RYkBvRO88oZt8Vo078WQRFLolLrq69rc8dxVHs11dByMZNv0x3yw0dkXUQdAHS5C7CXkcx3xLqI2+ZRN+RgaLwzVM8/EY8906u2w6bh5T29Ack40gsrHFhPxaTXPWrwJewlNzcjlcSBVnQdRMZiMa7M4xAMJpzGgH9NBRoi40lhxauytorkJzibBMtxuOtc7sRU2z/WQ0kThTbxfH4wytWR5lgym3MjBbIJTlQYvbyl/OvZkILuYhrC5WPWHq/rDXl0K0Ci8bokQDWyQIGVPsFqNiXUzyoJKCWTatXY4npZHSuNG8pZn1bp/SiTbHyJBVeUYGM5G24dm1cU0sWh10h6Ws0qmrbEmUdJexoUFFnTc1XWrauRc2E8JyIU6DK9rJ284TFoEvdUuKPErlyneX0lnwtGU0wqe7Lbs/gJId1R48KrkNQ8I0lnOfsWN0lu/j1hjRPnspL0KuT7z2XAsZF5FLfC/aU0Zedak/Y83JNORnLB7bu43GFza/XKn8aM5fwlk0dUjbz5rVUa+bUatrV8cNRquyYT2C7EzDuMaXKxmQVmmvFpNV0IbHWcfI7o6bxbLXEvqamTJuwXUXUiBbhfUnI5LSV9j0sNDn69m8Ugi0tZZiLx1pgYgmZ0WwKGJDrq1lcOETl7Bq5XRQCf6SV8q0XWDyLN+ewlRYn9qYRtEm0Q3bwohTp/AhMbXYedm4M6DOD64bUZ5dt7t4OpXUEMu97XEm8ELoz43wql0ID+wB7C6n8zklp25SMSmOATSFjWkfxPx2XE3XGlsFHs2crJG2ii4sGY+K8qJmGZsayzBcN2JxqevQTzBZkjckcyJPdC5k/qk8XXquHF3IeY2XjDOqDoD32WZMxegE2uU64x2PGePikvpccdnhhTt1xXkBGgo7NVeNbIdTLMtnC/Ua7sN0iaamztSCWLqna1d0C5FJuB4fZSSpUXK61FqBpqa+0kzB1msX09l6KVDRfgHpQpMCX0x9k5ZIOeMEWp9O58fzbH9YpWwwm6mNqJsYJwh7mB2qcR6Px/98en66va9+eiVwnhw9Pw0vKR6vGv6mJ9LhNS7eHkpIliWfn/6+R5/3x5Dvry5vrx6A47/etL/+Lfb/8vxUejG09f54u0qa8PEg9L89Ev7ybzzBHgT39/f3w3vZrn5/6VM74e3Ze5z5TVWX/VuVJ83tyTuMW1MN/+qnenu8Gnm6QZEW9eNx9neuwytBXgLPqeq3On97vJiJs+GNI/BjpwaPn+HjPcbzk9/DLIi96o1k6DdQFgMQj1dswxPk4R3b02//Bz/oil0EKQAA -->
