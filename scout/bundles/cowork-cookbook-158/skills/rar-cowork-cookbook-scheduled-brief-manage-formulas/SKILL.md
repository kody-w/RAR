---
name: "rar-cowork-cookbook-scheduled-brief-manage-formulas"
description: "Schedulable morning-brief email summarizing manage formulas for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_formulas", "rar_sha256": "d3521fd4817d81db69336f028297228430441852524dc0d834c71b41980b5190", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_formulas`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_formulas_agent.py` and in the RCI capsule.

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

Manage formulas Scheduled Email Brief — Schedulable morning-brief email summarizing manage formulas for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-formulas
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_formulas_agent.py` and embedded as the fenced Python below (sha256 d3521fd4817d81db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_formulas_agent.py` first:

```bash
python3 scheduled_brief_manage_formulas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_formulas_agent.py   # or on stdin
python3 scheduled_brief_manage_formulas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage formulas Scheduled Email Brief — Schedulable morning-brief email summarizing manage formulas for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-formulas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_formulas',
    "version": '2.0.1',
    "display_name": 'Manage formulas Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage formulas for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-formulas',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-formulas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e393035e21427f17',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-formulas'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-manage-formulas', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefManageFormulas(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageFormulas'
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
    print(ScheduledBriefManageFormulas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V66ZKbWLbuq3Dz/LCrZSfz5I6OuAjQABIgEBKiXGEzgxjFIEB16t3PRlKmq7q6T3dH3IgrOyMFrL2Gb417k7++OF0bl/XLlxcjcApo6WRZEgc15BQ+xJd9WafgV5m64AfyyqKtE7dry7p5+fTiB41XJ1WblMW03IsDv8scNwugvKyLpIg+u3UShFCQO0kGNV2eO3VyA/eh3CmcKIDCss7Bimb6ArVxANVBU5VFk0w8yr4I6r9CQEgSFYEPtSVUdwXkA14jBOj7IEiz8RXoEQxOXmVB8/Ll518+vSTg+8uXX188wLj5oVfgzydltnfJi6dgsDhzighQVSNAoQDXVVBPaoFbPlD9efWxCbLwE/SXv6S9U0fNT1++FtDz8/Vl+qcDzSYD2tJpWqCs51SOm2RJO75CXNY7YwNsa7u6aCAHagCIRfT6WPmDU1lBf5uefXwIeY2C9uPXlxKo4EwQf335aTL76wtAAXx/nbhUH396zco+qD/+9INP07nnwGsnZkDr12/P6ydbQPiDNAnvUv8GuD6c6QZfX35n3PR56D3ZCVa+vJ7LpPj4YFzV5TUonMILPv70z9gC8L00S5r23+L784NxHDg+sOmp+E+f7iD/As2eBr3z/OdiK+DW/8QSQP4m7hP0BOqf8b7j/3ess6QImnfE/yG7f7Rg9jfo539q2/+24BMUfn0Rgiy5gugA2fIF+vWboYn8zx/8Hzc//PIbYP0v2RhlV3t3Dt9AXiZh0LTfvv38obnf/vDLzx+6CsRa4OTfujr7Rzz/Ea53OX9A8En18Y9rgXyzSAuQ7NB7pEO/ltX/qX97hQ5Olvg/7jdfoN/ny/SZQZMRb0IfEPwuZxqg6+9w/OnlN1AfCmBN590fgyz/r/+CtolXl00ZtpDhlV07lZk2yYNJ+X2cNBD4/yhOANdHbXrQgfifPDxpXIbQ9//r3cvlZ+9ZLuHmrfJ8u9fBb4+q9+2t6n1/hfaAbVknUVI4GaRzmvZ1oijaSWQFimFQX0Exccc2+AxWfZ6+QEkBff8XnL/dmbxW4/d7GU8etUnn11NdasC618m2YxwUT0s8UPmDIfA6wD8rPaBMmICC+mkqyGV2BXVtwqFJkyyD/KQGRpf1eOcNsPoyMfv+/bvrNPHX4lFIcejRGhoYELyrA33+DKwKsySK269F4MUl9OHX3z5A/w39b6vuzCcZGijoT08ADSVDVSCQWV0OyICTgFtB2bh74tffntgCNqCJQMBvSZgEj8UgMtPAfwPaWHGfMZKC3ACAB8DNq7JupxaVtK/QOoTe9QVCp0dT/Y7LpgV9qQoKPyi8EXB1gDnvSBZlCzUg/Jpw/AR1TXCX+t2tnbuKOUhxp/0ObXkNdIsye+trExFYXBYJgP89DB73AZP6QwPN31i8QsoUi1Dl1E4V185TRug8/AK6xNtywNyBiqD/WkxtMZiguifGAx5ABJDxni79PPkc9HjQpgu/eZN9p3Gmnra/97b6a9E8g96pJ1d4oAkAoVGX+FMr+OszpJq47DL/jl/waO5PL/hPr9xjcPt3g8B7s4bE+9Bw79nQ1w5DUAL6/zRhTHpyy6UuLrm9KECistdPD/ymeWjC+TFCgWb/FANy5ccA8FY+3qro1yJLQDDU418flHfUnzSPytTVQBmd0+/8gcsBfhPfe0ROEVbXUyw7X4u3cv0JOPlem4BTQPqmD1veBE5P3zSNQY5O1z9a992DtT8lM4g6qOrcDEREGAS+63gp0KqesurpARCewZRhfZx48R+sggB3EAWAPwSUSECeAHTv0CklMBN4JKzL/Ad5Mg1EQAu/84C2YOAMXqEjSIzJAw3IRjDVTDQAhQ93VlAeAIyBiu8IN7FTPZSZZtSngs7kizIH8fp7Dzwf/gjluy6T+oCr4zstwLKfKqsfDA/Pvuv59BVQNp+S777oj+5+2gr9vq/89Wtx1/G9mIOcfsTtD3AgkEt5cy+iU0lqQFnJg/c4fXTf10cDfXTod12+/Gkw//ifze73lmj+0XNfoLhtq+YLDD/a2FsXewUFAQYxklRB86OjPfLu8yPLPr9l2R/YPlD6Av1nqv2BxTOmv0DoK/KKTI82iRdMQfv8ACT4z/PTZ2J6+rXQgx8ufsbBVE1BNrvje2t5IwH9JaqDaCJ+tJpm6lA9aIr32gqc8LV4D4NnkoDSXURTX2zK3yXvvccCpz589t4CwKOiBbL9aR6Lgmmnkk3qN8HLl6LLsk8vhZMH/3qHMlV5EKcAi2lbA3IGTDdtEtyv3ied6eKP+7F7NoEy4JdfpqT6BE1T6SfofcD8BL2N/Pc9VNGBPc/P03A7iQSk4Nc77ftmzw1ewBarHatJ78c+ZpqpnrPun5WYcglo7AVT5y7fk3OS+Ccm4EsUBfWfmaj3L072rBBN60x9OGnf8votKj9BwHMg30AKgcDswII/iwFy6uDSgYbnT+b+wO+HWeXDlt/uMLSPzeCvL2+V4umD5+AHyEFKfm6mlgeDKAUCwfUjnsCz/3QkfC4HpQ3MJNMWFCcxNPQJBqV9BvVdisVxKkQwBmNpDGMIHCEIlCExEiN8D/EZnPBo1CVQlkFcEmUndR5B+W1q68mkUoCEAc6imOfjFEaSBIvSmMP6DkE7jo8wDI3QoQ+q/4+lKaiLTzsfdk0gvk+nEx5Pc399cSkCUK6IZs09PjzMHhwKo109dmc1FZxsC167iXnJcGdz2Dsb9ULtBZ9PI1vzy4Jb+GmiVnJaCc02pp1kGe1JsaDnWtMy5JYe12Y1IglzTAD9upDSm83QmcoythwlPLLr7JE0DQNVOiodHGZf2Rd6rx74WlUyqSDSvEIPG4ZtuuvtlGy3o4lVzYBeq3qpyRVRXRB8iRaXAl54LmcbjLkwnfEg27tuf0SQ8bY6dmPqJYeDc/W6wVoewA0zisHuvofRSzVivXtOT8WNpPzihtCBpWHtPqZngcvMUJ6JnLNISpYsjyuQ0ahsHXFWai+yPj+NaJyyPTZDXBQ/XTJ93DIVYm2rccbEirWsS8Lxo12Fmv4uU24prB7dm4lIwoJKSvM2NutNsYjk2W49Z/WN7XRSqkpydnBca7nLO2tfOBvnjJiu1rp6PauR8mZbsm1TO0WX9lW6yandWaNu531yiC6Zdxq7k66mEj+Slrrv0WHjufhxtOpC42RjHHFpkc25A+k0fKWyihCF8IZrbo7jniX1yF+7wt+tWZSqzDKMu43Rjd1wHABM6M1bDcM4rN253uQE6fTsBd1IfV7VQ4oaexvHhrQKq2NFLg/RddVrq4OcKqedhCr26ItoLVEFVeE3W+5Cv6dMXRSyW4LR9NUshmVdbKqzr8WXwS0j/CjlbEGnEW30CQCj28xTJ5gZ1uFyU/T6MHdM1Jei6ijO1miI9Yf81O57xGOV4DQOGTuwi1qyhJuwiGvsRBSCHOx7s/F6A8u1daiEHU05CX44LKzTLB+PzFZb1X2jN3YZrS0johsEOXbR6HbF6CjXwsxm5VaZB/CeXs7m8xns4SJ8nYdBz0S4molmARNaveKoMNyw7Gq7PTfkgUTP1yBFjjhRETI2GNRFHhvMlqVFUJsXtPSa/aw5Lgddj89LqQMxG7QMjozSsrNr0vB7vmNXsnVO+Zl/mQmJJgSHZn6WZWz0nTJ2+5M5F5eIqZsoplcLYrMkl/464fabi94ferEyRll2mltP5EKiXzXStGNfGw8e0yGMeS0SImbFfRbqa+Q6FBTbjrIUcByN57OgYstj7g/LczhqXDtgjbXO2dMG3g+C56gKf9Yt0vJWx1qG0zHfoIN+lixGazEmcWrZFc6Gn6wU7xgs23a+1mVGYNie8RXTXxaRHpbpYUtf0sG8pBcrqeiqWEh+pZcDCo+zXXKmNH/d4jK3X95whhoCXS6vQ3/pjieNlrNFQ1lLVrnAtXuM5VG3D0eX41KKclXGMWxTvuCKZfSpd7lS63GDluqCa/cZH5RLbTeblVfeHfzNZVAPIiH7s3VGoZUhmhp8oUTHdKiDwCbCwFmVvuADFHPIWivEwDswkbHBeuFoJudiX1l+k29Wjr3HBIOMl2cCY/KtQ2LZXBqqi+0fKEFdpT0td8gwlj6XKxUFy8cGpTzXg8WkuGUcje33QcF66ZDwvNCMzUj0OV4uQ9g8KqEhu6jROmy/2GnuGevRdiYtd2Gm0IKwdQP4Ymx3SkSNt30fYLxnq0mmdcZqoZrHc2KtzvbVjkQEjZv4htZlJhGJgqDaQK66+X6f+CKpjMNmIODETrV2b9oy7ZqkUmC3LBGcm7RWz3NzWypipxcnMd6Ti3xbz/s1IXFmUp41KZq3R/LqBh1+0tOttRNbx/Q9Z32ziGzMsXiJq2Qjx9F4TJOuYW72TpG93G0YCSdI+nqI58Yw6288HDtBaDhFQBP+3C6kitaPxzDUQMwEcEGdRYNX4rz2fLddkYq8TWry1ul5M4bxTrzp5TFUYI0reJin6H2GLYay3LV74XrDGBbmNmwgzMh+NrMUGkaiQLYGAwm2TY2jpiemXI5JC2OplExmZ4e5NKc6X5eK3epEXtsyOScdVvKbUjl4V26HD16Sg8G2Eo9FIKJexO51xSEXON8ZvnhdUz4fRGekOsvnLu87LgoPF/tyChH9yDjZaSY02GmGjrs1YR8dtTxtlmdp2+8OdJquC+c6n13XzIbAyGNrIMSRLkdUtru106AF1pVj7w+cuG42S/Pq264eHOklbw9nJVe7Zb7enhid2asnQdFgc2FfxYzSFzjNWQqmSZoEukNonhfr0jw458RLzVWnNFo7KEPcx0pe04qW6GfOyM6LIVZHJkpWeb1pkI6spZqATztb62Nd3zlDTF5so9zIkZHLFX1B0L0xR/QBDVEwc6TtertbBcrS7Op8kaVb1UO2/KUzWmK2SfP5Njc35Kk8VOXIrTeNYsSbfqtFaSCT49LwJay5CuPiaq63cnFaRNcLfTnMm8Fhz4qw7BV1rm9D/pofmbBuvazkiUwcdnYgxj5O1K0vD2nNW1iaLI9SW275XprZ4yLl4QBDtjtMMlhnxtUhdrq6yK5VzIbqRVoBiZ/t0l2xpZclEvlbsl6aCMvOKF24iHhspDVz2gWFz+9T62Jd5LWx6YfFZqjXVe+cgsw5Ojx5SgtFbDEh4LK1zMXVYlnsyqSkmrGye3FdUxVn9QRGdLAjVmsP4VQqhNnId8kV7Ckn7JzuumCM+AWhyR0+jEjqUWmbUPJZqlCmnePwbSAJvJ3p1dYM97S4OsaYZrJLT+2Bl5RAG9prExq1QSpdxXo3Nt+kPn9h3dBzrHhetVJvG0q4oQuJE+eSMN9Frq9anoZ2WcHdsBiJlSgHbb8Ty+CKX2hp5+S02HD7k2IIR0VVzYt4a1ZZ7q8NNDmbkQmKnCefC8+SkKSyrgbPoupqQ3qXsqcY71Is56FZeVy03MFJR9rmckGptre55MVlwVmShvC71usu6dprbtpewsZorqW9bHPbdo3y/jpGw0G6moratWN+rVDkkBNzkMgSZTBMriiIeV04x86hCUUzt016SO2NvDTrfK0W/IHodid9vc/I+qSg6Xqx7ui4HCl9X4LGhImD6m41ssIWWaMTJh8oeSASBy/Chy1FS7pCeUzFRyrWOMcbPyju4UANEl9K22J7TB1shjX5zMACHkbW6HUXkAJbkox0ICk22trXrSJuagFb+NLRuyiXMcDOBWsYprU60TqKXHLawWTRh+WizIvQK5tqizPhXOM6GZPKTSyxut2sfRVZr3hjjdy6lCgXzmg68imhcsmwx9TaYt7a50ibxNHikDqCdWUxG+HOcpPjjLpHPfbmoxgqaUa7023Wrc2FYS6YzEG5PTEPEs9ezxsztR0hT4QwM1IiRMtjEsixyJSp2emkURy6LjAXeCK1TjzKWMZ7oH/EadVgh1ZoT3stH+ZWqM5Sb17Ndtvj0UDFHS+nrGkx8UbanfPQumCdl+MrVspOtnrQqnNEpuXZ5iP7srotcGVlrZcpX2W3W70rA2IoSEQO9yjF3QhN21z3Q5cWYcdW1c48rW0iWKI3udpd1ZObFU5c4+FlZVVOMvYJTzfinlXBvCdceUG9lWWD62EQnuO4N5ALnJ63DtLxIHiJIJvZBrlDysZT+n7rzBtjrdmYsEmuS+fg8Ke13hZSxtpqh87AxOLUDVlyQs/BznXUTtnZPTebk1jNjbl4I9utz4tBaVD9Gj7VsiaIXtW6p62zPPXOgdQTy0Y9GFTxEGy8hgxZaJpwmlFEV9Z2zInn3WANvN/OLHVRBHxKebvVYi+kI80LrJtZZ7hDg9VoeZ2mz8YauZk06ya0cWyWezxYzcPDGW46MvFxbrA22W25t0/YvHHrXEkPYrzocHWFnMg95xzonaepguHS29k8t8U6q4t5p5ZR0N2oC25XzC3i5UA8K4Uq4bt8Z8G0y2m6qLgr7XSpbwEsUJE7u7Blv932Oh7RVHaz+9UpY/eHWEClkNaXK+VcsiWvwLuDM1Z+Wp+Oq1s3tlcV4ZvGRcqZ0kuM7dMqsqTg1dqDtTC8AlTGubs82A4860LiEliIT9dFsQAhpFxBx95KiUTzji44+M6cbYrS4mR/wd74uUzrRAqXa1uKekW+2ovTXm7mlY6QRKJmK3GVbekI4wlSYI5679NgaDJof7x2ftIvB5/MSURZJQSHHmrpsCVQCd84LLk/t0trsdqeq20/zoRWZjjkRhDNfM+zXY4SEWx6Pb7ybGXdnJohwPnVEPhta42LmXvdwsaSr6ch5xze2DR0g3k0iu5GtQWPXSIDwS4oSmFHdjVTL/ABZk8wHSfxRj0vZ1FyjIxknCMzWDhRq7bQbgF2SmilRrFocRZ3bHTEF3lb05iV0c2StRQHvUXkCaUGXLz5DHz2r+kW63cmmHE7dj+AXTMsDvv1johOxSkJ9QsSXU/nBXWDJWvvMWtuF+aNMLBLonSJTArqiiTA0FD1q3Mumt5sIZ0rrq1F2Kfmni7NLoHZMC59pjmtiE4yKiwIHYX5ZHVldzh9xQlRPMUdIaCnxWnLWC3LKN4q1fudFLX9nJ0jLeWewGgeM2Z/WJzhMF2j6BFd6/CNSWZcWvrNOkzxLm/zgB5pcdf2Kd6Q0oaxvNuSHyjOz2aolJ3hi8l7Up0hIeEP2Aa2OJ/269TOQ78TWY9fLdU6Ou3hhQkPJbEa4pJiVFW6HYV4ez63VrO60d6RYQ8xbvZCFjXLsaRIxY1DRO18P9tf9/7GJzrUTgEn/7gXPSvoxeDcEuttD7YetUodGmnypnoTk0hbD/C2KGE5OnhFz8xSPqGl60V18RUj7B3a4oVAnJf+OMs8jWdtt7kys7BtrsSmvF2BI+F6MLgZrmlsZWoKh5d2P7LxbFnVLNt0oaTwm6Bb0tcrIZw6GrVq8eZhHU5oMFM0FnEQghbn3JqyrkcustczZm0OnBIsLw3V0QtY8DohdQ9aLiP+FvXpudWHhjVThJ0yl1QeVcLF/gb7MhGXCFnT51Sx8jG0W39w3MHdCHs95ECCgPDvhz2hUatFOfTh7rQywNh22yrWKl+VPtjpXqq2x0hXrVoNb6sO7P+0wam546JaKojWeeweZPOqZ7zV4JooYWqjcN6uek6yeJGxsEi6BYKayPGsUkjV4WyElKXtNpTjRhlPrKzmbK1a0TGgI3V7jagZmTe9NoMLs+iXh6Hq9zjrhKQogRmjJKzZjcc7peM3G7aQb2DTwSXq7HhQKUVa1ptoGA6sLMoVPCJjgVtbeoXN1eswEEI7V4TY8a+OIBrKtuU5kQ4NZA1fJIE6j/JV0YjLcFj5LK2t1r6i1AH4YpP+/kYJOMeclViRdxz38ullOnN+nhz/u++Bp8O8/2dnio/jv7f3R/dD48Dxv9xlffm3Nfrl00vtJUCfx6lpk3XR85Dx785MP/+Llw7T4vHxYnV6yTW0b6frrRNNfxL0khR+17T1+K0ps+5+aPvpxe2a6Q8Umm/Pw+mXu0l5NZ10/50Jj7PvJCq+teW3OmiTOniZ/opgen0T+InTvl1Gz5NkQD8C/yRe8w2nyG+gBE7GPt9lABuxV+QVffntfwDdez6reiUAAA== -->
