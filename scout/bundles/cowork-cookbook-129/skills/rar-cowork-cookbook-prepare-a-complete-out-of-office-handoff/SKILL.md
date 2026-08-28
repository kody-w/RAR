---
name: "rar-cowork-cookbook-prepare-a-complete-out-of-office-handoff"
description: "Step away from your laptop knowing nothing in flight will stall while you are out."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_a_complete_out_of_office_handoff", "rar_sha256": "6d9f56b07253ba06fef4da66d4c4caf1204fe4e4f9b92328b4b18cd24c251842", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/prepare_a_complete_out_of_office_handoff`. The original RAPP
agent is preserved byte-for-byte in `prepare_a_complete_out_of_office_handoff_agent.py` and in the RCI capsule.

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

Prepare a complete out-of-office handoff — Step away from your laptop knowing nothing in flight will stall while you are out.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prepare-a-complete-out-of-office-handoff
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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prepare_a_complete_out_of_office_handoff_agent.py` and embedded as the fenced Python below (sha256 6d9f56b07253ba06…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prepare_a_complete_out_of_office_handoff_agent.py` first:

```bash
python3 prepare_a_complete_out_of_office_handoff_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prepare_a_complete_out_of_office_handoff_agent.py   # or on stdin
python3 prepare_a_complete_out_of_office_handoff_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare a complete out-of-office handoff — Step away from your laptop knowing nothing in flight will stall while you are out.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prepare-a-complete-out-of-office-handoff
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prepare_a_complete_out_of_office_handoff',
    "version": '2.0.0',
    "display_name": 'Prepare a complete out-of-office handoff',
    "description": 'Step away from your laptop knowing nothing in flight will stall while you are out.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'prepare-a-complete-out-of-office-handoff',
        "upstream_url": 'https://coworkcookbook.com/recipes/prepare-a-complete-out-of-office-handoff',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f3c59d4f41c70cbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/coordinate-team-work/hand-off-work-during-absence'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/prepare-a-complete-out-of-office-handoff', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Calendar Management', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class PrepareACompleteOutOfOfficeHandoff(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepareACompleteOutOfOfficeHandoff'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(PrepareACompleteOutOfOfficeHandoff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/616+7eiSLLuv8Ld54eqHqs2iCBYs2ati7wUBBRQlK5e1TySl7zkIWCf/t9Pou5dXXOmz52+61gPN5AZEflFxBeRyf7txWmbqKhevrwYwMkR0UnTOAIV4uQ+whZdUZ3hV3F24T/EK/Kmit22Kar65dOLD2qvissmLvJxegNKxOmcAQmqIkOGoq2Q1CmbokTOedHFeYjkRRON33GOBGkcRg3SxWmK1A1UinRRnIJxGuJUACna5hWqAL2TlSmoX778/Munlxj+/PLltxcvdWp462VbgRIOZthiHNQArW20QAuC2AMraH8RBFBE6uQhHFsOcJk5vC5BFRRVBm/5IECeVx9rkAafkL/97dw5VVj/9OVrjjw/X1/GP3qbI00EkKZw6gb4iOeUjhuncTO8IkwKV10jFWjaKq8RBy6ogst8fcz8Lgki8Y/x2ceHktcQNB+/vhTQBGfE8OvLT0hRQX1VO/78OkopP/70mhYdqD7+9F1O3boJ8JpRGLT69dvz+ikWDvw+NA7uWv8BpT685YKvL39Y3Ph52D2uE858eU2KOP/4EFxWxRXkTu6Bjz/9mVgvAt45jevm35L780NwBBwfrulp+E+f7iD/gkyeC3qX+edqS+jWv7ISOPxN3SfkCdSfyb7j/0+i0zgH9Tvi/1Lcv5ow+Qfy85+u7X+a8AkJvr5wII2vMDrcFHxBfvtmbHn25w/+95sffvkdiv5/ijFgKnp3Cd8yJ48DUDffvv38ob7f/vDLzx/aEsYacLJvbZX+K5n/Cte7nh8QfI76+ONcqH+fjwSQI++RjvxWlP+n+v0VOThp7H+/X39B/pgv42eCjIt4U/qA4A85U0Nb/4DjTy+/Q5bI4Wpa7/4YZvl//AeixF5V1EXQIIYHiQWBDm7iDIzGm1FcI/DvmNsVgLjWMQT2OQ7G/+jh0eIiQH79v96dDz97Tz5Eywf/fHO+eU8G+ganfSsC+HckoW/Rg4V+fUVMKL+o4jDOnRTRme32a+6EIG9G3VBMDaorZBV3aMBnyEefxx9Gmvz131Xx7S7ttRx+vTN3/GArnV2PTFW3KXgdV2tFIH+uzYNkD3rgtVBRWnjQqgDyb/0JolAX6RUy3YhMfR4J2o8rCENRDXfZEL0vo7Bff/3Vderoa/6g1hnyqAY1Cge8m4N8/gyX8GD7rznwogL58NvvH5D/RP6nWXfho44tJPqnb6CFkqGpsDqEbQaHQbdBR0Miufvmt9+fIEMxOSxf0JNxEIPHZBirZ+C/IW6smM84OUdcAJGGKGdlUTX3stS8IusAebcXKh0fjYweFXWD+KAEuQ9yb4BSHbicdyRhYUNqGJB1MHxC2hrctf7qVs7dxAwmvdP8iijsFtaPIoX/jWbeB8HJRR5D+N/j4XEfCqk+1MjyTcQroo7RicBgcMqocp46AufhF1g33qZD4Q6Sg+5rPpZLMEJ1T5UHPHAQRMZ7uvTz6HNY1jPIC379pvs+xhmrnHmvdtXXvH6mwVia4URYFqDSsI39sTj8/RlSdVS0qX/HD1o6Snp6wX965R6Dz6INjXyL6LHYfy6Cz4+IRp4RjXxtcWxKIP/7fcVoBSOKOi8yJs8hvGrqpwc6Y4MzovjoiWBxR2CIPDLhe8F/o4s31vyapzF0dTX8/THyjulzzIOJ2gpCoDP6XT50KERnlHuPtzF+qmqMVOdr/kbPnyA6dy6CkMPkhME7xsybwk937B6WRjADx+vvpfrun8ofUxXGFFK2bgr9HQDgu453hlZVY848wYXBB8b8gSB50Q+rQqB06GMoH4FGxDALIIXfoVOfaN/d8T48HhsgaIXfetBa2EGCV8SCYT+6voa5BruYcQxE4cNdFJIBiDE08R3hOnLKhzFj0/k00HlGY/pHBzyffY/Tuymj9VCo4zsNhLIb+dMH/cOx72Y+XQVtzcbMuk/60dvPpSJ/LCN//5rfTXynbJiw6ViB/4ANAhMlq+8MOfJNDTkjA8/4gYFwL7avj3r5KMjvtnz5b432x7/Wi98r4P5Hx31BoqYp6y8o+qhab0XrFWYdCkMkLkH9VsA+O5/fcvHzD7n4+ZmLP8h/wPUF+Ws2/iDiGdtfkOkr9oqNjzZQ2xi8zw+EhP28PH0mxqdfcx189zVUX2SQ0UYXDLBivheQtyGwioQVCMfBj4JSj3Wog6XvzqDQG1/z93h4Jgsk6Dwcq19d/CGJ75UUevfhvHeih4/yBur2xz4sBOM+JR3Nr8HLl7xN008vuZOBf3d/MjI6DFuIyLi1gRkEe5smBver9z5nvPhxu3XPLUgKfvFlTLFPyNiTfkLe28tPyFvDf99H5S3c8fw8trajSjgUfr2Pfd/LueAFbrOaoRytf+xixo7q2en+uRFOWabDf+PJphhV/5M0KK4ClxaWH3806PsKvysuHtp+vxvaPDZrv728pfYTpWdjBofDHPpcjwUIhdEEFcLrh9/hs//vlu0pB3ISbBWgoLm/CMi5i1E4OXMdbB6AgPCd+dwnPMJzgimOEQEgABEs3AU+w2mXcKe05+OEh5NTmsChvEcUjXqzeLQNdxyP9qgp4S8oZ+6BGebOPDDFpz41Axi5mAU0DUX636eeIaM9F/xY4Ijme/c4AvNc928v7pyAI1dEvWYeHxZdHBx8tknUSFpMp36Y7QI7NohbC26W09iup/e5klq2QUxzlTwMB6bnd5GUxBnDeJzupPPrwAc5GygZcAtmb3jpDfcarkwGS2dYVU8XWk6cPN1fhdFBTFW+XJ9BpGZGm0cy5Vks2td0Z0i+MxhbwUK3VOVONvLlsFlX/iCVPu/Wvnbg3XOdG5RgOuLMcnkjOtpwhZhce8Nt6l8k13bzLrlIs0UzhWHmSFm0oTjF5hQi2M5IchIk9BQcj8R1Y19IDzUVo2pO6yE6aAJPSYODY0PU41NeXza6IW1aLxpAYW+5Uquw5JKQorOzuzq5gbmeU/H55q33phwahz47xGWQb6YZfWPK1BJvmdTKUogvEyWzhJXYn88GfvAN7US6+0FtNGFYHYZwcdDURaviYgRulIU5aOmJ16kjuDJDnHq54c/CjQsYGr/oNpGe5HLf2qs1lxtMZDuK1RZMk2aGZ6sYmRDLcz1sbSYsz1yMukxsU0J2U8wszIi52ZW+UKZ7btuY0mVdkYEx+MrhEPf7TQ6wqPMCOmZ73l02bRYqTu8PCwlujDD1MriCUQtrJaPdfOfSJxiTFuMbYiOd5RLzXHGFrdPD9coq7uIkXQtNEdOrD+bHYrZastXV9UM/aIpOriRBz+zcRnMvFFEqxOKcW7vGDEqoLVWw2sXeEDxilfAOhE5lxXYi4snA957DUWXkn2Ys2h2lqS8L7bpv6ijclu4pxzYTtclir6lOezqh9YV/UCgBryrjNjfNKNqnJxUTBlPnd5YDC/d2V6qkm2jtUcztnRuRehWjwMqK8xajmGbtmb3JDd5WCulOiWb4uorV7cBpBiUeUaxDo4ELSf9C4UJdmYFhW+Y8PyR1xE+VQ1JQlRPwXrUfnLNlnmbOHuqgIk4TayMlT/6S3+1jecn7nmy2LJheSKP2onJ2CTrfEzBeP3HLvWbNPbuXZ+HQxYR6ShLtfE0saZDwjvfX1UYSr/zhttfPtpBplo2VZjSoKEwttbsk3TBZBLQzDfFL3nNym+sbTnYF0DdE6R05WWFCmYx1Oyel5Xzil3bdeFQrzQs0EKa4s6Dbk1pf0VksNFeS1eQFGoeZXB01KhusFbbQN9KR1oi2SS5XQ0Mjg+mO6c6irajmzkuZxhKNntmGNjsLiQ1C1d2rk0iicXq5W5zbtArryX4WqWJfVWufVkmcOyxTGcdwewUYu7lEx3kpaYJJcRuhJ+SFOrWWErrni9m8VC5qXa2rY7nNaOWYlYwQCcyVzcmFeBS4qxm5ME1CZc6mCsrHtBNIk3XebYgez0RrdULXp1CfyidMPMghO9lNqOWi38ccH1KMarP8SquPMuSLrUbcVrEWnJcXKU3z1o6HarMnZHQq6htBYIJF2fV7dZ6HR787kwcCrcu9U+0CGt0mm60lzi8mS6+WYOUNi5YLh/q2Js1jt2Gr03EaOJJ7mDeOOqN2raqvAQommKJPtBCvvB7FlZLOy51ZpuX10pdqQgxmIg72KlCVOFnLB1KpIvRQ25vQ2bX65lCh0WodW3F37ac7ms1mnCMlVSquqjmpWryzJ32HOoNkyHS7CCe7tSqKIUPcmFNJD4swEHDaOvXYtkl7gyk1Xez8M9xItnvMX8RGXIZCKBJ44Z4cna10Ob1dWQlf0MSBZ/Zhz7b76GYbYD+/HmzC06OBOFesfLYorttkQiGkUgl8qaOOQJ8rjnUzqwXl5SuS0iqjwADMYOdGXYnbxYBZZ4I5JtUcuwds3BEL2Ahsg+rEdFVrnagm3OnigLI3krigJUlft6vBRoHN1FjEFKfDak+wl2ugKYS0Xh5qVklV1yT11rZ23hkr5nHjnTm/Ytqw3etktVZUY1319px1RTXdJ1HnnBenZm/sDcVRy91cThl3L3WiljSuyjF5L8a9Xdym7e3CFl7WGRyzY29M3morVypMTTWNRJW1gMDMuA5JvKgF0ibY03Wq6NvjhV/MYTIkySb1By/rq4FUy9I1Ksg8FX2lytuEt/REml3YGKvSNupSukh8bhMtdnpVCyvUMzo7MFGmlppSktckiV+a0iz1Tutnx66LvGy1Lk5V4gdu4FYTHZuAAiVZk5dbpyloXLiQ6uawC/Y6hjcdt4OtFrVaiaGX7+yA6evdLHOFNmcZZ8ujk/IgZfrkTK2vp13PTsPgzCwdRlcc/6hMhyPtsllzMix0iZeynvHS7njaXCOuVzaxAxgp20dHSasjTvB3hWBZVkjrfmtUaiMl1lRcX6poc9ouLwLsZzHHb6e37LyJwW25PPPGFOfidNvirsOfF5IQ71xDnOlbzdx0aBiQ+FFqxZ49Vns2dMFNmAK70g+bKUZUChosVsU83Z+HnJ+JTBf6il2JYM1e8WnPkEJjZLg3WRcg9zUzPF7MiypLJZ4IXnHIKL1Wi02NLUMDSMd0RS0DRSz19fSw4b2da/G1lx/aw0Zj4qm/MMJ5m042VzyRdc1hdrayIQDH6UNAmS3WecwqWWjMkoro2eI2BYl93aftwd7PVeWYFxMc3R6J4yTLFWA4dUido0Q8FN2Sh7sFfZhmdSBw5xa9qqvSrQa/jvykIhWpSWbFJrTmBr1bt6p4CwylZZdzmAHmVMuW7eEyNY6hS+3mu3lnrs8EvtsdKZy4ylx2MkI1Fk6qtMP7JefFE5gIiTFwZx4vWrqnzcCiz8fCzClxv09v6u2CN+r5Fm/0LeyYSq/gUFwP1S0/JXvIjGHTxHCf4zcX1Xf27hSvWMI54QwL2skhvWb8abfpr3Rv6DXM0u0+pASPbPYWpszTyaza2RcjLIdLKNe32FAuZcMGQNkljsnFqrgE1NoiLpxssSejOh4tOzir9amuC1Bm2jkpiErcJ1l4gvuzvQ5uNMtolbR3E3KOW9eh5s/AoZs9zzPSXkTdajbpiK2eA8WLuYOsYhs9objgtuLFy00w+sTpI7GXdHAx2otTT0lPH7xqKzq9MZm7glj47tJc6pQaNPX0yFgqH6FTjbxxRD+fmtmVxBOQo4whu4lUxf66FkTZ25TgvD6aeXlYVMGEZpzwkB6PKloyl8lWWW98agrzEXMrsatq0pDYEnPSliBO2VKz3A3D3qQaRoK/ltOtsT+w5e6W38yomg8FNyF5ydl6Qo35mLI8R/I5Red6M+RVk57RZYkeupVbXVCw3W6bs2safl7PyrrP5GUME/Fs+w6vDJNTzUo8yysLYn2wJtsu1rXkNiTTYNsCeTLHri3rUybTM9H0FOySW51EFUOnSyWZ1FZJ+DZPEbG2vhSbnd4Uk6Cb+YW6RL1ojmMrf9JsorNLX7ir1w5SccR1z++CHLUtfyBWoGvsU9BP87VCnl3ZF1zlJE20RNM3ClosVhEnM5e6QUnumuJcd+BM7OJWfmvnsCmfmbgWy2bod8puPV1xDAZC+VKpUSfIia+APjrni3o5VLdqxtCYfj76K3fJtdxUnqzxsMY4H3cmR3+bMReTo8n8uIsxzxdVMtKWxOoG9yAuLK1L3mt7rHC2AREHh4YQqm6XeZQirCirQVn13O5WIDzKQBf5VmT5eU7K5QnspM2G5lSsjVfXhtwEmuxFvqahK1YiowlTivlUIEUMZDwqZCBfOZa9b1Evd8PTBQbGdVYUW9AxQ8iQ/U5bAE/OKrA/Ycy5D7q17GoKmtqF57UKQV1W+RZ2Z5mWBgQ6nwzzBERiMr922tqjNlRTyJFO9dtzkwzyUs5lwVtV2mRGc1y0nmU1NScdtbIzK6J9EZathK7k6xFdnGi0Dw074aQ5UzeMoGZcuVgI5WzmToJzo/Qi7m+meC+E5OwwGJUZ3sQpvdrQ9DYBVT41iDUdOg2BxvYs2BJHk1qqES9M1odge7pmRKT219PAt4ol4XyOBftip+ioV6O9cPP2EaGEXloGvuntmr2zD1VC0eeri10yGpfZWhAJy1APDwXfLdwlbUsTfgOsiTwh+o4lSZGtix7w7H5d1OSkWhL0ZGuag2XGsxt3GKTYaK61oue8vtKFzCAPu37WX8PzdK7VN6rwNvOm1y5VQi6wiMuOGNzcHg8kKlgB1UvOtaotbybCcKrzSjdvynxLXpf4/mbPBmbP96wnV9Yk4A4ApRWhWx3tq+c3JxWnDZaHfaVvLdi1XJy0CWZfJiizGDxwPR03c1EKgHuucm4P8Jkf7lnqsjGvtn+j1DA93abCgXRJ2EDtk2Mc9lzl1kx02VbmhZmFWMBemVNYXNz9yps6Enbi9xypBY1te/56rZmYf4Vbce48m0Ys2TCLfKotuhhmmTO5NeRq24dW4LnDIbtVq6mKNvZ0cQBqEXkBes0jrKIy3sdomsBuxz7F5rqN9nuPzwZKRFfW4GJe4JlXc3G8Yke4195q+QZ08xl9qOZFmqyjwPG5y3pp3iyna53J+tg3AWdcOBirhXWddBeDp8gZ0S0YjOc7GUuZ4xaliIJlRam++R5+wPIMTW+hc8Pkg9cK82h16azCa7hVw8WYRGwLZnXaE5JUVQGfHWoPL7WybSiL3MhtM5nVJZhpMEHLAnZjJdw4bftTZFIzRgjnwSo6HqdrfTaYV23FMJsjy7NHK5Rv25Uayxe6XJCKk5cYeYkU5cr2dYq7Czk+g2m+wVyNjoBSF3N0lk4PFCGiwYmBxS6bHIjtRDwt3JVUTtoOPUc3ZRa4Z9GaUdIhW3HGEvNRa9CceGnN2utgMs5qDhvzm79FvVt+OWGQKMPdtpaw4HZ1cdhxs0nbFax/vZjLa7zhyvNhrFV9Q9c5dVupXlWWClXaF/qWT/E8hIlu43102O5ThmH+8fLpZTzAfB5D/uV3iOOJ0//awdfjjOrt7cT9EBI4/pe7ri9/3bRfPr1UXgwNexz21WkbPo/E/umo7/O/e7g9Shker+nGlyp983aK2zjh+IsnL3Hut3VTDd/qIm3vh46fXty2Hl+A1+PvSHjw++W+yKwcz1KLJgIV/B7NGd+4Q9vHt3DwjuNfRxDGI70RhG9Fnt5X9DwPHw8FxwPxl9//C1vPyMGXIwAA -->
