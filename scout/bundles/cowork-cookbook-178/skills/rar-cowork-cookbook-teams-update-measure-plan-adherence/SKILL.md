---
name: "rar-cowork-cookbook-teams-update-measure-plan-adherence"
description: "Drafts a Teams channel post on measure plan adherence status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_plan_adherence", "rar_sha256": "11689a152f92086939b328d7c67a730a5730fed9309556a6328c578109564c07", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_measure_plan_adherence`. The original RAPP
agent is preserved byte-for-byte in `teams_update_measure_plan_adherence_agent.py` and in the RCI capsule.

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

Measure plan adherence Teams Channel Update — Drafts a Teams channel post on measure plan adherence status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-plan-adherence
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_measure_plan_adherence_agent.py` and embedded as the fenced Python below (sha256 11689a152f920869…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_measure_plan_adherence_agent.py` first:

```bash
python3 teams_update_measure_plan_adherence_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_measure_plan_adherence_agent.py   # or on stdin
python3 teams_update_measure_plan_adherence_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure plan adherence Teams Channel Update — Drafts a Teams channel post on measure plan adherence status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-plan-adherence
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_measure_plan_adherence',
    "version": '2.0.1',
    "display_name": 'Measure plan adherence Teams Channel Update',
    "description": 'Drafts a Teams channel post on measure plan adherence status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-measure-plan-adherence',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-measure-plan-adherence',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7da31101ee93b763',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-plan-adherence'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-measure-plan-adherence', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateMeasurePlanAdherence(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMeasurePlanAdherence'
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
    print(TeamsUpdateMeasurePlanAdherence().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716e5Ob1pbvV2F6/ogzslsChACfStVFEg8hQBIIhBSnbN7v95vcfPe7kdTtZJIzczI1dWW7LWDv9V6/tdamf30xmtrPypfPL4pjpBBrxHHgOyVkpDa0ybqsjMB/WWSCf5CVpXUZmE2dldXLxxfbqawyyOsgS8H2bWm4dQUZ0NkxkgqyfCNNnRjKs6qGshRKHKNqSgfKY8DFsAELJ7UcqKqNuqmgLqh9wBIK0topDasOWgeibCO/f9kYpQ25WQkVTWBFEBDB8JxXIIDTG0keO9XL559/+fgSgO8vn399sWKjArde7nKouW3UjvhgfgS8qTfWYD+49MDCfAAWSMF17pSATQJu2Y4LPa8+VE7sfoT+4z+izii96sfPX1Lo+fnyMv2RmxSqfQeqM6OqHRuyjNwwgzioh1eIijtjqKDSqZsynYxTAelT7/Wx8zulLId+mp59eDB59Zz6w5eXDIhgTOb98vIjBPT/8lI20/fXiUr+4cfXOOuc8sOP3+lUjRk6Vj0RA1K/fn1eP8mChd+XBu6d60+A6sORpvPl5XfKTZ+H3JOeYOfLa5gF6YcH4bzMWic1gB0//PjPyFq+Y0VxUNX/Et2fH4R9x7CBTk/Bf/x4N/Iv0Oyp0DvNf852irC/owlY/sbuI/Q01D+jfbf/fyIdB6lTvVv8L8n91YbZT9DP/1S3/2rDR8j98rJ1YpAapWHGzmfo16/Kkd78/IP9/eYPv/wGSP+3ZJSsKa07ha+JkQauU9Vfv/78Q3W//cMvP//Q5CDWQCJ9bcr4r2j+lV3vfP5gweeqD3/cC/iraZRmXQq9Rzr0a5b/W/nbK6QZcWB/v199hn6fL9NnBk1KvDF9mOB3OVMBWX9nxx9ffgMQkQJtGuv+GGT5v/87JAZWmVWZW0OKlTU1BBxcB4kzCX/2gwoCf6fcLh1g1yoAhn2uA/E/eXiSOHOhb//HukPlJ+sJlfN6Ap+vzR19vj6x7x4bX9+x79srdAakszLwgtSIIZk6Hr+kANrSemKbl07llC0AFHOonU8Aij5NXwBEQt/+Bepf74Re8+HbHcqDB0bJm92ET1UTO6+TjhffSZ8aWQB+nd6xGsAjziwgkBsAbP0IdK+yGMBwPdmjioI4huygBMpn5XCnDWz2eSL27ds306j8L+kDUFHoUR6qOVjwLg706RPQzI0Dz6+/pI7lZ9APv/72A/R/of9q1534xOMIsP3pESAhrxwkCGRYk4BlwFnAvQA+7h759benfQGZFNQz4L/ADZzHZhChkWO/GVvhqE8ItoJMBxgZGDjJs7IGKA0F9Su0c6F3eQHT6dGE4/5U1mwnd1IbWHsAVA2gzrsl06yGKhCGlTt8hJrKuXP9ZpbGXcQEpLpRf4PEzRFUjSwGPyYx74vA5iwNgPnfQ+FxHxApf6ig9RuJV0iaYhLKjdLI/dJ48nCNh19AtXjbDogbUOp0X9KpQjqTqe4J8jAPWAQsYz1d+mnyOajzCUADu3rjfV9jTLXtfK9x5Ze0ega/UU6usEAxAEy9JrCnkvCPZ0hVftbE9t1+QNKJ0tML9tMr9xgU/7ozeLQRm2cb8ajj0JcGWcBL6P93rzGJSbGsTLPUmd5CtHSWrw/zTS3RZOZHFwVq/n3zPVW+9wFvKPIGpl/SOACxUA7/eKy8G/255gFQQHobAIJ8pw88Dsw30b0H5BRgZTmFsvElfUPtj8AYd4gC6oPsBdE9BdUbw+npm6Q+SNHp+nsFvzsQqA1cDoIOyhszBgHhOo5tGpMN/HJKqqfpQXQ6U4J1fmD5f9AKAtRBEAD6kw8C4B+A7HfTSRlQE+STW2bJ9+XB1BcBKezGAtJOTnqFLiAvptioQDKC5mZaA6zww50UcCuwMRDx3cKVb+QPYaY29SmgMfkiS6Zo+Z0Hng+/R/Jdlkl8QNUAsQVs2U3gajv9w7Pvcj59BYRNpty7b/qju5+6Qr8vL//4kt5lfMdzkNLxVJl/ZxwIBCAI3wlDJ0SqAKokzjOAQCTci/Dro44+CvW7LJ//1Jt/+Hvt+70yqn/03GfIr+u8+jyfP6rZWzF7BXgwBzES5E71KGyfHqXn0zPRPk2J9uk90f5A+mGpz9DfE+8PJJ5x/RmCXxevi+mREFj3jH5+gDU2n9bXT8vp6ZdUdr67+RkLE6DGA6ik79XlbQkoMV7peNPiR7WppiLVgbp4h1fgiC/peyg8E2XCG28qjVX2uwS+l1ng2Iff3qsAeJTWgLc9tWaPuSWexK+cl89pE8cfX1Ijcf6leWXCehCuwBzTnANSB/Q6deDcr977nunij5PZPakAGtjZ5ym3Pt5x8SP03m5+hN4GgPtQlTZgAvp5anUnlmAp+O997fvYZzovYOaqh3wS/THVTB3Ws/P9sxBTSgGJLWeq39l7jk4c/0QEfPE8p/wzkcP9ixE/gQIA+lSNg/otvSsgpw16m48QcB5IO5BJACAbsOHPbACf0gEoD5B2Uve7/b6rlT10+e1uhvoxGv768gYYTx8820CwHGTmp2oqfHMQqIAhuH6EFHj2P2kQnyQAyoHuBNCA4RVBGjCGuCSyIFYkSpooQti4tcINHF0YGPjhOjaJLkgMWxkr8NDCcAIGl6ultcABvUdsfp0KfDCJ5YANKAkjlo2uEAxbkjCOGKRtLHHDsBcEgS9w1waF4PvWCEDkU9eHbpMh33vVySZPlX99MVdLsJJbVjvq8dnMSc2YI7gp+8JMX8z6fr70G+yS5UIsWFYZq5LdWx5rSNxW2Xe5fuXdSKkLY+dHjaFa8PZ48meZTEZtndi5E+1FDbjN27KBsut5xE5vc3fcdNpa5DL/tk+K2ykTsUhIDEzLXZ4OzvbezLqlblWEhqXLOurj0pLbdt4VaSwPF7nyOVUP9mK5gffCrneu3QE+Ck3IBZfaLr3TxYZXhaIYSBtvff5mRe45uWhBoskgI6RzgDH6JcHUhsnso1AhbnqrMBG9LeY0YlUoRs6AOWAjME5UiHeXqkh12dBL4TKr4T4bBk1gD4WUzhhj22xiSVc5RzXMUIlNU8ZuXXE+xoq6PfFbjT4TOjackzEec50xj5qtBA6MrC1Ny9czm2GxtMjPW2S9MzD1dpbVcVlGdNmCgEUOWolYBpJeSAGpgqDRlJHf57fdZl9VBOcwGBB2RatNvIgDZZbUnSKBfvlGl6oyMqSWpaseJtdbX7/MeKmu3U5BWbtDTu1mFugloQz78GqLZ6VmROyYdPIQJfWGsGEDLvjCCqQglnUdjDtwT3S7MZPrBcyUF+FwyW+XqNhgN4lOEWG8qtwWKRdEvu90f5nGma+wRRctvfBgFizsSmprHhzzoI1jxp5YLHSaRNdbFdvigtl4Neg7ek7w42Ad2yl+UW7hQTDGgN4sdtrNN/hB1vuiF0Jz358qQh9l7ZTRSc+2M4TKBmZlMQWaGwxv9fMsCeGu9GddzxlScDycMH44sFqYsJfBH7YY7uBtXgi2hui3cGXyZtdbbrvJpVCk1+xKY28XFcEkllitCrXJ94au1jSSHxO7zIV0eThwK47pxJHQSYLBltuhdlfL0xmeI2teXaU6upjPleoiz5zCWmFjOxilubgQjGLkNpOYieLwGJtrhazK8qwLaexm+tv9xVI87CqdWI+udl2uaKIvLXMws+QUji3wTDArfMz8K6ugiZTBEqXQ2pI+bVU55iJxVPY9K/XisIup/FDRWrnWKUUTxCoPxsO2rzi6bOwhw6nVvN6vbk1OXucL+aKT9OgT8kyRivmZQY58B+odmlYHjZyPo7b2GyQ6z8MdukFvBltZMorPR0txRqaqeZrmert1U6LWOgMXCJPyKMMB4JYM61Ixwk5e4l7vMXC489aa185z9ow1Q57NSBleowMbKYFC6Gu32qIlu09gtfAXkqsRPiMt1iv52ix2Cc+FI3FZKYVV9p0VXDy917U4PJf4JY3dut6dSieDswKWCb5J/P54pNn4uif3iRrG2ursZa1mFqc16lwF42TNtsKQEreSXhxKGqPPoXImlLIOB3oZ2fphxau7Hi04jOaGXVOUm61txvCYuIcd0eW3Ze7XHVXnNXMsiwDDLItfBLm8EyrGWFXjEK4bO5dlyjAuuu14g4+Jh66uxSrlTnxoOO0qMiQnvQgcEqlIk6UXYDjyiOXrgB47bp9XxY6gliJ+mQ9kFotw0WfojKDg7Igf0bGSF1u0k6VVI9JXdOPuN7tBqm8bbnk6lj0ttqTCzPNNQFpbCrMOQ07dyGLLm6nApWaxWbPnaM5oJCFw4g5L5VMuEysBQ8gNnsGE61yNY4AO5rbmRoq5RbuORdUCPhkCAZLR24yrMTI1hgp8fneNluSVyZCwtOEEB8N4eKEUeD8sC6pAwlPQ63E8HUygtr878dbek7s0Mfc+f6702F2a5DiiXS4meUjesrW/72y/IkW7JfCg3Plpfmir1cxJbwPppj0j1MyGWdhreEY4SzEbeXuhOebxuuR2XqmmZbKyDu6W3lZ14171a+BtjlEQn+YNipOovkrmx2Uwd44htb6WJiMo3jC2Lix3ymkTblTjNORcVIgrcbc/akNxExOK2EokTMM78gxTsr0uyngZnJfaHmsSvrBZnkuO+jVSYfp82bWUutl28Vq4ns6I52qqJicjo627eb3AS29OMQcbkdVThynj5dRUM/RoNGU5CLIK3/gNnUWosyBmQh3UDO3IQieElBaIB4xfXVDBsZlLfnZ4BU5qA6BQYa/oDbtOr6M2FsLmWJvVldcZrerjXujXQRJoaa7CNUbHM7fnQAewrst9Mm8DrOkxxriZp1kq771wf83V0b6ItZCaR9M6WydLOCv7+XjG6WtHN9e+arUG39kBL55viLid1UdnE1DmJR+SMVrg5ElJ5aWhuIyqjevBi4MF6qKmHGsmlVP8VfT1zgzXi53piIpzEtm8WQ3cTPcP3U0sNbU+DedrtJabq4GrIzUg3tjrB3lQbkc4W7piAUJNyWG/xUfbRqLGp0Z0noo9gDdiLYuocE7yqi3tGyfTsoAFnWjxK5yEKQxdIEbFH+1FpZ7LPuc8e39DhB1HANyTTrNBqZX2VJrIskILPzDlK+wJiIlc4F28n1tjZYTWejGm1e3GwCXa1LwvrVRZuwjlLJQ358Wt0B1+n7Q95UtRHq7DY7Cg6out+XayPWgxZ6/bRFBXsQHcoewlMyh2YYbvYm6nGEck7udmEOZnkqb9HZOk7spEZ71wCo4NHg+SIKzV3t0dzYBgFxEXra5wcUn3YiFhaTguUJM8oKVfUifjxqyjve25yfVsLXehj2ANw5sAzGsyXGGXi2wWri7Ob8GNvRQpi6K3ZL9OZIDJOV7ddHu+owJvd9pft6cbypWspOZXbrY4RPKVr4td6u+5klw1g4rlq76Utp5jnYdqLON9a5NMdDxGvNHJBbxXwdy0yVaoPdS7QsMXUpjULB6r7AnNa3UBl6V0XGjoqVqzZW2OiiFddnSEcee9tdmIo8UTfWeokYztt8cguMXrwN15KsLf9orJ7OVt0SZnJwPNuxBL2Yjy5aFjicZRFjF57UYKC3Sv3pru1hCskY3XOrxvVTimBrkjWn1N86xyWzfSKafmawulKvfYDhsln+8NvotIy2944rTECJMe8Wo57rBTebt281Npz65nNTV3fWoY10HasCYd46ols5rmioPjaUp+gYNLF8O5ieoaf+aVQOMW+M67bQ9dQdie5IvsaeSW3fIYmnRtFZdK3TnLmveSeRTFkpFyDttgixmihf1uNlxi5ibNO2wTjSDk6dkeK4waroQDfwqqPd8xwXFBs/uLEG/3PgHqxxDtD+bmAnqqATNgT1M3vI46F5AwilFjLuqFWyvo4nZptQWGR3Ub0nzEhGYcwU69h7HTZWBGzW89esbDEcWii7A82cdTNei+Gt/grakXPLHayUNwkrE03scXMHt4uLRL+oFbhleVn8dOcZAZdqiua5S+SkQF6ws85yjDjbZMHIWKyRfiIajI2U6Zabv9Gt3YecLDs6PCN9wxIG1R5KRaNXfqNj9RV9Cc8B6L3hpqb9sEfhU4h77ObCqF19JCYls01gMTJ3nUrIabGidr1uG8uhoztZxH+7xGs32OrfwVp6t0tdmQAAXIw3bvUA1dSoFs2mMQYDyqqMxojIv4NvpIdzVNQ8b09UXft07XU6utV6/WlbI73pAgZBQRASnen0bzEKR9rEgtOV/vJJ1HZSrM1lsh3G8BpnDmkRw946r6a6XfjSvEvm6CqKk2u4M4xIN7oIe6chDm6l31+XLYVwUoGHsmxFHckmy6zI8Gj/fKsfFAfUiupzW/kkpHOdeeaayi1W5ZuPBJjsSZJQDU5xrG0WbALfOTgPcrDtFmYIIO2xavQTzeOBuzWP3SkgccYWBry7kNyp8kqTUvfltduV5VFk1v2ea51Ogwn5Vrj+mcs3vKluw8VgCYOEm3ynrUFI2MSMbxIO6CUrlGmHw8sGWTxdlSr4Ij54/EviAQvbPQY7MyyWqzbnYHsnXpxhRFnDsW+0p08pE09qelZXMt1TcrR3AueC2ZmxPiInaNIZSdUPODt0SpeGTRBu/0jLBCdGXi85lXklkTCpV0wMt0xrfCKrFhGE1dPZFmVrqI8spAotbjVCPKiK18zXa8zeDDfn0Epq7m19tt50Us6gaX0c+o9TlshpE+nLglF4tmhG522JZIbMwWhvGszOuxTZygY5HzTTdhm/OWJ8wob5q41DZljB0Ivu9DkYoTbRFcby51ZA47E8+pdp1syOaojie3PF65sBHbjckKkV53PoGmpskQoV2U4xHMasWCJ2Z9tJ4PxxKhqHrLx6Hoz65BVTlH2WlC12rl2Tlv4eP8coQNSeVvi0pf0MOS0pDrkTcBpGTOonItUvQZBNfD2hMOGYswhpWAmTe9WfpsYcC2tGTCepbly1WMSjqXtrtb6EVZR89rPE06mp/xAaJ6PbVYXANXvixa7hoyq3F+0930SnuduBjpues3e/YQlJy2IC2zc5sO6MdnmLXnNvMN4p1JtNqfemlGImpNnDGYzLjxJDLGuphlS3RTce38hAotOnNsn5Wyo0bZwXiFG3fAEyLYbCiiFwNlqZR2jtNDZw0CdfW9UkAXRKaTCMtdk7Dt/ANdFtpy6xZ2AbRysI0gytKyGSySEUTVMwT5TGQIarUOCYMBHIyybbUjF3lUybMmgxETPYwVO7dMZrG3slW19vTq7Al66Jksu21HMrRgDxSBJW7jF2JA2faoXW1EpJZXYV0XUqOzS5TcmJl+o/EFqqCOWV9u67BAtUXPMWi15grc2WzF44liQGZu12lOopdE3OzXxJYjCpvDVTGMZly68FT3JpG33rFw/4DkWOehPmVwblsW2yVamjY5B71P3M5Te2/P5r3pntnddl4T7qw+EdnWgV0KZ0s8QFrY30qzbHHYrDK9mrsegHjccohrMK7AVTsfeDkMI7JDrT5tc6z3N33l4Z0v0xS2vMhgar3OcI49OaHhEz2SmpLebjSCW9TzUK6TtD4vnTLIsXnDqLJotPhlSVIatogRwXTZxNI7VkR173z2HPnGNDbBkVyeIR3pdQff8EKqLIs4xVv9VOfpQNpXNMZxhywPepi2FYYz162cXVCSIyOhIupTjx+4nogYeCrKNI5uU4oJvU3DGb5pUtx2JV5y3d2fLVS6SggWrI8g1/yqgSUn354dvLl4eGktHLHyBteeX67c/AgL5+VWWEbLA5nbCjHQCKKfbGF+803QHK1v8XyEjcOS9XZhG8fnJlTkYljurWKusUE2D0BLqJvHUR+ogwsPS66gwtC/2kdjQ28kiRloGj+ey50bgC5FxphtkhIK0YUhtlBQ0ZplcrNF80qd1UtyTe6QIyI4QURR1E8/vXx8mY6ln4fLf+eN8XTY97925vg4Hnx71XQ/WHYM+/Od1+e/JdUvH19KK5hkup+uVnHjPQ8i/9PZ6qd/4R3FRGB4vIqd3ov19dthfG140+8TvYAhp6nqcvhaZXFzP+D9+GI21fSrDdXX50H2y121JJ9OxX+vymT6rHQso6q/1tnX5xn6/X1j4tjBY8V06T2PnD++2ANwVGBVX9EV9tUp80nb53sPoCTyuniFX377f3fKNAqtJQAA -->
