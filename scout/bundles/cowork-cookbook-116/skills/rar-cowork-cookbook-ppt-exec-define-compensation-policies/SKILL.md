---
name: "rar-cowork-cookbook-ppt-exec-define-compensation-policies"
description: "Generates an executive-ready PowerPoint deck on define compensation policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_compensation_policies", "rar_sha256": "cb8611accad6f58cf6e50adf20054fd0890d29a10a9252c39b5e9119456fd10c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_define_compensation_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-define-compensation-policies:410561fbeb48f823465b875b4a3a76d67e64aaf7faf12c258b3cec43b448f22e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_define_compensation_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_define_compensation_policies_agent.py` is
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

Define compensation policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define compensation policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-compensation-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_compensation_policies_agent.py` and embedded as the fenced Python below (sha256 cb8611accad6f58c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_compensation_policies_agent.py` first:

```bash
python3 ppt_exec_define_compensation_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_compensation_policies_agent.py   # or on stdin
python3 ppt_exec_define_compensation_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define compensation policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define compensation policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-compensation-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_compensation_policies',
    "version": '2.0.0',
    "display_name": 'Define compensation policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define compensation policies status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-compensation-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-compensation-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1dac3e911bdeb58f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/define-compensation-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-define-compensation-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDefineCompensationPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineCompensationPolicies'
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
    print(PptExecDefineCompensationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eXOjyLbnV2H8/qjuh8sCsco3OmJAIBACAVpAUleHi31fxCIE/fq7TyLJrqrXfe+7PTERI4ctIDPPfn7nZOLfn6y2CYvq6fVp61k5JFhpGoVeBVm5C82LrqgS8FUkNviFnCJvqshum6Kqn56fXK92qqhsoiIHywUv9yqr8WqwFPKuntM20cX7XHmW20Na0XmVVkR5A7mek0BFDr79KPcAzaz08toaqUBlkUZOBEjUjdW09fNtNPUaD+qiJoSc0Kqa+iZaY6VJlAefyxvNvAB8X4BI3tUaF9RPr7/+9vwUgeun19+fnNSqwaMnrWx4IBh34zz/jrH24AsopFYegKllD6ySg/vSq/yiysAjIDD0uPup9lL/GfrP/0w6qwrqn1+/5NDj8+Vp/Nm0OdSEHtQUVt14LuRYpWVHadT0LxCTdlZfQ5XXtFUOtAHKVkCVl/vKb5SKEvplHPvpzuQl8JqfvjwV5WhlIPOXp5+hogL8qna8fhmplD/9/JKOpv7p52906taOPacZiQGpX94e9w+yYOK3qZF/4/oLoHp3ru19efpOufFzl3vUE6x8eomBA366Ey6r4uLlVu54P/38z8g6IXB/GtXNv0X31zvhEMQQ0Okh+M/PNyP/BsEPhT5o/nO2JXDr39EETH9n9ww9DPXPaN/s/99IpyDA6g+L/yW5v1oA/wL9+k91+1cLniH/yxPnpSDjKstOvVfo97etxs9//eR+e/jptz8A6f+RzLZoK+dG4S2z8sj36ubt7ddP9e3xp99+/dSWINY8K3trq/SvaP6VXW98frDgY9ZPP64F/Pd5khddDn1EOvR7Uf6v6o8XyLDSyP32vH6Fvs+X8QNDoxLvTO8m+C5naiDrd3b8+ekPABI50KZ1bsMgy//jPyAlcqqiLvwG2jpF20DAwU2UeaPwuzCqod0jqb9uV0tZfsncrxB4OqY7gAirTRtIqKwohUA+jB4fNSh86Ov/dm5w+tl5wOmkLJu3ESjf7lD49j0Uvr1D4dcXaBcC3kUVBVFupdCG0TTICjwAe4DrLT7qNvt8GRkDoaI78GzmyxF06jb1/gF9/bc4vd2IvpT9qM6XHPjHAnMB1HpZWVRWFaU9ZI14ZfeN9xkgLcCUqkhT2wKAPv5py5fRRmbo5Q/LOR+lwIPSwgHS+xFA52fg/LpILwAfR3vWSZSmkBtVwFhF1d/wHdj8dST29etX26rDL/kdkDHoXnLqCZjwITD0+XNZeX4aBWHzJfecsIA+/f7HJ+i/oH+16kZ85KGB6nAzGgjqFJK26hoCGdpmYFoNjeEB4Ofmwd//uHtjlA4UOwjkVeSP5aoZPfRdOIwa3F307h+g8yiiVz04/Wg3qAuBXaCoAdYCuV4/f8lHEgWYWnVR7b0b8b74bvp3h9/5jD6pHzYEfvKrIrvNvUXi6EynqNwXaOlDH5YC6gK/jvUUCot6LMwgJlwvd3qw0mq+uRBUV2iMldrvn6G2BqqOlL/agPRonAyAlNV8hZS5BupdkYI/o4Fu7MHqIo9Gxz8i9v4YEKk+gRhj30m8QGsPWBMqrcoqw8qqvds837pHBKhz7+sBcQvKvQ4ai7s3+ugWxbfI4/5VS8G/tyTfNyPc2Ix8aacIikP//xuYUQdGEDa8wOx4DuLXu83xHnBj5zXqf2/WQBsBgTbknj3fWot3FHrH5y95GgEnVf0/7jP9W4zd59wxr61AAG2YzY3+mO3VjW7UgEgZXV9Voy7Wl/y9EDwD4wM/1aOuIKGTER6KD4bj6LukIcja8f5bUwDdg3DUHoQ3VLY2sBXke557y4QmHC397gwQNt6YcyAxnPAHrSBAHYQEoD86IQLmBMXiZro1yBdg0nvwf0yPxlYLSOG2DpAWJJT3ApljfIMYrSHbA/3SOAdY4dONFJR5wMZAxA8L16FV3oUZu+GHgNboiyID8fK9Bx6DwSOU3G+JCKhartUAW3bACSDPrnfPfsj58BUQNhuT4rboR3c/dIW+r1j/GJMRyPitIIAGfiz23xkHIHiV3aMOlOGkBumeeY8AApFwq+sv99J8r/0fsrz+aQvw09/bJdyK7f5Hz71CYdOU9etkci+I7/XwBeTKBMRIVHr1WBs/jzn4+Z5ln7/Pss/vWfYD8butXqG/J+APJB6R/QqhL8gLMg7JkeONofv4AHvMP7PHz/g4+iXfeN8c/YiGEesA/tr9R8l5nwLqTlB5wTj5XoLqsXJ1oFjekO9WQj6C4ZEqAC/yYKyXdfFdCo86ja69e+4DocFQPmK/O/Z7gTduh9JR/Np7es3bNH1+yq3M+ze3QSMQg5AFBhk3UCB9QAvVjEPg7qOdGm9+3ATeEgsgglu8jvkFih5ofZ+hjy72GXrfV9x2a3kLNla/jh30yBJMBV8fcz92mLb3BDZzTV+Owt83S2Pj9mio/yzEmFZAYscby3rxkacjxz8RARdB4FV/JqLeLqz0ARYAz0fkBhX6keI1kNMF3dUzBNwHUg9kEwDJFiz4MxvAp/LOLSjO7qjuN/t9U6u46/LHzQzNfcf5+9M7aIzX907hHjrjBvVvtXSjXd9L8dtI3Rpp3Bqvm5lvbesbUDEaS+53Q8HYP7zdw/HpFcCO9/w0GrOKQC8+3DbaT3eRgC7fGl5AAQDI53psISYgmwAlUNjLUQ9Q9dzvGIyPI/c2f7x4/asu+X9GglccRQgS9W3PxmmfnmI4Sdg0Rdi4hVkU6ZKUR+KW5VO+5aNTZ0rQNuZ4Do7ZOJg/nXpAktGjmfWQZIKOvgA6fBj8/659f7oTASVkSpCAimPTJIpajmO5pE/Qjk96BGK5/hRBCNx3EXqGuNOZhSLWbEpMHWxmE94MRWc4QfouijgjvUfveJfs7b1Pf/fOHRVGabJolHtqWQ7tUCjuziiLdDwMGVVHp6hLYR5CzDCfpj0crP9Y+vDQ6MC78mMAg7YRNG2Xkc/vD4+PQUniYKaI10vm/plPZoZFHZZ2cz3MBtJl1gNdSN5uuytLtUe37kqWay86TdeybO94O7RlgVou06I1As5UsnoTr4mIu4b5eZczTaDJWX7anf1dtPemZ93onAM/GWLk0PfRapNM+H1pzU9muYtcqVuhB2mVHpY7puKGBl5Vst1vKkZ2txckPK3S037GuzUKT/zkMEv6vZ6rsmdfk6JMSPQo59MJOc/ZE2NrlG7Up94kWknop/zCu5rT+CCj6dVOSnro8aYyLTJLT+vTqu3sGLHygSDcPKYp/4DBoTSd+CJG6PTVq6aZjASVgleGu+qxJo2mxik/NpzT4FdjfUI4jT7FAlEV/WIom83S0NYz/1hpGF/OZwulO+pkTe1N1a7py2EXqUcyyo2wPE5sR68402UZeHpht3JhXnnaPsXuXBjSrKDYc1WZZ6yYLYRh2GPW5DxD2lJI5UFh10q0H855gk+6C0+EUnXcLxOaiIX8cBJ2ebiQ2VKoJLtxehOGnRAReqyUaqUiecE1mvlJnRlc6LemJFc72z1J1/0c7n30miMHpm6OF3uWpW1Gzladwe7OaWsHsKDkkYDwttRqZq1aawumpaSiYJVNfMpgQ23bAO0qnssIA18hYRx5Dt2IDcWS2bHFsFJt/Jon9uKSQ7AWo+QCy9l5dbGbwL1oRq/mgjHdpMRkGuHzxJmiGW9aPKbV+so0cLtJjzbvLRd56qFDsK2vTVDNqIVxUig15S7nzJAPK5/sC9SZRz6jmEh8HJDE2UWCaBH5XF4Xjg4fJ26OoKdpU60G1R92K0xhLtUx2y04lg9X00VmmGaeCuguRyY7PybWGTac+8kpyypV25P0ZbnfXXNuqoq0qSnaqhmYzcLyQewT1/VlkoZw4ihxRCyIGa4zklxfskOZlqnS02fL3CkpbrXGImqtnAsumR1byzK4xjwmsZYyZXlpxbDaKtXZvbA+yAZXqJ6rU9wSb5mNqBxXETLlClFpE0NkE5ZGThLSboqkYnZu7EU6omdmr+JFnMnrFXw+G+s8DNciP8w8usAYUgsririW+BXrt/zS29pXMakIMamPMd4z6VRa8v6eMm2JypFUX2C9vZYrep0tmrJLa5LSdpMQLgVlAyvlWhNDUx2wy8rovHOl7OfRJmNrnlRXWag7u1mAVzqGrKMjm2QHPCeoECetnkq1jsdQb9sj2/N12cgcteHhYCWxcxDIUwsMWWtSHuRdFyvEmqYt58KTQkVvpSIVRHjbJg3og7CyOeA7B5FgdlmFuxobZKvcDtdSyuJrWRxVKRRTboM2iF/o1xrenAag/hGGyypySndYDnNXXqxOcBdRVh8Kg4+bfdLqW8+UJ6G+Ybs2XOnUxU1Cd0tG7cHhI38pdJzpc5ddmO8PxikGzt63J8nVh+0hPHkntJKXB+9atPbmup1nh9jgvJKItICzY9rv0ao2E2GiDTyRUjo8TaaHcHIolSqgGUKRNZPdozSzoKjoWlHSyioMatcGA4cVyx1mT66bViS6+EommkqwoNHZ84ulbZN7oehgJel6Il26dHJW+o7OkyvweoZJJCcJh93FM689qw41dQR43tnqsldTlYgI/DCgEzGOC5RwWwNeJecIRhxHd5f7fcDoQBuQcXDsVBua4fMwbTVmCJJwa0Suu5+bqSZMZ3Ib7XNOVtjATAV+TxaCYWhGGkZ6MwwDw/ClkCwcojC41czyFhvcmQEEDkqGdE/4oMuswcjcaXok8tM0C5Ewc13fbmhKG1Jyom63+jGNl9vTDIPX5yTpJivsnG5tTU/EZVGrmnnJrgN9YtbpbKAESlGFSIL90wJeXuIrnLf7aDLRlJ7ly+NCNnUSteBmiyfBYtUtyf3QiPlq3itLWTX6la2SjBKvZ4SA4vOI3jlMigiVeihk4ZhtdiYmnfWywq4LY6kj+c4Mtx5TmHmoLD2cySuenO7Xpnrm9F27J9uMcbvDZZ/utY5SwMZhpatli0QiUkbJ3D4mx2yYHlP9kh+W56ycJyJ+JepYbsKWRB0i3xjnPRZHTYvScNSeQng5v7LJkUsH+djOd3mADS0A601GRbUsKDx15hrS8NASmcTHXWi7+hHeVu2wwGbr5CRKxLIWYJXMNq5gKZym9ju4A3G41BPZpfcUoV4DaXvlCFlR+lxTZ9d6OHnTyDO0w0phqGzDTmM/2zOzRLUD/zw3qFVlXpGuY0kpX2VoVciWKIRCuOIl37TUHSMlzZyNtOwSchFB2Dq7HEQK5yMpSuylEjNFdO27fu5RXFJ5CzQje0YDu99id9rXHR/60935ENWIVcfruBqkYB/rkmgMhSpMDucz06jS0hS6jVS1wU73cBJZbLpjitTEpnLncTLJpYTMmIHMpmkMxDpU+3Vqt1jar3V5C2IUieXjZXYwzkjIExiOCIlYYCsU7dlq6RWwoshZmcp2LWAlsk1mAlMvDNM/zg/mPkREBzYc7uCQ2CbehRIWim6QJ/KuCNE00rfreSrFoONMc0aPLtOE9bXYjqhZsU2ugz53y8lkys7qs7OW0eysbrgrWQV82Hmul3FVqdmotDNQg+WkgJ5pmL9DYfHcrUT5kDUsSFBSWnAKngdTNdtIFDJV12hEuv5h1cxUe+qrEZ4ftrpvU5eDxIlIfww2CSUYWEkzy9Ti5yEztTzXnQq9QHOqo6XnWulRZomjYk+2Mh1z51Bx3cAN0OXaRyjCKmKfxcmBEMx6eTQWG/RABCt1NnGajUZS5AqVhdilV3p5BjbU1obr5Li07QRmiQ3mJPHYYr1WuIOCn6+cIeVDxG4H2tCPFBFa5SDBc8TawcV6z5PEWprxGbxJBhI7u0ieHw1f1whnfykG+xpgubGlCce+HjWuDtLKXGwA7HTYYkuw2CIrRUpgtjzhbU0uPZELkZaMPbU3WGp7dOIzMd1O19I1sQCiGla79eRGMEV8sY+JkMEp1zoqxGQzQ0tbHdLNOZQJ0GBendQeukUrNJdGlv0kzIMLsVpziNTqE8vzASPvcmSy03A4UpUwW+sKlWcCOpN3EgZLnCRfsXVBkoedbxx3yymZO/OzNSvRSsuTTVXyDNboXtC2xFbZZoulsgvjox8cFZ4+VKLBXfUVMd0kzcbYH6dSVbOEMAm5Yklp8BWxyH2TzVbqgV5dGtIDy7vCwIyzzpkw2kj6vF/Im/Ci8KaEGIwQ6TpaqPtCrhfnsp+6cr8h9NVigSXcNke1lXdump5kPZG2t0snaoRjfjpRgSGc17Gs01N+uOJW0xL9VnI6aulqV3lVY66zaIpVcIFlI2DVIhTcRnElJ8ZU10lwJXRVdr+68sFCK/fVYnlWyKOgmUpHuKXbtsw1L0VRvyxp5pCwCTppTybI/lydoPhmxSvd0icJ4mhq0z7FmIZpOHezvkSOqM/0fU2tFWLoaMGXw6W83q7s1uEPJ4kUWsbaT85Gvl7oLDuzXU3an6fNZh1yoHgcuXVAKOwhwxmeNrly6s5DfTipIHO3DVfOME1KbQ7V9+tCPcfR1QyFyUKxTYfdKclyga5EWjmYAeIui27rRlEw5zZdhjTxkDcbduuryryaX9LQM0q39v0BRdBWnS9wfiXmB3TN7qTVsrB0m2h3szNwb00s9/EuZeDVoe1a0K6YxAKXqNL36UONisuJBzYeF7ctpw6smdtyUnMB3A7aGfNSjwrwS9iXWFU74hxrwi7fr/nA0hEVcyxqFxi7qmQMhVoj5mbChqDblsdeymsD2LpS5MGqnJzi4mAj2Jm17zdapO4i7Gp1Etmz1tVninOHiZ3f7U4YtlZY1u58xIMLeq4NVFKVVj33y2ZmCcz14ooUe20XnIxZxsmChVDB6oqiWrCrE2ckF3vzg+571IX14m6Va8PhgFECh4RmcNpnE+0M9hRZ6voseVxXhwaODrs5PIsc1mMmms6H6OK4xck0iczUbNxlMwva/aQQbanoFOLiLfgdkK/coAQeq6nIi6lCFWBPQcS0uUFcqu93W2rWX1o3YgSyARhECvHgdFaL4lzikDVtrFW6JLD5caEpcal0PSi/K/qExteFw3ULylkPKDOp3KJV6d4Kj8QMPFtOOLe+tLDeimdiMTWvJSOIA8oOGLWEc5zjECUz614kzlIp9V49cwWYMMOJ6dqRD4P4wPujgW05X9/JOrs7dch0EuOk2Fy0wZseI2pdodNgEfPbddfkq9PUL0hPzK42qk8qbMEmnH8WHV/DuKmGwfvBZtebQJoQqL8uuh0RG3S7rHet03OZhKWdwB8vG5U4+WsZiVi2P+LwToKJ2OWteuW0+4TmmiVLH6lNzu/1enE9JIztzUAjw1MRlhPElhrAjujCeBYbyJYiH0OURZVMm1lrMcdo70qJE13cB+mRqmeXJjCuxNHl58ezwyS663uZCUBt6S+UxdaZXKa8da7sRFJ52PA31t7CeJVs2mwWeRRJHYNmmnZ76kQhe3pQ46u19FMVldMYg4tB5dGe1OYqDS8ul1BtzmjvYmqbC37LcpG4RhSp2FV+0bkc3qGuOhd54sJ2mYGg1fTqUo5Jz04xpiNsCjqkHifJWRW6iNoeXfTQ7taai7WohTgLHYiy6lzR2J3nWND58wsjBKS0gq88c6nlerfsloUIq3467zUzEsUrqWGScobPJ9DI4wNT+ojq4oEYijaWBIWIoe0UhokJFlHVZShJZ4ENh5Je47UywVCaRLk+Wgxyuzn2FNJUM6foKd0SM3cPGgIVbyJqsobrM6raDRxPKLma5ryO5X5noq18QNJgwu+9vXcMspjZTw3evdLm5cxelVUFDK6m1oSYDxQcTBpMX7OsMgfFYjFMZu6KDorUrewYVw9m5i0ql7Zw6RQLbYr5e785ROv54tDQOOOFkxPNMKiw6fIoSPFitgpZnbQsr2n1ngQhA9rnJm5KuFrsOSaUOziEZV71vIKfiRwOr1ZkM/fgnUsEBMOenFAPkWKLdOEAavVlBTCi2SokM7BTcxvosEE5VsL25iyh9o6m1JwoOCfNS9s1dwkodDYwaWdySNVhhGVxlCiVcIPX+myIcKchVbCPYveZyGBsbXft3MCsCPRE58uZY88iKfWzBIsRjO7EbKY0LM5wLiHEm6nerOL5xg038w6ZeCI+p8ly3u8kLl777iEiNQRbO+41mcmNETlweyTESSdcU2+D59uEYZhffnl6frq94316RRGSwJ6fxlcBjwP9v30WHAxR+fYgh1FT9Pnp/90B5f2w8P2l3+1437Pc1xv3178p6W/PT5UTAanuR8h12gaPg8n/dhj7+d86JR5J9Pc31uNbymvz/mKksYLbSXaUu23dVP1bXaTt7RwbWL2tx/9dqd8erxSebupl5fh+4l0dcBlGlffWFONxLLh6Gv+vZHzt5rmR1bzfBo9j/+cntweui5z6DSOJN68qR00fb5/GI9vx9dPTH/8Hfm/zz5wnAAA= -->
