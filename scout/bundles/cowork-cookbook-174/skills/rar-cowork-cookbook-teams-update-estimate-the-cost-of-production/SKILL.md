---
name: "rar-cowork-cookbook-teams-update-estimate-the-cost-of-production"
description: "Drafts a Teams channel post on estimate the cost of production status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_estimate_the_cost_of_production", "rar_sha256": "2d4fe8a4d0236a0dbe485b7aa1ac3c7a7d35f4ad072d9e9eee55d7465b26d911", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_estimate_the_cost_of_production`. The original RAPP
agent is preserved byte-for-byte in `teams_update_estimate_the_cost_of_production_agent.py` and in the RCI capsule.

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

Estimate the cost of production Teams Channel Update — Drafts a Teams channel post on estimate the cost of production status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-estimate-the-cost-of-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_estimate_the_cost_of_production_agent.py` and embedded as the fenced Python below (sha256 2d4fe8a4d0236a0d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_estimate_the_cost_of_production_agent.py` first:

```bash
python3 teams_update_estimate_the_cost_of_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_estimate_the_cost_of_production_agent.py   # or on stdin
python3 teams_update_estimate_the_cost_of_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Estimate the cost of production Teams Channel Update — Drafts a Teams channel post on estimate the cost of production status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-estimate-the-cost-of-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_estimate_the_cost_of_production',
    "version": '2.0.0',
    "display_name": 'Estimate the cost of production Teams Channel Update',
    "description": 'Drafts a Teams channel post on estimate the cost of production status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-estimate-the-cost-of-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-estimate-the-cost-of-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1a12d3f6e1de129f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/estimate-the-cost-of-production'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-estimate-the-cost-of-production', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateEstimateTheCostOfProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEstimateTheCostOfProduction'
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
    print(TeamsUpdateEstimateTheCostOfProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjyJLtX+HlfKjuUVUiNiHq2jUbQAsCxCIJhOhqy2YHiX2Hfv3fXyAps7qn7515PTNmo1pSQISH+3H34x5B/vpiNXWYlS9fX46elUJbK46j0CshK3UhNuuy8gZ+ZDcb/IOcLK3LyG7qrKxePr+4XuWUUV5HWQqmr0rLryvIgk6elVSQE1pp6sVQnlU1lKWQV9VRYtUeVIceEDTd9KG8zNzGmQRAVW3VTQV1UR2CtaEorb3SAo9aD6JdK79/Ya3ShfyshIomcm4Q0MUKvFegiddbSR571cvXn37+/BKB7y9ff31xYqsCt17uCmm5C1ZfP7U4hR4LdJB95UMDICa20gCMzweAyHSdeyVYLQG3XA8o+7j6ofJi/zP0r/9666wyqH78+i2Fnp9vL9OfQ5Pejawzq6o9F3Ks3LKjOKqHV4iOO2uooNKrmzKdwKqAEWnw+pj5XVKWQ3+fnv3wWOQ18Oofvr1kQAVr0vXby48QgOHbS9lM318nKfkPP77GWeeVP/z4XU7V2FfPqSdhQOvXt+f1UywY+H1o5N9X/TuQ+nCs7X17+Z1x0+eh92QnmPnyes2i9IeHYODJ1kut1PF++PGfiXVCz7nFUVX/f8n96SE49CwX2PRU/MfPd5B/hmZPgz5k/vNlc+DWv2IJGP6+3GfoCdQ/k33H/9+JjqPUqz4Q/4fi/tGE2d+hn/6pbf/RhM+Q/+1l5cUgQ0rLjr2v0K9vR2XN/vTJ/X7z08+/AdH/qZhj1pTOXcJbYqWRD7L27e2nT9X99qeff/rU5CDWQD69NWX8j2T+I1zv6/wBweeoH/44F6yvpbc061LoI9KhX7P8/5S/vUK6FUfu9/vVV+j3+TJ9ZtBkxPuiDwh+lzMV0PV3OP748htgihRY80j/iSj+5V+gfeSUWZX5NXR0sqaGgIMBY3iT8qcwqiDwd8rt0gO4VhEA9jkOxP/k4UljwGu//Jtzp84vzpM64XrioLfmTkJv71z4BkS9TVz4lvlv37nwl1cI8BNI8CiIUiuGDrSifEsB1aX1tH5eepVXtoBZ7KH2vgBO+jJ9AZQJ/fJXlnm7S3zNh1/uZB89WOvA7ibGqprYe52sPode+rTRAbzs9Z7TgMXizAGa+REg3c8AjSqL24nagXrVLYpjyI1KAEdWDnfZAMWvk7BffvnFtqrwW/qgWAx6FJAKBgM+1IG+fAEm+nEUhPW31HPCDPr062+foP8L/Uez7sKnNRRA+k8fAQ35oyxBIOeaBAwD7gMOB4Ry99Gvvz2BBmJSUPGARyM/8h6TQczePPcd9SNHf0GJBWR7AG2AdJJnZQ14G4rqV2g31bGnvmDR6dHE7OFU41wv91LXS50BSLWAOR9IplkNVSAwK3/4DDXVoy7+YpfWXcUEJL9V/wLtWQXUkSwG/01qPoqnlWZpBOD/iInHfSCk/FRBzLuIV0iaohTKrdLKw9J6ruFbD7+A+vE+HQi3oNTrvqVT6fQmqO4p84AHDALIOE+Xfpl8Dgp4AvjBrd7Xvo+xpmp3ule98ltaPdPBKidXOKA8gEWDJnKnIvG3Z0hVYdbE7h0/oOkk6ekF9+mVewyu/5Pe4dFxsM+O41HpoW8NOkdw6H+tLZkUp7fbw3pLn9YraC2dDpcHoFMbNQH/6LxAX3CffE+e773CO9O8E+63NI5AdJTD3x4j7254jnmQWFMC1A704S4fxAAAdJJ7D9Ep5MpyCm7rW/rO7J8BKncaA3aCfAbxPoXZ+4LT03dNQ5C00/X3Kn93KTAbBAEIQyhv7BiEiO95rm1NGITllGZPH4B49SZcuzBywj9YBQHpICyA/MkZEXAUYP87dFIGzAQZ5pdZ8n14NPVOD/cAbUGf6r1CZ5ApU7RUID1BAzSNASh8uouCEg9gDFT8QLgKrfyhzNTaPhW0Jl9k9zj4nQeeD7/H9l2XSX0g1QJBBrDsJt51vf7h2Q89n74CyiZTNt4n/dHdT1uh35egv31L7zp+UD1I8niq3r8DBwIBCOJ4YtWJoyrAM4n3DCAQCfdC/fqotY9i/qHL1z/18z/8tZb/Xj21P3ruKxTWdV59heFHxXsveK+AIWAQI1HuVY/i9+VRlb68Z9wXoO+XKeO+ZP6X7xn3hzUekH2F/pqefxDxDPCvEPI6f51Pj8TI8aYIfn4ALOwX5vIFn55+Sw/ed38/g2Li2ngA1faj8LwPAdUnKL1gGvwoRNVUvzpQMu/MCyz8ln7ExDNjJgYKpqpZZb/L5HsFBh5+OPCjQIBHaQ3Wdqc+7rHXiSf1K+/la9rE8eeX1Eq8v7LHmaoBCF+AyrRFAriD/qiOvPvVR680Xfxxd3dPMsAObvZ1yrXP0NTXfoY+WtTP0Pum4b4fSxuwa/ppao+nJcFQ8ONj7MfW0fZewHatHvLJgsdOaOrKnt3yn5WYUgxo7HhThc8+cnZa8U9CwJcg8Mo/C5HvX6z4SRyA4Kd6HdXv6V4BPV3Q/XyGgA9BGoLMAoTZgAl/XgasU3qA9QHzTuZ+x++7WdnDlt/uMNSP7eSvL+8E8vTBs3UEw0Gmfqmm0giDeAULgutHZIFn/62m8ikL0B9oZIAw1MV9b2nh7hzFFtbctT18SdikZSGWgzmkRboY4eOWOydRl/Ioz/MIwiXxBWGjC5dCECDvEatvUy8QTfqhluUsHRLBXYq0Fo6HzW3M8RAUcUnMmxMU5i+XHg6g+ph6A9z5NPph5IToR387gfO0/dcXe4GDkRxe7ejHh4Up3VrgpN2HxqxceJf9dTZP5qFGiiojpJ5oS2aJzFfVdtukqk0fEnZN3CJTdM6B3JxrpNJob3ebXfhZjI1B12bNCcmPkbC94ZXjLBzZ98fU2rI7JnLRed6agr6u9Uu0ty9HM0qEeXFAtCQ5RZQr2EWHn5fVUidSPNMinspg3w895UgmVcmz3q5da4yt7EIjUwyk5YvSjg6xW+4MOVzOC319a41jPiRVQysmye97V9DwG1rfhvoQ60WjrwIrPRGUl3IzSjkhs7PUw42I9Nos9PYoF6xdj9Vjw0KUAvRfdkGet44oqJVDZlt7cThwelj0Ansdd25Mio6SCusjgeZhoK5votbooFacotmldY+EkCd1eRP7khavVa0KehjWprAwNC5jI2Qo57kgJ1rSVGI1kMZ2jlYREaemhKFbzSIMUdlsI32XMMOVVw5Y6PVELPcbIZd46waHmaOVJmWn/IYqe3OBHqkMX9IExovt/sZvA3yQxnhPVTzdYl0cF4bp7k9qvTnJgsmMpZbpUQgbVcjHqV4diuXorGlM48b9tdK3nX3Ki9W5NaqUPSaKIBxM6eYvZY9EElePL0JfKSNCx4yWye5hveLnKlqlhV+UvnQTQISuspPTKSdZtNuGOuRRje2NcYv7Vz1Ae7qoRolU9mG6qkxkwwg7SVXrFY6PyyErEPQY+CLMLgunWdM3dKfDQ785q80YDKANsPf6ZYR7aV2GPkNF0X5O7h0nHE635Ubk9us6vy65MUQQf3TOiyLIyHQ5P2L5FffPm0i6SuuQXWipftZMSbbmKGwR0kXrbnheL8xE9pChwGbrijIdnx80X8VniexHqh/GM1Y/t7XMZ8kK8VH2WM0STJlj8HVvHEKvWJKyRN/gBNvVuJAQx0UhD9Xukt6s+FxsDhuOZDt7E7driTd7gYsjZG2xYzcU+6iOeYw5iOiG5wyhWvbtMvW8ZB2aonc5XzXqeLwFORdwGRYVu0S3pF26u9rr4+2Abo/Slm6TXRTGmtabKXObryKzUUzHDl2jl5YEN1+a/HjdHpz5qMmsxZLMmuCvolhwyh5dKSMf6bPVMslGX9LQQTihi4AgN1LhLGtRNhTSgYkUsYtD32lR5PN95l6rcnYSLq0fb7kzyD+m2qHNgMaxfpUVK7se7OPSlJfskuqWrqS527TNKJw3JUJn0nZrkOttgmjFdc77+jI8rjDYpRt/sT9sDQyj4nmk98Y17LWcbkcxjsNTSZ7TjR9LopAxh/yglVdi9JBV4kn0MQ7KWDCPsm4Q0iyiTDjU+M3IyPMNlnn+WmbkSxMjl1SMK/bkRyZoZOe3jQjjVCjE2yw+wpfdXnUs7aCmuRs3/riIuZTjdtySqmiE2FU8gp45M78eQLoOB9EJjLOWeLKJjKUo6PTx1lDlWvA1YpDXEhkndLOSGqOHOd0s5glGNME1PeUr0juZHj9rBpNnKGYIyn2zZ+VlXsGIdDXmUUJpJdo6fe07QQZ7PjzEMdwwh9YVh2zjWgkbXbsEdUezOPpn1vXkKFaaY7hR5pYYeQCxuog3GcJUlagXm42ER1Y1Kj2pLdkQY4/8YMdnrpyRnLELhDxf1COeD7ZSp9J6pxWSespoPFftfL+A5+vAivdMZcq6QBPH225t3KRik6Mz25PSjtP7Yknr46kqeMFMMlreSBV7cAimC439ko0P62tqWWZ1lFN/QefcNW1kYwfi296vxEtpDbU3R91EDlC3N5uduQAuJuvUnF1qg1iqx2ZfX1Y6iqVLS18Q+dLChBH1pG63Z3YLPV5xMFGsTwSmOH6zCVCZa9Pg4pf6MmmR3UZTuJZAFqqysbvSEqqOxJCLsy5Cs2L3sbQ4ELurXBbcqSD0XeperKNEzdqKiNc3tGPFjNcceM3izKVMyCzK55ebd6HcwDppB8k+E2xcLPNDURUtoSuL6zy/CtcidjUB9fXEBqUj31zxfDFE22hrwO0+QQq2McpZ01NHOw4wZNcdNKTd0lQxiMG1sC8bfg4bBZXvxeSIEMWZsRnK2FUrtcuu6DFxzIWRkaeGxqo+Hot+c0XZOFkTA9Hn6pzUmr3bF6R7McsrRxEyYTcMt1srzDEcrVN2OWiYTImFH8PuyVEpcXXkYdYkOXy5aXa9u1xFxA53Twmf0adeuabw5kJr9bljHdtDw6iI1GAXspkn8GKy2jAXsSTwNVoPEaLfurjQ6v0N7/MrN2fSU2isijIuYzgkVVDVNZLUs1rPh3DXVVeHlrt1SxMzwQQ845qLSjnNbqG25gRM3eJKURSxVPfCyBxOSi/ctjUbmTOsVcaFg1kmd1wfVuKV3s/4TOXCxZbwrqZ+WzC+uC730uEiGonDWHSb1vVqLVVae27TGUYlokPp3anQ4zPdmq1paNE6HBZbHNleVmXa6n2vWHarHqxQwrVcgNe1cipiflAQKd5seBO/mit5I/hnXnXnlDiv9qIz8rIl2vvtDORacd5l2bzbqBqnJ7rorQN1x/Pn2VGRkXKhDmqoqStkPsJkhCKYLN+SOcXtGI2KNSENlski45yhGIsjKmbF3g5OO3WEZzh8RFrkGtxy5ZyrAkn3MsKN8wO3qk6UpWLS3rVtBUuG4mQvHHTfHgIi0fIWJdH8nLDFIevoqsQyO6LX+rnZ0VtrNTdnnCu0zkpkQh+/arwUbZkwkbPYaccllV2YUly3UVvoo1SvZ8RQrlTdPYw5e640wECIdM6DRnFJtT8WoUe5GlnqEaEfEmlG6IKUzPCTSs8vK3lLxrVjHXd4hhuntcvm6o1PyZC5NdwxYTnlaBa6lDi7zEGZw+6Q58GNXuTEDS5EQzwSJ9Nd5av9kMwDf8Bz2G+uKzzGdwN6Na1Vf2Vte6NujSGMBSJb4V3pabd9dWN5z6pWtcmu2H1TrASLzmLCCYt8qaImPh6vIFSHDDHKC97BdKn6miic6kQzbrO9rdG3M8W7iRSB/M6Is40JpnepdnFN1J5EpctRY6hM7meLlbtHA2SVoQEV45tG5PetVeu8mR2o/mIzGFzkgoDIUrEgrydSd047bDgieLlrG7/Xt/ZsHqSbZtHtejve9cJaC3o5LKO4u7GMTOasxfRZth0SobHR804+JsR5DOI1Q6aYf3YvTC55lOIWKrN17YOxXJ10jRrcfozmNYMwSIrktarzqjHopcYoNw45XQXNBtyJBiQepL2RN6ulZa6TJHNlgZd2t62Tg2Yyjq8uHpHH3DmGhYptLRLXBbvOL5017Lo+wHRsIHJjf/HX4jZex0d7Vuw75ujDeu8J2ibGCjdNiHpZDLy7uZrm4rLn7QKfq5l1DNzcAEBwSMAMdGE6S3Qucc3enLlsOkelgNuuQAzhnrS8kS7qSgWbMldl1Z0TUxc2ZD9qKDn3HZI6XE7VUafpoAGtDHwKhjQQh91YLURb0c5GqeBs0JnW7FbK1ppdRaN9VFhSip3CzipVDnBBolFpw1ULumAMw+ot5pKZVcrHS1NLbdjvjpI+uHOV72jB9AkPNJI7kvFRZ3Vik0yrDg5o9mphcGbVUdxLbDla3PZyTmQu3O4asZqPVpU0PizUV7IKrGih3wQppXejLyIztPYWmUXKM7czmTnHjKQxHqWbaOBF0kmMQmWMt/UlBK02CianMizgS/i0H/vFBnFnmJXmo2e4zfxwo7C4M3QbRsXOSd1+7w6EQ95QVArt7Yy8WkWipqmd6sXBzRem4BLsljsQewpsub3koIAWdWOXzaAY9qhj1bxX14buHHZWc9Hm/Z7tlBA+L7s0i9KY22dFOTq+Dnf2SqYDOvfjMkiryJBajbqmiHLmFW3ho1dH5rgD1u3t2TEiY4v0z91NSqnU9lx1YwbwmMkSCI7QJZvlZqEoPA5fwB5vKfm0SO/lBQbPUrivCd/GmsoLddi98NbQHrrU4ZrNInP7xfHa1XyY0PncUKTL2m6v0YkIylvC0phAxXosUYEky6C9VYm1G3ja2Kwu4vWm9CbHYK0tSWKNyTMCFTSsLPeYl2dLjk0tAdVP8kbNCc9oWcfRUfU4Cqi637eBjV7FGh/OYufFHsYZI+3nGK6EjdMEqHNAfG7LdbJbuxjKwJwhNsMg5Qf+QqmnFXzkyqaTnK0tMpcrPt8QWxf07+cD3JwzWEKMooXLdOZsizWISHLJ8hdGIHfcjVpu+rliy37hJVaIkkZZB+J6tyXZWl5JtoFVrQhb0qIJrA0WzjICX1xT3uAwX9iMAejKaNgh27TT+OXuuDCCA4vNd5F7kClaubSbBYPZxmiOPBM42XYzm0W4VuPHVtksqaUWKNiGu271ypnpTEDt2iMfkvPN7pLAtCidPd5dNJ0xBnvJ6pMlr4zh2cSWBmjMCBACl0O0WFEqd6nQrh6XVwer1E7dJHXAJgzHkCYubOj+du4QJpz5oMM2jtjutOop3mcsbYdtlH6GBSiuuJQbZWf8ZA/uDVkIspMHlRdwpt9YZrBcx2rKWr3LzUQnjWCk4zzMIjgzxchAMYRrxG3mCqt0JV10LqgSiCuzHE20TJ/oHVJiJNE3kuc1Pdle6C44r2zNdxdS3yzW2KkZeCxv4oZKrXrYnjMXhzeEFw48tbJ7VQqx8BjgO362unFtt2qktbrVrrNte2hcTjSVK05tyHVi+PoezuCLwyHyYn1eqiu1rMlRNTYUaddwlgdYQpYtdl64CDzOO7qPaBjzObjUFIE2GrEb+mZG1iWVqJhf1vQFKEeqHD7i6GLBtRxdzVoMX8HLTnNwQnEobG+SC8dx1creyYssj+jLUtJNxEWNWd7jXIYW8KU8dCDp0Q3YQ/M+0V6YjOaDc07ije+TpLFebTvJcIJwgZMncm83tuGJvMVZJW7lq6S9nLeCfxjVjqLlFbqiFyzDJPzN7qqOWskYrUtSu8VWJiXVM6rme345X26KirlsbyrmzIgRUbhq43HXbjZYWMvO4MA9BHjGUl2obPpsuxzDrosKX1g5q222deRLcBrFLrNtN1HUIMe8KM4AW+ykPq64K1laowCPlIDQWrw8U5w0tmVjr9DmdHTt8SJisjgbsB3MNegyOHDdTLgYM10z3GK3sb1kttnzqqIriZfMPZRMA6I82Z3j0dhp3VnCuMHVi2VnSubwsjLfsu085FPNO7h9CZ9lJaNnVHWt9klJteMpHrbcBZ6tLu1JItNQUGn65fPLdDz9PGT+L71dnk77/scOHR/ng+8voe5HzJ7lfr2v9fW/pt7Pn19KJwLKPQ5cq7gJnkeS/+649ctfeY0xSRoeL3Knd2h9/X5eX1vB9GtKL1HqNlVdDm9VFjfPGXZTTb8qUb09D7lf7sYm+XRi/nvjnmfqb3X2tGi6c381mXhu9BgwXQbP0+jPL+4AXBg51Ru2IN68Mp+sfr4ZmdwyvRp5+e3/AfSvOk8MJgAA -->
