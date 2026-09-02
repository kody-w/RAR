---
name: "rar-cat-agent-skills-cowork-use-case-one-pager"
description: "Turn a Cowork conversation, into a one-page HTML use case write-up \u2014 narrative, impact figures, workflow steps, and outputs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/cowork_use_case_one_pager", "rar_sha256": "04d7936c14c1ba540141659716a7bacc34a2cd3fcb057a4625d749fd89492bb7", "source_kind": "rar-agent", "source_commit": "409a3c18c6511b9cbf68a9f6716c5be9715b10c4", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "cowork_use_case_one_pager_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/cowork-use-case-one-pager:73538ada056689315fd6b0810905f5be382d7755b7b70f3f02f8cbd53f7305c4", "kind": "skill"}, "version": "2.0.1", "author": "Tim Sparks", "tags": ["productivity", "use_case", "html", "documents", "writing", "audit"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/cowork_use_case_one_pager`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `cowork_use_case_one_pager_agent.py` is
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

Cowork Use Case One-Pager — Turn a Cowork conversation, into a one-page HTML use case write-up — narrative, impact figures, workflow steps, and outputs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#cowork-use-case-one-pager
  Upstream author: Tim Sparks
  Upstream version: 1.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `cowork_use_case_one_pager_agent.py` and embedded as the fenced Python below (sha256 04d7936c14c1ba54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `cowork_use_case_one_pager_agent.py` first:

```bash
python3 cowork_use_case_one_pager_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 cowork_use_case_one_pager_agent.py   # or on stdin
python3 cowork_use_case_one_pager_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cowork Use Case One-Pager — Turn a Cowork conversation, into a one-page HTML use case write-up — narrative, impact figures, workflow steps, and outputs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#cowork-use-case-one-pager
  Upstream author: Tim Sparks
  Upstream version: 1.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/cowork_use_case_one_pager',
    "version": '2.0.1',
    "display_name": 'Cowork Use Case One-Pager',
    "description": 'Turn a Cowork conversation, into a one-page HTML use case write-up — narrative, impact figures, workflow steps, and outputs.',
    "author": 'Tim Sparks',
    "tags": ['productivity', 'use_case', 'html', 'documents', 'writing', 'audit'],
    "category": 'productivity',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'cowork-use-case-one-pager',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#cowork-use-case-one-pager',
        "upstream_version": '1.0.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'e6c8d90451f0dc94',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.556, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'tag:writing', 'word:write'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class CoworkUseCaseOnePager(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CoworkUseCaseOnePager'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(CoworkUseCaseOnePager().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V5aZObWJb2X2GyP9g1SicgFqHs6IhXG0JiEatAlCvS7IvYV6Ga+u9zkZRpe6aqpydiIl45rERwz37Oc869/P5ktU2YV0+vT2qUQkphVef66fnJ9WqnioomyrPxUVtlkAWt8j6vzpCTZ51X1db48BmKsiYHz/LM+1JYgQcxKs9Bbe1BjgW++ipqvC9tAX1tpwiKQ5lVVYCw8wBhWlhOA/lR0FZe/QyNvP0k76G68Qrw28pcKG+bom3qF6CRd7HSIvHqp9dff3t+AsTJ0+vvT05i1eDW0101rfZWQOoh80SgSgWoEisLwONiAEZm4HfhVX5epeCW6/nQ49fn2kv8Z+jf//3cW1VQ//L6NYMen69P4z+5zaAm9KAmt4ByLjCtsOwoiZrhBVokvTXUUOU1wEk18ETdVFEWvNwpv3PKC+gf47PPdyEvgdd8/vqUAxVujvz69AuUV0Be1Y7XLyOX4vMvL8AhXvX5l+986taOPeA3wAxo/fL2+P1gCxZ+Xxr5N6n/AFzv8bS9r08/GDd+7nqPdgLKp5c4j7LPd8ZFlXdeZmWO9/mXv2LrhJ5zTqK6+Zf4/npnHHqWC2x6KP7L883Jv0GTh0EfPP9abAHC+r+xBCx/F/cMPRz1V7xv/v8vrJMo8+oPj/8puz8jmPwD+vUvbftnBM+Q//Vp7SWgTirLTrxX6Pc3Rdysfv3kfr/56bc/AOv/kY2St5Vz4/CWWlnke3Xz9vbrp/p2+9Nvv35qC5BrnpW+tVXyZzz/zK83OT958LHq88+0QL6WnbO8z6CPTId+z4t/q/54gY5WErnf79ev0I/1Mn4m0GjEu9C7C36omRro+oMff3n6AwBDBqxpndtjUOV/+xvER06V17nfQIoD8AQCAW6i1BuVV8OohtRHUX9T2B3HvaTuNwjcHcsdQITVJg20rawogUA9jBEfLch96Nv/c6zmC0CZrPlSn6MkqWHnhkFvAPveRux7A5D4NkJi9e0FUkMgMK+iIMqsBJIXogjdaEdRt6So2/RLN0oDmkR3tJFXuxFp6jbx/g59+0vubzdGL8Uw6v01A4GwQHRcqPHSIq+sKkoGyBqByR4AFAMYBeBR5UliW84ZGr/a4mV0hh562cNFjpVB3sVz2saDktwBGvtRMmI0AOo86QAQjo67mQ25UQW8klfDDbCBc19HZt++fbOtOvya3ZEXg+7tpIbBgg+FoS9fisrzkygIm6+Z54Q59On3Pz5B/wH9M6ob81GGCKD/5iiQvQm0Vw4CBEqxTcGyGhrzAODMLVS//3GPwKhd5lUQKKDIj7wbMeD2Pe6jBfewvMcE2DyqCNrdXdLPfoP6EPgFihrgLVDU9fPX7Na1wNKqj0D7ezjxTnx3/XuQ73LGmNQPH4I4+VWe3tbeUm4MppNX7gu086EPTwFzQVybMaJhXjcgSwsvc73MGQCl1XwPYZY30Nila394Hjvy12zk/M0GrEfnpACNrOYbxK9E0NjyBHyNDrqJB9R5Fo2Bf2Tp/TZgUn0CObZ8Z/ECCR7wJgTGBqsIq7Hjj+t8654RoKG909+GhMzrx7afeGOMbiV8y7zHXAG6NzS2bwj07y+3Bv4+Nfx/nz9GLRfbrbzZLtTNGtoIqny6pxRQphktvI9RYCKAwERxr4/vU8I7oLxD7dcsiUAYquHv95X+LYvua+7wBVRyAUzIN/5jPVc3vlEDcmEMblWN+Wt9zd4xHeg75nU9whMo2fMIAPmHwPHpu6YhqMvx9/f+Dt3TbLQYJDBUtHYSOZDvee4t15uwGivp3YPA02NVgdR3wp+sggB3EHTAH0QDqAr+9PcAC6AiwEx0T++P5dE4NQEt3NYB2oKS8V4gfcxgkIU1ZHtjLMAa4IVPN1ZQ6gEfAxU/PFyHVnFXZsyLh4LWIxY/+v/xCOTi2DqAtI9CAzwt12qAJ3sQAlBHl3tcP7R8RAqomo5JfyP6OdgPS6EfW8/fx2IDGn4HeStJxq79g2sAQldpfcsz0E/PNSjn1HukD8iDW4N+uffYexP/0OUVWi1UaHHjrdyaD/Q5fW9zt46o/RyTVyhsmqJ+heGPZS9B1ISt/RLl8H/rZH+7N5svoIy+jGX05b26qp94393wCn3fOfz0+JGOrxD6gryg4yMucrwx3x6fV6jNHljsQp9/uH6E6xYOz30GuDGCDEiWMTPr0HNvo4fsfY8nUCVPQWGPbh4Aqn50jvcloH0ElReMi++dpB4bUA963o33rRN8xPxRDwAfs2CEhjr/oU7HeI0RvAfoA2jBo2yEcHeczwJv3LIko7m19/SatUny/JRZqfdPtiojhoJsBE4bNzagLsCY00Te7ZfVutHoufH6563Z4XZhJWPp5GMndOuxHz08eNParYBKY60FoEd51TMENA2a8GZIP9bb2O5tYFgNGp7njpo3QzGqet/KjGPVx8z13zW4lSzAGjd/HSsXNEwwHz9DH6PuM/S++bht47IW7L5+Hcfs0WawFPz5WPux87S9p9/+RI3H1P3XSjzg5I7elj12wtHEP7EJcKu8sgWd1x31+W7gd7n5XdgfNz2b+77x96d3xBiv72PAPaEAwf88o43GvvfWt5GjNdLdyu5m+23gfLNA4Mce+sOjYBwI3u6J+fQKcMZ7fgLEoGLAFH29bYuf7moA/b+PqoADQIwv9TgTwKAOASfQqYtR9zMorx8EjLcj97Z+vHj9q/n2T0DhdYYRGAWcghAkSc0xlPBd0kYoFJkjhE/YHkZN3dmMIOyZPUN8zEemPuXYLoH5MwwhHByIr0EOpNZDPIyOTgeKf3j2fzFtP90pQW+YEiQgRXB3NsdIB8Ud1LYIHNQFShLzGUpaMxA/B8OtqeNivmMjxMzCySnhzvC571JzfD617dnI7zH23dV5ex+x3+NwR4I3J0/TaFQWR+YW5qCUQxIoas8d2ycpa+6TQKQDvAFEEzaK3M2+kz5iMYbqbvGYnmDiA/NWN8r5/RHbMeVIHKxk8Hq3uH9W8PxoznQ8lmV7jiFzeQoP/VojsmVAW+K+Pk6dnt/xDG8td3p12idDgyYtEs1aMivjVKDPRrDLikWGuxcbNefTZRMc9ZCmIxc9ul6nw2qMYYe8X+8OnL/37C28FY7efoWDuVzdT6mz3iSXFQXDytCyBb9n/eF84OdtYm8HlDlPaTWvHPya6PQyCPw4Itu2kxeazDuZuT1OyzNZBLx5RpZl09JHs1ldUuNUGkZypKfsOe7ZGsX6wip7xjP3CtsN5a60ZWlDEHMY7myamLgGR5AcTU5arMOzTeLYslFqbNTSFV8IcYZNT4VmazqJXFySNg6llrW0HTnJ8aS1MbE2d3N3v6sxON2XBFK2eZHSa3rvy/uL0F2b4eKRQZ/uuC0Z84qxlyQ7J7Qj38Ssyk40ztpWO0ZcbFecgF/aOjwz5UyPEDTj49nJmtCDBR/NjD9FOh9lBxXZntciO9HL04xWyuTMerxNLqR9ZPPOddUNiRs2LnctMs1d1E2q2lyw0FvO53Jxb7QabsxOOksIHfA8Xh6Zk0gmEcklsnw2oimOgMQ/DyxhseJuQRxEcrc8pU2QTtV8va0xJ15ZGitLbLG34Ul79TJCr2mkrqVpteCK9XYznC2Nd6slkZTBjKDc7WFCWSUX0biJqpMaJC8llMTQnzAV5/S1uGHSK9+d52p7km0da3dakTaEtWRdw4wviu2zIdVQDNgtHOOled47VO1uz2aKHzhKIYYrQZ2trJSNuDoRgt0Jx4PDUDZceOkuEXTZnLpZZV13ld42F21A4qyYbWoVjbkN1Q5qM+EOFn04r5AsAf9dmTWrNMwCwB9JmouuhdfTrI3FTk7xNEP2TMmerTlSrSIE5uf8ca80XmmEkcFkPJzuMmullE6gZYmQa4vYirU8lfyl3ijkZt2d9VJrp9ipS4wmPpEsixQwkHAcuvhYqcRC9xHNppl2W2Zb5XTQY2e24ydYHdaqnXQUgrfnHN5ZFF44W0snLL3f8gVr75GF6PTWNciXIBaRpvvhKWIOFwZd7Hui6TabRajy8jY5a9dWyfgNhbvewcRWJR/H+MzZxddLz030/QKmuzUTdMiFOrfzRs/QcKp2kyyNbJNhYWunw0rkCEGr1eTCmHcUPaXzgp6mtXoRqvkxKNDLKUaHA8M0weaggok3oRtOLCnWdgpYg4dWKJSNsDCQcLmTl/Mk8cJBEJ3oZJDotZ56QnvhXI+HjwUnmTRdylpJ9/stL8LNJcfIWliQmCacm1I1QeXW+ZI56QsyLjw/MC8OU2gJ6N+TBQ+7KnbZ19toEC+d5JeytZOTiYHxS3yFLqUt0wbGRoZX12u82FiEN11aw0kovJNKN3S6Zc4XcWNm/Ro5spnaWgOSJit9rwW80+3C65IRCRnbeVMKmUqnLJmYyhmzedWFcz3JhcW1Qjxmsz/jDMWYZys9KmmXMgGLVEVlm31pH9PmOFuLyqHqiq7J4C6eYrLilVlmqamipGGpH+3GDQmTZyOmFvnkyqKG5yM9XmxKDY66wfPFLstx0qv2SEaRmuvhG95NjtIxUJyEbVSdiTqskKTdLhNpZYrWnsxmSFUN8/SQXPdkyVwX82oiDLqcrPw9Is/tZUlEO6271iVsZQNywnKkAGBAXduFkIfr/rC8mE6UHDXdnvWUXCpcJyyKXEwHmeYyvJK2FSpctpJw6stzxhKEM1NNQkmaXYSujNT0N3YpsIjJNoXJSTJeJsIqFgh6CZtRZRDMZaYV7fbCa3Z2ZYVOjpJsvdsI0ny52a6JeOtcaJ9ByxPPhHuLYB0dJpdMJpHr9pToGp52C60sFkUyS4+mRfEL65iuNOI8czgzn8KbmaZEuHEQdpUyZQtkeXQCzDoJsJkiziRlirOELC46D4fIAQ3qS27RkuStVwU/JIVUuXVJLUuD29boUS42sjPIvu9n9ITwz90i2POblbbCc1wSqYm8WZzmeOw3NdclzLmGWypVYQfM8eIUdda5ac/r9SRyF/BlIfS8YHDHzVa263gSmOECt9nEQUpCV3qxl9j1/rTMSiFw/Cy9SNoRJjbIQnAHg4zleJMLqLorD/mAu2dZ7o/omo019XRsB7gO2E01RPJyl3sGK1gVEwJPzk48CNHxoFD9rlif+dIs0IjtG07mJrXss85xfpyuVElmuJbPkGsrH3tTIuiDgwR7S5/vlobGFJRCEutUWR7FVs5Du6+TurBSHjFSD9Q1DC+S47HQlAW5N12+uJYJzU/pxYTgiyI+qBdzKtKlYKql5F+PLmkM5VLKdZzY5uvwGNKzHqnSpZ0a5Fqz1y2yFDX9YJ7QvSTLHNeZvGlabKKc1naaCaLszioYywWVd9Mji52PorWvpLlH2OsNp4sCs9sVfK/lAKtJRZYqZBvu3UwIkgD352E5kQ6O5LFEeNpcfeGKnwb0YtG4G8t4jw3xadXJSGs5yTJlNnNeLQVZBnip7lNfx1dXLKeW/savOR/Tt6bSMasErg4SGfLBdouIBioc2aFoNmpkCPKQSa3C8F6yYfh6uyIrYmauU4OdF1y51vx4l0xkHZ0Ji3wm7Yn8etq5F9aVrDPYVUpNjltaUOf1DKuWYEDZVNWJNgEFtWZXrWovIoX1pLaMk9OFupysvBFrzxMN1w8RMJ2lxxUV05udaA7eeWFag08msYQI+sGb+g6uRhRbsx5Wixq1UjJUXQ3ZDkPWagTqc3NIy6ByLmxzdqs4KUR8gbRlxenIiiMUVLWL+IgFR1gpZWYTqU27jyNlaWoyhulKJudav1vvOREMDwzaywKeXE8JppH7i8XYVJwg1Zk7n8MJ3J5pZLJWjKNZwP4iTVH8RO6YlnamA0Kqpn8Ry51h0fOjcmasy7lXp6S0vFbK+aTaebQonRKxWpJlinyPrznJxZjDYSp32SqY2/sW33lqUSt4nsfNttwR5YqVhQvCWOglMyu90r04H0Ch1T47xabdRNBdPRIu05DyXBpz7W5FitfAr9oBNfADndlMeMhP2PKkDKI+82JaRPPjKTERb4tQvOmsDkFjKI0iUecZ4rmZT9UIe+VysvXiXS2gS1jNNVvf72GZcbcaFSzhtN/1tGpQNRYdj24NH+PVgRWk1YQUS3FRIfIgTRhxu7IviGoHlL3ory52zAhkZ9ahl8WKK3H+xXNhY+Ut97Mz3HFXFQ7oBDlzeGC3JApHDSEC9qmHCLMa2a1ParNT1dlF9oaCxudrUZZqiSyvgREtEUZqYKnlpbDnFX/VqVGwWKthPcPlbRoP9CAl2nm9cuSJzZ9UrOLmfNlkyyk+ZSNllsi4sAyoGcucwpKxM6qpsGR7qM1Ac4bD+bqqKJmwOG+wPLQXpSyGteO6I8xr7LgXQ48u8ZLoJzuHnk0RWt9NKX0mD1NhdzqsnMhqCcqrZ1ezl7bGeqJfcq4opm50spgLasWdbeiWMTHECX5ClCHnWotXwLZGl8SswyU1B5s2mJ+Z0T4nja6JuO2u4VbNYc3bBlZ3134ikK195Lr1ENTEBeOvE8/tW2a6ss8LjurLqRca4iWwQy/UOAdH1HrPVdg84tJeETlsLjVbSXJSRxzmG/48y5OJVyXk0Lkkt0SkK4uZ052zqlF5kWKxdVCXh77zymvIioznSIfdRGtoAw/riKExY2r4xnk4Ob4MuokYLi3ualxxnZyxfnjgr310XZ6CPqpdkSgCRFsxE3Wp6eK8lRqDNqlQg8VrRa2HdKyrgQvBrvcws64bYz7bYs78sudV55rxk5nkJs7+Qva7kI87EaDmHB6uErwWvNgmOBKzGwVMthKOz7vlcjMnefVkbrdd3gtz0ZdO3HFC05MZyXC9m8aOb8nhlQ1PQoLPrM6WTURvppOhRItp2/ZdqJlhXBpiDybVGbqwe0sMmbMgHWjbC+jtDGWszcCv2OUkZjAW4DHYGiFZv8WTwWLzDjNq3WzCNsS6zQJhZ90Jo3tpos9dqr2aRYI5neySZGVcpnsJuGsgtutCEwUJy8GWB1emJ94oYeCTpA0m5L5NzfrsTjMkptuoa+A1DG8S46po80vR4jMDkXIqB9NjvCp3S5VMlhZJuvChnecojUbLQDAMETODI2XgJbzeIOvekoK5YVxg3xFX0Y48bCRyOjFOV48m2kKYkRQaTRR2b8/TnLIamuC1cD0Je4t3mF6c20q4SiYnHHdwd3247o/ovLUMwUabAszmAmpi9qZBT6se3V3blrqCPZB46j1mrxm0oPpB4zmeuZiuliyuZCtkujzYuKmZhl+qnpoGW/eglOqaGWpbcFJRqQrNNYf56trh66iimGS2cc8rH3anm3YBeoUDok3MhVpKE5KMJ6CLXd15I5m2X5u6zy/J1Qmz1I2dIxula6nJvlvmaolduaPid841sE7IgDBZcEDOlEBYA5Vv9IjcreiguPoqtXRcLfW40HCsDpUcZjbpU01Gt7EfXdHLSj3t/YWztihJqXf9YvH0/HR79fX0Okex6fPTeLL6OB/9lw7RgmtUvD04YFOUfH76vzvvuZ+9vL8cuR1Wepb7epP++i9o99vzU+VEQJP7eVsN0vNxtvNfD7G+/OWR2kg33F/Sja9tLs37IXJjBbezvvtBZxN1UTP6410fcBk26e0sMXfur0LB9fgWbDz0fL4dJN+OCB+H80Cx6Xg6//THfwI4HORrCiQAAA== -->
