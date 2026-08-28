---
name: "rar-cat-agent-skills-booth-loop-video"
description: "Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen \u2014 rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/booth_loop_video", "rar_sha256": "a57ed23652a00cd4a470cd1e4b9ed2235169a024082d805be21ebc268a01cc6c", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "2.0.0", "author": "Al Macey", "tags": ["video", "animation", "python", "marketing", "events", "design", "ffmpeg"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/booth_loop_video`. The original RAPP
agent is preserved byte-for-byte in `booth_loop_video_agent.py` and in the RCI capsule.

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

Booth Loop Video — Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen — rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#booth-loop-video
  Upstream author: Al Macey
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `booth_loop_video_agent.py` and embedded as the fenced Python below (sha256 a57ed23652a00cd4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `booth_loop_video_agent.py` first:

```bash
python3 booth_loop_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 booth_loop_video_agent.py   # or on stdin
python3 booth_loop_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Booth Loop Video — Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen — rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#booth-loop-video
  Upstream author: Al Macey
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/booth_loop_video',
    "version": '2.0.0',
    "display_name": 'Booth Loop Video',
    "description": 'Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen — rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render.',
    "author": 'Al Macey',
    "tags": ['video', 'animation', 'python', 'marketing', 'events', 'design', 'ffmpeg'],
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
        "upstream_slug": 'booth-loop-video',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#booth-loop-video',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4be125c262ad5707',
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.667, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:design'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class BoothLoopVideo(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BoothLoopVideo'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(BoothLoopVideo().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
