---
name: "rar-cat-agent-skills-redlining-content"
description: "Redlines a document based on changes from a template with Track Changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/redlining_content", "rar_sha256": "1196f5449b1e765cd968e70f0a5568c40598968414f4ffb10380e02b9bdfed98", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "redlining_content_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/redlining-content:d2653579cf2bbc6980d49a7f75f294b04c75e3255b1a1174ad469f5c650183d4", "kind": "skill"}, "version": "2.0.0", "author": "AndrewHessMSFT", "tags": ["documents", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/redlining_content`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `redlining_content_agent.py` is
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

Redlining Content — Redlines a document based on changes from a template with Track Changes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#redlining-content
  Upstream author: AndrewHessMSFT
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `redlining_content_agent.py` and embedded as the fenced Python below (sha256 1196f5449b1e765c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `redlining_content_agent.py` first:

```bash
python3 redlining_content_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 redlining_content_agent.py   # or on stdin
python3 redlining_content_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Redlining Content — Redlines a document based on changes from a template with Track Changes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#redlining-content
  Upstream author: AndrewHessMSFT
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/redlining_content',
    "version": '2.0.0',
    "display_name": 'Redlining Content',
    "description": 'Redlines a document based on changes from a template with Track Changes.',
    "author": 'AndrewHessMSFT',
    "tags": ['documents', 'productivity'],
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
        "upstream_slug": 'redlining-content',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#redlining-content',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '1c2ec4d219101bd1',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class RedliningContent(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RedliningContent'
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
    print(RedliningContent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/61Z+ZPaWJL+V7Q1P9g9KhfolmpiIlYIhBDoBnG0O2zd94FOUG//7/sEVNmePnY2YnBEWUjv5fFl5pepx69PVtuERfX0+sTmbuX1glfXksFvn56fXK92qqhsoiIHj3XPTaPcqyELcgunzby8gWyr9lyoyCEntPIAPPOrIgMLGi8rU6vxoD5qQmhbWU4CcfclL0Cwd7HAc69+ev35l+enCFw/vf765KRWXb8rivKAK/IGaAEbUrAVPCmvwNQcfC+9yi+qDNxyPR96fPtYe6n/DP3970lvVUH90+vnHHp8Pj+N//Q2h5rQg5rCqhtgt2OVlh2lUXN9gdi0t641VHlNW+Wjj3VTARNe7ju/SSpK6J/js493JS+B13z8/FQAE6wRp89PP0FFBfRV7Xj9MkopP/70kha9V3386ZucurVjz2lGYcDqly+P7w+xYOG3pZF/0/pPIPUeEdv7/PSdc+PnbvfoJ9j59BIXUf7xLrisis7LrdzxPv70Z2Kd0HOSNKqbf0vuz3fBoWe5wKeH4T8930D+BYIfDr3L/HO1IEXy/48nYPmbumfoAdSfyb7h/y+i7+n7hvgfivujDfA/oZ//1Le/2vAM+Z+f5l4adSA77NR7hX79YqgL7ucP7rebH375DYj+P8UYRVs5NwlfMiuPfK9uvnz5+UN9u/3hl58/tCXINc/KvrRV+kcy/wjXm54fEHys+vjjXqB/lyd50efQe6ZDvxblf1W/vUCmlUbut/v1K/R9vYwfGBqdeFN6h+C7mqmBrd/h+NPTb4ATcuBN69wegyr/298gKXKqoi78BjKcom0gEOAmyrzR+G0Y1dD2UdRfjfVqs3nJ3K8QuDuWO6AIq00baFlZUQqBehgjPnpQ+NDX/3as5pMVAJr5VCdRmtaT6o1+vjh3/vn6Am1DoKiooiDKrRTSWVWFbntGFbdkqNvsUzdqARZEd5bRudXIMHWbev+Avv5O6pebgJfyOtr5OQfAWyAa7o06i8qqovQKWSMR2dfG+wQYE5BFVaSpPXLp+KctX0bn96GXPyBxrBzyLp7TAuJNCwdY6keAZZ9BVOsi7QDxjUDd3ITcqAIoFBVQkrsjmK+jsK9fvwJKDz/nd6bFoHsDAKC0+bvB0KdPZeX5aRSEzefcc8IC+vDrbx+g/4H+atdN+KhDBSx/AwhkawqJhiJDoPRu/aSGxrgDXrmF5tff7siP1uVeBYGCifzIu20G0r7FefTgHo63WACfRxO96qHpR9ygPgS4QFED0AJFXD9/zkcRBVha9VHtvYF433yH/i24dz1jTOoHhiBOt643rr2l2BhMp6jcF2jlQ+9IAXdBXJsxomFRNyArSy93vdy5gp1W8y2EedFANSiM2r8+Q20NXB0lf7WB6BGcDLCP1XyFJE4FjaxIwZ8RoJt6sLvIozHwj+y83wZCqg8gx2ZvIl4g2QNoQqVVWWVYgSZ+W+db94wADextPxBuQbnXQ2OT9sYY3Ur2lnnvfRp6NGroc4tOERz6T00KoxJ2udQXS3a7mEMLeasf7xnxqCHoPruABg6BAeCe3t+a+lv9vzHj5zyNAIrV9R/3lf4tCe5r7mzTgioF1a3f5I/lWN3kRg0I5RibqhrTz/qcv1HwM/AAAFmPbAIqLhnrt3hXOD59szQEZTV+/9aOoXuWjNkL8g8qWzuNHMj3PPeWqk1YjYXwgBTE1RuLAmSuE/7gFQSkg5gB+SO6EUgwQNM36GSQ0GN0bki/L4/GIQdY4bYOsBZkvPcC7ccEBElUQ7YHJpVxDUDhw00UlHkAY2DiO8J1aJV3Y4oqeTPQesTie/wfj0AqjUwPtL3XCZBpuVYDkOxBCEAZXO5xfbfyESlgajbm7G3Tj8F+eAp93yn+MdYKsPAbN1tpOjbZ76ABGVdl9Y0zQJImNajGzHukD8iDWz99ubfEe899t+UV4tgtxN5kG7deAX3M3rrSrYHtfozJKxQ2TVm/Tibvy14CkOat/RIVk981nr+994hPj6z5Qebd/VfoxzH9hyWPVHyFkJfpy3R8tIkcb8y1x+cVavMHjbrQx++uH6G6hcJzn0HJj/wAEmXMyjr03J/uFf8tlsCcIgNkMEJ8BYT4TvpvSwDzB5UXjIvvTaAee0cP2tVN9o3E3+P9qIUHOTyDOHxXo2Osxujdg/POkeBRPrKvO45SgTe+WKSju7X39Jq3afr8lFuZ98cvFCPzgSQEeI1vHqAcwDDSRN7tm9W60QjaeP3jK5Byu7DSsWKKsX+59dhFHuDdDHYrYM1YYgHoLF71DAEjA8Bsow/9WGZjk7aBTzVoU547Gt1cy9HK+wvHOPy8T0a/t+BWqYBi3OJ1LFjQ5sAU+wy9D6TP0Nsrwu09K2/BO9LP4zA8+gyWgv/e176/4dne0y9/YMZjNv5zIx4s8nxvwPbYv0YX/8AnIK3yzi3ol+5ozzcHv+kt7sp+u9nZ3N/ufn16I4rx+t6877kENvz5RDU6+dYJv4ySrHH9rcpuPt/GwS8WCPjY8b57FIzt+8s9F59eAa14z09gMygSMOMOt/fVp7t6YPe3QXI0xqo+1WMHn4DSA5JAXy1HmxNQUd8pGG9H7m39ePH6F9PnGwe8uihJYATFOD5q2w7J0FMXZyzKpwgfZXB7ijsU4WEoQdiIhSAUbrk4yfiEQxJThMZcHKitQcwz66F2gowgA4Pfkfw3ZuCn+w5A/ShBgi0IwpA+geOMjXgUSTguQ9IeNfWnFkGQtINPCYYGt3AE93Hft5EpRk+9KWoztut7LkOP8h5D2d2ML28D8Bvu92IH+rMsGo10QFskMWTqWz7poJZFYYiPUS5BO75HewyKWBg5ndIj+I+tD+zH0Nw9HdMQzGNgGupGPb8+YjmmFomDlQJer9j7h5sw5sneT2w93MBDCl8uGKkhUjkV5OthR5MCLF4PfBVlmnel8JZdk0XpGGazFTfyZh8eJXYy1SfHAyP6vkSpoukAnjts6Sk3W9vKUFPKRJWGuZwsV/ZsRuwTpVFP+3TI9lZ23XUDjU8nnGqae0MUEsfep8S0KU1jc91Kmp1Z6KWJNwQfrFMUNOONeDiSh1VcFahk0/t0gWccrmwatIc7DCGcDsPTQwVTk27eGfylS1cxs7dXZ5nKdcIkaydS17F9jNLCdMjS8HDbMfrUDA1STeQkRqZJNPjwYmEOpdloweJcRfWcHWhHXc6QXXe0kajZROrF1HL+kkXkruLMzMTL/ZQIJ6fp1Wxlw9Ip/5h7J5n2dSvDcr0p5IlJHicLIpWK1pS4StkaYpIGOn6IkK1wbM1dnRlUyrQFx4cmeiLKxIAXVSvHscfAfVjIeWdsTcoUfco+Hean9jJg2nR+7PBpb2fFbkjg81I4tSm/1GHhGBvo8jyszqnRSe7Vm5Mr5Jg0wRneHjfL+nCMOdQV7Yw6yUrOYJMdoZp01bK4vj314mmu7K47Yy818YxAsohKp84SbmhrOY/4gsA0LxEQhlZbBO1xYUutsvmGEEt62PDqjkoXe76ZsDyRWXQuK5xCNfv11iZMgYPXnnk97Wkx0czJJT7SoXTgCSfqu70v7KspY6xp0xbEyifO5YWdlBNmLQ2LMuo3II8Y2zIiWZu5G0Nxc9q6qstFtb0OldJhEiKkAx4LhumlrQrE7vebHZU0KeW6B5skqUVIoBK22KvH1jt6O19Jj4v1hMnFcyFJ+TldHM0LgXrree+yoqno622f72dzmloc06RnRex4VN1Wt/f76koieM3Qm6UeeqlqITyfrxk5K+U+aOEcR9eqxZ3zpYUry5CjWKGrMXqNYf41UcT54iDNNIMbNhzMX0xxj7fhQmOmVqCVulNs+KKm2Mtu7US4x9rhYHms2odzSV+myW5o0NxZ0LjrtSeMO9dxinuztSJenA1IIQPzuMm2av2EmJREESFrJCf089AXQYEGTkgNRkf4J5vfU9iMy7pmdXbdTWufjp2emyWT6+bq4iyMGBFMsZJVL3JWpUWgJ/WaF5zfIbFoZBOeNPfukl2tBxVGLRqQnGDoTcZfW6q4Cnkc7FYzO82kaZKrPeHsclN19rWjSOfFYbK70jZZxuKGwgozSJax03a9KzmCuV2uEJuR2oBljpswRFhCNJtCqwsSFO0UXdkicXXYuXDZmPom357d6/ScC6t+QZriUkgjydDjLlCONAaz3kAyMhjMGxAS3+ILa+4sUCU06t1Wq5WFu1gTikEs6bNsTpHGoffyGduXShbMZ6g5yWBl4g2Hs0cmKJ/kFzMoylOZoVu3mW3rqF7Hh5WaLsvqaMdzUoLFGG+P1SSf9xOY7k41JadOezTV5liUG2KRHR2vtg/CMsPL3bHUSEez7f2FWJx9ow3soTbFbDuZCul23zk24BrZdHNTAKGussUqmyjoGT77YjErz1PRm17rod0NJXfYaT5vXtemqZ+6bk4F6tQ7rQ/Gms1T0yxy5WIknsM7MG+6l0N5CBFZ4rcog2bDNV2RGt8sD5l8WOJnnsTcpVeeFrlpGYmcRRI/beDTMjry2InaVRGP0GDCMBSpq2JbWXIF4m/bEp33S03jeImhcqPEqiWBrleqgV4X03KSkKrCSZyrw1UR6n4xcCkXbPOtSaTXfRNPOfOU9A3XosJ+xc30NcUf2VVY8JlSTcM9F+CGLZd6Mq0rQ7isRYNdu6GPU4d1j2lnLpR3QhDwajZNN7k9y/VACXCXOZ/X/CpKLoZrUzDdqpbDz9iZ0ktqaBfxSRoGPuBinbYywbEQbKlWV6am0dOk3sYZx6HelrZxplhqXMoOuLYwaYQQD43IUEWqa3LGyQPH1bsEFy64Yi3tY4hYcuD4B5gxdghxWkzX60napWwsilhlsppYVSmqz8NQLJn14G13adZP6ELbVdcI0bmlfFjLvj2PwnYmtzzXAy6BdUbgkmN0LJpq3esbarOPDptu3aIGox36PTC0Pi/2tGFKR51JokVcbqbpgtGYINxUSbZL1uSpjouZjYpIvp6icqyQ811hCtHuLKYEK2H+kvPC7Xa90dT2sEFXZU4PbgB63PKkrY7G3Od0k7VkLkcqsqBkJbOP++F42VwjXBfik23Ma0w6bbPtTpkdppWO9sbiSKbHUhV9s7MClA0m1NAUKHyM6WgHC4xinQaN1i+HWcSTApIn63J13V2M0l5MseCQyqZ5NpDrZRUe22V1Ok5WMyPJC2cdSuv4kjJVBIYEKounynoPswg8kzkKa6Qdqy8ucsVTc0lw5UR0TzHlsGSSDyFHr+i+yCcL24dBEwT4XJRShLemUZ9tZIEDKA7KgIqSY3ImaCbhIqapTbM7246+9ltci2Ai3PPTZKpoQmf1M+eib69NkeJzuCp3Bm/sDlrf6WyZNrmzzXZi10dXYpX73XkTXVk/Q1mBj6pioxTIQTqs9ntyfqLULrKX8cqNJHhBtnuWbS69SxbNWcSdHXG2pdnJHLryEC9Kx08PoT1jTDbKeT0y642qXk/hNVuxG5dcKagUdafDGSWsCGNnyGV/2qOhbp8P5CaWA2VgD826Yd1hcTi5xw3DVmfxgKPHCY0oGsMnl8zbrlhMWmzgk7bzXS3laeWywDxnXwisuE0jF4cl+pzk5+2EimenValhqthpK4YpW8mDCUF1ikPGrUwumdW0KQWod2UF15rGK8pdaM3g7/1TQPVHmsPtXQRf0RlMm8sgZJTsQIUKt5KsQ5wWS51X1XHqO3sz99QdrGUsr4XoHG+xaZb2zHp7WJcdlvb+dps7pxYuugG8BXjKfHsE/GxTrcyVKbexVzAvw93utA+K6zalcV/X2JqfLwzMXcirKuzheKiziYllNUrOqyTtZxkpgvSwyDCyiVim1C2bM/DGKRlT1nms3FeUeIaZxuovyzkKZuNynqppp8XLEFZ1aaFGWqIGxXQetkJLCZd6ZTYzf34VvTrESGWYe7qIe103bIdJtBlCMCuzgrOZwCufQOmmFy66ekAvyHLOdKILr+cNWqrzfeB4aaZNkFk+29Gz4tSYMOdq9DZwEnlKZeZpt75w09qUPMAIUqqrZ2G/wCMj8i4HMPaRp4Pd+vUKjAzFHknseHdUld6s2enBFujOxnJBWVPsSQzt1V7e4yY8HOZ939v9KVUq4jhFy4SC+R6TD0fAIuTEphdanNtHxg2wUOuEiTFFgqvFqTmeneBB7VqW9wrAY/7cRfhj6+dFkeuF5xe+iJhk58kx1SxFtiHXg7I8kdx6IglRDPMJOa9zDFts09MJRlY4fqWwJDjTuEQ0R/gaq3MCOxNKoXkCMiOGUqlz2nfp4qBwxyTgYRKz5X5T4ZpMNlrE+k60khcUcWWiPO8vqo0xXsDPdm6yFxk4lrR5siM786LOd6xZ6X2eLfZDXThzh1+bci7s2hiUsTfF8sjyWgcJ8JgypqYfeeuVe3B9wmW84UTDrs5vEv/MF51sqwGVhmJM7lbxNRpmXtwZtauKaTCtlws4ZCsbm6JF2yWScTwfuj7pjmF1hvftKusLqrZr3ZksNG+YCLmuD0nL01hgpjS86YMZd1qq87PUYxM1Y2BO9gKKUASsIvSUKbWLnvtzTaMR52CdFK4+arOJ6u/AeHflUxjF+BwXpWUdIQHlSBzu2LMWo9F2KLaqwSRIe3AVmFMaKnEajaB2akoqttBw9sWQ+qpvNHi1gNWGx2LVXmrsPD1O9HlVyZcC1a7cAQ93GsDjdKCGWkjQEuvZec+iLUKZyEAf+W5ypckadU+M4FfgtfCQLweBDTFadKoZYgnpCrvOXf1SUjS/3HaEXnP0xZFn/mApujevsECzAp+ZzCYTid3PfZMJqPnl0J2Perjt46xeT1dcLotHpCJ8uqT28Xl+rpcs4jrwROBqA+YF+pgFFmcYc8T3hWHoaWtVHLGViDFO28v4bk8mWFdh+w2R6svJ1lJOFWLpPO7QhaSEgk6zE5QuNdDqFHgjCRrVXPmta6PNdQ/e8u3ONhzPRy6b046lRUOiqk4q4XybLfN5AivnrCH7aFIqNOD2mYVrWERO58YRxx3d9DPTjZVy6XKnYqjE3vEtt8WMgjh7Jw4RqMlKjCtpfaD2nSB3HIZN1chbXSektmQIhJLPF3mTIgJNS1d5Ak9nSDq5IK53nPd13KSN3uxTzbrg11U9Werc2afTnQgjg3LpdvkSp+jZNeA1Kq9sJtDX8xLTAtPtimssxLp42KN7NQpoz5/TDl9lSboDLxsx7A7pNNric5rc8EycrgKWfXp+uv049PRKMxj2/DQeYD6OIf/ywCoYovLLYyeGoGDnf+6s5X7u8fa7w+1A0LPc15v217+w6pfnp8qJRgtuZ1p12gaP85R/PTD69Ltjq3H99f5z1Xjj0rydyTZWcDtHe/tlqH66GeeOR/hd1Ny0Ps6xgTJ0PMh++u1/AQIQW2qmIgAA -->
