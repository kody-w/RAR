---
name: "rar-cat-agent-skills-wikipedia-human-style-writing"
description: "Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/wikipedia_human_style_writing", "rar_sha256": "1f50f40dc28b1760c266836dc179d8cb5be8ca2151a339e00fe612af9c163131", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "wikipedia_human_style_writing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/wikipedia-human-style-writing:5d71d6040d021b19bd253245a9044830ebf2a2551fd460e799a9384dc3a8dff8", "kind": "skill"}, "version": "1.1.0", "author": "Chris Garty", "tags": ["writing", "content", "editing", "style", "humanize", "ai_detection", "wikipedia"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/wikipedia_human_style_writing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `wikipedia_human_style_writing_agent.py` is
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

Wikipedia Human Style Writing — Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#wikipedia-human-style-writing
  Upstream author: Chris Garty
  Upstream version: 0.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wikipedia_human_style_writing_agent.py` and embedded as the fenced Python below (sha256 1f50f40dc28b1760…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wikipedia_human_style_writing_agent.py` first:

```bash
python3 wikipedia_human_style_writing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wikipedia_human_style_writing_agent.py   # or on stdin
python3 wikipedia_human_style_writing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Wikipedia Human Style Writing — Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#wikipedia-human-style-writing
  Upstream author: Chris Garty
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/wikipedia_human_style_writing',
    "version": '1.1.0',
    "display_name": 'Wikipedia Human Style Writing',
    "description": "Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide.",
    "author": 'Chris Garty',
    "tags": ['writing', 'content', 'editing', 'style', 'humanize', 'ai_detection', 'wikipedia'],
    "category": 'general',
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
        "upstream_slug": 'wikipedia-human-style-writing',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#wikipedia-human-style-writing',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4a55ea6837b037ca',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing', 'word:draft'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class WikipediaHumanStyleWriting(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WikipediaHumanStyleWriting'
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
    print(WikipediaHumanStyleWriting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V5aZOjxpruX2HqfOj2qLrYBaoTjrjaAAESEkJI4HZ0Jzti34V8/d9vIqmq2nNsz5mIibhURAlB5pvv+jxvpn57Ak0dZOXT69M8KMMK4UFZ90/PT45b2WWY12GWwneq25Vh7SJZiTgl8GokL7PKRaoMCWsEtFnoVEgduEjtxvGXGsTwVeinFZJ5yHSFDHPD1H9Gmgp+IMcwCnPXCcGnCvm0/9dxnxAvdGMH8ZvQcV+gLu4FJHnsVk+vv/z6/BTC+6fX357sGFTw0dO7OKFJQLqv+9g93gXBqTGAH69PeQ+NTOH33C29rEzgI8f1kMe3z5Ube8/If/5n1IHSr356/Zoij+vr0/CnNundvAxUtesgNsiBFcZh3b8g07gDfYWUbt2U0BKAVHUJ1365z/yQlOXIz8O7z/dFXny3/vz1KYMqgMHJX59+Grz79alshvuXQUr++aeXOOvc8vNPH3Kqxjq7dj0Ig1q/fHt8f4iFAz+Ght5t1Z+h1Hs4Lffr0w/GDddd78FOOPPp5ZyF6ee7YBji1k1Baruff/orsXbg2lEcVvW/JfeXu+DABQ606aH4T883J/+KjB4Gvcv862VzGNb/iSVw+Ntyz8jDUX8l++b//yI6DlO3evf4n4r7swmjn5Ff/tK2v5vwjHhfnxZuHLYwO6zYfUV++7bfLue/fHI+Hn769Xco+r8Vs8+a0r5J+AbLI/Tcqv727ZdP1e3xp19/+dTkMNdckHxryvjPZP6ZX2/r/MGDj1Gf/zgXrn9IozTrUuQ905Hfsvw/yt9fEB3EofPxvHpFfqyX4RohgxFvi95d8EPNVFDXH/z409PvEB1SaE1j317DKv/HP5B1aEOwyiBo7e2sqREY4DpM3EF5LYCIpz2K+vteWsnyS+J8R8I7mkGIAE1cI3wJwniAvCHigwUQrr7/HxvUX4DvpvWXKgrjuEK7NyD6FgxI9K0aoOjbA9S+vyBaABfNytAPUxAj6nS7RW7zh+VuiVE1yZd2WBFqE94RR52vBrSpmtj9J/L9b1f4dhP2kveD/l9TGBAAo+RATE7yrARlGPcIGADK6mv3C8RUCCJlFscWsCNk+NfkL4NTjoGbPlxlgxRxL67dQOiPMxtq7YUQh59htKssbiEgDg68mY84YQm9k5VwkdQZnPw6CPv+/bsFquBrekdgErmzSoXCAe8KI1++5KXrxaEf1F9T1w4y5NNvv39C/i/yd7Nuwoc1tpAHbs6CWRwj4l7ZILAkmwQOq5AhHyDe3EL22+/3KAzapW6JwEIKIdXcJkNpH/EfLLiH5i0u0OZBRbd8rPRHvyFdAP0ycKF7gcVdPX9NBxEZHFp2ISTKhxPvk++ufwv0fZ0hJtXDhzBOXpklt7G31BuCaWel84KsPOTdU9BcGNd6iGiQVTXM1txNHTe1ezgT1B8hTLMaqWDBVF4/UDA0dZD83YKiB+ckEJVA/R1Zz7eQ4LIY/hscdFsezs7ScAj8I1Pvj6GQ8hPMsdmbiBdk40JvIjkoQR6UoHJv4zxwzwhIbG/zoXCApG6HDDTuDjG6lfI9897SG7lROXLjcuRB5sjXhsBwCvn/2IoMOk55Xl3yU225QJYbTTXuCWVnaT3Yd2+mYF+AwL7iXh0fvcIbrLwB7tc0DmEQyv6f95HeLYfuY+4g1pQwQdSpepM/VHN5kxvWMBOG0JblkL3ga/qG7M/QuTAO1QBSsGCjofyz9wWHt2+aBrAqh+8fLI/ck2xIfpi+SN5YcWgjnus6t0yvg3Koo0cUYFq4g6tg4tvBH6xCoHQYcigfgUqEMD8h+t9ct4H1MDj9ltzvw8Ohd4JaOI0NtYUF474gxyF/YQ5WiOXCBmgYA73w6SYKSVzoY6jiu4erAOR3ZbIyelMQPGLxo/8fr2AmDgQCV3svMygTOKCGnuxgCGAVXe5xfdfyESmoajKk/G3SH4P9sBT5kYD+OZQa1PAD5kEcD9z9g2tgopZJdYMcyKpRBYs5cR/pM6T1QNMvd6a9U/m7Lq/IfKoh05vs/Y2CkM/JG9ndePHwx5i8IkFd59Urir4Pe/HDOmislzBD/4XP/vFON19udPPlRjdfHqXxB/l3V0CFPvYQf3j/yMlXBHvBX7DhlRza7pB0j+sVadIHHDvI5x/uHzG7xcR1niF0DDgDM2ZIzypwnVsXorofQYW6ZAkElcHXPQTWd/J4GwIZxC9dfxh8J5Nq4KAO0t5N9o0M3gP/KAoIkak/MB/EmY9iHYI2hPEepXesha/SAcWdoVXzb1uYeDC3cp9e0yaOn59SkLj/3dZlwFKYl9Bzw24HVghse+rQvX0DjRMO7hvu/7hTU243IB6KKBsYEcIhBMaHG2+qOyXUa6g6H3KVWz4jUF2/Dm7WdEPlDbRvQesqSHyuM6hf9/mg731rM7RZ7z3Yv2pwK16IOk72OtQwJE7YLz8j763vM/K2Gbnt7dIG7sZ+GdruwWY4FH68j33fiFru069/osajC/9rJR7A8nyndGtgxMHEP7EJSivdooEM7Az6fBj4sW52X+z3m571fR/529Mbdgz393bgnlVwwr/Xrw0Gv/Hst0EqGObeivBm/60J/QZrKhz49IdX/tAcfLtn6NMrRB33+QlOhqUDO+vrbb/8dFcF2vDRvkIJED++VEN/gMJyhJIga+eD/hGssx8WGB6Hzm38cPP6Nz3vn0HEK+0wuDPGKMzBCNzCJ5ZD0CRB0WCCURRLYq7lEYCgadxzqDHmMpMJmJAs5dgkYB3PY6EKFcyFBDxUQPHB+VD5dw//D7vwp/tsyBgEPYbTcY/GPKieTbAWzowxmxiPWXLs2DgzcVjboi2XtQGB0zggyYmLYZ47xgngTWx8TOIkPsh7tIJ3lb69td1v8bhDwzc7S5JwUNiGbAqnYh7wxjYBAEPiHsk4NGt7LutOCLjQGMPYISiPqY+YDCG7Wz2kKuwCYQ/WDuv89ojxkH5jCo4UqGo1vV9zdKKbKEGd64sw8ujRnPS6QDKFk4OlGicX41Bo6ObS704+Q9SGN1+qahHTK6MkDZKW6BjX5ruA9TU6SsdXc8EcGEmrp6HEr4xattPAVoCVHEeUofo8gx5xOd6HuRf2RJWvT6LF6KuUVHN7fKQaz2sD9ST5ThsmKk8vjWafc8ZJKoM1wcnZke1PeqhasZrFau7GolTK5jjVE7VkNRow3DUqQFiF+4440tHFPff2hl6VsiotGb5xJClcLQJ0ApP/Atqr049GyznqtnJL6b3mGqCirlihG55bkIpqNDO7BJzT1LPjRVbUfY6qa4Uhii43+f5I7MbFUTVbdK3plxwoRWosV3pM62po+VRLLC6HxJMqLnDURsTntsAD/sgt+GnS6hKRTrPcyvcXpZosk8o7HTkyuZ4M7Ng0dHQyFyTB0zx9EmXOmhcLnwzNmblsZnR9uOAyZ0rioTJP2DrdL8/GKE5cSZNVq9ieNZdlp7m8SZOdLEkzGd3U8XqTWILiLgrdTkgGaLYunSthsr84s2tG9dJl22zk1TGnVkq8b9fO1RYuan9ZWTO9Srr9xnBxnovGGsn1V1DLVkvUV7ekj2sRq6odUe4W+SJZXiLJWDuWSMXj2qIrR1CaziishKNoej+yUZKuNhk9xwB57eSjJjHipbkyG1GXG/mIz/BZXufW+rwgetBXxEg36Xo256XLWruu9hS9Gm1W5+0F3faOwntiPLHHGsAMizysacUt7Uym0VHAGHuDMPXUINw4X/c1LCNRk/eKk7Kg3/LLWuuvstLivs56s96w5kyl7gmRhKaHkoODqRI0iyUz3uf1hQyu5MhsRHGyUMd+zreO1K1OKJ2KRba2r/tQCoTzNXF6Tqjnoq6oktal3myqMAcjjvo5dZAwLzvsRzE4JNMRytnhpLIEVSXqzbiPpAbHICN40nxBFGfDR9dSaJu1T4ET2UaXS2OW5tE5hGI+pVe2CuhrmnFC1XdtpM/2/Vo7hgagNlp3XKUHLsQOTpg1nDLbkFMTo+rtkpemebo673tJvDoawdu2UvJrJtb5GT7xmrl+CSPZqYp5aknZmt54TIgry3y8v7ptGlomJ7WufGz7c2jpZi52cWovOpQOCjCqqHaznClZWOJ7MiYSOQO1ZqirC3sulC0hXUZ9AWAoLyJ6REfy9hAewCmkpFN7tnDBZtjZSZKPjZNqqE9bwIK4SR+jhbzO6r2M75r98bxAGRsoo5JRVafge34iXsg8pA7rGc2FGxpDt51NydxYF4GgNVWQMsVsJNYRzZ5ZgKHEXIZok9Iy6LhWLOdAmjMp5TtZzl7IZpnLBExCY0aWk9DYFGHXsZGYzXJvx2iHwlTocqHaftvrqyUj93MF+J0gKdSO2V4Ps2DktZp0TBgztNrJFNvMitATdlRlWNVaOTiJXpgxb42KRDtx+tayeEEDEbEXImKp4t5o0+csqzTk2IaQiY1tdrw/RMUlTphDPrHDpQqDlewnMWRzZVwpsrrFVa8t8ihFx2zverI5Ydk4qlp7wfA5flibXLiHlVtqOD87FCK5Oh8knC4MttEU8XSMLaaViBOhzxJ13K5ByrbSYS7sErvq15RzQJXxiis0Kbt0GUaDqGevTbSuF0Jkhlwx4aSiqsg0oMNVbW/XrJzuxfOJNvUs3VxC31tzGMOZ5uVkamdcXRtaOcESjYhksOPo5BSLzCIrVnNMPfaZ6AHV2GdKpGIMbo7NvebPO5HR8z3XsyyMJLFqtThW+EM08TSynI/iZdj4o/lUFFN5NTXP0iRLzV0wka2Vtk9HasZS5lTE+XETcgIrdFimK5uz3K6LPcdC0pPXEU3hRAf62a4Qj0YJ7T4YJo83etlMY1XZY8aB0JyQmWDifmUWiwSz0EV3ygLxrK2lzrf9KrePRZnLx8iyF1yq45WuHnI2nlwxtII8QlPEtK/8SFpIS8FdymRezAwNGykStuuKk9tfJ+gi305ClzmQVtw1cdTy2PYoraegU3cw8b162wHVmx+Ps9FyYfi1fWnKWNzO0GAmCsnaNM6YxOVOe7p2aXOe72dtQpIzpwiU4BoYbMmHeqz08tQeiKoiWcIE1baT+JnEZpdoF5z1/pzxHQUBW5GO4SILCjWduSsvOO9xrbnExjFGi3mlepK9mehEeNid+Q2wjTJKlwIXL6aH2XW/jHMZSzhnV6ezlcbbU7s3Vnk53/px2F72sRJn6No3RhzkZzHUFnvhmgaQSTsxbexTPh+FfT5a4wfJi/xkOW3Cns3pwyw/rIMjWdQVNgZ1UOrnZdvL6bJ34mo8TzPJWLWg6ySjiqJO5938KOn96WId/U26ms0nTKG0iSqIMVccUmVFZy5plt1lzi09CH6HxATWSq8ToPkynrR7TJRaExSNvSF6HJ2Om9VWsCfsVBfOp9FxWdlJ7AgZ2a43XUFMc9xhkkScGn4Vdry6C63UgGxx1UosYGginHFdyl6Nq3A5SFxBmXsUL+1RtY64ImPJHIyhH9RDumzspd6HypGfCuIiUvborE9nkVKMXGJHxz0D3HFwSKlO9CJ94yU7ScGmmsTO2QlQT8XCCFl9F1t6PlvANodkCm7eYNuw6bdTpod93k6m6k7mDbyYGkA9XEuwDJSKcDfoeDyLWIFZKIFb8/500duptVqzYcDEdMZOhLmOoZR8CW2lHRddjdptZx5ZehUlk47eMBjTzNa0yid4rJeryTHdHlxfbFm5K0CH1dNyslwex2N35zFRRG3mc69pxNgXpk0hl7QqahXO76YLsdza7W5BZeKc3WPZMq2Ute+kF4UEdbc97gV5zKjHK70S1UOV4tW80/SgrVI3U6+W5WRaTGDutWuxLV/E8wUwCnO2SZLpusfzZIqNs0ZOpFjQhHTGdDUhWhjDW6bQxzvPiVtb2JodsbFVXR2fj9GGm/FGQmnXGtCLnCv1dqf6aLnZZa6UimSrioZDhhuCj1F3M88dq10VKON7ctjjY2rDpRYfNLBXBMJ1DRehYLNQRMIBG2kVls7GynQNcz6rTztU29MmmbEMbDlOfblqomLM2wLdHDysF5RqnYyMrkkk47D0zha3kvJiXU1D3DFrD8cDV1ntEmLu4XNndtmOlgbsk5mr77L9csSe+elyQzq45db0vF4LGBuesgu1WZgBuo7Y+ZXKLxO0m7OGpme7HTnzvIuLpsaZ1CD4TNJCWFQ6scpRgypP4IAvQUBSDfT3zuwO5HzMlcDzNV6o7EVx7s6HruyDvCNqXzxfZ5OFuNSK0AmUVbpKWZ3C4ibRCSZm1gtOLfiDyVMYv7hWubXaiCSHysWEVq+p0hd7g++5WG84r4qv9tojWL7Q2tEJ3zSiggbVgD78JBS2NDqjVjRxIk/G0Qg33Qjw0Zo398c1ucS3hDmpKU7WF8C+UlaSJXFqjuULBoQYCCNHhy38xGAZNdzJTQ1Nuq52qmf5Y88LTN5nNszkLEZZ7cFN5Fq1VI4xdJWwzmCExiPAqaR1BTOddrFFoiSTCD1P2nhFdNqyggk+OV7tOTVaxm55WPlMugodVfSSU7VjXX5BE0x28anp2cZDt83QpaByqozb2hifcnvMlmjfrBlJmHqzY67BJBRmfkp5tWFSiXBOFUNZjQ41d6LiJFxx5InQvFPU27an4kK0jefEKcmTS00k0YWWlyqlmn69o/KjInR9B6TFwpv6Ol6y1kE4XXhnpW9RttiuRjnteicF0CmzPTf76sqdXLi24Myva2xNo+tGEmvm0m0Kk5enBctiqHDy0dm82TlsAjfpeNaP8czorm0Qr9nt7mTQyqwyDAVVTgeTmXWcRrcQli+czVesfrbOkULb8qwiBdjzG6LSTepTo+kbF0ePdS+lmc3US8k9Fxdml7DL81pitYMQzCwWzdBDzRjhfEqdhbFce2YzW/bJbocu+1DI07ImK7aD+yWGnC63vmAyltEshP5atnQBNnYz3ozDbVm0nmJEs23b6b0t7DPXCNqDisu0V3V6bXqVcpWduYCBA6ixthk3vrnBnElLeSh1aedgfm4BE25w2GzsJGm6oS+aPzXYXAd1c7r2TAe2WZN1xlXFrg7hct5sIp0ocjPFlhG2KMYjSRAu1EGV1ctOzpkJqUVoO2VJO5lMjuDiScLSIcgDCrt8tpF2M3JH1cp6QW3ZWjTOe2/p2o2tBIKZFGMC38BEHhMU7hLNuGLq8AiimQEii9Rc64xP04pWBPFw4jaa59Ou7ZrTyWqud8GWo7O5TXbXLCzQA88mm916bOO7hPcCgwD0xo21vT++xmMuciktLNlVS+xKcYNucGsf7k8jsN6Tq3ZMaFOyOU2dK8Q1cnu5zBkZ9vskG2yXnXK0TvzxeJqVQiiH6MhYzjM0jLXU0rbMsd/ZTBl3gjJ10hVljTBO3Imbut8fCCXZbNoLF0w002h455Kw3oWa2OQBkmUOrK1N2/qSmKPdIuhwRWX69XQ6/fnnp+en289hT68TfDJ5fhqOWh8Hpv/2gZp/DfNvDykkgVPPT/97Zz7385e3n01uh5cucF5vq7/+mxr++vxU2uGgze38rYob/3HG818PtL787RHbMLe//4g3/LBzqd9OmGvg387/PsY9fvkZzlyd97mDLPh5kxxeh1sQfnPc+nFS+Pzh8UHlxzH+Te1B8d//HwzMBqQ/JAAA -->
