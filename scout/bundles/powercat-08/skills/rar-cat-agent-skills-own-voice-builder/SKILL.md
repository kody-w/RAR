---
name: "rar-cat-agent-skills-own-voice-builder"
description: "Mines your sent emails to extract your real writing voice \u2014 languages, tone modes, structure, vocabulary, taboo phrases \u2014 and generates a personal voice skill that makes every email and Teams draft sound like you."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/own_voice_builder", "rar_sha256": "c94c678de5a3bd69cf2f1f4e4b50b38cdd931bfcd23aeec345fb3263b86df1b0", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "own_voice_builder_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/own-voice-builder:2e1b020d1d655b2f074175b7a25f451eaaa790126ad046f9f82f2b6c7d13f767", "kind": "skill"}, "version": "2.0.0", "author": "Marcel", "tags": ["writing", "voice", "email", "teams", "productivity", "microsoft_365"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/own_voice_builder`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `own_voice_builder_agent.py` is
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

Own Voice Builder — Mines your sent emails to extract your real writing voice — languages, tone modes, structure, vocabulary, taboo phrases — and generates a personal voice skill that makes every email and Teams draft sound like you.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#own-voice-builder
  Upstream author: Marcel
  Upstream version: 1.0.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `own_voice_builder_agent.py` and embedded as the fenced Python below (sha256 c94c678de5a3bd69…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `own_voice_builder_agent.py` first:

```bash
python3 own_voice_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 own_voice_builder_agent.py   # or on stdin
python3 own_voice_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Own Voice Builder — Mines your sent emails to extract your real writing voice — languages, tone modes, structure, vocabulary, taboo phrases — and generates a personal voice skill that makes every email and Teams draft sound like you.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#own-voice-builder
  Upstream author: Marcel
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/own_voice_builder',
    "version": '2.0.0',
    "display_name": 'Own Voice Builder',
    "description": 'Mines your sent emails to extract your real writing voice — languages, tone modes, structure, vocabulary, taboo phrases — and generates a personal voice skill that makes every email and Teams draft sound like you.',
    "author": 'Marcel',
    "tags": ['writing', 'voice', 'email', 'teams', 'productivity', 'microsoft_365'],
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
        "upstream_slug": 'own-voice-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#own-voice-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '45c780ef5e1ffdad',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.714, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:email', 'tag:writing', 'word:draft'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class OwnVoiceBuilder(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'OwnVoiceBuilder'
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
    print(OwnVoiceBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/91ZWZPaWJb+K5rsB7uadArtKDs6YgRCILQAAiSgXGFrudo3tIua+u9zBWTa7lqmJ2KeBkc4tZx79vOdc69+fTLrys+Kp9cnxSxsED89PzmgtIsgr4IsHR4HKSiRPqsLpARphYDEDOISqTIEdFVh2tX9XQHMGGmLoApSD2mywAbI5xofYyQSm6lXmx4on+GiFCBJ5gzXZVXUdlUX4BmS26ZVx2bRQxLTyjIk9wuzhGIfLMzUQTyQgsKs4EMTyUFRZikUeBdURkEcI5VvVkhiRpACNKDo75re1u6BmZSIU5huhZRZDZ/EQQQGxV+gvaAzkzwG5dPrz788PwXw+un11yc7Nkv46GndpvogZVoHsQMKSD8YBF/kPXRcCu+hNm5WJPCRA1zkcfexBLH7jPz971FrFl750+vnFHn8Pj8N/7Q6hSoD6BOzrICD2GZuWkEcVP0LwsWt2ZfQp9A/6WAwdBb068t95TdOWY78c3j38S7kxQPVx89PWT44Ckbv89NPSFZAeUU9XL8MXPKPP73EWQuKjz9941PWVghgJCEzqPXLl8f9gy0k/EYauDep/4Rc73ligc9P3xk3/O56D3bClU8vYRakH++M8yJrQGqmNvj405+xtX1gR3FQVv8W35/vjH1gwuB8fCj+0/PNyb8go4dB7zz/XGwOw/q/sQSSv4l7Rh6O+jPeN///C+v4VldvHv9Ddn+0YPRP5Oc/te2vFjwj7ucnHsQBrA3TisEr8uuX3WY++/mD8+3hh19+g6z/RzY7WPH2jcOXxEwDF5TVly8/fyhvjz/88vOHOoe5BovuS13Ef8Tzj/x6k/ODBx9UH39cC+Uf0ijN2hR5z3Tk1yz/j+K3F0Q348D59rx8Rb6vl+E3QgYj3oTeXfBdzZRQ1+/8+NPTbxAS0jtYDa9hlf/tb4gS2EVWZhBOdnZWVwgMcBUkYFB+7wclsn8U9dedJMryS+J8ReDTodwhRJh1XCGLYgAnWA9DxAcLMhf5+p+2WX2CUJlWn26YVqLQyi83kPti3fHn6wuy96GgrAi8YIBAjdtskNuaQcQtGco6+dQMUqAGwR1ltJk4IExZx+AfyNffcf1yY/CS94Oen1PoeBNGw0EqkORZYRZB3CPmAERWX4FPEDAhWBRZHFumHSHDf3X+Mhhv+CB9uMQ2U9ghgF1XAIkhwMeIG8QD8BegzOIGAt/gqDt0O0EBvZBBzB7QGjrzdWD29etXyyz9z+kdaQnk3pZKFBK8K4x8+pQXwI0Dz68+p8D2M+TDr799QP4L+atVN+aDjA0E+ZuDbv1rtVurCCy9OoFkJTLEHeLKLTS//nb3/KAdbEQILJjADcBtMeT2Lc6DBfdwvMUC2jyoCHvWXdKPfkNaH/oFCWBn7WARl8+f04FFBkmLNijBmxPvi++ufwvuXc4Qk/LhQxgnt8iSG+0txYZg2lnhvCCii7x7CpoL41oNEfWzsoJZmYPUAand39voewjTDHZMWBilC3tzXUJTB85fLch6cE4C0cesviLKbAMbWRYPY0HxaGxwdZYGQ+Af2Xl/DJkUH2COTd9YvCDq0K+R3CzMe9+/0bnmPSNgA3tbD5mbSApaZOjRYIjRrWRvmQfbNHLr08ijUb/NDv/P55fBdm6x0OYLbj/nkbm61073RLWztBoMvg94cK5A4Fxyr7pvs8YbLL0B9uc0DmBwi/4fd0r3lpt3mneLHQg62o3/gBLFjW9QwQwbUqYohqowP6dvneEZGgztKQeQg0AQDbCSvQsc3r5p6sNqH+6/TQnIPXkHJ8CyQPLaigMbcQFwbhVU+cVQnw8vp0N0YK3CgrL9H6xCIHfoUMgfgUoEMO8hAt5cp8I6GyJ+K5p38mCYvaAWTm1DbWEhghfEGMIDc7tELAAHqIEGeuHDjRWSAOhjqOK7h0vfzO/KZEX0ngaPWHzv/8ert+xwvpUv5Gk6ZgU92cIQwOrs7nF91/IRKahqMpTSbdGPwX5YinzfwP4xlDDU8FvLMON46P3fuQbifgETzrwlWhqVECQS8EgfgNzb/Mu9U99HgXddXpEZt0e4G+/drYUhH5O3Znnrq4cfY/KK+FWVl68o+k724gWVX1svQYb+rh/+DWr36VY1nx6t6weed/Nfkfte5odXjxR8RbCX8ct4eCVDLkOOPX6vSJ0+UN1BPn53/QjRLQTAeYYINMAVTJAhG0sfOLehRQPfYgjVyBKITYNre4jP7z3ojQQ2Iq8A3kB870nl0Mpa2D1vvG895T3OjxqASJveUKjMvqvNIUZD1O5BeYds+CodmoEzTHYeGLY58WBuCZ5e0zqOn59SMwF/uL0ZcBjmHnTXsA2CVQDRqgrA7c6snWDw2XD94zZxfbsw46FQsgFNnXLoaQ/f3fR1CqjMUFke7HOgeEagjl7l30xoh+oaRgYLmlTCpgmcQeeqzwcl79ufYRR7n9N+r8GtQCGyONnrUKew6ULkfkbex+Nn5G3Dctv0pTXcsf08jOaDzZAU/nmnfd8FW+Dplz9Q4zGp/7kSD/B4vo8D1tBNBxP/wCbIrQCXGnZvZ9Dnm4Hf5GZ3Yb/d9Kzue81fn97wYbi+jxL3VBoW/Ol8Nxj51pe/DJzMgf5WXDebb8PpFxMGfOi/373yhmHiyz0Vn14hmoDnJ7gY1gicuK+3zfPTXTzU+9tYCzlAXPhUDvMECisPcoJdPh90jmBBfSdgeBw4N/rh4vUPZ+EfS/8VB5g1xscO5tAUZeHumCExhrIYE6dcksKAaZoMO8Zw2nTGJO2y7gR3cYu2GQcjXIZmoNgSxjwxH2JRbHAyVPjdk//GRP50XwERH6douMRmSZtmJg6gTMJyaNZ2cRdzSUBa1NgiJrbjsARmubaDEyYANkFSrkXgNGFNaMeF9gz8HiPiXY0vb+P4m9/vtf7FzpIkGJS0YTekCWzsmi5t49BmAnMJxqEmtgsmgMUxk6DH48nA+bH04fshNHdLhzSE0yGczZpBzq+PWA6pRZOQckmWInf/zVAWOxMnxup8Y0RhqpJsq1VwPhf5ON73S0MLjXXKaYVVyvYqyHAvVAJfFRLpvLBEbHuRp664BbY42Vns9dx4RXFej/u5flnwlrA+bhJ0hTa8orS8wFQ2KmCZocSbS4XByTV0G6ZboQv9mh90nxbx9nKZzJMsdYyzoG99zOiis44zqrRKVo0D6UI38It0y0TXJMHyOl5hoUYz8yIKM1w3k/DSmBc+zk5MUit4tBZXyyLz+RiLAlnBE/Q6XXcHK+rLUrSkQx5bq2UoLcG8cc7n1eVSFYq2PmbqjNj5V5uXeyIqYwc7RdrF1Mu5oapUMtIDrRe47fFIXDuqiY4C5W42nbs5YvRodLQjuXCkbq6DyJT6ojgJAn8RK54jt1ip9ZhUOwermUjlzNaxmXButfMyrzJF2WtUeNnzh6gw6RVYbjq/imVc3bYGhglkWUqhSGj5YtZGTLyOTSI5TE3aEIhIDJrAHPWL/tyEpmxodt9UcUof88LXarvzhcsmaAMt8ji+oQkjOVHzS2x2scvh53Ym+PTIiqJA1Ec0vq5alZ3yIR+tuUoUZ/VEnYz8SQyEitssI0otQS1mZqyt+VF+mgSUfjgLpF/1wSW+SuzpIqHnOYce0us8LIVFb00lzGd009jn8uzIN0uANoR1YJoEn4op50UKFa404dTjyiYB5qpONdaira4QZ/JMTJ31Yl8cadJ1rnHU1ul4Vy524tEJTu6ZjW0PJ5zmtI33cLNWxlqss1a5w/A+AnKWctfyJKv+MpRDeuzN0GVJxitbWQNCUARjv7RpNTtU4yRbjNKJ2ljcFqezCwPkSSMZkloUJlZXojACXaFQpz7crKdpM1pGW4ZEW9JgqjlTqOMkQOd6JwZnd6wvcVKe7H1a4IlZH6JTr5RXKJaIaw+o+9AoN6MxG2HoaTK7nAOq20WKNG1Lqtb3ouyF4GJ3zVomzH6c7Dce5rm+iKtyUDFEPiupxTnERFPU6f4Y2hm/jbfUNZxWY7kwpsRlop1Tv47l8SRDJ9uc6sOM4ydMxwn2dHesl5kmbpypR0oHt55hZrFqVF3aTHWCMyIbTwM546KjGO56eYWfr/gC2GvGsJl4b6ywCai389GCFzaxTy3H14mQsDHeHHzciqkU961zI7Vm7AEdrI0Dn8hgZ6EValBjxxZkqZFEp54Uo/2CrAm9W5RYcipX6TjbuJzI6sstt7HCXl9H1oonWCtWcxYA1OW7M7hYbcZmByril/wRkKzGXnamnulGLIjZIduGEToijNC9BNjhaMYTv9xZVUQX0KER3y1i0yVI0z4c1nCndTyWWXgd5+vRCsPHfjjRiKa8NHNvnOoOXOkv8zzcmmC/KPEZeUzTGQwcyZYdRkbHDXO04zF98vbXktxSmzlmyA3HHSZrY5ePZ3tpEqRtbU/zKVjZ1jV0qksts7mZ6o1QXdlZpe4otXOjfj07N9ySdRdzeof1p7BXsaOwyZvFOagtTGsCR9h2e0xG1QkYsaPqxNLFjMQo/SRJSl9MY5zQBLbdTy9xxFPb+oxb5NVPhHnBM/R6w0QFyR5GhUCnkrmypiFQMUGUta1wOYgMzsZ7XJrtLisyu9aSoBYnOriq+XGHTrKDuT7Q1VzpA3MtXI9+fBGuXpIast7OTwkK+myduLIWLsJdXIQysaY05qACrY6MI70ysGMyYd12i5I6qedbejvGUIM1VnK5pY7hjFtPnYakpbot4qXq0yvGcgQtcsR45tkkn3Q1HQqO4peFoQmY0VZ7fcOnCnPAJ2nOXtqOtxZydaUEI62641GeHSCumGa4IDhnyvGkvEpsjrxWdtFxYrMr5QOZbujpId1epvUJ0w0yaA7ZuJ16Be7tmtRebLSOqrWSwLFTJVIbfZYbEoUVlWzkuh5Jac9vqADLoAfGrOiI4mXF8fQeDX1ghbtp5un2tl4G+SxJ8o4AJ2u7F9KpXh3Pp3OrY30fumgth+PLNNE4txcLT8VXo1mgYabot4KdbuyWdC9ccWaBMEl9a4muw7ikklNPMJqQCdxMnXHloc1tp+HMtu6P2yl+Co9KpV77IgYyh2qCPMdFk15yRlHRI3fTb0hlvijwS3E5SNnKLnFMEbO5XOg4VHZajk+JaqupwSwnO44NUmG1CHTRrA8LC1+KIIDZcRXO00MtX9NNnemnTh/rlcw0vt5Sq/xYmYxqXyRyxidtGYXeyS8gMEbByZxHG9PUhBlhzy+lRJvadRXs1nMZOokM9tcjJrNyenD3KxKCpxLPz6ddEIjBuLnwUUdtFDXdaQshhW2f5xSpiDnF4xppxMpnZ+aPZT5h6tlkRQbsOVjIUdXJ2aqFabSYLa6XdodXu62CXdpA1NZCVgh5ptSSwtqcLfkrZzTJLl006TItiDK3U+g0JOTTKUi0TqIOl72yVA85QXHJXJpUGl73CY0RfZPyWN005LYLrqSySdfLsLvUmF9JkzVV2B5LZjiXcQ6Be/L27HczXqC98dzGsxnRt/RCVNzNuefr+cSwFpohLCTDqhTZBU1xkbbTNKOTlEwk1TWOO6Hb1vNVSXGStekTT8qMY8tOW328sWRwlPZn9CJ4Z99xRrsdix84MunVnPcNNNDtmbfhk1qIhUPFrPZUe8A3s3K8snFWOlfs3jEO0yAeryhF86YmtrxQ4XQW4Jrq2aORcNivC8w7Ev4BN3b8tvKnDp31F2lTGlTRKYqs75tis95ffFcoQmvNOrPY6qNDfjJWZGz4vnKNdoesW5r4ZdcfaEyvdkuPoxhd3619DYj8InYrZT2aNYFUze3Z6nC1j0vFmIEscQ+TeG1tj5xXRtX+qoignfKbQOdFQl91yfI8uVbr4rT0Ik8a1TSR7Le5ZFbcqGr1nVk2V0HGZ8eidBSZkR0fVaW2n7RqKY5nVIIXflJLhJLk1jmbqhfrQu5PR8sf2/pGrta1gsa4Ry3lNSmAa9UsSLhpphZxR5k+ofF9mYKubA6MweDSPtrP9qQk4E7oZE6JlRgqmTzlLCdYjrpFa8oBs1y3Nk8s/NDC8Uk4qc/byOi5jgdFvCaycxKd1rDMcUWqOTquluK1l7iMiDB6hbJAs1a5T1OW7WPlDi3zxTmXEn8r11FiHkbXkGAs7zrW90yesH3dOBZeblft/jJrEp4MuxM+Z9uGR/3pfhKuwnZZeadTzdTEhCFlXCuiMRaNZ8v2mNpqm3oHALdKkzGJkrNRvxsbYe2ipI821o7gG4Fjw2KzO23wcUW02fFIR3x17nLaSHj0sLZjvl34C+xIzjSVX4oUx5CEYgaZbqvFQTmx3MY7youjsVZWnUApbL/2q3JMp1a99/tSF7JFEVv84dRMUb3oR0eTHh1ipk2X7Nme230Z7afFSN6h8+V2o16whX+sSGLMFxS4eiO1xa293mMxCkRbpXCiAyI12VvTnlD1cWbM43G1x1J3CTgp3uLHgFlQwRruLNglTat+78jM2kSPzKgE+dxOdnJiJCXXnaI9fkJ52g4NIqWXVZJVYs+q2eqE6xOldSzbMPGmOYOjT1qYM8fkhp94OUmHqQRHiibmunZ/yDjUZsojqa8mosTsDqLHmHAvkVVVd8XF80bmWWe/ht1uvlrUZsr0aqdR/H7CGnMZ268IYTED2s4axVPvLBa7lc8QgnhK3OmmkDeL7bqE+TPW5N1kc5zy3uRCuy6WTYDr+r4wP9aeWWBGqCyYbHRkhYs04bZXo5UneZiPFGURRNurbJtBi27wuZkXm4WkkqNL04oXy08L1KrXSUsxZVFqGlFazpWYl53WRXWM4p61nqghOtsGmgC29N4v0LXRjeYmv8B6lfUI+qBYlzDcJ91iOmXyU0Liinq0vIK0RxmJ5SPpykjl7sidGuPEEh4PlrOxdc7hjIMviEvI6Hx0DffOxgm3QdwvQGGPjiJdT7MlkHNSnNAnDoJdpnQxHA2jseZp201kucL14lZRl5Qj7jivjyddGNHyda0UznjlkN7SX54JZlsIIXNSm/G8whOCxdkpwcAVqhhr7iaUI2ldnSYxP4oLuEtqztlk1KALLNVxOcjq8rrMrvbKme+X2XrheijajUfT8Tl0JSZQWXaVbkiJU7FuP+cwcjdWz2BCRJtWAqFUhEG1nKlHZ6OXMhG7Id/yW27P5Tuic10XHWWiscK39O56PDCOIFARIJKWCHpDJhkIR9iiyc7CQWNCb0ovnNTjRvKInwqCwXDRlb3Oxhymqg1OcGdHbUZsLHdXrFrBbcvCWxjTSmATtJw4245xjj4exYQ1J+gVgaeRJ8vc0pZ537KmKU8rmXJp4lU1vW7DdbrWVlMYkcqv92m9H4uLjLrYJaPMSdOtKGezNIWGmFgBkHp3Zi/ZsT5STEqV43Haj5S+Inpieo7RK2aCE5/VYRNj+8qIQ93vdEpDFW96OE4qZcViTN2Ferokmck08MSWPqbW2NMkPjezrbQmCNkvWHF3xhu9onJ0o7frgo6Sg65yBVBSJj8k3hHl9IsmyZy74jju6fnp9uns6ZXFSeb5aThPfZyK/uUBmncN8i+PlQROYM9P/3dnP/dzmLfPH7cDSmA6rzfpr3+h1S/PT4UdQA3uZ2xlXHuP851/PcD69LtjtIG+v3/MGz7EdNXbEXFlerdzvcdnMUh3Wzecng6fpoazzOHD1NNNZWf4vtAE1eCh96P8LwRNDbo9Dt+hSvhw+v70238Da/1Q2HgkAAA= -->
