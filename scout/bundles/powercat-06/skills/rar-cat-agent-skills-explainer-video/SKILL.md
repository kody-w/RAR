---
name: "rar-cat-agent-skills-explainer-video"
description: "Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/explainer_video", "rar_sha256": "e67a73837e765ab5655949ff4d5fca1ed395181db51a69d1ea036fb3852bd6d6", "source_kind": "rar-agent", "source_commit": "657d2bb31e7d75b8fe4216443a5336cb035c07c9", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "explainer_video_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/explainer-video:e1293b619dfd5fccee2d7906766817a4b7710e86555e39a9337084221465cf17", "kind": "skill"}, "version": "2.0.0", "author": "Damien Bird", "tags": ["video", "education", "training", "communication"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/explainer_video`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `explainer_video_agent.py` is
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

Explainer Video — Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#explainer-video
  Upstream author: Damien Bird
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `explainer_video_agent.py` and embedded as the fenced Python below (sha256 e67a73837e765ab5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `explainer_video_agent.py` first:

```bash
python3 explainer_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 explainer_video_agent.py   # or on stdin
python3 explainer_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Explainer Video — Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#explainer-video
  Upstream author: Damien Bird
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/explainer_video',
    "version": '2.0.0',
    "display_name": 'Explainer Video',
    "description": 'Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots.',
    "author": 'Damien Bird',
    "tags": ['video', 'education', 'training', 'communication'],
    "category": 'creative',
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
        "upstream_slug": 'explainer-video',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#explainer-video',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '3922dbf6d24c64ac',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:communication'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ExplainerVideo(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ExplainerVideo'
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
    print(ExplainerVideo().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VZeZPaSJb/KtqaP+weyqX7oCY6YoWQAB0gIYGAdoetI3WA7gMkevu7bwqost3TPbMbsRGLI1xC+fLd7/deJr89OW0T5dXT69PUSWOQIZO48p+en3xQe1VcNHGewTWhAk4DkMypKvjXf0Y857YEfATHOKxAQFckTpyBCjnHPshr5BI3EVKBGjiVF0GyO7f6GQkBpBqYIO6nKk+SZ8TJ4HJbFEl8pwMgq6O8qV+gGqBz0iIB9dPrL78+P8Xw+en1tycvcWr46kl8k7odhELyxMlC+L7ooU0Z/F6AKsirFL7yQYA8vn2sQRI8I3//++niVGH90+vnDHl8Pj8N/9ZthjQRQJrcqQdFobGOGydx078gfHJx+hpa1rRVViMOUjdVnIUv953fOOUF8vOw9vEu5CUEzcfPT3kx2A4d9/npJySvoLyqHZ5fBi7Fx59ekvwCqo8/feNTt+4ReM3ADGr98uXx/cEWEn4jjYOb1J8h13v0XPD56Tvjhs9d78FOuPPp5ZjH2cc746LKzyBzMg98/Omv2MJIeqckrpv/Ed9f7owj4PjQpofiPz3fnPwrMnoY9M7zr8XCIGf/G0sg+Zu4Z+ThqL/iffP/H1gnMKXqd4//Kbs/2zD6GfnlL237VxuekeDz0xQk8Rlmh5uAV+S3L6YuCr988L+9/PDr75D1v2Vj5m3l3Th8SZ0sDkDdfPnyy4f69vrDr798aAuYa8BJv7RV8mc8/8yvNzk/ePBB9fHHvVD+Jjtl+SVD3jMd+S0v/qP6/QXZOknsf3tfvyLf18vwGSGDEW9C7y74rmZqqOt3fvzp6XeICBm0pvVuy7DK//Y3RIu9Kq/zoEFML28bBAa4iVMwKG9FcY1Yj6L+aioLVX1J/a8IfDuUO4QIp00aZFY5cYLAehgiPliQB8jX//Sc5pMDwav5VJ/iJKnRd8j7coO8ry+IFUExeRWHceYkyJrXdeS2YxBwS4W6TT+dBxlQfnzHmLWwGPClbhPwD+TrH3h+uW1/KfpBx88ZdPqw6CMNSIu8cqo46RFnACG3b8AniJUQKAZMdR3vhAz/tcXLYLgdQWC/u8NzMgjWwGshnCe5B/UMYoivzwNW58kZgt7gpJuJiB9X0AN51d8gGjrydWD29etX16mjz9kdZck3aEchwbvCyKdPRQWCJA6j5nMGvChHPvz2+wfkv5B/tevGfJChQ3y/uQdmaoLI5mqJwLJrU0hWI0PMIabcwvLb73e/D9rdug+o4iAGt82Q27cYDxbcg/EWCWjzoCKoHpJ+9BtyiaBfkLiB3oIFXD9/zgYWOSStLnEN3px433x3/Vto73KGmNQPH8I4BVWe3mhv6TUE08sr/wVZBMi7p6C5MK7NENEorxuYkQXIfJB5PdzpNN9CmOUNUsOiqIP+GWlraOrA+asLWQ/OSSHyOM1XRBN02MTyBP43OOgmHu7Os3gI/CM3768hk+oDzLHJG4sXZAmgN5HCqZwiqpwa3OgC554RsHm97YfMHSQDF2Roz2CI0a1cb5n33qGRW4tGPrcEhlPI/888MSjEz2ZrccZb4hQRl9Z6f88eL8+awZj7MAQbPQIHhXspfGv+bzjxhqCfsySGHq/6f9wpg1vC3GnuqNRWUIM1v77xv5sz8I0bGPYhjlU1pKrzOXuDaqj8kML1gDqwOk9DrefvAofVN00jWILD929tG7ln1GA+zFWkaN0k9pAAAP+W1k1UDUXzCADMATAUEMxyL/rBKgRyh/GF/BGoRAyTEcL5zXVLmPxw1Lln8jt5PAxDUAu/9aC2sDrAC2IPyQoTrkZcACeagQZ64cONFZIC6GOo4ruH68gp7srk1elNQecRi+/9/1j6FvH3moI8Hd9poCcvMASwZLp7XN+1fEQKqpoO+X3b9GOwH5Yi33eUfwx1BTX8huJOkgzN+DvXQDCu0vqWdLBNnmpYuSl4pA/Mg1vffbm3zntvftflFRF4C+FvvM1bT0E+pm/d69boNj/G5BWJmqaoX1H0newlhHXRui9xjv5Tg/rbexF9uhXRDxzvxr8i3039P6w/svAVwV+wF2xYUmMPDGn2+LwibfZAWx/5+N3zI0q3KAylnd1gBObIkJA1rN3bILEG38IIdclTiBmDd3uIm++94Y0ENoiwAuFAfO8V9dBiLrCr3XjfsP491I8ygAiYhUNjq/PvynMI0xC4e1zeoRQuZQNI+8O0FYLh5JEM5tbg6TVrIag8ZU4K/uzEMcAjzD7oreFgAusATitNDG7fnNaPB5cNzz+ep1a3BycZSiUfmpxfD63m4bqbun4FdRlqK4TtB1TPCFQxhBg4WHAZ6mvo5C60qIa9DPiDyk1fDDreTyTDdPQ+Ov2zBrcShdji569DpcJeCMfcZ+R9Yn1G3s4Qt2NY1sJD1C/DtDzYDEnhn3fa9+OiC55+/RM1HsPzXyvxgI87dDvu0OQGE//EJsitAmULm6o/6PPNwG9y87uw3296Nvfj329PbwgxPN87/D2T4Ia/GroGE9+a5ZeBjzNQ34rrZvFtWvziwHAPTfG7pXDo8F/uefj0CtEEPD/BzbBA4Ah8vR1mn+7Codbf5kzIAeLCp3po8igsO8gJtt5i0PgEq+k7AcPr2L/RDw+v/2I4vZf+K8CJMeky+NgPfDrwPAAInx1jDMswHM46lMuyOAY4hqZpQI6dMUmyGEcRBE4xtBfgLBRaw3inzkMoig8Ohuq+e/HfDshPd3qI9gTNDG5nWIclOZIFLEM7Lg1lj6lxEFCDgg4OfHJM4xzuuzTuMGMfBw5GMoFLcjTh+ozPDPweM9tdiS9v8/Gbz+9F/sXL0zQeVGRo1idcl8QB67O0ywWAInCGokiHJknGczGS9jDWGz+9b334fQjL3c4hAYthDKnOg5zfHnEckoqhIOWcqhf8/SOg4+2BISi363ajM8Z1ZHAJ001YERdCSEpGUVTFm8xC/0LuLYmvJtM5mNPimu25vlXEhXFaBAtxdJBHBXatcd+0mkWsCIuFWCVXuu7pbIRqUSrud0tiW/omrbVylTmRgOrXozVSTUU6FadNc+SmHC26Yq3g5EmJJD1Dr4lpJpt2lNrLJO2w8daezeztUhftw3RPtOW1jv0w30xEq7ZyfH0ogSAnx9Zk1e20Zoqdwqpm7k68uUTTI7QNKo5qyK1AznGmIdwAC2Jy68itFlbJ1hfwxiY0FdYEuY3W6m6btKap0KSpkX1lSP2uyVUMCi6Tg5Si48u6yuxyFi0MfC5tZ90VpdvFsiYBI0qNvwaqKuT9EvNyZWYbPU40iXIJW7ewO22xXMRoOGuZNtb3tD27piSWsgUgUsWmd6ouORdL6veRZOic2oHCym2Hsc1k350XE42SZ1dqPt3b3baqm2MFpmdjTc2uRCc1PC+REdkz835LbTEBDWIVdsqc2qdRKXG0xkRF5x62xuncZIpZhNANSoKl8nwpTdBL3olFOnXlWbh0WND78mJD5wfpNGZHweFscRw7UXlVns72/emw0fxqQmdlyNKcb69azonl44TTqMIY+QzqTt2V0cwajpsmp67tNbceXc2twsZ4TYE80U71Go9Lrqur5mSngWrxLLZt9qHtCsHM1llHuGq7pLOa7nK4BmQbYo2tOIwfbpok2mnjKeqMYqn1I3trZ9mB8Jqtu55MGrMyJ35WO93K9gqrZ68rPT1a9MGyCg81GAvbqYSZbk1qhPVuoaLtIqXaDDvoubB1R7m9lESwRelSXRmOvkvEq0Wmfj/1W4Ad/R0QqbVxkLLTYXRdzOPjqh5PYkGxEtOx2Hpbkox1tjerPpHb5WZdx7tKLpdxRcaSmqy0FWOAxp+Pzt223buRUYQxTimn9LywPWrHzWZAou2LreXVXMbzennm171YbtiJt6xTcrcort56ZHSlJIVeclpNQHSyd4U6x2YcZWTukdilnlrSS22qs+vWVheunDHT5jpvwOZguwWVEbk8OhOX/TEuEpOB7cDqVRRDG3ex7qjNuh/zSmk711OXqgVo1a3UrSQ+luTVuTBn+1iyT0pA9arKJFe222+zUBmXGzocc/uxbLFxtQ/oqeqcUlVoG0a/GLg5za4k65eTcTk1iZ1Sccli7TSjTSmtNPyYSA0zz2jFPeKu6TRHiWgjGcX584yChWiOuNGWSO1YtIONT4Xn7nAqj+KBnGLtKeaO2VxhVF3jzryA7UHDB5ZsbFerKSHpo4Vby3vGt7pds6Gs8hjKXNkrgbjuNXFJScx8JdqkQOkndsO0lluTa5XcCX7USQwwjZrPeO8gMkZSuokQoRsyK2sige19XZxNaZWPZTzRHXQVmNMdt6ISOtEBnclr4bQ16oZg4HFO3MtJfXGV5KrgwcbTDCrao0F6vtJUUqKbrHdXOoVxo6SSstFyIi70TddLRFQQFmEvVq28yndionC4drALUiwru1noY0thlSTI15edZfStc1odqrkmCLi73FlW7GPBcpVsRqdIkolIhqlb+8IpWPR9DKhTu+6Ppd7QVLCvOCPB7GKDW9sGt31GVDzKkEjO0rtlzJbK8dpxmjrNfYIwV6eFs57b2hl4hJRs6GlDNaIqGB3oTqG7TJbX3Hf2M7NnyILCi1giuDHI1kTeVMduNTPrYiry1l5PvXISjkZNsO53o7hWxUuil8v5XG8nbd5s7X2C8k1/Es7T7LCdZ/1h0zGKqvWHlCOukzN6gBy3YbsBumEx0Cd2S/FlgmOhYtsbX9UxwxQN25miGLubXYiw5CV9Mw8vpVEWys4hwSwRja7vznpC6lmc9lxLZpkY5zzvh0tl4tbHjUYcZ7k14ZV8mdZ7YF9HY+WgjhnAaKi7xbQogeWj83I43Ys8kQcOxzh8Y/gbwAtcN0tleRIlO4WzJ2ismIvaIJIVX9ouPg52WzXIssmxRJ0kjafSbnGO5ZO+xTdUrkTHLO+oi69utj01qhfaoTLj9dqMNZLhO9eK0Dbd1pK5z3Rpu/CixNREbJOa2Nk4z4q9VhPVKmmjNIxXO4fZTjVf2k2a6WlDYfLCxJa9IWxNz2eoopCnq5RcYEYzNjyOtdPktGPy6TTaOLIZxrRoXAuwmfpxsdjOFr6/2pXmCqeuUg6B8rQY82VdsJsoxeS5keOjuCMXSeTiRzGPrUyMurS+zFcYvjzZS8qB4HFOq8liIqzt+LSBgbSxCUfz20DoLZaOHUG20pBSzKYUjylAvUiIe1oSqzOVe/B1MhsvROq4w0t+a3ukne5UUOu7ErCxQOj6AjKiSl0qK4fHWIpKpwxPCtVegKNH4+ybiSglaX71jKtykqkpHFQ6iBBKgTE9imfOyNJOsyhP9Nxh5NgKsKMYeZuE5g3DG9lWWOTr3fy0EXIOG08Ik036Bc0w4Yipie25z6I6EVeTYsZKlwXe5ZK1scJluTVSJq5Sxcm9RKOzmszjEza/9DuHVS/HMs8EfHKSt/ya72aYVOLxJFaw9bKqR0A4p/GxWAdbrxTnewUz9r7i92Guym65ngjZ0mSdNXrZiwva9/Dr2VkVanjymViMbBsja3ZOTz1xOSn9ysMdvyzx8rgXA22S7KyNyRemI8QEnh0iP5DAaWkvcA9UaRgu7Y2CXi799FBucFyVjx5X9bzABzmFL82lWO6srp/oLnrEJ1WuClnYXuvTyeMI0yD3Mivx47Sj96U0x4SzqvEC0+jOpOXWm3KrKJ1Jp0TEp4IzteLCPeQTvdyXbNLo2uR4Cawq1OkmVw7dueXnBYNNPQXX86Nl1If1kYqo2bFyLrvcL8ejRj4tD3ItHXegGWHLlUPAo7hvyd78hItoAM/BVUzNVpw3FdPj0SVwzmJa+1Im3YUNfbdZWXs7Pe5lX6Ipb1NPulJOt2lPzXAwHmHHMz1mypnl+1frIKq75Dw9cpmRaP0pXS6Tq5FI+pkhkgAXl3PbJ5yWu2a0K1/DeCOBbt7tMswoRtFKn4omSjEmGgkOh1+WR/98wPSdd7QXMrrKT3OvHYVedNZqbnnE4Xli1AlcaCaF2ZN+gHYCejavpHUWqbHtzFtPJeqCDEl4ANigq0NUUHY/ZTfwVGvopDkV5qigT4T5guhYZbxylND2ltlOW9AT/bKTZ4GpaYduTtf0dTVpzhjREt6cPe4VFY62CjbLKTDlql2yb0mcK1QS6l+alEJLazmdB1SjcsaY4rJqc0iArhq7Rcbp3Qi0F2Jv4aOrxPeK11xJbAIWBbei1yahyzmcaOLRWdJAy/J4H9WtFOvH/e50IIJ4fJhHtHPkyC0ox+hOx5ilKR8w0lKkgycorDY/TUdS7U6bOXnVrOTgRDhF7WOCVwgqv9aojY9RNcaUeFVlswndBRg+n20MkvSUNRqlMjzTLNUmyz2VO8womDoCKWpHP5J9Y17b8UhYs87IhV1eOzb8RUcxI97VQiYzZzkzI7N1VmJ9sfCxOefbpZlM3a5RvMtyNXOtFMjd2KBVuZvbTc4EIn65sBqDsocR11qHuo8Vkgewqs9LQQ3RtS8fFW9xvM4uMqOebc7RZCnHT/aim0Zgd5Zxywq0vdH5yyDqvO4aTDmnNpahRQa7fSu1i9E4A0sQHzPFU+f5hNiyCzLkI6zXuEkeT3fjdXMNNZyY5Cf0PDmfTgGRTKXUZ1bC9Kp1flEflL7jSW48niTNbgF25L7eZecsgwdHZrSuhMhZNhhBey4EQLmJo17GizZp23xt01N91/pq6O0MTjhvMU5sD0veqCBhnYNKXzv7yyKf99o5HmN6ShyuM3ei9paSO+nIn3GjmVSy4ohaTy/Hhj0ttnE0rmcsm6Zu4I6OAJ7tyd1Zw9Y5erz4HTW3OWBG6FrAKoKoDf+80jPf3B5ispRdLWJUUiINr2OEKKN0lAOk68/2JO5fZqNRsiRqkbdHdBHzDievZ/V5T/TuOFt1xTbq7GNkn9tV2Ytsf+4iSipgE98UKnUOzsfI2OgiszgsDmzttbAYzbnfuyx+UJecwcHh2dpdljGz4DpeHE9X5IXXJ+jkAo/ry3B9aOnI4UGaZqwbam1Kos41oSjW7R0iWeeTJHTX8PzE6vONBsgt5Rdrn+iWo9gfd/RC6C8TUrhQNnFZX9CjMlUq2nQND1tcI3j+NfYjvNq7p45NxkJUrpxKBdfpapVd16Q1ISJ3jLJwmq+z8DxBAxNc4TBr0r5Mnada5VPni30IuLGdpTyj5ixtbdhtscf33na0Ca6wfUqouhUC37vWAX7oRiuU3+eCtpJoAjZeM2RsRxSO7VihHNQUU1+lA+AEHfCmJZMXiWQFDBFoY1+uCQG9TKSjBVZzQeN5/uefn56fbr8tPb1yY457fhouNh/Xk//iKiu8xsWXxz4Sp+jnp/+7m5j7rcjbDxG3i0Lg+K836a9/qdOvz0+VF0P597uuOmnDx13LH6+SPv3hOmug7u+/cw0/h3TN2y1t44S327U3KuC33v1+EK4Nv2wNl4jPT8ONUDvc671dHT5uu6F4Yrjufvr9vwGwTpuVGCMAAA== -->
