---
name: "rar-cowork-cookbook-scheduled-brief-correct-synchronous-integration-failures"
description: "Schedulable morning-brief email summarizing correct synchronous integration failures for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_correct_synchronous_integration_failures", "rar_sha256": "b9b47c05691108221d633007ac058e8bd4400f7cf1df61f72c5aea403b6648e2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_correct_synchronous_integration_failures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-correct-synchronous-integration-failures:e84a2cc19591f47c21e59f29ea86ba7a18c2d321e74be02d582ba08cc6fd0e7c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_correct_synchronous_integration_failures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_correct_synchronous_integration_failures_agent.py` is
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

Correct synchronous integration failures Scheduled Email Brief — Schedulable morning-brief email summarizing correct synchronous integration failures for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-correct-synchronous-integration-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_correct_synchronous_integration_failures_agent.py` and embedded as the fenced Python below (sha256 b9b47c0569110822…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_correct_synchronous_integration_failures_agent.py` first:

```bash
python3 scheduled_brief_correct_synchronous_integration_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_correct_synchronous_integration_failures_agent.py   # or on stdin
python3 scheduled_brief_correct_synchronous_integration_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct synchronous integration failures Scheduled Email Brief — Schedulable morning-brief email summarizing correct synchronous integration failures for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-correct-synchronous-integration-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_correct_synchronous_integration_failures',
    "version": '2.0.0',
    "display_name": 'Correct synchronous integration failures Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing correct synchronous integration failures for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-correct-synchronous-integration-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-correct-synchronous-integration-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '39977320e999647f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/correct-synchronous-integration-failures'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-correct-synchronous-integration-failures', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefCorrectSynchronousIntegrationFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCorrectSynchronousIntegrationFailures'
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
    print(ScheduledBriefCorrectSynchronousIntegrationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOjSJbuX2FiHqpqyEyxiC3a2uwihBaEQBKbRGVbFIsjQGxiR3Xrv19HUkRmTXXNTPf0w1VaZCBwP/v5zjl4/PriNHWYly+vLxpwMmTpJEkUghJxMh8R8i4vL/BXfnHhD+LlWV1GblPnZfXy6cUHlVdGRR3l2bjdC4HfJI6bACTNyyzKzp/dMgIBAlInSpCqSVOnjG7wPiRUlsCrkWrIvLDMs7ypkCirwbl0RmpIADc0JaiQIC+ROgQIvC7yrIpG4nmXgfIvCOQenTPgI3WOlE2G+HDPgMD1HQCXZPgCBQS9kxYJqF5ef/7bp5cIXr+8/vriJU5VfRMY+LNRSuEhkvZNovU3gRZPeSDNxMnOcHMxQKtl8HsBSihkCm/5UNXntx8rkASfkP/4j0vnlOfqp9evGfL8fH0Z/x2gwKNede5UNdTBcwrHjZKoHr4gfNI5QwVVrpsyqxAHqaDRs/OXx85vlPIC+ev47McHky9nUP/49SWHItxl/vry02iNry/QOPD6y0il+PGnL0negfLHn77RqRo3Hp0BiUGpv7w9vz/JwoXflkbBnetfIdWH813w9eU75cbPQ+5RT7jz5UucR9mPD8JFmbcgczIP/PjTn5GFPvEuSVTV/yO6Pz8Ih8DxoU5PwX/6dDfy3xD0qdAHzT9nW0C3/iOawOXv7D4hT0P9Ge27/f8T6STKYHS/W/zvkvt7G9C/Ij//qW7/1YZPSPD1ZQ6SqIXRAZPoFfn1TduJws8/+N9u/vC33yDp/5aMljeld6fwljpZFICqfnv7+YfqfvuHv/38Q1PAWANO+taUyd+j+ffseufzOws+V/34+72Qv5FdMogByEekI7/mxb+Vv31BTCeJ/G/3q1fk+3wZPygyKvHO9GGC73KmgrJ+Z8efXn6DsJFBbRrv/hhm+b//O7KNvDKv8qBGNC9v6hF96igFo/B6GFWI/kzqX7TNWpa/pP4vCLw7pjuECKdJamRZjogI82H0+KhBHiC//B/vDrefvSfcTqp3gHq74+jbEzXfvkPNt+9Q8+0dNX/5gughFCcvo3OUOQly4Hc7xDmDrB4FuYcMROPP7SgLlDN6YNFBWI84VEGOf0F++WeZv935fCmGUemvGfSiE91RGqRFXsICAEHaGVHNHWrwGSI0RJ4yTxLX8S7I+F9TfBktaYUge9rXg3UJ9MBraoAkuQcVCiKI6p/GqpAnLUTR0erVJUoSxI9GKfNyuBcw6JnXkdgvv/ziOlX4NXvANok8Clc1gQs+BEY+fy5KECTROay/ZsALc+SHX3/7Afm/yH+160585LGDVeVZq6CEkqYqCMzjJoXLxuIGI8Lx737+9beHg0bpYCVDYPZFQQTumyG1b0EzavDw2rvLoM6jiKB8cvq93ZAuhHZBohpaCyJC9elrNpLI4dKyiyrwbsTH5ofp32PgwWf0SfW0IfRTUObpfe09XkdnwijwvyDrAPmwFFQX+rUePRrmVQ1DvACZDzJvgDud+psLsxzWexgrVTB8QpoKqjpS/sWFpEfjpBDKnPoXZCvsYFXMk/eyPi6Cu/MsGh3/DOLHbUik/AHG2OydxBdEAdCaSOGUThGWTgXu6wLnERGwGr7vh8QdJAMdMjYFYPTRPYrvkSf8T5uTjwYCEe8dzr2PQL42BIZPkf/f2qFRM365PIhLXhfniKjoh9MjDMeubrTKoxGELciTzQgVH23JO4K9Y/vXLImg68rhL4+VwT3yHmseeAkF9iHyHO70Rwwo73SjGsbPGBBlOca88zV7LyKfoEug96pRY5jml4cu7wzHp++ShjCXx+/fGgrkEZpjysCgR4rGTSIPCQDw7/lRh+WYfU/XwGACYybCdPHC32mFQOowUCB9BAoRwaiG1r2bToFZNLrqnhIfy6OxTYNS+I0HpYVpBr4g1hj10AMV4gLYa41roBV+uJNCUgBtDEX8sHAVOsVDmLHTfgrojL7IU6cG33vg+RBG8FitIL+P9IRUHd+poS076ASYff3Dsx9yPn0FhU3HVLlv+r27n7oi31e7v4wpCmX8VjngcHAP6G/GgbheptUdqmAJv1QQBFLwEaePnuDLo6w/+oYPWV7/MF78+I9NIPdCbfzec69IWNdF9TqZPIrpey394uXpBMZIVIDqW119JOTnZ/p9/i79Pn+Xfp/f0+93/B7me0X+MZl/R+IZ7K8I/gX7go2P5MgDYzQ/P9BEwufZ6fN0fPo1O4Bvvn8GyAiKMM3d4aM2vS+BBepcgvO4+FGrqrHEdbCq3iHyXms+4uOZPRCBs/NYWKv8u6wedRq9/XDmB5TDR9lYJPyxfTyDcd5KRvEr8PKaNUny6SVzUvBPz1kjhsO4hiYaZzaYY7BHqyNw//bRr41ffj+F3rMPwoafv45JCOsl7K0/IR9t8ifkfXC5D4hZAye3n8cWfWQJl8JfH2s/RlwXvMD5sR6KUZ3HNDZ2hs+O/Y9CjLkHJfbA2BHkH8k8cvwDEXhxPoPyj0TU+4WTPBGlqp2xysLi/sSB9yj+hECHwvyEKQeRtIEb/sgG8inBtYF13R/V/Wa/b2rlD11+u5uhfoy0v768I8t4/WgyHsE00v7fNoijqd8L+9vI0LmTHdu4u+XvrfIb1DoaC/h3j85jN/L2iNmXVwhX4NPLaN8ygv3/7T7uvzykhOp9a7IhBQg8n6uxIZnAlIOUYJtQjKpdIGh+x2C8Hfn39ePF65935v8ggrwCduoQnodzFIcHU8YjcEBxAcEBh6Vdh3Fw1iN8Et5lpi7ACJ9iCdfBWM+jAx8DjAeFG3mnzlO4CT56DKr14ZZ/2RTx8qALCxRB0ZCwy7lQYIyiORzHWILAfZokMYxx4D0WsK4/nWJYwHgB7gc0HjCERznAmWKkS9NTFhAjvWe/+hD27X02ePfhA2CggGkajaoQjuOxHoNPfY5xaA+QmEt6AIecGRJgFEcGLAumcP/H1qcfRzc/7DFGPmxVYaPYjnx+fcbFGM30FK5cTas1//gIE850XGviHkIZLRO070l6TxqFkba2c5AvHl0WqnwR9NmFaaJqbRKCRV0gSDX8cKw3W2fW5jF6bhkNpW0CWPJma0pG33dzX15KmZ/ZaJCklr8UcunsL8uNEVlmpVSsZXupwhimep0Y10IzlTI5aQVpFq4c2a5kOTZRmFJfs2LPHq0rvpAnEzRpb4fKscWw1qm4CHRLQa9klJS651qgCNhFd2HI1sMKLbKiZpZ1jW5hpHA7Ws2Qe5FpOq0XhdrSXFmNEfX20HST5FoMROfGl1OmU7SX3TAKHI9ErIfMpCnZEBfY8zUWpxuBFctNg19dA/dPQX7F17awiDNfvE1EN8Nzq9Yig8yx26rQBnLOkUJxOoHgfLFw8bJwTaUPMlmdXq1lGPWWSS+m1mXRCUZ9Whuem4ImqWpT1FbLRLs05M3oBxowh5Xot8sbecSuTMHRa8wcrkdgyNaZX+jrQMFC1cczNRFlydycqMTbR/5aUy5J4yVhebWmx6a+tMdtwHtZkqR7ebPhSw13FoM9dUmeVa3CTrGBXOpGs2C5LX22qdJ0in0go9bCz/woCROqKK3progX0Z4QSls50HjImLmlh4p+LKXrpelbpZS0wGn1lLIENuBZ37ju8ZDPDDyTMN2qsmtwjQPlcoURPC8OYqEeVdltG04PRLfxmlTB0JW8aLyLadkNl8lZzkTTcJMcajmsTjbqGKbDKAfXnDkGBaRzbYlge5nA/mLbO1l4paaO12fxjlxhRpV4u614WLZ2HHnbhNrNtP42k50TG7IcyrTFVfZNw/Rj2pXcrmeDVuiXfRrxob+ZNzf9eKVxqaUPUkuIKelozKG4EDE3pW4J1Wx2jj8cp7zCyPFUYaZHklVtN9POm+OOXVFx6gctdP9KZVcSUd6aLSrFGnWK2qh0Z9L11G5uRZ5czKHWSivqDyJzy93Fol0q+C0y2rl0zVkp09yNhRqlLfg3U8Npeh7DVDoI6I3cznfbTdlu5cP15EwXx87lZ/3K8LWLe9CkAyqlB8lbD8rJXXr9wtheo1Re01uum6ZyTDZ+l7czfEIFHe4ebpaqJZGEHYFmrnbPn7iQxSOzxeWqQfWz3WZX115IpX/wJkLAT0zrmkkqKwRoyy7YnHZkq3a7OWvWFYNqm2nrL4gtr6+xNXFxLXtuFapNrz2zd0/yFRdNvuvcCTafc02UF+gyjoxVlWA5qdTnA3ewNUn3dromMMWkMZcF05INYywnRVJP9cEj0GaQWwxc5e1JLnFU4LRad5t02epEPblypXbgHdO89osTv0lv5epC2LOryRyXZ0c1V9RigRPYJMKM7dzcGZt5DgLeDINtlSSnTK48oZ3sY9bZ1HtnNR0OIN8o5rpE84yaHYdS6DeO7Lu7FZbumj178G3qdGjX+6RsFoo28J3qbSVSqLZZovddrqe2Rw9dEoqU3Dq9kE1T6JE5sB1HDvtTzu5603JqiWPpOib161y29AzsON/EUOakH862iaf+SlCnAt3Saa8T2g1cjswu1Lh5V3D1QE3q9Ozt5NNKLyZEt74cbXO/LGUlMTpebQXPBtfLDmjThYjx+WXTrm5Wztd9MafmSVCgphJtXN2YrPB5t1lt4RKpMU5g4mKmFxqlI8q6kKZShRIets8ECQv1baE0xmIz2cu5E5xXEbU0u47yLvn6KPqEWC7xYo9VyWq2uKZ8dzKG9mo1igLDII8iPCyO6tLbzCIBzCP1wt5sQxVC4DSeep1S3N4MlX2vcluBM0+AWzqZytKgt1PJJvUj4fo7nUVBe+viizXD+rT0/KAOjUuylHz2vJvbjHieikscp/FrtwsYh2+4BpzIYBYK8qXqvF3b3oZq0pL4eruaM8x0sm3SVZso+32rtztF6TVxJq+3/gakIcwO2zKs/bXw5czf2/lKQGMGtQ8Ls+UjWjCzXb+S97Z7s/GDQSvaTgUNL0vXNLEjztRPO8uolBwiVr4zrGRre76hM8VmuyG39eYiRhzlbGK8Pd5KN5VuXrjSxXRK+HzJ4lUmzZkl2ERSp50NmufkHanX3QKlWEFOy+uQnYMA9h/XtHC9NYUrDqegIqybZIFbu8uu70/eyVpwgE5v8ba/bTHm7MlQBBTTTv15al+r3qZXeEEzF8mddnJbqk15tjXa5Zh5OFXEDaXBsrIZaMeXCSY4Vox4BGtsoxc02vvb0NlvM3dGldpWXm5gzz3Qyba5DieYGltxltI1H+suYaicpR1mBruY9JYEiDQ6rW0FFO2GMhvtiKX7+TxN1y5+4yebJacKy51JSqY/kbHU3F4NmbvkqX0dhFyuFD/Uu81kFlemfvEuzq7dDdO5OteSOJ/LOmWbVkbkob1nDulJ0vk6hTGGTYKNiba6Ya80YT+Zt4KWLtf7CGVpCg8lWlAWslhj1mHPT6CKYr/LXRoojhF6VXtic9k4ikySpYXj2Jp5nuD2sRgg9tbtweG10OMYWVAxJgoZXDwWOsRa7cipsUjmg5GymmnqUeosu0M5YQleyG5srskHRfZyJleq3r2I9ewSbTswxYhpFV1d/rI6m8WWuEoduSGSHbO/FLNjroIomNh+rRwzg/Oi+LJvwHCe29PdpmkPFHbz6Esd0Zt4edKpzaqdkMdhyNnpUuq1QpDFFYjrnWWuPPWGcYUC0J5qq8AqNUppCs67cal88YUr5wYBDcgZ7Stn+6pMbm54igSFCPl8r4Qhz8rlbKMesmpOLZ2ZUu+NrXLgdvKC0FLcIRSbzw1HWLbpvNBKXWB9rpiGsrVUtNDEjjZ2VRVGieyZ1oJwIWDr+dxNjOUe8zaFfz1u9oGK9gK6YZJkf4oLyeyaq0vMjvEai7yqUnF2s13fDNqrpvyeqoR0Hyt7b33AtZuOFgobSglXYUUk+Ilf85Ok19BznS0XlLpJKHmgO7eUGEctL1GebKk9e/HKk9z1mn9Jt7pQOCdwFjqRuNimQRwNntslwzKHmWhner3FaD3aaPxtqOVLPJc5QbgJ4YAxdrKjQR7PzttFQzc3oTeBYWq0rOqpq65L2TRvre2jyZbdsoswXwKSD+rVLoZobFazUul11vBddZDL6Jb0taFbrDfJexdWw7DOjoerIlWnqb1jSyu2fa5bDuywaztYRwyrumFWJJOGnjvT3JP4s96g++jsXTeHqojKzEiSeH3wGLtbYMJhOQeW7x1KxWLJYaXNvahzW4zaLUhcWQUr41hvu94Z6MwqNli+oTb4lSc7gROnw35u5xKBrUhjiW5wpZuU+naxNecSdZCKbawnaulBD7mteHTw+dmoHbgp8AVJ9+tyM8/65WpbDRWo0Is3K9D91rI0XKro9URe2DdUhx3A/rZrMXel6vat1GxrqSc6fZqq9mZN7POlE7K93ntXccXOxIGiksth1Wxt1BcyGPxnFT0fkqymSEFvSQnDc2ctbll57lCJmR9jyaMVIqc5kj5jtDOtqvW5YWbiRD9DID3QGxuOKJ7hL6d4L87d/FZAEFru+8KrlZUy5STvWnYz6Xg6yfV5ul24l+m+2x7nC1B1ubEl9Pim7kuNCfzbwB06zrDbPb/bz0AdSOi8QevB75TtZn8uTpXNLiu/C+VSjGp+fvVuep8urvEB06Mw8dLUh+WM5FzR13brdrjQw3FlJSwRWYsQxxlcMb0jFs3Xy1BsuBx1nCa6ToC4rYjTacGf9hTDrrSb2+qyL3OreM7NqN2qcHfuxL4GrrKVRc5lZAbEc5ru2Eom7UDOT4zP2sx5SnA+q3AxrFCRVZNUxNRguJLKrMJXfDmzV+zifJYo0017DMNW9HJ3HFxzZUBjkIJEG7GaORK7Vzx3YlFREPHuRfVC85hO4DCR5MRajOfd7XQ8ZicDDVSvFNurU50BtUbrzdpT1Zg4r0kOEyZJZ1Ll1BFv4Fa3zVSoquCWq0onBQefadgFvdtJ20kbBEFlBoa83ao0OeG0SV9TQU42DchwDuRsM7SnfUZklXQU97F/0Kc1CG98gR3JHS+WERln3KyXtksewydSKTjdWVHVbMfvhyl7ZovYW3b6ah2kN3VeAjiaH93GZ2+swVNuuSX99jBVRfV8JUxdXez9AW2BwVJ9Wmg3GQtt253tcKFzqXB17Ho+OK5cn2eK3XQXwpHnTHj7dcuEi+lOJQiGEoJsflMubWzuLxbaxf4kWpVNt/XmSnLeHlAnok4ciA7OCsXduGKOwCHRekL1eBcme3NHrPHzMofmbHcdoc4Y53Yl2/SUdg7nl7NpvyjXi7q34RxRFwxwF60pg8Y7LY8KWvg9TXqw3DHUYeuJuMBnTOnDghXuQvE4YMJ6yQ3rzNACjMwPEbdw65LL1Uu3VmVhSYHMNZRuz06kgfMOt714XvXxrlR3m7CTuxMmnFDGxE6wQdlxRZeQmeMHgGcNWbC6fR1JCWPk/aQEk6Ahu8kc2+G8r80tfR0zpK4eZ73oicuTXIn4vim91JrH+5Mubhe+M8nwmeIfmmEhT9B1HErOyp2Rw6IrrcnO7/1obU01FwWXhJAa6I4Tt1aHiTbL435pCp5UJlgwvRGehaIiTZRH2IXRqGejU1Fde8c9ZqE867IqNT1thpDn0IDgO0LOdzrTVtJObU51z5TUudjLYVip6NWhM3teshNgupebrgc3gjGiDp+1XWV2vizqtErKPLEC/GLW6cnEzreTtOmrmI/OQUehyi3nnLUXrHLSuwwlXWT1OtvYlN/0SiPy7JoB9FxZ9KzLtY3SkynjuqiNJySTNmgV8UsWLAFDsL4TMvseW7HbA7/rMmciVIfbgig6AGQ1myynSz+EOGcSkwPDDhoKZxSFItlF3UoAPQvSJZa7WBdFbLpJ+2vRRKiDxqv1cA28Q07bucv3bhdoR3Qb75WZpAq4Eizi2wRspnFOFmUxbBYzWkwI2Q2slDWHhsXne6Kkl+EyJVRvttszNcrzTryeaqGUUlLFeFNOUPX5Ea+j5VF3ydoeYP9Ax0UPI3stdEo+qXqOzK6znd2hu+jcyKe0FVtwAifeUvnNFCSCRfDqCrMNSidxO1nf8vl2Zdub2Zw61v11v5JcwqwPsIL2mGf3CYux+ExF5+0c82ZyXjGSG7dhRawIVdd893YKmWxBHuwLquMuujdXe3K+lUlFSG521J+wYpI4grHDV3Zc1lndUvxqR1Pe7HZeUn2lxtVMM5dpfopnsO/CtXgaDXTBDvGgN2p77ntumOuZuhy0dk6yF6Mhp9xiwnud21fpbXPm+ZdPL/fz6ZdXHONI/NPLeDrxPGP4V7yMPt+i4u3JgWQY5tPLv+7d5+M95Ptp5f3IATj+65376/9e+L99eim9CAr6eK1dJc35+Rr0P70N/vzPvrkeqQ6PY/rxELav3w95aud8f+EeZX4zjj5vVZ4099ft0F1NNf5ZT/X2PAx5uRshLerna+zvlIZ3HD+NsgjyKN/q/O1xRgFexj/AGc8YgR99+/qUbjwmGGAEwIb4jaSpN1AWoyme52rjG+TxYO3lt/8Hcey2ROUoAAA= -->
