---
name: "rar-cat-agent-skills-clipchamp-video"
description: "Produce a polished, narrated demo video of a live web app or Copilot Studio agent \u2014 real screen-flow footage under an AI (Ava neural) voiceover \u2014 either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/clipchamp_video", "rar_sha256": "2e87128dd2c080ab21531502b82cdfe9e1d8bb835a873d40d586a62fab55e4f8", "source_kind": "rar-agent", "source_commit": "657d2bb31e7d75b8fe4216443a5336cb035c07c9", "version": "2.0.0", "author": "Phi-Lay Nguyen", "tags": ["video", "demo", "narration", "playwright", "ffmpeg", "copilot_studio", "clipchamp", "tts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/clipchamp_video`. The original RAPP
agent is preserved byte-for-byte in `clipchamp_video_agent.py` and in the RCI capsule.

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

Clipchamp Narrated Demo Video — Produce a polished, narrated demo video of a live web app or Copilot Studio agent — real screen-flow footage under an AI (Ava neural) voiceover — either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#clipchamp-video
  Upstream author: Phi-Lay Nguyen
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `clipchamp_video_agent.py` and embedded as the fenced Python below (sha256 2e87128dd2c080ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `clipchamp_video_agent.py` first:

```bash
python3 clipchamp_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 clipchamp_video_agent.py   # or on stdin
python3 clipchamp_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clipchamp Narrated Demo Video — Produce a polished, narrated demo video of a live web app or Copilot Studio agent — real screen-flow footage under an AI (Ava neural) voiceover — either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#clipchamp-video
  Upstream author: Phi-Lay Nguyen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/clipchamp_video',
    "version": '2.0.0',
    "display_name": 'Clipchamp Narrated Demo Video',
    "description": 'Produce a polished, narrated demo video of a live web app or Copilot Studio agent — real screen-flow footage under an AI (Ava neural) voiceover — either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project.',
    "author": 'Phi-Lay Nguyen',
    "tags": ['video', 'demo', 'narration', 'playwright', 'ffmpeg', 'copilot_studio', 'clipchamp', 'tts'],
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
        "upstream_slug": 'clipchamp-video',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#clipchamp-video',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'c2e348b1022ad7a1',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['word:produce'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ClipchampVideo(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ClipchampVideo'
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
    print(ClipchampVideo().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
