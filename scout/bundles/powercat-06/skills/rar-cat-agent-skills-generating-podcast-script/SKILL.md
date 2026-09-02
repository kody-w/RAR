---
name: "rar-cat-agent-skills-generating-podcast-script"
description: "Turn a topic or a pile of source material \u2014 a newsletter, news digest, or set of articles \u2014 into a two-host, NotebookLM-style podcast episode, with multi-voice SSML and optional Azure Text-to-Speech audio."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/generating_podcast_script", "rar_sha256": "38267f60dffe6f5f867e473ee794685bb89ea2833f4716dfd9ea9431b3bef325", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "generating_podcast_script_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/generating-podcast-script:b2fcf094bee2a0b1efd07368f781da71c3fc859007958663b93967147c7adee5", "kind": "skill"}, "version": "2.1.0", "author": "Remi Dyon", "tags": ["content", "podcast", "audio", "text_to_speech", "ssml", "news"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/generating_podcast_script`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `generating_podcast_script_agent.py` is
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

Podcast Script Generator — Turn a topic or a pile of source material — a newsletter, news digest, or set of articles — into a two-host, NotebookLM-style podcast episode, with multi-voice SSML and optional Azure Text-to-Speech audio.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#generating-podcast-script
  Upstream author: Remi Dyon
  Upstream version: 1.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `generating_podcast_script_agent.py` and embedded as the fenced Python below (sha256 38267f60dffe6f5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `generating_podcast_script_agent.py` first:

```bash
python3 generating_podcast_script_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 generating_podcast_script_agent.py   # or on stdin
python3 generating_podcast_script_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Podcast Script Generator — Turn a topic or a pile of source material — a newsletter, news digest, or set of articles — into a two-host, NotebookLM-style podcast episode, with multi-voice SSML and optional Azure Text-to-Speech audio.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#generating-podcast-script
  Upstream author: Remi Dyon
  Upstream version: 1.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/generating_podcast_script',
    "version": '2.1.0',
    "display_name": 'Podcast Script Generator',
    "description": 'Turn a topic or a pile of source material — a newsletter, news digest, or set of articles — into a two-host, NotebookLM-style podcast episode, with multi-voice SSML and optional Azure Text-to-Speech audio.',
    "author": 'Remi Dyon',
    "tags": ['content', 'podcast', 'audio', 'text_to_speech', 'ssml', 'news'],
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
        "upstream_slug": 'generating-podcast-script',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#generating-podcast-script',
        "upstream_version": '1.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b619697cd53a907a',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.667, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class GeneratingPodcastScript(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GeneratingPodcastScript'
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
    print(GeneratingPodcastScript().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
