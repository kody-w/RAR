---
name: "rar-cat-agent-skills-campaign-deck-builder"
description: "Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/campaign_deck_builder", "rar_sha256": "9eaee36124c834b7c71a49853abb992be0a0ca4f7db6ab125621475019ee15de", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Adi Leibowitz", "tags": ["marketing", "presentations", "powerpoint", "automation", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/campaign_deck_builder`. The original RAPP
agent is preserved byte-for-byte in `campaign_deck_builder_agent.py` and in the RCI capsule.

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

Campaign Deck Builder — Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#campaign-deck-builder
  Upstream author: Adi Leibowitz
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `campaign_deck_builder_agent.py` and embedded as the fenced Python below (sha256 9eaee36124c834b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `campaign_deck_builder_agent.py` first:

```bash
python3 campaign_deck_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 campaign_deck_builder_agent.py   # or on stdin
python3 campaign_deck_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Campaign Deck Builder — Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#campaign-deck-builder
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/campaign_deck_builder',
    "version": '2.0.0',
    "display_name": 'Campaign Deck Builder',
    "description": 'Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template.',
    "author": 'Adi Leibowitz',
    "tags": ['marketing', 'presentations', 'powerpoint', 'automation', 'scripts'],
    "category": 'devtools',
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
        "upstream_slug": 'campaign-deck-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#campaign-deck-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '23b22be138aae9b6',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint', 'tag:presentations', 'word:deck'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class CampaignDeckBuilder(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CampaignDeckBuilder'
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
    print(CampaignDeckBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8Va+ZObSJb+V9iaH+weyiUuCakmJmIRSEgCCcQlRLvD5kgOcYpLAm//75tIqrI90z2zG7ERKzu6OV6+/N71vczE357spg7z8un1ifEiRASRk1+iun96fvJA5ZZRUUd5Bt9qTZkhNlJB2RqJshqUbQQuw1UOH7uhXaZRFjwjbeSUdlYj5KcqiTyApHYZgxq++uTaaWFHQYZ4wI0Rp0P8KEngCzjcaTIvAR4i5xdQyjlUitQgLRK7Bi8QCbjCoQmonl5//e35KYLXT6/fntzEruCjJ/ahl4Nq502UeKCEYxI7C+DLooPWZfC+AKWflyl85AEfedx9rEDiPyN//Wt8scug+uX1c4Y8fp+fhj9KkyF1CJA6t6saAnTtwnaiJKq7F4RJLnZXISWooWuqwTd1Cc15uY/8rikvkL8P7z7eJ3kJQP3x81MOIdiDbz8//YLkJZyvbIbrl0FL8fGXl2TwxcdfvuupGucE3HpQBlG/fHncP9RCwe+ikX+b9e9Q6z2KDvj89INxw++Oe7ATjnx6OUGvf7wrLsq8BZmdueDjL3+m1g2ht5Ooqv9Hen+9Kw6BDYPz8QH8l+ebk39D0IdB7zr/fFqYEtn/xhIo/jbdM/Jw1J/pvvn/H1TD/ATVu8f/UN0fDUD/jvz6p7b9qwHPiP/5iQNJ1MLscBLwinz7osoL9tcP3veHH377Har+t2rUvCndm4YvqZ1FPqjqL19+/VDdHn/47dcPTQFzDdjpl6ZM/kjnH/n1Ns9PHnxIffx5LJxfz+Isv2TIe6Yj3/LiP8rfXxDDhtTw/Xn1ivxYL8MPRQYj3ia9u+CHmqkg1h/8+MvT75AWMmhN495ewyr/y1+QbeSWeZX7NaK6eVMjMMB1lIIBvBZGFQL/DrVdAujXKoKOfcjB/B8iPCDOfeTrf7p2/ckOQFZ/qmJIWdXojcm+DEz2xblzztcXRIPa8jIKosxOEIWR5c/ZbdwwU1GCCnIm5BCnq8EnyD6fhgtIoMjXP9T35Tb0pei+InbmDXIDWIVdDyRUNQl4GQw5hCB7wHbtDAFX4DZQa5K7EAIkWFA9QwOrPGkhiQ1G30xAvKiEFuZld9MNHfM6KPv69atjV+Hn7M6aJHJvANUICrzDQT59grb4SRSE9ecMuGGOfPj2+wfkv5B/NeqmfJhDhqT9cDtEuFGlHQLLqEmhGIwIjCHkiJvbv/3+8ChUk4ESgUGK/AjcB8M0jIH35l51xXwixhPEAdCt0KVpAZvU0Fmi+gVZ+8g7Xjjp8Gog6zCvatiJCpB5IHM7qNWG5rx7MstrpIK5VvndM9JU4DbrV9jabhBTWM92/RXZsjJsDXkC/zPAvAnBwXkWQfe/B//+HCopP1TI/E3FC7IbEg8p7NIuwtJ+zOHb97jAlvA2/NZhM3D5nA2tDwyuulXB3T1QCHrGfYT00xBzxM1TWPJe9Tb3TcYeGph2a2Tl56x6ZLhdDqFwIePDSYMm8gbe/9sjpWC3bxLv5j+IdND0iIL3iMotB98aMDJ0YOTRgpHPDYHhFPL/tm4YkDE8ryx4RltwyGKnKce7x9wcwoCi95UP7OUITJt7dXzv72/s8EaSn7NkQFh2f7tL3vz8kLkTT1NCJAqj3PTDIEMfDHpvOTjkVFkO2Wt/zt7Y+BlacKMeGAZYsDChhzx6m3B4+4Y0hFU53H/vzLeYld5QvjDPkKJxEpgDPgCeY0Mv1WE51NEjBjAhwVBTlzByw5+sQqB2GHeoH4EgIlgZkLFvrtvl0EzoZL/M0+/i0bDegSi8xoVoQ1CCF+QAS2FIhwrWH1y0DDLQCx9uqpAUQB9DiO8erkK7uIPJy/gNoP2IxY/+f7z6nro3JAN4qNP27Bp68jLwpweu97i+o3xECkJNh2K7Dfo52A9LkR+bxt8+ZzeE75QNazgZ+u0ProHpVabVjTQHCqogjaTgkT4wD26t9eXeHe/t9x3LK8IyGsLc+erWRpCP6VuDuvUy/eeYvCJhXRfV62j0LvYSRHXYOC9RPvqnnvSXtzL5NJTJp0cT+Unv3QWvyE8L/Z8kHtn4iuAv2As2vBIjFwzp9vi9Ik32TgEff7h+ROsWDeA9Q7oauA3mypCYVQi825pBAd/DCdHkKeSxwcvdUNZvbeNNBPaOoATBIHxvI9XQfS6w4d10Q4d/zt5D/igHyCdZMPS8Kv+hTG/9EwbwHp93eoevshrO7Q0Lq+C200gGcyvw9Jo1SfL8lNkp+NMdxkDcMBWhy4bdCCwKuDqpI3C7sxsvGvw2XP+8j5JuF3Yy1E0+NMGBpes3/90weyUENBRaEA1c/YxAnEEd3sy4DMU2dHoHmlVVsG96A+66Kwag9x3IsBp6Xyr9M4JbvUKi8fLXoWyfkWFZ+4y8r1Cfkbc9w23vlTVw0/TrsDoebIai8H/vsu/bRAc8/fYHMB6L5T8H8eCS55txtjM0ncHEP7AJaivBuYFdzhvwfDfw+7z5fbLfbzjr+3bv29MbXTyi9FjaQXFYl5+qoc+NYLrDCeH9PdHgu//hou8xCpIaXH/AYTNgA0BOcIJypyTl0C6N29RsOiZtx5nNCAdgNubalE97zsR2cDiIwCl6jOEzAPCxB6C+e5J+GVp4NCBxIaNPSBzzbX/iErZNk7hP0t546vpgCmYEbpMTDJti34fGsAof5t3NGXz3vv68pefdym9PzoSCkiuqWjP3HzuaGZZzGJ2u4QrtE/RqaeO1mmoTOl8fSptqqPbUxAFXjE0u20WBuzdSRSCSU5QqhOo156PKjNbl9NJONLlnx75ioOoyXigXmknopq/a7bTvemYbXJqxONGA1QjL6DxaFmNDWhDmQutHU4GlyvgSFzRLkYU3t85utzNKHxNc/wRYf2emvgMTS7E7qdez6/SYSJ4g8uY4ORsH7ryxZ9RmalD+dWFngmJffANPVDtXp6o9MoC14852ZMiw/u2DEDTctJqOQNv21UgWE3a06mbAdHzMjNyzt8gW2/Viez6Hi24yF0dutBKy8hgma8+dFAefMnKBEtJrkewuK+GYZFw19daqst/t4/W5jCpuq1BgNDkQeuPtzTo6T+u1v+TZSlvaB5XnWrfHFMhCXJO0ibiY9JhqX2f+kTvK+nW2PIvAk4gQn4nYFc17wbrq+XEJ3HShbUTm1LX4OZWuul1YLB7mq/WKCzJHrqp+4wu7ZkcWYOdrCsX2kjJvmf0Si0yU5PWekHIP3UokP5abA7/J7dCXNCG3XYkw9I1Ig84QjkK5i0pPnCZpFIzyvRU5BOtYUrC1e69zN5u4qMtljE9Q0qu1CiXZs82h13XGVPHWOglKsb82R39b6aYvnSgcI0/63t2POGniY5DE8QtBZ+L85MnB7Lgt44Sn5RbD1YbynMMqD5KK9mKr6BTTaK7dyBeUSzvNEjctToxGhfjIYRQrWre9Sq6kbDfz1nhUp9IYd1aC40xzayKPlNl0w9Lbc1etWw2jjmeiKTpjgp0ya8RXMMsFHYa/L2f5YrJeYOd1TBtiHY2dYoSzGevZvpBhUjkyxg5Kzzm6WzabYsYqk6DQW8++5FXby/tkb9mywl+uK61PvW7h18zGlBRB67JOYNY11xj9WgzKQz5juVXXqhc89S0mOtSnnGrVrD7GAp15fKknVAjLTJCjgA+N00mqVpwCZideDoplnVgkN9rg+mYOFGx8laltVXVYHVaWakhcqRxFsCwxQT+nLH4udpda2WTUiQpO+tahr8yI0oWFEtpL2GOLfi5LpJmns8u5jDFUGi15+oiZzWGVkJp8IRwis9HjtTK1mVwvDpZ0vp7r83ZZs8tDnwkA89G62DldIweRbuaKEaGmmzZXwBkFV/Tbq72/dNXmHJeSvJoxm7mFMyRaBJ0mT8bRLqnafXU0Vbx3iXkf97pmZdnZJmSUnqgGNz4UxjHWqRMb+8usJWh9NjZ5Sm0M0pofu6l9DvV1bvWL87bHZLlbydlkkuDOQrzOWM2POLDb6uSiHk268irsWOE6mjv8HovsSwzf1/5l7zfu/prPJ0VWX/aVQkpVXFSYk63mXZBG23K6tCe1dh2LUUQV+2Dptut5BxONUsg96FwM3etZgtpqRTo7HYywco/xe6cbb6JL5I7nslKFpX4VEhE9x5lp4ZzlEI5mS+2SP9d9fmpH6YSZoZJfS+xpVBccoxXGnhS9Ji+t9Wku1BPOUluLP9Nak64WOBBOM1/OzqSBUaORKJiTblTIWbPkVkdSH0XBCTuWhHfu2uQqJlxt6O1O5OFm6iqcyfI4m5ld2OW9vZyMSX0Kl8JQBM9Cjq8O5Wl9lab1zA911A55g09EkjfS2ImjMW/qh5ZfqvzBuGqtfLq0imLQ+XJhUqYRJ9KwHttyuxGuTqORdOYkFyRmoHtOK+p9wR5yleq5S+aFGR7OLaO0DgtZCDXszKziXpr1tWp2/ooouOOuOtaknOg2IJfJJK5XFjiGLCNcDhqDHy8jP9ZKfC+Fs71mkjpZLlCFzRs8MAo/oCvo1mAzBmM78kUKn6OEIfWtVoexeZpBhr3y52RLYcRO1M+kyySq6I0D0ktFlZwtFsliKYXWTJpRlUetg+DYz48LMekFM8mKjqVdXtjmFmZYy1jZqBtrNh352bjYgynLXBmZmrvVvJ6DkNLXynWi8iMQmHLJ0BbqFlgWjmVHHzlOVyVxyxPydEMxZLzTYfahTrG4pvXCozT9wmNz9RpZB8EF3EjlVXl7JBLJzQ8iTk9HAku0+IIPNXOasHl3FB0uya1a6ZpmZbGYuzztoxxf4zMHctKaS4VpftyroaZ0ETG5Uv1etVcTOjsK8VVyEz0keIO59Ji5FWHkUEjkXQ/qc4tZxkLpOZObWv2xobb5McrScM3yaavuFXw+8RdNure746UIO3khAk2qKCLdxc5EXmeoJLhSqojRWinVqXWZLJkttmPQseuv1WDF2pURHbecMDQjQd9NtGCur+cL4sSGhOO5kBi7a2QW876xUI3QmJ27nMmWdzwut+yeoBtuy7fLdSGPZ+V+1cccCjxYXf2KjdV4t+zjxMHEVYVPx+xuNVbZjRmOVSvvleQwWy+o0wG3F/ihmhlAOoyOdot55mJVgYMwF8heB6J50DcFqYy3K2xeLQ8XXioDFLuq7JoX6qPHnHXHOGpT3lGuHT21mLCNGW4TFLl4vnRzlvZniUP3Y0NTT4sriy29vZ3mfazBfeZaZ0Pxuh6z6goLlZRrW9bVjLoZ74sdxp6lccQvzdmqzw4c26xHzn5tm7m9Uo09P+KbJb4wx1e7X6DslG6Y5T7XvdDbEXuGmBSduGZQi9YtqWO5s2L0u2iZxJHDXEdTQ8EXmT332Z0psrnOhNIY2jCXCbfCinQhnMc9JvahlPtdeqkz0F9VYswSRiUyU6bXtB0dG9PjGLXZpo9t/Hyyc5xRZhfdOuDhujthZuoAr1v6WGKvx3utIKhU2lDLWtmP7ELw0vjMzK2dlcXCnhGXXTHR8qKjPWnB0H4FiuV+7sXVjvSmwTWjOhUtNdk9rmKiXbibedYaZMVMclkE4cgUpl0lnI29c5DSyGRVhjvXthXvpPMiHfeFKh9G+0bis9MhcwqzLy/OKV7pC3mMYZoLMGV7MvbubL5ahxNMKWu3mNS4NCtiRZhvpsuQbtAp3pI5YY9OO3TacAe7okc4iS/HPpc55Nym2WvVO+71Yki57lirkwXXXxmNCZFaXWUO1RZLc32KDmWpFEs3pTuYnSRaVklKKjN31mhr4mqOt2F5JjZtyoq5mSaQPQhaZRo7cBhxZx4cc+Sp+EmB5V5z03N/lhI/104XKjBHUnScrk5HnudyuqKlsLdiAbYaC1+06BLHZtVuvMyiCzqTZBllzAN7rNl5Q5U0KpLY5AwmHrVf1bMIWy28RACuJOBSwjhpboPlececRYm1KHGvqfSUVZgZF7gBurDTpaWLEk+e04UbZJSYnLhizW+paJq618w/EJMj6TRa2FXGIoE7nYt9mlOEUIdSRztmNG2B7lJltY3TZRUeNSc06Z1LcvKlnec6LRkc5xy0ljI5t/fC9piWsxGkBJd2VmXOTr2Qmk2ipDpoe21LL3BT3KINxRiTsGqWl22vG7FFgGjq8dcxCKeZYZ7r0UHWO0mde6Sh8QurYjf0Vk44ad7afb0k+4WaFADFF4etcuSXjns4Em1rATOkHNxbGWLLTYOcmpxKoT31bbK+XjRI1n6zI0SXjdFFAhx9HdL2VpHyvG56Ym3JojjTNEIN3MWa82WNG/PUBj0V6KFkebsI6Og0lzfFzleDyz42igU2pdl4q7VxgidZuM2AzEqeqO6ahcOEE4DDzMGtbdaPx0sd7FFdNIA9dVjSXGrTjZFKW3G7DLg5f8VGacop+7WTbJfKcZSOWdzFs2i5nY4Mg1rV0qWfzAJS1I5TjzAO65ImdtWYPqvH/NKZHTHe72qwUcZwDcBErVyLl5rsRYpkdujJHtMo5GVhsTOsvuiPHMPgk6rfOzx/Ki8JJvkX19qBHY9S0koMdPNUmcd9SHLhcddg2aFxOAtX6m7W2eOSOJyvraKOuUyvAjH2zFaft8vYZ1t2zFBGPaEwo9WS826x5/XTbEnyDMg4S7ZEObIULiZwxW/6fXmySZ+VwXqeeyS4xuI1J8gZjqWilbRk0KozFC1J5bDer0bjbgyB6rKwN7NugmMiMYGL/HbcWstxNJ1w5928U0jbV93rhEfJqTya2jjYSRq59HoeoPFuFa8YfkIVEXOcFoCvGtPp6NGOz9EzdTwpl94jnKlxYNAddBgz37KJ6C/hHnYqBOExG3OFuPOuKSX1s50DHA6IG7uN2+hwcm00jQ2wkiSGy2EGMxzVUvpCh8sTIcRzfS0VDUxkShSbekZWBZClSZ7U5d5mCt3CSGKPaleS00ICnJwN3N2L8lSpV1wUiCS7mJp8YPdyGM6XBpp7l60dWBer2Ge8GVWw0aYrYGICn1s40Gc872ptGrXrumVJmvCV1dJqC8ABOkX53TFNJhMNLr+tA037QdWNjl0tb+fY4YpeJjlaqorQUT1VjXiGPfvTQt+geN9cT3rGU/R0HgWb/cQsHSxQBK4A+V6QaEIMy9latYjaqMfFaLm5Spllban2vOEnx4xOsBTSHeOeyEKdqOsLwzw9Pw1neY8TuX/9xWw4Cvk/O5G5H568nbvfjsKA7b3e5nr9Nzh+e34q3QiiuB8wVUkTPA5m/vF46dMfHt8OY7r796bhS8C1fjuYrO1g+NcQT+9fSZ4eJzyPT0PVcD98FCmGjyLw5u209fZvIR4nrQO8x4kvREUMR75Pv/838rRLVxEiAAA= -->
