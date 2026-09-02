---
name: "rar-cowork-cookbook-scheduled-brief-measure-adoption-and-success"
description: "Schedulable morning-brief email summarizing measure adoption and success for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_adoption_and_success", "rar_sha256": "b95d64ece15641e9f5ab51bef9b829c4ace71bb46e4038dae12828556de57cab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_measure_adoption_and_success_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-measure-adoption-and-success:30dbabb4f00069484c888e5eaaf9a0266ff37f54e727690f4fe45e434de8aecf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_measure_adoption_and_success`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_measure_adoption_and_success_agent.py` is
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

Measure adoption and success Scheduled Email Brief — Schedulable morning-brief email summarizing measure adoption and success for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-adoption-and-success
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_measure_adoption_and_success_agent.py` and embedded as the fenced Python below (sha256 b95d64ece15641e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_measure_adoption_and_success_agent.py` first:

```bash
python3 scheduled_brief_measure_adoption_and_success_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_measure_adoption_and_success_agent.py   # or on stdin
python3 scheduled_brief_measure_adoption_and_success_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure adoption and success Scheduled Email Brief — Schedulable morning-brief email summarizing measure adoption and success for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-adoption-and-success
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_measure_adoption_and_success',
    "version": '2.0.0',
    "display_name": 'Measure adoption and success Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing measure adoption and success for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-measure-adoption-and-success',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-measure-adoption-and-success',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'acfb59770760788f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/measure-adoption-and-success'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-measure-adoption-and-success', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefMeasureAdoptionAndSuccess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMeasureAdoptionAndSuccess'
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
    print(ScheduledBriefMeasureAdoptionAndSuccess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZejxrbmX6HzPti+VJWYEXWW12qQEBKSADFowOWVxRAMYhSDELj93zuQlFnl6+PT16f7oVWrMgXs2PP+9g4if3tx2iYqqpfPLwZwckRy0jSOQIU4uY/Miq6oEvirSFz4H/GKvKlit22Kqn758OKD2qvisomLfFzuRcBvU8dNAZIVVR7n4Ue3ikGAgMyJU6Rus8yp4gHeRzLg1G0FEMcv7svv0urW80BdI0FRIU0EkArUZZHX8ciw6HJQ/QOBEuMwBz7SFEjV5ogPGfcIpO8ASNL+E1QK3JysTEH98vmXXz+8xPD7y+ffXrzUqetvSgJfGDXbPtTgn1rwuW88dIB8UicP4YKyh97J4XUJKqhYBm/50KTn1Y81SIMPyH/+Z9I5VVj/9PlLjjw/X17GfzpUcrSlKZy6gXp7Tum4cRo3/SeETzunr6GZTVvlNeIgNXRuHn56rPzGqSiRn8dnPz6EfApB8+OXlwKq4Ixaf3n5afTAlxfoEPj908il/PGnT2nRgerHn77xqVv3DLxmZAa1/vT6vH6yhYTfSOPgLvVnyPURZBd8efnOuPHz0Hu0E658+XQu4vzHB+OyKq4gd3IP/PjTX7GFcfCSNK6b/xbfXx6MI+D40Kan4j99uDv5VwR9GvTO86/FljCsf8cSSP4m7gPydNRf8b77/7+wTuMc1O8e/6fs/tkC9Gfkl7+07V8t+IAEX17mII2vMDtg4XxGfns1NHH2yw/+t5s//Po7ZP1/ZGMUbeXdObxmTh4HoG5eX3/5ob7f/uHXX35oS5hrwMle2yr9Zzz/mV/vcv7gwSfVj39cC+VbeZLDukfeMx35rSj/R/X7J2TvpLH/7X79Gfm+XsYPioxGvAl9uOC7mqmhrt/58aeX3yFU5NCa1rs/hlX+H/+BbGOvKuoiaBDDK9pmRJwmzsCovBnFNWI+i/qrsV5tNp8y/ysC747lDiHCadMGkaoR+WA9jBEfLSgC5Ov/9O6w+tF7wuqkfgOl1ztevj7R8fUNHV8hOr4+0fHrJ8SMoApFFYdx7qSIzmsa4oQgb0bh9zSBSPvxOsqHusUP/NFnqxF7aijlH8jXvyPw9c77U9mPxn3JYbSc+I7AICuLCgI6BGBnRC+3b8BHiL4QYaoiTV3HS5DxR1t+Gj12iED+9KMH+wy4Aa9tAJIWHjQiiCFifxgRv0ivEC1H79ZJnKaIH1fQdUXV31sEjMDnkdnXr19dp46+5A94JpFHI6onkOBdYeTjx7ICQRqHUfMlB15UID/89vsPyP9C/tWqO/NRhgY7xrMPQQ1lQ1UQWK9tBslqZEwWCEb3eP72+yMoo3awSyGwyuIgBvfFkNu35BgteETqLUzQ5lFFUD0l/dFvSBdBvyBxA70FK7/+8CUfWRSQtOriGrw58bH44fq3uD/kjDGpnz6EcQqqIrvT3vNyDKZXVP4nZBUg756C5sK4NmNEo6JuYCqXIPdB7vVwpdN8C2FeNEgNq6kO+g9IW0NTR85fXch6dE4GIctpviLbmQa7X5G+teyRCK4u8ngM/DNxH7chk+oHmGPCG4tPiAKgN5HSqZwyqpwa3OkC55ERsOu9rYfMHSQHHTI2fDDG6F7n98zb/qth430gQMT7lHKfC5AvLYHhFPL/w0gzWsBLki5KvCnOEVEx9dMj3cZpbLT+McDBkeIpZoSB9zHjDZHesPpLnsYwRFX/jwdlcM+wB80D/6ARPkQV/c5/rPXqzjduYJ6Mga+qMbedL/lbU/gAXQ+jVI9Gw3JOHra8CRyfvmkawZodr78NCMgjBUdnweRGytZNYw8JAPDvddBE1Vhlz3DApAFjxcGy8KI/WIVA7jAhIH8EKhHD7IXevbtOgdUyhuee+u/k8Th2QS381oPawnICn5DDmN0wAjXiAjg7jTTQCz/cWcHoQh9DFd89XEdO+VBmnJCfCjpjLIrMacD3EXg+hJk6dh8o770MIVfHdxroyw4GAVbZ7RHZdz2fsYLKZmNJ3Bf9MdxPW5Hvu9c/xlKEOn7rCnCovyfxN+dA/K6y+p6ksCUnNSz2DLzn6aPHf3q06ccc8K7L5z9tC378ezuHe+O1/hi5z0jUNGX9eTJ5NMe33vjJK7IJzJG4BPW3Pvkowo/Pkvv4VnIfoeSPz5L7g4yHyz4jf0/PP7B4JvhnBP+EfcLGR5vYA2MGPz/QLbOPwukjNT79kuvgW7yfSTECHixtt3/vO28ksPmEFQhH4kcfqsf21cGOeYe/ex95z4lnxUB0zcOxadbFd5U82jRG+BHAd5iGj/KxAfjjCBiCcZ+UjurX4OVz3qbph5fcycDf2h+NmAzzF7pl3F/BWoKzVROD+9X7nDVe/HGXeK8yCA9+8XksNtj/4Ez8AXkfbz8gbxuO+2Yub+GO65dxtB5FQlL46532fQvqghe412v6cjThsYsaJ7rnpP1nJcYagxrfoXnsHM+iHSX+iQn8Eoag+jMT9f7FSZ/IUTfO2DVhs37W+1u2fkBgEGEdwtKCiNnCBX8WA+VU4NLCPu2P5n7z3zezioctv9/d0Dy2or+9vCHI+P0xNDwSaOT97wx5o3vfmvPrKMS5sxpHsbu372PtK7Q0Hpvwd4/CcaJ4feTmy2cIReDDy+jTKoaz+nDfjr88NIMmfRuIIQcIKh/rcaiYwNKCnGCrL0dzEgiI3wkYb8f+nX788vmvp+j/Bjp8JjHYYFyXCjAMYzhqSnnT6RTQwHECzsEIhgkCkg1oCrAEy3BYQAWAogFFUj6YOsALoEKjvMx5KjTBx8hAU97d/3815b88eMEmQ9AMZOZytM9QwAM4zVA44ALacWncBQHnTgnOoxwPsDg0hwEURk59B+DElJjSNOMDmvUcd+T3nC0fCr6+zfFvsXoAxiuE2ywe1Sccx5t6LE75HOswHiAxl4TiCdxnSYDRHBlAf1Fw/fvSZ7zGcD58MGY1HCvhUHcd5fz2jP+YqQwFKZdUveIfn9mE2zvsceMqkctVTMDXZy5pbuu9X/nKnstrfCn5ruQ4iqTkDafclH2/i2amtdiKu1Ig9xSdoLqMdia7yY8FHxTRjmQ8VnXnirqKNP7mHTlV8z1LFHfnBVU4oDFmduYUzSpbDLIGHW3qi6TalGvcaJttCeR6RVpZXurOxjtctcnEOG9DyiLkc58O+YXItwVV5kR+GRLniM68yYKuqCa9nCx8f5GtJp/RC8fcLVXzMlnrhnzcX269u8ccyzdoY6ZQ62HD6UxcudFF03tXyWki0MwUZp5BqseKQicDZVW9eNkes3SaVKs2vbhW6rtXKiNWpbQ4L/fSMOFddl8fm/iyJ1ddv7RBT87pXqQ9B1zDMlvw+cJidvFVNb3b6Qqnx6R2i/Ut2K7DpPXIsKCJOvI29KGRk/XawfeOmgtZEjfkOTuxUkZiR7FlywbdYGlfHdWTfDC2N9u6SFK7oJcHjxGtNsXSMNtzvCymMrEj6D6T6tJtTswBoJ6OCX1rHG0+rIq+lPcnd30UWjC3aCcljobp+bJxClDMvMzzQ2ldFgra2NaeaHr5kLlZpJpnNOOPQskKjZoVisOB3pMvp2lR7hNCn9S0tGfS1tfT0/pWawM+S4VDonqmZKX6ADpQMpdmypjVkQXqnjcw22IbtGdwerq70AR7WrqsszWYXt/bmUsE7encbGary/5A1TphZNO+rvDMOROXGVbGlCk4tex5YnDAjhnVmJ1loUp7qm77281fy9nG5qJZR1K1Z8aL5YKFjjqVrLlIJrl23JPqrbpUsyEDQyR4WZASp2yLbUVH3NgHQBhWdnRTNTgq26x13BNQL+aFRRc1Z3uBHB+CXYJmahBjE0FAef5MopFouXNGG+YyE5gyx6mT01LAqnNxRYfzztaYJt4EM/litetzU5WJ3jdGtY9je8nOOneRXkVl5dzWxzTGRWc2ULdkE6j7OlKpiww6X7j1lbZ1JzKZl9HqsCOzRbXfKp5xpbbdvDs768LwrUIsJgv2FKqiLXDKsD7FzMzSzUXqH06UZwo3is299apXr+QKzc62ykSdWR+2MUvHhWd1Im1srtlGPNIJvp6eqXMxuJpFEBtTYs52tdUEND0k+UbiqutUmwpEQV82huJeQmLdH/YTOfWOl34Q+QKzMXemVHCbhS2tiaiuqWarVM5sfc7MGSuhm7BcXwvME05c0qYSzRWzObNZ62s37Nc7IdcV6bIwySDlIkxCLbcV09yH6uDcdHnJemmGToMwzyqsp0tdI/DKZK5Mku4OsuV4+8NOtq9MdNOyMEtBqlTSPDJQ0/J9Zck0iznfz29C5yzzbu9Zl0o5HUqCmvD5FF9NxAvrwGTfBNdWEC+We9lrnDTEs2V/WYt+dV1gUmCvprRgy7tjU4h1qdzU0OhZfeupWJ9sM/wmKPLQ2lsHH1J5Rm5Mq+8r7OCd5Fm79/EqpRxR5AccPTZ2iZ0IGi0XSn6Rya2ETjRnImeieFrajZ3qkXblfRYt6hOaeORl4ZCsON+hazUmucmU65Zcd7mxp0Ap5hLNWKKtuza7lW48uk26nsNX3jRdr2cdekywXBwkdFbdIoEeEr9Ad0xMX3VL01JwEjSVq41kKdbXvJqq2WGF2zZTdoqZEEdHXfM7fYuFy0Sm+5Az6Zk+N6f86bDq26VoholgQKTqUoWgXTYNVxTfbDtxPvP3jaHcklAxMrDeACn0KKGjJFHu1RVjDkq6w6oJfbl19Oac98JBxOcii/Ebfx+xnn3x2HnJLrITDL3i2sqUg6BCg1xerLbzxVnxGGZyxA3DOqUkXXmudkqWfNipV6PO9Anq8IvKH8glW6wk/RRt0+syD0iSmm6X882Nmk60zaZsXEq3xM2NHXrXsyLe62dLI6MLDzezfbrA1tnRoElLMoTrtUCHzNJTN1y1YWoPU13GFr3qtvE61y86beK9UCrQIu+YrE2BNspz3cmcseovygX0JyZxlqiiwUdX8TgxM6tIaY7T7b0nDxhXxLV5Zn2ZCjGiPyaswiYkpLy4YVyWztZnl+lSJC9ccchFzl8eWrOl5/usOKnrSRkRvHRbNLBrDNWG0WKS6naqYtc3vOdvUbg4N2E1zO1ywiTlkQqvcMxDtz1ei3PB33hhN11clnW5jsqF7k3UZsNdq9aNl43oKBvMDGx3Gzm7be4K9MbYbqR10Zx7Nt22lzjItFYTeZQpec90CUvk9oYtrLyFedvLgMji02qv+MJ1ne5bY49lu9k5u6xsfOBpR0rVmbTZk/JemyjdjsnMdYozlpbgNo8tCSHuCpgr3UFbePZmoybs4RgNu9tFihdDIjQbpmBwy91K9Qrjb7Xoh5ZJ3pbM/Arbh7lxdukl8/aUYXX7mEjh5NLXcuAYK/kUBgLFT7YTiRO0ynUOW0eE+9rAxK+sdxDZ1SG7HGx75scT3D+UhmbCoX/n7EDs4cNqBjg3KAZh5naluW9XsmZeIrnXcCVdLOQ9dZplR6y2poqnxfVGWR7qmZnHEitc+cNtwe/IuORPhVYu99l+o/KhdfLXs0kukumE3aWykBUzNJzA7kEQ1a1VG1/vt0dNtgSvXqZHv2YZyfGNA+4vhNyX7Nnyer0u+0Mz4bx5mPQrbgVofkCJUqHkc4kCwCnVBcCp5YgTtj9vucwVjyvGN5kDweIkmGewaw3WPDrmNrlYbXZSX/KEKvSh0lAX2jC7gNpdrKyb89awFK1jNaXVi2M5/W2zwqbCwbtxfOsVGHZYVpK/MvBLZO28YH85bc5kgCnWpTheD2HKrGVhk+6lRSftjcFquwQVdpxxuUlFUw2H09IjRGw4QMgS+PRMR6FVkwtLUlE7K62b3YXRcFqIkcTk6m5+yTMTLRqv2aRKigXJll1vDGGyiXMuMrdbs/f2LqOnXHgjzJiwj4KkX+w+snlIR95uMz3JtkepjL3WjHRGPOLyfi/k+OW4o+qmkGOPsOvBUJTNKU6K1dT1qFXHcDxt+Bgxy1ys5MwFf9racMBc9LZUumVm+EbUezdb37iMEwesVmLypMqKrTIzUWbm8zhqNxSrnOZue3bP7HmJ66lz9NplGTOTaJnudUwTbVemMecW2xKY+ZN1WREb3yvhgFKtTwJ50KXKo5dFzzXiRarXy5mxwoY2oYrlpbecseFfZcPuk+OW8FY+X9gcieeW6JyPV58sMf68rjNyqpq4xw0+3EaorhHtIptzXGthWItp6uC8SQkw1e2V0GJJ6cyHeB6kRkIFeJXFYB2J0yKxWp028n3bAmtBxnLjRP2aSGdQtTZKyprYNzx7OmsZpu+DAHYuoUR328PBwOWaWZGbBWDR3R4rdoN2xVw4m7M4kfTTVbYmsa7ziL1eR7ttOqfja2YUvHMTh3matdwwFc5av/LQ3KWkzhK1Whk2VG/TNMFcZ7qVZoIIjnVbz2qoF0pgM5LgLGKir/ZNIu7zk3yMnWXSCQF+sDP96E/6jInyoxgKjYeWBw+zeWlB4Ni0CrF9X153q8SPwi0xL7o9MMN5hztbnOlmt91gq3ON7hu55CbKBl8KuB5qIQ9iKQXc2VvaPhsz/HpnRbrXn0zOuyzXYlsbG0ydVcN+KZ0OmbaMpJWUoic7PehHDaKuvKGX07OvyTRV5K1ZRo4q6zjhc541zFaylK+vecKejDYqtV5ZY+hKiSVtrZDbhUEaV2XirqZBMuVujELigHRzpwJHtccBdiOizj96V3LTTa9+5+072qP2pCRELtFT5+vCWFnLZjjjsorRaQqocu7W00wdtFBTdY0+sHJVNeHyWquVTDhUIUbpXjQOVbZQLLOo51RDHYf4cObzlWLTwTHr0NnktJNUec53PrEPTRpn++kaLde0wYo5c7WP5060SYEY6g2aGtciqjbmDbOzSXrUwU5xTsHy5LEUoGN38E9nDECQnjD9dELxu+OmVjbMcTLdaSyZcClLatpwERrCYg2Lxvy6ooSpU140fsDgAIrGU2p7yuCEdgwwOU92uzmbU01NFzyfUKxXy3Nzjs56SendG+9FqKlRbUTZdAra8jhoujcP1Lr3GfXceVsfXxRV5q0jNr0BuL/vz9ssyYQ6sm1XIPHZyaWT67FjeUAujz5/LklKi651Gx48fXWtojmlqX3L0rNJuMmOtitZfEagUeRPjGXVdpg3V9Jwq6NOzJy4IL7BwQF3z1f3CBwSbSb07dZF6c4NYp3lt7osckArfW/eY7l9DbY3JcIZ9jiP4g3BL934rA6ceySn2Sa4SDSgutXV5XbsuWxpcGPIvg9O8oXnNfJQ0dPFLJjBZkGJu2YIdZXKQUIWesyJbFpxFzVJVup8tqRBxlpKZ3QTuec8fdCscHk7q6yqraNO647Y7ISyOnaSUenobimDHSpVy3mwXpw3lGDdxNnkMt1N8LADQaA7UhE0vG/MD+ZyYI8m3JfeRE+UTptaLHcN6WWH+Xl3MsXtwncmOS4ovl734jCZbM+RzKyYGYlK7KIK8hZrb+IGyA2pGcYgkls8rNFkaV+rs33CFml4nTu0vkQDr4w1/LZsB4cm9wnJRtvjruzPzFQUJ9yKP029+anDfFRjRbsSOsm+EWQ3CVUKpxl22U7C+Vo4KamOkwM5YwvOV9l1DjIGsIR/IVdbxWD7w4pqGzgBLt1uJ4ckLxgehnsZM8dpn5BFXt2f0bWmo3uxorWI4oRWrjP0Qk906TZX4F5521ChFJEuHOfqJZm2OIoRc7Bp20nEluQx0CBWS6v5xJ8GaLqbQthmJvNquWE74opd5g16tWYqW0AwDtLgzFYF8Lx2YCZBeJ3cDGMeW1xPerfsWs56YXarQ7aLdJGnKefCVu72yuHJStGb0/S02eMDTmKLYIHKWndT+KmUrLQ9PgWqxnVFrFZutmjNXQR82Y9VEi+vCy+9KimlWczcis3NUuPJwiOuoqAIoS/vwsHDVK/1QLS00wuT4XM4jDPElANES98warJwEuEkJS65Q9kB5/OaCua33XHRmEHYgBOweWImrCkjnxGEoLqdbdlHEpcbeTjN1aWsy8KZtpqoNZeliZmN3U9nA+nJt3S63JMklwjBZGos1FnfLsAMJdhDsIqUTUouY5I4HbjbdWe7QU0fAm++E2+TDm7P9HKFu17Wypq8O++vhJFhKEPnu2lX4lNV44NCDsFmSOnd6WKWu8Lgc5fJhCXsP0cL6D5dTrSDUkwA15iJmk31ViGH2mpvMPZogR7sYd5DPOJ//vnlw8v9zPjlM46xDPvhZTxVeJ4N/LsvlMMhLl+fXEmWhkz/373XfLxjfDtNvB8VAMf/fJf++d9T+NcPL5UXQ+Uer6PrtA2frzX/yxvdj3/njfPIqX8ci4+Hobfm7eClccL7y/E499u6qfrXukjb+6txGIq2Hv9cpn59Hla83I3Nyub5+vk74+Adx8/iPIYyqtemeH2cIYCX8Q9bxrM+4MffLsPn8cKHF7+H0Y29+pVk6FdQlaP5z7Ou8S3weNj18vv/BjTCkxolKAAA -->
