---
name: "rar-cowork-cookbook-teams-update-pay-taxes"
description: "Drafts a Teams channel post on pay taxes status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_pay_taxes", "rar_sha256": "86f487af575ffdf83ee66b2438e272e5768a8825fb341de59d5789bf84d78b15", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_pay_taxes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-pay-taxes:edd1caeabb623da3e82b46f71eca2095eeda728225006d30e557345e53f6928f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_pay_taxes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_pay_taxes_agent.py` is
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

Pay taxes Teams Channel Update — Drafts a Teams channel post on pay taxes status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pay-taxes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_pay_taxes_agent.py` and embedded as the fenced Python below (sha256 86f487af575ffdf8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_pay_taxes_agent.py` first:

```bash
python3 teams_update_pay_taxes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_pay_taxes_agent.py   # or on stdin
python3 teams_update_pay_taxes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pay taxes Teams Channel Update — Drafts a Teams channel post on pay taxes status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pay-taxes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_pay_taxes',
    "version": '2.0.0',
    "display_name": 'Pay taxes Teams Channel Update',
    "description": 'Drafts a Teams channel post on pay taxes status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-pay-taxes',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-pay-taxes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd2eecc6126be717c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/pay-taxes'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-pay-taxes', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdatePayTaxes(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePayTaxes'
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
    print(TeamsUpdatePayTaxes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+5OjxrLmv8L2/cH2VU/zBtEnTsQihCQk3kJCyONo8wbxfkmA1//7FlJ3z/javueeiI3VxHQjqMrM+jLzy6yif3uyuzYq6qfXp71v59DaTtM48mvIzj2IK25FnYBfReKA/5Bb5G0dO11b1M3T85PnN24dl21c5GD6sraDtoFsyPDtrIHcyM5zP4XKommhIodKe4Bau/cbqGnttmugW9xGQAsU561f224bX32I9ezyfsHZtQcFRQ1VXewmENBqh/4L0On3dlamfvP0+vMvz08xuH56/e3JTe0G3Hq6qz6Unt36qj0YkzowJ7XzEDwsB7DQHHwv/RqIzsAtzw+g928/Nn4aPEP/+Z/Jza7D5qfXrzn0/vn6NP3TuxxqIx9qC7tpfQ9y7dJ24jRuhxeITW/20EC133Z1PmHQAIvz8OUx85ukooT+OT378aHkJfTbH78+FcAEe0Lx69NPEFjz16e6m65fJinljz+9pMXNr3/86ZucpnMuvttOwoDVL2/v39/FgoHfhsbBXes/gdSHvxz/69N3i5s+D7undYKZTy+XIs5/fAgu6+Lq53bu+j/+9Hdi3ch3kzRu2v+R3J8fgiPf9sCa3g3/6fkO8i/Q7H1BnzL/Xm0J3PrvrAQM/1D3DL0D9Xey7/j/F9FpnIPg/UD8L8X91YTZP6Gf/3Zt/92EZyj4+rT0U5AOte2k/iv029te5bmff/C+3fzhl9+B6H8pZl90tXuX8JbZeRz4Tfv29vMPzf32D7/8/ENXglgDyfPW1elfyfwrXO96/oDg+6gf/zgX6D/kSV7ccugz0qHfivJ/1b+/QEc7jb1v95tX6Pt8mT4zaFrEh9IHBN/lTANs/Q7Hn55+B7SQg9V07v0xyPL/+A9Iit26aIqghfZu0bUQcHAbZ/5kvBHFDWS8J/Wv+50gii+Z9ysE7k7pDijC7tIWWtd2DNisLiaPTysoAujX/+3eGfKL+86QcDsR0Ft3Z6A3QHlvd8r79QUyIqCsqOMwzu0U0llVhQCj5e2k5h4QTZd9uU6agBXxg2l0TphYpulS/x/Qr38t+u0u5aUcJoO/5sADNnCLB7V+Vha1XcfpANkTIzlD638B7AlYoy7S1LEBrU4/uvJlQsGM/PwdGxeQst/7btf6UFq4wNwgBoz7DNzbFCkg53ZCrEniNIW8uAZwFPVwrxcA1ddJ2K+//urYTfQ1f1AuDj3qRAODAZ8GQ1++lLUfpHEYtV9z340K6Ifffv8B+j/QfzfrLnzSoQLGv6MEwjaFtntFhkAOdhkY1kBTAACCufvot98f8E/W5aCwgcyJg9i/TwbSvjl8WsHDJx8OAWueTPTrd01/xA26RQAXKG4BWiCbm+ev+SSiAEPrW9z4HyA+Jj+g//DwQ8/kk+YdQ+CnoC6y+9h7rE3OdIvae4GEAPpECiwX+PVeZ6Opsnp+6eeen7ugukZ2+82FedFCDciQJhieoa4BS50k/+oA0RM4GaAhu/0VkjgVVLQiBT8mgO7qwewijyfHv4fo4zYQUv8AYmzxIeIFkn2AJijttV1Gtd3493GB/YgIUMk+5gPhNpT7N2gq2P7ko3vuvjwc+dEYPBoH7r1xeJRx6GuHISgB/X/oLiZj2PVa59eswS8hXjZ06xE5U98zLeTRKoGKf598T4NvXcAHYXxQ6dc8jQHa9fCPx8jgHiyPMQ966moQCTqr3+VPaVvf5cYtcPnkw7qewtT+mn9w9jNYPwC8megHZGYy5XnxqXB6+mFpBNJv+v6tfkOPaJqiHMQpVHZOGrtQ4PvePaTbqJ4S5h1t4H9/Sh4Q4W70h1VBQDrwLZA/wR4DlwBev0Mng8AHPc8jij+Hx1NXBKzwOhdYCzLDf4HMKVBBsDWQ44PWZhoDUPjhLgrKfIAxMPET4Sayy4cxUy/6bqA9+aLIpgD5zgPvD0HQTcUB6PvMKCDVBuEEsLwBJ4CE6R+e/bTz3VfA2GyK7vukP7r7fa3Q98XlH1NWARu/UTlon6e6/B04gIprELETNYCKmTQgbzP/PYBAJNxL8Mujij7K9Kctr39qwH/893r0e108/NFzr1DUtmXzCsOP2vVRul7cIoNBjMSl3zzK2JdHrfkCcuvLPbf+IO0Bziv071n0BxHvofwKoS/ICzI9EmPXn2L1/QMA4L4srC/E9PRrrvvfPPvu/omlAHM6w2ex+BgCKkZY++E0+FE8mqnm3ECZu3PWnfw/vf+eGxOrhFOla4rvcnZa0+TLh6s+uRU8yifW9qZe7LE5SSfzG//pNe/S9PkptzP/bzclE2mCqAQQTBsYkCGgoWlj//7ts7mZvvxxl3XPHZD0XvE6pRAoUKARfYY+e8pn6KPLv++W8g5sc36e+tlJJRgKfn2O/dzCOf4T2Ey1QzmZ+9i6TG3Ue3v7ZyOmzAEWu/5UgovPVJw0/kkIuAhDv/6zEOV+YafvfAB4eyproJq+Z3ED7PRA6/MMAYeB7AIJA3iwAxP+rAboqX1A5oBQp+V+w+/bsorHWn6/w9A+9n+/PX3wwnT9qOqPYAET/kW/NQH5USffJnH2NOneFd1xvXeNb2BN8VQPv3sUTsX97RFxT6+ASvznpwk9UITSeLzvbJ8eNgDjv/WbQAIghS/NVN9hkDBAEqi65WR4AgjtOwXT7di7j58uXv+6Sf1Tdr/6noe6tm87DoXhno37c8whqIBGfdfGEIYEpcKmsTmGkQhCeTjikySNE6RP4gHFYPMAqJ58ltnvqmF0QhsY/Qnp/7BdfnrMAsSPkRSYNqcCYk7bAUmTQeAFc9z3KcrBCHzuYzTmkzQ1t+dzjAwcnEA9n2Q8kp4zTjAnPHruoOQk7711e5jy9tEmf+D/SO03QIFZPBmK2bY7d2mU8BjaplwfRxzc9VEM9WjcR0gGD+ZznwDzP6e++2By0WO1U0yCrg30TNdJz2/vPp3ijCLAyA3RCOzjw8HM0aZN2tEjh6kp3zqfYMGJD9XgU1gobn10Y7qOwGZLvcfjuXDEOJ5MKjvbC+cl1vL24lpogSvMhjNJn+Gw7LOMxtgDtl90znUj53QLfEXQoF+gk4s3iIeaPOnpreoMNXa4q3HkTjE2Dmap72D4Ooj+yhE8M+O9xU5P5uF4IIpmdcout/N+qIWBQP2jOayMol3tVxe+ZIq5XoobdUYcbmZzjPLoFJ0oP7JTwTTXs6O6rdzrKR3c6xgz6maejSkTnPLxGs+7lk/59cZMyvPq2DXI7uSjpO1cTEU4SWeq2PuE4+5v6bEbwu0m5zRKXO/7ACtW6FjqrRbyVRU3XGSKMSOJx5hBq7A0K6QNrtwQdVyI1Nu1kR9G1CzTYdG21+OaR2oeG6hFVQ/UeL60tEky/a6hTsF82NEHO5WE4bBbmWAxttMvpFktyWvd5MDKSFHCke1yXJFKg+63Dod27VjbTHfTkdXY7A2fNAfpgJnILqVxxVrNKN5vYow+cY2oa9hy1gllP1a3Oo1nM6yJ9FWqF3oV7+mtnlkqdlxZVRBi+AXsZ87N2STVJDqdgqW+hRsGS9m5VzOKc7HEcb4csIhaGBqJ8lRz2YrO4PddxVxMfVQj191shA0KDGMktRYlvVoPFIEbgzeXM20Hs4M+MtuzcGHbiNCHpZ1s+0FWvW0t0M7ZqNO55u/HqggLxNKJYZxjCzTbNUQvq243UP0Sjm0F57qcZtO2mAlzdJkcCkI4KMTZ4Ta8mgOSskTXxMSNMp64W3yKYtI7UQdadwRui9TNEJe5Yh1XTOEeDSPfdUXV4OQ5bhk8r4h1Sp/FuRfB5BLmMopBSy5scX1uBaMDU9creYIXg1ttbF+sBBsXkVOh05a95UjqeEa53QJf33btfhOFkhzDm0GlpWPt8MUsH7XeG4/sIK70c3EOPb4yxh2vYWEYNVlmp64YHo9lTPVxcdAXvM9z9V5fHnQ94YnEcA03FEZEd85bBV+tiGiOj0qP5qyVMRlOeUMJL7BZZcp9fVOiG7qweEkTWG0RYcsqveQ5AtohUqQp3+7lPOGI47W5RRe7TjdmhMAhrMlH6ky261bJr3tKp4J9gi+q7lpWl5yLN95iOIu7yzZRItVoljv2sJa4kKf4YJacg3ZMtwF+YIwl46RStBMldrc9HEVJyujjvsm1kbkma6XT8FjVh1bo1fksUGCQCgLYdON1eBkyarQSzPRkFyNx1NwnoI9rTbE+nAZ615iGWS20+cqPjN1yvx63N9TSqiPBdTIvBIUS+Cmpn2KUtTdemjDkWGxnW5mFzdlM3qDhfmkOqjrog0bwNS1w5NDhlOzujTENkw2lYAea4rcMo5YmcrRSr7yoiX/V5aMu5sfYs2zTyDZCJgJkmBW6dZenaC6eeWdBICvrmqeImZ47hN71cAHgro6DY2h0QjFaUErD9rzSkq1acBv8YKLBbWccF60t36h9gTSza6suh2VXtYK0uIyNdeOFrWVnfVBFuqdoDOUtatV30LWE7C1buxlmW4LF2Vp3WG1oO1o1Md+Mao8GLpfhy1RPc2kWbCrSPqnOzukquUdJNLPpbSCIymITRdrmOkTYTvBg1rvWqwatzuu83hzOeyLmHQrXRsP02q7CUy43xwWVFscFPz/rJ+tAOtf4rFvHWyMu5MVe4HFDWW3WJbnrnMNJKEtMc2wu4S7pYZHEqHvgUEXpVm7EZ6YThmbvBdfxRgcwjuGsIBYrdYlekQCZl+HWY3LbsWhkye33mYEUpYMH446trq1iqS2I5GSvonwVX0gYVozxsMH7mXAFYJUOuTxpQ3wNUvK2v3EbItEKs8STjqckYXk9UrUtVax1a5c0PyZmLHuusFLk4/7K2mO/bb3jcauxY0nqKKZorZSg3bLZLEN6Sw6oxlPWJtLPx7IoGY0VT6o0ZGPDnvATX60UaR/jLntj42IliucVYUqX076p25VJSDU2KJqC8DLNSIsl3zvJaRe4FIbAtlXiq8E08RJ1t4K6MmBzXV82J6VJhL3alREfJx2W4YsLv1oQAuZYI4bYcddmgm3PVbNv7BalPcPGjvRaJNSCVa18D7rrxlgHi9tKIXMi5I9ZQc/Fa2ZdIhMx1qiNbaQN2Cfe5OVaV/IGthxL8VOFM7pRwrjFHgDSI0u8Py38LOc9QTl0NMjFClvIyiiwmHdoxB3SG9YmLC1rpe+ZqztXfXPOyXp9WceSme+CIRzaGZtt6vl6rWtXfb+rZbmggsOFWKpIht5Si2i7Ic4P2epiyqYV4/xxKWR00g8FyrRM0xR7JBkizVF43B2EDGkzOaw4fWxS1lwvkoInR7nfIXEuw5LN+FqXXeouwy8idd7W43577tr9TYVl00f02BldY7CM3QofzOa81ymWXvBqsTHNeiYUfu7tjPhUBJVzO9Tj0t5q9RKHJSnelP5qG2rmVpJ1sQ0xd6HXshVzy31h9Ky7PpsNv2eR+SpZgoawFVUk4s/zRBM3ZT5XTkufClpWDc7rnVHOB1bTIlIZGkVPlvUhVVP/sFvKyano8Jl7qksyd/ikL26Kt1eWVXktksXAaKeTmR1OS/V8nvlnfDWD8zasJAtbSsexdjc3qmYboXBZdwXSlsZCUA50ghtuB0NuKEYfOrBBFEIiplmpdmfBYg0H+RbWveXuuPAie3kUUZ7H0CE2FMAn5BCJ/m51VMiutIRgiSGhlKJu7u+qE65X5FFr5dE+dDI2S8eEDYmlktGp4dpXoUn4k5F4XD+Qy2OZ0xuu1Y+rJJFmg11Zq/MQL3KLjMt1p6xYpfHtAN1cD+UObbM6L0ep6IpN3FXBsPK0QUT61bU0Vx1HLlRbGF2eO5S1LSdcInSnHXxb762okx2+ldKlsLoccFTnhB5QFErQWwfs8wmG2jZH04vKyhGMiwwaDWncYmNFIl6289k2sJIZEnMEUjlpbCDn9rBtrUtzya5tXQTKRUXD43h0b2e8iyuUAL3qtma3uGQbHMHMC9CmaqCKq3JvGYvTrNzt9uNaQVqvLg9VrvAevTUPxxiHl+5uIePpTb2JSR2fR8to9nlK8H3I8E5c8MumO6HVpotZeqeFJE/a2pZz0qu5kLUt4zMphaK7aHQEOiL5FbkK64BYCSmJGdgM09I+98Tz4uTcWu+QrkMnNQ3glNAjNRZ4RLONTOD80jsb+cmYSxFi9Ii+PfILPDkfSMah8WwxRyJjnclnirgaDLc4ItW4XR16DBNuZ9dNgd/ZZHu6bc7zoqjy81G77LcMTqQ1eQizTZBinpadsJVgEkf06JSJVkbifNF0i6wMBOPgH4h1zDnRMKDuxRf6fMXLJ6Nh2PN8CbjAQ0+L4Ip0BFpQFi8PImeS2eGaX0R0MGQNtNMgTqSasATO6BtuHBQdubJgi5hiltWNuuGdnJpeRAVMHV2waUBsR7R10lzrJ7tDFvFBWbNDw/ZhFecsV1c3q4YTIV2qCTHookzYjWrfrof95sA5CLucc03V9jzbNn15dc3b1gTFbJuMPIytEtK1NNM6pkYcK+tbu7NNzjpI4vUw2k2GBfAWvYgY6e9VHHSx8oWpfCqqUhLP0UPb0WcEPzUw5h52mt+GvjzOfLGW1xi+zpe4bs03Rm546i4K8vFEMQ6KH/2Lw5xh1QG01lLXU3AM6sKqfdg7h4TpgYYavQjSLjI9qu1V2ceqk7c1T+4+ZjCb58OionYKno4rRBxWEi2NR+dAaGcx2jDKqt23DSVgnQgvD6Oqs/g+32lVfbJh0MHVdEY56k3uuNl80+OJRodztNXxUJOlgNbCy5rB1JkceRf3OIe9I+EvLtLY1LQc83W8mHszGj+0NYg5xrnEphpfYXqQYIoz46Nle8MV7j1YIU5gC0sTTHBoy9gwdmYc117AylrP6SRl9OeBuxlwHrrmaPUnOBKSaB7aLsxb2criF2F+TtKg0VRC3Fm36kr2OL2S4Dklxrixg9uhOy5idl0dzxu7JdXFrSc552xK/HFRp2NLkjgntSftNiMspYGdWVSc6X4cCTtc7iq4s2euBzOEQ9c1SvF7FaEiajvOr11384bjoAXzi+6vTC7a9henp/urTLO3swg4ows7/tKQ/AGTlhd0M5t1yOEKe7NVOAbb3DgFmq6y8pFk5+YV9pWIpsZ5hOD8yUGL0YlFpaZorutGzjHFpqo1yrM7o+CNdpZYBHWk5fbiwYmE4TFILQ9jvK0TA1RQrzAIEBjueVloiJJblxN5UwWcsTRhsZeGmoeD2WynZFvVqDBfuSE8LW3J841ciQvfRsOl03dr6SYqG7Wwb7maGWAvzCnybkAZwraio4zOExWl5LWxpekr1s+KJbG3ORPFZ90JE8Sbft5bG/OmpTPQTMwsaawFu7x1wXWVGh5uWU0vpYFvuzpu4LcFU2KegvN0UjX9Ck/gRY/um37nV+1RHjLngjTKmp/rgoNTqrRl4pqnDNnb4oOHX08nQ8z5qF9m1FqLCRvH5kpPEHZ/YXGEbBbh9YSnOW0ZeXDcDwDUE85eYldGIwxl6dVoiUou32C362ymoToaMdeFS8grV9WPe1jPSPdiH4llArY9oMsMLyTAmOQXRwGeGWSqXPoi7ee+cemNXWG3PpK55uWCOxuf0pbIpWU6KVtvqFutzvoZvT2jV1SipBXK7IPGKtmAueYR0m22alCHkcHcCKtr4Ku3n8kUv2g1D/fpvhxybNk15WUUmW5zhQnDTeDdeub0LHZKrkEUgb20jOhlzDrzpTZWNbJymZm8lrBKm+sFta2Yvmn0GSrOcYZFeL7fHVr3pMI4UnCrWKnaqzy3OimZGSad4GOMrXvMnDE7JapTwKGWOy8kJRJ1mA3l1Z69wFunSEZvjJEtiIUrhW/PHnrtmCNgPfwwR+NiUezTc67B5Y5UaldQltFMrbKWujUBcjGkzQ2UUI53T1lojdcIbFU8kGGxhbJjMVal5Kqyjdmkr9jXIrT7DCW1NchN228D3xKDBS6O7kKsmo3shdddjG2wtSF6TkFFYJcG8juBdTRQrPVFMOIMHbJoT4KoiGkRRvfsQUWN7aXscvKashuFot1FH64cy6RPs1vMZ1lMwJx8KbNxEFZ9ViLD4qb50tXQBxl3LXeGH3R5XqrOMvEMmAB76DULGpCCZdl/Pj0/3V+pPr2iCEGiz0/T+f37Kfy/Ps4Nx7h8e5+P0yjy/PT/7gTycRr48S7ufiTv297rXfvrvzLtl+en2o2BGY9j3ybtwvejxv9ynvrlr092pznD453v9Hqwbz9eULR2eD9ujnOva9p6eGuKtLsfNgMgu2b6+47m7f2g/+m+gKyc3hp8b/B0uHo/y35ri7fHy+mn6S8wprdevhc/Rkxfw/cj+ecnbwA+id3mDafIN78upwW+vwuazl6nl0FPv/9fnLr4nZkmAAA= -->
