---
name: "rar-cat-agent-skills-generating-podcast-script"
description: "Turn a topic or a pile of source material \u2014 a newsletter, news digest, or set of articles \u2014 into a two-host, NotebookLM-style podcast episode, with multi-voice SSML and optional Azure Text-to-Speech audio."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/generating_podcast_script", "rar_sha256": "38267f60dffe6f5f867e473ee794685bb89ea2833f4716dfd9ea9431b3bef325", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.1.0", "author": "Remi Dyon", "tags": ["content", "podcast", "audio", "text_to_speech", "ssml", "news"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/generating_podcast_script`. The original RAPP
agent is preserved byte-for-byte in `generating_podcast_script_agent.py` and in the RCI capsule.

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
