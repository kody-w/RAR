---
name: "rar-cat-agent-skills-booth-loop-video"
description: "Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen \u2014 rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/booth_loop_video", "rar_sha256": "a57ed23652a00cd4a470cd1e4b9ed2235169a024082d805be21ebc268a01cc6c", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "booth_loop_video_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/booth-loop-video:65003022916ac9764151495fd1f8b259a437b8a65e86dc9b3c044d7917041b2f", "kind": "skill"}, "version": "2.0.0", "author": "Al Macey", "tags": ["video", "animation", "python", "marketing", "events", "design", "ffmpeg"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/booth_loop_video`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `booth_loop_video_agent.py` is
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
