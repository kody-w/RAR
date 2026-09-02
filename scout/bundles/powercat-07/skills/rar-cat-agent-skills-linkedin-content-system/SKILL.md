---
name: "rar-cat-agent-skills-linkedin-content-system"
description: "Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/linkedin_content_system", "rar_sha256": "cd5a44eb81ec76324921f288cf231f95096b3a9c67f5a5269038dc5b748eb744", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "linkedin_content_system_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/linkedin-content-system:5247ea83113ac0204c8f6ff542cdcc5cd686b0de712b57fde83879c8895a742f", "kind": "skill"}, "version": "1.1.0", "author": "Simon Owen", "tags": ["linkedin", "social_media", "writing", "marketing", "content"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/linkedin_content_system`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `linkedin_content_system_agent.py` is
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

LinkedIn Content System — Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#linkedin-content-system
  Upstream author: Simon Owen
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `linkedin_content_system_agent.py` and embedded as the fenced Python below (sha256 cd5a44eb81ec7632…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `linkedin_content_system_agent.py` first:

```bash
python3 linkedin_content_system_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 linkedin_content_system_agent.py   # or on stdin
python3 linkedin_content_system_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
LinkedIn Content System — Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#linkedin-content-system
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/linkedin_content_system',
    "version": '1.1.0',
    "display_name": 'LinkedIn Content System',
    "description": 'Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts.',
    "author": 'Simon Owen',
    "tags": ['linkedin', 'social_media', 'writing', 'marketing', 'content'],
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
        "upstream_slug": 'linkedin-content-system',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#linkedin-content-system',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '207c56909d447f78',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class LinkedinContentSystem(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LinkedinContentSystem'
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
    print(LinkedinContentSystem().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71ZaZObSJr+K2zNB7uHcgkQIKiJiVjQiUAgARKS2h02R3LfhxB4+79vIqnK9mz3zGzExqoiJI587+N5M+vbk9nUflY+vT5pQZKliNKC9On5yQGVXQZ5HWQpfDUtgVkDBFwCB6Q2+BQDB5GCNAKOkCJ5VtXVM5KXWZLB3xS0VQzqGpRIkNbl8MhMHSTOUu+Tm5UJYmd5h7hwNVI1eR4HkJdr2nWFZCXilKZbVy9QAXA1kzwG1dPrr789PwXw+un125MdmxV89HQXHqTTLK1BWmtdVYMEUsVm6sHXeQdtGszIQTnIhI8c4CKPu48ViN1n5K9/jVqz9KpfXj+nyOPz+Wn4U5sUqX2A1JkJ+TqIbeamFcRB3b0gXNyaXYWUoG7KtEJMpKrLIPVe7pTfOWU58vfh3ce7kBcP1B8/P2VQBXNw6uenXwZ7Pz+VzXD9MnDJP/7yEmctKD/+8p1P1VghsOuBGdT65cvj/sEWLvy+NHBvUv8Oud7DZ4HPTz8YN3zueg92QsqnlzAL0o93xjB+F5CaMLwff/kztrYP7CgOqvrf4vvrnbEPTAfa9FD8l+ebk39D0IdB7zz/XGwOw/q/sQQufxP3jDwc9We8b/7/B9ZxkILq3eN/yO6PCNC/I7/+qW3/jOAZcT8/zUAcXGB2WDF4Rb590bbz6a8fnO8PP/z2O2T9L9loWVPaNw5fEjMNXFDVX778+qG6Pf7w268fmhzmGjCTL00Z/xHPP/LrTc5PHnys+vgzLZS/T6M0a1PkPdORb1n+H+XvL8jBjAPn+/PqFfmxXoYPigxGvAm9u+CHmqmgrj/48Zen32FjSKE1jX17Dav8L39BNoENm07m1ohmZ02NwADXQQIG5XU/qBD9UdRfNVGQpJfE+YrAp0O5wxZhNnGNLEsziId+NkR8sCBzka//aZv1J9ODzeZTFQVxXI3iRw/6Yt+b0Jfq1oW+viC6D8VlZeAFqRkjKrfdIjfKQdAtJaom+XQZZEE9gnuvUafC0GeqJgZ/Q77+Ce8vNzYveTfo/DmFQTBhZBwEvsqz0iyDuEPMoSlZXQ0+wRYKG0eZxbFl2hEyfDX5y+AIwwfpwz22mSLgCuwG9vc4s6G+bgDb7jOMcJXFF9gEB6fdTEacoIQeycru1tGhY18HZl+/frXMyv+c3rvuGLkjRzWCC94VRj59ykvgxoHn159TYPsZ8uHb7x+Q/0L+GdWN+SBjC9v+zU0wc2NkrSkyAsuwSeCyChlyAPaYW5i+/X73/6BdCiEIFk/gBuBGDLl9j/lgwT0obxG5YRhwQfmQ9LPfkNaHfkGCGnorGADvczqwyODSsg0q8ObEO/Hd9W8hvssZYlI9fBg/EHBYe0u3IZh2VjoviOAi756C5sK41kNEfYiyMENzkA4Q3EFKs/4ewjSrkQoWSeV2z0hTQVMHzl8tyDq9JY4Nl39FNtMtBLUshl+Dg27iIXWWBkPgHzl6fwyZlB9gjvFvLF4QGUBvIrlZmrlfmhW4rRuge8gICGZv9JC5OYwByIDaYIjRrXxvmfc+NTyQG7lDN/K5ITCcRP6/B41BJW65VOdLTp/PkLmsq6d7/jwKD7mPRxD6EcjzXgzfx4G3zvHWUz+ncQB9XnZ/u690bylzX3PvU00JtVA59cZ/KN7yxjeoYeCHSJblkKzm5/SteUOjhiSuhj4E6zMaqj17Fzi8fdPUh0U43H8HcuSeU4NbYLYieWPFgY24ADi3xK79ciibh+thFoChhGCe2/5PViGQO4ww5I9AJYLBge09mjJMfzj83J38vjwYxiOohdPYUFtYH+AFMYZ0hSlXIRaAM86wBnrhw40VkgDoY6jiu4cr38zvymRl9Kag+YjFj/5/vIKJN2DEEOC3qoI8TcesoSdbGAJYNNd7XN+1fEQKqpoMGX4j+jnYD0uRHzHmb0NlQQ2/93Mzjgd4/sE1sB2XSXVPRpi7FazdBDzSB+bBDYlf7mB6R+t3XV6RKacj3I23dkMZ5GPyhmc36Nv/HJNXxK/rvHodjd6XvXhB7TfWS5CN/gdk/eUNVz49kubTHVd+4nx3wivyfT/w0+tHMr4i2Av+gg2vpMAeivUNl1+RJn20XQf5+MP1I1i3YABnKOChn8BUGfKy8oFzmzBU8D2aUJUsgc1jcHIHG+g7SLwtgUjhlcAbFt9BoxqwpoXwduN9a/rvEX9UA2yFqTcgXJX9UKVDtIb43cPz3lPhq3To1s4whnlg2JnEg7kVeHpNmzh+fkrNBPyTHcnQLmEuQqcN+xdYFXCaqQNwuzMbJxg8N1z/vOFSbhdmPBRONoCeUw3Q8/DgTWunhCoNleZBOALlMwI19Wr/Zkg7VNuA7BY0rILYBpxB87rLB1XvO5Zhenofrf6nBreChZ3GyV6HuoVtF47Bz8j7RPuMvO0xbru1tIGbrF+HaXqwGS6FP+9r3/eTFnj67Q/UeAzXf67Eo5ncG7xpDaA3mPgHNkFuJSgaCLLOoM93A7/Lze7Cfr/pWd+3h9+e3vrFcH1H/HtCQYJ/NYwNpr6B6JeBnzlQ3UruZvltqvxiwrAP8PPDK29A/i/3tHx6hT0GPD9BYlgvcFTub3vfp7sSUPvv8yjkALvFp2oA/xGsQcgJQnI+aB7B4vpBwPA4cG7rh4vXPx9i/6EhvFIEOQEmM8bxsWljBEbajEu7LkUStmPblO3QDG1hDpjghEVNXAcwY2bC2gzDUuaEJFwovILxT8yH8BE+OByq/e7Vf3ugfrrTQUwgKBoS2g5lkiSwGBzYE3pMkCyBuwTD2C4xxl2WwljaGpusTU9cyqQImsXGjGNT1oRkAPwiB36P2e6uzJe3OfotBvceANVIkqC+SbRMeoxjrunSNmGaEyhnPHEoKBIwAIo3xzSGMUMgHqSPOAxhuts7JCYc6+BQdRnkfHvEdUg2moQrV2QlcPfPdMQezpYxCq/+Cu1j9HrWKUFLelqKAkuN7aN9JiasMMMm6RSVA8/eHRJVJOIwSFRCs5vpSeNGQsm0F1rf9lPKVQ+otgiiXTvh4knTV5cN03c9t/Gga5xC0WIqIXtJ1s6mQSq1r01sdbsdtZmUEVquSsUhsIuAPeSFL6kYDygJEGtx3qHdaD7ajxurKNd7tQkqeasK5ywWGOLaN9VE1iuVslW+3HO1tdgbRWtUNcmK4lgI593qkGfdlES3klQz6OiyCscj7nIdycakHqHKVWrqNj6lSdGLlkFhU31yOixpfGHNK2pepCzXu5rPH30N89mOElg7F+xxmExlmz7o+/VULMiSu87B6nKN61hK94vuVFwkTWqr1vFOpdnt2j2VgAKvpqfjvNTXBnVN90EyX+yBJduWanaT5OBEF/d0rq14n5x03ztQ3cmPWpU8Fri2OjX4vorFawh2U7XV5DQxzlgZmZOVS6ehhWGAq/poZ7VzXubjJmUWUTmWspggbFOtA3OZ7fsILZardRMfliq6ykqNWBa9UBy0y4bF9jN2qm80pT1a62gRGlJz8M+bSO7tKrnoMAkKO02YvS7YpHZuhfVMOXV7zdjU4YyKk2CSt+4STRizmwWz7DzWm2iCo81qbFPnjZSzi5KP7GhDnGs0LQ49nPQxllfWlzM+joTDtCaU04QyNwu3Ysp5dznpgleOak/Y+OC4QEdz/qigTb3IzeqA5YQyty2yOdOz0ZllJHsyrztGUnqGNIskCDuCwINURRfVpYvFPVPbfTkRlH2FndO8p+Z6gKfGGVxhrTblZaegZQ8KupvQnnyRcvie3qTGFvqa0vT2MtqoZ4NXCyYvadPp0Z3vZAtRnKfXlBNnXM03B12Q4GRQOBofdSvQ4Uv97OGe4wuELEX55JBvKso4h7hgCjHd+eF5dkBpvEuXqyhbLbvZKCbFiSLvwqQFmq13+220QW2tmUkSE69P0nIfhxGJEcuxV/hcLMZeQ1+vtlQZVMOxAsnOlgapbhUe+NH+6M9W5JIkd6kVErpCHg8dcFYTWFWVqwNjll/07XVpERcTpbTqqLPbeopr4BAaIc/k6Y6g7Nrqy+3EvVo7o2X2B83hl4cSN7psvOguRlRXYaTOr9Uqac5S6pJSk05WUbLmoo3rsJJdbAtJZqmIPKd8vyz0pN04FBDi0h5Rl3y9l3IzPgTqerqJ+lHTH0O3QLHIOud23mhnanFi1tOzsWsOyzW9SimlDClLM+twMUb99QjnLstEtDQNLVXCMgUVoBoezMJFNvXkki2beciu09VGEbQNW/E42YKC7ZPZWbVhIoq2cLl4i7I4bFc2fsxlcRHE09m4q/yVuLNJf+WoNN5ra34JLr1yUJL0uNriGsauo6WU6CdGoJeCi5ukhm2CWB0VpYgbB50grjlG5LOUp3OzkCej/DLbjjycH2sdG0WpSUVZbqxzYk/Vptr6hnwus1Xr79ka12doFMjHld7T8mgUpD1FMXHad53plvpoVC31yX6+j+pZa4S50OGnCcHEon/VFsfrzq+ttDLzWqTG7oHJbXpm+LG4w/slVXh93Nh0pi883GGX63E/xp3zTnLaU6Dhl0AKlYnaztdAjRaHst0XZtcB5UIJqgPrhprmdMAcCONALzqb3M3Ho5l8XQDnsDxT5FoRVWxMW/lYm9ec3yfHWJnM1IKfEppRrE47FVwj78zGbJ875hnoIj0eKiFYEAwLUo0QLlLkK8sgwl09LadMvLqCXTDl1n3aC3yZNewm1QWfFSeCrqWomjGkvlvjC7oJFluGU+fZYSdr0mVTaBRjeny/SSkSJ9pJu/b3Wn09ivkG3svSvjjastRtRJ2/WBsjLmnhLAqiPJ1Ab19PJabyHI5NPeG4M/aN5B6TRbqX27XWFygz66F+o9E4gJMzG/B7b7fknYqveJcnLWG/pj0FjTw0N3iiZ0fT83ZWuJPN2IqxKo4uS2J7WjPcZK54GcQw05t3mRw5rX5qlx2vXwPfEG0wG2lLbbs5EQcFy4wFzYIjtbaOTDAz8gZo4Z6X0xT1s7EQlHMnEviWladiuJ+dFg2ERe90KrtkxSsLeSXO1qUU9/x6slijtVfoc6pPuhV53ocza6H7psGtqHNFaOaBPTT+XggVsaPKmZgtxot4Nt3z2JnbYTW9myqZomcx3umatjzIpkr6llXwJd+ePKXLjFWwL2DizGRRD3l93/BJ0RQThemmxWV5qhfYnPMWB66MXRBtGh+Yy5MiG1NqYW9BJfgULLV4v8GTFuc5nVowhiHvuI3atYGghosoX+TppqY3rM2dNMyuUGBjmUqfsBOq7fs2cvrxJBbm6mwtxLZ5kBJe3hcExSVzkcn1rumSguAU3J8bNIF6XSNsd0xjC8Z2WYyMaVT2kyTsuFURnqYXDqsNvva9eWTsCeBt+XRdcMpoY9bGdH2pLc/PtZkp7ENXXF3cKXGYnrLzau+48+uhpMOl2ogc55uB4IZnKoo27DQIVk6zDJLy7HS5Zi3lvRNuuOKYz62xsZsuHSFxlMUWlYUi8nUPiMYuFwNWj1U4V3B6iomztujodby9FLbYcduk4dbrgBEkIsOPG1IwDG1dzVajjp7ljgI26IKujNGu8HmHzspi3Vc6VUqb1fmgX7KLMhX9kVROCYcOF+IsWozVep6fVbeXm6jdqIQRLOtQ4goSL0IzwzmVbY2zgfu8mR8LqZY9hZyONK2eW7t1NHH01SyaNlnqlqdI6fdU2Bq6cSZhmmdckF7FILGKeVbPKiCP00XGY9qecldgZW3X+ZqO1yjRGpq4qfV+gk1XZe2t51upZFl+ylxzsdh7pSgnmmloOymrxXUsN8GcyNNye2ApVtmupr3j6HKjUHK1UQP9Mk1zEgt3G7zN/MNpQ/A9FpLNoqhFGVfiYAwwfKmes3nYGz2K02XRgc5v5LU7jtrj2EgvzQUlE5GseqeY6WcCz6xJs27zw1S3ODSUlcveTGKncxKVtKOWl2lxHyckSqtwNMHSlJLRQpMtGdsexDKTYbGgembSkabTaUJzeudtGWtXooEZSltLPhrWceLs8EAVp0Q0Y4q+UBbuSQ9b0juOth2EmP60XM6ySTVR/P4ciRS/PePzy2iBY2wlU4s0wFDoiC3KHbvpvp5yCVlOUGmM0R2gHRJdFf21UwMFi7fFll+uTA+OqfI2wCMPX6T8Dltlqu+i/HIH/HYrgO6iB162TGdnvJ8qO51ZdGqMRbOlraKWcurT0mLlsk55lCKmHhZtuprPlNVFgyXnSDXrippD6qERddNG3Wtnf4yu7ctia283NLZSj2GLLbrraHZy07KS6TnuttfdJkglm3W4Q9CuVuNCNK5nmd/11RE/VT098fhjsezIhBvJqqGnFC1dMWsV06vOOYBizJ5YXaCExdHxNyc1aYW0atH9hlyypYId3Y0qGvFksldP10V2OtTXc2iibEyBFX85YM6+YbbdNAwLpSrQrYLuwxUva94Cpceu3Ao6qeFovQtWdXad0wFBjLcnf85UF1zenqZ8u/Nkht1sI8tLUSWlzEqAc+esETdzJpjjrDjjRdWIdL2vxN1VQbdjwwDzziEZgcJqCY5q1XRFTQ6o7h6iznbd63URuTWHH4t4uWPHPmzA0nxPwt2DwW3W5UpHzZO84Pxq3x4WIWpF0qE3gHCY9axz9FSMCLcTfGxbcngdW4dTsL2ciD5t8nUQznggWTFHOGS+KjbhfCoyKHbhj+7pEtrcmJbL9DI511i2ww+pktbeZjo7Fr3MVydTuUyPO2rEX9MDSViTA2k2HADK1Wm6pa0sPGKiOae8klN7SUjjdZlczqBcsgspUhyj4xqVBexuyRgqIzJSNPONcSmrgJWMDFO5s7bFjoDqi5McsVGFruO5olsHbWSjvrokFHQOmNNsZxVslLmhWl/ISb5K+vJYr9CaYlmtCjYnb+teD1292mdg718UdiwJqwuG5rrbKa2oL1gM2OdZVFYBqE7h3hldSHdEigFjMmkl16MFaC5CPF2Fkrw7qp4IQWZmHPUtGY8Tf786gA1f0JQxEaaXYLSYtGbCGbwWbQsUVZYrtcXgGNzC3TzWORFLRmASt9B5hkSSZFjhy8u1WKTxNeQ29FIufQ5C/cJfz02LTHu55zGO2uAuQfC5g19QPJGu+PgYsZXY7zlpZgRoZ/UAZCenKVtrrTrYVUbDmoE9iD+T3MQn95J+2py2Ah12U/SQ7GcKlLRhOpsPLasiaA3ugvCVVEwnl1YPS0a4EGQ5r0fy2NJ47Xg9VlQzcwuGWNR2E9GG2h0b+ziR7JBRJlbHy7Jv29dmU2SNbmsiOulJr13CccfZOI6AQkZ8DxKCIxnegA0TczJp52mmFAVZJW8scxtIsayf7SZxrglj5OjmKJdKpjfKcmTFEnROu4LdxPO0qdBy3NPz0+3/Vk+vLMZiz0/DWenjxPPfOBbz+iD/8qAf4wz9/PR/d4pzP1F5+1fH7fARmM7rTfrrv9Ttt+en0g6gHvfzsypuvMd5zT8eS336kyOygerO9Pb8Wr8dCNemdzu5e6O7nQrZgRl/SeCtCW/bMqiH08rhtK+MwOP6wX5Q7XHGflNvUPD3/wacVsPApyMAAA== -->
